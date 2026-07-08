# Nhật ký dự án (Task Log)

> **Mục đích:** File này lưu trữ bộ nhớ trạng thái của dự án để AI nắm bắt ngay tiến độ khi bắt đầu một phiên làm việc (session) mới mà không cần User phải nhắc lại bối cảnh.
> **Quy tắc đối với AI:** BẮT BUỘC phải đọc file này đầu tiên ở mỗi phiên chat, và CẬP NHẬT lại tiến độ vào file này trước khi kết thúc công việc. Mọi bản ghi nhận công việc mới ĐỀU PHẢI có thời gian (timestamp) theo format YYYY-MM-DD HH:MM:SS.

## 1. Trạng thái hiện tại (Current Status)
- **Phase hiện tại:** Tư vấn kiến trúc hệ thống, tích hợp Antigravity & NotebookLM.
- **Cập nhật gần nhất (2026-07-08 10:20:00):** Hoàn thành research + lên Implementation Plan nâng cấp kịch bản phỏng vấn v1.0 → v2.0. Chờ user review và duyệt trước khi thực thi.

## 2. Công việc vừa hoàn thành (Recently Completed)
- [x] [2026-07-08 10:20:00] Research phương pháp luận phỏng vấn bán cấu trúc (IPR Framework — Castillo-Montoya 2016, Delphi-AHP — Al Hazza et al. 2022, Cognitive Probing — Willis 2005). Lên Implementation Plan chi tiết nâng cấp kịch bản phỏng vấn v1.0 → v2.0 với 7 thay đổi lớn (Informed Consent, Stimulus Cards, Trade-off Scenarios, RQ-IQ Mapping, Template ghi chép, Closing protocol). Plan lưu tại artifact, **chờ user review**.
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
- [x] [2026-07-04 22:56:00] Tiếp nhận, đổi tên (chuẩn `TacGia_Nam_TuKhoa.pdf`) và phân loại 17 bài báo khoa học cùng 2 báo cáo Consensus/CSV vào `01_tai-lieu-tham-khao`. Xóa thư mục tạm `paper_search`.
- [x] [2026-07-04 22:58:37] Cập nhật tiến độ vào `timeline.md` (chuyển Phase 0 sang Hoàn thành, Phase 1 sang Đang làm).
- [x] [2026-07-04 23:03:15] 3 subagents đã hoàn thành việc đọc 17 file PDF và trích xuất thành công bộ tiêu chí vào `01_tai-lieu-tham-khao\tong-hop-tieu-chi.md` (T1.3).
- [x] [2026-07-04 23:06:53] Tự động trích xuất các DOI từ file CSV và gọi API `doi.org` để sinh thành công file `04_bao-cao-latex\references.bib` với 98 danh mục trích dẫn (T1.4).
- [x] [2026-07-04 23:07:58] Gộp kết quả NotebookLM và dữ liệu Subagents, phân nhóm thành 11 tiêu chí sơ bộ tại `03_phan-tich\tieu-chi\2026-07-04_danh-sach-tieu-chi-so-bo_v1.0_draft_AI.md` (T1.5).
- [x] [2026-07-04 23:09:23] Người dùng chốt danh sách 11 tiêu chí, chính thức đóng Phase 1 và chuẩn bị chuyển sang Phase 2 (T1.6). Tiến hành sao lưu và lưu lịch sử.
- [x] [2026-07-05 08:42:00] Tiếp nhận 17 file PDF đã được người dùng đổi tên qua Zotero, di chuyển vào `01_tai-lieu-tham-khao\bai-bao` (thay thế file cũ) và gộp nội dung `Exported Items.bib` vào `04_bao-cao-latex\references.bib`.
- [x] [2026-07-05 09:01:00] Phân tách và chuẩn hóa danh sách tiêu chí thành 14 tiêu chí độc lập theo chuẩn học thuật (áp dụng skill `professional-writing`). Gắn trích dẫn in-text và xuất danh mục tài liệu tham khảo. Lưu tại `03_phan-tich\tieu-chi\2026-07-05_danh-sach-tieu-chi-chinh-thuc_v1.0_draft_AI.md`.
- [x] [2026-07-05 09:34:00] Đã thực hiện Deep Read (đọc sâu toàn văn) 16 file PDF hợp lệ (loại bài unpublished). Audit và tuân thủ chặt chẽ skill `professional-writing`, viết lại hoàn toàn bản thảo Literature Review dựa trên số liệu, lập luận đối chiếu và citekey chính xác.
- [x] [2026-07-05 09:43:00] Cải thiện tuyệt đối skill `professional-writing` lên v3.5: Tích hợp công cụ `academic_parser.py` (Tiered Pipeline: Docling -> pdfplumber -> pypdf) vào hệ thống để đọc mượt mà báo cáo khoa học chứa công thức và bảng biểu. Áp dụng cơ chế Cache `02_du-lieu-tho/parsed_papers/` tự động băm (MD5).
- [x] [2026-07-05 10:10:00] Hoàn thành Deep Read 16 bài báo khoa học thông qua `academic_parser.py` (Cache Markdown MD5). Cập nhật và tinh chỉnh hệ thống tiêu chí đánh giá (bản Final) tại `03_phan-tich\tieu-chi\2026-07-05_danh-sach-tieu-chi-chinh-thuc_vFINAL.md` với các luận điểm và dẫn chứng định lượng cụ thể (trọng số AHP/TOPSIS).
- [x] [2026-07-05 11:04:00] Thiết lập Luật số 5 vào `AGENTS.md` và `README.md` quy định chuẩn Tech-blog cho thư mục `08_new_knowledge`.
- [x] [2026-07-05 11:04:00] Refactor 4 bài viết Tech-blog (04 đến 07) thành cấu trúc 5 bước (Hook, Analogy, Root Cause, Solution, Citations) và loại bỏ tiền tố đánh số ở tiêu đề chính.
- [x] [2026-07-05 12:14:00] Hoàn tất sử dụng skill `professional-writing` gọi kịch bản `academic_parser.py` để parse thành công toàn bộ 17/17 bài báo khoa học PDF, lưu cache Markdown tại `02_du-lieu-tho\parsed_papers\`.
- [x] [2026-07-05 12:22:00] Nâng cấp `academic_parser.py`: Thay thế Tier 2 (`pdfplumber`) bằng `pymupdf4llm` để xử lý triệt để bố cục 2 cột (2-column layout) của bài báo khoa học. Đã parse lại hoàn hảo 4 bài báo bị lỗi.
- [x] [2026-07-05 14:06:00] Chạy thành công tiến trình băm hàng loạt (batch parsing) 17/17 file PDF bằng hệ thống Tiered Pipeline (ưu tiên Docling thay cho MinerU bị nghẽn trên CPU). Kiểm tra ngẫu nhiên thấy Markdown giữ nguyên cấu trúc rất tốt. Cập nhật bài blog giải thích nguyên lý CPU/GPU cho người dùng.
- [x] [2026-07-05 14:13:48] Áp dụng vai trò TBT (skill `professional-writing`), thiết kế và chạy quy trình GATE để hoàn thiện toàn diện Hệ thống 14 Tiêu chí đánh giá Laptop. Trình sườn bài (Outline) cho user duyệt và sau đó xuất bản thành công bản thảo học thuật hoàn chỉnh (v4.1) tại `03_phan-tich\tieu-chi\2026-07-05_danh-sach-tieu-chi-chinh-thuc_vFINAL.md`.
- [x] [2026-07-05 14:23:00] Hoàn tất triển khai 3 Subagents đọc sâu 17 bài báo khoa học. Xóa bỏ file `extracted_insights.md` sơ sài và thay thế toàn bộ bản thảo `vFINAL.md` thành phiên bản **Literature Review chuyên sâu (v4.2)**. Đã khai thác cực tốt các định nghĩa học thuật, mức độ quan trọng và các quan điểm trái chiều (Agreements/Disagreements) giữa các tệp khách hàng.
- [x] [2026-07-05 14:31:00] Nâng cấp cấu hình lõi hệ thống dự án theo yêu cầu User: Cập nhật Luật số 6 (Academic Flow & Cross-Reference Check linh hoạt VN/EN) vào `AGENTS.md` và bổ sung Prompting Guide mẫu vào `README.md` nhằm loại bỏ triệt để văn phong máy móc, gạch đầu dòng và rác trích dẫn.
- [x] [2026-07-05 14:37:00] Hoàn tất rà soát Cross-Reference cho báo cáo Literature Review (`vFINAL.md`). Loại bỏ các trích dẫn thừa không xuất hiện trong bài, định dạng lại Danh mục tài liệu tham khảo theo đúng chuẩn APA 7th Edition, và bổ sung Bảng Tổng hợp Tiêu chí - Nguồn trích dẫn ở cuối bài.
- [x] [2026-07-05 14:40:00] User yêu cầu quay lại Phase 1: Xóa bỏ hoàn toàn bài báo "Elnatan and Tannady" khỏi dự án do không được xuất bản chính thức (không uy tín). Đã xóa PDF gốc, file Markdown parsed, và gỡ bỏ toàn bộ luận điểm/trích dẫn liên quan khỏi bản thảo Literature Review `vFINAL.md`. Tổng số bài báo hợp lệ rút xuống còn 15 bài.
- [x] [2026-07-05 15:15:00] Phân tích so sánh văn phong do user hiệu đính và bản nháp AI (khử tính từ mạnh, tăng tính liền mạch, tối ưu in-text citation). Phát triển và làm rõ luận điểm "Thương hiệu như một bộ lọc hấp thụ giá trị phần cứng" theo chuẩn academic writing.
- [x] [2026-07-05 15:15:00] Phân tích so sánh văn phong do user hiệu đính và bản nháp AI (khử tính từ mạnh, tăng tính liền mạch, tối ưu in-text citation). Phát triển và làm rõ luận điểm "Thương hiệu như một bộ lọc hấp thụ giá trị phần cứng" theo chuẩn academic writing.
- [x] [2026-07-05 15:18:00] Rà soát và đề xuất phát triển mở rộng các Mục 1, 2, 3, 4 theo yêu cầu của user. Bổ sung giải thích cơ sở lý luận (ví dụ: khấu hao công nghệ, trade-off pin-trọng lượng) và ví dụ thực tiễn cho từng luận điểm.
- [x] [2026-07-05 15:21:00] Hoàn thiện toàn bộ bài viết danh sách tiêu chí, tích hợp bản gốc đã hiệu đính của user cùng các điểm mở rộng luận điểm. Xuất bản lưu trữ thành công tại `03_phan-tich\tieu-chi\2026-07-05_danh-sach-tieu-chi-chinh-thuc_v5.0_final_user.md`.
- [x] [2026-07-05 15:25:00] Khắc phục lỗi thất lạc dữ liệu: Bổ sung lại "Bảng Tổng hợp Tiêu chí - Nguồn trích dẫn" và "Danh mục tài liệu tham khảo" chuẩn APA 7th Edition vào cuối file `v5.0_final_user.md`. Mọi Cross-Reference đã được đồng bộ.
- [x] [2026-07-05 15:27:00] Nâng cấp skill `professional-writing` lên version 4.0. Tích hợp sâu "Chuẩn Mực Academic Writing (Bắt Buộc)" vào bộ core prompt của TBT, quy định rõ 4 nguyên tắc: Khử tính từ mạnh, citation liền mạch, cấm dùng gạch đầu dòng, bắt buộc giải thích cơ sở lý luận & ví dụ thực chứng.
- [x] [2026-07-05 20:49:00] Hoàn thành phân tích và phát triển mở rộng luận điểm về card đồ họa (GPU) tại Mục 2 của `03_phan-tich\tieu-chi\2026-07-05_danh-sach-tieu-chi-chinh-thuc_v5.0_final_user.md`. Áp dụng skill `professional-writing` để phân tích sâu cơ chế đánh đổi vật lý (nhiệt lượng, pin, trọng lượng) và kinh tế (over-specification theo Rau & Fang, 2018).
- [x] [2026-07-05 20:53:00] Hoàn thành viết lại và nâng cấp học thuật đoạn văn về năng lực cốt lõi (CPU & RAM) tại Mục 2. Giải thích rõ cơ chế nút thắt cổ chai (bottleneck) và nền tảng vi kiến trúc, đồng thời khử hoàn toàn các tính từ mạnh ("sức nặng áp đảo") để tăng tính thuyết phục theo chuẩn Academic Writing v4.0.
- [x] [2026-07-05 21:15:04] Sửa lỗi cú pháp YAML (dấu hai chấm) trong file `SKILL.md` của `task-processor`. Áp dụng skill `professional-writing` (TBT) để biên soạn và xuất bản bài Tech-blog giải thích lỗi YAML này vào `08_new_knowledge\2026-07-05_yaml-parsing-error_v1.0_final_agent.md`.
- [x] [2026-07-05 22:15:00] Khởi động Phase 2 (Phỏng vấn chuyên gia). Thiết lập Kế hoạch triển khai chốt phương án phỏng vấn người thật. Hoàn thành T2.1: Viết kịch bản phỏng vấn bán cấu trúc tại `02_du-lieu-tho\phong-van\2026-07-05_kich-ban-phong-van_v1.0_draft_AI.md`. Hoàn thành T2.2: Lập danh sách chuyên gia dự kiến tại `00_quan-ly-du-an\bien-ban-hop\2026-07-05_danh-sach-chuyen-gia.md`.
- [x] [2026-07-06 17:15:00] Thực hiện commit và push toàn bộ thay đổi của dự án lên kho lưu trữ.
- [x] [2026-07-08 10:11:00] Merge toàn diện skill `professional-writing` từ bản cải tiến Claude (`professional-writing-improved`). Sửa ~25 file tham chiếu lỗi thời (`quality/`→`review/`, `style/`→`editorial/`, `meta/`→`development/`, `platform/`→`publishing/`, `examples/`→`archive/`). Cập nhật description YAML, version header lên v4.0, README và changelog. GIỮ NGUYÊN `scripts/academic_parser.py` cho Antigravity. Xóa thư mục tạm `professional-writing-improved/`.

## 3. Các bước tiếp theo (Next Steps)
- Đầu việc phân tích ma trận quyết định AHP/TOPSIS cho 7 laptop văn phòng đã bị **Hủy (Cancelled)** theo yêu cầu của user.
- Chờ chỉ thị tiếp theo từ user.
- Sử dụng skill `task-processor` để tiếp nhận và điều phối mọi yêu cầu mới.

## 4. Cảnh báo & Ngữ cảnh quan trọng (Warnings & Context)
- **Tuyệt đối tuân thủ 3 luật vàng về quản lý file:** `02_du-lieu-tho` là vùng đóng băng, `06_nop-bai` là vùng thiêng liêng chỉ chứa bản final. Mọi dữ liệu làm việc phải lưu tại `03_phan-tich`.
- Luôn dùng `xelatex` và `biber` để biên dịch báo cáo LaTeX.
- Việc tính toán AHP/TOPSIS bắt buộc phải gọi skill `mcdm-toolkit`, không tự tính tay.
