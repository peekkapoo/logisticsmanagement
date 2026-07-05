# Quản lý "Nhà kho" Hugging Face (Cache Management)

## Ổ C bỗng dưng "bay màu"
Bạn vừa cài đặt một thư viện AI mới và tải thử vài mô hình Open-source về máy. Mọi thứ chạy rất mượt. Nhưng vài ngày sau, bạn nhận được cảnh báo đáng sợ từ Windows: `Low Disk Space`. Mở My Computer lên, bạn tá hỏa nhận ra ổ C: của mình giờ chỉ còn đúng... 0 bytes trống, dù bạn không hề cài đặt thêm phần mềm nào nặng. Dữ liệu rác từ đâu chui ra?

## Gã giao hàng IKEA và Phòng khách của bạn
Hugging Face (Hub chứa các mô hình AI lớn nhất thế giới) giống như siêu thị nội thất IKEA. Các mô hình AI (như Llama, BERT) chính là những món đồ nội thất khổng lồ nặng hàng chục Gigabyte.

Khi bạn chạy code tải AI, bạn giao việc cho anh shipper của Hugging Face. Theo mặc định, anh shipper này rất lười. Anh ta không thèm hỏi bạn muốn cất đồ ở đâu, mà tự động vứt toẹt toàn bộ đống nội thất khổng lồ đó ngay tại **Phòng khách** của bạn (chính là ổ C: mặc định của hệ điều hành). Phòng khách chật ních, và bạn không còn lối để đi lại. Việc của chúng ta là phải chỉ mặt đặt tên: "Hãy giao hàng ra cái **Nhà kho** (Ổ D:) ngoài kia!".

## Điều gì đang lén lút diễn ra?
Khi bạn sử dụng thư viện `transformers` hay `huggingface_hub` để load model, hệ thống sẽ tự động tải các tệp trọng số (file `.bin`, `.safetensors` nặng hàng chục GB) về máy tính để không phải tải lại ở lần sau.
- Vị trí lưu trữ mặc định trên Windows luôn là: `C:\Users\<Tên_User>\.cache\huggingface\hub` [1].
- Thư mục `.cache` này bị ẩn, nên người dùng thông thường rất khó phát hiện ra ổ C: của mình bị "ăn mòn" bởi hàng loạt phiên bản mô hình AI khác nhau.

## Giải pháp: Đổi địa chỉ giao hàng
Để di dời "nhà kho" này sang ổ đĩa có dung lượng lớn hơn (ví dụ ổ `D:\`), bạn có 2 cách.

**Cách 1: Thiết lập vĩnh viễn trên Windows (Khuyên dùng)**
Thiết lập Biến môi trường (Environment Variables) để anh shipper ghi nhớ mãi mãi:
1. Mở Start Menu, gõ `Environment Variables` -> Chọn *Edit the system environment variables*.
2. Bấm nút **Environment Variables...**
3. Ở phần *User variables*, bấm **New...**
4. Tạo biến mới với tên: `HF_HOME`, giá trị: `D:\AI_Cache\huggingface` (thay đường dẫn tùy ý bạn).
5. OK và khởi động lại Terminal.

**Cách 2: Gắn lệnh trực tiếp trong Code (Dùng một lần)**
Chèn đoạn code này lên **dòng đầu tiên** của file Python, trước khi import bất kỳ thư viện Hugging Face nào:
```python
import os
# Đổi địa chỉ kho chứa sang ổ D
os.environ["HF_HOME"] = "D:\\AI_Cache\\huggingface"

# Sau đó mới import transformers
from transformers import AutoModel
```
Từ nay, phòng khách ổ C: của bạn sẽ luôn sạch sẽ và rộng rãi!

---
### Nguồn tham khảo (Citations)
- `[1]` Hugging Face Documentation, "Cache Setup - Managing the cache directory".
- `[2]` GitHub, Hugging Face `huggingface_hub` repository, Environment Variables Reference.
