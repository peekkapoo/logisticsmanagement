# Rà soát toàn diện báo cáo — cập nhật 2026-07-12

> Bản rà soát lần 2, thay thế bản 2026-07-11. Phạm vi: toàn bộ `main.tex` (Ch1-Ch6 + phụ lục + bảng/hình), đối chiếu chéo với `timeline.md`, `task_log.md`, `SUON-NOI-DUNG.md`, kịch bản khảo sát/phỏng vấn và file kết quả script trong `03_phan-tich/`.

## 1. Tổng trạng thái từng phần

| Phần | Trạng thái | Ghi chú |
|---|---|---|
| Abstract + Keywords | 🟡 placeholder | Đúng kế hoạch — cần kết quả TOPSIS mới viết được (Phase 6) |
| Ch1 Introduction | ✅ đạt chuẩn | Đã sửa nốt điểm lặp ý §1.2/§1.3 trong lần rà này |
| Ch2 Literature Review | ✅ đạt chuẩn | Đã thêm tín hiệu cross-ref mở đầu §2.6 trong lần rà này |
| Ch3 Methodology | ✅ đạt chuẩn (trừ §3.5) | Stage 1-3 đầy đủ; §3.5 Sensitivity design chờ Phase 5 |
| Ch4 Results | ✅ §4.1-4.2 / 🟡 §4.3-4.5 | Phần TOPSIS đúng kế hoạch chờ dữ liệu |
| Ch5 Discussion | 🟡 skeleton | §5.1 và §5.3 đã đủ nguồn để viết ngay không cần chờ TOPSIS (xem mục 4) |
| Ch6 Conclusion | 🟡 skeleton | Chờ Phase 5-6 |
| Appendix A (bảng hỏi) | ✅ MỚI ĐIỀN lần rà này | Bảng `tab:questionnaire` từ kịch bản khảo sát thật |
| Appendix B (ma trận AHP) | ✅ MỚI ĐIỀN lần rà này | Bảng `tab:pcm-full` 7×7 từ CSV chính thức, kèm CR |
| Appendix C (laptop data) | 🟡 | Chờ Phase 5 |
| Appendix D (phỏng vấn) | 🟡 | Nguồn có sẵn — viết được ở Phase 6, không phụ thuộc dữ liệu |

## 2. Bảng & hình — đánh giá trình bày

Toàn bộ 10 bảng đều dùng booktabs (không kẻ dọc), đúng quy ước AGENTS.md. Danh mục: `tab:mcdm-frequency`, `tab:prior-studies` (Ch2) · `tab:criteria`, `tab:saaty`, `tab:ri`, `tab:review-sources` (Ch3) · `tab:survey-results`, `tab:ahp-weights` (Ch4) · `tab:questionnaire` (A), `tab:pcm-full` (B). Hình duy nhất: `fig:framework` (TikZ, đã kiểm render trực quan — bố cục cột Stage 1 + hàng ngang Stage 2-3 rõ ràng).

Đã sửa trong lần rà này:
- Caption 2 bảng trong `tables/` thiếu dấu chấm cuối (không nhất quán với 8 bảng còn lại) — đã thêm.

Còn 2 điểm nhỏ chấp nhận được, KHÔNG bắt buộc sửa:
- Caption `tab:mcdm-frequency` chứa `\textcite` — citation sẽ hiện trong List of Tables. Hợp lệ về kỹ thuật (compile sạch), nhưng nếu muốn LOT gọn thì thêm short-caption: `\caption[Frequency of MCDM method use]{...}`.
- 3 overfull hbox nhỏ (1.5-11pt) trong Ch2 — dưới ngưỡng nhìn thấy bằng mắt ở bản in, xử lý ở lần polish cuối Phase 6 nếu muốn.

Gợi ý bổ sung (tùy chọn, làm khi rảnh): thêm **biểu đồ cột trọng số AHP** (bar chart) vào §4.2 — mẫu Lam 2023 Figure 2 dùng chart thay vì chỉ bảng; TikZ/pgfplots vẽ được từ 7 số đã có, giúp Ch4 bớt "toàn bảng".

## 3. Đối chiếu chéo file quản lý — các điểm LỆCH đã phát hiện và xử lý

1. **`timeline.md` lệch nặng** (Phase 3 ghi "Đang làm", Phase 4 "Chưa làm", ngưỡng ghi "mặc định 3.5", T3.5 trỏ file template đã vào `_cu/`) trong khi thực tế Phase 3-4 đã xong với ngưỡng 3.0 → **đã cập nhật**: Phase 3-4 ✅ kèm số liệu thật + citekey ngưỡng, Phase 5 "Đang làm", thêm 3 mốc 2026-07-11 vào bảng mốc.
2. **`SUON-NOI-DUNG.md` lệch cấu trúc** (đánh số §3.4/3.5/3.6 cũ; ghi "tổng hợp nhiều chuyên gia geometric mean" đã bỏ; thiếu §3.2.4 và §4.1 mới; Appendix B trỏ file xlsx template cũ) → **đã đồng bộ** toàn bộ trạng thái ✅/🟡 theo hiện trạng.
3. **Appendix B comment** trỏ nguồn cũ `ahp-thu-thap-chuyen-gia.xlsx` (template 5 chuyên gia đã vào `_cu/`) → đã thay bằng nguồn CSV chính thức + điền luôn nội dung thật.
4. `task_log.md` nhất quán, không lệch.

## 4. Việc có thể làm TIẾP không cần chờ dữ liệu TOPSIS

- **§5.1 Interpretation of the Criteria Weights** — mọi nguồn đã sẵn (trọng số + insight phỏng vấn + đối chiếu Lam 2023). Đây là "điểm bán" của đề tài theo SUON-NOI-DUNG.
- **§5.3 Practical and Managerial Implications** — phần trọng số đã cho phép viết hàm ý cho người mua/bộ phận thu mua (phần ranking bổ sung sau).
- **Appendix D** — kịch bản v3.0 + hồ sơ 5 chuyên gia đều có sẵn trong `03_phan-tich/phong-van/`.
- **Paper.tex** — có thể nén Ch1-Ch3 report thành §P1-P3 (Introduction đoạn 2-3, Lit review, Methodology framework+criteria) mà không cần chờ Phase 5.

## 5. Việc tồn đọng phía user (nhắc lại)

1. `references.bib` — entry `saaty_analytic_1987` vẫn ghi `author = {Saaty, R. W.}`, cần sửa thành `Saaty, Thomas L.` (đã flag 3 lần).
2. Thu thập dữ liệu laptop Phase 5 **phải theo đúng quy trình đã cam kết ở §3.4.2-3.4.3**: 7 trang review (không Engadget) → dedup theo model → lọc CellphoneS → PassMark cho CPU → đếm trung tâm bảo hành ủy quyền VN cho Brand → ghi ngày thu thập vào tên file.
3. 30/84 dòng khảo sát trùng hoàn toàn (36%) — user đã quyết giữ; nếu giảng viên hỏi thì cần chuẩn bị giải trình (ví dụ: khảo sát nhóm cùng văn phòng dễ trùng pattern trên 14 câu thang 5).
