# Sườn nội dung chi tiết — Report + Scientific Paper (AHP–TOPSIS chọn laptop VP)

> Bản đồ hướng dẫn viết cho từng section. Học cấu trúc từ 8 bài Q1/Q2: **Lam 2023** (`weng_siew_lam_evaluation_2023`, pipeline AHP-TOPSIS chuẩn), **Gaur 2023** (`gaur_application_2023`), **Sönmez Çakır 2020** (`sonmez_cakir_determination_2020`), **Maghsoudi 2026** (`maghsoudi_hybrid_2026`), **Çalık 2021** (`calik_novel_2021`), **Saputro 2023** (`saputro_hybrid_2023`), **Villalba 2024** (`villalba_review_2024`), **Tighnavard 2025** (`tighnavard_balasbaneh_systematic_2025`).
>
> Quy ước áp dụng cho MỌI section: văn xuôi liền mạch, **không gạch đầu dòng** (trừ RQ/Step); citation **APA narrative** (`\textcite` khi tác giả là chủ thể câu, `\parencite` khi đóng ngoặc); khử tính từ cường điệu (blacklist Case 4 trong SKILL.md); method viết theo khối **Step 1…k** + phương trình đánh số.
>
> **Trạng thái:** phần đánh dấu 🟢 = đã có nguồn, sẵn sàng viết; 🟡 = chờ Phase 4-5 (tính AHP/TOPSIS).

---

## PHẦN A — REPORT (`main.tex`, report class)

### Front matter (`chapters/00-frontmatter.tex`)
Abstract ~250 từ, khuôn **gap → method → result → implication** (mẫu Maghsoudi 2026). Keywords 5 (đã điền). 🟡 Abstract viết sau khi có kết quả.

### Chapter 1 — Introduction 🟢 (đã viết + compiled)
Đã đủ 5 mục: 1.1 Background · 1.2 Problem statement · 1.3 Research gap & contributions (twofold, kiểu Saputro) · 1.4 Objectives & RQ1-3 · 1.5 Scope & structure. Số liệu thị trường đã xác minh full-text (161,6M/2017; 218M/2020; 225M/2021).

### Chapter 2 — Literature Review
- **§2.1 Laptop selection as an MCDM problem** — đặt bài toán vào phạm vi MCDM; nhiều tiêu chí xung đột (hiệu năng vs pin, độ bền vs trọng lượng) không quy về một đơn vị. Citekey: `sonmez_cakir_determination_2020`, `gaur_application_2023`. 🟢
- **§2.2 Overview of MCDM methods** — mượn **phân loại 5 nhóm của Villalba (2024)**: (1) scoring (SAW, COPRAS); (2) distance-based (TOPSIS, VIKOR); (3) pairwise (AHP, ANP, MACBETH); (4) outranking (PROMETHEE, ELECTRE); (5) utility (MAUT, MAVT). Chốt độ phổ biến: `basilio_systematic_2022`, `zyoud_bibliometric-based_2017` — **văn xuôi thuần, KHÔNG dùng bảng** (đã bỏ `tab:mcdm-frequency` 2026-07-12, số liệu trùng lặp giữa bảng và văn xuôi, trình bày không hợp lý). 🟢
- **§2.3 AHP** — nguyên lý Saaty: phân cấp, thang 1-9, eigenvector, CR. (Bảng Saaty/RI đặt ở Ch.3.) 🟢
- **§2.4 TOPSIS** — nguyên lý Hwang & Yoon: PIS/NIS, chuẩn hóa vector, closeness coefficient. 🟢
- **§2.5 Prior studies** — văn xuôi + **bảng `tab:prior-studies`** (đã có khung, format kiểu Tighnavard Table 5: Source | Product | Criteria | Method). Bổ sung nguồn tiêu chí chi tiết từ `01_tai-lieu-tham-khao/tong-hop-tieu-chi.md`. 🟢
- **§2.6 Research gap & positioning** — chốt gap kép (thiếu AHP-TOPSIS chuẩn trên data laptop thực tế VN; lệch trọng số quốc tế vs VN). Citekey: `tighnavard_balasbaneh_systematic_2025`. 🟢

