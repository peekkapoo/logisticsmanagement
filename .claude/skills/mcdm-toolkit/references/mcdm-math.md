# Cơ sở toán học AHP và TOPSIS

Tài liệu tham chiếu để (a) hiểu script đang làm gì, (b) viết mục 3.3 và 3.4 chương Methodology của báo cáo. Nguồn gốc: Saaty (1980) cho AHP, Hwang & Yoon (1981) cho TOPSIS — cả hai đã có sẵn trong `references.bib` (khóa `Saaty1980`, `HwangYoon1981`).

## AHP

### Thang so sánh cặp Saaty

| Giá trị a_ij | Ý nghĩa (i so với j) |
|---|---|
| 1 | Quan trọng như nhau |
| 3 | Hơi quan trọng hơn |
| 5 | Quan trọng hơn rõ rệt |
| 7 | Quan trọng hơn rất nhiều |
| 9 | Quan trọng hơn tuyệt đối |
| 2,4,6,8 | Mức trung gian |
| Nghịch đảo | a_ji = 1/a_ij |

### Tính trọng số

Script tính bằng cả hai cách và in ra để đối chiếu (chênh lệch lớn cũng là dấu hiệu bất nhất):

1. **Geometric mean of rows (Crawford-Williams):** GM_i = (∏_j a_ij)^(1/n), rồi w_i = GM_i / Σ GM_k.
2. **Eigenvector (chuẩn Saaty):** vector riêng ứng với giá trị riêng lớn nhất λmax của ma trận A, tính bằng power iteration (nhân lặp A·w rồi chuẩn hóa đến hội tụ).

### Kiểm định nhất quán

- λmax = trung bình của (A·w)_i / w_i
- CI = (λmax − n) / (n − 1)
- CR = CI / RI, đạt khi **CR ≤ 0.1**

Bảng Random Index (RI) của Saaty:

| n | 1-2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RI | 0 | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 | 1.49 | 1.51 | 1.48 | 1.56 | 1.57 | 1.59 |

### Tổng hợp nhiều chuyên gia

Chuẩn AIJ (Aggregation of Individual Judgments): phần tử tổng hợp = **geometric mean** các phần tử tương ứng của những ma trận ĐẠT CR. Ma trận hỏng loại khỏi tổng hợp, không "pha loãng" cho đạt.

## TOPSIS

Cho ma trận quyết định X (m phương án × n tiêu chí), trọng số w từ AHP:

1. **Chuẩn hóa vector:** r_ij = x_ij / √(Σ_i x_ij²)
2. **Nhân trọng số:** v_ij = w_j · r_ij
3. **Giải pháp lý tưởng:** A⁺_j = max_i v_ij nếu benefit, min nếu cost; A⁻ ngược lại.
4. **Khoảng cách Euclid:** D⁺_i = √(Σ_j (v_ij − A⁺_j)²), D⁻_i tương tự với A⁻.
5. **Hệ số gần gũi:** C_i = D⁻_i / (D⁺_i + D⁻_i) ∈ [0,1], càng gần 1 càng tốt.
6. **Xếp hạng** giảm dần theo C_i.

## Sensitivity analysis (mục 4.5 báo cáo)

Với từng tiêu chí j: nhân w_j với (1±10%), (1±20%), chuẩn hóa lại tổng = 1, chạy lại TOPSIS. Nếu top 3 không đổi trong mọi kịch bản → kết luận bền vững (robust). Nếu đổi → chỉ ra tiêu chí nhạy và bàn luận trong chương Discussion.

## Vì sao AHP cho trọng số nhưng TOPSIS cho xếp hạng (luận điểm mục 5.2)

AHP chấm k phương án trên n tiêu chí cần n · k(k−1)/2 phép so sánh cặp — với 20 laptop và 8 tiêu chí là 1.520 phép so sánh, bất khả thi cho người điền và CR gần chắc chắn vỡ. TOPSIS nhận thẳng dữ liệu định lượng khách quan (giá, benchmark) với số phương án tùy ý. Kết hợp AHP (trọng số từ phán đoán chuyên gia có kiểm soát nhất quán) + TOPSIS (xếp hạng từ dữ liệu khách quan) là mô hình hybrid chuẩn trong literature.
