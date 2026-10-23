# 03 — OUTPUT MẪU

Một ca gọt hàm chạy hết luồng, từ lúc nhân viên mở việc đến lúc bàn giao.

---

## Lượt 1 — nhân viên mở ca

> Khách KH0417 quan tâm gọt hàm, đã gửi 3 ảnh và đồng ý cho xử lý ảnh.
> Khách nói: *"muốn mặt nhìn thon hơn ở phần góc hàm nhưng vẫn giữ nét mặt hiện tại"*.

**Agent trả:**

```
CỔNG A — ẢNH ĐẦU VÀO
A1 đủ 3 góc .................. ĐẠT
A2 cùng một khách ............ ĐẠT
A3 vùng thiết kế không bị che  ĐẠT
A4 không filter .............. ĐẠT
A5 tư thế đạt ................ ĐẠT
A6 đủ nét .................... ĐẠT
A7 đã đồng ý ................. ĐẠT
→ 7/7, đi tiếp.
```

```
PHÂN TÍCH
0°  · góc hàm      · Đường viền hai bên rộng hơn ở vùng góc hàm, hai bên tương đối đều
                     → Có thể thử mô phỏng đường viền mềm hơn ở mức M1
                     → Cần bác sĩ đánh giá: CÓ (không phân biệt được xương và mô mềm qua ảnh)
45° · má – góc hàm · Chuyển tiếp từ má xuống góc hàm khá rõ nét
                     → Làm mềm đoạn này có thể là điều khách muốn khi nói "thon hơn"
                     → Cần bác sĩ đánh giá: không
90° · bờ dưới hàm  · Bờ dưới hàm liên tục, chuyển về cằm không gấp khúc
                     → Không cần can thiệp vùng cằm, giữ nguyên theo yêu cầu khách
                     → Cần bác sĩ đánh giá: không
```

```
PHIẾU THIẾT KẾ
MÃ PHIẾU   : FD-2026-1023-KH0417-v1
DỊCH VỤ    : Hàm mặt / Gọt hàm
MỤC TIÊU   : "muốn mặt nhìn thon hơn ở phần góc hàm nhưng vẫn giữ nét mặt hiện tại"
MỨC · PHONG CÁCH : M1 · Tự nhiên
VÙNG MỞ    : đường viền góc hàm · bờ dưới hàm · chuyển tiếp góc hàm → cằm
VÙNG KHOÁ  : cằm · gò má · thái dương · trán · má trên · mắt · mũi · môi · tai · chân tóc
GIỮ NGUYÊN : nốt ruồi bên má phải · dáng mắt hiện tại
GÓC MÔ PHỎNG : 0° · 45° · 90°
GIỚI HẠN   : —
ĐỒNG Ý     : true

Chị duyệt phiếu này giúp em rồi em dựng ảnh. Em làm mức M1 trước để có cái so.
```

⛔ Agent **dừng ở đây**. Chưa tạo ảnh.

---

## Lượt 2 — duyệt phiếu, tạo ảnh

> Phiếu ổn. Tạo M1 cho cả ba góc.

```bash
python tools/fd.py render out/KH0417/phieu.json
```
```
  → góc 0° · gemini · KH0417-0.jpg
  → góc 45° · gemini · KH0417-45.jpg
  → góc 90° · gemini · KH0417-90.jpg

Đã tạo:
  out\KH0417\FD-2026-1023-KH0417-v1-mo-phong-0.jpg
  out\KH0417\FD-2026-1023-KH0417-v1-so-sanh-0.jpg
  out\KH0417\FD-2026-1023-KH0417-v1-mo-phong-45.jpg
  out\KH0417\FD-2026-1023-KH0417-v1-so-sanh-45.jpg
  out\KH0417\FD-2026-1023-KH0417-v1-mo-phong-90.jpg
  out\KH0417\FD-2026-1023-KH0417-v1-so-sanh-90.jpg

⛔ CHƯA ĐƯỢC GỬI KHÁCH. Chạy cổng B (19 ô) trước:
   template/checklist-kiem-duyet.md
```

---

## Lượt 3 — cổng B trượt (tình huống hay gặp nhất)

