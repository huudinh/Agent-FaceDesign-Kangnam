# 🧑‍🎨 AGENT-FACEDESIGN-KANGNAM — Trợ lý thiết kế mô phỏng thẩm mỹ khuôn mặt

> Version 1.0 · Biến **ảnh thật của một khách hàng** thành **bộ mô phỏng trước – sau cá nhân hoá** cho ba nhóm dịch vụ: **hàm mặt · nâng mũi · cắt mí**.
>
> Agent **không** chẩn đoán, **không** chỉ định phẫu thuật, **không** cam kết kết quả. Ảnh nó tạo là **mô phỏng ý tưởng thẩm mỹ**, không phải dự báo kết quả phẫu thuật.

Kiến trúc **lõi quy trình brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **tri thức thẩm mỹ** ([`knowledge/FD-A…FD-G`](knowledge/)) + **module theo dịch vụ** ([`prompts/`](prompts/)) → **đổi dịch vụ = thêm module, không sửa lõi**.

---

## Nguyên tắc tối thượng

> **Nhận diện đứng trên cái đẹp.**
>
> Không thể vừa thực hiện thay đổi vừa giữ nhận diện → **hạ mức độ** hoặc **thiết kế lại**. Một ảnh đẹp mà khách không còn nhận ra mình là một ảnh **trượt**, không phải một ảnh thành công.

> **Agent chỉ dựng, người duyệt trước khi gửi khách.**
>
> Agent phân tích, dựng câu lệnh, kiểm duyệt và viết phiếu bàn giao. Người thật xem ảnh rồi mới bấm gửi.

---

## Hai cổng chặn — xương sống của agent

```
B1 dịch vụ → B2 mong muốn → ⛔ CỔNG A (7 ô) → B4 phân tích → B5 chốt phiếu
                                                                    ↓
                        ⛔ CỔNG B (19 ô) ← B6 tạo ảnh (M1 trước) ←──┘
                                 ↓
                      ĐẠT 19/19 → bàn giao        TRƯỢT → E01…E08, quay về ẢNH GỐC
```

| Cổng | Khi nào | Trượt thì sao |
|---|---|---|
| **A** — 7 ô ảnh đầu vào | trước khi tạo ảnh | Thiếu ảnh → xin bổ sung. ⛔ Không tự dựng góc thiếu. **A7 (đồng ý) trượt → dừng hoàn toàn** |
| **B** — 19 ô kiểm duyệt | trước khi phát hành | Tra mã lỗi `E01–E08`. ⛔ Không sửa đè lên ảnh lỗi — quay về **ảnh gốc** |

---

## Ba module dịch vụ

| Module | Dịch vụ | Vùng MỞ | Góc chủ lực |
|---|---|---|---|
| **Hàm mặt** ([`FD-C`](knowledge/FD-C-ham-mat.md)) | Gọt hàm · Hạ gò má · Trượt cằm | đường viền góc hàm · độ nhô gò má · hình dáng cằm | 0° · 45° (trượt cằm cần **90°**) |
| **Nâng mũi** ([`FD-D`](knowledge/FD-D-nang-mui.md)) | Nâng mũi | sống mũi · đầu mũi · cánh mũi (theo yêu cầu) | cả 3 góc |
| **Cắt mí** ([`FD-E`](knowledge/FD-E-cat-mi.md)) | Cắt mí | **chỉ** nếp mí trên | **0°** · 45° |

⛔ **Không dùng chung một câu lệnh "làm mặt V-line" cho cả ba dịch vụ hàm mặt.** Mỗi dịch vụ tác động một vùng khác nhau; gộp lại là cách nhanh nhất để mất nhận diện khách.

---

## Mười hai mã tri thức

| Mã | Nội dung | File |
|---|---|---|
| `FD-01` | Vai trò · ranh giới · KPI | [`FD-A`](knowledge/FD-A-tiep-nhan.md) |
| `FD-02` | 11 trường tiếp nhận · cách khai thác mong muốn | `FD-A` |
| `FD-03` | **Cổng A** — tiêu chuẩn 3 ảnh | `FD-A` |
| `FD-04` | 4 nhóm tỉ lệ khuôn mặt · 6 điều không vi phạm | [`FD-B`](knowledge/FD-B-ty-le-khuon-mat.md) |
| `FD-05` | Hàm mặt — 3 module | [`FD-C`](knowledge/FD-C-ham-mat.md) |
| `FD-06` | Nâng mũi — 6 vùng · 3 phong cách · 7 lỗi | [`FD-D`](knowledge/FD-D-nang-mui.md) |
| `FD-07` | Cắt mí — 7 hạng mục · 6 điều không vi phạm | [`FD-E`](knowledge/FD-E-cat-mi.md) |
| `FD-08` | 5 thành phần đầu ra · 8 luật giữ nhận diện | [`FD-F`](knowledge/FD-F-tao-anh-kiem-duyet.md) |
| `FD-09` | **Cổng B** — 19 ô · mã lỗi E01–E08 | `FD-F` |
| `FD-10` | Thư viện mẫu · 4 giai đoạn triển khai | `FD-F` |
| `FD-11` | Giọng · từ cấm · khuôn trả lời ngoài phạm vi | [`FD-G`](knowledge/FD-G-giao-tiep-bao-mat.md) |
| `FD-12` | 6 quy tắc bảo mật ảnh khuôn mặt | `FD-G` |

---

## Quick start (4 bước)

