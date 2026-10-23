# PROMPT MODULE — CẮT MÍ
> Dùng **sau** khi system prompt chung đã nạp và **sau** khi phiếu thiết kế đã được duyệt.
> Tri thức nền: [`knowledge/FD-E-cat-mi.md`](../knowledge/FD-E-cat-mi.md).

---

## 1. Prompt nghiệp vụ — dán vào chat khi mở việc

```
Tạo ảnh mô phỏng nếp mí từ ảnh gốc của khách hàng.

Ghi nhận mục tiêu của khách: nếp mí tự nhiên, nếp mí rõ hơn hoặc hai bên nhìn hài hòa hơn.

Chỉ điều chỉnh nếp mí trên theo yêu cầu. Giữ nguyên hình dáng mắt, góc mắt, màu mắt, lông mi, cung mày, biểu cảm và các đặc điểm không thuộc phạm vi chỉnh sửa.

Không tự động làm mắt to hơn, kéo dài đuôi mắt, nâng cung mày hoặc loại bỏ hoàn toàn các khác biệt tự nhiên giữa hai bên.

Không tạo nếp mí sâu bất thường hoặc thay đổi toàn bộ khuôn mặt.

Kiểm tra ảnh sau ở góc chính diện và góc 45°. Nếu ảnh gốc không đủ rõ, yêu cầu bổ sung ảnh.

Không chẩn đoán sụp mi, chức năng cơ nâng mi hoặc bệnh lý mắt.

Đầu ra gồm ảnh gốc, ảnh mô phỏng và ảnh so sánh trước – sau có nhãn "Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế".
```

---

## 2. Câu lệnh sửa ảnh — bản tiếng Việt có tham số

```
Chỉnh sửa ảnh đính kèm. Đây là ảnh thật của một khách hàng, góc <0° / 45°>.

CHỈ ĐƯỢC SỬA: nếp mí trên <một bên / hai bên> — độ rõ và độ cong của nếp mí
MỨC ĐỘ: <M1 nhẹ / M2 vừa / M3 rõ nét>
PHONG CÁCH: <A mí tự nhiên / B mí rõ nét / C cân đối hai bên>

GIỮ NGUYÊN TUYỆT ĐỐI, không được chạm vào:
chiều dài mắt · góc đầu mắt · góc đuôi mắt · độ mở của mắt · màu tròng mắt
· lông mi (độ dài, hướng, độ dày) · cung mày (vị trí và hình dáng)
· bọng mắt dưới · nếp nhăn vùng dưới mắt · mũi · môi · khuôn mặt tổng thể
và: danh tính người trong ảnh · màu da · nốt ruồi, sẹo · độ tuổi biểu hiện
· kiểu tóc · phông nền · góc chụp · tiêu cự · biểu cảm · ánh sáng · độ nét.

KHÔNG ĐƯỢC:
- Làm mắt to hơn, mở rộng mắt theo chiều ngang hoặc chiều dọc.
- Kéo dài đuôi mắt hoặc thay đổi hướng góc mắt.
- Nâng cung mày.
- Tạo nếp mí sâu bất thường, hoặc nếp mí có độ cong không phù hợp dáng mắt gốc.
- Ép hai mắt trở nên giống nhau hoàn toàn nếu ảnh gốc có bất đối xứng tự nhiên —
  chỉ làm hai bên hài hòa hơn trong giới hạn hiện có.
- Xóa toàn bộ da chùng hoặc bọng mỡ mí.
- Làm mịn da, làm sáng ảnh, thêm hiệu ứng trang điểm hoặc kẻ mắt.
- Thay đổi khuôn mặt tới mức không còn nhận ra là cùng một người.

Nếu không thể thực hiện thay đổi mà vẫn giữ nhận diện, hãy làm thay đổi NHẸ HƠN.
Giữ nguyên kích thước và tỉ lệ khung ảnh gốc.
```

---

## 3. Bản tiếng Anh cho công cụ sửa ảnh

```
Edit the attached photograph. It is a real photo of a cosmetic-surgery consultation
client, taken at <0° frontal / 45° three-quarter>.

EDIT ONLY: the upper eyelid crease <on one side / on both sides> —
its visibility and curve shape.
INTENSITY: <subtle / moderate / pronounced>
STYLE: <natural crease / defined crease / improved symmetry>

PRESERVE EXACTLY, do not touch:
palpebral fissure length · inner and outer canthal angles · eye aperture height
· iris colour · eyelashes (length, direction, density) · eyebrow position and shape
· lower eyelid bags · under-eye lines · nose · lips · overall face shape
plus: the person's identity and facial recognisability · skin tone · moles and scars
· apparent age · hairstyle · background · camera angle · focal length · expression
· lighting · sharpness and grain.

DO NOT:
- Enlarge the eyes, or widen the aperture horizontally or vertically.
- Lengthen the outer canthus or change canthal tilt.
- Raise the eyebrows.
- Create an unnaturally deep crease, or a crease curve that does not suit
  the client's original eye shape.
- Force the two eyes into perfect symmetry if the original shows natural asymmetry —
  only improve harmony within the existing structure.
- Remove all skin laxity or eyelid fat.
- Smooth skin, brighten the image, or add makeup/eyeliner effects.
- Change the face to the point it is no longer recognisably the same person.

If the requested change cannot be made while preserving recognisability,
make a SMALLER change. Keep the original dimensions and aspect ratio.
```

---

## 4. Yêu cầu riêng về ảnh của module này
- **0° là góc chính · 45° để đối chiếu.** Góc 90° gần như không dùng được cho nếp mí.
- Ảnh phải chụp **gần, rõ vùng mắt**, mắt nhìn thẳng, **không nhướn mày** (nhướn mày làm nếp mí hiện ra giả).
- Không đủ nét vùng mí → `E07`, dừng, xin ảnh chụp lại. ⛔ Không đoán nếp mí từ ảnh mờ.

## 5. Hai câu cấm — nhắc lại ở đây vì khách rất hay hỏi
⛔ *"Mắt sẽ to hơn."* → *"cần bác sĩ khám trực tiếp để phân biệt khe mắt hẹp do da dư hay do cơ nâng mi yếu — hai tình trạng này xử lý khác nhau."*
⛔ *"Hai bên sẽ cân đối tuyệt đối."* → *"cải thiện sự cân đối trong giới hạn cấu trúc giải phẫu của từng mắt."*
Khách có dấu hiệu bất thường cần kiểm tra → `E08`, chuyển bác sĩ. ⛔ Không chẩn đoán sụp mi từ ảnh.
