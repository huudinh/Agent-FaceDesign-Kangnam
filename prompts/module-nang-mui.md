# PROMPT MODULE — NÂNG MŨI
> Dùng **sau** khi system prompt chung đã nạp và **sau** khi phiếu thiết kế đã được duyệt.
> Tri thức nền: [`knowledge/FD-D-nang-mui.md`](../knowledge/FD-D-nang-mui.md).

---

## 1. Prompt nghiệp vụ — dán vào chat khi mở việc

```
Tạo ảnh mô phỏng nâng mũi cá nhân hóa từ ảnh gốc của khách hàng.

Trước tiên, ghi nhận mục tiêu: sống mũi rõ hơn, đầu mũi gọn hơn, đường nét nghiêng thanh thoát hơn hoặc tổng thể tự nhiên hơn.

Chỉ điều chỉnh vùng mũi theo mục tiêu đã được khách xác nhận.

Giữ nguyên hình dáng mắt, môi, cằm, trán, màu da và đặc điểm nhận diện.

Không tự động tăng chiều cao sống mũi đến mức cực đoan. Không tạo đầu mũi nhọn bất thường, sống mũi gãy khúc, lỗ mũi méo hoặc đường nét không tự nhiên.

Đối chiếu chính diện, góc 45° và góc nghiêng 90°. Nếu chỉ có ảnh ở một góc, phải nêu rõ giới hạn của mô phỏng.

Không tự suy ra cấu trúc sụn, vách ngăn hoặc chỉ định phẫu thuật.

Tạo ảnh gốc và ảnh mô phỏng với điều kiện hình ảnh tương đương. Gắn nhãn "Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế".
```

---

## 2. Câu lệnh sửa ảnh — bản tiếng Việt có tham số

```
Chỉnh sửa ảnh đính kèm. Đây là ảnh thật của một khách hàng, góc <0° / 45° / 90°>.

CHỈ ĐƯỢC SỬA: <vùng mở — lấy từ bảng ánh xạ FD-06 mục 2 bước 2>
MỨC ĐỘ: <M1 nhẹ / M2 vừa / M3 rõ nét>
PHONG CÁCH: <A tự nhiên / B thanh thoát / C rõ nét>

GIỮ NGUYÊN TUYỆT ĐỐI, không được chạm vào:
mắt · môi · cằm · trán · gò má · góc hàm · màu da · chân tóc · biểu cảm
và: danh tính người trong ảnh · nốt ruồi, sẹo, tàn nhang · độ tuổi biểu hiện
· kiểu tóc · trang phục · phông nền · góc chụp · tiêu cự · hướng và cường độ ánh sáng
· độ nét và nhiễu của ảnh.
Các vùng mũi KHÔNG nằm trong "CHỈ ĐƯỢC SỬA" cũng phải giữ nguyên
(gốc mũi · sống mũi · đầu mũi · cánh mũi · trụ mũi — chỉ sửa đúng vùng được ghi).

KHÔNG ĐƯỢC:
- Nâng sống mũi lên mức cực đoan so với khuôn mặt.
- Tạo sống mũi gãy khúc, méo hoặc lệch.
- Tạo đầu mũi nhọn bất thường.
- Làm biến dạng cánh mũi, hoặc làm hai lỗ mũi không đồng nhất.
- Thay đổi môi hoặc cằm để "tạo ra" một tỉ lệ mũi – môi – cằm mong muốn.
- Làm mịn da, làm sáng ảnh, thêm hiệu ứng trang điểm.
- Thay đổi khuôn mặt tới mức không còn nhận ra là cùng một người.

Nếu không thể thực hiện thay đổi mà vẫn giữ nhận diện, hãy làm thay đổi NHẸ HƠN.
Giữ nguyên kích thước và tỉ lệ khung ảnh gốc.
```

---

## 3. Bản tiếng Anh cho công cụ sửa ảnh

```
Edit the attached photograph. It is a real photo of a cosmetic-surgery consultation
client, taken at <0° frontal / 45° three-quarter / 90° profile>.

EDIT ONLY: <open nasal subregions, e.g. "the dorsum (bridge) line">
INTENSITY: <subtle / moderate / pronounced>
STYLE: <natural / refined / defined>

PRESERVE EXACTLY, do not touch:
eyes · lips · chin · forehead · cheekbones · jawline · skin tone and texture
· hairline · expression · the person's identity and facial recognisability
· moles, scars, freckles · apparent age · hairstyle · clothing · background
· camera angle · focal length · light direction and intensity · sharpness and grain.
Nasal subregions NOT listed in EDIT ONLY must also stay unchanged
(radix · dorsum · tip · alae · columella).

DO NOT:
- Raise the dorsum to an extreme height relative to the face.
- Create a kinked, bent or deviated dorsal line.
- Create an unnaturally pointed tip.
- Distort the alae or make the two nostrils asymmetric.
- Alter lips or chin in order to "achieve" a nose-lip-chin proportion.
- Smooth skin, brighten the image, or add makeup effects.
- Change the face to the point it is no longer recognisably the same person.

If the requested change cannot be made while preserving recognisability,
make a SMALLER change. Keep the original dimensions and aspect ratio.
```

---

## 4. Sáu cấu hình `EDIT ONLY` theo yêu cầu của khách
| Khách nói | `EDIT ONLY` |
|---|---|
| *"sống mũi cao hơn"* | the dorsum (bridge) line only |
| *"đầu mũi gọn hơn"* | the nasal tip definition only |
| *"nhìn nghiêng thanh thoát"* | the overall dorsal-to-tip profile line (requires the 90° photo) |
| *"cân đối khi nhìn thẳng"* | the dorsum and tip, within the stated intensity |
| *"cánh mũi gọn hơn"* | the alar width only |
| *"mũi tự nhiên"* | the dorsum and tip at subtle intensity, prioritising recognisability |

## 5. Góc bắt buộc
Mục tiêu *"nhìn nghiêng thanh thoát"* **bắt buộc có ảnh 90°**. Thiếu → cổng A trượt (`FD-03`), xin ảnh, không ước lượng.
Chỉ có một góc → được làm bản thử nghiệm giới hạn, và phải khai `gioi_han_mo_phong` trong phiếu: *"chỉ mô phỏng được ở góc X, chưa đối chiếu được độ nhô đầu mũi và đường nét nghiêng."*
