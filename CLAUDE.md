# CLAUDE.md

Luật dự án dùng chung nằm ở **`AGENTS.md`** (nguồn duy nhất, dùng chung với Codex). Đọc và tuân thủ toàn bộ file đó:

@AGENTS.md

---

## Phần riêng cho Claude Code

- **Skills:** nằm ở `.claude/skills/<tên>/SKILL.md`, được nạp tự động. Gọi qua **Skill tool** theo bảng routing ở `AGENTS.md` mục 5. Điểm vào mặc định cho yêu cầu mơ hồ/đa bước: skill **`task-processor`**.
- **Subagents:** nằm ở `.claude/agents/`, gọi qua Agent tool (chạy phòng riêng, cô lập ngữ cảnh; mỗi cái bọc sẵn skill liên quan): **`skill-smith`** (tạo → viết chuẩn → audit skill), **`data-gatherer`** (crawl/làm sạch dữ liệu laptop), **`office-docs`** (xử lý Office files dài/nhiều file). Mỗi subagent trừ `office-docs` có bản mirror cho Codex ở `.codex/skills/<tên>/`.
- **Nhắc lại 2 điều tối quan trọng** (chi tiết ở AGENTS.md): (1) đọc `00_quan-ly-du-an/task_log.md` **đầu mỗi phiên**, cập nhật kèm timestamp `YYYY-MM-DD HH:MM:SS` trước khi kết thúc; (2) `02_du-lieu-tho/` đóng băng, `06_nop-bai/` chỉ chứa bản nộp cuối.
- **Chuyển project mới:** dùng skill **`project-switch`** để phân tích bối cảnh và đề xuất chỉnh lại toolkit (structure, AGENTS/CLAUDE, skills, subagents). Mọi nâng cấp skill/agent/luật ghi vào `.claude/skills/project-switch/upgrade-log.md`.

## Compact Instructions

Khi tóm tắt hội thoại (tự động hoặc `/compact`), luôn giữ lại:
- Đường dẫn file `.tex`/`.md` đang chỉnh sửa (chương report, `paper.tex`, hay tài liệu Phase nào).
- Citekey đã xác minh tồn tại trong `references.bib` và citekey nào còn thiếu/chờ user bổ sung.
- Quyết định cấu trúc đã chốt cho Report (`main.tex`) và Scientific Paper (`paper.tex`) — không suy luận lại từ đầu.
- Phase hiện tại của dự án theo `00_quan-ly-du-an/task_log.md` và bước GATE đang ở đâu (research/editorial/review).
- Bất kỳ cảnh báo biên dịch LaTeX (`undefined citation/reference`) chưa được giải quyết.

Có thể bỏ qua khi tóm tắt:
- Nội dung thô/log chi tiết từ Explore agent hoặc subagent research (đã tổng hợp thành kết luận thì không cần giữ nguyên văn).
- Log biên dịch `xelatex`/`biber` đầy đủ (chỉ cần kết luận: sạch hay còn lỗi gì).
- Trích dẫn full-text dài từ paper tham khảo đã được rút gọn thành luận điểm trong chương viết.
