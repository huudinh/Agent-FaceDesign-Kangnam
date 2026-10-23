# 01 — CÀI ĐẶT (20 phút)

Agent này có **hai nửa**:
- **Nửa não** — prompt + knowledge, chạy trên Claude / ChatGPT / Gemini. Không cần cài gì lên máy.
- **Nửa tay** — `tools/fd.py`, dựng câu lệnh từ phiếu, gọi công cụ sửa ảnh, in nhãn và ghép ảnh so sánh. Cần Python 3.9+ và Pillow.

Dùng nửa não mà chưa có nửa tay thì vẫn ra được phân tích, phiếu thiết kế và câu lệnh — chỉ là phải tự chạy ảnh bằng công cụ khác và tự gắn nhãn.

---

## 0. Ba ô phải điền khi tạo agent mới

**Tên**
```
Agent-FaceDesign-Kangnam
```

**Mô tả** — 243 ký tự, dưới giới hạn 300 của ChatGPT:
```
Dựng ảnh mô phỏng thẩm mỹ trước – sau từ ảnh thật của khách cho ba nhóm dịch vụ: hàm mặt, nâng mũi, cắt mí. Chỉ sửa vùng khách yêu cầu, giữ nhận diện, qua hai cổng kiểm tra trước khi phát hành. Không chẩn đoán, không cam kết kết quả phẫu thuật.
```

**Câu mở đầu hội thoại** — ô *Conversation starters* của ChatGPT:
```
/wizard — mở một ca mô phỏng mới
```
```
Khách gửi 3 ảnh và muốn xem thử nếu gọt hàm thì mặt thế nào
```

---

## 1. Nạp bộ não

| Nền tảng | Dán vào đâu | Dùng file nào |
|---|---|---|
| **Claude Project** | *Custom instructions* | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md), khối giữa hai vạch ▼▲ |
| **ChatGPT Custom GPT** | *Instructions* (giới hạn 8.000 ký tự) | [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) |
| **Gemini Gem** | *Chỉ dẫn* | `SYSTEM-PROMPT.md` |
| **Claude Code** | `CLAUDE.md` của repo, hoặc dán vào chat | `SYSTEM-PROMPT.md` |

## 2. Nạp tri thức

**Bản rời (12 file)** — chuẩn, dùng khi nền tảng không giới hạn:
```
knowledge/FD-A-tiep-nhan.md          prompts/module-ham-mat.md
knowledge/FD-B-ty-le-khuon-mat.md    prompts/module-nang-mui.md
knowledge/FD-C-ham-mat.md            prompts/module-cat-mi.md
knowledge/FD-D-nang-mui.md           prompts/prompt-wizard.md
knowledge/FD-E-cat-mi.md             prompts/prompt-kiem-duyet.md
knowledge/FD-F-tao-anh-kiem-duyet.md template/checklist-kiem-duyet.md
knowledge/FD-G-giao-tiep-bao-mat.md
```

**Bản gộp (1 file)** — khi nền tảng giới hạn số file upload (Gemini Gems: 10):
```
goi/KANGNAM-FD-tri-thuc.md
```
Sinh lại bản gộp sau mỗi lần sửa `knowledge/`:
```bash
python tools/fd.py gop
```
⛔ Đừng sửa tay file gộp — lần `gop` tiếp theo sẽ ghi đè.

---

## 3. ⚠️ Nền tảng phải sửa được ảnh

Đây là điều kiện quyết định, và là chỗ dễ vỡ kế hoạch nhất.

**Agent này chỉnh sửa ảnh thật của khách.** Nó không sinh ảnh mới từ mô tả. Vì vậy nền tảng chạy nó phải có công cụ **nhận ảnh đầu vào và trả về ảnh đã sửa** (image-to-image / inpainting). Dán prompt vào một cuộc chat chỉ có văn bản thì ra được phân tích, phiếu và câu lệnh — **không ra được bộ ảnh nhất quán ở ba góc**.

Ba cách triển khai, chọn một:

| Cách | Mô tả | Khi nào hợp |
|---|---|---|
| **A. Nền tảng tự sửa ảnh** | Dùng công cụ sửa ảnh có sẵn của ChatGPT / Gemini | Chạy thử, ít ca/ngày |
| **B. Nửa não + `tools/fd.py render`** | Agent chốt phiếu → script gọi API sửa ảnh → in nhãn, ghép so sánh | **Khuyến nghị cho vận hành** — nhãn và ảnh so sánh ra đều tay |
| **C. Nửa não + designer** | Agent xuất câu lệnh + phiếu, người thiết kế tự chạy công cụ quen dùng | Khi đã có đội thiết kế và công cụ riêng |

### Cài nửa tay (cách B)
```bash
pip install Pillow
```
Khoá API đặt ở biến môi trường, ⛔ **không commit vào repo**:
```powershell
# Windows PowerShell — đặt cho phiên hiện tại
$env:GEMINI_API_KEY = "..."
# hoặc
$env:OPENAI_API_KEY = "..."
```
Tên model là tham số vì nó đổi theo thời điểm:
```powershell
$env:FD_GEMINI_MODEL = "gemini-2.5-flash-image"   # mặc định
$env:FD_OPENAI_MODEL = "gpt-image-1"              # mặc định
```
Model nào sửa ảnh giữ nhận diện tốt nhất là **câu hỏi phải tự kiểm thử**, không phải câu hỏi có đáp án sẵn — chạy giai đoạn 2 trong `FD-10` mục 2 với ảnh nhân sự nội bộ trước khi chốt.

---

## 4. Chạy thử 5 phút
```bash
# 1. Xem câu lệnh agent sẽ dùng, dựng từ phiếu mẫu
python tools/fd.py prompt template/phieu-thiet-ke.mau.json --goc 0

# 2. Xuất phiếu thiết kế ra Markdown
python tools/fd.py phieu template/phieu-thiet-ke.mau.json

# 3. In nhãn lên một ảnh bất kỳ
python tools/fd.py nhan duong/dan/anh.jpg

# 4. Ghép ảnh so sánh trước - sau
python tools/fd.py ghep anh-goc.jpg anh-mo-phong.jpg
```

Thử cổng chặn: sửa `"dong_y": true` thành `false` trong phiếu mẫu rồi chạy lại lệnh 1 — script phải **dừng**, không in câu lệnh. Dừng đúng là cổng còn sống.

---

## 5. Trước khi đưa ảnh khách thật vào

Bốn việc, làm theo thứ tự (`FD-12`):
1. Kiểm tra **loại tài khoản và cấu hình dữ liệu** của nền tảng đang dùng — ảnh có bị dùng để huấn luyện không.
2. Chốt **chính sách lưu trữ**: lưu ở đâu, ai xem được, giữ bao lâu, xoá thế nào, xử lý ra sao khi khách rút lại đồng ý.
3. Soạn **câu xin đồng ý** chuẩn, tách riêng đồng ý *mô phỏng* và đồng ý *đăng tải*.
4. Chạy giai đoạn 2 của `FD-10` bằng **ảnh nhân sự nội bộ đã đồng ý**, không dùng ảnh khách.

⛔ Chưa xong bốn việc này thì chưa đưa ảnh khách thật vào quy trình.

> Thư mục `out/` **không commit** (đã `.gitignore`). Ảnh khuôn mặt khách là dữ liệu nhận diện cá nhân — không đẩy lên GitHub, kể cả repo riêng tư.
