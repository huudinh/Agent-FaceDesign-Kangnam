# 04 — TRIỂN KHAI TRÊN CHATGPT VÀ GEMINI

Tài liệu này dành cho phương án chạy agent **trực tiếp trên ChatGPT và Gemini** (cách A trong [`01-cai-dat.md`](01-cai-dat.md) §3) — nền tảng tự sửa ảnh, không gọi API.

> **Việc phải làm đầu tiên, trước khi cài gì:** chạy §4 — *Bài test 15 phút*. Nó trả lời câu hỏi quyết định cả dự án: **nền tảng có chịu sửa ảnh khuôn mặt khách không.** Cài xong mới phát hiện nó từ chối thì mất cả buổi.

---

## 1. Bảng so sánh — chọn gì dán vào đâu

| | **ChatGPT Custom GPT** | **Gemini Gem** |
|---|---|---|
| Ô chỉ dẫn | *Instructions* — **8.000 ký tự** | *Chỉ dẫn* — rộng hơn nhiều |
| Dùng file nào | [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) (**7.988 ký tự**, vừa khít) | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) (bản đầy đủ) |
| Số file tri thức | **20 file** | **10 file** |
| Nạp tri thức | **bản rời 13 file** — đủ chỗ | **bản gộp** — bản rời không đủ chỗ |
| Sửa ảnh | công cụ ảnh có sẵn trong ChatGPT | công cụ ảnh có sẵn trong Gemini |

**Hệ quả quan trọng:** Gemini chỉ cho 10 file nên **bắt buộc dùng bản gộp**. Sinh lại bản gộp sau mỗi lần sửa `knowledge/`:
```bash
python tools/fd.py gop
```

---

## 2. ChatGPT Custom GPT — danh sách nạp

**Instructions** → dán khối ▼▲ trong [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md).
⚠️ Bản ngắn đang ở **7.988/8.000 ký tự**. Chị thêm chữ vào là ChatGPT từ chối lưu. Muốn thêm luật riêng thì bỏ bớt một dòng khác, hoặc đưa luật đó xuống `knowledge/`.

**Knowledge (13 file)** — bản rời, đủ chỗ trong giới hạn 20:
```
knowledge/FD-A-tiep-nhan.md            prompts/module-ham-mat.md
knowledge/FD-B-ty-le-khuon-mat.md      prompts/module-nang-mui.md
knowledge/FD-C-ham-mat.md              prompts/module-cat-mi.md
knowledge/FD-D-nang-mui.md             prompts/prompt-wizard.md
knowledge/FD-E-cat-mi.md               prompts/prompt-kiem-duyet.md
knowledge/FD-F-tao-anh-kiem-duyet.md   template/checklist-kiem-duyet.md
knowledge/FD-G-giao-tiep-bao-mat.md
```

**Capabilities** — bật **image generation**; tắt **Web Browsing** (không cần, và càng ít công cụ thì agent càng ít đi lạc).

**Conversation starters**
```
/wizard — mở một ca mô phỏng mới
```
```
Khách gửi 3 ảnh, muốn xem thử nếu gọt hàm thì mặt thế nào
```

---

## 3. Gemini Gem — danh sách nạp

**Chỉ dẫn** → dán khối ▼▲ trong [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) (bản đầy đủ — Gemini không bó 8.000 ký tự).

**Knowledge (7 file)** — vừa trong giới hạn 10, còn dư 3 chỗ cho tài liệu riêng của chị:
```
goi/KANGNAM-FD-tri-thuc.md          ← gộp cả 7 file knowledge/
prompts/module-ham-mat.md
prompts/module-nang-mui.md
prompts/module-cat-mi.md
prompts/prompt-wizard.md
prompts/prompt-kiem-duyet.md
template/checklist-kiem-duyet.md
```
⛔ Đừng sửa tay `goi/KANGNAM-FD-tri-thuc.md` — lần `python tools/fd.py gop` tiếp theo sẽ ghi đè. Sửa ở `knowledge/` rồi gộp lại.

