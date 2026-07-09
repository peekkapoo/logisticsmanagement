# AGENTS.md — Dự án MADM/MCDM: Bộ tiêu chí ra quyết định mua laptop

> **Nguồn luật chung cho hệ thống Antigravity IDE** làm việc trên repo này.
> File này được nạp tự động thông qua Workspace Customizations Root.
>
> Sửa luật thì sửa ở ĐÂY — không rải rác ra nhiều file. `README.md` là sổ tay cho **người**; file này là luật cho **agent**.

---

## 0. Giao thức mỗi phiên (BẮT BUỘC)

1. **Đọc `00_quan-ly-du-an/task_log.md` ĐẦU TIÊN** để nắm trạng thái, việc đang dở, cảnh báo.
2. Đọc `README.md` (workflow) hoặc `00_quan-ly-du-an/timeline.md` khi cần thêm ngữ cảnh.
3. **Định vị** yêu cầu vào pipeline 7 phase (mục 1) trước khi làm. Nếu yêu cầu nhảy cóc trình tự (vd chạy TOPSIS khi chưa chốt trọng số AHP) — DỪNG, cảnh báo, chỉ tiếp tục khi người dùng xác nhận.
4. **Kết thúc phiên/đầu việc:** cập nhật `task_log.md`. Mỗi mục ghi kèm timestamp chuẩn `YYYY-MM-DD HH:MM:SS`.

---

## 1. Dự án là gì (snapshot)

Đồ án nhóm môn Logistics Management: xây bộ tiêu chí mua laptop qua ba giai đoạn (tổng quan tài liệu → phỏng vấn chuyên gia → khảo sát Likert), tính trọng số bằng **AHP**, xếp hạng laptop thực tế bằng **TOPSIS**.

- **Persona chốt:** *nhân viên văn phòng*, tình huống mua laptop phục vụ công việc văn phòng. **Không khóa trước một mức giá cụ thể**; giá cả/ngân sách là một tiêu chí đánh giá hoặc một rule lọc dữ liệu sẽ chốt riêng nếu cần. (KHÔNG dùng "thiết kế đồ họa" — persona đó đã bị loại bỏ.)
- **Ngôn ngữ:** làm việc nội bộ bằng **tiếng Việt**; chỉ **báo cáo LaTeX cuối + slide** là **tiếng Anh**, viết lại độc lập (không dịch máy từng câu).
- **Sản phẩm nộp:** báo cáo học thuật LaTeX (EN) + slide thuyết trình (EN).

