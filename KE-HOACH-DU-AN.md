# Plan: Cấu trúc dự án + README workflow chi tiết + hệ sinh thái skill cho đồ án MADM/MCDM

> **Trạng thái:** BẢN NHÁP đang review — chưa thực thi. (Lưu ngày 2026-07-04)

## Context (Bối cảnh)

Đồ án nhóm môn Logistics Management: xây bộ tiêu chí mua laptop (literature review → phỏng vấn chuyên gia → khảo sát Likert), tính trọng số bằng **AHP**, xếp hạng alternatives bằng **TOPSIS**. 

Các quyết định đã chốt:
- Chủ đề **giữ nguyên** "cá nhân mua laptop" (giảng viên đã duyệt).
- **Ngôn ngữ làm việc là tiếng Việt** trong toàn bộ quá trình; chỉ **báo cáo LaTeX cuối và slide thuyết trình là tiếng Anh**.
- LaTeX viết **cục bộ** trong workspace, AI hỗ trợ.
- Người dùng là **trạm trung tâm** nhận file từ thành viên (cần ngăn `inbox`).
- Khảo sát **thật** qua Google Form; dữ liệu laptop **AI crawl** từ CellphoneS + benchmark.
- **Không tạo bảng phân công** — chỉ cần hệ thống task chi tiết theo phase, người dùng tự phân công.
- Skill `professional_writing` viết được **cả tiếng Việt lẫn tiếng Anh** (đã chuẩn hóa văn phong) → dùng được cho cả nháp lẫn bản cuối. Skill health/life-consultant đã bị xóa.

## Phần 1 — Cấu trúc thư mục sẽ tạo

Nguyên tắc (theo thực hành quản lý dự án nghiên cứu): chia theo **vòng đời dữ liệu** raw → working → final; đánh số theo pipeline; tên không dấu kebab-case; vùng raw đóng băng; vùng nộp bài thiêng liêng; thư mục LaTeX tự trị.

```
d:\LogManagement\
├── README.md                      ← Sổ tay vận hành dự án (chi tiết ở Phần 2)
├── 00_quan-ly-du-an\
│   ├── brainstorm.md              ← DI CHUYỂN từ gốc vào
│   ├── timeline.md                ← các phase + milestone + deadline (khung sẵn, nhóm điền ngày)
│   └── bien-ban-hop\              ← ghi chú các buổi họp nhóm / gặp giảng viên
├── 01_tai-lieu-tham-khao\
│   ├── MADM.pdf                   ← DI CHUYỂN từ gốc vào
│   ├── bai-bao\                   ← PDF papers, đặt tên TacGia_Nam_TuKhoa.pdf
│   └── tong-hop-tieu-chi.md       ← bảng: paper → tiêu chí rút ra → trang → trích dẫn
├── 02_du-lieu-tho\                ← ĐÓNG BĂNG sau khi lưu, không sửa trực tiếp
│   ├── _HUONG-DAN.md
│   ├── inbox\                     ← file thành viên gửi, chưa phân loại
│   ├── khao-sat\                  ← CSV export từ Google Form
│   ├── phong-van\                 ← kịch bản + ghi chú/ghi âm phỏng vấn chuyên gia
│   └── laptop-thi-truong\         ← dữ liệu crawl (kèm ngày crawl trong tên file)
├── 03_phan-tich\                  ← vùng làm việc, copy từ 02 vào xử lý
│   ├── tieu-chi\                  ← sàng lọc Likert → bộ tiêu chí chốt
│   ├── ahp\                       ← ma trận so sánh cặp, CR, trọng số
│   ├── du-lieu-sach\              ← dữ liệu laptop đã làm sạch + benchmark đã map
│   └── topsis\                    ← ma trận quyết định, chuẩn hóa, xếp hạng, sensitivity
├── 04_bao-cao-latex\              ← tiếng Anh, tự biên dịch được
│   ├── main.tex + chapters\ + figures\ + tables\ + references.bib
├── 05_slide\                      ← nguồn slide EN + nháp
├── 06_nop-bai\                    ← CHỈ bản nộp cuối
├── 07_sao-luu\                    ← snapshot ZIP theo milestone (xem Phần 2.E)
└── skill\                         ← công cụ AI (sẽ bổ sung, xem Phần 3)
```

Thao tác: tạo cây thư mục; di chuyển 2 file hiện có; tạo `README.md`, `timeline.md`, `tong-hop-tieu-chi.md`, `_HUONG-DAN.md`; tạo skeleton LaTeX biên dịch được (main.tex + 6 chapter + references.bib).

