# FD-C — HÀM MẶT (gọt hàm · hạ gò má · trượt cằm)
> Mã bên trong: `FD-05` kiến thức & quy tắc thiết kế hàm mặt.
> ⛔ **Không dùng chung một câu lệnh "làm mặt V-line" cho cả ba dịch vụ.** Mỗi dịch vụ tác động lên một vùng khác nhau, và gộp lại là cách nhanh nhất để mất nhận diện khách.

| Mã | Nội dung | Dùng khi |
|---|---|---|
| `FD-05-ham-mat` | Module A gọt hàm · B hạ gò má · C trượt cằm · quy tắc kết hợp | `nhom_dich_vu = Hàm mặt` |

---

# FD-05 — HÀM MẶT
Version 1.0 · Cập nhật 2026-10-23

## 1. MODULE A — GỌT HÀM

### A.1 Kiến thức cần có
| Hạng mục | Nội dung |
|---|---|
| Vùng quan sát | Đường viền từ vùng trước tai → góc hàm → bờ dưới cằm |
| Chính diện 0° | Chiều rộng tương đối vùng góc hàm; hình dáng đường viền hai bên |
| Góc 45° | Độ chuyển tiếp giữa vùng má và góc hàm |
| Nghiêng 90° | Đường viền hàm dưới và sự chuyển tiếp về cằm |
| Mục tiêu mô phỏng | Đường viền hàm mềm hơn · thon hơn · **hoặc giữ nét góc cạnh** theo yêu cầu |
| Giới hạn | ⛔ Không xác định được độ dày xương, cơ cắn hay mỡ dưới da chỉ từ ảnh |

### A.2 Logic thiết kế — sáu bước, không đảo
1. Chốt khách muốn **thu gọn chiều rộng góc hàm** hay muốn **đường viền mềm mại hơn**. Hai thứ này khác nhau.
2. Quan sát phần rộng nổi bật ở **góc hàm**, ở **vùng má**, hay **cả hai**.
3. Khoanh vùng thay đổi, giới hạn ở **đường viền hàm dưới**.
4. Mô phỏng **M1 (nhẹ) trước**. Chỉ lên M2/M3 khi khách yêu cầu và xác nhận.
5. Đối chiếu cả 0°, 45° và 90°.
6. Kiểm tra cằm, môi, mũi, mắt và nhận diện có bị thay đổi ngoài ý muốn không.

### A.3 Vùng mở / vùng khoá
| ✅ Vùng MỞ | ⛔ Vùng KHOÁ |
|---|---|
| Đường viền góc hàm | Cằm (hình dáng, chiều dài, độ nhọn) |
| Bờ dưới hàm | Gò má |
| Chuyển tiếp góc hàm → cằm | Thái dương · trán · má trên |
| | Mắt · mũi · môi · tai · chân tóc |

**Được phép:** mô phỏng đường viền góc hàm thon hơn · chuyển tiếp mềm hơn từ góc hàm về cằm · tạo **hai mức độ** cho khách so sánh.

**Không được phép:**
- ⛔ Tự làm cằm nhọn hoặc kéo dài cằm khi khách chỉ yêu cầu gọt hàm.
- ⛔ Thu nhỏ cả thái dương, má và trán.
- ⛔ Xoá đường nét tự nhiên khiến khuôn mặt mất nhận diện.
- ⛔ Khẳng định ảnh mô phỏng phản ánh chính xác phần xương có thể loại bỏ.

---

## 2. MODULE B — HẠ GÒ MÁ

### B.1 Kiến thức cần có
| Hạng mục | Nội dung |
|---|---|
| Vùng quan sát | Phần nhô hai bên vùng gò má |
| Chính diện 0° | Chiều rộng tương đối vùng gò má và sự cân đối hai bên |
| Góc 45° | Độ nhô nhìn thấy của gò má; chuyển tiếp má – thái dương |
| Nghiêng 90° | **Chỉ tham khảo** — góc này không thể hiện đầy đủ hai bên gò má |
| Mục tiêu mô phỏng | Vùng gò má nhìn mềm hơn, hoặc giảm cảm giác nhô ngang |
| Giới hạn | ⛔ Không suy ra vị trí, độ dày hay cấu trúc cung gò má từ ảnh thông thường |

