# Kế hoạch cải thiện Chương 1 và Chương 2

## 1. Kết luận đánh giá

Hai chương hiện có cấu trúc tổng thể đúng hướng: Chương 1 đi từ bối cảnh đến vấn đề, khoảng trống, đóng góp, câu hỏi nghiên cứu và phạm vi; Chương 2 đi từ bản chất bài toán MCDM đến phân loại phương pháp, AHP, TOPSIS, nghiên cứu trước và định vị nghiên cứu. Mạch RQ1–RQ3 cũng khớp với ba giai đoạn criteria development–AHP–TOPSIS. Tuy nhiên, bản hiện tại chưa đủ chặt để xem là bản cuối vì một số claim về phạm vi và novelty không còn đúng sau khi Phase 5 chuyển nguồn dữ liệu sang Amazon.com, đồng thời gap về AHP–TOPSIS tự mâu thuẫn với chính tài liệu được tổng hợp trong Bảng 2.1.

Độ ưu tiên sửa được chia thành ba mức. Mức P0 là lỗi làm sai mô tả thiết kế nghiên cứu hoặc làm novelty không đứng vững. Mức P1 là lỗi về logic, evidence và sự lặp lại. Mức P2 là cải tiến trình bày và trực quan hóa.

## 2. Các sửa đổi P0 bắt buộc

### P0.1 — Đồng bộ Problem Statement với scope đã chốt

Chương 1 hiện khẳng định ngân sách văn phòng thường nằm trong khoảng 8–15 triệu đồng. Con số này không có citation và mâu thuẫn với scope dự án đã chốt là không khóa trước một mức giá. Đoạn này cần bỏ range 8–15 triệu và diễn đạt price như một cost criterion hoặc một eligibility rule tùy tình huống mua, nhất quán với dữ liệu thực tế có dải giá rộng trong Phase 5.

### P0.2 — Sửa mô tả nguồn dữ liệu thị trường

Các câu “real laptop data from the Vietnamese market” và “laptop models available on the market” gây hiểu rằng alternatives được lấy từ thị trường bán lẻ Việt Nam. Dataset thực tế gồm các model quốc tế chọn từ bảy review outlet và lấy giá/cấu hình tại Amazon.com ngày 12 July 2026. Chương 1 phải gọi đúng đây là một international recommendation set evaluated for a Vietnamese office-worker decision context, không phải Vietnamese market dataset.

### P0.3 — Viết lại research gap và novelty

Gap hiện nói các nghiên cứu laptop chủ yếu dừng ở weighting và AHP–TOPSIS được áp dụng chủ yếu cho mobile phone. Claim này không đứng vững vì Gaur (2023) đã dùng AHP+BWM+TOPSIS để rank laptop, còn review trong Sönmez Çakır và Pekkaya (2020) liệt kê các mô hình laptop FAHP–TOPSIS và nhiều hybrid ranking khác. Gap nên chuyển từ novelty phương pháp sang novelty về thiết kế nghiên cứu và bối cảnh: literature synthesis → five expert interviews → survey screening of 84 office-worker responses → AHP weighting → TOPSIS on a date-stamped candidate set. Đóng góp nên nhấn vào traceability, contextual calibration và sự tách biệt giữa criterion salience, criterion weight và alternative performance.

### P0.4 — Đồng bộ số người cung cấp AHP judgement

Chương 1 dùng số nhiều “experts” khi mô tả pairwise comparison, trong khi Phase 4 chỉ có một representative expert. Cần sửa thành “a representative expert” và đưa group AHP vào limitation/future work, tránh tạo ấn tượng có nhiều ma trận đã được geometric aggregation.

### P0.5 — Quyết định dứt điểm đối với Elnatan–Tannady

Entry này hiện không có năm trong BibTeX và lịch sử dự án từng ghi đã loại vì chưa được xuất bản chính thức, nhưng full-text folder, citation và Bảng 2.1 vẫn còn. Trước khi hoàn thiện Ch2 cần audit provenance. Nếu không xác minh được venue, year và peer-review status, loại khỏi prose, Bảng 2.1 và bibliography; không dùng nó làm bằng chứng cho gap.

## 3. Các sửa đổi P1 về lập luận và evidence

### P1.1 — Làm mới Background and Motivation

