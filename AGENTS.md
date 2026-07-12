# AGENTS.md — Dự án MADM/MCDM: Bộ tiêu chí ra quyết định mua laptop

> **Nguồn luật chung cho MỌI AI agent** làm việc trên repo này.
> - **Claude Code** đọc file này gián tiếp qua `CLAUDE.md` (`@AGENTS.md`).
> - **Codex** (và các agent theo chuẩn agents.md) đọc trực tiếp file này ở gốc repo.
>
> Sửa luật thì sửa ở ĐÂY — không rải rác ra nhiều file. `README.md` là sổ tay cho **người**; file này là luật cho **agent**.

---

## 0. Giao thức mỗi phiên (BẮT BUỘC)

1. **Đọc `00_quan-ly-du-an/task_log.md` ĐẦU TIÊN** để nắm trạng thái, việc đang dở, cảnh báo.
2. Đọc `README.md` (workflow) hoặc `00_quan-ly-du-an/timeline.md` khi cần thêm ngữ cảnh.
3. **Định vị** yêu cầu vào pipeline 7 phase (mục 1) trước khi làm. Nếu yêu cầu nhảy cóc trình tự (vd chạy TOPSIS khi chưa chốt trọng số AHP) — DỪNG, cảnh báo, chỉ tiếp tục khi người dùng xác nhận.
4. **Ghi `task_log.md` ngay sau khi xong một đầu việc** (không đợi hết cả phiên dài) — nếu phiên bị ngắt giữa chừng, log vẫn phải phản ánh đúng tiến độ thật.

### 0.1 Quy định ghi `task_log.md` (BẮT BUỘC, áp dụng như nhau cho Claude Code và Codex)

- **Vị trí:** LUÔN thêm entry mới vào **đầu** mục `## 2. Công việc vừa hoàn thành (Recently Completed)`, ngay dưới dòng header — mới nhất nằm trên cùng. **Không** thêm entry mới vào mục `## 5. Agent research log` — mục đó là log lịch sử cũ trước khi quy định này có hiệu lực, đã đóng, chỉ giữ lại để tra cứu.
- **Định dạng bắt buộc mỗi entry:**
  ```
  - [x] [YYYY-MM-DD HH:MM:SS] **Tiêu đề ngắn 1 dòng.** Nội dung chi tiết.
  ```
  Timestamp lấy giờ thực tế lúc ghi (không bịa, không copy giờ của entry trước).
- **Nội dung chi tiết phải trả lời đủ 4 câu hỏi** (thiếu câu nào thì entry chưa đạt):
  1. *Đã làm gì* — mô tả cụ thể, không chung chung ("đã sửa Ch3" là chưa đủ, phải nói sửa gì, ở đâu).
  2. *Tại sao* — bám theo yêu cầu nào của người dùng, hoặc phát hiện/lỗi gì dẫn tới việc này.
  3. *File nào đã đổi* — liệt kê đường dẫn cụ thể (không chỉ tên module chung chung).
  4. *Kiểm chứng ra sao* — compile sạch (số trang, 0 undefined), test pass, số liệu đối chiếu, hay bằng chứng cụ thể khác. Nếu việc còn dang dở, ghi rõ phần nào chưa xong và bước tiếp theo là gì.
- **Đồng thời cập nhật dòng "Cập nhật gần nhất (...)" ở mục `## 1. Trạng thái hiện tại`** — đổi timestamp + tóm tắt 1 câu khớp với entry mới nhất vừa thêm ở mục 2. Đây là dòng đầu tiên người/agent phiên sau nhìn thấy, phải luôn khớp với thực tế mới nhất.
- **Không có ngoại lệ "việc nhỏ khỏi cần ghi".** Việc nhỏ thì entry ngắn, nhưng vẫn phải có — chuỗi việc-nhỏ-không-ghi là cách trạng thái dự án lệch khỏi thực tế nhanh nhất, nhất là khi chuyển đổi qua lại giữa Claude Code và Codex (hai agent không chia sẻ hội thoại, chỉ chia sẻ file này).
- **Không tự xóa hoặc viết đè entry cũ** để "dọn gọn" — muốn rút gọn lịch sử, việc đó do người dùng quyết định, không tự ý làm.

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
| Trọng số AHP (1 chuyên gia) | `python .claude/skills/mcdm-toolkit/scripts/ahp.py matran.csv` |
| AHP tổng hợp nhiều chuyên gia | `python .claude/skills/mcdm-toolkit/scripts/ahp.py cg1.csv cg2.csv [--latex out.tex]` |
| Xếp hạng TOPSIS | `python .claude/skills/mcdm-toolkit/scripts/topsis.py ma-tran-quyet-dinh.csv [--latex out.tex] [--sensitivity]` |
| Phân tích Likert | `python .claude/skills/likert-analysis/scripts/likert.py survey.csv [--threshold 3.5] [--cols "C1,C2"] [--latex out.tex]` |

