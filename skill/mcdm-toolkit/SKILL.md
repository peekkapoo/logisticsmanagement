---
name: mcdm-toolkit
description: Use when the project needs AHP criteria weights, a consistency (CR) check, TOPSIS ranking of alternatives, or weight sensitivity analysis — including reading pairwise matrices from the Excel collection file or CSV. Trigger on AHP, TOPSIS, trọng số, ma trận so sánh cặp, CR, nhất quán, xếp hạng, sensitivity, eigenvector, closeness coefficient.
---

# MCDM Toolkit — AHP + TOPSIS

## Overview

Nguyên tắc cốt lõi: **không tính tay, không tính nhẩm** — mọi con số ra từ script trong `scripts/` để đúng tuyệt đối và tái lập được. Công thức toán và bảng RI để viết chương Methodology nằm ở `references/mcdm-math.md`.

## When to Use

- Tính trọng số tiêu chí từ ma trận so sánh cặp (một hoặc nhiều chuyên gia).
- Kiểm tra nhất quán CR, chẩn đoán ma trận bất nhất.
- Xếp hạng phương án bằng TOPSIS, phân tích độ nhạy trọng số.

## When NOT to Use

- Chưa chốt bộ tiêu chí cuối (Phase 3 chưa xong) → chưa được dựng ma trận AHP.
- Chưa có trọng số AHP chốt → chưa được chạy TOPSIS (báo task-processor cảnh báo nhảy cóc).
- Sàng lọc tiêu chí bằng khảo sát → skill `likert-analysis`.

## Quick Reference

| Việc | Lệnh |
|---|---|
| Trọng số 1 chuyên gia | `python scripts/ahp.py matran.csv` |
| Tổng hợp nhiều chuyên gia | `python scripts/ahp.py cg1.csv cg2.csv ... [--latex out.tex]` |
| Xếp hạng TOPSIS | `python scripts/topsis.py ma-tran-quyet-dinh.csv [--latex out.tex]` |
| Kèm độ nhạy | thêm `--sensitivity` |
| Format input mẫu | xem `examples/ahp-vidu-3x3.csv`, `examples/topsis-vidu.csv` |
| Công thức + bảng RI | `references/mcdm-math.md` |

## Input

**AHP:** ma trận vuông n×n chỉ chứa số (chấp nhận phân số `1/5`), không header — xem `examples/ahp-vidu-3x3.csv`. Nguồn thực tế: vùng ma trận trong `03_phan-tich\ahp\ahp-thu-thap-chuyen-gia.xlsx` (xuất từng sheet ChuyenGia ra CSV bằng skill `xlsx`).

**TOPSIS:** CSV 4 phần — header `Alternative,C1,...`, dòng `type` (benefit/cost), dòng `weight` (từ AHP), rồi mỗi dòng một phương án — xem `examples/topsis-vidu.csv`. Nguồn thực tế: `03_phan-tich\du-lieu-sach\`.

## Output chuẩn

- Kết quả ghi CSV kèm ngày vào thư mục tương ứng trong `03_phan-tich\` (`ahp\` hoặc `topsis\`).
- Bảng cho báo cáo xuất bằng `--latex` vào `04_bao-cao-latex\tables\` (booktabs, không kẻ dọc).
- Luôn in kèm kiểm định: CR từng ma trận (AHP) hoặc kết quả sensitivity (TOPSIS).

## Common Mistakes

| Sai lầm | Hậu quả / Cách đúng |
|---|---|
| Dùng ma trận có CR > 0.1 vì "chỉ hơi vượt" | Kết quả không bảo vệ được trước giảng viên. Gửi lại người điền kèm 3 cặp bất nhất script đã chỉ ra. |
| Quên dòng `type`, để cost thành benefit (giá càng cao càng tốt?) | Xếp hạng đảo ngược hoàn toàn. Soát dòng type trước khi chạy. |
| Trọng số gõ tay lại từ kết quả AHP, gõ nhầm 1 số | Dùng file, không gõ lại. Tổng weight lệch 1 script tự chuẩn hóa nhưng vẫn phải soát nguồn. |
| Tính bằng công thức Excel tự chế thay vì script | Hai nguồn số khác nhau không biết tin bên nào. Excel chỉ để thu thập, script là nguồn sự thật. |
| Chạy TOPSIS xong không chạy sensitivity | Mục 4.5 của báo cáo trống và kết luận thiếu độ tin cậy. |

## Red Flags — DỪNG lại nếu

- Đang gõ số trọng số/điểm Ci trực tiếp vào báo cáo mà không có file kết quả tương ứng trong `03_phan-tich\`.
- Đang "ước lượng" điểm cho phương án thiếu dữ liệu thay vì báo thiếu.
- Ma trận đầu vào không truy được về file Excel thu thập hoặc file trong `02_du-lieu-tho\`.
