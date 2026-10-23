# FD-F — TẠO ẢNH & KIỂM DUYỆT
> **Nhóm quan trọng nhất của agent này.** Kiến thức thẩm mỹ tốt nhưng thiếu quy tắc kiểm soát ảnh thì AI vẫn tạo ra một người khác, sai góc mặt, hoặc đổi nhiều vùng không ai yêu cầu.
> Mã bên trong: `FD-08` quy tắc tạo ảnh · `FD-09` cổng kiểm duyệt B · `FD-10` thư viện mẫu & vòng học.

| Mã | Nội dung | Dùng khi |
|---|---|---|
| `FD-08-tao-anh` | 5 thành phần đầu ra · 8 luật giữ nhận diện · luật theo góc | bước B6 |
| `FD-09-cong-kiem-duyet` | checklist A–E · bảng mã lỗi E01–E08 | **bước B7 — cổng chặn** |
| `FD-10-thu-vien` | 7 mã mẫu · 4 giai đoạn triển khai | khi xây/cập nhật thư viện |

---

# FD-08 — QUY TẮC TẠO ẢNH
Version 1.0 · Cập nhật 2026-10-23

## 1. Năm thành phần của một bộ đầu ra
| # | Thành phần | Yêu cầu |
|---|---|---|
| **01** | **Ảnh gốc** | Ảnh đối chứng. ⛔ Không chỉnh đường nét khuôn mặt, không chỉnh sáng, không làm mịn da |
| **02** | **Ảnh mô phỏng sau thiết kế** | Cùng góc · cùng biểu cảm · cùng điều kiện hình ảnh với ảnh gốc |
| **03** | **Ảnh so sánh trước – sau** | Ghép đôi, **bắt buộc có nhãn** (xem mục 4) |
| **04** | **Bộ góc nhìn bổ sung** | Các góc còn lại trong 0° / 45° / 90° đã mô phỏng được |
| **05** | **Phiếu mô tả phương án** | Phiếu thiết kế — xem `template/phieu-thiet-ke.schema.json` |

Thiếu thành phần nào → ghi rõ **thiếu cái gì và vì sao**, không im lặng bỏ qua.

## 2. Tám luật giữ nhận diện — đưa vào MỌI câu lệnh tạo ảnh
1. Giữ nguyên **danh tính** và các đặc điểm nhận diện của khách.
2. Giữ hình dáng mắt, môi, trán, màu da và mọi đường nét **không thuộc vùng điều chỉnh**.
3. Giữ nguyên **độ tuổi biểu hiện** và đặc điểm cá nhân có trong ảnh gốc (nốt ruồi, vết sẹo, tàn nhang… nếu khách không yêu cầu bỏ).
4. ⛔ Không tự động làm đẹp toàn khuôn mặt.
5. ⛔ Không thay đổi giới tính biểu hiện.
6. ⛔ Không đổi kiểu tóc, trang phục, phông nền hoặc phụ kiện nếu không cần thiết.
7. ⛔ Không tạo da mịn hoàn hảo, hiệu ứng trang điểm hay ánh sáng quảng cáo khiến ảnh sau đẹp hơn ảnh trước.
8. ⛔ Không đổi góc chụp, tiêu cự hoặc biểu cảm để che đi các điểm chưa hoàn hảo.

**Quy tắc ưu tiên:** không thể vừa thực hiện thay đổi vừa giữ nhận diện → **giảm mức độ** hoặc **thiết kế lại**.
⛔ Không hy sinh tính nhất quán của khuôn mặt để đổi lấy một bức ảnh đẹp hơn.

## 3. Bảy luật tạo ảnh
1. Luôn **chỉnh sửa từ ảnh thật của khách**, không sinh ảnh mới từ mô tả.
2. Ảnh sau cùng góc nhìn, biểu cảm, điều kiện hình ảnh với ảnh gốc.
3. ⛔ Không thay đổi vùng không được yêu cầu (đối chiếu bảng vùng mở/vùng khoá của module).
4. ⛔ Không tạo thêm chi tiết giải phẫu giả.
5. ⛔ Không dùng ảnh tham khảo của người khác thay cho khuôn mặt khách.
6. ⛔ Không tự dựng ảnh trước **và** ảnh sau như thể cả hai là ảnh chụp thực tế.
7. ⛔ Không khẳng định mô phỏng thể hiện chính xác kết quả phẫu thuật.

## 4. Nhãn bắt buộc
Mọi ảnh mô phỏng và mọi ảnh so sánh **phải có nhãn in trên ảnh**:

```
Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế
```