1. Tạo 1 Project / GPT / Gem mới. Tên và mô tả: xem [`doc/01-cai-dat.md`](doc/01-cai-dat.md) §0.
2. **Instructions:** dán khối ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — riêng **ChatGPT Custom GPT** (giới hạn 8.000 ký tự) dùng [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md).
3. **Knowledge:** upload 7 file [`knowledge/`](knowledge/) + 5 file [`prompts/`](prompts/) + [`template/checklist-kiem-duyet.md`](template/checklist-kiem-duyet.md). Nền tảng giới hạn số file (**Gemini Gems: 10**) → dùng [`goi/KANGNAM-FD-tri-thuc.md`](goi/KANGNAM-FD-tri-thuc.md).
4. Gõ `/wizard` để mở ca đầu tiên.

> **Chạy trên ChatGPT hoặc Gemini?** Đọc [`doc/04-trien-khai-gpt-gemini.md`](doc/04-trien-khai-gpt-gemini.md) trước — nó có **bài test 15 phút** phải làm *trước khi cài*, trả lời câu hỏi quyết định cả dự án: nền tảng có chịu sửa ảnh khuôn mặt khách không.

**Câu lệnh mẫu:**
```
/wizard — mở một ca mô phỏng mới
```
```
Khách KH0417 quan tâm gọt hàm, đã gửi 3 ảnh và đồng ý cho xử lý ảnh.
Khách nói "muốn mặt nhìn thon hơn ở phần góc hàm nhưng vẫn giữ nét mặt hiện tại".
```

---

## ⚠️ Nền tảng phải sửa được ảnh

Agent này **chỉnh sửa ảnh thật của khách**, không sinh ảnh mới từ mô tả. Dán prompt vào một cuộc chat chỉ có văn bản thì ra được phân tích, phiếu thiết kế và câu lệnh — **không ra được bộ ảnh nhất quán ở ba góc**.

Ba cách triển khai, chi tiết ở [`doc/01-cai-dat.md`](doc/01-cai-dat.md) §3:
**A.** nền tảng tự sửa ảnh · **B.** nửa não + `tools/fd.py render` *(khuyến nghị)* · **C.** nửa não + người thiết kế tự chạy.

---

## Nửa tay — `tools/fd.py`

```bash
pip install Pillow

python tools/fd.py prompt template/phieu-thiet-ke.mau.json --goc 0   # xem câu lệnh
python tools/fd.py render out/KH0417/phieu.json                      # chạy ảnh + nhãn + ghép
python tools/fd.py nhan  anh.jpg                                     # in nhãn bắt buộc
python tools/fd.py ghep  goc.jpg mo-phong.jpg                        # ảnh so sánh
python tools/fd.py phieu out/KH0417/phieu.json -o phieu.md           # phiếu bàn giao
python tools/fd.py gop                                               # gộp knowledge/
```

Script tự chặn **hai** thứ: `dong_y != true` → dừng; thiếu góc ảnh mà không khai `gioi_han_mo_phong` → dừng.
Script **không** chấm được B1 nhận diện, C4 nhất quán góc, D3 ánh sáng — ba ô khó nhất của cổng B vẫn cần mắt người.

---

## ⚠️ Trước khi đưa ảnh khách thật vào

Ảnh khuôn mặt là dữ liệu **nhận diện được một cá nhân**. Bốn việc phải làm xong trước (`FD-12`, chi tiết [`doc/01-cai-dat.md`](doc/01-cai-dat.md) §5):

1. Kiểm tra loại tài khoản và cấu hình dữ liệu của nền tảng — ảnh có bị dùng để huấn luyện không.
2. Chốt chính sách lưu trữ: ở đâu · ai xem được · giữ bao lâu · xoá thế nào · xử lý ra sao khi khách rút đồng ý.
3. Soạn câu xin đồng ý, **tách riêng** đồng ý *mô phỏng* và đồng ý *đăng tải*.
4. Chạy thử bằng **ảnh nhân sự nội bộ đã đồng ý**, không dùng ảnh khách.

⛔ Thư mục `out/` không commit. Không đẩy ảnh khuôn mặt khách lên GitHub, kể cả repo riêng tư.

---

## Ba tài liệu bác sĩ phải duyệt trước khi mở rộng

Prompt chỉ là **lớp hướng dẫn**. Độ ổn định thật phụ thuộc công cụ tạo ảnh, chất lượng ảnh đầu vào và quá trình kiểm thử. Ba tài liệu quyết định chất lượng (`FD-10` mục 3):

1. **Bộ tiêu chí thẩm mỹ được phép dùng** — mốc quan sát, nguyên tắc hài hoà, và những gì AI **không được** kết luận.
2. **Bộ ảnh chuẩn theo từng dịch vụ** — ảnh đầu vào, ảnh mô phỏng đạt, ảnh lỗi và **lý do lỗi**.
3. **Bộ quy tắc thay đổi hình ảnh** — vùng được chỉnh, vùng giữ nguyên, mức độ, tiêu chí loại ảnh.

---

## Tài liệu
| File | Nội dung |
|---|---|
| [`doc/01-cai-dat.md`](doc/01-cai-dat.md) | Cài đặt · 3 cách triển khai ảnh · chạy thử 5 phút |
| [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) | Câu lệnh chat · lệnh `fd.py` · luồng đầy đủ một ca |
| [`doc/03-output-mau.md`](doc/03-output-mau.md) | Một ca gọt hàm chạy hết luồng, kể cả lượt trượt cổng B |
| [`doc/04-trien-khai-gpt-gemini.md`](doc/04-trien-khai-gpt-gemini.md) | **Chạy trên ChatGPT + Gemini** — nạp gì vào đâu · bài test 15 phút · tài khoản & dữ liệu |
| [`doc/CHANGELOG.md`](doc/CHANGELOG.md) | Phiên bản · những gì chưa có |
"# Agent-FaceDesign-Kangnam" 