**Lưu ý quota:** Gemini có hạn mức lưu trữ hoạt động riêng (chat + file + Gem). Đầy thì báo *"Delete data to upload file"* — phải xoá hội thoại cũ hoặc Gem không dùng.

---

## 4. ⚠️ Bài test 15 phút — làm TRƯỚC khi cài

Cả ChatGPT và Gemini đều có chính sách **từ chối tạo/sửa ảnh người nhận diện được**. Thực tế hai công cụ này **vẫn sửa được ảnh do người dùng tải lên**, nhưng mức độ từ chối không ổn định — Gemini có trường hợp nhầm mặt khách thường thành người nổi tiếng rồi từ chối thẳng.

Đây là **rủi ro vận hành số 1** của phương án chạy trên nền tảng tiêu dùng, không phải rủi ro về prompt. Prompt viết hay cỡ nào cũng không gỡ được một lời từ chối.

**Test bằng ảnh nhân sự nội bộ đã đồng ý, ⛔ không dùng ảnh khách.**

| # | Việc | Đạt là gì |
|---|---|---|
| 1 | Tải 1 ảnh chính diện lên chat thường (chưa cần Gem/GPT), dán câu lệnh ở [`prompts/module-ham-mat.md`](../prompts/module-ham-mat.md) §3 | Trả về ảnh đã sửa, không từ chối |
| 2 | Lặp lại trên **Gem / Custom GPT** vừa tạo | Vẫn trả về ảnh — công cụ ảnh **có chạy bên trong** Gem/GPT |
| 3 | So ảnh trước–sau: che vùng đã sửa đi, nhìn phần còn lại | Phần không được sửa **không đổi** → qua ô B1 |
| 4 | Chạy cùng câu lệnh cho cả 3 góc | Ba góc đổi **nhất quán** → qua ô C4 |
| 5 | Nhìn trán, cổ, phông nền ở ảnh sau | Không sáng hơn, không mịn hơn ảnh gốc → qua ô D3 |
| 6 | Thử ảnh của 3 người khác nhau | Không ai bị từ chối vì "người nhận diện được" |

**Đọc kết quả:**
- **Trượt bước 1 hoặc 2** → nền tảng không dùng được cho việc này. Chuyển sang **cách B** (`tools/fd.py render` gọi API) — xem [`01-cai-dat.md`](01-cai-dat.md) §3.
- **Trượt bước 3 hoặc 4** → đây là giới hạn của công cụ ảnh, không phải của prompt. Ghi nhận và tính vào tỉ lệ tạo lại khi lên kế hoạch nhân sự.
- **Trượt bước 6 lác đác** → chuẩn bị sẵn kịch bản cho nhân viên khi gặp từ chối, và đừng hứa thời gian trả ảnh với khách.

---

## 5. Ba việc nền tảng KHÔNG làm thay — vẫn cần `tools/fd.py`

Kể cả khi chạy thuần ChatGPT/Gemini, ba việc dưới đây không giao cho mô hình được:

| Việc | Vì sao không để AI làm | Lệnh |
|---|---|---|
| **In nhãn tiếng Việt lên ảnh** | Mô hình ảnh viết chữ tiếng Việt có dấu rất hay sai, và nhãn sai chính tả còn tệ hơn không có nhãn | `python tools/fd.py nhan anh.jpg` |
| **Ghép ảnh so sánh trước–sau** | Để mô hình ghép thì nó sẽ tiện tay chỉnh luôn ảnh gốc → trượt ô **D1** | `python tools/fd.py ghep goc.jpg mo-phong.jpg` |
| **Xuất phiếu bàn giao** | Cần đúng cấu trúc để bác sĩ và tư vấn viên đọc nhanh | `python tools/fd.py phieu phieu.json -o phieu.md` |

Luồng thực tế:
```
Gem/GPT: phân tích → phiếu → tạo ảnh mô phỏng (tải ảnh về máy)
   ↓
fd.py nhan  → in nhãn lên ảnh mô phỏng
fd.py ghep  → ghép ảnh so sánh từ ẢNH GỐC + ảnh mô phỏng
   ↓
người: rà 19 ô template/checklist-kiem-duyet.md
   ↓
đạt → fd.py phieu → bàn giao
```

