---
name: mcdm-toolkit
description: AHP and TOPSIS calculator for the MADM/MCDM project. Use when the user needs to compute AHP criteria weights (pairwise comparison matrix, eigenvector or geometric mean, lambda_max, CI, CR consistency check, aggregating multiple experts), run TOPSIS ranking (vector normalization, ideal solutions, closeness coefficient Ci), or perform sensitivity analysis on weights. Trigger on mentions of AHP, TOPSIS, trọng số, ma trận so sánh cặp, CR, xếp hạng phương án, sensitivity.
---

# MCDM Toolkit — AHP + TOPSIS

Nguyên tắc số 1: KHÔNG tính tay/tính nhẩm. Mọi kết quả phải chạy từ script trong `scripts/` để tái lập được và đúng tuyệt đối. Kết quả ghi ra file trong `03_phan-tich\` kèm bảng LaTeX (booktabs) cho báo cáo.

## AHP — tính trọng số

Input: ma trận so sánh cặp. Hai nguồn hợp lệ:
- File Excel `03_phan-tich\ahp\ahp-thu-thap-chuyen-gia.xlsx` (đọc bằng skill `xlsx` hoặc openpyxl, lấy vùng ma trận từng sheet ChuyenGia).
- File CSV vuông n×n (chỉ số, không header) — xuất từ Excel ra để chạy script.

Chạy:
```
python scripts/ahp.py matran1.csv [matran2.csv ...] [--latex out.tex]
```

Script tính cho TỪNG ma trận: trọng số (geometric mean of rows + eigenvector bằng power iteration, in cả hai để đối chiếu), λmax, CI, CR (bảng RI của Saaty). Nhiều ma trận thì tổng hợp bằng geometric mean từng phần tử rồi tính trọng số trên ma trận tổng hợp.

Quy tắc bắt buộc:
- CR > 0.1 → ma trận KHÔNG hợp lệ. Báo rõ ma trận nào hỏng và in ra 3 cặp phần tử đóng góp nhiều nhất vào bất nhất (script tự in) để người điền xem lại. Không lặng lẽ dùng ma trận hỏng.
- Kết quả cuối ghi vào `03_phan-tich\ahp\` theo quy ước tên có ngày, và xuất `04_bao-cao-latex\tables\ahp-weights.tex` khi người dùng cần cho báo cáo.

## TOPSIS — xếp hạng phương án

Input: file CSV ma trận quyết định tại `03_phan-tich\du-lieu-sach\`, định dạng:
- Dòng 1: header — `Alternative,C1,C2,...`
- Dòng 2: hướng tối ưu — `type,benefit,cost,...` (benefit = càng cao càng tốt, cost = càng thấp càng tốt)
- Dòng 3: trọng số — `weight,0.25,0.10,...` (từ kết quả AHP, tổng = 1)
- Từ dòng 4: mỗi dòng một phương án.

Chạy:
```
python scripts/topsis.py matran-quyet-dinh.csv [--latex out.tex] [--sensitivity]
```

Các bước script thực hiện (chuẩn Hwang & Yoon 1981): chuẩn hóa vector → nhân trọng số → xác định giải pháp lý tưởng A+ và A- → khoảng cách Euclid D+ và D- → hệ số gần gũi Ci = D-/(D+ + D-) → xếp hạng giảm dần theo Ci.

`--sensitivity`: thay trọng số từng tiêu chí ±10% và ±20% (chuẩn hóa lại tổng = 1), báo thứ hạng top 3 có đổi không — đây là nội dung mục 4.5 của báo cáo.

## Đầu ra chuẩn

Mỗi lần chạy, ghi kết quả thành file CSV kèm ngày trong thư mục tương ứng của `03_phan-tich\`, và in tóm tắt cho người dùng: trọng số/xếp hạng + kiểm định (CR hoặc sensitivity). Khi xuất LaTeX, dùng booktabs (\toprule \midrule \bottomrule, không kẻ dọc) đúng chuẩn `professional_writing\publishing\latex.md`.
