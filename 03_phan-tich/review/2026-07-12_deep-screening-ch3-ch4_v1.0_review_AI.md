# Deep screening Chapters 3–4

## 1. Kết luận điều hành

Hai chương đã có khung phương pháp tương đối đầy đủ, công thức AHP–TOPSIS đúng hướng, các trọng số và thứ hạng khớp với các tệp phân tích. Tuy nhiên, bản hiện tại chưa nên xem là sẵn sàng nộp vì còn bốn nhóm vấn đề trọng yếu: chuỗi hình thành tiêu chí chưa nhất quán; một số tuyên bố phương pháp vượt quá bằng chứng thực tế; dữ liệu alternatives thiếu dấu vết nguồn ở cấp từng model; và phần diễn giải kết quả có nhiều câu sai trực tiếp so với ma trận quyết định.

Đánh giá tổng quát: Chapter 3 mạnh về mô tả thuật toán nhưng yếu ở sampling, construct operationalisation và reproducibility; Chapter 4 có đủ kết quả chính nhưng chưa tách sạch result khỏi discussion và còn các lỗi kiểm tra chéo số liệu.

## 2. Phát hiện P0 — phải sửa trước khi nộp

### 2.1 Chuỗi tiêu chí trước và sau phỏng vấn tự mâu thuẫn

Chapter 4 nói literature synthesis tạo 14 tiêu chí, sau đó phỏng vấn loại GPU và thêm Software compatibility. Tuy nhiên Table 4.1 được giới thiệu là 14 tiêu chí ban đầu nhưng đã chứa Software compatibility và không còn GPU. Bảng đang trình bày bộ tiêu chí hậu phỏng vấn dưới nhãn tiền phỏng vấn. Cần tách rõ: (i) initial literature-derived set có GPU; (ii) expert-revised set có Software compatibility thay GPU; (iii) seven survey-retained criteria.

Quy tắc phương pháp còn nói chỉ thay đổi khi được đa số năm chuyên gia xác nhận. GPU đạt điều kiện này, nhưng phần kết quả chỉ quy việc thêm Software compatibility cho CG01 và CG03, tức 2/5. Cần kiểm lại coding matrix: nếu chỉ có hai chuyên gia thì không thể tuyên bố áp dụng majority rule; hoặc phải sửa quy tắc, hoặc bổ sung bằng chứng từ ít nhất chuyên gia thứ ba.

### 2.2 Mô hình AHP được mô tả sai cấu trúc

Chapter 3 nói pairwise comparisons được cấu trúc theo thematic groups và mô hình có ba tầng goal–criteria–alternatives. Dữ liệu thực tế chỉ có một ma trận phẳng 7×7 giữa các tiêu chí; alternatives không được so sánh bằng AHP mà được đánh giá trong TOPSIS. Cách mô tả đúng là two-level AHP weighting model (goal → criteria), nối với TOPSIS alternative ranking. Figure 3.1 cũng đang gắn nhãn sai luồng: đầu vào AHP không phải “weights”, và đầu ra AHP sang TOPSIS không phải “ranking”.

### 2.3 Operationalisation có hai lệch construct nghiêm trọng

“Battery life” được đo bằng battery capacity (Wh). Wh không đồng nghĩa runtime vì mức tiêu thụ điện, màn hình, CPU và tối ưu hệ điều hành khác nhau. Phải đổi tên tiêu chí vận hành thành Battery capacity, hoặc thay dữ liệu bằng runtime từ một protocol thử nghiệm thống nhất; nếu giữ Wh cần nêu đây là proxy và phân tích hạn chế.

“Brand/trust and after-sales” được đo bằng Gartner worldwide PC shipment share. Market share phản ánh market presence, không trực tiếp đo độ tin cậy, chất lượng hay dịch vụ hậu mãi tại Việt Nam. Nên đổi nhãn thành Market presence, hoặc dùng proxy sát construct hơn; nếu giữ, cần giải thích giới hạn và chạy sensitivity khi bỏ/thay proxy.

### 2.4 Dữ liệu alternatives chưa tái lập được

Chương 3 tuyên bố lấy hợp của danh sách từ bảy review outlets, deduplicate và thu dữ liệu Amazon, nhưng các tệp hiện có không lưu outlet URL, review URL, Amazon URL/ASIN, cấu hình khớp, access date theo từng model, pool trước loại trùng hay lý do loại. Vì vậy con số 12 alternatives và các giá trị đầu vào chưa audit được từ nguồn gốc.

