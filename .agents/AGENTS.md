# Antigravity Rules - MADM/MCDM Laptop Selection Project

## 1. Mệnh lệnh khởi động (Initialization Workflow)
**CRITICAL RULE:** Trong mọi phiên làm việc hoặc khi nhận yêu cầu mới từ người dùng, bạn PHẢI tuân thủ luồng làm việc sau:
1. Đọc file `00_quan-ly-du-an/task_log.md` đầu tiên để hiểu ngữ cảnh hiện tại, tiến độ đang làm dở, và cảnh báo lưu ý.
2. Đọc thư viện kiến thức tổng thể tại `README.md` hoặc `00_quan-ly-du-an/timeline.md` nếu cần.
3. Kích hoạt và tuân thủ skill `task-processor` để định vị yêu cầu, phân loại task và chuyển hướng công việc.
4. **Mệnh lệnh kết thúc:** Trước khi hoàn thành một đầu việc hoặc kết thúc phiên, hãy luôn cập nhật lại tiến độ vào file `00_quan-ly-du-an/task_log.md`. LƯU Ý BẮT BUỘC: Mỗi lần ghi nhận một mục cập nhật hoặc một công việc hoàn thành, bạn PHẢI luôn đính kèm thời gian (timestamp) theo chuẩn `YYYY-MM-DD HH:MM:SS`.

## 2. Kho Skill và Định Tuyến
Các skill chuyên sâu đã được tích hợp trong thư mục `.agents/skills`. Bạn có thể tự động gọi chúng bằng ID đã được khai báo ở YAML frontmatter:
- `task-processor`: Phân tích yêu cầu, lên Task Brief.
- `professional_writing`: Viết học thuật, LaTeX, literature review.
- `mcdm-toolkit`: Tính toán AHP, TOPSIS.
- `likert-analysis`: Phân tích khảo sát.
- `data-pipeline`: Thu thập dữ liệu laptop, crawl, benchmark, làm sạch.
- `supply-chain-consultant`: Tư vấn SCM.
- `pptx`, `xlsx`, `pdf`: Xử lý định dạng file tương ứng.

## 3. Luật vàng về file (Không có ngoại lệ)
1. **`02_du-lieu-tho\` là vùng ĐÓNG BĂNG**: file vào rồi thì không sửa, không xóa. Xử lý dữ liệu = copy sang `03_phan-tich\` rồi làm trên bản copy.
2. **`06_nop-bai\` CHỈ CHỨA BẢN NỘP CUỐI** đã được nhóm duyệt. Không bao giờ tự ghi vào đây.
3. **Quy tắc đặt tên file** theo README mục 4: `YYYY-MM-DD_ten_vX.Y_trangthai_nguoi.ext`. Dữ liệu thị trường bắt buộc phải có ngày.

## 4. Quy ước Kỹ Thuật
- **Báo cáo LaTeX (`04_bao-cao-latex\`)**: Biên dịch bằng `xelatex` + `biber`.
- **Tính toán AHP/TOPSIS**: Sử dụng script thông qua `mcdm-toolkit`, tuyệt đối không tự tính tay. Ma trận nào CR > 0.1 bị xem là hỏng, dừng và báo user.
- **Viết báo cáo**: Nháp tiếng Việt trước, viết lại tiếng Anh độc lập (không dịch word-by-word) thông qua skill `professional_writing`.