Nhãn phải đọc được khi ảnh bị nén hoặc chụp lại màn hình. Không đặt nhãn ở vị trí dễ bị crop mất. ⛔ Không chỉ ghi nhãn trong tin nhắn rồi để ảnh trần — ảnh sẽ bị forward tách khỏi tin nhắn.

## 5. Ba mức độ — luôn bắt đầu từ M1
| Mã | Mức | Dùng khi |
|---|---|---|
| **M1** | Nhẹ | **Mặc định cho mọi ca.** Luôn tạo M1 trước |
| **M2** | Vừa | Khách xem M1 rồi yêu cầu rõ hơn |
| **M3** | Rõ nét | Khách yêu cầu **và** xác nhận; kèm lưu ý cần bác sĩ đánh giá |

⛔ Không nhảy thẳng vào M3 dù khách nói *"làm thật rõ cho em xem"* — M1 trước, có cái để so, rồi mới lên mức.

## 6. Luật theo từng góc
| Góc | Vai trò | Lỗi phải kiểm |
|---|---|---|
| **0°** | Cân đối hai bên · chiều rộng mặt · mũi · mí | Lệch trục · đổi chiều rộng ngoài yêu cầu |
| **45°** | Chuyển tiếp giữa các vùng · hài hoà tổng thể | Biến dạng má, mũi, cằm, góc hàm |
| **90°** | Đường nét trước–sau · độ nhô tương đối | Sai đường viền · đổi môi/cằm không yêu cầu |

⚠️ Ảnh gốc và ảnh sau **không cùng góc chụp** → ⛔ không được trình bày như một phép so sánh trực tiếp chính xác.
⛔ Không tự dựng một ảnh nghiêng mới rồi gắn nhãn là **ảnh gốc thật**.

## 7. Luật tích luỹ sai lệch — quay về ảnh gốc
Ảnh mô phỏng bị lỗi → ⛔ **không tiếp tục yêu cầu AI sửa trên ảnh lỗi đó.** Mỗi vòng sửa đè lên một bản đã sai sẽ dồn thêm sai lệch và khuôn mặt trượt xa khách dần.

**Đúng:** quay lại **ảnh gốc**, thu hẹp vùng thay đổi, hạ mức độ, tạo lại từ đầu.

---

# FD-09 — CỔNG KIỂM DUYỆT (CỔNG B)
Cơ chế **Quality Gate**: ảnh chỉ được trả cho khách sau khi vượt **toàn bộ** các ô dưới đây. Trượt một ô = **không phát hành**.

## 1. Checklist năm nhóm

**A. Đúng yêu cầu**
```
[ ] A1 Đúng dịch vụ khách chọn
[ ] A2 Đúng vùng cần thay đổi
[ ] A3 Đúng mức độ và phong cách khách đã xác nhận
[ ] A4 Không tự thêm dịch vụ hoặc thay đổi vùng khác
```

**B. Giữ nhận diện**
```
[ ] B1 Vẫn nhận ra cùng một khách hàng
[ ] B2 Giữ nguyên mắt, môi, trán và các vùng không chỉnh sửa
[ ] B3 Không đổi tuổi biểu hiện hoặc đặc điểm cá nhân
```

**C. Đúng hình thể**
```
[ ] C1 Không méo đường viền khuôn mặt
[ ] C2 Không có lỗi mắt, mũi, miệng, tai
[ ] C3 Các vùng tiếp giáp tự nhiên
[ ] C4 Các góc nhìn không mâu thuẫn rõ rệt
```

**D. Công bằng khi so sánh**
```
[ ] D1 Ảnh gốc được giữ nguyên
[ ] D2 Góc chụp và biểu cảm tương đương
[ ] D3 Ánh sáng và chất lượng ảnh không tạo lợi thế giả
[ ] D4 Có nhãn mô phỏng rõ ràng, in trên ảnh
```

**E. Bảo mật và bàn giao**
```
[ ] E1 Đã xác nhận sự đồng ý xử lý ảnh
[ ] E2 Không lộ thông tin cá nhân không cần thiết
[ ] E3 Có trạng thái kiểm duyệt và số phiên bản
[ ] E4 Đã lưu đúng nơi, theo chính sách lưu trữ
```

Checklist này là **công cụ vận hành**, không thay thế đánh giá y khoa.

