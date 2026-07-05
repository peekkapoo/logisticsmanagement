# Giải mã Lỗi 1455 và Bí ẩn Virtual Memory

## Sự cố sập nguồn giữa chừng
Bạn đang hừng hực khí thế tải một mô hình AI ngôn ngữ lớn (như Llama) hoặc chạy bộ công cụ phân tích tài liệu nặng (như Docling). Đột nhiên, máy tính đơ cứng, quạt tản nhiệt rú lên, và màn hình quăng vào mặt bạn dòng chữ lạnh lùng:
`OS error 1455: The paging file is too small for this operation to complete.`
Rõ ràng ổ cứng của bạn vẫn còn trống hàng chục GB, tại sao hệ thống lại báo "quá nhỏ"?

## Bàn bếp, Tủ lạnh và Chiếc bàn gập
Để hiểu lỗi này, hãy tưởng tượng máy tính của bạn là một căn bếp:
- **RAM (Bộ nhớ trong):** Là chiếc **bàn bếp**. Nó rất nhanh để thao tác, nhưng diện tích (dung lượng) lại hạn chế.
- **Ổ cứng (Drive C/D):** Là chiếc **tủ lạnh**. Rộng rãi, chứa được nhiều đồ, nhưng mỗi lần lấy đồ ra nấu lại rất chậm.

Khi bạn chạy mô hình AI, nó giống như việc bày một bữa tiệc khổng lồ ra bàn bếp. Bàn bếp (RAM) nhanh chóng bị lấp đầy! Để bếp không bị sập, hệ điều hành (Bếp trưởng) vội vàng lấy một chiếc **bàn gập tạm thời** (Pagefile) đặt ngay cạnh tủ lạnh để chứa bớt nguyên liệu.
Lỗi 1455 xảy ra khi chiếc bàn gập tạm thời này *cũng hết chỗ*, và Bếp trưởng thì không có quyền mở rộng nó thêm nữa.

## Tại sao Windows lại "báo ảo"?
Khi máy tính cạn kiệt RAM vật lý (Physical Memory) để nạp các khối trọng số (Tensors/Weights) khổng lồ của AI, Windows sẽ cầu cứu đến **Virtual Memory** (Bộ nhớ ảo). 
- Virtual Memory được lưu dưới dạng một file ẩn tên là `pagefile.sys` trên ổ cứng.
- Mặc định, Windows đặt file này ở ổ C và tự động quản lý kích thước. 
- Tuy nhiên, khi ổ C sắp đầy, hoặc khi AI đòi hỏi cấp phát một lượng bộ nhớ (Memory Allocation) tăng vọt quá nhanh, Windows không kịp (hoặc không thể) "phình" cái `pagefile.sys` ra thêm. Tiến trình nạp AI bị từ chối cấp phát RAM ngay lập tức, sinh ra lỗi OS Error 1455 [1].

## Giải pháp: Mua chiếc bàn gập to hơn
Giải pháp là tước quyền tự động của Windows và "chỉ định" một ổ đĩa rộng rãi hơn (ổ D) để làm Virtual Memory tĩnh:
1. Nhấn `Windows + R`, gõ `sysdm.cpl` -> Enter.
2. Chuyển sang tab **Advanced**, mục *Performance* chọn **Settings**.
3. Tab **Advanced**, mục *Virtual memory* chọn **Change**.
4. Bỏ tick ô *Automatically manage paging file size...*
5. Chọn ổ **C:** -> chọn **No paging file** -> Set.
6. Chọn ổ **D:** (ổ có nhiều dung lượng trống) -> chọn **Custom size**:
   - Initial size: `16384` (16GB)
   - Maximum size: `65536` (64GB - tùy thuộc độ trống ổ D)
7. Bấm **Set**, OK và Khởi động lại máy.

Lúc này, các mô hình AI có thể thoải mái "tràn" bộ nhớ xuống ổ D mà không lo bị ngắt ngang [2].

---
### Nguồn tham khảo (Citations)
- `[1]` Microsoft Learn, "Introduction to the page file".
- `[2]` Hugging Face Forums & GitHub Issues, "Resolving OS Error 1455 when loading large safetensors on Windows".
