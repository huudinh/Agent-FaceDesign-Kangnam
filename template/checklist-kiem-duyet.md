# CHECKLIST KIỂM DUYỆT — in ra, tick tay
> Cổng A (7 ô) chạy **trước khi tạo ảnh**. Cổng B (19 ô) chạy **trước khi phát hành**.
> **Trượt một ô = không phát hành.** Checklist là công cụ vận hành, không thay thế đánh giá y khoa.

```
PHIẾU : FD-________-______-v__      NGÀY : ____/____/______
KHÁCH : ______________  DỊCH VỤ : ______________  MỨC : M__
NGƯỜI DỰNG : ______________  NGƯỜI KIỂM DUYỆT : ______________
```
⚠️ Người kiểm duyệt nên **khác** người dựng ảnh.

---

## CỔNG A — ẢNH ĐẦU VÀO (trước khi tạo ảnh)
```
[ ] A1  Đủ 3 góc chụp: 0° · 45° · 90°
[ ] A2  Nhận ra cùng một khách hàng ở cả 3 ảnh
[ ] A3  Vùng cần thiết kế không bị che khuất (tóc, kính, tay, trang điểm dày)
[ ] A4  Không có filter / hiệu ứng làm đổi tỉ lệ khuôn mặt
[ ] A5  Không sai lệch tư thế quá lớn giữa các góc
[ ] A6  Độ nét đủ để quan sát đường viền vùng cần thiết kế
[ ] A7  Khách đã đồng ý cho xử lý ảnh theo mục đích đã thông báo
```
**A7 trượt → DỪNG HOÀN TOÀN.** Không bản thử nghiệm, không ngoại lệ.
**A1 trượt** → nói rõ thiếu góc nào, xin bổ sung. ⛔ Không tự dựng góc thiếu.

---

## CỔNG B — TRƯỚC KHI PHÁT HÀNH

### A. Đúng yêu cầu
```
[ ] A1  Đúng dịch vụ khách chọn
[ ] A2  Đúng vùng cần thay đổi (đối chiếu allow-list `vung_mo` trong phiếu)
[ ] A3  Đúng mức độ và phong cách khách đã xác nhận
[ ] A4  Không tự thêm dịch vụ hoặc thay đổi vùng khác
```

### B. Giữ nhận diện
```
[ ] B1  Vẫn nhận ra cùng một khách hàng
        → cách chấm: CHE vùng đã sửa đi, so phần còn lại
[ ] B2  Giữ nguyên mắt, môi, trán và các vùng không chỉnh sửa
[ ] B3  Không đổi tuổi biểu hiện hoặc đặc điểm cá nhân (nốt ruồi, sẹo, tàn nhang)
```

### C. Đúng hình thể
```
[ ] C1  Không méo đường viền khuôn mặt
[ ] C2  Không có lỗi mắt, mũi, miệng, tai
[ ] C3  Các vùng tiếp giáp tự nhiên, không thấy đường ghép
[ ] C4  Các góc nhìn không mâu thuẫn rõ rệt
        → 0° thấy đổi mà 45° như cũ = trượt (lỗi hay gặp khi chạy 3 góc rời)
```

### D. Công bằng khi so sánh
```
[ ] D1  Ảnh gốc được giữ nguyên, không chỉnh gì
[ ] D2  Góc chụp và biểu cảm tương đương giữa ảnh trước và ảnh sau
[ ] D3  Ánh sáng và chất lượng ảnh không tạo lợi thế giả
        → cách chấm: nhìn VÙNG KHÔNG ĐƯỢC SỬA (trán, cổ, phông nền).
          Sáng hơn / mịn hơn / bớt nhiễu hơn ảnh gốc = trượt
[ ] D4  Nhãn mô phỏng rõ ràng, IN TRÊN ảnh, không bị crop mất
```

### E. Bảo mật và bàn giao
```
[ ] E1  Đã xác nhận sự đồng ý xử lý ảnh
[ ] E2  Không lộ thông tin cá nhân không cần thiết (dùng mã khách, không tên thật)
[ ] E3  Có trạng thái kiểm duyệt và số phiên bản trong phiếu
[ ] E4  Đã lưu đúng nơi, theo chính sách lưu trữ
```

---

## KẾT LUẬN
```
TỔNG : ĐẠT ___/19

[ ] ĐẠT 19/19  → phát hành, in đầu ra 8 mục
[ ] TRƯỢT      → Ô trượt : ______________________________
                 Nhìn thấy gì : ________________________________________
                 Mã lỗi : ____________  Hành động : ____________________
                 Phiên bản tiếp : FD-________-______-v__
```

**Ghi được "nhìn thấy gì" thì lần tạo lại mới sửa đúng chỗ.** Ghi *"ảnh chưa tự nhiên"* thì lần sau vẫn trượt đúng ô đó.

---

## BẢNG MÃ LỖI → HÀNH ĐỘNG
| Mã | Lỗi | Hành động |
|---|---|---|
| `E01` | Sai vùng thay đổi | Tạo lại với phạm vi hẹp hơn |
| `E02` | Thay đổi nhận diện | ⛔ Huỷ bản lỗi · tạo lại **từ ảnh gốc** |
| `E03` | Lỗi giải phẫu do AI | ⛔ Không phát hành · tạo lại hoặc kiểm duyệt thủ công |
| `E04` | Sai góc nhìn | Xin ảnh đúng góc, hoặc thiết kế lại từ ảnh đủ chuẩn |
| `E05` | Mức độ quá mạnh | Về phương án nhẹ hơn, xác nhận lại với khách |
| `E06` | Khách không thích phương án | Hỏi **cụ thể** điều khách muốn đổi, tạo bản mới |
| `E07` | Ảnh không đủ thông tin | Tạm dừng, xin bổ sung ảnh |
| `E08` | Khách yêu cầu kết luận phẫu thuật | Chuyển bác sĩ đánh giá |

⛔ **Không sửa đè lên ảnh đã lỗi.** Mỗi vòng sửa trên một bản đã sai dồn thêm sai lệch và khuôn mặt trượt xa khách dần. Quay về ảnh gốc.