### B.2 Logic thiết kế
1. Chốt khách muốn **giảm cảm giác gò má rộng**, **giảm độ nổi bật**, hay chỉ muốn **tổng thể mềm mại**.
2. Ưu tiên quan sát **0° và 45°** (không phải 90°).
3. Chỉ thay đổi vùng gò má theo yêu cầu.
4. Giữ nguyên mắt, thái dương, mũi, đường nét nhận diện.
5. Đảm bảo má **không lõm sâu** và không mất thể tích một cách giả tạo.
6. Đối chiếu các góc: tránh trường hợp chính diện nhìn hẹp hơn nhưng góc 45° lại mất hài hoà.

### B.3 Vùng mở / vùng khoá
| ✅ Vùng MỞ | ⛔ Vùng KHOÁ |
|---|---|
| Độ nhô vùng gò má | Thái dương |
| Chuyển tiếp má – thái dương (mức nhẹ) | Chiều rộng góc hàm |
| | Cằm · mắt · mũi · môi |

**Bốn lỗi AI phải tránh ở module này:** làm gò má biến mất hoàn toàn · làm thái dương rộng bất thường · tạo vùng má lõm · thay đổi luôn chiều rộng hàm dù khách chỉ yêu cầu hạ gò má.

---

## 3. MODULE C — TRƯỢT CẰM

### C.1 Kiến thức cần có
| Hạng mục | Nội dung |
|---|---|
| Vùng quan sát | Từ dưới môi dưới đến điểm thấp nhất của cằm |
| Chính diện 0° | Chiều rộng, hình dáng và tính cân đối của cằm |
| Góc 45° | Chuyển tiếp giữa cằm và hai bên đường viền hàm |
| Nghiêng 90° | Độ nhô tương đối của cằm so với môi và mũi |
| Mục tiêu mô phỏng | Cằm cân đối hơn · mềm hơn · rõ nét hơn · hoặc đổi hình dáng theo yêu cầu |
| Giới hạn | ⛔ Ảnh không xác định được cấu trúc xương, khớp cắn, vị trí chân răng hay chỉ định phẫu thuật |

### C.2 Logic thiết kế
1. Hỏi khách quan tâm **chiều dài**, **độ nhô**, **chiều rộng** hay **hình dáng** cằm. Bốn hướng khác nhau.
2. Phân tích ảnh chính diện **và** ảnh nghiêng — module này bắt buộc có ảnh 90°.
3. Chỉ điều chỉnh cằm. ⛔ Không thay đổi mũi hoặc môi để "tạo ra" một tỉ lệ mong muốn.
4. Tạo phương án nhẹ; thêm phương án rõ nét hơn nếu khách đồng ý.
5. Kiểm tra cằm có trở nên quá nhọn, quá dài, mất tự nhiên.
6. **Gắn cảnh báo bắt buộc:** phương án trượt cằm thực tế cần bác sĩ đánh giá **khớp cắn** và cấu trúc hàm mặt.

### C.3 Vùng mở / vùng khoá
| ✅ Vùng MỞ | ⛔ Vùng KHOÁ |
|---|---|
| Hình dáng cằm | Môi trên · môi dưới |
| Chiều dài cằm (trong giới hạn mô phỏng) | Mũi |
| Độ nhô tương đối của cằm | Góc hàm · gò má |
| | Mắt · chân tóc |

---

## 4. QUY TẮC KẾT HỢP BA DỊCH VỤ
Khách yêu cầu **gọt hàm + hạ gò má + trượt cằm** cùng lúc → tạo **một phương án tổng thể có phân vùng rõ ràng**. ⛔ Không cộng dồn ba hiệu ứng làm nhỏ mặt quá mức — đây là đường ngắn nhất tới một khuôn mặt không còn là khách.

Bộ kiểm duyệt phải trả lời được năm câu:
1. Khu vực nào thay đổi do **gọt hàm**?
2. Khu vực nào thay đổi do **hạ gò má**?
3. Khu vực nào thay đổi do **trượt cằm**?
4. Những vùng nào được yêu cầu **giữ nguyên**?
5. Tổng thể **có còn giống khách** không?

Trả lời được cả năm câu mới phát hành. Không trả lời được câu nào → tách lại thành từng dịch vụ riêng.

⛔ Không suy ra cấu trúc xương, khớp cắn hoặc chỉ định phẫu thuật từ ảnh thông thường. Hình minh hoạ trong nhóm này chỉ thể hiện **vùng quan sát và mục tiêu thẩm mỹ** — không phải hướng dẫn cắt xương hay thông số phẫu thuật.
