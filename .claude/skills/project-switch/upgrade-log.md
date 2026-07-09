# Upgrade Log — Lịch sử tiến hoá bộ công cụ (skills + subagents + luật)

> **Mục đích:** file này **đi kèm bộ công cụ** khi copy sang project mới. Nó ghi lại mỗi skill/subagent/luật *đã được nâng cấp những gì, vì sao*, để project sau kế thừa bài học thay vì làm lại từ đầu. `project-switch` đọc file này ở pha Recon và ghi thêm ở pha Log.
>
> **Cách ghi entry (mới nhất lên đầu phần Changelog):**
> ```
> ## YYYY-MM-DD — <tên project / bối cảnh>
> **Giữ / Bỏ / Sửa / Thêm:** …
> **Vì sao:** …
> **Bài học cho project sau:** …
> ```

---

## Component registry (trạng thái hiện tại)

Cột **Portable**: `generic` = mang sang project nào cũng dùng được · `domain` = gắn lĩnh vực, project khác lĩnh vực nên cân nhắc bỏ.

| Component | Loại | Portable | Công dụng |
|---|---|---|---|
| `project-switch` | skill | generic | Bối cảnh hoá toolkit cho project mới (chính file này thuộc về nó) |
| `task-processor` | skill | generic* | Điều phối/định vị task; *routing bên trong gắn pipeline MADM, cần chỉnh khi đổi lĩnh vực |
| `professional-writing` | skill | generic | Viết học thuật/blog VN-EN, LaTeX, citation |
| `skill-smith` | subagent | generic | Tạo → viết chuẩn → audit skill (bọc skill-creator/writing-skills/audit-skills) |
| `literature-researcher` | subagent | generic | Đọc sâu nhiều paper, trích tiêu chí/citation (bọc pdf + professional-writing) |
| `pdf` / `xlsx` / `pptx` | skill | generic | Xử lý file định dạng |
| `mcdm-toolkit` | skill | **domain** | AHP/TOPSIS — chỉ hợp project MCDM/ra quyết định đa tiêu chí |
| `likert-analysis` | skill | **domain** | Phân tích khảo sát Likert |
| `data-pipeline` | skill | generic | Thu thập/làm sạch/xuất dữ liệu có cấu trúc |
| `data-gatherer` | subagent | **domain** | Crawl laptop CellphoneS + PassMark (bọc data-pipeline + xlsx) |
| `supply-chain-consultant` | skill | domain | Tư vấn SCM/logistics |

---

## Changelog

## 2026-07-09 (c) — Chỉnh scope project: laptop văn phòng không khóa ngân sách
**Sửa:** cập nhật scope trong `AGENTS.md`, `README.md`, artifact phỏng vấn v3.0 VN/EN, skeleton LaTeX/slide, `data-gatherer` và `data-pipeline`: dự án tập trung vào tiêu chí mua laptop cho nhân viên văn phòng, không khóa trước một mức giá cụ thể. Giá/ngân sách trở thành một tiêu chí đánh giá hoặc rule lọc dữ liệu sẽ chốt riêng nếu cần.
**Vì sao:** người dùng chốt lại chủ đề rộng hơn — chỉ cần "tiêu chí mua laptop văn phòng", không cần cố định dải giá.
**Bài học cho project sau:** đừng hard-code budget/range vào luật, skill hoặc câu hỏi phỏng vấn nếu đó chỉ là giả định tạm thời; để budget như một biến trong Task Brief hoặc tiêu chí đánh giá.

## 2026-07-09 (b) — Đồng bộ task-processor + luật bảo trì routing
**Sửa:** cập nhật bảng routing `task-processor` (Bước 4) cho đủ 3 subagent (`skill-smith`, `literature-researcher`, `data-gatherer`) + `project-switch`, tách rõ Skills vs Subagents. Thêm mục "Bảo trì routing".
**Thêm (luật):** khi thêm/bớt/gộp/đổi tên skill hoặc subagent, PHẢI đồng bộ 3 nơi — bảng routing task-processor · `AGENTS.md` mục 5 · `upgrade-log.md`. Ghi vào AGENTS.md; `skill-smith` và `project-switch` nhắc/thực hiện ở phần kết.
**Vì sao:** task-processor là nhạc trưởng mặc định; nếu bảng routing lệch danh sách skill/agent thực tế thì nó điều phối sai. Trước đó thêm 3 subagent mà quên cập nhật task-processor.
**Bài học cho project sau:** coi task-processor routing là một "nơi phải cập nhật" bắt buộc mỗi lần đổi toolkit — đừng để nó lệch âm thầm.

## 2026-07-09 — MADM/MCDM Laptop Selection (project gốc của toolkit)
Đây là project nơi bộ công cụ hình thành. Chuỗi nâng cấp trong ngày:

**Thêm:** hạ tầng "một nguồn luật, hai cửa vào" — `AGENTS.md` gốc (tool-agnostic, Codex đọc trực tiếp) + `CLAUDE.md` (import `@AGENTS.md`, phần riêng Skill/Agent tool).
**Sửa:** chuyển skill từ `.agents/skills/` (Antigravity) sang `.claude/skills/` để Claude Code tự nạp; làm phẳng mọi skill về 1 cấp; catalog script CLI trong AGENTS.md để Codex chạy được dù không có cơ chế skill.
**Vì sao:** project chạy song song Claude Code + Codex trong VSCode; hai công cụ đọc cấu hình khác nhau (CLAUDE.md vs AGENTS.md ở gốc; Claude tự nạp `.claude/skills` còn Codex thì không).
**Bài học cho project sau:** luôn đặt luật chung ở `AGENTS.md` gốc + `CLAUDE.md` mỏng import nó; skill để `.claude/skills/<tên>/SKILL.md` (1 cấp); mọi năng lực "tính toán" nên có script CLI để Codex tái dùng.

**Sửa (consolidate):** gom 3 skill authoring rời rạc (`skill-creator`/`writing-skills`/`audit-skills`) thành lớp orchestrator `skill-smith` — subagent Claude `.claude/agents/skill-smith.md` + mirror `.codex/skills/skill-smith/`. Giữ 3 skill gốc làm kho tri thức/tooling.
**Vì sao:** ba skill là một vòng đời liền mạch (tạo → viết → audit); rời rạc khiến phải tự ghép.
**Bài học:** mẫu **subagent BỌC skill** (frontmatter `skills:`) — subagent lo cô lập ngữ cảnh, skill lo tri thức; không nhân bản.

**Thêm (subagent):** `literature-researcher` (đọc sâu paper) + `data-gatherer` (crawl dữ liệu), theo tiêu chí Anthropic *Sub-agents*.
**Vì sao:** hai việc này sinh output rất dài, tự chứa, và lặp cùng loại thợ (Phase 1 đã bung 3 subagent đọc PDF thủ công) — đúng điều kiện nên tách subagent. Ngược lại giữ làm skill: `task-processor`, `mcdm-toolkit`, `likert-analysis`, phần viết của `professional-writing` (cần đối đáp nhiều vòng, chia sẻ ngữ cảnh — ca "hội thoại chính").
**Bài học:** quyết skill-hay-subagent theo 3 câu hỏi — output có dài dòng không · việc có tự chứa không · có lặp cùng loại thợ không. "Có" cả ba → subagent; cần đối đáp nhiều vòng → skill.

**Thêm:** chính `project-switch` + `upgrade-log.md` này, để việc bê toolkit sang project sau có quy trình và có lịch sử.
