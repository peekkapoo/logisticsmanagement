# Trói chặt "Quái vật" Đa luồng: Bí quyết chống giật/tràn RAM khi chạy AI bằng PyTorch

Có một sự thật ít người biết khi làm quen với Machine Learning: Các thư viện AI như PyTorch, TensorFlow hay NumPy không hề hiền lành. Mặc định, chúng là những con quái vật **cực kỳ tham lam** tài nguyên máy tính.

Nếu máy tính của bạn đột ngột bị sập hoặc văng lỗi khi vừa khởi chạy một model AI, 90% thủ phạm là do hội chứng "Cú sốc RAM" (RAM Spike) gây ra bởi xử lý Đa luồng (Multi-threading).

## 1. Chuyện gì xảy ra bên dưới mui xe?
CPU máy tính của bạn hiện nay thường có rất nhiều lõi/luồng (ví dụ Core i7 có 8 luồng, 16 luồng). 

Khi bạn ra lệnh cho AI (như Docling) đọc một file PDF, thay vì từ từ xử lý từng trang, PyTorch và các thư viện toán học (như OpenBLAS, MKL) sẽ ngay lập tức tung **TOÀN BỘ 16 luồng** vào cuộc chiến. 

**Vấn đề là ở đây:** Mỗi luồng khi hoạt động đều yêu cầu hệ điều hành cấp cho nó một phần RAM (Memory Buffer) để tính toán ma trận độc lập. 16 luồng cùng đòi hỏi một lúc tạo ra một mức tiêu thụ RAM khổng lồ dâng lên theo chiều thẳng đứng chỉ trong phần ngàn giây. 

RAM vật lý cạn kiệt, Virtual Memory không kịp bơm. Chào mừng bạn đến với Crash!

## 2. Nghệ thuật "Trói" Quái vật
Đôi khi, chậm mà chắc lại là chìa khóa để hoàn thành công việc. Chúng ta cần nói cho PyTorch biết: *"Hãy dùng đúng 1 luồng thôi, xếp hàng mà làm!"*.

Để làm được điều này, chúng ta không cần can thiệp vào code của thư viện AI. Thay vào đó, chúng ta can thiệp vào **Biến môi trường (Environment Variables)** ở cấp độ hệ điều hành.

Chỉ cần đặt những dòng code này ở **DÒNG ĐẦU TIÊN** của file Python (trước khi `import torch` hay bất kỳ thư viện nào khác):

```python
import os

# Trói PyTorch và các thư viện toán học lại về 1 luồng
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import torch # Bây giờ import mới an toàn!
```

## 3. Sự đánh đổi đáng giá
Khi ép xung số luồng về 1:
- **Tốc độ:** AI sẽ xử lý chậm hơn (có thể mất 5 giây thay vì 2 giây cho một tác vụ).
- **RAM:** Lượng RAM tiêu thụ sẽ chỉ bằng khoảng 1/10, duy trì một đường ngang bình ổn thay vì dựng đứng lên trời.
- **Sự ổn định:** Máy tính không bị đơ, không giật lag màn hình, bạn vẫn có thể vừa chạy AI vừa xem YouTube mượt mà.

---
*💡 Kết luận: Đừng để AI lộng hành chiếm đoạt tài nguyên. Là một kỹ sư, việc kiểm soát tài nguyên hệ thống thông qua các biến môi trường đa luồng là kỹ năng sinh tồn bắt buộc!*
