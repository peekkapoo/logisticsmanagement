# Nhật ký dự án (Task Log)

> **Mục đích:** File này lưu trữ bộ nhớ trạng thái của dự án để AI nắm bắt ngay tiến độ khi bắt đầu một phiên làm việc (session) mới mà không cần User phải nhắc lại bối cảnh.
> **Quy tắc đối với AI:** BẮT BUỘC phải đọc file này đầu tiên ở mỗi phiên chat, và CẬP NHẬT lại tiến độ vào file này trước khi kết thúc công việc. Mọi bản ghi nhận công việc mới ĐỀU PHẢI có thời gian (timestamp) theo format YYYY-MM-DD HH:MM:SS.

## 1. Trạng thái hiện tại (Current Status)
- **Phase hiện tại:** Cập nhật lại phạm vi dự án và chuẩn bị thu thập dữ liệu thử nghiệm mới.
- **Cập nhật gần nhất (2026-07-04 22:05:00):** Đã đổi đối tượng từ "nhà thiết kế đồ họa" sang "nhân viên văn phòng". Chuyển dữ liệu crawl cũ vào thư mục `_cu`.

## 2. Công việc vừa hoàn thành (Recently Completed)
- [x] [2026-07-04 19:28:12] Tạo `AGENTS.md` với các rules của dự án.
- [x] [2026-07-04 19:28:43] Di chuyển thư mục `skill` cũ sang `.agents/skills`.
- [x] [2026-07-04 19:30:05] Tạo file bộ nhớ `task_log.md`.
- [x] [2026-07-04 20:06:05] Tạo `.agents/skills.json` đăng ký các thư mục lồng sâu và xóa các skill trùng lặp.
- [x] [2026-07-04 20:09:00] Đổi tên skill `viet-chuyen-nghiep` thành `professional-writing` để đồng bộ hệ thống.
- [x] [2026-07-04 20:32:00] Tái cấu trúc và biên soạn lại thư mục `08_new_knowledge` theo quy trình chuẩn Tòa soạn Báo chí.
- [x] [2026-07-04 20:45:00] Cài đặt extension LaTeX Workshop và cấu hình mặc định biên dịch bằng `xelatex` + `biber`.
- [x] [2026-07-04 20:51:00] Biên soạn và xuất bản `03_kien-truc-antigravity.md` có trích dẫn học thuật vào kho kiến thức.
- [x] [2026-07-04 20:52:00] Cải tiến lõi skill `professional-writing` lên v3.3 (Ép buộc kiểm tra trích dẫn/sự thật cho mọi thể loại bài viết).
- [x] [2026-07-04 20:57:00] Cập nhật `README.md` để đồng bộ kiến trúc mới (Antigravity IDE, LaTeX Live Preview, Skill V3.3).
- [x] [2026-07-04 21:58:00] Crawl thử CellphoneS (laptop đồ họa 20-25tr): 20 sản phẩm raw → 5 sản phẩm sau lọc giá. Lưu CSV listing + CSV chi tiết vào `02_du-lieu-tho\laptop-thi-truong\`.
- [x] [2026-07-04 22:00:00] Xóa skill `crawl-laptop-data` (trùng lắp với `data-pipeline`). Cập nhật `AGENTS.md` routing.
- [x] [2026-07-04 22:05:00] Cập nhật toàn bộ project: Đổi đối tượng sang nhân viên văn phòng (README, KE-HOACH, LaTeX, Slide, v.v.), lưu trữ dữ liệu crawl cũ.

## 3. Các bước tiếp theo (Next Steps)
- Tiến hành crawl lại dữ liệu thử nghiệm cho đối tượng "laptop văn phòng 20-25tr" từ CellphoneS.
- Cập nhật lại các tiêu chí đánh giá cho phù hợp với dân văn phòng (màn hình, bàn phím, pin, trọng lượng...) thay vì đồ họa (nếu cần, xin ý kiến User).
- Sử dụng skill `task-processor` để tiếp nhận và điều phối mọi yêu cầu mới.

## 4. Cảnh báo & Ngữ cảnh quan trọng (Warnings & Context)
- **Tuyệt đối tuân thủ 3 luật vàng về quản lý file:** `02_du-lieu-tho` là vùng đóng băng, `06_nop-bai` là vùng thiêng liêng chỉ chứa bản final. Mọi dữ liệu làm việc phải lưu tại `03_phan-tich`.
- Luôn dùng `xelatex` và `biber` để biên dịch báo cáo LaTeX.
- Việc tính toán AHP/TOPSIS bắt buộc phải gọi skill `mcdm-toolkit`, không tự tính tay.