## Phần 2 — README.md: Sổ tay vận hành + workflow task chi tiết

README viết **tiếng Việt**, theo mô hình PM chuẩn (charter → phases → tasks → definition of done), gồm:

**A. Tổng quan dự án** — mục tiêu, 2 sản phẩm nộp (report EN + slide EN), quy ước ngôn ngữ (làm việc VN, output EN).

**B. Bản đồ thư mục + 3 luật vàng** — (1) file thô vào `02` là đóng băng, xử lý thì copy sang `03`; (2) `06` chỉ chứa bản nộp; (3) mọi file thành viên gửi đi qua `inbox` rồi mới phân loại. Quy ước đặt tên chi tiết ở mục E.

**C. Workflow 7 phase với hệ thống task chi tiết** — mỗi phase ghi rõ: mục tiêu, task cụ thể (đánh số để phân công), input/output, thư mục lưu, skill dùng, tiêu chí hoàn thành (Definition of Done). Khung task chính:

- **Phase 0 – Khởi động** (T0.x): chốt scope với giảng viên, xin rubric, lập timeline, thống nhất quy ước file.
- **Phase 1 – Literature review** (T1.x): xây chuỗi từ khóa tìm kiếm (search string), thu thập 10–15 papers về laptop selection/AHP-TOPSIS, đọc + trích tiêu chí vào `tong-hop-tieu-chi.md`, tổng hợp thành bộ tiêu chí sơ bộ, tạo file .bib ngay từ lúc này.
- **Phase 2 – Phỏng vấn chuyên gia** (T2.x): thiết kế kịch bản phỏng vấn bán cấu trúc, chọn 3–5 chuyên gia (maximum variation sampling), phỏng vấn + ghi chú, điều chỉnh bộ tiêu chí theo bối cảnh VN.
- **Phase 3 – Khảo sát Likert** (T3.x): dựng Google Form thang 5 điểm, xác định cỡ mẫu mục tiêu + kênh phát, thu thập, phân tích mô tả (mean/SD), chốt ngưỡng giữ tiêu chí (>3.5, có trích nguồn), chốt bộ tiêu chí cuối.
- **Phase 4 – AHP** (T4.x): thiết kế bảng hỏi so sánh cặp, thu ma trận từ chuyên gia/nhóm, tính trọng số (eigenvector), kiểm tra CR ≤ 0.1 (quy trình xử lý nếu vượt), tổng hợp nhiều người bằng geometric mean.
- **Phase 5 – Dữ liệu laptop + TOPSIS** (T5.x): crawl CellphoneS (laptop 20–25tr), map benchmark (PassMark cho CPU/GPU — 1 nguồn/loại, ghi ngày truy cập), rubric chấm tay tiêu chí định tính, làm sạch → ma trận quyết định, chạy TOPSIS, sensitivity analysis, diễn giải kết quả.
- **Phase 6 – Báo cáo & slide** (T6.x): viết từng chương LaTeX EN (outline IMRaD: Intro → Lit review → Methodology → Results → Discussion → Conclusion), làm figures/tables từ kết quả Phase 4–5, hoàn thiện trích dẫn, thiết kế slide EN sinh động, tổng duyệt thuyết trình, checklist rà soát cuối, xuất PDF vào `06_nop-bai`.

**D. Hướng dẫn LaTeX** — cần MiKTeX, lệnh biên dịch, hoặc nhờ AI biên dịch giúp.

**E. Chiến lược backup & quản lý phiên bản bản thảo** (3 lớp, ghi thành quy trình trong README):

