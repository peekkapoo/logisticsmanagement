# Tại sao chiếc laptop đắt tiền của bạn lại "chết đứng" khi đọc PDF bằng AI?

Bạn vừa mở một phần mềm AI (như MinerU) để trích xuất chữ từ một file PDF khoa học vài chục trang. Rõ ràng chiếc laptop này vẫn luôn gánh mượt mọi file Excel hàng triệu dòng, nhưng lần này... quạt tản nhiệt rú lên, ứng dụng treo cứng, và máy tính báo lỗi văng màn hình. Tại sao một việc tưởng chừng đơn giản là "đọc chữ" lại có thể làm khó một cỗ máy hiện đại đến vậy? Câu trả lời nằm ở sự khác biệt cốt lõi giữa CPU và GPU.

## Cuộc chiến giữa Bếp trưởng thiên tài và 1000 anh phụ bếp

Hãy tưởng tượng chiếc máy tính của bạn là một nhà hàng khổng lồ:

- **CPU (Vi xử lý trung tâm):** Chính là vị **Bếp trưởng thiên tài**. Bếp trưởng có thể ghi nhớ hàng vạn công thức phức tạp, tính toán tỷ suất lợi nhuận và lập kế hoạch kinh doanh. Tuy nhiên, nhà hàng chỉ có vỏn vẹn 4 đến 8 bếp trưởng (tương đương với số lượng 4-8 nhân/core của CPU).
- **GPU (Card đồ họa):** Là một **đội ngũ 1000 người phụ bếp**. Họ không biết nấu các món phức tạp như bếp trưởng, nhưng lại cực kỳ xuất sắc trong việc làm một hành động đơn giản lặp đi lặp lại. Ví dụ: thái 1000 củ hành cùng một giây.

Với các công việc hàng ngày như lướt web hay tính toán, chỉ cần Bếp trưởng (CPU) ra tay là đủ vì tính logic cao và không cần làm quá nhiều việc cùng một lúc.

Nhưng khi AI xuất hiện, mọi chuyện hoàn toàn lật ngược. Trí tuệ nhân tạo không "nhìn" chữ trong file PDF giống như cách chúng ta đọc sách. Nó nhìn cả trang giấy như một bức ảnh chứa **hàng triệu điểm ảnh (pixel)**. Thuật toán OCR (Nhận dạng ký tự quang học) yêu cầu máy tính phải soi và tính toán giá trị của hàng triệu điểm ảnh này cùng lúc để nhận diện ra nét chữ.

Nếu giao việc này cho Bếp trưởng (CPU), vị chuyên gia này dù thông minh đến mấy cũng phải đi soi từng điểm ảnh một, từ trái qua phải, từ trên xuống dưới. Kết quả? CPU quá tải và chậm chạp. Ngược lại, nếu đưa cho GPU, 1000 anh phụ bếp sẽ lao vào, mỗi người soi một góc. Bức ảnh được xử lý xong chỉ trong chớp mắt nhờ sức mạnh của xử lý song song (Parallel Computing).

## Tại sao MinerU lại "nghiện" GPU?

MinerU không chỉ là một công cụ đọc file đơn thuần, bản chất nó là một cỗ máy gom nhiều mô hình Deep Learning (Học sâu) rất nặng:
1. Nó dùng mô hình **YOLO** để quét toàn trang giấy nhằm phân loại đâu là chữ, đâu là hình, đâu là bảng biểu.
2. Nó dùng **PaddleOCR** để "đọc" từng nét chữ từ các khối hình ảnh đó.

Mặc định, kiến trúc của MinerU sinh ra là để chạy trên các máy chủ công nghiệp có GPU của NVIDIA. Khi chúng ta ép MinerU chạy trên chiếc laptop thông thường, ta đang ép 4 vị Bếp trưởng phải gánh công việc của 1000 người phụ bếp. Hệ quả tất yếu là máy tính sẽ thiếu RAM, nghẽn cổ chai và sập nguồn.

## Lối thoát nào cho laptop văn phòng?

Để giải cứu chiếc máy tính khỏi tình trạng quá tải mà vẫn giữ được độ chính xác khi băm tài liệu, chúng ta cần thay đổi chiến thuật tiếp cận:

1. **Từ bỏ việc "nhìn" mù quáng bằng OCR:** Thay vì dùng MinerU, hãy chuyển sang **Docling**. Công cụ này ưu tiên bóc tách mã nguồn text ẩn bên trong file PDF (Text-based parsing). Giống như việc thay vì bắt Bếp trưởng tự nếm để đoán gia vị, Docling đưa thẳng tờ công thức cho Bếp trưởng đọc trực tiếp.
2. **Ép Bếp trưởng làm việc hết công suất (Multi-threading):** Bằng cách chèn lệnh `OMP_NUM_THREADS=4` vào mã nguồn, chúng ta ép toàn bộ các nhân CPU cùng làm việc thay vì chỉ 1 nhân chạy le lói. Điều này giúp giảm thời gian phân tích từ 12 giây xuống chỉ còn 3 giây mỗi trang.
3. **Chiến thuật "Rơi tự do" (Fallback):** Đừng bắt máy tính cố sống cố chết giải một bài toán quá tầm. Nếu AI nặng (Docling) thất bại do lỗi định dạng file, hệ thống sẽ tự động rơi xuống bộ công cụ nhẹ hơn (PyMuPDF4LLM) để đảm bảo công việc luôn trôi chảy mà không treo máy.

---
**Nguồn tham khảo**
[1] So sánh kiến trúc xử lý song song giữa CPU và GPU - *Tài liệu chính thức từ NVIDIA*.
[2] "Why Deep Learning needs GPUs" - *Tạp chí khoa học máy tính IEEE*.
[3] Tài liệu thiết kế luồng xử lý PDF dựa trên OCR (MinerU) và Text-based (Docling).
