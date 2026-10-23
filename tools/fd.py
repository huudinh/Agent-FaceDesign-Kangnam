#!/usr/bin/env python3
"""fd.py — nửa tay của Agent-FaceDesign-Kangnam.

Bộ não (prompt + knowledge) chạy trên Claude / ChatGPT / Gemini. Script này làm bốn
việc mà một cuộc chat không làm chắc tay được: dựng câu lệnh từ phiếu, gọi công cụ
sửa ảnh, in nhãn bắt buộc lên ảnh, và ghép ảnh so sánh trước - sau.

    python tools/fd.py prompt  <phieu.json> [--goc 0|45|90]
    python tools/fd.py render  <phieu.json> [--goc 0,45,90] [--backend gemini|openai]
    python tools/fd.py nhan    <anh.jpg> [-o <ra.jpg>]
    python tools/fd.py ghep    <goc.jpg> <mo-phong.jpg> [-o <ra.jpg>]
    python tools/fd.py phieu   <phieu.json> [-o <ra.md>]
    python tools/fd.py gop

Khoá API đọc từ biến môi trường, KHONG commit vao repo:
    GEMINI_API_KEY   + (tuy chon) FD_GEMINI_MODEL
    OPENAI_API_KEY   + (tuy chon) FD_OPENAI_MODEL

Ten model la tham so vi doi theo thoi diem - xem doc/01-cai-dat.md §3.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NHAN = "Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế"

# Vùng mở mặc định theo dịch vụ, bản tiếng Anh cho công cụ sửa ảnh.
# Nguồn: knowledge/FD-C mục 5 · FD-D mục 4 · FD-E mục 2.
VUNG_MO_EN = {
    "Gọt hàm": "the mandibular angle outline and the lower jaw border, "
               "including the transition from jaw angle to chin",
    "Hạ gò má": "the perceived projection and contour of the cheekbone (zygomatic) "
                "region and the cheek-to-temple transition",
    "Trượt cằm": "the chin shape, length and relative projection",
    "Nâng mũi": "the nasal dorsum (bridge) line and nasal tip definition",
    "Cắt mí": "the upper eyelid crease — its visibility and curve shape",
}

KHOA_CHUNG_EN = (
    "the person's identity and facial recognisability · skin tone and texture · "
    "moles, scars and freckles · apparent age · hairstyle · clothing · background · "
    "camera angle · focal length · expression · light direction and intensity · "
    "image sharpness and grain"
)

KHOA_THEO_DICH_VU_EN = {
    "Gọt hàm": "chin shape and length · cheekbones · temples · forehead · mid-cheek",
    "Hạ gò má": "temple width · jaw width · chin · eyes · nose · lips",
    "Trượt cằm": "upper and lower lips · nose · jaw angle · cheekbones · hairline",
    "Nâng mũi": "eyes · lips · chin · forehead · cheekbones · jawline · hairline; "
                "and any nasal subregion not listed above (radix · dorsum · tip · "
                "alae · columella)",
    "Cắt mí": "palpebral fissure length · inner and outer canthal angles · eye "
              "aperture height · iris colour · eyelashes · eyebrow position and shape "
              "· lower eyelid bags · under-eye lines · nose · lips · overall face shape",
}

CAM_THEO_DICH_VU_EN = {
    "Gọt hàm": [
        "Impose a generic V-line face shape.",
        "Create hollow cheeks, a pointed chin, or a lengthened chin.",
        "Alter temple width, cheekbones, or jaw width beyond the EDIT ONLY region.",
    ],
    "Hạ gò má": [
        "Make the cheekbones disappear entirely.",
        "Create hollow cheeks or an unnatural loss of mid-face volume.",
        "Widen the temples or narrow the jaw.",
    ],
    "Trượt cằm": [
        "Create an excessively pointed or lengthened chin.",
        "Alter lips or nose in order to 'achieve' a chin proportion.",
    ],
    "Nâng mũi": [
        "Raise the dorsum to an extreme height relative to the face.",
        "Create a kinked, bent or deviated dorsal line.",
        "Create an unnaturally pointed tip.",
        "Distort the alae or make the two nostrils asymmetric.",
        "Alter lips or chin in order to 'achieve' a nose-lip-chin proportion.",
    ],
    "Cắt mí": [
        "Enlarge the eyes, or widen the aperture horizontally or vertically.",
        "Lengthen the outer canthus or change canthal tilt.",
        "Raise the eyebrows.",
        "Create an unnaturally deep crease, or a crease curve that does not suit "
        "the client's original eye shape.",
        "Force the two eyes into perfect symmetry if the original shows natural "
        "asymmetry — only improve harmony within the existing structure.",
        "Remove all skin laxity or eyelid fat.",
    ],
}

MUC_DO_EN = {"M1": "subtle", "M2": "moderate", "M3": "pronounced"}
GOC_EN = {"0": "0° frontal", "45": "45° three-quarter", "90": "90° profile"}


# ---------------------------------------------------------------- phiếu

def doc_phieu(duong_dan: str) -> dict:
    p = Path(duong_dan)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        loi(f"không thấy phiếu: {p}")
    phieu = json.loads(p.read_text(encoding="utf-8"))
    kiem_phieu(phieu)
    return phieu


def kiem_phieu(phieu: dict) -> None:
    """Cổng A ở mức script làm được. Phần còn lại là việc của người và của bộ não."""
    thieu = [k for k in ("ma_phieu", "ma_khach", "dich_vu", "muc_do", "vung_mo",
                         "anh_dau_vao", "dong_y") if k not in phieu]
    if thieu:
        loi("phiếu thiếu trường bắt buộc: " + ", ".join(thieu))

    if phieu.get("dong_y") is not True:
        loi("dong_y != true → DỪNG. Chưa có đồng ý xử lý ảnh thì không tạo ảnh "
            "(FD-03 ô A7, không có ngoại lệ).")

    if not phieu.get("dich_vu"):
        loi("dich_vu rỗng")

    co = [g for g in ("goc_0", "goc_45", "goc_90") if phieu["anh_dau_vao"].get(g)]
    if len(co) < 3 and not phieu.get("gioi_han_mo_phong"):
        loi(f"chỉ có {len(co)}/3 góc ảnh mà phiếu không khai 'gioi_han_mo_phong' "
            "→ cổng A ô A1 trượt (FD-03 mục 3). Xin bổ sung ảnh, hoặc khai rõ giới hạn.")


def dung_prompt(phieu: dict, goc: str) -> str:
    dich_vu = phieu["dich_vu"]
    muc_do = MUC_DO_EN.get(phieu.get("muc_do", "M1"), "subtle")

    vung_mo = "; ".join(VUNG_MO_EN.get(d, d) for d in dich_vu)
    khoa = " · ".join(dict.fromkeys(
        KHOA_THEO_DICH_VU_EN.get(d, "") for d in dich_vu if KHOA_THEO_DICH_VU_EN.get(d)
    ))
    giu = phieu.get("giu_nguyen") or []

    cam: list[str] = []
    for d in dich_vu:
        for c in CAM_THEO_DICH_VU_EN.get(d, []):
            if c not in cam:
                cam.append(c)
    cam += [
        "Beautify the whole face, smooth the skin, or add any makeup effect.",
        "Brighten the image or raise contrast relative to the original.",
        "Change the face to the point it is no longer recognisably the same person.",
    ]

    khoi = [
        "Edit the attached photograph. It is a real photo of a cosmetic-surgery",
        f"consultation client, taken at {GOC_EN.get(goc, goc)}.",
        "",
        f"EDIT ONLY: {vung_mo}",
        f"INTENSITY: {muc_do} — keep the change small and believable.",
        "",
        "PRESERVE EXACTLY, do not touch:",
        f"{khoa}",
        f"plus: {KHOA_CHUNG_EN}.",
    ]
    if giu:
        # Nét riêng khách nói rõ muốn giữ — để nguyên chữ của khách, không dịch.
        khoi.append("The client also asked to keep unchanged: " + " · ".join(giu) + ".")
    khoi += ["", "DO NOT:"]
    khoi += [f"- {c}" for c in cam]
    khoi += [
        "",
        "If the requested change cannot be made while preserving recognisability,",
        "make a SMALLER change rather than losing recognisability.",
        "",
        "Keep the original image dimensions and aspect ratio.",
    ]

    if len(dich_vu) > 1:
        khoi += [
            "",
            "Treat these as separate, bounded edits with the stated intensity for each;",
            "do NOT compound them into an overall face-slimming effect.",
        ]
    return "\n".join(khoi)


# ---------------------------------------------------------------- backend ảnh

def goi_gemini(prompt: str, anh: Path) -> bytes:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        loi("thiếu GEMINI_API_KEY trong biến môi trường")
    model = os.environ.get("FD_GEMINI_MODEL", "gemini-2.5-flash-image")
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
           f":generateContent?key={key}")
    mime = mimetypes.guess_type(anh.name)[0] or "image/jpeg"
    body = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": mime,
                                 "data": base64.b64encode(anh.read_bytes()).decode()}},
            ]
        }],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    kq = _post_json(url, body, {})
    for cand in kq.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            data = (part.get("inlineData") or part.get("inline_data") or {}).get("data")
            if data:
                return base64.b64decode(data)
    loi("Gemini không trả về ảnh. Phản hồi: "
        + json.dumps(kq, ensure_ascii=False)[:600])


def goi_openai(prompt: str, anh: Path) -> bytes:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        loi("thiếu OPENAI_API_KEY trong biến môi trường")
    model = os.environ.get("FD_OPENAI_MODEL", "gpt-image-1")
    mime = mimetypes.guess_type(anh.name)[0] or "image/jpeg"
    bien = uuid.uuid4().hex
    phan: list[bytes] = []

    def truong(ten: str, gia_tri: str) -> None:
        phan.append(
            f'--{bien}\r\nContent-Disposition: form-data; name="{ten}"\r\n\r\n'
            f"{gia_tri}\r\n".encode()
        )

    truong("model", model)
    truong("prompt", prompt)
    phan.append(
        f'--{bien}\r\nContent-Disposition: form-data; name="image"; '
        f'filename="{anh.name}"\r\nContent-Type: {mime}\r\n\r\n'.encode()
        + anh.read_bytes() + b"\r\n"
    )
    phan.append(f"--{bien}--\r\n".encode())

    req = urllib.request.Request(
        "https://api.openai.com/v1/images/edits",
        data=b"".join(phan),
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": f"multipart/form-data; boundary={bien}"},
    )
    kq = _doc_json(req)
    for item in kq.get("data", []):
        if item.get("b64_json"):
            return base64.b64decode(item["b64_json"])
    loi("OpenAI không trả về ảnh. Phản hồi: "
        + json.dumps(kq, ensure_ascii=False)[:600])


def _post_json(url: str, body: dict, headers: dict) -> dict:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
    )
    return _doc_json(req)


def _doc_json(req: urllib.request.Request) -> dict:
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        loi(f"HTTP {e.code} từ {req.full_url.split('?')[0]}\n"
            + e.read().decode("utf-8", "replace")[:800])
    except urllib.error.URLError as e:
        loi(f"không gọi được API: {e.reason}")


# ---------------------------------------------------------------- ảnh

def _pil():
    try:
        from PIL import Image, ImageDraw, ImageFont  # noqa: F401
    except ImportError:
        loi("cần Pillow cho việc này:  pip install Pillow")
    from PIL import Image, ImageDraw, ImageFont
    return Image, ImageDraw, ImageFont


def _font(ImageFont, co: int):
    for ten in ("segoeui.ttf", "arial.ttf", "DejaVuSans.ttf",
                "C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(ten, co)
        except OSError:
            continue
    # Font mặc định không có dấu tiếng Việt đầy đủ — cảnh báo thay vì im lặng.
    print("  ⚠️  không tìm thấy font TTF, nhãn có thể mất dấu tiếng Việt",
          file=sys.stderr)
    return ImageFont.load_default()


def in_nhan(anh_vao: Path, anh_ra: Path) -> Path:
    """In nhãn bắt buộc lên ảnh. FD-08 mục 4: nhãn phải nằm TRÊN ảnh."""
    Image, ImageDraw, ImageFont = _pil()
    im = Image.open(anh_vao).convert("RGB")
    w, h = im.size
    co = max(13, w // 42)
    font = _font(ImageFont, co)
    d = ImageDraw.Draw(im, "RGBA")

    hop = d.textbbox((0, 0), NHAN, font=font)
    dem = max(6, co // 2)
    cao = (hop[3] - hop[1]) + dem * 2
    # Dải nhãn đặt sát đáy, chiếm hết chiều ngang → crop mất là crop mất cả mặt.
    d.rectangle([0, h - cao, w, h], fill=(0, 0, 0, 165))
    d.text((w / 2, h - cao / 2), NHAN, font=font, fill=(255, 255, 255), anchor="mm")

    anh_ra.parent.mkdir(parents=True, exist_ok=True)
    im.save(anh_ra, quality=93)
    return anh_ra


def ghep_so_sanh(goc: Path, mo_phong: Path, anh_ra: Path) -> Path:
    """Ghép trước - sau. Ảnh gốc KHÔNG được chỉnh (cổng B ô D1)."""
    Image, ImageDraw, ImageFont = _pil()
    a = Image.open(goc).convert("RGB")
    b = Image.open(mo_phong).convert("RGB")

    # Cùng chiều cao để so sánh được; không crop, không chỉnh sáng.
    if a.height != b.height:
        b = b.resize((round(b.width * a.height / b.height), a.height))

    khe, le_tren = 10, 0
    co = max(14, a.width // 26)
    font = _font(ImageFont, co)
    le_tren = co * 2
    cao_nhan = co * 2

    w = a.width + khe + b.width
    im = Image.new("RGB", (w, le_tren + a.height + cao_nhan), (255, 255, 255))
    im.paste(a, (0, le_tren))
    im.paste(b, (a.width + khe, le_tren))

    d = ImageDraw.Draw(im)
    # anchor="mm" để hai nhãn cột nằm cùng một đường, không lệch theo chiều cao glyph.
    for chu, x, rong in (("TRƯỚC", 0, a.width), ("SAU (mô phỏng)", a.width + khe, b.width)):
        d.text((x + rong / 2, le_tren / 2), chu, font=font, fill=(32, 32, 32),
               anchor="mm")

    d.text((w / 2, le_tren + a.height + cao_nhan / 2), NHAN, font=font,
           fill=(150, 20, 20), anchor="mm")

    anh_ra.parent.mkdir(parents=True, exist_ok=True)
    im.save(anh_ra, quality=93)
    return anh_ra


# ---------------------------------------------------------------- lệnh

def lenh_prompt(args) -> None:
    phieu = doc_phieu(args.phieu)
    gocs = [args.goc] if args.goc else [g for g in ("0", "45", "90")
                                        if phieu["anh_dau_vao"].get(f"goc_{g}")]
    for g in gocs:
        print(f"\n===== GÓC {g}° — {phieu['ma_phieu']} =====\n")
        print(dung_prompt(phieu, g))


def lenh_render(args) -> None:
    phieu = doc_phieu(args.phieu)
    goi = {"gemini": goi_gemini, "openai": goi_openai}[args.backend]
    thu_muc = ROOT / "out" / phieu["ma_khach"]
    gocs = args.goc.split(",") if args.goc else [
        g for g in ("0", "45", "90") if phieu["anh_dau_vao"].get(f"goc_{g}")
    ]

    ra = []
    for g in gocs:
        nguon = phieu["anh_dau_vao"].get(f"goc_{g}")
        if not nguon:
            print(f"  ⚠️  bỏ qua góc {g}° — phiếu không khai ảnh", file=sys.stderr)
            continue
        p_nguon = Path(nguon)
        if not p_nguon.is_absolute():
            p_nguon = ROOT / p_nguon
        if not p_nguon.exists():
            loi(f"không thấy ảnh đầu vào: {p_nguon}")

        print(f"  → góc {g}° · {args.backend} · {p_nguon.name}")
        anh = goi(dung_prompt(phieu, g), p_nguon)

        tho = thu_muc / f"{phieu['ma_phieu']}-mo-phong-{g}-raw.png"
        tho.parent.mkdir(parents=True, exist_ok=True)
        tho.write_bytes(anh)

        co_nhan = in_nhan(tho, thu_muc / f"{phieu['ma_phieu']}-mo-phong-{g}.jpg")
        so_sanh = ghep_so_sanh(p_nguon, tho,
                               thu_muc / f"{phieu['ma_phieu']}-so-sanh-{g}.jpg")
        ra += [co_nhan, so_sanh]

    print("\nĐã tạo:")
    for p in ra:
        print(f"  {p.relative_to(ROOT)}")
    print("\n⛔ CHƯA ĐƯỢC GỬI KHÁCH. Chạy cổng B (19 ô) trước:")
    print("   template/checklist-kiem-duyet.md")


def lenh_nhan(args) -> None:
    vao = Path(args.anh)
    ra = Path(args.o) if args.o else vao.with_name(vao.stem + "-nhan.jpg")
    print(in_nhan(vao, ra))


def lenh_ghep(args) -> None:
    ra = Path(args.o) if args.o else Path(args.mo_phong).with_name("so-sanh.jpg")
    print(ghep_so_sanh(Path(args.goc), Path(args.mo_phong), ra))


def lenh_phieu(args) -> None:
    phieu = doc_phieu(args.phieu)
    d = phieu
    dong = [
        f"# PHIẾU THIẾT KẾ — {d['ma_phieu']}",
        "",
        f"| | |", "|---|---|",
        f"| Ngày | {d.get('ngay', '')} |",
        f"| Mã khách | `{d['ma_khach']}` |",
        f"| Dịch vụ | {d.get('nhom_dich_vu', '')} / {', '.join(d['dich_vu'])} |",
        f"| Mục tiêu (chữ của khách) | {d.get('muc_tieu', '')} |",
        f"| Mức · Phong cách | {d['muc_do']} · {d.get('phong_cach', '')} |",
        f"| Số phương án | {d.get('so_phuong_an', 1)} |",
        f"| Người lập | {d.get('nguoi_lap', '')} |",
        "",
        "## Vùng mở (allow-list — ngoài danh sách này là vùng khoá)",
    ] + [f"- {v}" for v in d["vung_mo"]] + [
        "",
        "## Vùng khoá",
    ] + [f"- {v}" for v in d.get("vung_khoa", [])]

    if d.get("giu_nguyen"):
        dong += ["", "## Nét riêng khách yêu cầu giữ"] + \
                [f"- {v}" for v in d["giu_nguyen"]]

    dong += ["", "## Ảnh đầu vào"]
    for g in ("0", "45", "90"):
        v = d["anh_dau_vao"].get(f"goc_{g}")
        dong.append(f"- **{g}°** — {v if v else '⛔ THIẾU'}")

    if d.get("gioi_han_mo_phong"):
        dong += ["", f"> ⚠️ **Giới hạn mô phỏng:** {d['gioi_han_mo_phong']}"]

    if d.get("phan_tich"):
        dong += ["", "## Phân tích (3 tầng diễn giải)", "",
                 "| Góc | Vùng | Quan sát được | Giả thuyết thẩm mỹ | Cần bác sĩ |",
                 "|---|---|---|---|---|"]
        for r in d["phan_tich"]:
            dong.append(f"| {r['goc']}° | {r['vung']} | {r['quan_sat']} | "
                        f"{r['gia_thuyet']} | {'có' if r['can_bac_si'] else 'không'} |")

    cb = d.get("cong_b", {})
    dong += [
        "", "## Kiểm duyệt",
        f"- Trạng thái: **{cb.get('trang_thai', 'CHUA_RA')}**",
        f"- Ô trượt: {', '.join(cb.get('o_truot') or []) or '—'}",
        f"- Mã lỗi: {', '.join(cb.get('ma_loi') or []) or '—'}",
        f"- Ghi chú: {cb.get('ghi_chu_truot') or '—'}",
        f"- Người kiểm duyệt: {cb.get('nguoi_kiem_duyet') or '—'}",
        "",
        f"## Ghi chú cho bác sĩ / tư vấn viên",
        d.get("ghi_chu_bac_si") or "—",
        "",
        "---",
        f"> **{NHAN}**",
        "> Đồng ý xử lý ảnh: "
        f"{'có' if d.get('dong_y') else 'KHÔNG'} · đồng ý đăng tải: "
        f"{'có' if d.get('dong_y_dang_tai') else 'không'}",
    ]

    noi_dung = "\n".join(dong) + "\n"
    if args.o:
        p = Path(args.o)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(noi_dung, encoding="utf-8")
        print(p)
    else:
        print(noi_dung)


def lenh_gop(args) -> None:
    """Gộp knowledge/ thành một file cho nền tảng giới hạn số file upload."""
    thu_tu = ["FD-A-tiep-nhan", "FD-B-ty-le-khuon-mat", "FD-C-ham-mat",
              "FD-D-nang-mui", "FD-E-cat-mi", "FD-F-tao-anh-kiem-duyet",
              "FD-G-giao-tiep-bao-mat"]
    phan = [
        "# KANGNAM FACE DESIGN — TRI THỨC (bản gộp)",
        "> Gộp 7 file trong `knowledge/`. Mỗi mục `# FD-xx` dưới đây nguyên là một "
        "phần của file nhóm; **mã FD vẫn là đơn vị tham chiếu**, chỉ đổi chỗ nằm.",
        "> Tham chiếu `[[FD-03-cong-anh]]` trỏ tới **mục cùng tên trong chính file này**.",
        "> Sinh bằng `python tools/fd.py gop` — ⛔ đừng sửa tay, sửa ở `knowledge/`.",
        "",
    ]
    for ten in thu_tu:
        p = ROOT / "knowledge" / f"{ten}.md"
        if not p.exists():
            loi(f"không thấy {p.relative_to(ROOT)}")
        phan += ["<!-- " + "=" * 68 + " -->",
                 f"<!-- NGUỒN: knowledge/{ten}.md -->",
                 "<!-- " + "=" * 68 + " -->",
                 "",
                 p.read_text(encoding="utf-8").rstrip(),
                 ""]
    ra = ROOT / "goi" / "KANGNAM-FD-tri-thuc.md"
    ra.parent.mkdir(parents=True, exist_ok=True)
    ra.write_text("\n".join(phan) + "\n", encoding="utf-8")
    print(f"{ra.relative_to(ROOT)} — {len(ra.read_text(encoding='utf-8')):,} ký tự")


def loi(msg: str):
    print(f"⛔ {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    # Console Windows mặc định cp1252 — không in nổi dấu tiếng Việt.
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="lenh", required=True)

    p = sub.add_parser("prompt", help="dựng câu lệnh sửa ảnh từ phiếu")
    p.add_argument("phieu")
    p.add_argument("--goc", choices=["0", "45", "90"])
    p.set_defaults(func=lenh_prompt)

    p = sub.add_parser("render", help="gọi công cụ sửa ảnh, in nhãn, ghép so sánh")
    p.add_argument("phieu")
    p.add_argument("--goc", help="vd 0,45 — mặc định mọi góc có trong phiếu")
    p.add_argument("--backend", choices=["gemini", "openai"], default="gemini")
    p.set_defaults(func=lenh_render)

    p = sub.add_parser("nhan", help="in nhãn mô phỏng lên một ảnh")
    p.add_argument("anh")
    p.add_argument("-o")
    p.set_defaults(func=lenh_nhan)

    p = sub.add_parser("ghep", help="ghép ảnh so sánh trước - sau")
    p.add_argument("goc")
    p.add_argument("mo_phong")
    p.add_argument("-o")
    p.set_defaults(func=lenh_ghep)

    p = sub.add_parser("phieu", help="xuất phiếu thiết kế ra Markdown")
    p.add_argument("phieu")
    p.add_argument("-o")
    p.set_defaults(func=lenh_phieu)

    p = sub.add_parser("gop", help="gộp knowledge/ thành goi/KANGNAM-FD-tri-thuc.md")
    p.set_defaults(func=lenh_gop)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
