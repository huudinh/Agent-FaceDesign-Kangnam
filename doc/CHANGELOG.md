# CHANGELOG

## v1.0 — 2026-10-23
Bản đầu. Dựng từ kho kiến thức nội bộ *"Trợ lý AI thiết kế mô phỏng thẩm mỹ khuôn mặt"* (K01–K12), chuyển thành khuôn agent của repo `Project/Agent`.

**Có gì**
- Bộ não: `SYSTEM-PROMPT.md` (13 §) + `SYSTEM-PROMPT-NGAN.md` (7.988 ký tự, vừa giới hạn 8.000 của ChatGPT).
- Tri thức: 12 mã `FD-01…FD-12` trong 7 file nhóm.
- Ba module dịch vụ: hàm mặt (3 dịch vụ con) · nâng mũi · cắt mí — mỗi module có prompt nghiệp vụ, câu lệnh sửa ảnh bản Việt và bản Anh.
- Nửa tay `tools/fd.py`: `prompt` · `render` · `nhan` · `ghep` · `phieu` · `gop`.
- Phiếu thiết kế có schema JSON + bản mẫu; checklist kiểm duyệt in ra tick tay.

**Bốn thứ thêm so với bản gốc trong chat**
| Thêm | Vì sao |
|---|---|
| Hai cổng chặn có mã ô — A 7 ô, B 19 ô | *"Hãy kiểm tra trước khi trả ảnh"* là lời khuyên; 26 ô có mã là một cổng |
| Bảng **vùng mở / vùng khoá** cho từng module | Nguồn của gần như mọi lỗi nhóm này là AI sửa vùng không ai yêu cầu. Allow-list chặn được, lời nhắc thì không |
| Ba mức `M1/M2/M3` + luật M1 trước | Đặt mã để phiếu và thư viện mẫu tham chiếu được |
| Mã lỗi `E01–E08` + luật quay về ảnh gốc | Sửa đè lên ảnh đã lỗi làm khuôn mặt trượt xa khách sau mỗi vòng |

**Chưa có — việc của giai đoạn sau** (`FD-10` mục 2)
- Thư viện mẫu `HM-01…MM-02` chưa có ảnh thật: cần ảnh đã được phép dùng + prompt + đánh giá người kiểm duyệt cho từng mã.
- Chưa chọn model sửa ảnh: `FD_GEMINI_MODEL` / `FD_OPENAI_MODEL` là tham số, phải chạy kiểm thử giai đoạn 2 bằng ảnh nhân sự nội bộ rồi mới chốt.
- Chưa có số liệu KPI thật — `FD-01` mục 4 chỉ định nghĩa chỉ số, không đặt sẵn ngưỡng.
- Ba tài liệu bác sĩ phải duyệt (`FD-10` mục 3) chưa có chữ ký duyệt.

## v1.1 — 2026-10-23
- Thêm [`doc/04-trien-khai-gpt-gemini.md`](04-trien-khai-gpt-gemini.md): danh sách nạp riêng cho ChatGPT Custom GPT (20 file, bản rời) và Gemini Gem (10 file, bản gộp), **bài test 15 phút** về khả năng sửa ảnh khuôn mặt, và phần tài khoản/dữ liệu cho nền tảng tiêu dùng.
- README trỏ sang tài liệu mới ở Quick start.
