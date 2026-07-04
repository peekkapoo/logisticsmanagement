# Nhật ký dự án (Task Log)

> **Mục đích:** File này lưu trữ bộ nhớ trạng thái của dự án để AI nắm bắt ngay tiến độ khi bắt đầu một phiên làm việc (session) mới mà không cần User phải nhắc lại bối cảnh.
> **Quy tắc đối với AI:** BẮT BUỘC phải đọc file này đầu tiên ở mỗi phiên chat, và CẬP NHẬT lại tiến độ vào file này trước khi kết thúc công việc. Mọi bản ghi nhận công việc mới ĐỀU PHẢI có thời gian (timestamp) theo format YYYY-MM-DD HH:MM:SS.

## 1. Trạng thái hiện tại (Current Status)
- **Phase hiện tại:** Tư vấn kiến trúc hệ thống, tích hợp Antigravity & NotebookLM.
- **Cập nhật gần nhất (2026-07-04 22:45:00):** Tư vấn tính khả thi và giải pháp tích hợp NotebookLM vào Antigravity.

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
- [x] [2026-07-04 22:15:00] Crawl CellphoneS (laptop văn phòng): Lọc 7 sản phẩm có giá KM từ 20-25tr. Lưu vào `02_du-lieu-tho\laptop-thi-truong\`.
- [x] [2026-07-04 22:20:00] Lên chiến lược tìm kiếm tài liệu (Literature Review): cung cấp boolean strings cho Scopus và prompts cho Elicit AI, Consensus.
- [x] [2026-07-04 22:45:00] Tư vấn tính khả thi và giải pháp tích hợp NotebookLM vào hệ thống Antigravity để trích xuất dữ liệu tự động.
- [x] [2026-07-04 22:46:00] Biên dịch lại báo cáo LaTeX (main.pdf) để cập nhật trang bìa hiển thị đối tượng "Office Workers".

## 3. Các bước tiếp theo (Next Steps)
- Nếu user duyệt danh sách 7 laptop văn phòng, chạy Bước 2 (map benchmark CPU/GPU hoặc trọng lượng/pin tuýp văn phòng).
- Bước 3 (làm sạch + ma trận quyết định TOPSIS).
- Sử dụng skill `task-processor` để tiếp nhận và điều phối mọi yêu cầu mới.

## 4. Cảnh báo & Ngữ cảnh quan trọng (Warnings & Context)
- **Tuyệt đối tuân thủ 3 luật vàng về quản lý file:** `02_du-lieu-tho` là vùng đóng băng, `06_nop-bai` là vùng thiêng liêng chỉ chứa bản final. Mọi dữ liệu làm việc phải lưu tại `03_phan-tich`.
- Luôn dùng `xelatex` và `biber` để biên dịch báo cáo LaTeX.
- Việc tính toán AHP/TOPSIS bắt buộc phải gọi skill `mcdm-toolkit`, không tự tính tay.
