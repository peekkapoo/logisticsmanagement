---
name: likert-analysis
description: Analyse 5-point Likert survey data for the MADM/MCDM project criteria screening. Use when the user wants to process Google Form survey exports, compute descriptive statistics (N, mean, SD, frequency), screen criteria against a threshold, or produce the survey results table for the report. Trigger on mentions of khảo sát, Likert, Google Form, phân tích mô tả, sàng lọc tiêu chí, mean, threshold.
---

# Likert Analysis — Phân tích khảo sát sàng lọc tiêu chí

Phục vụ task T3.5 và T3.6: từ CSV export của Google Form, tính thống kê mô tả và kết luận giữ/loại từng tiêu chí theo ngưỡng.

## Input

CSV export từ Google Form, lưu tại `02_du-lieu-tho\khao-sat\` (đóng băng). Trước khi phân tích, copy sang `03_phan-tich\tieu-chi\`. Cột tiêu chí là điểm 1-5; cột nhân khẩu học (giới tính, nghề nghiệp...) giữ lại để mô tả mẫu.

## Chạy

```
python scripts/likert.py khao-sat.csv --threshold 3.5 [--cols "C1,C2,..."] [--latex out.tex]
```

- `--threshold`: ngưỡng giữ tiêu chí. Mặc định 3.5. Ngưỡng dùng trong báo cáo PHẢI kèm trích dẫn nguồn học thuật — nhắc người dùng nếu chưa có.
- `--cols`: tên các cột tiêu chí; bỏ qua thì script tự nhận diện cột có toàn giá trị 1-5.

Script xuất: N, mean, SD, tần suất 1-5 và kết luận GIU/LOAI cho từng tiêu chí; thống kê mô tả mẫu (số phản hồi hợp lệ, số bị loại vì thiếu dữ liệu).

## Quy tắc phân tích

1. **Làm sạch trước khi tính**: phản hồi bỏ trống nhiều hơn 20% số câu → loại khỏi mẫu và báo số lượng. Phản hồi trả lời cùng một mức cho mọi câu (straight-lining) → đếm và báo, để nhóm quyết định giữ hay loại.
2. **Không tự đổi ngưỡng** cho đến khi tiêu chí "đạt đủ đẹp". Ngưỡng chốt một lần ở T3.6, có nguồn, rồi mới chạy kết luận cuối.
3. **Kết quả song song với Excel**: file `likert-thu-thap-phan-tich.xlsx` có cùng công thức — nếu hai bên lệch nhau là có lỗi dữ liệu, phải tìm nguyên nhân, không chọn bên "đẹp hơn".
4. Kết quả cuối ghi CSV kèm ngày vào `03_phan-tich\tieu-chi\` và bảng LaTeX (booktabs) vào `04_bao-cao-latex\tables\survey-results.tex` khi cần cho báo cáo.
