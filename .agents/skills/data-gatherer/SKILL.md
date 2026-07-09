---
name: data-gatherer
description: "Thu thập/làm mới dữ liệu laptop văn phòng trên thị trường — crawl CellphoneS theo scope đã chốt, map benchmark PassMark, làm sạch và dựng ma trận quyết định TOPSIS."
---

# data-gatherer (Codex) — Thu thập & làm sạch dữ liệu thị trường

> **Dành cho Codex.** Codex không có subagent như Claude — đọc file này khi làm việc crawl/làm sạch dữ liệu (được `AGENTS.md` gốc mục 5 trỏ tới). Bản Claude tương ứng là subagent `.claude/agents/data-gatherer.md`.

Mục tiêu: crawl + tra benchmark + làm sạch, ghi ra CSV/xlsx sạch — không giữ HTML thô trong ngữ cảnh.

## Ràng buộc
- Bám `.claude/skills/data-pipeline/SKILL.md` (collect → clean → validate → aggregate → export) và `rules/data-ethics.md`.
- Raw crawl → `02_du-lieu-tho/laptop-thi-truong/` KÈM ngày crawl (vùng đóng băng, chỉ ghi mới). Benchmark 1 nguồn/loại (PassMark), ghi ngày truy cập.
- Dữ liệu sạch + ma trận → `03_phan-tich/du-lieu-sach/`, `03_phan-tich/topsis/`.
- `AGENTS.md` mục 0/2.

## Quy trình
```
python .claude/skills/data-pipeline/skills/data-collection/scripts/collect_*.py   # collect
python .claude/skills/data-pipeline/shared/scripts/validate.py <file>             # validate (fail -> sửa -> lại)
```
Ghép benchmark → dựng ma trận quyết định → xuất CSV/xlsx (skill `xlsx`).

## Trả về
Tóm tắt: số máy sau lọc giá, ngày crawl, cột dữ liệu, file đã ghi, cảnh báo chất lượng. Không dán bảng thô dài.
