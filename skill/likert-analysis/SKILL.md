---
name: likert-analysis
description: Use when the project has Likert survey data to process — Google Form exports, descriptive statistics (N, mean, SD, frequency), screening criteria against a threshold, or building the survey results table for the report. Trigger on khảo sát, Likert, Google Form, phân tích mô tả, sàng lọc tiêu chí, ngưỡng, mean, threshold, straight-lining.
---

# Likert Analysis — Phân tích khảo sát sàng lọc tiêu chí

## Overview

Nguyên tắc cốt lõi: **ngưỡng chốt trước, dữ liệu chạy sau** — không được nhìn kết quả rồi mới chọn ngưỡng. Phục vụ task T3.5 và T3.6 của workflow.

## When to Use

- Có CSV export từ Google Form cần thống kê mô tả.
- Cần kết luận giữ/loại tiêu chí theo ngưỡng đã chốt.
- Cần bảng kết quả khảo sát cho chương Results.

## When NOT to Use

- Chưa thu xong khảo sát (dữ liệu nhỏ giọt) → chờ chốt đợt thu, phân tích trên bản export đóng băng.
- Phân tích ma trận AHP hay xếp hạng phương án → skill `mcdm-toolkit`.

## Quick Reference

| Việc | Lệnh |
|---|---|
| Phân tích + sàng lọc | `python scripts/likert.py khao-sat.csv --threshold 3.5` |
| Chỉ định cột tiêu chí | thêm `--cols "C1,C2,..."` |
| Xuất bảng báo cáo | thêm `--latex out.tex` |
| Format input mẫu | `examples/khao-sat-mau.csv` |

## Quy trình

1. File export gốc nằm ở `02_du-lieu-tho\khao-sat\` (đóng băng). Copy sang `03_phan-tich\tieu-chi\` rồi mới phân tích.
2. Chạy script. Script tự loại phản hồi thiếu hơn 20% câu trả lời (báo số lượng) và ĐẾM straight-lining (trả lời cùng mức mọi câu) nhưng không tự loại — nhóm quyết định và ghi vào biên bản.
3. Kết quả cuối ghi CSV kèm ngày vào `03_phan-tich\tieu-chi\`; bảng LaTeX xuất vào `04_bao-cao-latex\tables\survey-results.tex`.
4. Đối chiếu chéo với sheet PhanTich của `likert-thu-thap-phan-tich.xlsx` — lệch nhau là có lỗi dữ liệu, phải tìm nguyên nhân.

## Common Mistakes

| Sai lầm | Thực tế |
|---|---|
| Thấy tiêu chí yêu thích mean 3.4, hạ ngưỡng xuống 3.4 | Ngưỡng đổi sau khi thấy kết quả = ngụy tạo. Muốn đổi phải có nguồn học thuật mới + người dùng duyệt + ghi lý do. |
| Lặng lẽ xóa straight-liner cho "dữ liệu sạch" | Loại respondent là quyết định phương pháp luận của nhóm, phải ghi biên bản và khai trong báo cáo. |
| Dùng ngưỡng 3.5 trong báo cáo mà không trích nguồn | Giảng viên hỏi "3.5 ở đâu ra?" là mất điểm. Nhắc người dùng bổ sung citation trước khi viết chương 3. |
| Phân tích trực tiếp trên file trong `02_du-lieu-tho\` | Vi phạm vùng đóng băng. Luôn copy sang `03\`. |
| Hai nguồn kết quả (script vs Excel) lệch nhau, chọn bên "đẹp hơn" | Tìm nguyên nhân lệch. Không bao giờ chọn theo kết quả mong muốn. |

## Red Flags — DỪNG lại nếu

- Đang chạy lại phân tích với ngưỡng khác sau khi đã thấy kết quả.
- Đang gõ tay số mean/SD vào báo cáo thay vì dùng bảng xuất từ script.
- File input không truy được về bản export gốc trong `02_du-lieu-tho\khao-sat\`.
