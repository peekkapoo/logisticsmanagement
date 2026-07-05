---
name: task-processor
description: Project orchestrator for the MADM/MCDM laptop-selection project. Use when the user gives ANY project task, request, or instruction related to this project — research, data collection, survey, AHP, TOPSIS, report writing, slides, file management — especially when the request is ambiguous, incomplete, or spans multiple steps. Analyze the request deeply, clarify missing context, then route execution to the right specialist skills. Also trigger on /task-processor.
---

# Task Processor — Nhạc trưởng dự án MADM/MCDM

Vai trò: phân tích chuyên sâu mọi yêu cầu trước khi thực thi. KHÔNG bắt tay làm ngay. Chạy đủ 4 bước dưới đây theo thứ tự, có cổng bàn giao (GATE) giữa các bước.

## Bước 1 — Định vị yêu cầu

Đối chiếu yêu cầu với `README.md` mục 5 (workflow 7 phase, task T0.1 → T6.8):

1. Yêu cầu thuộc phase nào, task mã nào? Nếu không khớp task nào, đây là yêu cầu ngoài workflow — vẫn xử lý nhưng ghi rõ.
2. Kiểm tra trình tự pipeline. Nếu yêu cầu nhảy cóc (ví dụ đòi chạy TOPSIS khi `03_phan-tich\ahp\` chưa có trọng số chốt, hoặc đòi viết chương Results khi chưa có kết quả), CẢNH BÁO người dùng và đề xuất bước đúng, chỉ tiếp tục khi người dùng xác nhận.
3. Kiểm tra trạng thái trong `00_quan-ly-du-an\timeline.md` nếu liên quan deadline.

## Bước 2 — Làm rõ ngữ cảnh

Liệt kê thông tin mơ hồ hoặc thiếu. Tự bổ sung từ ngữ cảnh dự án TRƯỚC, theo thứ tự tra cứu: `README.md` → `KE-HOACH-DU-AN.md` → dữ liệu có sẵn trong `02_du-lieu-tho\` và `03_phan-tich\` → `00_quan-ly-du-an\brainstorm.md`.

Chỉ hỏi người dùng khi thật sự không tự suy ra được, tối đa 2-3 câu hỏi, ưu tiên câu ảnh hưởng đến kết quả cuối. Câu hỏi kèm phương án khuyến nghị.

## Bước 3 — Task Brief

Xuất Task Brief ngắn theo mẫu, hiển thị cho người dùng trước khi thực thi nếu nhiệm vụ chạm nhiều file hoặc mất nhiều bước; nhiệm vụ nhỏ thì gộp Brief vào câu mở đầu:

```
Task Brief: [tên việc] (khớp task T#.# / ngoài workflow)
- Mục tiêu: ...
- Input: [file/thư mục nguồn]
- Output: [file kết quả] → lưu tại [thư mục theo luật vàng]
- Skill sẽ gọi: [theo bảng routing]
```

Luật vàng bắt buộc khi chọn nơi lưu: dữ liệu gốc vào `02_du-lieu-tho\` (đóng băng, kèm ngày), file xử lý vào `03_phan-tich\`, KHÔNG BAO GIỜ ghi vào `06_nop-bai\` trừ khi người dùng nói rõ đây là bản nộp.

## Bước 4 — Điều phối thực thi

Gọi skill chuyên môn theo bảng routing. Mỗi bước xong phải có sản phẩm ghi ra file rồi mới chuyển bước tiếp (GATE).

| Loại việc | Skill |
|---|---|
| Viết mọi loại văn bản (VN/EN), literature review, LaTeX, citation | `professional_writing` (theo quy trình GATE nội bộ của nó) |
| Tính AHP, TOPSIS, sensitivity analysis | `mcdm-toolkit` |
| Thu thập dữ liệu laptop, benchmark | `crawl-laptop-data` |
| Phân tích khảo sát Likert | `likert-analysis` |
| Dựng slide | `pptx` (+ chuẩn dataviz cho chart) |
| Đọc/ghi/sửa file Excel | `xlsx` |
| Trích xuất từ PDF paper | `pdf` |
| Câu hỏi chuyên môn logistics/SCM | `supply-chain-consultant` |

Kết thúc nhiệm vụ:
- Báo kết quả kèm đường dẫn file đã tạo/sửa.
- Nếu nhiệm vụ hoàn thành một task T#.#, nhắc cập nhật `timeline.md`.
- Nếu nhiệm vụ kết thúc một phase, nhắc checklist kết thúc phase trong README mục 6 (ZIP sao lưu + upload Drive).

## Ngoại lệ không cần chạy đủ 4 bước

Câu hỏi kiến thức thuần túy (không tạo/sửa file), câu xã giao, hoặc yêu cầu đã kèm Task Brief rõ ràng từ người dùng — trả lời trực tiếp, nhưng vẫn tôn trọng luật vàng nếu có ghi file.
