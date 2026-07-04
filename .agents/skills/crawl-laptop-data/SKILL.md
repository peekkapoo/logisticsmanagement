---
name: crawl-laptop-data
description: Use when the project needs laptop market data — crawling or collecting listings from CellphoneS or another Vietnamese retailer, mapping CPU/GPU benchmark scores from PassMark, cleaning specs, or building the decision-matrix dataset for TOPSIS. Trigger on crawl, thu thập dữ liệu laptop, CellphoneS, benchmark, PassMark, thông số máy, dữ liệu thị trường, ma trận quyết định.
---

# Crawl Laptop Data — Thu thập và chuẩn hóa dữ liệu thị trường

## Overview

Nguyên tắc cốt lõi: **dữ liệu thị trường là ảnh chụp một thời điểm** — mọi file phải kèm ngày thu thập và truy được về nguồn (URL), nếu không thì vô giá trị cho báo cáo. Phục vụ task T5.1 → T5.4.

## When to Use

- Thu thập danh sách laptop + thông số theo khoảng giá dự án (20-25 triệu).
- Tra và ghép điểm benchmark PassMark cho CPU/GPU.
- Làm sạch dữ liệu, dựng ma trận quyết định cho TOPSIS.

## When NOT to Use

- Chưa chốt bộ tiêu chí cuối (Phase 3) → chưa biết cần cột nào, crawl sớm là crawl lại.
- Chạy TOPSIS trên dữ liệu đã sạch → skill `mcdm-toolkit`.
- Trang chặn crawl tự động → KHÔNG lách; chuyển phương án thủ công (dưới).

## Quick Reference

| Bước | Output | Lưu tại |
|---|---|---|
| 1. Crawl CellphoneS | `YYYY-MM-DD_cellphones-laptop-20-25tr.csv` | `02_du-lieu-tho\laptop-thi-truong\` |
| 2. Map benchmark | `YYYY-MM-DD_benchmark-passmark.csv` | `02_du-lieu-tho\laptop-thi-truong\` |
| 3. Làm sạch + ma trận | CSV đúng format input topsis.py | `03_phan-tich\du-lieu-sach\` |
| 4. Nhật ký nguồn gốc | `YYYY-MM-DD_nguon-goc.md` | `03_phan-tich\du-lieu-sach\` |
| Schema cột chuẩn | `examples/schema-output.csv` | — |

## Quy trình chi tiết

**Bước 1 — Crawl (WebFetch/WebSearch):** cellphones.com.vn, lọc khoảng giá. Mỗi máy: tên đầy đủ, giá niêm yết + khuyến mãi, CPU model chính xác (vd "i5-13420H"), GPU model, RAM (GB, loại), lưu trữ, màn hình (kích thước, phân giải, tấm nền, độ phủ màu), pin Wh, cân nặng, bảo hành, `url`, `ngay_thu_thap`.

**Bước 2 — Benchmark:** cpubenchmark.net + videocardbenchmark.net (PassMark, MỘT nguồn duy nhất). Cột: `model, loai, diem, ngay_truy_cap, url_nguon`. Không tìm thấy điểm → để trống + ghi chú, không ước lượng.

**Bước 3 — Làm sạch:** loại máy trùng model, thiếu quá nhiều thông số, ngoài khoảng giá; join benchmark theo model; thống nhất đơn vị. Tiêu chí định tính (thương hiệu, ngoại hình): xuất **cột trống + rubric** để nhóm chấm tay độc lập rồi lấy trung bình (T5.3) — skill không tự chấm.

**Bước 4 — Nhật ký nguồn gốc:** ngày crawl, số máy thu/số sau lọc, lý do loại từng máy, nguồn benchmark + ngày. Đây chính là tư liệu viết mục 3.4 báo cáo.

**Phương án khi trang chặn crawl:** người dùng mở trang, lưu HTML hoặc copy dữ liệu vào `02_du-lieu-tho\inbox\`; skill chỉ làm phần trích xuất và chuẩn hóa.

## Common Mistakes

| Sai lầm | Thực tế |
|---|---|
| File không có ngày thu thập trong tên | Giá đổi hàng tuần. Không ngày = không kiểm chứng được = loại khỏi báo cáo. |
| Trộn PassMark với Cinebench/Geekbench "cho đủ số" | Hai thang điểm khác nhau, ma trận thành rác. Thiếu thì để trống + báo. |
| Tự chấm điểm thương hiệu/ngoại hình cho nhanh | Điểm định tính phải do nhóm chấm theo rubric, có ghi lại — nếu không mục Methodology bị hở. |
| Sửa trực tiếp file crawl trong `02_du-lieu-tho\` | Vùng đóng băng. Copy sang `03\du-lieu-sach\` rồi mới sửa. |
| Ghi "khoảng 20 máy" thay vì danh sách + lý do loại | Số máy vào/ra phải khớp nhật ký nguồn gốc từng dòng. |

## Red Flags — DỪNG lại nếu

- Một ô thông số được điền từ "kiến thức chung" thay vì trang nguồn có URL.
- Chuẩn bị crawl khi bộ tiêu chí cuối chưa tồn tại trong `03_phan-tich\tieu-chi\`.
- Đang thử vượt CAPTCHA/chặn bot của trang bán lẻ.
