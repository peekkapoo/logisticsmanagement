# Đòi lại tự do cho Ổ đĩa C: Kỹ thuật quản lý Cache của Hugging Face và PyTorch

Bạn cài một thư viện AI (ví dụ: Docling, Transformers) bằng pip, dung lượng tải về chỉ vỏn vẹn 30MB. Bạn yên tâm ấn nút chạy. Đùng một cái, máy tính báo ổ đĩa C đỏ lòm, dung lượng sụt giảm hàng chục Gigabyte! Chuyện quái gì vừa xảy ra vậy?

Chào mừng bạn đến với sự khác biệt giữa **Source Code** (Mã nguồn) và **Model Weights** (Trọng số mô hình) trong Deep Learning.

## 1. Kẻ trộm giấu mặt: `~/.cache/huggingface`
Khác với phần mềm thông thường, một công cụ AI chỉ là một cái "vỏ não". Để công cụ đó biết đọc chữ (OCR) hay nhận diện bảng biểu, nó phải tải các mô hình trí tuệ nhân tạo (Model Weights) từ trên mạng về (đặc biệt là từ thư viện Hugging Face). 

Những file mô hình này rất nặng (thường có định dạng `.pth`, `.bin` hoặc `.safetensors`), từ vài trăm MB đến cả chục GB. 

**Điều tệ hại là:** Mặc định, Hugging Face và PyTorch sẽ lẳng lặng tải toàn bộ đống đồ sộ này vào ổ đĩa hệ thống của bạn, giấu sâu ở thư mục:
`C:\Users\Tên_Của_Bạn\.cache\huggingface\hub`

Nếu bạn đang dùng một ổ SSD 256GB chỉ để cài Windows, ổ đĩa của bạn sẽ nhanh chóng "thở oxy".

## 2. Dời "Não bộ" AI đi nơi khác
Làm thế nào để ra lệnh cho AI tải mô hình vào ổ D (ổ dữ liệu) hoặc một thư mục cục bộ của dự án thay vì nhồi nhét vào ổ C?

Rất may mắn, các nền tảng AI lớn đều có thiết kế cửa hậu (Backdoor) cho phép bạn chuyển hướng kho lưu trữ thông qua các **Biến môi trường (Environment Variables)**.

Chỉ cần đặt đoạn code này lên đầu script Python của bạn:

```python
import os
from pathlib import Path

# Thư mục ổ D mà bạn muốn lưu trữ AI
models_dir = Path("D:/My_AI_Project/models")
models_dir.mkdir(parents=True, exist_ok=True)

# Lệnh chuyển hướng (Redirect)
os.environ["HF_HOME"] = str(models_dir)     # Dành cho Hugging Face
os.environ["TORCH_HOME"] = str(models_dir)  # Dành cho PyTorch
```

## 3. Lợi ích kép (Double Win)
Khi chạy đoạn code trên, phép màu sẽ xảy ra:
1. **Bảo vệ ổ C:** Toàn bộ ổ đĩa hệ thống của bạn được giải thoát, giúp Windows chạy mượt mà và an toàn.
2. **Tính Đóng gói (Portability):** Dự án AI của bạn giờ đây đã được gói gọn toàn bộ trong ổ D. Bạn có thể copy cả thư mục dự án đó mang sang máy khác chạy mà không cần tốn thời gian (và băng thông mạng) tải lại model AI hàng chục GB nữa!

---
*💡 Mẹo nhỏ: Bất cứ khi nào bạn cài đặt một thư viện AI mã nguồn mở mới, trước khi ấn `Run`, hãy luôn tự hỏi "Mô hình (Weights) của nó sẽ được tải về đâu?". Biết cách kiểm soát nó, bạn sẽ làm chủ hoàn toàn hệ thống của mình.*