Phần mở đầu đang dựa nặng vào shipment 2017 và cú tăng 2020–2021. Các số này có thể dùng để giải thích lịch sử nhưng không đủ làm bối cảnh hiện tại năm 2026. Nên rút gọn pandemic statistics còn một câu hoặc thay bằng dữ liệu PC shipment gần thời điểm nghiên cứu từ Gartner/IDC, sau đó chuyển nhanh sang bản chất recurring, high-variety and multi-attribute của quyết định mua laptop. Mục tiêu là tránh để Ch1 giống một paper viết trong giai đoạn COVID-19.

### P1.2 — Tách rõ research problem, empirical context và methodological response

Problem Statement đang trộn ba lớp: budget constraint, local interview result và research gap. Nên tổ chức lại thành ba đoạn. Đoạn một mô tả decision problem của office worker. Đoạn hai giải thích vì sao international criteria không tự động transfer sang bối cảnh Việt Nam. Đoạn ba dẫn sang nhu cầu của một staged MCDM design. Kết quả phỏng vấn cụ thể như pin 4–7 giờ và motorbike commuting chỉ nên được preview có hedging, không trình bày như kết luận đã biết trước khi methodology/results xuất hiện.

### P1.3 — Giảm lặp giữa Chương 1 và §2.6

Gap và contribution đang được phát biểu gần như hai lần ở Ch1, rồi lặp lại lần thứ ba ở cuối Ch2. Ch1 nên nêu gap ngắn và contribution ở cấp strategic; §2.6 phải là synthesis có evidence, chỉ rõ từng stream đã làm gì, còn thiếu gì, và nghiên cứu này định vị ở giao điểm nào. Không lặp nguyên câu “AHP for weighting and TOPSIS for ranking”.

### P1.4 — Không phổ quát hóa taxonomy theo một review chuyên ngành

Phân loại năm nhóm của Villalba et al. (2024) được xây trong building assessment. Có thể dùng làm organizing lens, nhưng cần ghi rõ đó là taxonomy adopted from a domain review, sau đó triangulate với một general MCDM review như Basílio et al. (2022) hoặc một state-of-the-art review khác. Câu hiện tại khiến taxonomy này có vẻ là phân loại duy nhất được toàn ngành chấp nhận.

### P1.5 — Bổ sung giới hạn phương pháp trong §2.3–§2.4

AHP section đã nêu rank reversal và independence nhưng chưa nối những giới hạn đó với thiết kế hiện tại. TOPSIS section thiên về ưu điểm và thiếu phần phê bình. Nên bổ sung một đoạn cân bằng về sensitivity to normalization and weights, compensatory behavior, rank reversal/alternative-set dependence và việc ideal solution là điểm tham chiếu được dựng từ sample. Sau đó giải thích các lựa chọn kiểm soát: cố định candidate set/date, dùng một normalization rule nhất quán, công bố decision matrix và đọc top-three như short list thay vì tuyệt đối hóa hạng 1.

### P1.6 — Sửa lý do chọn crisp AHP/TOPSIS

Việc chuyên gia có kinh nghiệm trực tiếp không tự động chứng minh judgement là crisp hoặc không có uncertainty. Lý do phù hợp hơn là study design đã yêu cầu Saaty-scale judgements cụ thể, dữ liệu performance là số quan sát được, quy mô bài tập không biện minh cho fuzzy layer, và crisp model giúp audit/reproduce dễ hơn. Đây là trade-off về parsimony và transparency, không phải khẳng định uncertainty không tồn tại.

### P1.7 — Tăng chất lượng evidence hierarchy

Các nguồn phương pháp mạnh hiện có gồm Saaty (foundational AHP), Hwang–Yoon (foundational TOPSIS), Behzadian et al. và Zyoud–Fuchs-Hanusch trong Expert Systems with Applications, cùng Liu et al. về fuzzy AHP. Các paper ứng dụng laptop nên được dùng để mô tả empirical precedent, không dùng thay cho nguồn phương pháp nền. Khi nói “widely used”, “most common” hoặc nêu ưu/nhược điểm, ưu tiên systematic review/state-of-the-art paper; khi nói criterion hoặc ranking cụ thể, dùng primary application study.

### P1.8 — Nâng Bảng 2.1 từ inventory thành synthesis table

Bảng 2.1 đã được sửa để Source gọi `\textcite{}` thật. Ở lượt viết lại tiếp theo nên thay hoặc bổ sung cột Context/sample, Weighting method, Ranking method và Key limitation. Cột Criteria chỉ giữ nhóm tiêu chí chính. Thiết kế này giúp bảng trực tiếp chứng minh gap thay vì chỉ liệt kê tên paper.

