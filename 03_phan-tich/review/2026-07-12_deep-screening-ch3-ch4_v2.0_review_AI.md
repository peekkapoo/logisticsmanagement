# Deep-screening Chương 3–4 (lượt 2) — văn phong, luận điểm, flow, đề xuất visual

> Bản v1.0 (cùng thư mục) là review từ TRƯỚC đợt sửa lớn hôm nay (kiến trúc AHP 2 tầng,
> 4 lỗi số liệu Ch4, overclaim geometric-mean/sensitivity, thuật ngữ Delphi/pilot/end-user).
> Toàn bộ mục P0/P1 liên quan trong v1.0 đã được giải quyết trong các lượt sửa trước đó
> hôm nay. Bản v2.0 này không lặp lại, chỉ tập trung vào phát hiện MỚI từ một lượt đọc phản
> biện toàn văn: một rủi ro cấu trúc LaTeX cụ thể, và đánh giá văn phong/luận điện/flow.

## 1. Đánh giá tổng quan

Ch3–4 hiện là hai chương có chất lượng lập luận tốt nhất trong toàn báo cáo, một phần vì
chúng vừa trải qua nhiều vòng sửa số liệu và kiến trúc trong phiên hôm nay. Không phát hiện
overclaim, không còn dấu hai chấm liệt kê trong prose (đã rà lại bằng grep, chỉ còn trong
comment code), không còn thuật ngữ sai. Phát hiện đáng chú ý nhất của lượt này KHÔNG phải
lỗi văn phong mà là một **rủi ro cấu trúc LaTeX** đã từng gây lỗi thật trong phiên hôm nay
và có khả năng tái diễn ở một vị trí khác chưa được kiểm tra.

## 2. Phát hiện quan trọng nhất: Table 4.6 / Figure 4.3 vẫn dùng `[htbp]`

Sáng nay đã sửa lỗi khoảng trắng lớn giữa Table 4.3 và Figure 4.2 bằng cách đổi
`[htbp]` → `[H]` cho cả hai, vì nguyên nhân là hai float đặt liên tiếp không có văn xuôi
xen giữa khiến LaTeX đẩy chúng thành "trang float" riêng. Đọc lại `chapters/04-results.tex`
phát hiện **đúng pattern tương tự** ở một cặp float khác chưa được kiểm tra: `\input{tables/
topsis-ranking}` (Table 4.6, dòng 240) và ngay sau đó là `\begin{figure}[htbp]` (Figure 4.3,
dòng 242) — không có câu văn nào xen giữa hai float này, giống hệt cấu trúc đã gây lỗi.

Đã kiểm tra trực tiếp bản PDF hiện tại (`pdftoppm` trang vật lý 37): may mắn hiện tại Table
4.6 và Figure 4.3 vẫn nằm gọn cùng một trang, không có khoảng trắng bất thường — nghĩa là
bug **chưa xảy ra**, nhưng cấu trúc vẫn dễ vỡ (fragile): bất kỳ chỉnh sửa nhỏ nào ở văn bản
phía trên (thêm/bớt vài dòng) cũng có thể đẩy cặp float này sang trang riêng và tái tạo
đúng lỗi đã sửa sáng nay. Khuyến nghị (ưu tiên trung bình, phòng ngừa chứ không khẩn cấp):
đổi Figure 4.3 (dòng 242) từ `[htbp]` sang `[H]` để nhất quán với Table 4.3/Figure 4.2 đã
sửa, tránh phải quay lại xử lý sự cố tương tự sau này. Không cần sửa ngay nếu không có kế
hoạch chỉnh sửa văn bản Ch4 sắp tới, nhưng nên sửa trước khi coi Ch4 là bản final.

## 3. Chương 3 — Methodology

### 3.1 Luận điểm — đã phát triển tốt, không cần sửa

Các đoạn giải thích lý do kỹ thuật (vì sao chọn eigenvector thay vì column-average ở Step
4, vì sao chọn Gartner thay vì IDC, vì sao watt-hour thay vì giờ sử dụng) đều có cơ chế cụ
thể + citation hỗ trợ, đúng chuẩn "bung luận điểm" mà chuẩn academic writing yêu cầu. Đây
là phần lập luận chặt nhất trong toàn báo cáo — không có khuyến nghị sửa nội dung.

### 3.2 Một câu quá dài (không phải lỗi văn phong nghiêm trọng, chỉ là ghi chú đọc)

