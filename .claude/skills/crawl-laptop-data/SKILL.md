---
name: crawl-laptop-data
description: Collect and standardise laptop market data for the MADM/MCDM project. Use when the user asks to crawl, scrape, collect, or update laptop listings from CellphoneS (or another Vietnamese retailer), map CPU/GPU benchmark scores from PassMark, or build the decision-matrix dataset for TOPSIS. Trigger on mentions of crawl, thu thập dữ liệu laptop, CellphoneS, benchmark, PassMark, dữ liệu thị trường.
---

# Crawl Laptop Data — Thu thập và chuẩn hóa dữ liệu thị trường

Mục tiêu: tạo bộ dữ liệu laptop sạch, có nguồn gốc, tái kiểm chứng được, làm đầu vào cho ma trận quyết định TOPSIS.

## Nguyên tắc bất di bất dịch

1. **Mọi file đều kèm ngày thu thập trong tên** (`YYYY-MM-DD_...`). Dữ liệu thị trường là ảnh chụp một thời điểm — thiếu ngày là vứt.
2. **Dữ liệu thô vào `02_du-lieu-tho\laptop-thi-truong\` và đóng băng.** File làm sạch vào `03_phan-tich\du-lieu-sach\`.
3. **Một nguồn benchmark duy nhất cho mỗi loại linh kiện** (PassMark cho cả CPU và GPU), ghi ngày truy cập vào cột riêng. Không trộn Cinebench với PassMark.
4. **Không bịa thông số.** Trường nào không tra được thì để trống và ghi vào cột `ghi_chu`, báo người dùng bổ sung tay.

## Quy trình

### Bước 1 — Crawl danh sách laptop (WebFetch/WebSearch)

Nguồn chính: cellphones.com.vn, danh mục laptop, lọc theo khoảng giá dự án (20-25 triệu). Với từng máy lấy: tên đầy đủ, giá niêm yết, giá khuyến mãi, CPU (model chính xác, ví dụ "i5-13420H"), GPU (model chính xác), RAM (GB, loại), lưu trữ (GB, loại), màn hình (kích thước, độ phân giải, tấm nền, độ phủ màu nếu có), pin (Wh nếu có), cân nặng, bảo hành (tháng), URL sản phẩm.

Kết quả ghi CSV: `02_du-lieu-tho\laptop-thi-truong\YYYY-MM-DD_cellphones-laptop-20-25tr.csv` — mỗi dòng một máy, kèm cột `url` và `ngay_thu_thap`.

### Bước 2 — Map benchmark

Tra điểm PassMark cho từng CPU/GPU model (cpubenchmark.net, videocardbenchmark.net). Ghi file riêng: `YYYY-MM-DD_benchmark-passmark.csv` với cột `model, loai (cpu/gpu), diem, ngay_truy_cap, url_nguon`. CPU/GPU không tìm thấy điểm → ghi chú lại, không ước lượng.

### Bước 3 — Làm sạch và dựng ma trận quyết định

Copy sang `03_phan-tich\du-lieu-sach\`, xử lý:
- Loại máy trùng (cùng model khác màu), máy thiếu quá nhiều thông số, máy ngoài khoảng giá.
- Join điểm benchmark theo model. Đơn vị thống nhất (giá VND, RAM GB, cân nặng kg).
- Tiêu chí định tính (thương hiệu, ngoại hình): KHÔNG tự chấm — xuất cột trống kèm rubric để nhóm chấm tay độc lập rồi lấy trung bình (task T5.3).
- Output cuối: CSV đúng định dạng đầu vào của `mcdm-toolkit\scripts\topsis.py` (header Alternative/C1..Cn, dòng type, dòng weight lấy từ kết quả AHP).

### Bước 4 — Nhật ký nguồn gốc

Ghi kèm file `YYYY-MM-DD_nguon-goc.md`: ngày crawl, số máy thu được, số máy sau lọc và lý do loại từng máy, nguồn benchmark + ngày truy cập. Đây là nội dung viết mục 3.4 của báo cáo.

## Giới hạn cần báo người dùng

Trang bán lẻ có thể chặn crawl tự động hoặc đổi giao diện — khi WebFetch thất bại, chuyển phương án: người dùng mở trang và lưu HTML/copy dữ liệu vào `inbox\`, skill xử lý phần trích xuất và chuẩn hóa. Không cố lách cơ chế chặn.