### Chapter 3 — Methodology ✅ (đã viết trừ phần TOPSIS elaboration)
**Nguyên tắc IMRaD áp dụng nghiêm 2026-07-12: Ch3 CHỈ mô tả phương pháp/quy trình (thiết kế, lý do, quy tắc quyết định) — KHÔNG nêu kết quả áp dụng phương pháp (số liệu/phát hiện cụ thể chuyển hết sang Ch4 §4.1).**
- **§3.1 Research framework** ✅ — prose + hình TikZ inline `fig:framework` (KHÔNG dùng file figures/framework.pdf nữa). Hình vẫn giữ số liệu thật (kiểu PRISMA flow diagram) — ngoại lệ hợp lệ vì là sơ đồ tổng quan quy trình, không phải văn xuôi kết quả.
- **§3.2.1 Literature synthesis** ✅ — CHỈ quy trình tìm/gộp/loại tiêu chí ứng viên; KHÔNG nêu con số 14/6 nhóm nữa (forward-ref sang §4.1.1).
- **§3.2.2 Expert interviews** ✅ — purposive n=5 (CG-01..05), IPR framework (Castillo-Montoya 2016) + cognitive probing (Willis 2005) + Delphi round-1 (Al Hazza 2022, McMillan 2016); CHỈ nêu QUY TẮC quyết định đổi tiêu chí (đồng thuận đa số 5 chuyên gia) — KHÔNG kể GPU bị loại/software được thêm nữa (đã chuyển sang Ch4 §4.1.2).
- **§3.2.3 Survey-based screening** ✅ (renumber từ 3.2.4 sau khi bỏ subsection "Candidate Criteria Set" khỏi Ch3) — thiết kế Likert, ngưỡng midpoint 3.0 (Chyung 2017), chốt trước khi thu.
- **§3.3 AHP (Step 1-5)** ✅ — Step 2: 1 chuyên gia đại diện (KHÔNG tổng hợp nhiều chuyên gia); Step 4: EIGENVECTOR `eq:weight` (Saaty 2003, Ishizaka & Lusti 2006), GM làm cross-check; Step 5: CR + quy trình xử lý CR>0.1.
- **§3.4 Stage 3 scenario-based** ✅ — 3.4.1 Decision scenario · 3.4.2 Alternative identification (7 trang review `tab:review-sources`, loại Engadget, dedup, **nguồn giá/thông số ĐỔI sang Amazon.com 2026-07-12** — GIỮ NGUYÊN trong Ch3 vì đây là mô tả nguồn dữ liệu/data provenance, tương đương PRISMA search strategy, không phải "finding" về đối tượng nghiên cứu; citation Rau & Fang 2018 làm tiền lệ dùng Amazon) · 3.4.3 Operationalisation (PassMark cho CPU; Brand ĐỔI proxy 2 lần: "trung tâm bảo hành VN" → IDC toàn cầu → **thị phần Gartner Q1/2026** — `gartner_2026`, vì IDC không công bố % riêng Acer trong khi Gartner có đủ cả 6 hãng cùng kỳ; Battery đổi sang watt-hour thay vì giờ) · 3.4.4 TOPSIS Step 1-7.
- **§3.5 Sensitivity analysis design** ❌ ĐÃ BỎ (2026-07-12, theo yêu cầu user) — section cũ mô tả 28 kịch bản ±10%/±20%; đã xóa khỏi `03-methodology.tex` cùng section kết quả tương ứng ở Ch4 §4.6 (không còn tính năng sensitivity analysis trong report).