```
CỔNG B — 17/19
Ô TRƯỢT : C4 · D3
C4 : góc 0° đường viền hàm đã thon hơn, góc 45° gần như không đổi → hai góc mâu thuẫn
D3 : vùng trán và phông nền ở ảnh sau sáng hơn rõ rệt so với ảnh gốc

MÃ LỖI    : E03 (C4) · E01 (D3)
HÀNH ĐỘNG : KHÔNG PHÁT HÀNH.
            Tạo lại cả bộ 3 góc TỪ ẢNH GỐC, thêm vào câu lệnh dòng chặn
            "do not brighten the image or raise contrast relative to the original".
PHIÊN BẢN TIẾP : FD-2026-1023-KH0417-v2
```

⛔ Không sửa đè lên v1. Quay về ảnh gốc, tạo v2.

---

## Lượt 4 — đạt, bàn giao

```
1. DỊCH VỤ MÔ PHỎNG     : Hàm mặt — gọt hàm
2. MỤC TIÊU THẨM MỸ     : mặt nhìn thon hơn ở phần góc hàm, giữ nét mặt hiện tại
3. VÙNG ĐÃ THAY ĐỔI     : đường viền góc hàm và bờ dưới hàm, mức M1 (nhẹ);
                          chuyển tiếp góc hàm → cằm được làm mềm hơn
4. VÙNG ĐƯỢC GIỮ NGUYÊN : cằm · gò má · thái dương · mắt · mũi · môi · chân tóc ·
                          nốt ruồi bên má phải · dáng mắt
5. DANH SÁCH ẢNH        : ảnh gốc (3 góc) · ảnh mô phỏng (3 góc) ·
                          ảnh so sánh trước–sau (3 góc) · phiếu thiết kế
6. TRẠNG THÁI KIỂM DUYỆT: ĐẠT 19/19 · v2 · người kiểm duyệt NV-QC-01
7. CẢNH BÁO             : Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế
8. GHI CHÚ CHO BÁC SĨ   : Khách quan tâm gọt hàm. Qua ảnh không xác định được phần
                          rộng đến từ xương hay mô mềm — đề nghị bác sĩ xác nhận khi khám.
                          Khách nói rõ muốn giữ nét mặt hiện tại, không muốn V-line.
```

**Gợi ý tin nhắn gửi khách** *(người thật đọc lại rồi gửi)*
```
Chị ơi, em gửi chị bản mô phỏng theo đúng điều chị nói là muốn phần góc hàm nhìn
thon hơn mà vẫn giữ nét mặt hiện tại ạ.

Em chỉ điều chỉnh đường viền góc hàm và phần bờ dưới hàm, ở mức nhẹ. Cằm, gò má,
mắt, mũi, môi và nốt ruồi bên má phải em giữ nguyên như ảnh gốc của chị.

Đây là ảnh mô phỏng bằng AI để chị hình dung hướng thiết kế, không phải kết quả
phẫu thuật thực tế ạ. Phần nào làm được tới đâu thì cần bác sĩ khám trực tiếp mới
nói chính xác được, vì qua ảnh chưa xác định được phần rộng đó đến từ xương hay
mô mềm.

Chị xem thử rồi cho em biết muốn rõ hơn một chút hay giữ như vậy nhé. Nếu chị
muốn, em sắp lịch để bác sĩ xem trực tiếp cho chị ạ.
```

---

## Những gì KHÔNG có trong output mẫu này — và vì sao
| Không có | Lý do |
|---|---|
| Giá, ưu đãi | Ngoài phạm vi agent này → chuyển tư vấn viên hoặc `Agent-BaoGia-Kangnam` |
| *"Chị hợp với gọt hàm"* | Kết luận về mức độ phù hợp là việc của bác sĩ (`FD-01` mục 2) |
| *"Sau mổ chị sẽ như thế này"* | Cam kết kết quả — từ cấm (`FD-11` mục 3) |
| Mốc hồi phục | Không mốc cứng, chuyển bác sĩ / tư vấn viên |
| Ba mức M1/M2/M3 cùng lúc | M1 trước, có cái để so rồi mới lên mức (luật nền ③) |
