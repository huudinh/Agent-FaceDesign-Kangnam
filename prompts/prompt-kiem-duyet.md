# PROMPT — CHẠY CỔNG B (KIỂM DUYỆT)
> Dùng khi đã có ảnh mô phỏng và cần rà 19 ô trước khi phát hành.
> Người kiểm duyệt nên là **người khác** với người dựng ảnh. Cùng một người tự chấm ảnh mình vừa làm sẽ bỏ qua đúng những ô mình đã quen mắt.

---

## 1. Khối lệnh — tự kiểm trong chat

```
/kiemduyet

Đây là ảnh gốc và ảnh mô phỏng của phiếu <MÃ PHIẾU>.
Rà đủ 19 ô của cổng B. Với mỗi ô ghi ĐẠT hoặc TRƯỢT; ô TRƯỢT phải kèm
một dòng nói rõ nhìn thấy gì trên ảnh, không kết luận chung chung.

Rà xong thì:
- Trượt ô nào → tra bảng mã lỗi E01–E08 và nói đúng hành động phải làm.
- Đạt cả 19 ô → in đầu ra 8 mục và đoạn tin nhắn gợi ý gửi khách.

⛔ Không tự sửa tiếp trên ảnh đã trượt. Nếu phải làm lại thì làm lại từ ảnh gốc.
```

---

## 2. Cách đọc ba ô dễ chấm sai

**B1 — "vẫn là cùng một khách"**
Đừng so hai ảnh cạnh nhau rồi kết luận giống. Cách chấm đúng: che vùng đã sửa đi, so phần còn lại. Phần **không được sửa** mà cũng khác đi → B1 trượt, dù khuôn mặt tổng thể vẫn "na ná".

**C4 — "các góc không mâu thuẫn"**
Góc 0° thấy hàm thon hơn mà góc 45° vẫn như cũ (hoặc ngược lại) → mô hình chỉ sửa được một ảnh, không sửa nhất quán cả bộ. Đây là lỗi hay gặp nhất khi chạy ba góc bằng ba lần gọi riêng. Xử theo `E03`.

**D3 — "ánh sáng không tạo lợi thế giả"**
Ô bị bỏ qua nhiều nhất. Cách chấm: nhìn **vùng không được sửa** — nếu trán, cổ hoặc phông nền ở ảnh sau sáng hơn, mịn hơn, bớt nhiễu hơn ảnh gốc thì mô hình đã chỉnh cả tấm ảnh, không chỉ chỉnh vùng cho phép. Khách sẽ thấy "đẹp hơn" vì ảnh đẹp hơn, không vì phương án tốt hơn.

---

## 3. Mẫu ghi kết quả vào phiếu
```
TRẠNG THÁI KIỂM DUYỆT : TRƯỢT
Ô TRƯỢT  : C4 · D3
C4 : góc 0° đường viền hàm đã thon hơn, góc 45° gần như không đổi → hai góc mâu thuẫn
D3 : vùng trán và phông nền ở ảnh sau sáng hơn rõ rệt so với ảnh gốc
MÃ LỖI   : E03 (C4) · E01 (D3)
HÀNH ĐỘNG: không phát hành · tạo lại cả bộ 3 góc từ ảnh gốc, thêm dòng chặn
           "do not brighten the image or raise contrast relative to the original"
PHIÊN BẢN TIẾP : FD-2026-1023-KH0417-v2
```

Ghi được **nhìn thấy gì** thì lần tạo lại mới sửa đúng chỗ. Ghi *"ảnh chưa tự nhiên"* thì lần sau vẫn trượt đúng ô đó.