Pipeline 7 phase (chi tiết task T#.# trong `README.md` mục 5): **P0** khởi động · **P1** literature review · **P2** phỏng vấn chuyên gia · **P3** khảo sát Likert · **P4** AHP · **P5** dữ liệu laptop + TOPSIS · **P6** báo cáo & slide.

---

## 2. Ba luật vàng về file (không ngoại lệ)

1. **`02_du-lieu-tho/` là vùng ĐÓNG BĂNG.** File vào rồi thì không sửa, không xóa. Muốn xử lý → copy sang `03_phan-tich/` rồi làm trên bản copy.
2. **`06_nop-bai/` CHỈ chứa bản nộp cuối** đã được nhóm duyệt. Không bao giờ tự ghi vào đây, không có "ghi tạm".
3. **Mọi file thành viên gửi đi qua `02_du-lieu-tho/inbox/`** trước, rồi mới đổi tên đúng quy ước và phân loại.

File tạm/nháp của agent (script thử nghiệm, output trung gian) để trong `scratch/` — **không** commit, **không** để lẫn vào `02/`, `03/`, `06/`.

---

## 3. Quy ước đặt tên file

```
YYYY-MM-DD_<ten-tai-lieu>_v<X.Y>_<trangthai>_<nguoi>.<ext>
Ví dụ: 2026-07-10_kich-ban-phong-van_v2.1_draft_an.md
```

- `vX.Y`: X tăng khi thay đổi lớn, Y tăng khi sửa nhỏ.
- `<trangthai>`: `draft` → `review` → `final`. File `final` không sửa; muốn sửa tạo version mới.
- Bản cũ chuyển vào thư mục con `_cu/` tại chỗ, không xóa.
- PDF bài báo: `TacGia_Nam_TuKhoa.pdf`, khớp citekey trong `references.bib`.
- Dữ liệu thị trường (laptop, benchmark) **bắt buộc có ngày** trong tên file.

---

## 4. Catalog công cụ — script CLI (chạy trực tiếp)

Mọi tính toán dùng script đã kiểm thử, **tuyệt đối không tự tính tay**. Chạy từ gốc repo:

| Việc | Lệnh |
|---|---|
| Trọng số AHP (1 chuyên gia) | `python .agents/skills/mcdm-toolkit/scripts/ahp.py matran.csv` |
| AHP tổng hợp nhiều chuyên gia | `python .agents/skills/mcdm-toolkit/scripts/ahp.py cg1.csv cg2.csv [--latex out.tex]` |
| Xếp hạng TOPSIS | `python .agents/skills/mcdm-toolkit/scripts/topsis.py ma-tran-quyet-dinh.csv [--latex out.tex] [--sensitivity]` |
| Phân tích Likert | `python .agents/skills/likert-analysis/scripts/likert.py survey.csv [--threshold 3.5] [--cols "C1,C2"] [--latex out.tex]` |
| Parse PDF paper → Markdown | `python .agents/skills/professional-writing/scripts/academic_parser.py <file.pdf>` |

Quy tắc: ma trận AHP nào **CR > 0.1** bị coi là hỏng → DỪNG, báo người dùng cặp so sánh mâu thuẫn, không tự nới ngưỡng. Bảng xuất `--latex` dùng booktabs (không kẻ dọc), lưu vào `04_bao-cao-latex/tables/`.

---

## 5. Định tuyến chuyên môn (routing)

Skills nằm ở `.agents/skills/<tên>/SKILL.md` và được tự động phát hiện theo Antigravity IDE Workspace Customizations.

| Loại việc | Module (`.agents/skills/…`) |
|---|---|
| Điều phối / định vị task mơ hồ, đa bước | `task-processor` |
| Bối cảnh hoá toolkit khi sang project mới | `project-switch` (đề xuất→chờ duyệt) |
| Viết VN/EN, LaTeX, citation, Đọc sâu nhiều paper, trích tiêu chí/citation | `professional-writing` |
| Tính AHP, TOPSIS, sensitivity | `mcdm-toolkit` |
| Phân tích khảo sát Likert | `likert-analysis` |
| Crawl/làm mới dữ liệu laptop khối lượng lớn, benchmark | `data-gatherer` |
| Thao tác nhanh dữ liệu (làm sạch lẻ) | `data-pipeline` |
| Câu hỏi logistics/SCM chuyên sâu | `supply-chain-consultant` |
| Dựng slide / Excel / trích PDF | `pptx` / `xlsx` / `pdf` |
| Tạo/đọc/sửa/QA Office files (.docx/.xlsx/.pptx) qua CLI | `officecli` |
| Tạo/cải tiến/audit skill | `skill-smith` |

Điểm vào mặc định cho yêu cầu mơ hồ hoặc đa phase: **`task-processor`** (Định vị → Làm rõ → Task Brief → Điều phối).

**Khi THÊM / BỚT / GỘP / ĐỔI TÊN một skill — cập nhật đồng bộ 3 nơi (việc chưa xong nếu thiếu nơi nào):**
1. **Bảng routing `task-processor`** (Bước 4 trong `.agents/skills/task-processor/SKILL.md`) — để nhạc trưởng điều phối đúng.
2. **`AGENTS.md` mục 5** — bảng routing ở trên.
3. **`.agents/skills/project-switch/upgrade-log.md`** — ghi đã đổi gì · vì sao · bài học (file này đi kèm toolkit khi copy sang project mới).

Khi chuyển sang project mới, dùng skill `project-switch` để bối cảnh hoá lại toàn bộ toolkit.

---

## 6. Quy ước kỹ thuật

- **LaTeX (`04_bao-cao-latex/`):** biên dịch bằng **XeLaTeX + biber** (đã cấu hình trong `.vscode/settings.json`, recipe `xelatex ➞ biber ➞ xelatex ➞ xelatex`). Không dùng pdflatex. Nếu không có IDE: chạy `xelatex main` → `biber main` → `xelatex main` ×2.
- **Viết báo cáo:** nháp tiếng Việt trước, viết lại tiếng Anh độc lập qua `professional-writing`.
- **AHP/TOPSIS:** luôn qua script ở mục 4; kết quả kèm file tái lập được.

---

## 7. Chuẩn Academic Writing & Cross-Reference

Khi viết văn bản học thuật (literature review, phân tích, chương báo cáo):

1. **KHÔNG** gạch đầu dòng hay nhãn in đậm kiểu máy (`**Khái niệm:**`). Viết thành đoạn văn liền mạch, độ dài biến thiên tự nhiên, thể hiện rõ đồng thuận/trái chiều (agreements/disagreements).
2. **In-text citation linh hoạt:** tích hợp vào câu như chủ thể hành động.
   - VN: *"Theo Nguyễn và cộng sự (2024)…"*
   - EN: chia thì đúng chuẩn academic — *"Smith et al. (2023) argued that…"* / *"Recent evidence suggests… (Doe, 2024)"*.
3. **Cross-Reference Check:** danh mục "Tài liệu tham khảo" CHỈ chứa tài liệu thực sự được trích trong bài. Cấm bốc cả database vào danh mục.

---

## 8. Chuẩn Tech-blog `08_new_knowledge/`

"Bộ não thứ hai" của người dùng Non-IT. Bài viết vào đây **bắt buộc**:

1. **Luồng tư duy 5 bước (ẩn, KHÔNG đặt tiêu đề máy móc kiểu "The Hook"):** Nỗi đau thực tế → Ẩn dụ đời thường (Mental Model) → Bản chất học thuật → Giải pháp/code → **Nguồn tham khảo** (footnote `[1]`, `[2]` từ official docs / forum uy tín / paper).
2. **Quy trình:** dùng skill `professional-writing` để đảm bảo research + văn phong đồng cảm, de-jargonized.
3. **Tiêu đề H1 trong bài KHÔNG chứa tiền tố số** ("Bài 01:"). Đánh số chỉ dùng cho tên file.
