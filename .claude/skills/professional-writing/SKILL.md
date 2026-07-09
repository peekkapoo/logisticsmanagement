---
name: professional-writing
description: Tòa soạn báo AI viết tiếng Việt chuyên nghiệp — dùng khi cần viết hoặc rà soát bài blog/cảm xúc, bài đăng Facebook, bài phản bác (debunk), tài liệu kỹ thuật, hoặc báo cáo/bài báo học thuật (tiếng Việt, tiếng Anh, hoặc song ngữ, kể cả xuất LaTeX .tex/.bib). Tổng biên tập nhận đề bài → phân tích → điều phối các ban Thu thập/Biên tập/Kiểm duyệt/Xuất bản/Tư liệu/Phát triển theo quy trình GATE. Kích hoạt khi user yêu cầu "viết bài", "viết blog", "phản bác/debunk", "viết báo cáo/luận văn/bài báo khoa học", "rà soát/biên tập bài viết tiếng Việt", hoặc "cải tiến skill viết".
---

# Viết Chuyên Nghiệp 4.0 — Tổng Biên Tập

Nhận đề bài → phân tích → chọn ban → thiết kế quy trình GATE → điều phối thực hiện.

**Nguyên tắc phân quyền:**
- TBT giao MỤC TIÊU cho lead, KHÔNG chọn staff
- Lead tự lập danh sách task chi tiết, chọn staff, ước lượng độ dài, đánh giá hoàn thành nội bộ
- Lead chuyển output cho ban tiếp theo khi đạt cam kết hoàn thành

---

## Bước 1: Kiểm tra lịch sử

- Liên quan bài đã viết trước? → CẬP NHẬT nhiệm vụ cũ
- Đề bài mới hoàn toàn? → TẠO nhiệm vụ mới

## Bước 2: Phân tích request

| # | Câu hỏi | Quyết định |
|---|---------|------------|
| 1 | User cung cấp gì? (data thô, ý tưởng, topic trống?) | Cần research/? |
| 2 | Mục đích? (inspire, educate, instruct, inform) | Tone & depth? |
| 3 | Độc giả là ai? (công chúng, professionals, technical) | Chọn ban nào? |
| 4 | Platform? (Facebook, blog, docs, report) | Cần publishing/? |
| 5 | Có claims/số liệu quan trọng? | Cần fact-check? |
| 6 | Có bài mẫu/pattern tương tự trong archive/? | Tra cứu pattern-catalog |
| 7 | Tài liệu học thuật? Loại nào? (IMRaD đầy đủ / báo cáo-tiểu luận linh hoạt) | Cấu trúc + citation style nào? |
| 8 | Ngôn ngữ xuất bản? (chỉ VN / chỉ EN / 2 bản song song) | Số lượt viết + rà soát |
| 9 | Định dạng xuất academic? (Markdown/Word-style hay LaTeX `.tex`) | publishing/academic.md hay publishing/latex.md |

## Bước 3: Lựa chọn ban

Từ kết quả phân tích, TBT chọn 3 vai:

- 🔴 **Chủ trì** — ban chịu trách nhiệm chính, dẫn dắt output
- 🟡 **Phối hợp** — ban hỗ trợ, cung cấp input cho ban chủ trì
- 🟢 **Kiểm tra** — ban rà soát chất lượng output cuối

**Bảng tham chiếu** (TBT có thể vượt ngoài bảng khi cần):

| Đề bài | 🔴 Chủ trì | 🟡 Phối hợp | 🟢 Kiểm tra |
|--------|-----------|------------|------------|
| Viết bài cảm xúc/blog | editorial/ | research/ (nếu cần) | review/ (+citation-check) |
| Phản bác/debunk | editorial/ | research/ | review/ (+fact-check, +citation-check) |
| Viết tài liệu kỹ thuật | editorial/ | research/ | review/ (+fact-check, +citation-check) |
| Phân tích data → viết | research/ → editorial/ | — | review/ (+fact-check) |
| Format cho kênh | publishing/ | — | review/ |
| Viết bài báo/báo cáo học thuật (VN/EN/song ngữ) | research/ (literature) → editorial/ (technical+academic) | archive/ (pattern academic nếu có) | review/ (+fact-check, +citation-check, +latex-check nếu LaTeX, theo ngôn ngữ) |
| Cải tiến skill | development/ | archive/ | — |
| Phân tích bài viết → nâng cấp skill | development/ | archive/ | — |

## Bước 4: Thiết kế quy trình GATE

TBT tự xây chuỗi bước phù hợp cho request cụ thể, bằng 4 mô hình luồng:

```
TUẦN TỰ     A → ⛔ → B → ⛔ → C
SONG SONG   A ┬→ ⛔ → C
             B ┘
ĐIỀU KIỆN   A → ⛔ → [nếu X: B] [nếu Y: C]
VÒNG LẶP    A → ⛔ → B → ⛔ → [chưa đạt? → quay lại A]
```

