# Kiến trúc Hệ thống: Tối ưu Không Gian Tên và Quản trị Mã nguồn với Git

## 1. Không Gian Tên Phẳng (Flat Namespace): Tránh "Bóng Đêm" Thư Mục
Khi tổ chức file trong các dự án công nghệ, một bản năng tự nhiên là phân loại chúng vào các thư mục lồng nhau nhiều lớp (Deep Nesting) — ví dụ: `.agents/skills/nhom_A/phong_ban_B/skill_1`. 

Mặc dù có vẻ gọn gàng dưới con mắt con người, điều này lại là một thảm họa đối với các hệ thống quét tự động (Auto-discovery Parsers) của AI. Để bảo vệ tài nguyên phần cứng (I/O) và tránh các vòng lặp vô hạn, các trình quét này thường được giới hạn độ sâu (Max Depth). Bất kỳ file nào nằm quá giới hạn đó sẽ biến thành một "điểm mù" (Unreachable).

**Thực hành chuẩn (Best Practice):** 
Kiến trúc tối ưu là **Không Gian Tên Phẳng (Flat Namespace)**. Giống như việc bạn trải tất cả hồ sơ lên một chiếc bàn lớn thay vì nhét chúng vào các ngăn kéo lồng nhau, Flat Namespace đưa tất cả các thư mục con ra ngang hàng. Điều này giúp:
- Indexing (lập chỉ mục) diễn ra tức thì.
- Tránh được rủi ro vượt quá giới hạn ký tự đường dẫn tối đa (Path Length Limit) trên hệ điều hành Windows.

## 2. Bản chất của Git: Cỗ Máy Thời Gian Nguyên Tử
Làm việc với mã nguồn hay tài liệu quan trọng mà không có Git, giống như bạn đi bộ trên dây mà không có lưới bảo hộ. Một lần ấn nhầm "Lưu đè" (Ctrl+S) có thể cuốn bay công sức hàng tháng trời.

**Git không phải là một công cụ sao lưu thông thường (Backup tool).** Khác với các hệ thống cũ lưu trữ sự thay đổi dựa trên file (Delta-based), Git lưu trữ dữ liệu dưới dạng các bản Snapshot (Ảnh chụp) của một hệ thống file mini [1].

Mỗi khi bạn thực hiện một `commit`, Git chụp lại "bức ảnh" toàn bộ dự án tại khoảnh khắc đó, gắn cho nó một dấu vân tay mã hóa (SHA-1 Checksum) và lưu lại vĩnh viễn [2]. Không một ai có thể thay đổi lịch sử mà Git không phát hiện ra.

## 3. Workflow: Từ Ý Tưởng đến Sản Phẩm
Trái tim của Git nằm ở sự phân tách các môi trường làm việc thông qua khái niệm **Branch (Nhánh)**. 

Thay vì sao chép toàn bộ dự án ra một thư mục `Copy of Project_Final` để thử nghiệm tính năng mới, Git Branch hoạt động như một con trỏ (pointer) siêu nhẹ chỉ vào một điểm trong lịch sử [3]. Bạn có thể tạo ra vô số "vũ trụ song song" để thử nghiệm các ý tưởng rủi ro một cách hoàn toàn độc lập với dòng thời gian chính (`main`) [4].

**Ba bước thao tác cốt lõi hàng ngày:**
1. **Chuẩn bị (Staging):** Lệnh `git add .` không lập tức ghi lại lịch sử. Nó đưa các file thay đổi vào Vùng Đệm (Index/Staging Area). Vùng đệm thông minh này cho phép bạn chia nhỏ các thay đổi khổng lồ thành nhiều nhóm nhỏ mang ý nghĩa độc lập [5].
2. **Ghi Lịch Sử (Commit):** Lệnh `git commit -m "Chú thích"` biến các file trong Vùng Đệm thành một Snapshot không thể thay đổi [2].
3. **Phân Tán (Push):** Khác với hệ thống tập trung (Centralized), Git là hệ thống Phân tán (Distributed). Kho lưu trữ trên máy tính của bạn chứa 100% lịch sử dự án. Lệnh `git push` chỉ đơn giản là đồng bộ các Snapshot mới của bạn lên đám mây (như GitHub) để phối hợp với đồng nghiệp [1].

---
### Nguồn Tham Khảo (Citations)
- `[1]` Atlassian Git Tutorial, "What is Git - Distributed Version Control Systems".
- `[2]` Atlassian Git Tutorial, "git commit - Recording snapshots to the repository history".
- `[3]` Atlassian Git Tutorial, "Git Branching - Lightweight pointers".
- `[4]` Atlassian Git Tutorial, "Isolating independent lines of development".
- `[5]` Atlassian Git Tutorial, "git add - Staging changes".
