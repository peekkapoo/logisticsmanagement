# Kiểm soát Đa luồng (Multi-threading) trong PyTorch

## Khi CPU rú lên và RAM bốc hơi
Một buổi tối đẹp trời, bạn cho chạy một đoạn script AI khá nhẹ nhàng (như nhúng vector văn bản - Text Embeddings). Đột nhiên, Task Manager báo CPU hoạt động 100%, quạt tản nhiệt quay điên cuồng, và 32GB RAM của bạn bốc hơi sạch sẽ chỉ trong nháy mắt. Máy tính treo cứng. Bạn tự hỏi: "Mình chỉ xử lý vài dòng text cơ mà, sao lại ngốn tài nguyên như đào Bitcoin thế này?".

## Bài toán Xưởng may 16 công nhân
Hãy hình dung CPU của bạn là một xưởng may có 16 công nhân (tương ứng với 16 CPU cores), còn RAM chính là chiếc máy khâu duy nhất.

Khi có một xấp vải (dữ liệu) cần may, người quản đốc thiếu kinh nghiệm sẽ hét lên: "Tất cả xông vào!". Hậu quả là 16 công nhân cùng lao vào giành giật chiếc máy khâu. Họ chen lấn, dẫm đạp lên nhau, mỗi người cố lôi một miếng vải ra may. Thời gian dành cho việc "giành giật" (Context Switching) và nhồi nhét nguyên liệu còn tốn hơn cả thời gian may thực tế, dẫn đến toàn bộ xưởng sụp đổ.

## Nguồn cơn của thảm họa
Vấn đề nằm ở thiết lập mặc định của các thư viện AI như **PyTorch** hay **ONNX Runtime**:
- Theo mặc định, để tối đa hóa tốc độ, các thư viện này sẽ tự động sinh ra số lượng luồng tính toán (Threads) **bằng đúng với số nhân CPU** (hoặc logical cores) hiện có trên máy [1].
- Tuy nhiên, khi bạn chạy AI trong một môi trường có khả năng gọi đồng thời (như xử lý song song nhiều luồng - multithreading pool) hoặc các mô hình không yêu cầu tính toán ma trận quá nặng, việc mỗi worker lại tự bung ra 16 threads con sẽ dẫn đến bùng nổ cấp số nhân (Thread Explosion).
- Quá nhiều luồng tranh chấp nhau tài nguyên bộ nhớ đệm (Memory Cache Bandwidth), tạo ra Overhead khổng lồ, vắt kiệt cả CPU lẫn RAM [2].

## Giải pháp: Ra lệnh "Mỗi người làm một lúc"
Để khắc phục, chúng ta cần can thiệp vào biến môi trường của hệ điều hành, yêu cầu các thư viện lõi (như OpenMP, MKL) chỉ sử dụng **1 luồng tính toán** cho mỗi tác vụ. 

Thêm đoạn code này lên **dòng đầu tiên** của script (TRƯỚC KHI import PyTorch hay bất cứ thư viện AI nào):

```python
import os
# Ép các thư viện toán học lõi chỉ dùng 1 luồng
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
```

Chỉ với 5 dòng lệnh này, bạn đã bắt 16 công nhân xếp hàng ngay ngắn. Tài nguyên sẽ được giải phóng, máy tính chạy êm ru và mượt mà hơn gấp bội!

---
### Nguồn tham khảo (Citations)
- `[1]` PyTorch Official Documentation, "CPU threading and TorchScript inference".
- `[2]` OpenMP Architecture Review Board, "Thread Affinity and Thread Explosion issues in High-Performance Computing".
