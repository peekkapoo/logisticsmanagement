---
name: data-pipeline
description: "Use when the project needs to collect, clean, aggregate, or export structured data — especially crawling laptop listings from CellphoneS, mapping PassMark benchmarks, cleaning the raw data, and building the TOPSIS decision matrix (Phase 5). Also for any web/API/file data extraction feeding the analysis. Trigger on crawl, thu thập dữ liệu, laptop, benchmark, PassMark, làm sạch dữ liệu, ma trận quyết định, data collection/cleaning/aggregation/export."
---

# Data Pipeline — Thu thập → làm sạch → tổng hợp → xuất

Bộ kỹ năng mô-đun cho vòng đời dữ liệu có cấu trúc, dùng chính cho **Phase 5** (dữ liệu laptop + benchmark → ma trận quyết định TOPSIS). Bốn bước con nằm ở `skills/<tên>/SKILL.md`; ràng buộc đạo đức/tái lập ở `rules/data-ethics.md`; script dùng chung ở `shared/scripts/`.

## Khi nào dùng

- Crawl danh sách laptop 20–25tr từ CellphoneS (kèm ngày crawl trong tên file).
- Tra điểm benchmark CPU/GPU từ **một nguồn duy nhất** (PassMark), ghi ngày truy cập.
- Làm sạch, ghép benchmark, dựng ma trận quyết định hoàn chỉnh.
- Bất kỳ tác vụ trích xuất dữ liệu web/API/file phục vụ phân tích.

## Quy trình (đọc `workflows/pipeline.md` để làm đầy đủ)

collect → clean → **validate** (`shared/scripts/validate.py`) → aggregate → export → report.

| Bước | Đọc SKILL con | Việc |
|---|---|---|
| 1. Thu thập | `skills/data-collection/SKILL.md` | Trích dữ liệu từ API / web tĩnh–động / file. Ra dataset thô + source log. |
| 2. Làm sạch | `skills/data-cleaning/SKILL.md` | Chuẩn hóa tên cột, ngày, số, tiền tệ; xử lý khuyết; khử trùng lặp. |
| 3. Kiểm định | `shared/scripts/validate.py` | Kiểm cột bắt buộc, kiểu dữ liệu, trùng lặp, ngoại lai. Fail → sửa ở bước 2 rồi chạy lại. |
| 4. Tổng hợp | `skills/data-aggregation/SKILL.md` | Gộp, pivot, tính chỉ số (chỉ khi cần). |
| 5. Xuất | `skills/data-export/SKILL.md` | Ghi Excel đa sheet / CSV / JSON, header đóng băng, auto-width. |

## Ràng buộc dự án

- **Nơi lưu:** dữ liệu thô crawl → `02_du-lieu-tho/laptop-thi-truong/` (vùng đóng băng, kèm ngày). Dữ liệu đã làm sạch + ma trận → `03_phan-tich/du-lieu-sach/` và `03_phan-tich/topsis/`.
- **Benchmark:** 1 nguồn/loại (PassMark), ghi ngày truy cập — coi như ảnh chụp thị trường tại một thời điểm.
- Tuân thủ `rules/data-ethics.md` (tái lập, hợp pháp) trong mọi lần crawl.
