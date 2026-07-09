# CLAUDE.md

Luật dự án dùng chung nằm ở **`AGENTS.md`** (nguồn duy nhất, dùng chung với Codex). Đọc và tuân thủ toàn bộ file đó:

@AGENTS.md

---

## Phần riêng cho Claude Code

- **Skills:** nằm ở `.claude/skills/<tên>/SKILL.md`, được nạp tự động. Gọi qua **Skill tool** theo bảng routing ở `AGENTS.md` mục 5. Điểm vào mặc định cho yêu cầu mơ hồ/đa bước: skill **`task-processor`**.
- **Subagents:** nằm ở `.claude/agents/`, gọi qua Agent tool (chạy phòng riêng, cô lập ngữ cảnh; mỗi cái bọc sẵn skill liên quan): **`skill-smith`** (tạo → viết chuẩn → audit skill), **`literature-researcher`** (đọc sâu nhiều paper, trích tiêu chí/citation), **`data-gatherer`** (crawl/làm sạch dữ liệu laptop). Mỗi subagent có bản mirror cho Codex ở `.codex/skills/<tên>/`.
- **Nhắc lại 2 điều tối quan trọng** (chi tiết ở AGENTS.md): (1) đọc `00_quan-ly-du-an/task_log.md` **đầu mỗi phiên**, cập nhật kèm timestamp `YYYY-MM-DD HH:MM:SS` trước khi kết thúc; (2) `02_du-lieu-tho/` đóng băng, `06_nop-bai/` chỉ chứa bản nộp cuối.
- **Chuyển project mới:** dùng skill **`project-switch`** để phân tích bối cảnh và đề xuất chỉnh lại toolkit (structure, AGENTS/CLAUDE, skills, subagents). Mọi nâng cấp skill/agent/luật ghi vào `.claude/skills/project-switch/upgrade-log.md`.
- **Memory:** ghi chú bền vững nằm ở `~/.claude/projects/D--LogManagement/memory/` (index: `MEMORY.md`).