### Chapter 4 — Results (mirror 1-1 với Ch.3, mẫu Maghsoudi)
- **§4.1 Criteria development outcomes** ✅ (MỚI 2026-07-12, chuyển từ Ch3) — 4.1.1 The Candidate Criteria Set: bảng `tab:criteria` 14 tiêu chí/6 nhóm (đã MOVE nguyên khối từ Ch3 §3.2.3 cũ, label `subsec:criteria-set`/`tab:criteria` giữ nguyên); 4.1.2 Interview-Driven Refinement: narrative GPU loại/Software Compatibility thêm/định nghĩa SSD+Design tinh chỉnh/pin hạ chuẩn (MOVE nguyên khối từ Ch3 §3.2.2 cũ).
- **§4.2 Criteria screening results** ✅ — `tables/survey-results.tex`, 84 phiếu, 7 giữ/7 loại, trả lời RQ1.
- **§4.3 Criteria weights + CR** ✅ — `tables/ahp-weights.tex` (eigenvector, CR=0.0483), battery-reversal vs Lam 2023, trả lời RQ2.
- **§4.4 Decision scenario & alternatives** ✅ (2026-07-12) — 12 candidate thật từ Amazon.com, bảng `tab:decision-matrix` (xoay ngang, `sidewaystable`). Nguồn: `02_du-lieu-tho/laptop-thi-truong/2026-07-12_amazon-laptop-candidates-raw_v1.0_final_user.csv`.
- **§4.5 TOPSIS ranking** ✅ (2026-07-12) — chạy `topsis.py --latex tables/topsis-ranking.tex` thật trên `03_phan-tich/du-lieu-sach/2026-07-12_topsis-decision-matrix_v1.0_final_user.csv`; hạng 1 Lenovo ThinkPad T14 Gen 6 (AMD) Ci=0.6152, hạng 2 Dell 14 Premium 0.6046, hạng 3 Apple MacBook Air M5 0.6039. Section cuối cùng của Ch4 (không còn §4.6 sau khi bỏ sensitivity analysis).

### Chapter 5 — Discussion
- **§5.1 Interpretation of weights** ✅ (2026-07-12) — **TRỌNG TÂM/điểm bán**: nghịch lý pin/trọng lượng (screening cao nhất nhưng AHP thấp nhất — salience vs marginal decision value), loại GPU → dồn ngân sách CPU, tương thích phần mềm Windows lock-in bị survey loại (expert vs end-user divergence, đọc là eligibility condition), caveat Display granularity (đã có từ trước). Nguồn: `03_phan-tich/tieu-chi/...v2.0` + Ch4 số liệu thật.
- **§5.2 Interpretation of ranking** ✅ (2026-07-12) — T14 Gen 6 thắng nhờ cân bằng không nhờ trội đơn tiêu chí, khớp kỳ vọng phỏng vấn (mid-tier CPU đủ); 2 cực Acer rẻ nhất hạng 7 / X1 Carbon đắt nhất chót (over-specification, Rau & Fang 2018); top-3 cách <0.011 → đọc là short list, tie-breaker là eligibility conditions (macOS vs Windows lock-in).
- **§5.3 Practical/managerial implications** ✅ (2026-07-12) — 4 nhóm kiểu Saputro: người mua cá nhân (cấu trúc trọng số làm checklist), thu mua doanh nghiệp (auditable, tái dùng — giữ weight vector, thay decision matrix), nhà bán lẻ (assortment mid-tier cân bằng), hãng SX (đầu tư biên vào giá + thế hệ CPU, không phải pin/mỏng vượt ngưỡng).
- **§5.4 Comparison with prior studies** ✅ (2026-07-12) — đồng thuận: price dominance (Liao 2022, Šostar 2023, Elnatan); khác biệt: brand (Sönmez 2020 cao nhất vs 0.0430 ở đây — signaling/information asymmetry), battery (Lam 2023); Gaur 2023 Dell top ↔ Dell hạng 2 ở đây; Maghsoudi 2026 GPU chót + price top (corroborate), display hạng 3 là disagreement duy nhất → về caveat granularity §5.1.

### Chapter 6 — Conclusion
- **§6.1 Summary of findings** ✅ (2026-07-12) — RQ1 (7 tiêu chí sau screening, quá trình -GPU/+software là một phần finding), RQ2 (Price .3491 + CPU .2769 = 62.6%, CR=0.0483, battery reversal), RQ3 (T14 Gen 6 AMD Ci=0.6152, top-3 short list, balance > dominance).
- **§6.2 Contributions** ✅ (2026-07-12) — twofold từ §1.3 + điểm methodological: 2-instrument design làm expert-vs-crowd divergence quan sát được.
- **§6.3 Limitations** ✅ (2026-07-12) — 4 hạn chế: 1 chuyên gia AHP, mẫu 84 convenience, snapshot Amazon.com 1 ngày, proxy PassMark/market-share; thêm ghi chú không có sensitivity analysis → ranking đọc là short list.
- **§6.4 Future work** ✅ (2026-07-12) — group AHP, sensitivity analysis (đã bỏ khỏi report → thành future work), fuzzy AHP-TOPSIS, re-run với catalogue VN + giá nội địa, tách Display sub-criteria (test caveat §5.1), segment khác.

