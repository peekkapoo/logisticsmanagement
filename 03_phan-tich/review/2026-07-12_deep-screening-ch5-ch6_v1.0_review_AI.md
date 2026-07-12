# Deep-screening Chương 5–6 — văn phong, luận điểm, flow, đề xuất visual

> Đây là bản review ĐẦU TIÊN cho Ch5–6 (chưa có v1.0 cũ như Ch1-2/Ch3-4). Ch5–6 có qua
> sửa nhỏ trong phiên hôm nay (đồng bộ "leads no criterion" tự mâu thuẫn, đổi "expert and
> end-user perspectives" → "expert panel and survey respondents") nhưng CHƯA qua đợt rà soát
> dấu hai chấm/thuật ngữ toàn diện như Ch2–4. Lượt deep-screening này phát hiện đúng hai loại
> sót đó, cộng thêm đánh giá văn phong/luận điểm/flow độc lập.

## 1. Phát hiện ưu tiên CAO NHẤT: lỗi số liệu CPU bị lặp lại ở Ch5, sáng nay chỉ sửa ở Ch4

`chapters/05-discussion.tex` dòng 114–116 hiện viết:

> "At the other end, the ThinkPad X1 Carbon Gen 14 Aura Edition finishes last at \$3,499
> despite **the second-highest processor score** in the set, an outcome that echoes the
> over-specification argument of \textcite{rau_optimal_2018}..."

Đây là **đúng lỗi số liệu đã sửa ở Ch4 sáng nay** (PassMark thật của model này là 20,946,
xếp thứ **4/12**, không phải thứ 2 — hai mức cao nhất là Dell 30,684 và MacBook Air M5
26,831, theo `appendices/E-laptop-data.tex` bảng `tab:cpu-passmark`). Khi sửa Ch4 sáng nay,
tôi chỉ tìm-và-sửa cụm "second-highest processor score" trong `04-results.tex`, không kiểm
tra xem câu tương tự có bị lặp lại ở Ch5 hay không — và nó có. Đây là bằng chứng cụ thể cho
thấy các luận điểm diễn giải lại số liệu ở Ch5 (vốn thường paraphrase lại Ch4) cần được đối
chiếu lại toàn bộ với Ch4 sau bất kỳ đợt sửa số liệu nào ở đó.

**Đề xuất sửa (chưa tự áp dụng theo đúng chế độ review-only đã chọn):** đổi thành cùng cách
diễn đạt đã dùng ở Ch4 — "despite a mid-to-upper processor score (20,946, the fourth highest
in the set)" — để nhất quán số liệu và lập luận giữa hai chương. Lập luận "over-specification"
của đoạn này (trả giá cao cho năng lực vượt nhu cầu không tạo thêm giá trị) vẫn đứng vững
sau khi sửa số, không cần viết lại toàn đoạn.

## 2. Phát hiện thứ hai: "end users" còn sót lại một chỗ, không nhất quán với phần đã sửa

`chapters/05-discussion.tex` dòng 51 đã được sửa sáng nay thành "the expert panel and the
survey respondents", nhưng cùng đoạn văn đó, 6 dòng sau (dòng 57), vẫn còn:

> "The likely mechanism is that **end users** experience compatibility as a background
> condition rather than a choice variable..."

Đây là cùng loại overclaim đã bị flag và sửa ở đầu đoạn (khảo sát không xác minh occupation
người trả lời, nên gọi họ là "end users" đã xác nhận là quá đà) — nhưng sót lại ngay trong
cùng đoạn văn vì lượt sửa sáng nay chỉ target đúng cụm "expert and end-user perspectives",
không quét toàn bộ các lần xuất hiện riêng lẻ của "end user(s)" trong cả đoạn.

**Đề xuất sửa:** đổi "end users experience compatibility..." thành "survey respondents
experience compatibility..." hoặc "the wider respondent pool experiences compatibility...",
giữ nguyên phần còn lại của câu.