TBT kết hợp linh hoạt 1+ mô hình. Quy trình dài ngắn tùy request.

**Output bắt buộc:** TBT phải xuất quy trình GATE viết rõ ràng TRƯỚC KHI bắt đầu thực hiện. Đây là evidence cho toàn bộ quá trình.

### Quy tắc GATE (bắt buộc)

Mỗi bước trong quy trình có một cổng bàn giao. KHÔNG ĐƯỢC load ban tiếp theo cho đến khi ban hiện tại hoàn thành:

1. **Làm xong** — Lead đánh giá cam kết hoàn thành nội bộ đạt
2. **Xuất ra** — Viết sản phẩm vào file hoặc hiển thị cho người dùng
3. **Ghi nhận** — Ghi log bàn giao: ban nào → ban nào, sản phẩm gì

### Ví dụ quy trình GATE

**"Viết bài blog"** — tuần tự:
```
editorial/ viết → ⛔ GATE xuất draft → review/ rà soát → ⛔ GATE duyệt/từ chối
```

**"Phản bác bài viral"** — tuần tự + vòng lặp:
```
research/ thu thập nguồn gốc → ⛔ GATE xuất brief
→ editorial/ viết debunk → ⛔ GATE xuất draft
→ review/ rà soát → ⛔ GATE [đạt? → xuất bản] [chưa đạt? → quay lại editorial/]
```

**"Phân tích bài viết → nâng cấp skill"** — tuần tự + điều kiện:
```
development/ style-audit → ⛔ GATE xuất báo cáo
→ development/ upgrade đề xuất → ⛔ GATE trình user duyệt
→ [duyệt? → sửa file skill đích + ghi changelog] [từ chối? → sửa đề xuất]
```

**"Phân tích data rồi viết bài đăng Facebook"** — tuần tự:
```
research/ phân tích → ⛔ GATE xuất brief
→ editorial/ viết → ⛔ GATE xuất draft
→ publishing/ format FB → ⛔ GATE xuất bản thảo
→ review/ rà soát → ⛔ GATE duyệt/từ chối
```

**"Viết bài báo học thuật song ngữ VN+EN, xuất LaTeX"** — tuần tự + rẽ nhánh ngôn ngữ/định dạng:
```
research/ literature review → ⛔ GATE Content Brief (kèm metadata trích dẫn đầy đủ)
→ editorial/ viết bản VN (technical + academic) → ⛔ GATE draft VN
→ editorial/ viết lại bản EN từ Content Brief (KHÔNG dịch máy) → ⛔ GATE draft EN
→ review/ rà soát bản VN (bộ rule VN + citation-check) → ⛔ GATE
→ review/ rà soát bản EN (academic-en + citation-check) → ⛔ GATE
→ publishing/ [Markdown] academic.md  [LaTeX] latex.md sinh .tex+.bib → review/latex-check.md
→ ⛔ GATE xuất bản thảo
```

---

## Chuẩn Mực Academic Writing (Bắt Buộc)

Khi thực hiện các báo cáo mang tính học thuật, phân tích dữ liệu, Literature Review, hoặc bất kỳ văn bản nào yêu cầu tính chuyên nghiệp cao, TBT và các Ban BẮT BUỘC tuân thủ 4 nguyên tắc sau:

1. **Khử sắc thái cảm xúc (De-jargonize & Objectivity):** Tuyệt đối KHÔNG sử dụng các tính từ mạnh, đao to búa lớn (ví dụ: "vô cùng quan trọng", "không thể bàn cãi", "đóng vai trò then chốt"). Thay bằng các từ ngữ khách quan, điềm đạm (ví dụ: "giữ vị trí trung tâm", "đóng vai trò thứ yếu"). Cấm dịch word-by-word từ tiếng Anh.
2. **Trích dẫn liền mạch (In-text Citation):** Biến tài liệu tham khảo/tác giả thành chủ thể hành động trong câu để tạo luồng tranh luận (discourse) tự nhiên (ví dụ: "Sönmez Çakır và Pekkaya (2020) đã nhìn nhận...", "Nghiên cứu của ABC cho thấy..."). Tuyệt đối KHÔNG quăng một cái tên vô hồn hoặc nhãn `[1]` vào cuối câu.
3. **KHÔNG dùng gạch đầu dòng (No Bullet Points):** Tuyệt đối KHÔNG sử dụng gạch đầu dòng để liệt kê, KHÔNG bôi đậm tiêu đề kiểu AI gượng ép (ví dụ: `**Khái niệm:**`). Phải viết thành các đoạn văn (paragraphs) liền mạch, kết nối bằng các từ nối thể hiện sự đối chiếu (Ví dụ: "Trái ngược với đó", "Ở một khía cạnh khác").
4. **Phát triển luận điểm (Elaboration):** Không bao giờ chỉ nêu luận điểm suông rồi bỏ lửng. Phải "bung" các luận điểm bằng cách giải thích rõ cơ sở lý luận (ví dụ: cơ chế kinh tế, giới hạn vật lý) và đưa ra ví dụ thực tiễn (empirical evidence) để chứng minh.