### Appendices
Thứ tự đã sắp lại 2026-07-12 theo đúng flow Stage 1→2→3 của Ch3 (trước đó A-D xếp không theo trình tự pipeline — interview protocol ở D dù thuộc bước sớm hơn AHP/khảo sát):
- **A. Theoretical Basis for the Candidate Criteria** ✅ MỚI (2026-07-12) — lý luận học thuật thuần túy (không đưa interpretation chuyên gia) cho 14 tiêu chí từ literature (`2026-07-05_danh-sach-tieu-chi-chinh-thuc_v5.0`, viết lại độc lập sang EN, 5 nhóm) + 1 tiêu chí bổ sung sau phỏng vấn (Software Compatibility, cơ sở lý thuyết riêng: Guan & Yuen 2022 — OS là leaf attribute có preference value; Lam et al. 2023 trích Chakraborty et al. — OS xếp hạng 2/6 tiêu chí điện thoại). Bảng tổng hợp `tab:criteria-theory-summary` 15 dòng.
- **B. Expert Interview Protocol and Summary** ✅ (đổi từ D, nội dung không đổi).
- **C. Likert Survey Questionnaire** ✅ (đổi từ A, nội dung không đổi).
- **D. AHP Pairwise Comparison Matrix + tính từng bước** ✅ (đổi từ B; 4 mục D.1-D.4 tái lập power-iteration của `ahp.py`).
- **E. Laptop Dataset + Benchmarks + TOPSIS step-by-step** ✅ (đổi từ C; 2026-07-12: E.1 Raw Dataset — 12 candidate thật từ Amazon.com + bảng truy vết CPU/weight nguyên văn; E.2 Benchmark and Market-Share Conversion — bảng conversion key PassMark (9 CPU) + Gartner Brand % (6 hãng) + ma trận đã chuyển đổi `tab:decision-matrix-converted`; E.3 TOPSIS Step-by-Step Calculation — norms, normalised matrix, weighted matrix, A+/A-, separation S+/S-, toàn bộ sinh từ `topsis.py`, không tính tay).

---

## PHẦN B — SCIENTIFIC PAPER (`paper.tex`, article class, cô đọng ~12-15 trang)

Nguyên tắc: nén ~40-50% report; giữ Methodology gần đủ (method đã chốt), nén Introduction/Lit review, kết quả trình bày gọn.

- **§P1 Introduction** — đoạn 1 đã viết (real, có citation). 🟢 Cần thêm: đoạn 2 (problem + gap + twofold contribution, nén từ Report §1.2-1.3); đoạn cuối (3 RQ + "The remainder of this paper is organised as follows").
- **§P2 Literature Review** 🟢 — nén ~1-1.5 trang: tổng quan MCDM (5 nhóm) + định vị AHP-TOPSIS + gap. Có thể giữ bảng tổng hợp rút gọn.
- **§P3 Research framework & criteria** 🟢 — sơ đồ 3 giai đoạn + bảng 14 tiêu chí rút gọn.
- **§P3 AHP/TOPSIS** — đã dựng đầy đủ equation (`eq:p-weight`, `eq:p-cr`, `eq:p-closeness`). 🟢
- **§P4 Results** 🟡 — bảng trọng số + CR; ma trận quyết định; bảng xếp hạng `C_i`; hình độ nhạy.
- **§P5 Discussion** 🟢/🟡 — phát hiện lý thuyết-vs-VN (🟢); hàm ý (🟢); đối chiếu nghiên cứu trước (🟡).
- **§P6 Conclusion** 🟡 — trả lời 3 RQ + đóng góp + hạn chế + hướng phát triển (gộp gọn kiểu Çalık/Saputro).

---

## Quy ước biên dịch
- Report: `xelatex main.tex → biber main → xelatex main → xelatex main`
- Paper: `xelatex paper.tex → biber paper → xelatex paper → xelatex paper`
- Dùng chung `references.bib` + `figures/`. Hai document compile độc lập → nhãn (`\label`) không xung đột chéo.
