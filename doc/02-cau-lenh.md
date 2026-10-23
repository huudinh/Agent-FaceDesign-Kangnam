# 02 — CÂU LỆNH

## Mở một ca mới
```
/wizard
```
Agent hỏi tối đa 3 câu một lượt, thu đủ 11 trường, chạy cổng A, in phân tích và phiếu thiết kế, rồi **dừng** chờ duyệt.

Hoặc đưa thẳng ngữ cảnh:
```
Khách KH0417 quan tâm gọt hàm. Khách nói "muốn mặt nhìn thon hơn ở phần góc hàm
nhưng vẫn giữ nét mặt hiện tại". Đã đồng ý cho xử lý ảnh. Đây là 3 ảnh:
[đính kèm 0°, 45°, 90°]
```

---

## Chốt phiếu rồi tạo ảnh
```
Phiếu ổn rồi. Tạo mức M1 cho cả ba góc.
```
```
M1 nhìn còn nhẹ quá. Khách muốn rõ hơn một chút — tạo thêm M2 để so, giữ nguyên vùng mở.
```
⛔ Đừng gõ *"làm thật rõ cho em xem"* ngay từ đầu — agent sẽ từ chối và quay về M1 (luật nền ③).

---

## Kiểm duyệt
```
/kiemduyet
```
```
Rà cổng B cho bộ ảnh vừa tạo. Ô nào trượt thì nói rõ nhìn thấy gì trên ảnh.
```

---

## Khi có vấn đề
| Tình huống | Gõ |
|---|---|
| Ảnh sau nhìn không ra khách nữa | `Ảnh v1 mất nhận diện ở vùng cằm. E02 — làm lại từ ảnh gốc, hẹp vùng mở lại.` |
| Góc 0° đổi, góc 45° không đổi | `C4 trượt: 0° thấy hàm thon hơn, 45° gần như không đổi. Tạo lại cả bộ.` |
| Ảnh sau sáng hơn ảnh gốc | `D3 trượt: phông nền và trán ở ảnh sau sáng hơn. Thêm dòng chặn brighten/contrast.` |
| Khách chỉ gửi 1 ảnh | `Khách chỉ có ảnh chính diện. Làm được tới đâu?` |
| Khách hỏi có mổ được không | `Khách hỏi "em làm được không bác sĩ nói sao"` → agent chuyển E08 |

---

## Lệnh của nửa tay — `tools/fd.py`

| Lệnh | Việc |
|---|---|
| `python tools/fd.py prompt <phieu.json> [--goc 0]` | In câu lệnh sửa ảnh dựng từ phiếu |
| `python tools/fd.py render <phieu.json> [--goc 0,45] [--backend gemini\|openai]` | Gọi công cụ sửa ảnh → in nhãn → ghép so sánh → lưu vào `out/<ma_khach>/` |
| `python tools/fd.py nhan <anh.jpg> [-o ra.jpg]` | In nhãn bắt buộc lên một ảnh |
| `python tools/fd.py ghep <goc.jpg> <mo-phong.jpg> [-o ra.jpg]` | Ghép ảnh so sánh trước – sau |
| `python tools/fd.py phieu <phieu.json> [-o ra.md]` | Xuất phiếu thiết kế ra Markdown để bàn giao |
| `python tools/fd.py gop` | Gộp `knowledge/` → `goi/KANGNAM-FD-tri-thuc.md` |

### Luồng đầy đủ một ca
```bash
# 1. Agent chốt phiếu → lưu thành out/KH0417/phieu.json
# 2. Xem lại câu lệnh trước khi tiêu tiền API
python tools/fd.py prompt out/KH0417/phieu.json

# 3. Chạy ảnh
python tools/fd.py render out/KH0417/phieu.json --backend gemini

# 4. Mở ảnh ra, rà 19 ô cổng B bằng template/checklist-kiem-duyet.md
# 5. Đạt → xuất phiếu bàn giao
python tools/fd.py phieu out/KH0417/phieu.json -o out/KH0417/phieu.md
```

`render` in sẵn dòng nhắc cuối cùng: **chưa được gửi khách trước khi qua cổng B.** Script không tự chặn bước gửi được — việc đó là của người.

---

## Hai thứ script tự chặn
1. `dong_y != true` → dừng ngay, không dựng câu lệnh, không gọi API.
2. Thiếu góc ảnh mà phiếu **không khai** `gioi_han_mo_phong` → dừng, bắt khai rõ giới hạn hoặc xin thêm ảnh.

Còn lại là việc của người và của bộ não. Script không nhìn được ảnh, nên nó **không chấm được** B1 nhận diện, C4 nhất quán góc hay D3 ánh sáng — ba ô khó nhất của cổng B vẫn cần mắt người.
