---
name: skill-smith
description: "Vòng đời tạo/cải tiến/audit một Agent Skill cho dự án MADM — dùng khi tạo skill mới, refactor SKILL.md, hoặc kiểm định an toàn skill, cho cả Claude Code (.claude/skills/) lẫn Codex (.codex/skills/)."
---

# skill-smith (Codex) — Nhạc trưởng vòng đời skill

> **Dành cho Codex.** Codex không tự nạp skill như Claude Code — đọc file này khi làm việc skill-authoring (được `AGENTS.md` gốc mục 5 trỏ tới). Bản này tự chứa phần hướng dẫn và trỏ tới **cùng kho tri thức/tooling canonical** trong `.claude/skills/*` (đều nằm trong repo, đọc bằng file bình thường) — không nhân bản.

Ba pha nối tiếp: **tạo → viết chuẩn → audit**. Mỗi pha mở file skill gốc tương ứng rồi bám theo.

## Nguyên tắc
- Skill mới đặt ở `.claude/skills/<ten>/` (Claude tự nạp) và/hoặc `.codex/skills/<ten>/` (Codex đọc khi được trỏ). Sinh cho cả hai khi cần chạy song song.
- Tuân thủ `AGENTS.md`: mục 0 (đọc `00_quan-ly-du-an/task_log.md` đầu phiên; cập nhật timestamp `YYYY-MM-DD HH:MM:SS` cuối phiên) và mục 2 (luật vàng file: không ghi vào `02_du-lieu-tho/`, `06_nop-bai/`).

## Pha 1 — Tạo / scaffold
Nguồn: `.claude/skills/skill-creator/SKILL.md` (Discovery → Brainstorm → Enhance → Generate → Validate → Install; đã hỗ trợ sinh cho cả Claude Code và Codex).
```
python .claude/skills/skill-creator/scripts/init_skill.py <ten-skill> --path <thư-mục-cha>
```
(`--path` bắt buộc, vd `.claude/skills` hoặc `.codex/skills`.)
Tham khảo `.claude/skills/skill-creator/references/workflows.md` và `output-patterns.md` để chọn loại skill (technique / pattern / reference).

## Pha 2 — Viết chuẩn
Nguồn: `.claude/skills/writing-skills/SKILL.md`.
- `description`: chỉ điều kiện kích hoạt, ngôi thứ ba, mở đầu "Use when…", KHÔNG nhét workflow.
- Thân skill: Overview → When to Use / When NOT to Use → Quick Reference → Core Pattern → Common Mistakes → Red Flags.
- Tài liệu: `.claude/skills/writing-skills/anthropic-best-practices.md`, `persuasion-principles.md`, `testing-skills-with-subagents.md`. Sơ đồ: `render-graphs.js` + `graphviz-conventions.dot`.

## Pha 3 — Audit (bắt buộc)
Nguồn: `.claude/skills/audit-skills/SKILL.md` — static analysis bảo mật (pattern độc hại, rò rỉ dữ liệu, payload che giấu, lệnh rủi ro). Chỉ bàn giao khi sạch.

## Kiểm tra nhanh
```
python .claude/skills/skill-creator/scripts/quick_validate.py <thư-mục-skill>
python .claude/skills/skill-creator/scripts/package_skill.py <ten-skill>   # khi cần đóng gói
```

## Kết thúc
Báo: skill tạo/sửa ở đâu (Claude/Codex), kết quả validate + audit, nhắc cập nhật routing `AGENTS.md` mục 5 nếu thêm skill mới.
