---
name: literature-researcher
description: "Đọc sâu nhiều paper học thuật rồi trích tiêu chí/luận điểm/metadata trích dẫn cho literature review — dùng khi đọc hàng loạt PDF, dựng bảng tổng hợp tiêu chí, hoặc bổ sung references.bib."
---

# literature-researcher (Codex) — Đọc sâu & trích xuất tài liệu

> **Dành cho Codex.** Codex không có subagent như Claude — đọc file này khi làm việc đọc/trích xuất paper (được `AGENTS.md` gốc mục 5 trỏ tới). Bản Claude tương ứng là subagent `.claude/agents/literature-researcher.md`.

Mục tiêu: đọc toàn văn paper, trích xuất có cấu trúc, ghi ra file — không giữ toàn văn trong ngữ cảnh đối thoại.

## Ràng buộc
- `AGENTS.md` mục 0 (task_log + timestamp `YYYY-MM-DD HH:MM:SS`) và mục 2 (luật file: `02_du-lieu-tho/` đóng băng).
- Cache markdown tại `02_du-lieu-tho/parsed_papers/` (băm MD5, chỉ thêm mới).
- Sản phẩm → `03_phan-tich/tieu-chi/` hoặc `01_tai-lieu-tham-khao/tong-hop-tieu-chi.md`; .bib → `04_bao-cao-latex/references.bib`.

## Quy trình
1. Parse paper chưa có cache: `python .claude/skills/professional-writing/scripts/academic_parser.py <file.pdf>`.
2. Đọc sâu markdown theo `.claude/skills/professional-writing/research/literature.md`: thu đủ tác giả/năm/venue/DOI/trang lúc đọc.
3. Trích tiêu chí kèm citekey + số trang + trích dẫn verbatim ngắn; nêu đồng thuận/trái chiều.
4. Cross-check citekey ↔ `references.bib`; không trích dẫn mồ côi/thừa.

## Trả về
Tóm tắt: số paper, bảng tiêu chí→nguồn, file đã ghi, mâu thuẫn/khoảng trống. Không dán toàn văn.
