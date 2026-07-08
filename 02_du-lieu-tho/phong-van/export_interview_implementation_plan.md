# Nâng cấp Kịch bản Phỏng vấn Bán cấu trúc v1.0 → v2.0

## Bối cảnh

Kịch bản phỏng vấn hiện tại ([v1.0 draft](file:///d:/LogManagement/02_du-lieu-tho/phong-van/2026-07-05_kich-ban-phong-van_v1.0_draft_AI.md)) đã có cấu trúc cơ bản 5 phần (Lời chào → Warm-up → Đánh giá 14 tiêu chí → Tiêu chí ẩn → Pre-AHP) nhưng cần cải thiện trên nhiều phương diện để đạt chuẩn phỏng vấn học thuật quốc tế trước khi tiến hành phỏng vấn thực tế.

**Đánh giá hiện trạng v1.0:**

| Khía cạnh | Hiện trạng v1.0 | Vấn đề |
|---|---|---|
| Cơ sở phương pháp luận | Không trích dẫn framework nào | Thiếu tính chính danh học thuật; peer-review sẽ hỏi "interview protocol dựa trên gì?" |
| Alignment câu hỏi ↔ mục tiêu nghiên cứu | Chỉ ngầm hiểu, không tường minh | Vi phạm Phase 1 của IPR Framework (Castillo-Montoya, 2016) |
| Số lượng câu hỏi | 11 câu cho ~30-40 phút | Ít câu warm-up, thiếu probing questions |
| Kỹ thuật câu hỏi | Một số câu dẫn dắt (leading); hỏi "đúng/sai" ngầm | Dễ gây bias xác nhận (confirmation bias) |
| Tận dụng literature | Chỉ nhắc vài tác giả trong câu 4,5 | Bỏ phí 16 bài báo parsed với nhiều insight có thể biến thành stimulus |
| Phần đạo đức nghiên cứu | Có nhưng sơ sài | Thiếu quyền rút lui, cam kết thời gian, mục đích sử dụng rõ ràng |
| Cấu trúc ghi chép | Không có template ghi chép | Người phỏng vấn không có hướng dẫn ghi chú thực tế |
| Kịch bản kết thúc | 1 dòng cảm ơn | Thiếu member-checking, cơ hội bổ sung, next steps |

---

## Khung lý thuyết áp dụng

> [!IMPORTANT]
> Kịch bản v2.0 sẽ được xây dựng dựa trên **3 khung phương pháp luận** đã được nghiên cứu và xác minh từ nguồn uy tín:

### 1. Interview Protocol Refinement (IPR) Framework — Castillo-Montoya (2016)
Quy trình 4 phase chuẩn hóa thiết kế kịch bản phỏng vấn:
- **Phase 1:** Đảm bảo câu hỏi phỏng vấn khớp (align) với câu hỏi nghiên cứu → Dùng **ma trận RQ–IQ mapping**
- **Phase 2:** Thiết kế cuộc hội thoại có tính khám phá (inquiry-based conversation) → Sắp xếp câu hỏi từ dễ → khó, cụ thể → trừu tượng
- **Phase 3:** Thu thập phản hồi từ đồng nghiệp/chuyên gia về protocol → Bước này sẽ do nhóm tự thực hiện sau khi AI soạn xong
- **Phase 4:** Pilot test → Nhóm tự thực hiện trước khi phỏng vấn thật

*Nguồn: Castillo-Montoya, M. (2016). Preparing for Interview Research: The Interview Protocol Refinement Framework. The Qualitative Report, 21(5), 811-831. NSU Florida — nova.edu*

### 2. Integrated Delphi–AHP Criteria Validation — Al Hazza et al. (2022)
Phỏng vấn chuyên gia đóng vai trò **Vòng Delphi định tính** (qualitative Delphi round) nhằm:
- Cho phép chuyên gia **thêm, loại bỏ, hoặc định nghĩa lại** tiêu chí (Round 1 — Exploratory)
- Tạo cơ sở dữ liệu đồng thuận/bất đồng trước khi chuyển sang AHP định lượng (Phase 4)

*Nguồn: Al Hazza et al. (2022). An integrated approach for supplier evaluation and selection using the Delphi method and AHP. International Journal of Technology, 13(6), 1220–1230.*

### 3. Cognitive Probing Techniques — Willis (2005)
Kỹ thuật "thăm dò nhận thức" để đảm bảo chuyên gia hiểu đúng tiêu chí:
- **Paraphrasing probes:** "Anh/chị có thể diễn đạt lại tiêu chí này bằng ngôn ngữ của mình không?"
- **Process probes:** "Anh/chị đi đến nhận định đó dựa trên cơ sở nào?"
- **Recall probes:** "Anh/chị có thể cho một ví dụ thực tế từ kinh nghiệm?"

---

## Proposed Changes

### Tổng quan cấu trúc mới (v2.0 vs v1.0)

| Phần | v1.0 (11 câu) | v2.0 (dự kiến 15-17 câu + probes) | Thay đổi chính |
|---|---|---|---|
| **Phần 0** | Lời chào + Consent | Lời chào + Informed Consent đầy đủ + Bảng thông tin nghiên cứu | Thêm quyền rút lui, cam kết thời lượng, mục đích cụ thể |
| **Phần 1** | Warm-up (3 câu) | Warm-up & Profiling (3-4 câu, có probes) | Thêm câu khám phá kinh nghiệm cá nhân, giảm câu hỏi chung chung |
| **Phần 2** | Đánh giá 14 tiêu chí (4 câu) | Phản biện có kích thích (Stimulus-based Critique) (5-6 câu + probes) | Tách thành nhóm tiêu chí, sử dụng **thẻ kích thích** (stimulus cards) trích từ literature, thêm câu hỏi "tại sao" |
| **Phần 3** | Tiêu chí ẩn (2 câu) | Khám phá bối cảnh Việt Nam (2-3 câu) | Hỏi sâu hơn về contextual factors (thời tiết, văn hóa mua hàng, kênh mua) |
| **Phần 4** | Pre-AHP (2 câu) | Xếp hạng sơ bộ + Kịch bản đánh đổi (3-4 câu) | Thêm kịch bản giả lập (hypothetical trade-off scenarios) để tránh bias |
| **Phần 5** | *(không có)* | Đóng phỏng vấn đúng chuẩn | Cơ hội bổ sung, member-checking, cảm ơn |
| **Phụ lục** | *(không có)* | Ma trận RQ–IQ + Hướng dẫn ghi chép + Thẻ kích thích | Công cụ hỗ trợ cho người phỏng vấn |

---

### Chi tiết các thay đổi lớn

---

#### A. Phần 0 — Informed Consent (Cải thiện toàn diện)

**Vấn đề v1.0:** Thiếu 3 yếu tố chuẩn đạo đức nghiên cứu quốc tế: (1) Quyền rút lui bất cứ lúc nào, (2) Cam kết thời lượng cụ thể, (3) Giải thích rõ dữ liệu sẽ được sử dụng ra sao.

**Giải pháp v2.0:** Viết lại hoàn toàn lời chào theo chuẩn Informed Consent đầy đủ, bao gồm:
- Giới thiệu nghiên cứu cụ thể (tên đề tài, mục tiêu)
- Cam kết thời lượng (~20-30 phút)
- Quyền từ chối trả lời bất kỳ câu nào hoặc rút lui hoàn toàn
- Giải thích rõ dữ liệu chỉ phục vụ nghiên cứu học thuật, ẩn danh, không ghi âm
- Xin phép tường minh ("Anh/chị có đồng ý tham gia không?")

---

#### B. Phần 1 — Warm-up & Profiling (Cải thiện)

**Vấn đề v1.0:** Câu 1 quá mở ("kỳ vọng gì lớn nhất") dễ nhận câu trả lời chung chung. Câu 3 mang tính đánh giá thị trường (market assessment) hơn là khám phá hành vi.

**Giải pháp v2.0:**
- Giữ cấu trúc 3-4 câu warm-up nhưng thiết kế lại theo nguyên tắc "từ cá nhân → tổng quát" (IPR Phase 2)
- Câu mở đầu hỏi về **kinh nghiệm cá nhân cụ thể** thay vì ý kiến trừu tượng (ví dụ: "Lần gần nhất anh/chị tư vấn/mua laptop cho nhân viên văn phòng, tiêu chí nào anh/chị cân nhắc đầu tiên?")
- Thêm câu hỏi về **pain points thực tế** mà chuyên gia quan sát được
- Bổ sung **probing question mẫu** sau mỗi câu chính (ví dụ: "Anh/chị có thể cho một ví dụ cụ thể không?")

---

#### C. Phần 2 — Phản biện tiêu chí có kích thích (Thay đổi lớn nhất)

**Vấn đề v1.0:** 
1. Chỉ hỏi 4 câu cho 14 tiêu chí → thiếu chiều sâu 
2. Câu 4 (GPU) và câu 5 (Cổng kết nối) đã chứa sẵn kết luận trong câu hỏi → **leading questions** (dẫn dắt)
3. Không tận dụng được insights từ 16 bài báo đã parsed

**Giải pháp v2.0:** Chia 14 tiêu chí thành **4 nhóm** (theo cấu trúc [v5.0 criteria](file:///d:/LogManagement/03_phan-tich/tieu-chi/2026-07-05_danh-sach-tieu-chi-chinh-thuc_v5.0_final_user.md)), mỗi nhóm có 1-2 câu hỏi chính + probes:

| Nhóm | Tiêu chí | Nguồn kích thích (stimulus) từ literature |
|---|---|---|
| **Kinh tế & Ngân sách** | Giá cả | Rau & Fang (2018): Hàm thoái hóa giá trị theo thời gian; Jiménez-Parra et al. (2014): Laptop tái tạo |
| **Phần cứng cốt lõi** | CPU, RAM, Ổ cứng, GPU | Kang et al. (2022): CPU trọng số cao nhất; Maghsoudi (2026): GPU over-specification cho văn phòng |
| **Di động & Bền vững** | Pin, Trọng lượng, Độ bền, Thiết kế | Lam et al. (2023): Pin trọng số #1; Zakeri et al. (2023): Vật liệu quyết định vòng đời |
| **Trải nghiệm & Niềm tin** | Màn hình, Bàn phím, Cổng kết nối, Thương hiệu, Hậu mãi | Sönmez Çakır & Pekkaya (2020): Thương hiệu "bộ lọc"; Šostar & Ristanović (2023): Hậu mãi = bảo hiểm rủi ro |

**Kỹ thuật mới:**
- **Thẻ kích thích (Stimulus Cards):** Chuẩn bị các tấm thẻ/slide trích dẫn ngắn 1-2 câu từ bài báo (VÍ DỤ: "Theo một nghiên cứu trên PLoS One 2026, nhiệt lượng và tiếng ồn quạt tản nhiệt là mối lo ngại lớn nhất của nhân viên văn phòng"). Đọc cho chuyên gia nghe → hỏi phản hồi. Đây là kỹ thuật **elicitation** tránh leading question.
- **Cognitive probes:** Sau mỗi nhận xét quan trọng, hỏi: "Anh/chị đi đến nhận định đó dựa trên kinh nghiệm/trường hợp cụ thể nào?"
- Loại bỏ hoàn toàn các câu hỏi "đúng/sai" ngầm (implicit yes/no)

---

#### D. Phần 3 — Khám phá bối cảnh Việt Nam (Cải thiện)

**Vấn đề v1.0:** Câu 8 đã gợi ý sẵn ví dụ (webcam, bản lề, quạt) → dẫn dắt tư duy chuyên gia. Câu 9 hỏi "thêm 1 tiêu chí" quá giới hạn.

**Giải pháp v2.0:**
- Hỏi mở hơn: "Theo kinh nghiệm thực tế, có yếu tố nào đặc thù tại thị trường Việt Nam ảnh hưởng đến quyết định mua laptop mà nghiên cứu quốc tế có thể bỏ sót?" (không gợi ý)
- Bổ sung câu hỏi về **contextual factors VN:** hệ sinh thái phần mềm (Office 365 vs Google Workspace), cơ sở hạ tầng (điện, internet), kênh mua hàng (online vs offline), văn hóa "hỏi ý kiến bạn bè" (word-of-mouth)
- Không giới hạn "1 tiêu chí" → hỏi thoải mái: "Có tiêu chí nào anh/chị muốn bổ sung hoặc loại bỏ khỏi danh sách?"

---

#### E. Phần 4 — Xếp hạng & Kịch bản đánh đổi (Cải thiện)

**Vấn đề v1.0:** Câu 10 hỏi "top 3 sống còn" là tốt nhưng cách diễn đạt "tuyệt đối không được phép đánh đổi" quá cực đoan, có thể gây áp lực. Câu 11 hỏi bottom 3 tốt nhưng thiếu kịch bản trade-off.

**Giải pháp v2.0:**
- Giữ nguyên ý tưởng rank top/bottom nhưng điều chỉnh ngôn ngữ bớt cực đoan
- Thêm **2 kịch bản đánh đổi giả lập** (hypothetical trade-off):
  - Kịch bản A: "Nếu có 2 máy cùng giá, máy A pin 10 tiếng nhưng nặng 1.8kg, máy B pin 6 tiếng nhưng nhẹ 1.3kg — anh/chị sẽ khuyên khách hàng văn phòng chọn máy nào? Vì sao?"
  - Kịch bản B: "Máy A thương hiệu lớn (Dell/HP) nhưng cấu hình Core i5/8GB RAM. Máy B thương hiệu ít tên (ASUS/Acer) nhưng Core i7/16GB RAM, cùng tầm giá 22 triệu — chuyên gia thấy khách hàng thường chọn bên nào?"
- Kịch bản trade-off giúp **kích hoạt tư duy so sánh thực tế** thay vì xếp hạng lý thuyết, đồng thời cung cấp dữ liệu sơ bộ cho Phase 4 (AHP Pairwise Comparison)

---

#### F. Phần 5 — Đóng phỏng vấn (Thêm mới)

**Vấn đề v1.0:** Chỉ có 1 dòng "Cảm ơn" ở cuối. Không có cơ hội cho chuyên gia bổ sung, không có member-checking.

**Giải pháp v2.0:** Thêm Phần 5 hoàn chỉnh:
- Câu hỏi mở cuối: "Có điều gì em chưa hỏi đến mà anh/chị muốn chia sẻ thêm không?"
- **Member-checking:** Tóm tắt lại 2-3 ý chính nhất đã ghi nhận và hỏi: "Em tóm tắt lại vài ý chính, anh/chị xem có đúng ý không ạ?"
- Cảm ơn + giải thích next steps (dữ liệu sẽ được mã hóa, tổng hợp cùng các phỏng vấn khác, phục vụ báo cáo)

---

#### G. Phụ lục — Công cụ hỗ trợ (Thêm mới)

Bổ sung 3 phụ lục đi kèm kịch bản:

| Phụ lục | Nội dung | Mục đích |
|---|---|---|
| **A. Ma trận RQ–IQ** | Bảng mapping từng câu hỏi phỏng vấn (IQ) → câu hỏi nghiên cứu (RQ) | Đảm bảo IPR Phase 1; Minh chứng cho báo cáo methodology |
| **B. Thẻ kích thích** | 4-6 trích dẫn ngắn từ bài báo, in ra thẻ A5 | Dùng khi hỏi Phần 2 để tránh leading |
| **C. Template ghi chép** | Bảng ghi chú theo từng phần: Ý chính / Trích dẫn nguyên văn / Quan sát phi ngôn ngữ | Chuẩn hóa ghi chép giữa các thành viên nhóm |

---

## Quy trình thực hiện (GATE — skill `professional-writing`)

```
research/ đọc sâu 16 bài parsed + literature → ⛔ GATE: Content Brief (thẻ kích thích, insights)
→ editorial/ viết bản thảo v2.0 (academic writing, Vietnamese) → ⛔ GATE: Draft v2.0
→ review/ rà soát (anti-bias check, citation-check, leading-question audit) → ⛔ GATE: duyệt/sửa
→ xuất file final
```

**Output file:**
- Bản v2.0 lưu tại `03_phan-tich/phong-van/2026-07-08_kich-ban-phong-van_v2.0_draft_AI.md` (bản làm việc)
- SAU KHI nhóm duyệt + pilot test → Copy bản final vào `02_du-lieu-tho/phong-van/` (theo quy tắc vùng đóng băng: chỉ ghi vào khi là bản chốt)

---

## Open Questions

> [!IMPORTANT]
> **Q1. Thời lượng phỏng vấn mong muốn?** v2.0 dự kiến 15-17 câu (kèm probes) sẽ mất ~30-45 phút. Nếu nhóm chỉ có ~15-20 phút/người, cần cắt bớt 1 nhóm tiêu chí hoặc giảm kịch bản trade-off.

> [!IMPORTANT]
> **Q2. Ngôn ngữ kịch bản?** Viết hoàn toàn bằng tiếng Việt (phục vụ phỏng vấn thực tế tại VN), hay cần bản song ngữ VN-EN cho báo cáo LaTeX?

> [!NOTE]
> **Q3. Có cần tạo thẻ kích thích dạng file riêng** (PDF/slide) hay chỉ cần liệt kê trong body kịch bản? Nếu cần file riêng, sẽ xuất thêm 1 bản phụ lục dạng slide.

---

## Verification Plan

### Automated Checks
- **Leading-question audit:** Grep toàn bộ v2.0 tìm các cụm dẫn dắt ("đúng không?", "phải không?", "có phải là...")
- **Cross-reference check:** Đảm bảo mọi trích dẫn/stimulus đều khớp với nguồn trong [v5.0 criteria](file:///d:/LogManagement/03_phan-tich/tieu-chi/2026-07-05_danh-sach-tieu-chi-chinh-thuc_v5.0_final_user.md)

### Manual Verification
- Nhóm tự đọc v2.0 và phản hồi (IPR Phase 3)
- Thử phỏng vấn nội bộ 1 thành viên nhóm (IPR Phase 4 — Pilot test)
