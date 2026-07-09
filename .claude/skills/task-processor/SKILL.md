---
name: task-processor
description: "Use when the user gives any task or request for the MADM/MCDM laptop-selection project — research, survey, interview, AHP, TOPSIS, data collection, report writing, slides, or file management — especially when the request is vague, incomplete, out of pipeline order, or spans multiple steps. Also use when unsure which specialist skill applies, and on /task-processor. Trigger words: làm giúp, phân tích, tính toán, viết, thu thập, khảo sát, xử lý dữ liệu, chạy AHP/TOPSIS."
---

# Task Processor — Nhạc trưởng dự án MADM/MCDM

## Overview

Nguyên tắc cốt lõi: **hiểu đúng yêu cầu trước, làm sau**. Mọi task dự án đi qua 4 bước: Định vị → Làm rõ → Task Brief → Điều phối. Bỏ bước nào là mở cửa cho làm sai thứ tự pipeline, lưu sai chỗ, hoặc làm thứ người dùng không cần.

## When to Use

- Người dùng ra yêu cầu công việc cho dự án (tạo, sửa, tính, viết, thu thập).
- Yêu cầu mơ hồ, thiếu thông tin, hoặc chạm nhiều phase/kỹ năng.
- Không chắc nên dùng skill chuyên môn nào.

## When NOT to Use

- Câu hỏi kiến thức thuần túy, không tạo/sửa file nào (trả lời trực tiếp).
- Câu xã giao, hỏi trạng thái dự án.
- Người dùng đã đưa Task Brief đầy đủ và chỉ đích danh skill — nhảy thẳng Bước 4, nhưng luật vàng về nơi lưu file vẫn áp dụng.

## Quick Reference

| Bước | Việc | Nguồn đối chiếu |
|---|---|---|
| 1. Định vị | Yêu cầu thuộc phase/task T#.# nào? Đúng trình tự pipeline chưa? | `README.md` mục 5, `timeline.md` |
| 2. Làm rõ | Tự bổ sung ngữ cảnh trước, hỏi người dùng tối đa 2-3 câu | README → KE-HOACH → dữ liệu trong `02\`, `03\` |
| 3. Task Brief | Mục tiêu, input, output, nơi lưu, skill sẽ gọi | Luật vàng README mục 3 |
| 4. Điều phối | Gọi skill chuyên môn, mỗi bước ghi file xong mới chuyển (GATE) | Bảng routing dưới |

## Bốn bước chi tiết

### Bước 1 — Định vị

Đối chiếu với workflow 7 phase trong README. Nếu yêu cầu **nhảy cóc trình tự** (chạy TOPSIS khi chưa có trọng số AHP chốt trong `03_phan-tich\ahp\`; viết chương Results khi chưa có kết quả; khảo sát khi chưa chốt tiêu chí sau phỏng vấn) — DỪNG, cảnh báo kèm bước đúng, chỉ tiếp tục khi người dùng xác nhận vẫn muốn làm.

### Bước 2 — Làm rõ

Liệt kê điểm mơ hồ. Tự trả lời bằng ngữ cảnh dự án trước; chỉ hỏi khi không tự suy ra được và câu trả lời làm thay đổi kết quả. Mỗi câu hỏi kèm phương án khuyến nghị.

### Bước 3 — Task Brief

```
Task Brief: [tên việc] (khớp T#.# / ngoài workflow)
- Mục tiêu · Input · Output → lưu tại [thư mục]
- Skill sẽ gọi: [...]
```

Việc lớn (nhiều file, nhiều bước): hiển thị Brief chờ xác nhận. Việc nhỏ: gộp Brief vào câu mở đầu rồi làm luôn — nhưng vẫn phải CÓ.

### Bước 4 — Điều phối theo bảng routing

| Loại việc | Skill (đọc `.claude\skills\<ten>\SKILL.md` trước khi làm) |
|---|---|
| Viết văn bản VN/EN, literature review, LaTeX, citation | `professional-writing` |
| Tính AHP, TOPSIS, sensitivity | `mcdm-toolkit` |
| Thu thập/làm sạch dữ liệu laptop, benchmark | `data-pipeline` |
| Phân tích khảo sát Likert | `likert-analysis` |
| Dựng slide | `pptx` |
| Đọc/ghi Excel | `xlsx` |
| Trích xuất PDF paper | `pdf` |
| Câu hỏi logistics/SCM chuyên sâu | `supply-chain-consultant` |
| Tạo/sửa/kiểm định skill | `skill-creator`, `writing-skills`, `audit-skills` |

Kết thúc: báo kết quả kèm đường dẫn file; nhắc cập nhật `timeline.md` nếu xong task T#.#; nhắc checklist kết thúc phase (ZIP + Drive) nếu chạm mốc phase.

## Common Mistakes — chặn ngụy biện

| Ngụy biện | Thực tế |
|---|---|
| "Việc nhỏ, khỏi cần Brief" | Brief việc nhỏ chỉ tốn 1 câu. Chuỗi việc-nhỏ-sai-chỗ là cách repo nát nhanh nhất. |
| "Người dùng đang vội, làm luôn cho nhanh" | Làm sai còn chậm hơn. Định vị + Brief mất chưa tới 30 giây. |
| "Chỉ đọc dữ liệu chứ không ghi, khỏi định vị" | Đọc sai phase → kết luận sai → người dùng quyết định sai. Vẫn định vị. |
| "Ghi tạm vào 06_nop-bai rồi dọn sau" | `06` là vùng thiêng liêng. Không có "tạm". Ghi vào `03` hoặc scratchpad. |
| "Dữ liệu chắc đúng rồi, nhảy phase cũng được" | "Chắc" không phải bằng chứng. Kiểm tra file chốt của phase trước có tồn tại thật không. |
| "Kết quả gần đạt, nới điều kiện một chút" | Ngưỡng/điều kiện đã chốt có nguồn. Muốn đổi phải qua người dùng, ghi lý do. |

## Red Flags — DỪNG lại nếu thấy mình đang...

- Tạo/sửa file mà chưa nói được nó thuộc task T nào.
- Ghi file vào `02_du-lieu-tho\` (vùng đóng băng) hoặc `06_nop-bai\`.
- Chạy bước tính toán mà input là số tự chế thay vì file thật trong `03\`.
- Trả lời "để sau cũng được" với việc cập nhật timeline/backup cuối phase.

Gặp cờ đỏ nào: quay lại Bước 1.