## 3. Dấu hai chấm — Ch5–6 CHƯA qua đợt rà soát sáng nay

Đợt rà soát dấu hai chấm sáng nay (chuyển câu liệt kê bằng dấu hai chấm thành câu liền mạch)
chỉ chạy trên Ch2–4 theo đúng phạm vi yêu cầu lúc đó của user. Ch5 hiện còn **15 dấu hai
chấm** trong văn xuôi, Ch6 còn **4 dấu hai chấm** — đây là tỷ lệ cao nhất trong 6 chương,
đúng cùng một mẫu hình đã sửa ở các chương khác (câu nêu luận điểm rồi dùng dấu hai chấm để
mở phần diễn giải/liệt kê thay vì câu mới hoặc liên từ phụ thuộc). Ví dụ tiêu biểu:

- Ch5 dòng 17: "The dominant position of price is consistent with the wider
  consumer-behaviour evidence: \textcite{liao_determinants_2022} find price..."
- Ch5 dòng 57–58: "...as a background condition rather than a choice variable: almost
  every machine they encounter in a Vietnamese office already runs Windows..."
- Ch5 dòng 79: "\textcite{maghsoudi_hybrid_2026} report the starkest contrast: in their
  sentiment-weighted ranking of sixteen notebook features..."
- Ch5 dòng 133: "...but the structure of the weights: roughly 63\% of the decision is a
  price--processor trade-off..."
- Ch5 dòng 149–150: "The screened-out criteria retain a role here as eligibility gates:
  software compatibility and after-sales coverage are best enforced as pass-or-fail..."
- Ch6 dòng 13: "...produced a set of seven evaluation criteria: price, processor
  capability, memory, solid-state storage, brand, physical size and weight, and battery
  life." (đây là liệt kê 7 mục thật — có thể giữ dấu hai chấm nếu muốn, đây là trường hợp
  liệt kê chính đáng, không bắt buộc sửa như các trường hợp khác).
- Ch6 dòng 73: "the market data are a snapshot: prices and configurations were collected
  from a single retail platform..."

Không liệt kê hết toàn bộ 19 vị trí ở đây để tránh review quá dài — nếu user duyệt sửa, nên
áp dụng đúng kỹ thuật đã dùng ở Ch2–4 (tách câu, hoặc thay bằng "since"/"in which"/"because"/
"where") cho từng trường hợp, trừ các chỗ liệt kê thật sự (như Ch6 dòng 13) có thể giữ
nguyên tuỳ lựa chọn văn phong.

## 4. Đánh giá luận điểm — Ch5 là chương lập luận tốt nhất báo cáo

Sau khi loại trừ hai lỗi ở mục 1–2, phần còn lại của Ch5 có chất lượng phát triển luận điểm
cao nhất trong 6 chương. Đoạn về nghịch lý pin (dòng 27–49) là ví dụ mẫu mực về "bung luận
điểm" đúng chuẩn: nêu contradiction (survey cao nhất nhưng AHP thấp nhất) → giải thích cơ chế
(hai công cụ đo hai thứ khác nhau: salience vs marginal decision value) → nối với bằng chứng
thực tế (hạ tầng điện lưới văn phòng, dải cân nặng máy hội tụ 1.3–1.6kg) → khái quát hoá
nguyên lý ("criteria whose requirements the market already meets lose weight..."). Đoạn về
Display granularity (dòng 66–89) cũng vậy — trích dẫn 3 nghiên cứu khác nhau decompose màn
hình theo cách khác nhau, rồi tự áp cơ chế đó để giải thích vì sao Display bị loại, đồng thời
tự giới hạn phạm vi suy luận ("offered as an interpretive caveat rather than a claim..."). Đây
chính xác là mức độ elaboration + hedging phù hợp mà chuẩn academic writing yêu cầu. Không có
khuyến nghị sửa nội dung lập luận ở đây, chỉ sửa hình thức (dấu hai chấm, số liệu).

