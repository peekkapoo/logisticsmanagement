# Dự án MADM/MCDM - Bộ tiêu chí ra quyết định mua laptop (Logistics Management)

Đồ án nhóm: xây bộ tiêu chí mua laptop (literature → phỏng vấn chuyên gia → khảo sát Likert), tính trọng số bằng AHP, xếp hạng bằng TOPSIS. Sản phẩm nộp: báo cáo LaTeX tiếng Anh + slide tiếng Anh. Ngôn ngữ làm việc nội bộ: tiếng Việt.

## Định tuyến yêu cầu (bắt buộc)

Mọi yêu cầu liên quan đến dự án (nghiên cứu, dữ liệu, tính toán, viết, slide, quản lý file) phải đi qua quy trình của skill `task-processor` TRƯỚC khi thực thi: định vị yêu cầu vào phase/task trong README → làm rõ điểm mơ hồ → Task Brief → điều phối skill chuyên môn. Ngoại lệ duy nhất: câu hỏi kiến thức thuần túy không tạo/sửa file.

## Luật vàng về file (không có ngoại lệ)

1. `02_du-lieu-tho\` là vùng đóng băng: file vào rồi thì không sửa, không xóa. Xử lý dữ liệu = copy sang `03_phan-tich\` rồi làm trên bản copy.
2. `06_nop-bai\` chỉ chứa bản nộp cuối đã được nhóm duyệt. Không bao giờ tự ghi vào đây.
3. File mới đặt tên theo quy ước README mục 4 (`YYYY-MM-DD_ten_vX.Y_trangthai_nguoi.ext`); dữ liệu thị trường/benchmark bắt buộc kèm ngày thu thập.

## Quy ước kỹ thuật

- Báo cáo `04_bao-cao-latex\`: biên dịch bằng **XeLaTeX + biber** (không dùng pdflatex). Bảng dùng booktabs, không kẻ dọc.
- Tính AHP/TOPSIS: luôn chạy script trong `.claude\skills\mcdm-toolkit\scripts\`, không tính tay. CR > 0.1 là ma trận hỏng, phải báo.
- Viết học thuật: nháp tiếng Việt trước, bản tiếng Anh viết lại độc lập từ Content Brief (không dịch máy từng câu) — theo skill `professional_writing`.
- Khi người dùng nói "lưu phiên bản báo cáo": git commit với message mô tả nội dung vừa làm. Khi nói "khôi phục báo cáo": tìm commit theo mô tả/ngày và restore, hỏi xác nhận trước khi ghi đè.

## Tài liệu định hướng

- `README.md` — sổ tay vận hành: bản đồ thư mục, workflow 7 phase với task T0.1→T6.8, DoD, backup.
- `KE-HOACH-DU-AN.md` — kế hoạch tổng thể và lý do các quyết định thiết kế.
- `00_quan-ly-du-an\timeline.md` — deadline và trạng thái từng phase.
