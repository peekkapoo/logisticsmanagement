---
name: project-switch
description: "Bối cảnh hoá bộ công cụ đã copy sang project mới — phân tích mục đích/cấu trúc project rồi đề xuất chỉnh AGENTS.md, structure, skill/subagent cho phù hợp; ghi upgrade-log."
---

# project-switch (Codex) — Bối cảnh hoá toolkit cho project mới

> **Dành cho Codex.** Bản Claude tương ứng là skill `.claude/skills/project-switch/SKILL.md`. Lịch sử tiến hoá toolkit ở `.claude/skills/project-switch/upgrade-log.md` — đọc trước khi làm.

Mỗi project có mục đích/cấu trúc/quy ước riêng; toolkit cũ chưa chắc vừa. Skill này **phân tích project mới rồi ĐỀ XUẤT cách chỉnh toolkit, CHỜ DUYỆT trước khi ghi đè**.

## Nguyên tắc: ĐỀ XUẤT → CHỜ DUYỆT
Không tự ghi đè `AGENTS.md`/`CLAUDE.md`/skill. Luôn trình kế hoạch, chờ người dùng đồng ý.

## Quy trình 5 pha
1. **Recon:** đọc `README`, cây thư mục, `git log`, tech stack; đọc `.claude/skills/project-switch/upgrade-log.md` để hiểu toolkit đã tiến hoá ra sao (cái nào generic / cái nào gắn lĩnh vực cũ).
2. **Gap analysis:** luật/cấu trúc còn đúng? Skill nào giữ / bỏ (gắn lĩnh vực cũ) / thêm? Subagent còn hợp tiêu chí?
3. **Proposal (GATE):** trình bảng Giữ/Bỏ/Sửa/Thêm + bản nháp `AGENTS.md`. **Chờ duyệt.**
4. **Apply (sau khi duyệt):** viết lại `AGENTS.md`; dựng structure; prune/tạo skill (tạo mới qua `skill-smith`, kèm mirror `.codex/skills/`). Mỗi lần thêm/bớt skill/subagent, đồng bộ 3 nơi: bảng routing `task-processor`, `AGENTS.md` mục 5, `upgrade-log.md`.
5. **Log:** ghi entry vào `upgrade-log.md` (ngày, bối cảnh, Giữ/Bỏ/Sửa/Thêm, vì sao, bài học) + cập nhật Component registry.

## Red flags
- Ghi đè khi chưa duyệt (P3). — Giữ skill lĩnh vực cũ mà chưa hỏi. — Kết thúc mà chưa ghi upgrade-log.