## 2. Bảng mã lỗi → hành động
| Mã | Lỗi phát hiện | Hành động |
|---|---|---|
| **E01** | Sai vùng thay đổi | Tạo lại với phạm vi hẹp hơn |
| **E02** | Thay đổi nhận diện | ⛔ Huỷ bản lỗi · tạo lại **từ ảnh gốc** |
| **E03** | Lỗi giải phẫu do AI | ⛔ Không phát hành · tạo lại hoặc chuyển kiểm duyệt thủ công |
| **E04** | Sai góc nhìn | Yêu cầu ảnh đúng góc, hoặc thiết kế lại từ ảnh đủ chuẩn |
| **E05** | Mức độ quá mạnh | Quay về phương án nhẹ hơn và xác nhận lại với khách |
| **E06** | Khách không thích phương án | Hỏi **cụ thể** điều khách muốn đổi rồi tạo phiên bản mới |
| **E07** | Ảnh không đủ thông tin | Tạm dừng · yêu cầu bổ sung ảnh |
| **E08** | Khách yêu cầu kết luận phẫu thuật | Chuyển bác sĩ đánh giá |

---

# FD-10 — THƯ VIỆN MẪU VÀ VÒNG HỌC

## 1. Bảy mã mẫu khởi đầu
⛔ **Không chỉ lưu ảnh đẹp.** Thư viện phải có cấu trúc để trợ lý học cách **tuân thủ yêu cầu**, không phải học cách làm mặt đẹp.

| Mã mẫu | Dịch vụ | Phong cách | Mục tiêu | Tiêu chí đạt |
|---|---|---|---|---|
| `HM-01` | Gọt hàm | Tự nhiên | Đường viền hàm mềm hơn | Giữ cằm và gò má |
| `HM-02` | Hạ gò má | Tự nhiên | Giảm cảm giác nhô ngang | Giữ thái dương, không làm má lõm |
| `HM-03` | Trượt cằm | Thanh thoát | Cằm cân đối hơn | Không tự đổi mũi, môi |
| `NM-01` | Nâng mũi | Tự nhiên | Sống mũi rõ vừa phải | Giữ nhận diện và đầu mũi tự nhiên |
| `NM-02` | Nâng mũi | Rõ nét | Đường nét mũi nổi bật hơn | Không làm mũi cực đoan |
| `MM-01` | Cắt mí | Tự nhiên | Nếp mí rõ vừa phải | Giữ hình dáng mắt |
| `MM-02` | Cắt mí | Cân đối | Nếp mí hai bên hài hoà | Không phóng đại độ mở mắt |

Mỗi mẫu phải có đủ **năm** thứ: ảnh gốc **được phép sử dụng** · ảnh mô phỏng · **prompt đã dùng** · đánh giá của người kiểm duyệt · **lỗi cần tránh**.
⛔ Không dùng ảnh khách hàng làm dữ liệu huấn luyện lại nếu chưa có sự đồng ý phù hợp cho mục đích đó.

## 2. Bốn giai đoạn triển khai
| Giai đoạn | Việc | Đầu ra |
|---|---|---|
| **1. Xây kho chuẩn** | Chỉ dùng nội dung chuyên môn **đã được bác sĩ phụ trách thẩm định**. ⛔ Không lấy tỉ lệ thẩm mỹ chưa có nguồn làm tiêu chuẩn cứng | Kho FD-01…FD-10 đã duyệt |
| **2. Chuẩn hoá bộ ảnh mẫu** | Thử nghiệm riêng theo dịch vụ, góc chụp, mức độ, điều kiện ảnh | Bộ ảnh được phép dùng + prompt tương ứng + kết quả đã đánh giá |
| **3. Kiểm thử với khách thật** | Bác sĩ đánh giá chuyên môn · thiết kế đánh giá hình ảnh · CSKH đánh giá khả năng khách hiểu | Báo cáo chất lượng · danh sách lỗi · quy tắc cần sửa |
| **4. Vận hành** | Theo dõi tỉ lệ ảnh đạt chuẩn, số lần tạo lại, thời gian xử lý, tỉ lệ khách xác nhận đúng ý, số ca cần bác sĩ can thiệp | SOP · phân quyền · dashboard · quy trình bàn giao |

## 3. Ba tài liệu bác sĩ phải duyệt trước khi mở rộng
1. **Bộ tiêu chí thẩm mỹ được phép sử dụng** — các mốc quan sát, nguyên tắc hài hoà, và những nội dung AI **không được** kết luận.
2. **Bộ ảnh chuẩn theo từng dịch vụ** — ảnh đầu vào, ảnh mô phỏng đạt, ảnh lỗi và **lý do lỗi**.
3. **Bộ quy tắc thay đổi hình ảnh** — vùng được phép chỉnh, vùng phải giữ nguyên, mức độ, và tiêu chí loại bỏ ảnh.

Ba tài liệu này quyết định chất lượng trợ lý. **Prompt chỉ là lớp hướng dẫn** — độ ổn định thực tế còn phụ thuộc công cụ tạo ảnh, chất lượng ảnh đầu vào và quá trình kiểm thử.