Ch6 (Conclusion) đọc gọn, đúng vai trò tổng hợp, không đưa thông tin mới (đúng quy định ghi
trong comment đầu file), không phát hiện overclaim mới sau đợt sửa sáng nay.

## 5. Flow

Mạch §5.1 (weights) → §5.2 (ranking) → §5.3 (implications) → §5.4 (comparison) hợp lý, mỗi
mục nối tiếp mục trước bằng cross-reference cụ thể (`\Cref{sec:interp-weights}` được nhắc lại
đúng lúc ở §5.2 và §5.4), không lặp nguyên văn. Ch6 §6.1→6.2→6.3→6.4 theo đúng khuôn RQ→
contribution→limitation→future work chuẩn, không lấn sang nội dung mới.

## 6. Figure/Table cho Chương 5–6

Ch5–6 hiện hoàn toàn không có bảng/hình nào. Với Ch6 (Conclusion), điều này bình thường và
không cần bổ sung — Conclusion thường thuần văn xuôi tổng hợp, không nên giới thiệu bảng/hình
mới.

Với Ch5 §5.4 (Comparison with Prior Studies), có một khoảng trống đáng cân nhắc: đoạn văn
đang so sánh bằng lời trọng số/kết quả của nghiên cứu này với 5 nghiên cứu trước (Liao,
Šostar, Maghsoudi, Sönmez Çakır, Weng Siew Lam, Gaur) trên nhiều tiêu chí (price, brand,
battery, GPU, display, ranking outcome) — đây là đúng loại nội dung mà một bảng so sánh nhỏ
sẽ tóm tắt cho người đọc thay vì phải tự ghép nối qua 4 đoạn văn dài. Đề xuất (ưu tiên trung
bình, tuỳ chọn): thêm một bảng "Table 5.1 — Priority structure compared with prior studies"
gồm cột Criterion/dimension | This study | Prior study & context | Agreement or divergence,
với các dòng Price (agree, đối chiếu Liao/Šostar/Maghsoudi), Brand (diverge, đối chiếu
Sönmez Çakır), Battery life (diverge, đối chiếu Weng Siew Lam), GPU removal (agree, đối chiếu
Maghsoudi), Display (diverge, đối chiếu 3 nguồn ở §5.1). Bảng này không thay thế phần diễn
giải cơ chế bằng văn xuôi (vẫn cần giữ nguyên phần "tại sao" hiện có), chỉ bổ sung một điểm
tra cứu nhanh — hữu ích nhưng không bắt buộc.

## 7. Tóm tắt việc cần làm (nếu user duyệt sửa)

1. **Ưu tiên cao nhất:** sửa lại số liệu CPU sai ở Ch5 dòng 114–116 (second-highest → fourth
   highest, 20,946), đồng bộ với Ch4 đã sửa sáng nay.
2. **Ưu tiên cao:** sửa "end users" còn sót ở Ch5 dòng 57 thành "survey respondents" hoặc
   "the wider respondent pool", đồng bộ với phần đã sửa cùng đoạn.
3. **Ưu tiên trung bình:** rà soát và sửa 15 dấu hai chấm ở Ch5 + 4 dấu hai chấm ở Ch6 (trừ
   trường hợp liệt kê chính đáng như Ch6 dòng 13), theo đúng kỹ thuật đã áp dụng ở Ch2–4.
4. **Tuỳ chọn, ưu tiên trung bình:** thêm Table 5.1 so sánh priority structure với 5 nghiên
   cứu trước ở §5.4 (mục 6).

Mục 1–2 là lỗi thật (số liệu sai + overclaim sót), nên ưu tiên sửa trước; mục 3–4 là cải
thiện hình thức/trình bày, có thể làm sau hoặc bỏ qua tuỳ thời gian còn lại của dự án.
