# Logistics Management - MADM Project: Laptop Selection

## 1. Project Overview
**Topic:** Multiple Attribute Decision Making (MADM) - Selecting an office laptop for an office worker.
**Methodology:** 
- Criteria Generation: Scientific Research -> Expert Interview -> Survey
- Weighting: AHP (Analytic Hierarchy Process)
- Ranking/Selection: TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)
**Final Output:** Academic essay in English (LaTeX format) & Presentation in English.

## 2. Directory Structure

- **`01_Admin/`**: Quản lý dự án, chứa file `brainstorm.md`, task list, biên bản họp nhóm (meeting minutes).
- **`02_Literature_Review/`**: Chứa các bài báo khoa học tham khảo, kịch bản phỏng vấn chuyên gia, và file raw data khảo sát (survey).
- **`03_Data/`**: Chứa dataset thu thập từ CellphoneS (giá, cấu hình) và các benchmark scores (CPU, GPU, màn hình).
- **`04_Methodology_Analysis/`**: Chứa file Excel hoặc mã nguồn (Python/R) dùng để tính toán ma trận AHP và thuật toán phân hạng TOPSIS.
- **`05_Report_LaTeX/`**: Nơi lưu trữ source code LaTeX (`main.tex`, `references.bib`, thư mục `images/`) để render báo cáo cuối cùng.
- **`06_Presentation/`**: Chứa slides thuyết trình và kịch bản (script) bằng tiếng Anh.

## 3. Execution Strategy

### Phase 1: Criteria Development (Tuần 1-2)
- **Literature Review:** Liệt kê các tiêu chí phổ biến từ các bài báo khoa học về đánh giá thiết bị công nghệ.
- **Expert Interview:** Chuẩn bị 5 câu hỏi phỏng vấn 3 chuyên gia (IT/Office Workers) để lọc lại tiêu chí cho bối cảnh Việt Nam.
- **Survey:** Phát phiếu khảo sát Likert 5 điểm, phân tích mô tả để chốt danh sách tiêu chí cuối cùng (điểm trung bình > 3).

### Phase 2: Weighting with AHP (Tuần 3)
- Lập ma trận so sánh cặp (Pairwise Comparison Matrix) cho các tiêu chí đã chốt.
- Tính toán tỷ số nhất quán (CR - Consistency Ratio), đảm bảo CR < 0.1 để ma trận hợp lệ.

### Phase 3: Alternatives & TOPSIS Ranking (Tuần 4)
- **Data Collection:** Crawl/thu thập thủ công khoảng 50 alternatives từ CellphoneS.
- **Data Normalization:** Chuẩn hóa các tiêu chí (càng cao càng tốt vs càng thấp càng tốt).
- **TOPSIS Calculation:** Xác định giải pháp lý tưởng tích cực (A+) và tiêu cực (A-). Tính khoảng cách và độ tương tự để ra rank.

### Phase 4: Finalizing Deliverables (Tuần 5)
- **Report (LaTeX):** Sử dụng `professional_writing` skill để viết các chương (Introduction, Methodology, Results, Conclusion) bằng Academic English.
- **Presentation:** Thiết kế slides và viết script, tối ưu giọng điệu thuyết trình tự nhiên.

## 4. Rationale cho việc kết hợp AHP và TOPSIS
Trong phần lý luận bảo vệ phương pháp (defense): AHP xuất sắc trong việc đánh giá chủ quan của con người để tính trọng số (weights) một cách logic nhờ tỷ số CR. Tuy nhiên, nếu dùng AHP để so sánh 50 chiếc laptop thì số lượng ma trận so sánh cặp sẽ khổng lồ và bất khả thi. Do đó, việc dùng TOPSIS ở giai đoạn 3 là lựa chọn hoàn hảo vì TOPSIS xử lý dữ liệu định lượng, khách quan và nhiều alternatives rất nhanh và hiệu quả.
