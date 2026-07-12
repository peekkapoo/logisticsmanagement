# Deep-screening Chương 1–2 (lượt 2) — văn phong, luận điểm, flow, đề xuất visual

> Bản v1.0 (cùng thư mục) là review từ TRƯỚC đợt viết lại lớn Ch1–2 trong phiên hôm nay
> (bỏ budget range 8–15 triệu, sửa singular expert, sửa Amazon-as-VN-market, gỡ Elnatan,
> thêm qualifier cho taxonomy Villalba, restructure Table 2.1). Hầu hết P0/P1 của v1.0
> **đã được giải quyết** — bản v2.0 này không lặp lại các mục đó, chỉ ghi chú mục nào của
> v1.0 nay đã lỗi thời/mâu thuẫn với quyết định mới, rồi tập trung vào review MỚI: giọng
> văn, phát triển luận điểm, flow, và figure/table.

## 1. Đánh giá tổng quan

Giọng văn Ch1–2 nhìn chung đã ở mức tốt — không còn gạch đầu dòng, không còn tính từ đao
to búa lớn, citation phần lớn tích hợp làm chủ thể câu đúng chuẩn ("Sönmez Çakır và
Pekkaya (2020) frame this directly..."). Vấn đề còn lại không nằm ở từ vựng cường điệu mà
ở ba chỗ cụ thể: (a) Ch1 vẫn còn 3 câu dùng dấu hai chấm kiểu liệt kê — đợt rà soát dấu
hai chấm trong phiên hôm nay chỉ chạy trên Ch2–4, bỏ sót Ch1; (b) hai luận điểm trong §1.1
bị nêu suông, không "bung" cơ chế đằng sau (đúng loại lỗi mà chuẩn mực academic writing
gọi là thiếu elaboration); (c) đoạn liệt kê 5 nhóm phương pháp MCDM trong §2.2 lặp một
khuôn câu 5 lần liên tiếp, đọc như bullet list cải trang thành văn xuôi — đây là dấu hiệu
"văn AI" rõ nhất trong hai chương. Ngoài ra, Figure 2.1 hiện không khớp với đúng đoạn văn
mà nó minh hoạ (xem mục 4).

## 2. Chương 1 — Introduction

### 2.1 Dấu hai chấm còn sót (chưa qua đợt rà soát hôm nay)

Ba câu sau vẫn dùng dấu hai chấm để mở đầu phần liệt kê/diễn giải, cùng lỗi đã sửa hệ
thống ở Ch2–4:

- Dòng 7–8: "Historical shipment evidence illustrates the scale of this decision:
  \textcite{sonmez_cakir_determination_2020} reported 161.6 million laptop units sold in
  2017..." — nên tách câu hoặc dùng "\textit{as}"/"in that" thay dấu hai chấm.
- Dòng 17: "These attributes also create trade-offs: a lower price may restrict hardware
  capability, while greater battery capacity or structural durability may add weight." —
  xem thêm mục 2.2 vì câu này còn có vấn đề nội dung, không chỉ hình thức.
- Dòng 28: "AHP and TOPSIS perform different analytical roles: AHP derives a priority
  vector from pairwise judgements, whereas TOPSIS ranks alternatives..." — tách thành 2
  câu hoặc nối bằng "in which".

Đề xuất sửa (không tự áp dụng ở lượt review này): đổi cả ba theo đúng pattern đã dùng ở
Ch2–4 — thay dấu hai chấm bằng dấu chấm mở câu mới, hoặc liên từ phụ thuộc ("since",
"in which", "because").

### 2.2 Luận điểm nêu suông, chưa "bung" cơ chế

Hai chỗ trong §1.1 nêu claim đúng nhưng dừng lại ở mức khẳng định, không giải thích *tại
sao* — đúng loại lỗi mà Case 1/Case 2 trong chuẩn academic writing của skill này minh hoạ
(trade-off pin/trọng lượng, giá/cấu hình).

Câu ở dòng 17 ("a lower price may restrict hardware capability, while greater battery
capacity or structural durability may add weight") chỉ liệt kê hiện tượng, không chạm vào
cơ chế vật lý/kinh tế đứng sau. Vì sao giá thấp giới hạn cấu hình (biên lợi nhuận buộc nhà
sản xuất hạ cấp linh kiện) và vì sao dung lượng pin lớn hơn kéo theo trọng lượng (mật độ
năng lượng Wh/kg của pin lithium-ion là hằng số vật lý xấp xỉ, không phải lựa chọn thiết
kế tuỳ ý) đều là những cơ chế có thể nêu trong 1 câu bổ sung, giúp đoạn văn có chiều sâu kỹ
thuật thay vì chỉ là quan sát bề mặt. Câu hiện tại giống mô tả AI Case 2 "bản cũ" trong
SKILL.md (chỉ liệt kê trade-off mà không chỉ ra bản chất vật lý).

Câu ở dòng 47 ("Those priorities cannot be assumed to transfer unchanged to Vietnamese
working conditions") là một claim quan trọng — đây chính là luận điểm khung cho toàn bộ
thiết kế 3 giai đoạn của nghiên cứu — nhưng trong Ch1 nó chỉ được khẳng định, chưa gợi ý
lý do cụ thể nào (hạ tầng điện lưới, thói quen di chuyển bằng xe máy, v.v. chỉ xuất hiện
ở Ch4–5). Ch1 không cần tiết lộ hết kết quả, nhưng một mệnh đề ngắn kiểu "vì các thuộc
tính như thời lượng pin hay trọng lượng có thể mang ý nghĩa khác nhau tuỳ hạ tầng điện và
thói quen di chuyển tại nơi tiến hành khảo sát" sẽ neo được luận điểm vào một cơ chế cụ
thể thay vì để nó trôi nổi như một tuyên bố trừu tượng. Hiện tại câu này đọc hơi giống
hedge ngẫu nhiên hơn là một luận điểm có căn cứ trước khi bằng chứng xuất hiện.

### 2.3 Flow

Mạch §1.1 → §1.2 → §1.3 → §1.4 → §1.5 hợp lý, không nhảy cóc. Đoạn cuối §1.5 (roadmap 5
chương) là đoạn kết cấu chuẩn IMRaD, không phải lỗi văn phong dù có nhịp liệt kê — loại
đoạn này chấp nhận được vì chức năng của nó là điều hướng, không phải lập luận.

### 2.4 Figure/Table cho Chương 1

Không đề xuất thêm figure/table cho Ch1. Phần lớn Introduction ở các báo cáo Q1 không có
visual riêng; nội dung Ch1 hiện là framing bằng văn xuôi, và mọi sơ đồ minh hoạ pipeline
nghiên cứu đã có chỗ hợp lý hơn ở Ch2 (Figure 2.1) và Ch3 (Figure 3.1). Thêm một sơ đồ ở
đây sẽ trùng chức năng mà không tăng thông tin — đúng khuyến nghị "Không khuyến nghị"
trong bản v1.0 vẫn còn giá trị.

## 3. Chương 2 — Literature Review

### 3.1 Đoạn liệt kê 5 nhóm phương pháp MCDM (§2.2, dòng 29–37) — lỗi văn phong rõ nhất

Đoạn này lặp một khuôn câu giống hệt nhau 5 lần liên tiếp:

> "Direct scoring methods, such as... aggregate weighted performance scores directly.
> Distance-based methods, principally..., rank alternatives by their geometric distance...
> Pairwise comparison methods, led by..., derive priorities from relative judgements...
> Outranking methods, such as..., build a preference relation... Utility and value methods,
> including..., construct explicit utility functions..."

Về nội dung, thông tin đúng và đủ. Vấn đề là nhịp điệu: mỗi câu đều theo cấu trúc [Tên
nhóm] + [ví dụ phương pháp], + [động từ hành động] — năm lần liên tục không có câu nào phá
nhịp bằng cách bắt đầu từ góc độ khác (ví dụ mở đầu bằng cơ chế thay vì tên nhóm, hoặc nối
hai nhóm bằng một câu so sánh trực tiếp). Đây chính là kiểu "liệt kê máy móc cải trang
thành văn xuôi" mà chuẩn academic writing của skill này yêu cầu tránh. Gợi ý hướng sửa
(không tự áp dụng): giữ nguyên nội dung nhưng phá nhịp bằng cách gộp 2 nhóm liền kề thành
một câu so sánh ("Trong khi các phương pháp direct-scoring... thì distance-based lại..."),
hoặc chuyển hẳn đoạn này thành một bảng nhỏ (xem đề xuất Table 2.0 ở mục 4) để tránh phải
gồng văn xuôi cho một nội dung vốn có cấu trúc liệt kê tự nhiên.

### 3.2 Câu kết đoạn dùng list-cadence (dòng 208–209)

"These differences are not measurement noise alone; they reflect different products,
populations, criteria definitions, and elicitation procedures." — câu này kết một đoạn
bằng cách liệt kê 4 danh từ nối tiếp, một nhịp điệu nhẹ nhàng hơn nhưng cùng họ với vấn đề
ở mục 3.1. Không nghiêm trọng, có thể giữ nguyên nếu không muốn sửa nhiều, nhưng nếu sửa
đoạn 3.1 thì nên tiện tay đa dạng hoá câu này luôn để tránh lặp motif "khẳng định + liệt kê
nguyên nhân bằng danh từ" hai lần trong cùng một chương.

### 3.3 Phát triển luận điểm — nhìn chung tốt

Khác với Ch1, các luận điểm chính ở Ch2 đều được "bung" đủ: mục AHP giải thích cơ chế rank
reversal cụ thể (dòng 103–107), mục TOPSIS giải thích rõ vì sao phương pháp compensatory
lại kéo theo rủi ro (dòng 152–160) kèm biện pháp kiểm soát cụ thể (fix candidate set, một
normalisation rule, công bố ma trận). Đây là phát triển luận điểm đúng chuẩn — không cần
sửa.

### 3.4 Flow §2.1 → §2.6

Mạch chương hợp lý: vấn đề MCDM → tổng quan phương pháp → AHP → TOPSIS → nghiên cứu trước
→ gap. Không phát hiện đoạn nào nhảy cóc ý hoặc lặp lại nguyên văn giữa các section.

## 4. Đề xuất Figure/Table cho Chương 2

### 4.1 Vấn đề hiện tại: Figure 2.1 không khớp với đoạn văn nó minh hoạ

Figure 2.1 (`fig:mcdm-taxonomy`, dòng 43–60) hiện chỉ vẽ 3 hộp AHP → TOPSIS → Decision
output — về bản chất đây là sơ đồ quy trình của CHÍNH nghiên cứu này, gần như trùng lặp
với Figure 3.1 ở Ch3 (vốn đầy đủ hơn: literature synthesis → screening → criteria → AHP →
weights → TOPSIS → ranking). Trong khi đó, đoạn văn ngay phía trên hình (dòng 27–41) lại
đang giải thích taxonomy 5 nhóm phương pháp MCDM (direct scoring, distance-based, pairwise
comparison, outranking, utility/value) — một nội dung hoàn toàn khác với hình. Người đọc
kỳ vọng hình minh hoạ 5 nhóm này (hoặc vị trí AHP/TOPSIS trong 5 nhóm đó), nhưng lại thấy
một sơ đồ pipeline 3 hộp. Đây là điểm bất nhất đáng sửa nhất trong 2 chương.

**Đề xuất (ưu tiên cao):** thay Figure 2.1 hiện tại bằng một trong hai phương án:

- (a) Một bảng nhỏ "Table 2.0 — Families of MCDM methods" với 3 cột (Family | Representative
  methods | Core mechanism), dựng trực tiếp từ nội dung đoạn văn dòng 29–37 (Direct
  scoring/Distance-based/Pairwise comparison/Outranking/Utility-value). Bảng này vừa giải
  quyết vấn đề liệt kê ở mục 3.1 (chuyển nội dung có cấu trúc liệt kê ra khỏi văn xuôi),
  vừa cho người đọc một điểm tra cứu nhanh, vừa không trùng Figure 3.1.
- (b) Nếu muốn giữ dạng hình, vẽ lại thành sơ đồ 5 nhánh (5 family) với AHP/TOPSIS được
  highlight ở đúng nhánh của chúng (pairwise comparison / distance-based), có mũi tên nối
  hai nhánh đó thể hiện lý do phối hợp — đây là chính đề xuất Figure 2.1 đã nêu ở bản v1.0
  (mục 4, "Đề xuất ưu tiên cao"), nay vẫn còn giá trị và CHƯA được triển khai.

Hình 3-hộp hiện tại của Ch2 nên di chuyển hoặc xoá, vì nội dung của nó (AHP→TOPSIS→ranking
cho chính nghiên cứu này) thuộc phạm vi Ch3, không phải phạm vi "tổng quan taxonomy MCDM"
của Ch2.

### 4.2 Table 2.1 — một điểm cần lưu ý (khác với đề xuất cũ ở v1.0)

Bản v1.0 từng đề xuất thêm cột "Key limitation" vào Table 2.1 (mục P1.8/Table 2.1 revised).
Đề xuất đó nay **mâu thuẫn với quyết định mới của user** trong phiên hôm nay — user đã yêu
cầu XÓA cột "Limitation relevant here" khỏi bảng này để bảng gọn hơn. Ghi chú lại ở đây để
tránh nhầm lẫn nếu ai đọc lại v1.0: không nên thêm lại cột limitation, quyết định hiện hành
(4 cột: Source, Context/data, Criteria input, Weighting/ranking) là bản chốt mới nhất.

### 4.3 Đề xuất tuỳ chọn (ưu tiên vừa, không bắt buộc)

**Table 2.2 — Method-selection rationale** (đã nêu ở v1.0, vẫn còn giá trị): so sánh AHP,
BWM, entropy, TOPSIS, VIKOR, PROMETHEE theo input/output/strength/limitation/role trong
nghiên cứu này. Chỉ nên làm nếu còn dư dung lượng trang — không phải sửa bắt buộc, vì §2.3–
§2.4 hiện tại đã giải thích khá đủ lý do chọn AHP+TOPSIS bằng văn xuôi.

Không khuyến nghị thêm Figure 2.2 (criteria evidence heatmap) đã nêu ở v1.0 — nội dung này
đòi hỏi mapping lại 14 candidate criteria với từng paper, tốn công đối chiếu mà lợi ích
trình bày không lớn hơn nhiều so với Table 2.1 hiện tại.

## 5. Tóm tắt việc cần làm (nếu user duyệt sửa)

1. Sửa 3 câu dùng dấu hai chấm còn sót ở Ch1 (mục 2.1).
2. Bổ sung 1 câu giải thích cơ chế cho đoạn trade-off giá/cấu hình và pin/trọng lượng ở Ch1
   dòng 17 (mục 2.2).
3. Neo luận điểm "priorities cannot transfer unchanged" ở Ch1 dòng 47 bằng một gợi ý cơ chế
   cụ thể, không cần tiết lộ hết kết quả (mục 2.2).
4. Phá nhịp đoạn liệt kê 5 nhóm MCDM ở Ch2 §2.2 (mục 3.1) — khuyến nghị chuyển thành bảng
   (mục 4.1a) thay vì chỉ viết lại câu.
5. Thay Figure 2.1 hiện tại (trùng Figure 3.1) bằng bảng hoặc sơ đồ taxonomy 5 nhóm đúng
   nội dung đoạn văn liền kề (mục 4.1).
6. Không thêm cột limitation vào Table 2.1 (đã chốt bỏ, mục 4.2 — chỉ để tránh nhầm với
   đề xuất cũ ở v1.0).

Không mục nào trong danh sách này ảnh hưởng tới số liệu AHP/TOPSIS hay cấu trúc chương —
toàn bộ là điều chỉnh văn phong/trình bày, có thể triển khai độc lập với các chương khác.
