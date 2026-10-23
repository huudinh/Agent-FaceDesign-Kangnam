# PROMPT MODULE — HÀM MẶT (gọt hàm · hạ gò má · trượt cằm)
> Dùng **sau** khi system prompt chung đã nạp và **sau** khi phiếu thiết kế đã được duyệt (`SYSTEM-PROMPT.md` §7).
> Tri thức nền: [`knowledge/FD-C-ham-mat.md`](../knowledge/FD-C-ham-mat.md).

---

## 1. Prompt nghiệp vụ — dán vào chat khi mở việc

```
Tạo ảnh mô phỏng thẩm mỹ hàm mặt dựa trên ảnh gốc của khách hàng đã được cung cấp.

Trước khi tạo ảnh, xác định chính xác dịch vụ được chọn: gọt hàm, hạ gò má hoặc trượt cằm.

Giữ nguyên danh tính và mọi đặc điểm khuôn mặt không thuộc phạm vi chỉnh sửa.

Với gọt hàm, chỉ điều chỉnh đường viền góc hàm và bờ dưới hàm theo mục tiêu khách đã xác nhận.

Với hạ gò má, chỉ điều chỉnh cảm nhận về độ nhô và đường nét vùng gò má, tránh tạo vùng má lõm bất thường.

Với trượt cằm, chỉ điều chỉnh hình dáng cằm trong phạm vi mô phỏng, không tự ý thay đổi môi hoặc mũi.

Tạo mức thay đổi tự nhiên trước. Chỉ tăng mức độ nếu khách yêu cầu và xác nhận.

Giữ nguyên góc chụp, ánh sáng, biểu cảm và bối cảnh. Không áp dụng khuôn mặt V-line tiêu chuẩn cho tất cả khách hàng.

Không tự suy ra cấu trúc xương hoặc khả năng đạt được kết quả phẫu thuật.

Đầu ra phải có ảnh gốc, ảnh mô phỏng, ảnh so sánh trước – sau và nhãn "Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế".
```

---

## 2. Câu lệnh sửa ảnh — bản tiếng Việt có tham số

Thay `<…>` bằng giá trị trong phiếu thiết kế. Một câu lệnh cho **một ảnh một góc**; chạy lại cho từng góc, cùng tham số.

```
Chỉnh sửa ảnh đính kèm. Đây là ảnh thật của một khách hàng, góc <0° / 45° / 90°>.

CHỈ ĐƯỢC SỬA: <vùng mở — copy từ bảng vùng mở của FD-05>
MỨC ĐỘ: <M1 nhẹ / M2 vừa / M3 rõ nét> — thay đổi phải nhỏ và tin được, không cường điệu.

GIỮ NGUYÊN TUYỆT ĐỐI, không được chạm vào:
<vùng khoá — copy từ bảng vùng khoá của FD-05>
và: danh tính người trong ảnh · hình dáng mắt · môi · trán · tai · chân tóc · màu da
· nốt ruồi, sẹo, tàn nhang · độ tuổi biểu hiện · kiểu tóc · trang phục · phông nền
· góc chụp · tiêu cự · biểu cảm · hướng và cường độ ánh sáng · độ nét và nhiễu của ảnh.

KHÔNG ĐƯỢC:
- Làm đẹp toàn khuôn mặt, làm mịn da, thêm hiệu ứng trang điểm.
- Làm sáng ảnh hoặc tăng tương phản so với ảnh gốc.
- Áp một khuôn mặt V-line chuẩn lên khách.
- Tạo vùng má lõm, cằm nhọn hoặc kéo dài cằm nếu không nằm trong "CHỈ ĐƯỢC SỬA".
- Thay đổi chiều rộng thái dương, gò má hay góc hàm nếu vùng đó không nằm trong "CHỈ ĐƯỢC SỬA".
- Thay đổi khuôn mặt tới mức không còn nhận ra là cùng một người.

Nếu không thể thực hiện thay đổi mà vẫn giữ nhận diện, hãy làm thay đổi NHẸ HƠN
thay vì làm mất nhận diện.

Giữ nguyên kích thước và tỉ lệ khung ảnh gốc.
```

---

## 3. Bản tiếng Anh cho công cụ sửa ảnh

Phần lớn mô hình sửa ảnh tuân thủ tiếng Anh tốt hơn tiếng Việt. Dùng bản này khi gọi API; bản tiếng Việt ở trên để người thật đọc và duyệt.

```
Edit the attached photograph. It is a real photo of a cosmetic-surgery consultation
client, taken at <0° frontal / 45° three-quarter / 90° profile>.

EDIT ONLY: <open regions, e.g. "the mandibular angle outline and the lower jaw border">
INTENSITY: <subtle / moderate / pronounced> — keep the change small and believable.

PRESERVE EXACTLY, do not touch:
<locked regions, e.g. "chin shape and length, cheekbones, temples, forehead">
plus: the person's identity and facial recognisability · eye shape · lips · forehead
· ears · hairline · skin tone and texture · moles, scars, freckles · apparent age
· hairstyle · clothing · background · camera angle · focal length · expression
· light direction and intensity · image sharpness and grain.

DO NOT:
- Beautify the whole face, smooth the skin, or add any makeup effect.
- Brighten the image or raise contrast relative to the original.
- Impose a generic V-line face shape.
- Create hollow cheeks, a pointed chin, or a lengthened chin unless listed in EDIT ONLY.
- Alter temple width, cheekbones, or jaw width unless listed in EDIT ONLY.
- Change the face to the point it is no longer recognisably the same person.

If the requested change cannot be made while preserving recognisability,
make a SMALLER change rather than losing recognisability.

Keep the original image dimensions and aspect ratio.
```

---

## 4. Ba cấu hình `EDIT ONLY` sẵn dùng
| Dịch vụ | `EDIT ONLY` | `PRESERVE` thêm vào |
|---|---|---|
| **Gọt hàm** | the mandibular angle outline and the lower jaw border; the transition from jaw angle to chin | chin shape and length · cheekbones · temples · forehead · mid-cheek |
| **Hạ gò má** | the perceived projection and contour of the cheekbone (zygomatic) region; the cheek-to-temple transition | temple width · jaw width · chin · eyes · nose · lips |
| **Trượt cằm** | the chin shape, length and relative projection | upper and lower lips · nose · jaw angle · cheekbones · hairline |

## 5. Khi khách yêu cầu kết hợp nhiều dịch vụ
⛔ Không cộng ba `EDIT ONLY` vào một câu lệnh rồi để mô hình tự xoay xở — đó là cách mặt khách bị thu nhỏ quá mức.

**Đúng:** ghi rõ từng vùng kèm mức độ riêng, và thêm một dòng chặn tổng:
```
Treat these as three separate, bounded edits with the stated intensity for each;
do NOT compound them into an overall face-slimming effect.
Total facial width reduction must stay within the intensity stated for each region.
```
Sau đó trả lời được **năm câu** ở `FD-05` mục 4 mới được phát hành.