*Lớp 1 — Quy ước đặt tên phiên bản (áp dụng cho mọi bản thảo ngoài LaTeX: ghi chú, Excel, slide nháp):*
```
YYYY-MM-DD_<ten-tai-lieu>_v<X.Y>_<trangthai>_<tennguoi>.<ext>
Ví dụ: 2026-07-10_chuong-3-methodology_v2.1_draft_an.docx
```
- `vX.Y`: X tăng khi thay đổi lớn (viết lại chương, đổi phương pháp), Y tăng khi sửa nhỏ.
- `<trangthai>`: `draft` (đang viết) → `review` (chờ nhóm góp ý) → `final` (đã chốt, không sửa nữa; muốn sửa phải tạo version mới).
- Bản cũ không xóa — chuyển vào thư mục con `_cu\` trong cùng chỗ, để thư mục làm việc chỉ hiện bản mới nhất.

*Lớp 2 — Git cho riêng `04_bao-cao-latex\` (AI quản lý hộ, nhóm không cần biết git):*
- `git init` tại gốc workspace, `.gitignore` bỏ qua file tạm LaTeX (.aux, .log...) và `02_du-lieu-tho\inbox`.
- Quy trình: mỗi khi kết thúc buổi làm việc trên báo cáo, người dùng nhờ AI "lưu phiên bản báo cáo" → AI commit với message mô tả (vd: "Hoàn thành mục 3.2 AHP"). Muốn quay lại bản cũ → nhờ AI khôi phục. README ghi rõ 2 câu lệnh nhờ AI này.

*Lớp 3 — Snapshot ZIP theo milestone + offsite:*
- Kết thúc mỗi Phase (0→6): nén toàn bộ workspace (trừ `skill\` và file tạm) thành `07_sao-luu\YYYY-MM-DD_phase<N>_<ten-milestone>.zip`.
- Sau khi tạo ZIP, upload thủ công lên Google Drive nhóm (chống mất máy/hỏng ổ). README có checklist "kết thúc phase" nhắc việc này.
- `07_sao-luu\` chỉ chứa ZIP, không bao giờ giải nén đè lên workspace; muốn khôi phục thì giải nén ra chỗ khác rồi chọn file cần lấy.

(Chi tiết từng task con sẽ viết đầy đủ trong README khi thực thi — mỗi phase 4–8 task đánh mã T#.#, người dùng dựa vào đó phân công.)

## Phần 2b — Sườn báo cáo LaTeX, sườn slide, template Excel thu thập dữ liệu

### Sườn báo cáo LaTeX (tiếng Anh, tạo sẵn file .tex cho từng chương với tiêu đề mục con)

`main.tex` (report class, 12pt, biblatex APA, biên dịch **XeLaTeX + biber**, preamble kế thừa mẫu đã kiểm chứng compile thật trong `professional_writing\publishing\latex.md` — xem Phần 3.1) input các chương:

```
chapters\00-frontmatter.tex   Title page, Abstract, Table of Contents, List of Figures/Tables
chapters\01-introduction.tex  1.1 Background & motivation  1.2 Problem statement
                              1.3 Objectives & research questions  1.4 Scope & structure of the report
chapters\02-literature.tex    2.1 MCDM/MADM overview  2.2 AHP: theory & applications
                              2.3 TOPSIS: theory & applications  2.4 Prior studies on laptop selection criteria
                              2.5 Research gap & justification of the hybrid AHP–TOPSIS approach
chapters\03-methodology.tex   3.1 Research framework (sơ đồ 3 giai đoạn)
                              3.2 Stage 1 – Criteria development (3.2.1 Literature synthesis,
                                  3.2.2 Expert interviews, 3.2.3 Likert survey & screening threshold)
                              3.3 Stage 2 – AHP weighting (pairwise design, eigenvector, CR, aggregation)
                              3.4 Stage 3 – TOPSIS ranking (data collection từ CellphoneS,
                                  benchmark mapping, normalization, ranking steps)
chapters\04-results.tex       4.1 Final criteria set  4.2 Criteria weights (AHP) & consistency check
                              4.3 Decision scenario & alternatives  4.4 TOPSIS ranking results
                              4.5 Sensitivity analysis
chapters\05-discussion.tex    5.1 Interpretation  5.2 Why TOPSIS over AHP at Stage 3
                              5.3 Practical implications  5.4 Limitations & future work
