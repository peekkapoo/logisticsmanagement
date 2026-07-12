# Sườn slide thuyết trình (tiếng Anh, 15 slide) — bản khớp deck đã dựng

> Bản này thay thế `_cu/2026-07-09_outline-slide_v1.0_draft_AI.md` (đã lỗi thời: nguồn dữ liệu ghi CellphoneS,
> ngưỡng Likert ghi 3.5, có slide sensitivity analysis). Deck thực tế: `2026-07-13_slide-thuyet-trinh_v1.0_draft_AI.pptx`,
> dựng bằng skill `pptx` (pptxgenjs, from-scratch), 15 slide, layout 13.333x7.5in (LAYOUT_WIDE).
> Palette: navy `0F1B3C` chủ đạo + amber `F0A63C` làm accent duy nhất. Font: Cambria (header) / Calibri (body).

| # | Slide | Thông điệp chính | Hình/bảng chính | Nguồn số liệu (đã xác minh) |
|---|---|---|---|---|
| 1 | Title | Tên đề tài, nhóm 5, 5 thành viên + MSSV, giảng viên | Logo UFM, panel navy 2 cột | `chapters/00-frontmatter.tex` |
| 2 | Agenda | Lộ trình 3 stage, mỗi stage trả lời 1 RQ | 3 card ngang có mũi tên nối | `chapters/03-methodology.tex` §3.1 |
| 3 | Problem & Motivation | Laptop là bài toán MCDM thật; giá là 1 tiêu chí, không phải ngân sách chốt trước | 7 chip thuộc tính (2 cột + Brand full-width) | `chapters/01-introduction.tex` §1.1–1.2 |
| 4 | Research framework | Sơ đồ pipeline 5 bước, gắn nhãn Stage 1/2/3 + dải số liệu chốt (5 experts, N=84, CR=0.0483, 12 candidates) | Pipeline dark-navy + key-number strip | `chapters/03-methodology.tex` Figure 3.1 |
| 5 | Stage 1: Criteria-building funnel | 14 → 14 (expert-revised) → 7 (survey-retained) | Funnel 3 tầng | `chapters/04-results.tex` §4.1, Figure 4.1 |
| 6 | Stage 1 Results | 7 tiêu chí giữ lại + mean khảo sát + cost/benefit | 7 card tiêu chí + card ghi chú ngưỡng | `tables/survey-results.tex`, §4.2 |
| 7 | Stage 2: AHP method | Hierarchy 2 cấp, 1 chuyên gia đại diện, thang Saaty, CR=0.0483 đạt | Sơ đồ hierarchy + 3 fact card | `chapters/03-methodology.tex` §3.2 (Stage 2, 5 bước) |
| 8 | Stage 2 Results | Price+CPU = 62.6% tổng trọng số | Horizontal bar chart 7 trọng số AHP | `tables/ahp-weights.tex`, Figure 4.2 |
| 9 | Insight: Battery-life reversal | Battery mean cao nhất khảo sát (4.02) nhưng trọng số AHP thấp nhất (0.0258) — ngưỡng đủ dùng, không phải điểm khác biệt | 2 stat card (#1 vs Last) + diễn giải | §4.3, geometric-mean robustness check |
| 10 | Stage 3: Data collection | 12 candidate, 7 outlet review, nguồn giá Amazon.com (12/07/2026), quy đổi CPU→PassMark & Brand→Gartner | 3 stat card + 2 conversion-key card | `chapters/03-methodology.tex` §3.4.3–3.4.4, `appendices/E-laptop-data.tex` |
| 11 | Why TOPSIS, not AHP, for alternatives | AHP cần 66 so sánh cặp/tiêu chí (462 tổng) — không scale; TOPSIS chấm trực tiếp 84 giá trị đo được | 2 card so sánh AHP vs TOPSIS + badge VS | §3.4.3 rationale |
| 12 | Stage 3 Results | Bảng xếp hạng đầy đủ 12 candidate, highlight người thắng | Horizontal bar chart Ci (12 mục) + callout winner | `tables/topsis-ranking.tex`, Figure 4.3 |
| 13 | Winner profile | Lenovo ThinkPad T14 Gen 6 (AMD) thắng nhờ cân bằng, không áp đảo 1 tiêu chí; đối chiếu 2 cực rẻ nhất/đắt nhất | Card thông số winner + card diễn giải | `chapters/04-results.tex` §4.6 |
| 14 | Conclusion & Contribution | Biến quyết định ad hoc thành quy trình tái lập được; 2 đóng góp + hạn chế trung thực | 2 contribution card + 1 dải "Honest Limitations" | `chapters/06-conclusion.tex` |
| 15 | Thank you / Q&A | Cảm ơn, tên đề tài, trường, thời gian | Icon dấu hỏi trong vòng tròn | - |

## Số liệu neo cứng (không suy diễn, lấy đúng từ báo cáo)

- Ngưỡng giữ tiêu chí Likert: **mean ≥ 3.0** (điểm giữa thang đo), khảo sát **N = 84**, 5 chuyên gia phỏng vấn.
- 7 tiêu chí giữ lại: Price, CPU, RAM, SSD, Brand, Size/weight, Battery life.
- AHP: hierarchy 2 cấp, 1 chuyên gia đại diện, **CR = 0.0483** (đạt, ngưỡng 0.10). Trọng số: Price 0.3491, CPU 0.2769, SSD 0.1592, RAM 0.1201, Brand 0.0430, Size/weight 0.0258, Battery life 0.0258. Price+CPU = 62.6%.
- TOPSIS: 12 candidate, 7 outlet review, giá/cấu hình lấy từ **Amazon.com ngày 2026-07-12**. Người thắng: **Lenovo ThinkPad T14 Gen 6 (AMD)**, Ci = 0.6152 (giá $1,100). Top 3 cách nhau ≤ 0.011. Rẻ nhất Acer Aspire 5 ($395) hạng 7; đắt nhất ThinkPad X1 Carbon Gen 14 Aura ($3,499) hạng chót.
- **Không có** slide/nội dung sensitivity analysis (đã loại bỏ khỏi scope theo commit `b36a1bd`) — hạn chế này được nêu tường minh ở slide 14.
- Nguồn dữ liệu KHÔNG phải CellphoneS — đã chuyển sang Amazon.com từ Phase 5.

## Ghi chú chuẩn bị thuyết trình (T6.7)

- Phân vai người nói theo slide, mỗi người nói phần mình đã làm (gợi ý: 1 người/2-3 slide liền kề theo stage).
- Canh tổng thời gian theo yêu cầu của giảng viên (điền sau khi có rubric).
- Chuẩn bị sẵn câu trả lời cho 3 câu hỏi dễ bị hỏi: (1) vì sao ngưỡng Likert là 3.0 chứ không phải mốc khác, (2) vì sao AHP chỉ dùng 1 chuyên gia thay vì cả 5, (3) vì sao Stage 3 không tiếp tục dùng AHP cho 12 alternative.
- File nguồn dựng slide (pptxgenjs script) không lưu trong repo — chỉ lưu kết quả `.pptx`; nếu cần chỉnh sửa, dựng lại qua skill `pptx` bám theo bảng trên.
