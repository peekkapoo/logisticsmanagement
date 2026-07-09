---
name: project-switch
description: "Use when a copied Claude/Codex toolkit lands in a new project and must be re-contextualized — analyzing the project's purpose and structure, then adapting AGENTS.md, CLAUDE.md, folder structure, skills, and subagents to fit. Trigger on 'project-switch', 'chuyển project', 'khởi tạo/thiết lập project mới', 'adapt toolkit', 'tinh chỉnh skill cho project', 'bối cảnh hoá'."
---

# project-switch — Bối cảnh hoá bộ công cụ cho project mới

Bạn mang nguyên `.claude/`, `.codex/`, `AGENTS.md`, `CLAUDE.md` từ project cũ sang project mới. Mỗi project có mục đích, cấu trúc, quy ước riêng — bộ công cụ cũ chưa chắc vừa. Skill này **phân tích project mới rồi đề xuất cách chỉnh lại toàn bộ toolkit cho khớp**, và ghi lại quá trình vào `upgrade-log.md` để các project sau hiểu lịch sử phát triển.

## When to Use
- Vừa copy toolkit sang một project mới (khác lĩnh vực/cấu trúc).
- Muốn rà lại xem skill/subagent/luật hiện tại còn hợp với project này không.

## When NOT to Use
- Đang giữa một task chuyên môn (viết, tính toán, crawl) — dùng skill/subagent tương ứng.
- Chỉ sửa một file lẻ — sửa thẳng, không cần cả quy trình.

## Nguyên tắc vận hành: ĐỀ XUẤT → CHỜ DUYỆT
Skill này **không tự ghi đè**. Luôn trình kế hoạch và **chờ người dùng duyệt** trước khi đụng `AGENTS.md`, `CLAUDE.md`, hay bất kỳ skill/agent nào. Áp dụng luật vàng file của project đích nếu đã có.

## Quy trình 5 pha

Copy checklist này và tick dần:
```
- [ ] P1. Recon — hiểu project mới + đọc upgrade-log
- [ ] P2. Gap analysis — toolkit hiện có so với nhu cầu
- [ ] P3. Proposal — trình kế hoạch, CHỜ DUYỆT (GATE)
- [ ] P4. Apply — chỉ sau khi được duyệt
- [ ] P5. Log — ghi upgrade-log
```

### P1 — Recon (hiểu bối cảnh)
- Đọc dấu hiệu project: `README`, tài liệu mục tiêu, cây thư mục, tech stack, `git log`, file cấu hình. Với project lớn/mơ hồ, có thể ủy thác quét rộng cho subagent `Explore`.
- **Đọc `.claude/skills/project-switch/upgrade-log.md`** để hiểu bộ công cụ này *là gì*, đã tiến hoá ra sao, cái nào generic cái nào gắn lĩnh vực cũ.
- Chốt một câu: "Project này là gì, mục tiêu, quy ước, pipeline (nếu có)."

### P2 — Gap analysis
Đối chiếu toolkit hiện tại với nhu cầu project mới:
- **Luật/cấu trúc:** `AGENTS.md`/`CLAUDE.md` còn đúng không? Pipeline/luật file cần viết lại thế nào? Cây thư mục có cần dựng lại?
- **Skill:** cái nào giữ (generic), cái nào **gỡ/vô hiệu** (gắn chặt lĩnh vực cũ, vd `mcdm-toolkit` cho project không phải MCDM), cái nào **thiếu cần tạo mới**.
- **Subagent:** tiêu chí Anthropic (output dài dòng / tự chứa / lặp cùng loại thợ) còn đúng với việc của project này không.

### P3 — Proposal (GATE — chờ duyệt)
Trình bảng rõ ràng: cấu trúc thư mục đề xuất · danh sách skill/subagent **Giữ / Bỏ / Sửa / Thêm** kèm lý do · nội dung `AGENTS.md`+`CLAUDE.md` mới (bản nháp). **Dừng, chờ người dùng đồng ý.** Nếu họ chỉnh, cập nhật kế hoạch rồi hỏi lại.

### P4 — Apply (chỉ sau khi duyệt)
- Viết lại `AGENTS.md` (nguồn luật) + `CLAUDE.md` (`@AGENTS.md` + phần Skill/Agent riêng) cho bối cảnh mới.
- Dựng/điều chỉnh cây thư mục.
- Prune skill/subagent không hợp; **tạo cái mới qua subagent `skill-smith`** (kèm mirror `.codex/skills/` nếu dùng Codex).
- Đồng bộ routing trong `AGENTS.md` mục 5.

### P5 — Log (bắt buộc)
Ghi một entry vào `.claude/skills/project-switch/upgrade-log.md` (định dạng ở đầu file đó): ngày, project/bối cảnh, đã Giữ/Bỏ/Sửa/Thêm gì, **vì sao**, và bài học rút ra cho project sau. Cập nhật bảng "Component registry" nếu version skill/agent đổi.

## Common Mistakes
| Ngụy biện | Thực tế |
|---|---|
| "Toolkit cũ chạy tốt, bê nguyên là xong" | Skill gắn lĩnh vực cũ sẽ kích hoạt sai chỗ, làm nhiễu. Phải prune. |
| "Tự chỉnh luôn cho nhanh" | Sai bối cảnh còn chậm hơn. Luôn qua GATE P3. |
| "Ghi log để sau" | Log là giá trị cốt lõi — project sau mất lịch sử là mất bài học. Ghi ngay ở P5. |

## Red Flags — DỪNG nếu thấy mình đang...
- Ghi đè `AGENTS.md`/`CLAUDE.md` khi chưa được duyệt ở P3.
- Giữ nguyên skill lĩnh vực cũ mà chưa hỏi project mới có cần không.
- Kết thúc mà chưa ghi `upgrade-log.md`.
