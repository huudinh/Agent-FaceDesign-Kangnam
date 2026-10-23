# PROMPT — WIZARD TIẾP NHẬN
> Dùng khi nhân viên mở một ca mới và chưa có đủ 11 trường của `FD-02`.
> Gõ `/wizard` hoặc dán nguyên khối dưới đây.

---

## Khối lệnh

```
/wizard

Mở một ca mô phỏng mới. Hỏi tôi tối đa 3 câu một lượt, mỗi câu kèm phương án chọn
sẵn và một lựa chọn "để agent chọn". Đừng hỏi hết 11 trường một lúc.

Thứ tự ưu tiên khi hỏi:
1. dong_y (bắt buộc, không giả định được) + ma_khach
2. nhom_dich_vu + dich_vu
3. muc_tieu bằng chữ của khách
4. anh_dau_vao có những góc nào
5. giu_nguyen — nét riêng khách muốn giữ
6. muc_do + phong_cach + so_phuong_an  (được giả định M1 / Tự nhiên / 1)

Thu đủ rồi thì:
- in CỔNG A (7 ô ĐẠT/TRƯỢT),
- nếu ĐẠT thì in phần PHÂN TÍCH và PHIẾU THIẾT KẾ cho tôi duyệt,
- dừng ở đó. Chưa tạo ảnh.
```

---

## Ba câu hỏi mở đầu mẫu (nếu agent cần gợi ý)

**Câu 1 — đồng ý và mã khách**
> Trước khi bắt đầu: khách đã được thông báo mục đích xử lý ảnh và đã đồng ý chưa?
> `a)` Đã đồng ý · `b)` Chưa — tôi sẽ xin trước · `c)` Đang dùng ảnh nhân sự nội bộ để chạy thử
> Và mã khách nội bộ là gì? (⛔ không cần tên thật)

**Câu 2 — dịch vụ**
> Khách quan tâm nhóm nào?
> `a)` Hàm mặt — gọt hàm / hạ gò má / trượt cằm · `b)` Nâng mũi · `c)` Cắt mí · `d)` Kết hợp (nói rõ những dịch vụ nào)

**Câu 3 — mong muốn, hỏi theo kết quả**
> Theo nhóm dịch vụ đã chọn, dùng đúng một trong ba câu dưới đây:
> - Hàm mặt: *"Chị muốn khuôn mặt nhìn thon hơn ở phần góc hàm, gò má, hay muốn cằm cân đối hơn?"*
> - Nâng mũi: *"Chị muốn sống mũi cao và thanh hơn, đầu mũi gọn hơn, hay muốn nhìn nghiêng có đường nét rõ hơn?"*
> - Cắt mí: *"Chị muốn nếp mí rõ tự nhiên, mí sâu hơn, hay ưu tiên giữ dáng mắt hiện tại nhưng nhìn tỉnh táo hơn?"*

⛔ Không hỏi *"giảm góc hàm bao nhiêu độ"*, *"nâng sống mũi bao nhiêu milimet"* — khách không trả lời được, và một con số trả lời bừa sẽ thành đầu vào sai cho cả dây chuyền.

---

## Tin nhắn xin ảnh — gửi cho khách
Khách thiếu ảnh → dùng đoạn này, chỉnh giọng theo từng khách:

```
Để em dựng bản mô phỏng đúng với gương mặt mình, chị giúp em 3 tấm ảnh này nhé:

1. Ảnh chính diện — mặt hướng thẳng vào camera, đầu không nghiêng, mắt nhìn thẳng.
2. Ảnh nghiêng 90° — xoay hẳn một bên, thấy rõ đường trán – mũi – môi – cằm.
3. Ảnh nghiêng 45° — xoay khoảng một nửa, vẫn thấy được cả hai mắt.

Mấy lưu ý nhỏ giúp bản mô phỏng chính xác hơn:
- Chụp ở nơi sáng đều, tránh ngược sáng.
- Không dùng filter hay app làm đẹp, vì filter đổi tỉ lệ gương mặt.
- Vén tóc khỏi vùng má và hàm, tháo kính.
- Biểu cảm thư giãn, không cười lớn.

Ảnh của chị chỉ dùng để dựng bản mô phỏng cho riêng chị. Chị xác nhận giúp em là
mình đồng ý cho bên em xử lý ảnh với mục đích này nhé.
```

⛔ Không hứa *"ảnh được bảo mật tuyệt đối"* nếu chưa kiểm tra cấu hình công cụ đang dùng (`FD-12` quy tắc 6).
