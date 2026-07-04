# Quy tắc vùng dữ liệu thô - ĐỌC TRƯỚC KHI BỎ FILE VÀO ĐÂY

Thư mục `02_du-lieu-tho\` là vùng ĐÓNG BĂNG. File đã lưu vào đây thì không sửa, không đổi tên, không xóa. Muốn xử lý dữ liệu thì copy file sang `03_phan-tich\` rồi làm trên bản copy. Lý do là nếu tính toán sai, nhóm luôn còn bản gốc để làm lại.

## Quy trình nhận file từ thành viên

1. Thành viên gửi file qua kênh chat hoặc Drive của nhóm.
2. Nhóm trưởng lưu nguyên trạng vào `inbox\`.
3. Nhóm trưởng đổi tên theo quy ước (xem README mục 4) rồi chuyển vào đúng thư mục con bên dưới.
4. `inbox\` được dọn sạch sau mỗi lần phân loại.

## File nào vào thư mục nào

| Thư mục | Chứa gì | Lưu ý đặt tên |
|---|---|---|
| `khao-sat\` | File CSV export từ Google Form | Kèm ngày export, ví dụ `2026-08-01_khao-sat-likert_raw.csv` |
| `phong-van\` | Kịch bản phỏng vấn, ghi chú, file ghi âm | Kèm mã chuyên gia, ví dụ `2026-07-20_phong-van_chuyengia-01.docx` |
| `laptop-thi-truong\` | Dữ liệu crawl CellphoneS, điểm benchmark | BẮT BUỘC kèm ngày thu thập, ví dụ `2026-08-10_cellphones-laptop-20-25tr.csv` |

Dữ liệu thị trường và benchmark là ảnh chụp tại một thời điểm, giá và model thay đổi liên tục, vì vậy thiếu ngày thu thập là dữ liệu coi như không dùng được cho báo cáo.