Đoạn mô tả cấu trúc 5 phần của phỏng vấn (dòng 105–119, "warm-up section... stimulus-based
section... open section... trade-off scenario... closing section...") là một câu duy nhất
khoảng 200 từ nối bằng dấu chấm phẩy. Khác với đoạn liệt kê 5 nhóm MCDM ở Ch2 (đã bị flag
nặng ở review Ch1-2), câu này không lặp khuôn mẫu máy móc — mỗi mệnh đề có cấu trúc và nội
dung giải thích riêng, nên không bị coi là "văn AI". Tuy nhiên độ dài có thể gây khó đọc.
Có thể cân nhắc tách thành 2 câu (ví dụ ngắt sau "an abstract opinion;") nếu muốn tăng khả
năng đọc, nhưng đây là tuỳ chọn văn phong, không phải lỗi.

### 3.3 Flow

Mạch §3.1 (proposed model) → Stage 1 → Stage 2 → Stage 3 rất rõ ràng, mỗi stage đóng đúng
vai trò trả lời 1 RQ, không nhảy cóc. Đây là chương có flow tốt nhất trong 6 chương.

### 3.4 Figure/Table cho Chương 3

Ch3 hiện có 1 figure (framework) + 4 bảng (Saaty scale, RI, review outlets,
operationalisation) — mật độ minh hoạ đã khá đầy đủ cho một chương Methodology. Không đề
xuất thêm bắt buộc. Một ý tưởng tuỳ chọn, ưu tiên thấp: có thể vẽ một sơ đồ nhỏ minh hoạ
5-phần phỏng vấn ở mục 3.2 để giảm tải cho câu văn dài nêu ở mục 3.2, nhưng xét báo cáo đã
có khá nhiều diagram dạng box-arrow (framework, criteria-transition), thêm một cái nữa có
nguy cơ gây trùng lặp phong cách hình ảnh mà không tăng nhiều giá trị thông tin — khuyến
nghị **không làm** trừ khi user thấy đoạn văn dòng 105–119 thực sự khó theo dõi khi đọc.

## 4. Chương 4 — Results

### 4.1 Luận điểm và số liệu — đã chính xác sau đợt sửa sáng nay

Đối chiếu lại một lần nữa các con số đã sửa (nearly ninefold, RAM 8GB/16GB, CPU rank thứ 4,
Brand đồng hạng 26.5) với `tables/decision-matrix.tex` và `appendices/E-laptop-data.tex`:
khớp hoàn toàn, không phát hiện sai lệch mới. Các đoạn diễn giải pattern/magnitude trong
§4.5 (TOPSIS Ranking Results) giữ đúng phạm vi mô tả dữ liệu, không lấn sang giải thích
nguyên nhân sâu (phần đó đã đúng chỗ ở Ch5).

### 4.2 Flow

Mạch §4.1 → §4.2 → §4.3 → §4.4 → §4.5 phản chiếu đúng 1-1 với Ch3 (đúng nguyên tắc đã ghi
trong comment đầu file), không lặp lại nội dung giữa các mục con.

### 4.3 Figure/Table cho Chương 4

Ch4 hiện đã rất giàu minh hoạ: 3 figure (criteria-transition, ahp-weights bar chart,
topsis-coefficients dot plot) + 6 bảng (criteria, survey-results, ahp-weights,
candidate-ids, decision-matrix, topsis-ranking). Đây là chương có mật độ visual cao nhất
báo cáo. Không đề xuất thêm bảng/hình mới — thêm nữa có nguy cơ làm chương quá tải hình ảnh
so với dung lượng nội dung, đặc biệt vì Figure 4.3 (dot plot) và Table 4.6 (cùng dữ liệu
ranking) đã hơi trùng thông tin với nhau (bảng có số chính xác, hình có so sánh trực quan
khoảng cách) — đây là sự trùng lặp CÓ CHỦ ĐÍCH và hợp lý (bảng để tra cứu, hình để cảm nhận
khoảng cách giữa các closeness coefficient), không phải lỗi, chỉ ghi chú lại để không ai
đề xuất bỏ một trong hai một cách vô tình.

## 5. Tóm tắt việc cần làm (nếu user duyệt sửa)

1. **Ưu tiên trung bình:** đổi Figure 4.3 (`chapters/04-results.tex` dòng 242) từ `[htbp]`
   sang `[H]` để phòng ngừa tái diễn lỗi khoảng trắng đã sửa sáng nay cho Table 4.3/Figure
   4.2 — hiện tại chưa lỗi nhưng cấu trúc dễ vỡ.
2. **Tuỳ chọn, không bắt buộc:** tách câu dài ~200 từ ở Ch3 dòng 105–119 (mô tả 5 phần
   phỏng vấn) thành 2 câu nếu muốn tăng khả năng đọc.
3. Không cần thêm figure/table nào cho Ch3–4 — mật độ minh hoạ đã đủ, thậm chí đã cao.

Mục 1 là mục duy nhất có giá trị sửa thực sự (rủi ro cấu trúc); mục 2 hoàn toàn tuỳ chọn.