chapters\06-conclusion.tex    Kết luận + khuyến nghị
references.bib                + appendices\ (bảng hỏi khảo sát, ma trận AHP đầy đủ, dữ liệu laptop)
```

Mỗi file .tex tạo sẵn `\chapter`/`\section` đúng như trên kèm ghi chú `% TODO` tiếng Việt hướng dẫn cần viết gì — sườn biên dịch được ngay ra PDF mục lục đầy đủ; nội dung tinh chỉnh sau theo yêu cầu của bạn.

### Sườn slide thuyết trình (tiếng Anh, ~14 slide, lưu thành `05_slide\outline-slide.md` để sau này dựng bằng skill pptx)

1. Title + team members → 2. Agenda → 3. Problem & objectives → 4. Research framework (sơ đồ 3 stages) → 5. Stage 1: How criteria were built (lit review → experts → survey) → 6. Survey results & final criteria set → 7. Stage 2: AHP — cách làm + bảng trọng số → 8. Decision scenario (designer, budget 20–25M) → 9. Data collection (CellphoneS + benchmarks) → 10. Stage 3: Why TOPSIS? (luận giải chuyển phương pháp) → 11. TOPSIS ranking results (bảng + chart) → 12. Sensitivity analysis → 13. Conclusion & recommendation → 14. Q&A.

Mỗi slide trong outline ghi: thông điệp chính, hình/bảng cần có, nguồn số liệu (folder nào). Thiết kế sinh động sẽ làm ở Phase 6 bằng skill `pptx` + `dataviz`.

### 2 file Excel thu thập dữ liệu (tạo bằng Python/openpyxl, công thức Excel có sẵn)

1. **`03_phan-tich\ahp\ahp-thu-thap-chuyen-gia.xlsx`**
   - Sheet `HuongDan`: thang Saaty 1–9 giải thích tiếng Việt, cách điền.
   - Sheet `ChuyenGia1..5`: ma trận so sánh cặp n×n — chỉ điền nửa trên, nửa dưới tự động nghịch đảo bằng công thức; ô tô màu cho biết ô nào cần điền.
   - Sheet `TongHop`: geometric mean các chuyên gia, trọng số (approximation bằng geometric-mean-of-rows), λmax, CI, CR tự động — CR > 0.1 thì ô báo đỏ.
   - (Số tiêu chí n để tạm 8, dễ thêm/bớt hàng cột sau khi chốt bộ tiêu chí.)
2. **`03_phan-tich\tieu-chi\likert-thu-thap-phan-tich.xlsx`**
   - Sheet `DuLieu`: mỗi hàng 1 người trả lời, cột = thông tin nhân khẩu + từng tiêu chí (1–5); dán trực tiếp từ export Google Form.
   - Sheet `PhanTich`: mean, SD, tần suất từng tiêu chí tự động; cột "Giữ/Loại" theo ngưỡng (ô ngưỡng chỉnh được, mặc định 3.5).

## Phần 3 — Hệ sinh thái skill: phân tích sâu `professional_writing` + repo GitHub bổ trợ

### 3.1 Phân tích sâu skill `professional_writing` v3.2 (đã đọc toàn bộ module học thuật)

Kiến trúc "tòa soạn báo" (Tổng biên tập → 6 ban → 31 staff, quy trình GATE có cổng bàn giao). Bản 3.2 (cập nhật 04-07-2026) đã mở rộng riêng cho học thuật với 7 module mới. **Độ che phủ cho dự án này:**

| Nhu cầu dự án | Module trong skill | Đánh giá |
|---|---|---|
| Literature review có metadata trích dẫn | `research/literature.md` | ✅ Tốt — ép thu đủ tác giả/năm/venue/DOI ngay lúc đọc, phân tầng nguồn primary/secondary, cross-check 2 nguồn cho claim quan trọng |
| Viết chương báo cáo chuẩn IMRaD | `editorial/technical.md` + `academic.md` | ✅ Tốt — Abstract 4 thành phần, research question/gap, hedging học thuật đúng chuẩn (không bị anti-ai xóa nhầm) |
| **Song ngữ VN→EN** (đúng quy trình nhóm: làm việc VN, output EN) | `editorial/academic.md` mục 6 | ✅ **Rất khớp** — bản EN *viết lại độc lập* từ Content Brief, không dịch máy từng câu; quy ước EN riêng ở `review/academic-en.md` |
| Sinh LaTeX + BibTeX | `publishing/latex.md` | ✅ Tốt — preamble đã kiểm chứng compile thật (XeLaTeX + biber, fontspec/polyglossia, biblatex-apa, booktabs, cleveref); ghi sẵn 3 bẫy crash thường gặp |
| Rà soát trích dẫn + cú pháp .tex | `review/citation-check.md`, `latex-check.md` | ✅ Có — đối chiếu citation ↔ references, APA/IEEE/Chicago/Vancouver |
| Chống văn phong AI | `review/anti-ai.md`, `natural.md` | ✅ Có, đã có ngoại lệ academic |

→ **Kết luận: KHÔNG cần clone repo scientific-writer bên ngoài cho phần VIẾT** — `professional_writing` che phủ trọn pipeline literature → draft VN → rewrite EN → citation-check → LaTeX → latex-check, lại được thiết kế sẵn cho tiếng Việt (điều không repo nước ngoài nào có). Điều chỉnh kỹ thuật kéo theo: **sườn LaTeX ở Phần 2b sẽ dùng chuẩn của skill này** — biên dịch bằng **XeLaTeX + biber** (không phải pdflatex), preamble kế thừa mẫu đã kiểm chứng trong `publishing/latex.md` (đổi sang `report` class + `\setmainlanguage{english}` cho bản nộp EN).

**Lỗ hổng còn lại của skill (phần viết):** (a) không có công cụ *tìm* paper — nhưng môi trường Claude Code ở đây có sẵn Scholar Gateway (semantic search paper học thuật) bù được; (b) chưa có pattern học thuật trong `archive/pattern-catalog.md` (nhóm Học thuật đang trống — chính README skill ghi vậy) → sau khi viết xong chương đầu được duyệt, nên lưu làm pattern để các chương sau đồng nhất; (c) không làm slide, không tính toán, không crawl — đúng phần cần bổ sung bên dưới.

### 3.2 Nhu cầu còn thiếu theo phase → giải pháp

| Phase | Năng lực cần | Giải pháp |
|---|---|---|
| 1 | Tìm paper (search) | Scholar Gateway có sẵn trong môi trường + `research/literature.md` lo phần synthesis |
| 3 | Phân tích Likert | **Tạo mới** `likert-analysis` |
| 4+5 | AHP (eigenvector, CI/CR, geometric mean) + TOPSIS (normalization, ranking, sensitivity) | **Tạo mới** `mcdm-toolkit` (kèm script Python để tính đúng, tái lập được) |
| 5 | Crawl CellphoneS + map benchmark | **Tạo mới** `crawl-laptop-data` |
| 6 report | Viết + LaTeX | ✅ `professional_writing` (mục 3.1) |
| 6 slide | Slide đẹp, sinh động | Clone **`pptx`** từ repo chính chủ + skill `dataviz` có sẵn trong Claude Code |
| Xuyên suốt | Đọc/ghi Excel, trích bảng từ PDF paper | Clone **`xlsx`**, **`pdf`** từ repo chính chủ |

**Repo GitHub sẽ clone (chọn lọc từng thư mục skill, không tải cả kho):**
- **[anthropics/skills](https://github.com/anthropics/skills)** — repo chính chủ Anthropic, uy tín nhất mảng này: lấy đúng 3 skill `pptx`, `xlsx`, `pdf`.
- ~~K-Dense-AI/claude-scientific-writer~~ — **bỏ**, trùng chức năng với `professional_writing` mà không hỗ trợ quy trình song ngữ VN→EN.

**Skill tự tạo bằng `skill-creator` (sẵn có trong `tao-skill-danh-gia-skill`):** `mcdm-toolkit`, `crawl-laptop-data`, `likert-analysis` — cả 3 thiết kế output ăn khớp với 2 file Excel ở Phần 2b và xuất bảng LaTeX-ready (booktabs) để cắm thẳng vào `04_bao-cao-latex\tables\`.

Sau khi clone, chạy `audit-skills` (sẵn có) kiểm tra an toàn skill tải về. Skill UI (`taste-skill-main`, `ui-ux-pro-max`) không dùng cho dự án này.

## Thứ tự thực thi

1. Tạo cây thư mục + di chuyển `brainstorm.md`, `MADM.pdf`.
2. Viết `README.md` đầy đủ (workflow 7 phase, task T#.# chi tiết, luật vận hành, quy trình backup mục E).
3. Viết `timeline.md`, `tong-hop-tieu-chi.md`, `_HUONG-DAN.md`; dựng sườn LaTeX đầy đủ chương mục như Phần 2b; viết `05_slide\outline-slide.md`.
3b. Tạo 2 file Excel (AHP + Likert) bằng Python/openpyxl với công thức tự động; nếu máy chưa có Python thì dùng PowerShell/COM Excel hoặc tạo sau khi clone skill `xlsx`.
4. `git init` workspace + `.gitignore` (file tạm LaTeX, inbox) + commit đầu tiên làm baseline backup.
5. Clone chọn lọc skill từ 2 repo trên vào `skill\` (git clone/tải về đúng thư mục skill cần).
6. Tạo 3 skill mới bằng skill-creator, chạy audit-skills kiểm tra skill clone về.
7. Kiểm tra: liệt kê cây thư mục; biên dịch thử sườn LaTeX bằng **XeLaTeX + biber** nếu máy có MiKTeX/TeX Live (chưa có thì ghi hướng dẫn cài trong README, không tự cài); tạo snapshot ZIP đầu tiên `phase0_khoi-tao` vào `07_sao-luu\` để xác nhận quy trình backup chạy được.

## Ngoài phạm vi

Chưa crawl dữ liệu thật, chưa dựng Google Form, chưa viết nội dung báo cáo — làm ở các phase sau theo README.