## 4. Đề xuất visual và bảng bổ sung

### Đề xuất ưu tiên cao

**Table 1.1 — Alignment of research questions and analytical stages.** Bảng gồm RQ, evidence/input, analytical method, output và chapter reporting the result. Bảng này làm rõ RQ1 dùng literature–interview–survey, RQ2 dùng một AHP matrix, RQ3 dùng TOPSIS và candidate snapshot. Nó cũng ngăn người đọc hiểu nhầm expert interview với AHP elicitation.

**Figure 2.1 — MCDM method taxonomy and the role of the selected hybrid.** Một sơ đồ cây nhỏ gồm scoring, distance-based, pairwise comparison, outranking, utility/value; highlight AHP ở pairwise và TOPSIS ở distance-based, nối bằng mũi tên weights → ranking. Hình này trực quan hóa lý do hai phương pháp bổ sung nhau mà không lặp Figure 3.1 về research process.

**Table 2.1 revised — Evidence synthesis of laptop/electronics studies.** Mỗi dòng phải cho thấy product/context, sample or data source, criteria elicitation, weighting, ranking và limitation relevant to the current study. Dùng ký hiệu “criteria weighting only”, “ranks alternatives”, “context calibrated”, “real/date-stamped data” để gap có thể đọc trực tiếp từ bảng.

### Đề xuất ưu tiên vừa

**Figure 2.2 — Criteria evidence heatmap.** Trục dọc là 14 candidate criteria, trục ngang là các nghiên cứu laptop/electronics quan trọng; ô đánh dấu criterion xuất hiện trong paper nào. Hình cho thấy price/CPU/RAM/brand được hỗ trợ rộng, trong khi software compatibility hoặc after-sales có evidence thưa hơn và cần expert validation. Chỉ nên thêm nếu dữ liệu mapping được tái lập từ Appendix A.

**Table 2.2 — Method-selection rationale.** So sánh AHP, BWM, entropy, TOPSIS, VIKOR và PROMETHEE theo input, output, strengths, limitations và role in this study. Bảng không nhằm chứng minh AHP–TOPSIS “tốt nhất”, mà giải thích vì sao nó phù hợp với dữ liệu và mục tiêu hiện tại.

### Không khuyến nghị

Không nên thêm một flowchart literature→interview→survey→AHP→TOPSIS trong Ch1 hoặc Ch2 vì Figure 3.1 đã làm đúng chức năng này. Lặp lại sẽ tăng số trang nhưng không tăng thông tin. Không nên thêm biểu đồ shipment lịch sử nếu không có chuỗi dữ liệu cập nhật và trực tiếp phục vụ research problem.

## 5. Trình tự triển khai sau khi được duyệt

1. Chốt provenance của Elnatan–Tannady và quyết định giữ/loại.
2. Viết lại §1.1–§1.3 để sửa scope, data source, gap và contribution; đồng bộ singular expert.
3. Rút gọn §1.4–§1.5 và thêm Table 1.1 RQ–stage alignment.
4. Chỉnh §2.2 taxonomy với qualifier và general-review triangulation.
5. Viết lại §2.3–§2.4 theo cấu trúc principle → strength → limitation → design response.
6. Dựng lại Table 2.1 thành evidence-synthesis table và viết lại §2.5 theo agreements/disagreements thay vì tuần tự từng paper.
7. Viết lại §2.6 thành gap synthesis không trùng Ch1.
8. Chỉ sau khi prose ổn định mới dựng Figure 2.1; cân nhắc Figure 2.2/Table 2.2 theo giới hạn trang.
9. Chạy citation cross-reference, compile XeLaTeX–biber, render Ch1–2 và kiểm tra List of Tables/Figures.

## 6. Tiêu chí hoàn thành

Chương 1–2 đạt khi mọi claim về novelty đều được chứng minh bởi review, không còn mô tả Amazon dataset như dữ liệu thị trường Việt Nam, không còn budget range không nguồn, singular/plural expert khớp Phase 4, Bảng 2.1 trực tiếp hỗ trợ gap, ưu và nhược điểm AHP/TOPSIS được trình bày cân bằng, citation đều truy được đến BibTeX/full text, và visual mới không trùng chức năng với Figure 3.1.
