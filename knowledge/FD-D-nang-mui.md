# FD-D — NÂNG MŨI
> Mã bên trong: `FD-06` kiến thức & quy tắc thiết kế nâng mũi.

| Mã | Nội dung | Dùng khi |
|---|---|---|
| `FD-06-nang-mui` | 6 vùng quan sát · ánh xạ yêu cầu → vùng mở · 3 phong cách · 7 lỗi phải loại |

---

# FD-06 — NÂNG MŨI
Version 1.0 · Cập nhật 2026-10-23

## 1. Sáu vùng quan sát theo ba góc
| Vùng | Chính diện 0° | Nghiêng 90° | Góc 45° |
|---|---|---|---|
| **Gốc mũi** | Vị trí và độ rõ của gốc mũi | Điểm chuyển tiếp trán → mũi | Sự chuyển tiếp trán – sống mũi |
| **Sống mũi** | Độ thẳng, vị trí tương đối | Đường cong và độ nhô nhìn thấy | Độ nổi và đường nét sống mũi |
| **Đầu mũi** | Hình dáng, mức độ rõ nét | Độ nhô tương đối | Hình khối đầu mũi |
| **Cánh mũi** | Chiều rộng tương đối | Độ nhô ở góc nghiêng | Sự chuyển tiếp cánh mũi |
| **Trụ mũi** | Chỉ quan sát được một phần | Mức độ lộ trụ mũi trong ảnh | Tương quan với đầu mũi |
| **Mũi – môi** | Vị trí tương đối theo trục giữa | Góc mũi – môi nhìn thấy | Sự hài hoà tổng thể |

**Giới hạn cứng:** AI chỉ mô tả **đặc điểm quan sát được**. ⛔ Không kết luận tình trạng vách ngăn, chức năng hô hấp, độ dày da, độ vững sụn, hay khả năng chịu lực của mô.

## 2. Logic thiết kế

### Bước 1 — Xác định mục tiêu chính
Khách có thể chọn một hoặc nhiều:
- Sống mũi nhìn rõ hơn.
- Đường sống mũi thẳng hơn hoặc mềm mại hơn.
- Đầu mũi nhìn gọn hơn.
- Tổng thể hài hoà hơn **khi nhìn nghiêng**.
- Hình dáng cân đối hơn **khi nhìn chính diện**.
- Giữ vẻ tự nhiên, không quá cao, không quá sắc nét.

### Bước 2 — Ánh xạ yêu cầu → vùng được phép thay đổi
| Khách nói | ✅ Vùng MỞ | ⛔ Kèm theo điều KHÔNG được làm |
|---|---|---|
| *"Muốn sống mũi cao hơn"* | Sống mũi | Không đụng đầu mũi, cánh mũi |
| *"Muốn đầu mũi gọn hơn"* | Đầu mũi | Không tự thu nhỏ toàn bộ cánh mũi |
| *"Muốn nhìn nghiêng thanh thoát"* | Đường nét tổng thể của mũi | Bắt buộc đối chiếu ảnh 90° |
| *"Muốn mũi cân đối khi nhìn thẳng"* | Sống mũi + đầu mũi, trong giới hạn yêu cầu | Không đổi chiều rộng cánh mũi nếu khách không nói |
| *"Muốn cánh mũi gọn hơn"* | Chỉ vùng cánh mũi | Không tự đổi chiều cao sống mũi |
| *"Muốn mũi tự nhiên"* | Mức M1, ưu tiên giữ nhận diện | Không đẩy lên M3 |

**Vùng KHOÁ ở mọi trường hợp:** mắt · môi · cằm · trán · gò má · góc hàm · màu da · chân tóc · biểu cảm.

### Bước 3 — Sáu câu kiểm tra hình dáng
1. Sống mũi có chuyển tiếp tự nhiên với vùng trán không?
2. Đầu mũi có hài hoà với sống mũi không?
3. Mũi có cân đối với môi và cằm **ở góc nghiêng** không?
4. Nhìn chính diện, sống mũi có **lệch bất thường do lỗi tạo ảnh** không?
5. Lỗ mũi, cánh mũi, trụ mũi có bị **biến dạng giả tạo** không?
6. Mũi sau thiết kế **có còn giữ nhận diện** của khách không?

⛔ **Không có một chiều cao sống mũi, một góc mũi – môi hay một độ nhô đầu mũi "chuẩn" dùng cho mọi khách.** Thông số giải phẫu chuyên sâu chỉ được dùng khi có nguồn chuyên môn đáng tin cậy **và** có bác sĩ kiểm duyệt.

## 3. Ba phong cách trong thư viện
| Mã | Phong cách | Đặc điểm |
|---|---|---|
| **A** | **Tự nhiên** | Thay đổi nhẹ · đường sống mũi mềm · đầu mũi không quá sắc · giữ tối đa nhận diện |
| **B** | **Thanh thoát** | Đường nét rõ hơn nhưng vẫn hài hoà · chuyển tiếp đầu mũi–sống mũi tự nhiên · tôn trọng cấu trúc hiện tại |
| **C** | **Rõ nét** | Đường nét nổi bật hơn theo yêu cầu · ⛔ không tự đẩy chiều cao/độ nhô đến mức cực đoan · **cần khách xác nhận + bác sĩ đánh giá tính phù hợp** |

Đây là **phong cách hình ảnh để khách lựa chọn** — không phải loại phẫu thuật, không phải cam kết về khả năng đạt được trong thực tế.

## 4. Bảy lỗi phải loại bỏ
1. ⛔ Mũi quá cao hoặc quá sắc nét so với khuôn mặt.
2. ⛔ Sống mũi gãy khúc, méo hoặc lệch giả tạo.
3. ⛔ Đầu mũi nhọn bất thường.
4. ⛔ Cánh mũi biến dạng, lỗ mũi không đồng nhất.
5. ⛔ Thay đổi môi hoặc cằm không theo yêu cầu.
6. ⛔ Tạo ra khuôn mặt khác người ban đầu.
7. ⛔ Tạo ảnh sau với ánh sáng, biểu cảm hoặc góc chụp khác khiến kết quả trông đẹp hơn **một cách không công bằng**.

Lỗi 7 là lỗi tinh vi nhất và hay bị bỏ qua nhất: ảnh sau sáng hơn, da mịn hơn, góc đẹp hơn — khách tưởng mũi đổi, thực ra ánh sáng đổi.
