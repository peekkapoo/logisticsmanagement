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

## 5. Tiêu chuẩn Tech-blog Vibecoding (`08_new_knowledge\`)
Thư mục `08_new_knowledge` là "bộ não thứ hai" của user (Non-IT). Khi lưu kiến thức mới vào đây, Agent **BẮT BUỘC** phải tuân thủ:
1. **Flow Logic 5 bước (Chỉ là luồng tư duy ẩn, KHÔNG đặt tiêu đề máy móc kiểu "The Hook", "The Analogy"):** 
   - *Bước 1 (Mở bài):* Tình huống lỗi/Nỗi đau thực tế. Đặt tiêu đề gợi sự đồng cảm.
   - *Bước 2 (Giải thích):* Bắt buộc dùng phép ẩn dụ đời thường (Mental Model) để giải thích khái niệm IT. Đặt tiêu đề ẩn dụ.
   - *Bước 3 (Nguyên nhân):* Giải thích bản chất học thuật dựa trên phép ẩn dụ. 
   - *Bước 4 (Giải pháp):* Code/Các bước khắc phục rõ ràng.
   - *Nguồn trích dẫn:* Nguồn trích dẫn (Footnote `[1]`, `[2]`) từ Official Docs, Reputable Forums, Academic Papers. Tiêu đề: "Nguồn tham khảo".
2. **Quy trình:** Bắt buộc dùng skill `professional-writing` (TBT → Lead → Staff) để đảm bảo chất lượng research và văn phong đồng cảm, dễ hiểu (de-jargonized).
3. **Quy tắc đặt tiêu đề (H1):** Tiêu đề chính bên trong bài viết KHÔNG ĐƯỢC chứa các tiền tố đánh số như "Bài 01:", "Bài 02:". Việc đánh số thứ tự chỉ được dùng cho tên file để hệ thống quản lý.

## 6. Tiêu chuẩn Academic Writing & Cross-Reference
Khi thực hiện các báo cáo mang tính học thuật (như Literature Review, Phân tích dữ liệu), Agent BẮT BUỘC tuân thủ:
1. **Flow & Formatting:** Tuyệt đối KHÔNG sử dụng gạch đầu dòng (bullet points) hoặc nhãn in đậm kiểu AI (`**Khái niệm:**`, `**Quan điểm:**`). Phải viết thành các đoạn văn (paragraphs) liền mạch, có độ dài ngắn biến thiên tự nhiên, thể hiện rõ tính phản biện (Agreements/Disagreements).
2. **In-text Citations linh hoạt (VN/EN):** Tích hợp trích dẫn vào cấu trúc ngữ pháp câu như một chủ thể hành động. 
   - *Với tiếng Việt:* Dùng cấu trúc linh hoạt như *"Theo nghiên cứu của Nguyễn và cộng sự (2024)..."* hoặc *"Dữ liệu từ Trần (2023) minh chứng..."*. Tránh để `[1]` vô hồn ở cuối câu.
   - *Với tiếng Anh (báo cáo LaTeX):* Phải linh hoạt tuân theo quy tắc chia thì (Tense) và cấu trúc academic English (ví dụ: *"Smith et al. (2023) argued that..."* hoặc *"Recent evidence suggests... (Doe, 2024)"*).
3. **Cross-Reference Check:** Danh mục "Tài liệu tham khảo" ở cuối bài CHỈ ĐƯỢC PHÉP chứa những tài liệu đã được thực sự gọi tên (in-text citation) trong bài viết. Nghiêm cấm bốc toàn bộ file/database đưa vào danh mục nếu không sử dụng trong văn bản.