Cần bổ sung một provenance dataset/table với tối thiểu: candidate ID, exact model/configuration, recommending outlet(s), review URL, Amazon URL/ASIN, PassMark CPU URL/version, data-access date, inclusion/exclusion decision. Table 3.3 hiện chỉ mô tả outlet ở mức tổng quát và các nhận định về Engadget/CNET cũng phải có citation hoặc được lược bỏ.

### 2.5 Các câu diễn giải sai số liệu trong Chapter 4

- Khoảng giá 395–3,499 USD là gần chín lần, chưa đạt “an order of magnitude”.
- Câu mọi máy trừ Acer có 32 GB hoặc Apple 24 GB là sai vì ThinkPad T14 Gen 6 AMD có 16 GB.
- ThinkPad X1 Carbon Gen 14 có CPU 20,946, là thứ tư chứ không phải thứ hai; hai mức cao nhất là Dell 30,684 và MacBook Air M5 26,831.
- Mẫu đứng đầu không phải “không dẫn đầu tiêu chí nào”: nó đồng hạng mức Brand cao nhất 26.5. Có thể viết rằng máy không độc chiếm vị trí dẫn đầu ở các tiêu chí chi phối.

Các lỗi này cần sửa bằng đối chiếu tự động với decision matrix, không sửa theo trí nhớ.

## 3. Phát hiện P1 — ảnh hưởng độ chặt chẽ học thuật

### Chapter 3

1. Không nên gọi khảo sát 84 người là “large-scale” hoặc khẳng định “actual office workers”, vì questionnaire không thu occupation/demographics để kiểm chứng persona. Cần mô tả đúng là convenience screening sample và bổ sung kênh tuyển mẫu, thời gian, eligibility, response handling và sample-size rationale.
2. Likert gồm một item cho mỗi tiêu chí khác loại; đây là item-level screening, không phải thang đo một latent construct. Ngưỡng mean ≥ 3.0 là decision rule thực dụng theo midpoint, không phải psychometric validation. Cần nói rõ phạm vi suy luận.
3. “Delphi-style first round” dễ gây hiểu nhầm vì không có nhiều vòng, controlled feedback hay consensus iteration. “Structured expert refinement” chính xác hơn.
4. Việc tuyên bố đã review và pilot interview protocol phải có artifact/bằng chứng; nếu pilot chưa diễn ra, sửa thành “informed by the IPR framework”.
5. “Representative expert” cho AHP cần nêu tiêu chí chọn và mã ẩn danh. Một người là designated decision-maker/expert, không đại diện thống kê cho panel.
6. “Filtered for local availability” mâu thuẫn với lý do chuyển sang Amazon vì model chưa có ở catalog Việt Nam. Phải xác định lại geography: international candidate set evaluated for a Vietnamese office-worker scenario.
7. Câu Amazon là nhà bán lẻ lớn nhất thế giới không giúp tái lập nghiên cứu và thiếu citation; nên thay bằng lý do chọn nguồn, snapshot date và giới hạn giá quốc tế.
8. Size/weight cuối cùng chỉ đo weight; cần gọi đúng operational criterion hoặc giải thích việc thu hẹp construct.
9. PassMark cần URL/version/access date và cảnh báo về so sánh Apple Silicon với x86. TOPSIS normalization không tự khắc phục khác biệt về tính hợp lệ của benchmark.
10. Script AHP thực sự có diagnostic ba cặp lệch nhất khi CR > 0.1, nên mô tả này có cơ sở; tuy nhiên cần dẫn rõ script/output reproducible.

### Chapter 4

1. Câu “professional and end-user perspectives” vượt bằng chứng vì survey không xác minh người trả lời là office workers; nên viết “expert panel and survey respondents”.
2. Việc cùng thứ tự giữa eigenvector và geometric mean chỉ chứng minh ordering ổn định giữa hai cách tính đã dùng, không chứng minh priority structure độc lập với derivation method.
3. Khoảng cách top three dưới 0.011 chỉ “gợi ý khả năng nhạy”; chưa đủ kết luận sensitive nếu chưa chạy sensitivity analysis.
4. Nhiều đoạn giải thích vì sao model thắng/thua và so sánh với literature thuộc Chapter 5. Chapter 4 nên giữ mô tả pattern, magnitude và đối chiếu trực tiếp dữ liệu.
5. Candidate pool có sáu Lenovo trên 12 model; cần nêu selection composition và nguy cơ pool bias, nhất là khi Brand cũng được chấm bằng market share.
6. CR=0.0483 chỉ chứng minh internal consistency của judgments, không chứng minh weights có validity hay representativeness.
7. Appendix D trình bày column sums như normalisation constant nhưng sau đó dùng power iteration; hoặc dùng chúng trong một approximation rõ ràng, hoặc bỏ bước không tham gia phép tính chính.