### Ví dụ Đối chiếu Thực tế (Before vs After)

Để Agent dễ hình dung, dưới đây là sự khác biệt rất lớn giữa văn phong AI thông thường và văn phong Học thuật đã được tối ưu hóa:

**📌 Case 1: Khử tính từ đao to búa lớn & Giải thích cơ chế (Ví dụ Kinh tế & Rào cản)**
*   **❌ Bản Cũ (AI Sinh):** *(Lỗi: Dùng từ "tối thượng", "đỉnh cao", bỏ lửng hàm thoái hóa).*
    > "...Rau và Fang (2018) định nghĩa giá cả là phần bù trừ cho giá trị thương hiệu, và giá trị thiết bị sẽ thoái hóa dần theo hàm thời gian. Lam và cộng sự nhấn mạnh giá cả là rào cản tối thượng... sẵn sàng hy sinh thông số cấu hình đỉnh cao để đổi lấy ngân sách phù hợp."
*   **✅ Bản Chuẩn (User Hiệu đính):** *(Ưu điểm: Khử từ cảm xúc, "bung" giải thích cơ chế chu kỳ công nghệ).*
    > "...Rau và Fang (2018) bổ sung thêm góc nhìn từ kinh tế học khi định nghĩa giá cả chính là phần bù trừ cho giá trị thương hiệu, và giá trị thiết bị sẽ thoái hóa dần theo hàm thời gian. Bản chất của sự thoái hóa này bắt nguồn từ chu kỳ thay đổi công nghệ quá nhanh, khiến một thiết bị đắt tiền cũng có thể trở nên lỗi thời chỉ sau vài năm. Tập khách hàng này sẵn sàng đánh đổi các thông số phần cứng dư thừa—ví dụ như chấp nhận cấu hình Core i5 hoặc vi xử lý thế hệ cũ thay vì chạy theo dòng chip i9 đắt đỏ..."

**📌 Case 2: Phân tích sự đánh đổi (Trade-off) thay vì ngợi ca một chiều (Ví dụ Pin & Trọng lượng)**
*   **❌ Bản Cũ (AI Sinh):** *(Lỗi: Chỉ khen tính năng mà không nhìn thấy sự mâu thuẫn vật lý).*
    > "Khả năng hoạt động độc lập đưa thời lượng pin trở thành thuộc tính sinh tử. Khách hàng theo đuổi lối sống xanh ưu tiên pin hiệu suất cao... Nhóm sinh viên đặt nặng độ bền và thời lượng pin, đẩy tiêu chí độ mỏng nhẹ xuống cuối bảng xếp hạng."
*   **✅ Bản Chuẩn (User Hiệu đính):** *(Ưu điểm: Chỉ ra sự mâu thuẫn vật lý trade-off để lập luận có chiều sâu kỹ thuật).*
    > "...Khách hàng theo đuổi lối sống xanh cũng đặc biệt ưu tiên pin hiệu suất cao... Tuy nhiên, các nhà sản xuất luôn phải đối mặt với một sự đánh đổi (trade-off) vật lý: dung lượng pin tỷ lệ thuận với trọng lượng tổng thể của thiết bị... Xu hướng này lý giải vì sao người dùng sẵn sàng chấp nhận thiết bị có phần nặng hơn một chút, hoặc chi trả thêm cho lớp vỏ hợp kim nhôm chống va đập thay vì vỏ nhựa mỏng, nhẹ nhưng giòn, dễ gãy."

**📌 Case 3: Bổ sung logic kỹ thuật & Tính thực tiễn (Ví dụ Năng lực phần cứng)**
*   **❌ Bản Cũ (AI Sinh):** *(Lỗi: Bỏ quên RAM đa nhiệm, nhận xét SSD thay HDD chỉ vì "tiết kiệm pin").*
    > "Sức mạnh tính toán cấu thành từ CPU và RAM luôn giữ vị trí trung tâm... Sự dịch chuyển này giải thích lý do SSD dần thay thế hoàn toàn HDD. Ổ cứng thể rắn không chứa linh kiện cơ học, qua đó triệt tiêu rủi ro hỏng hóc và tiết kiệm pin đáng kể."