Quy tắc: ma trận AHP nào **CR > 0.1** bị coi là hỏng → DỪNG, báo người dùng cặp so sánh mâu thuẫn, không tự nới ngưỡng. Bảng xuất `--latex` dùng booktabs (không kẻ dọc), lưu vào `04_bao-cao-latex/tables/`.

---

## 5. Định tuyến chuyên môn (routing)

Skills nằm ở `.claude/skills/<tên>/SKILL.md`.
- **Claude Code:** tự nạp, gọi qua Skill tool theo `name` trong routing.
- **Codex / agent khác:** đọc `.claude/skills/<tên>/SKILL.md` trực tiếp để theo đúng quy trình, và chạy script ở mục 4.

| Loại việc | Module (`.claude/skills/…`) |
|---|---|
| Điều phối / định vị task mơ hồ, đa bước | `task-processor` |
| Bối cảnh hoá toolkit khi sang project mới | `project-switch` (đề xuất→chờ duyệt) |
| Viết VN/EN, LaTeX, citation, Đọc sâu nhiều paper, trích tiêu chí/citation | `professional-writing` |
| Tính AHP, TOPSIS, sensitivity | `mcdm-toolkit` |
| Phân tích khảo sát Likert | `likert-analysis` |
| Thao tác nhanh dữ liệu (làm sạch lẻ) | `data-pipeline` |
| Câu hỏi logistics/SCM chuyên sâu | `supply-chain-consultant` |
| Dựng slide / Excel / trích PDF | `pptx` / `xlsx` / `pdf` |
| Tạo/đọc/sửa/QA Office files (.docx/.xlsx/.pptx) qua CLI | `officecli` (dùng chung cho cả Claude và Codex, không có bản mirror riêng) |

Điểm vào mặc định cho yêu cầu mơ hồ hoặc đa phase: **`task-processor`** (Định vị → Làm rõ → Task Brief → Điều phối).

**Subagents (`.claude/agents/`) — chỉ Claude Code có, chạy phòng riêng cô lập ngữ cảnh.** Dùng cho việc sinh nhiều output không cần giữ trong hội thoại chính; **subagent bọc skill** (frontmatter `skills:`), không thay thế skill — khi cần chạy nhanh trong chat thì gọi thẳng skill. Codex không có cơ chế subagent → đọc mirror ở `.codex/skills/<tên>/SKILL.md` để làm việc tương đương.

| Subagent (Claude) | Bọc skill | Mirror Codex | Dùng khi |
|---|---|---|---|
| `skill-smith` | skill-creator, writing-skills, audit-skills | `.codex/skills/skill-smith/` | Tạo → viết chuẩn → audit một skill |
| `data-gatherer` | data-pipeline, xlsx | `.codex/skills/data-gatherer/` | Crawl/làm mới dữ liệu laptop khối lượng lớn |
| `office-docs` | officecli, pptx, xlsx, pdf | *(không có, Codex dùng thẳng skill `officecli`)* | Xử lý Office files dài/nhiều file cần render/validate/QA riêng |

Đọc sâu nhiều paper/trích tiêu chí đã được gộp lại vào skill `professional-writing` (không còn subagent `literature-researcher` riêng — xem `upgrade-log.md` 2026-07-09(e)/2026-07-11 để biết lý do).

**Khi THÊM / BỚT / GỘP / ĐỔI TÊN một skill hoặc subagent — cập nhật đồng bộ 3 nơi (việc chưa xong nếu thiếu nơi nào):**
1. **Bảng routing `task-processor`** (Bước 4 trong `.claude/skills/task-processor/SKILL.md`) — để nhạc trưởng điều phối đúng.
2. **`AGENTS.md` mục 5** — bảng routing + bảng subagent ở trên.
3. **`.claude/skills/project-switch/upgrade-log.md`** — ghi đã đổi gì · vì sao · bài học (file này đi kèm toolkit khi copy sang project mới).

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

---

## 9. Phân vai Claude Code ⇄ Codex (để hai agent không giẫm chân)

Gợi ý mặc định, không cứng nhắc:

- **Claude Code:** viết học thuật/song ngữ, điều phối đa bước (`task-processor`), thao tác skill/subagent, biên tập báo cáo/slide, quản lý ngữ cảnh dài.
- **Codex:** refactor/sửa script Python, chạy nhanh tính toán CLI (mục 4), thao tác lặp trên nhiều file, sinh code tiện ích.

Dù là agent nào: **mục 0 (giao thức phiên) và mục 2 (luật vàng file) luôn áp dụng.** Ghi lại đầu việc vào `task_log.md` với timestamp khi kết thúc.