## 4. Phát hiện P2 — trình bày và minh họa

1. Sửa Figure 3.1 thành pipeline có nhãn đúng: retained criteria → pairwise judgments → AHP weights → TOPSIS decision matrix → closeness scores/ranking. Nêu n=1 tại AHP và n=12 tại TOPSIS nếu muốn thể hiện quy mô.
2. Thêm một criteria-transition figure: literature set (14, có GPU) → expert revision (GPU out, Software compatibility in) → Likert screening (7 retained). Đây là visual có giá trị nhất vì giải quyết trực tiếp logic đang khó theo dõi.
3. Thêm horizontal bar chart cho bảy AHP weights, có data labels; tránh pie chart vì khó so sánh Price 0.3491 và CPU 0.2769.
4. Thêm lollipop/dot plot cho 12 TOPSIS closeness coefficients, sắp giảm dần và đánh dấu khoảng cách top three.
5. Chỉ thêm sensitivity figure sau khi thực sự chạy phân tích; ưu tiên heatmap/rank-stability plot thay vì hình minh họa trang trí.
6. Thêm operationalisation table: theoretical criterion, measured variable, unit, benefit/cost, source, access date, proxy limitation. Bảng này quan trọng hơn việc thêm prose.
7. Đưa provenance table dài sang appendix; trong Chapter 3 chỉ giữ flow tuyển alternatives và số lượng ở mỗi bước.

## 5. Plan triển khai đề xuất

### P0 — khóa logic và số liệu

1. Dựng traceability matrix cho 14 tiêu chí ban đầu, coding của 5 chuyên gia, 14 tiêu chí hậu phỏng vấn và 7 tiêu chí hậu khảo sát.
2. Quyết định xử lý Software compatibility: chứng minh đủ majority, hoặc sửa decision rule và diễn giải kết quả.
3. Viết lại mô tả AHP thành goal–criteria weighting rồi TOPSIS ranking; sửa Figure 3.1.
4. Chốt lại hai proxy Battery và Brand trước khi viết prose; nếu giữ proxy, đổi nhãn/qualifier và thêm limitation.
5. Tạo candidate provenance dataset, đối chiếu toàn bộ 12 model và từng cấu hình.
6. Chạy kiểm tra tự động các statement định lượng của Chapter 4 từ decision matrix và TOPSIS output; sửa bốn lỗi số liệu đã nêu.

### P1 — tăng độ tin cậy phương pháp

7. Viết lại sampling/survey section theo đúng evidence có thật; bỏ large-scale/verified office-worker claims.
8. Đổi Delphi-style thành structured expert refinement; kiểm tra bằng chứng pilot/IPR.
9. Nêu rõ selection rationale của AHP expert và giới hạn single-expert elicitation.
10. Chuẩn hóa source/access date cho outlets, Amazon, PassMark và Gartner; đồng bộ appendix.
11. Chạy sensitivity analysis có kịch bản minh bạch: perturb AHP weights, bỏ Brand proxy, và kiểm tra rank stability của top three.

### P2 — biên tập và visual QA

12. Tách Results khỏi Discussion; giữ Chapter 4 thiên về observed results và chuyển mechanism/comparison sang Chapter 5.
13. Bổ sung criteria-transition figure, AHP weight chart và TOPSIS ranking plot.
14. Compile XeLaTeX–biber đầy đủ, kiểm tra 0 undefined/error; render riêng toàn bộ trang chứa Figure 3.1, Table 4.1 và các visual mới.

## 6. Thứ tự quyết định cần người dùng duyệt trước khi viết lại

Điểm cần chốt đầu tiên là cách xử lý hai proxy. Khuyến nghị học thuật: đổi Battery life thành Battery capacity nếu không có runtime test thống nhất; đổi Brand thành Market presence nếu tiếp tục dùng Gartner share. Sau đó mới sửa prose, vì giữ nhãn cũ sẽ tiếp tục tạo construct mismatch xuyên Chapter 3–5.

Tệp này là biên bản screening; chưa sửa nội dung Chapter 3 hoặc Chapter 4 và chưa thay đổi dữ liệu nghiên cứu.