**Watermark của nền tảng:** ảnh Gemini sửa ra có gắn SynthID (watermark ẩn), và có thể kèm watermark hiện. Watermark hiện của Google **không thay thế** nhãn tiếng Việt bắt buộc — khách Việt phải đọc được *"Ảnh mô phỏng AI – không phải kết quả phẫu thuật thực tế"*, nên vẫn chạy `fd.py nhan`.

---

## 6. ⚠️ Tài khoản và dữ liệu — việc phải chốt trước khi có ảnh khách

Đây là phần `FD-12`, và chạy trên nền tảng tiêu dùng thì nó gắt hơn chạy qua API.

**ChatGPT**
- Tài khoản **Plus cá nhân**: cần vào *Settings → Data controls* tắt *"Improve the model for everyone"*. ⛔ Không coi là xong — đây là cài đặt một người bấm, người khác dùng tài khoản khác thì lại khác.
- **Business / Enterprise**: mặc định không dùng dữ liệu để huấn luyện, có quản trị tập trung. Đây là thứ nên mua nếu đưa ảnh khách thật vào.
- Custom GPT **chia sẻ cho người khác** → người dùng đó tải ảnh khách lên bằng tài khoản của họ. Cài đặt dữ liệu của họ, chị không kiểm soát được.

**Gemini**
- Tài khoản **cá nhân**: tắt *Gemini Apps Activity*.
- **Google Workspace**: dữ liệu nằm trong phạm vi hợp đồng Workspace, quản trị tập trung được.

**Ba việc chốt trước, không có ngoại lệ:**
1. Chốt **loại tài khoản** dùng chung cho cả đội — không để mỗi người một tài khoản cá nhân.
2. Chốt **chính sách lưu trữ**: ảnh gốc và ảnh mô phỏng lưu ở đâu · ai xem được · giữ bao lâu · xoá thế nào · làm gì khi khách rút lại đồng ý.
3. Soạn **câu xin đồng ý**, tách riêng đồng ý *mô phỏng* và đồng ý *đăng tải*. Đồng ý mô phỏng ≠ đồng ý đăng.

⛔ Chưa xong ba việc này thì chỉ chạy bằng ảnh nhân sự nội bộ.

---

## 7. Hai điều khác nhau giữa hai nền tảng cần nhớ khi vận hành

**① Ba góc = ba lần sửa riêng.** Trên cả hai nền tảng, mỗi ảnh là một lượt sửa độc lập — mô hình không "nhớ" nó đã làm gì ở góc trước. Vì vậy ô **C4 (các góc mâu thuẫn)** sẽ trượt nhiều hơn chị nghĩ.
Cách giảm: tải **cả ba ảnh trong một lượt** và yêu cầu sửa cùng một mức, thay vì ba lượt tách rời. Vẫn phải kiểm C4 bằng mắt.

**② Bản ngắn trên ChatGPT trông cậy vào Knowledge.** `SYSTEM-PROMPT-NGAN.md` đã cắt bảng chi tiết. Không nạp đủ 13 file thì agent sẽ bắt đầu **đoán vùng nào được sửa** — và đó đúng là chỗ sinh ra gần như mọi lỗi của nhóm agent này.
Gemini dùng bản đầy đủ nên ít rủi ro hơn ở điểm này, bù lại phải dùng bản gộp nên tra cứu thô hơn.

---

## 8. Nên chạy cả hai hay chọn một?

Chạy cả hai thì có cái để so — nhưng chỉ nên so **trong giai đoạn 2** (`FD-10` mục 2), bằng cùng một bộ ảnh nhân sự nội bộ, cùng một phiếu thiết kế, rồi chấm bằng cùng 19 ô của cổng B.

Vào vận hành thật thì **chốt một nền tảng cho một dịch vụ**. Hai nền tảng cho cùng một dịch vụ nghĩa là hai chất lượng ảnh khác nhau gửi cho hai khách giống nhau, và không ai trả lời được vì sao.