*   **✅ Bản Chuẩn (User Hiệu đính):** *(Ưu điểm: Liên kết RAM với bài toán đa nhiệm, liên kết tính phi cơ học của SSD với rủi ro va đập khi di chuyển).*
    > "Khả năng xử lý thông tin của CPU và RAM luôn giữ vị trí trung tâm... Đồng hành cùng CPU, dung lượng RAM lớn không còn là một sự xa xỉ mà trở thành tiêu chuẩn bắt buộc nhằm giải quyết bài toán đa nhiệm (multitasking) với các nền tảng web ngốn tài nguyên. Sự chuyển dịch này cũng giải thích lý do SSD thay thế HDD. Ổ cứng thể rắn không chứa đĩa từ quay hay linh kiện cơ học, qua đó không chỉ triệt tiêu hoàn toàn rủi ro mất mát dữ liệu do va đập vật lý trong quá trình di chuyển, mà còn tiết kiệm pin."

---

## Kho tư liệu (archive/)

TBT tra cứu `archive/pattern-catalog.md` khi phân tích request (Bước 2, câu 6). Cập nhật kho khi:
- Bài viết qua review/ duyệt → lưu bài mẫu vào archive/
- development/ phân tích bài viết bên ngoài → lưu pattern mới vào pattern-catalog

---

## Lỗi Cần Tránh

**❌ TBT không nên:**
- Tự chọn staff (đó là việc của lead)
- Load tất cả staff cùng lúc (vượt 200 dòng/lượt)
- Bỏ qua thiết kế quy trình GATE (phải xuất evidence)
- Ước lượng độ dài (đó là việc của lead)
- Giao mục tiêu không rõ ràng
- Phê duyệt Draft nếu bài viết thiếu danh mục trích dẫn (Nguồn tham khảo) đối với các thông tin kỹ thuật/số liệu.
- **Thu thập thông tin hời hợt:** Tuyệt đối không chỉ lọc từ khóa từ file bibtex hoặc metadata mà bỏ qua việc đọc toàn văn (full-text) các tài liệu gốc (PDF/nguồn hoàn chỉnh), dẫn đến bỏ sót luận điểm quan trọng.

**✅ TBT nên:**
- Giao mục tiêu rõ ràng: loại bài + tone
- Thiết kế quy trình GATE phù hợp cho từng request
- Tra cứu archive/ trước khi bắt đầu
- Để lead tự chọn staff và ước lượng độ dài
- Gọi development/ sau bài phức tạp để rút kinh nghiệm
- **Bắt buộc Ban Thu thập (research/):** Đọc sâu toàn văn (full-text) nguồn tài liệu PDF. ĐỂ TIẾT KIỆM TÀI NGUYÊN, Agent BẮT BUỘC phải gọi script `.agents/skills/professional-writing/scripts/academic_parser.py` để trích xuất nội dung PDF thành Markdown (chỉ lấy text thô). File Markdown này sẽ tự động được cache tại `02_du-lieu-tho/parsed_papers/`. Agent chỉ cần đọc file Markdown đã cache để lấy dữ liệu.

---

## Tổ Chức

```
research/      Ban Thu thập     → lead.md tự chọn: research.md, analysis.md, literature.md (academic)
editorial/     Ban Biên tập     → lead.md tự chọn: story-core, hook-close, rhythm, metaphor, reframe, debunk, emphasis, technical, academic
review/        Ban Kiểm duyệt   → lead.md tự chọn: punctuation, capitalization, natural, anti-ai, fact-check, consistency, academic-en, citation-check, latex-check
publishing/    Ban Xuất bản     → lead.md tự chọn: facebook.md, academic.md, latex.md
archive/       Ban Tư liệu     → lead.md quản lý: pattern-catalog.md
development/   Ban Phát triển   → lead.md quản lý: upgrade, style-audit, research-framework, research-results
```

**Quy tắc load:** Mỗi lượt ≤ 1 lead + 1-2 staff (do lead chọn). Tổng ≤ 200 dòng.

---

**Version:** 4.0
**Kiến trúc:** Tòa soạn báo (TBT → Lead → Staff)
**Nguyên tắc mới:** 
1. BẮT BUỘC kiểm tra trích dẫn (citation-check) và sự thật (fact-check) cho mọi định dạng bài viết. TBT phân tích + thiết kế quy trình GATE, Lead lập task chi tiết.
2. BẮT BUỘC thu thập dữ liệu từ nguồn hoàn chỉnh (full-text) thông qua Academic Parser Tiered Pipeline, cache dữ liệu Markdown vào `02_du-lieu-tho/parsed_papers/` để tái sử dụng. Nghiêm cấm lọc từ khóa hời hợt từ metadata.
3. BẮT BUỘC áp dụng nghiêm ngặt "Chuẩn Mực Academic Writing": Khử tính từ mạnh cảm xúc, citation liền mạch mạch lạc, KHÔNG dùng gạch đầu dòng, và bắt buộc phát triển luận điểm kèm ví dụ thực chứng.
