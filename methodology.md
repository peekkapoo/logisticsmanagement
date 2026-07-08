
# Hệ thống Phương pháp Luận Toàn diện trong Nghiên cứu Ra Quyết định Đa Tiêu chí và Kiến tạo Đồng thuận Chuyên gia

Lý thuyết ra quyết định đa tiêu chí (Multi-Criteria Decision-Making - MCDM), hay phân tích quyết định đa tiêu chí (Multi-Criteria Decision Analysis - MCDA), là một phân nhánh học thuật cốt lõi của vận trù học (Operations Research - OR).^^ Ngành khoa học này cung cấp hệ thống công cụ toán học vững chắc để hỗ trợ các nhà quyết định trong bối cảnh phức tạp, nơi tồn tại sự mâu thuẫn giữa các mục tiêu, tính bất định của thông tin và sự phụ thuộc vào tri thức chủ quan của chuyên gia.^^ Việc thiết lập một mô hình nghiên cứu MCDM hoàn chỉnh đòi hỏi sự kết hợp chặt chẽ giữa hai pha: pha kiến tạo dữ liệu/tiêu chí đầu vào thông qua các kỹ thuật lấy ý kiến chuyên gia (expert elicitation) và pha mô hình hóa toán học để xác định trọng số cũng như xếp hạng phương án.^^

## Khung Phân tích Bản chất và Sự Phân tách Giữa các Hệ hình Quyết định

Trong không gian lý thuyết của MCDM, sự phân chia phương pháp luận cơ bản nhất nằm ở cấu trúc không gian giải pháp, tạo nên hai hệ hình nghiên cứu lớn: Ra quyết định đa thuộc tính (Multi-Attribute Decision-Making - MADM) và Ra quyết định đa mục tiêu (Multi-Objective Decision-Making - MODM).^^

### Bản chất Toán học và Không gian Giải pháp

Hệ hình MADM tập trung vào không gian quyết định rời rạc (discrete solution space).^^ Nhiệm vụ của nhà quyết định là đánh giá, phân loại hoặc xếp hạng một số lượng hữu hạn các phương án đã được định hình sẵn.^^ Mỗi phương án được đặc trưng bởi một tập hợp các thuộc tính (tiêu chí) có tính chất mâu thuẫn trực tiếp với nhau.^^

Ngược lại, hệ hình MODM xử lý không gian quyết định liên tục (continuous solution space).^^ Trong mô hình này, các phương án không có sẵn mà phải được thiết kế hoặc tối ưu hóa dựa trên một tập hợp các hàm mục tiêu toán học mâu thuẫn, chịu sự ràng buộc bởi các giới hạn vật lý, tài chính hoặc kỹ thuật.^^ Mục tiêu của MODM là tìm kiếm tập hợp giải pháp tối ưu Pareto (Pareto-optimal solutions), biểu thị các trạng thái cân bằng mà tại đó không một mục tiêu nào có thể cải thiện thêm nếu không làm suy giảm mục tiêu khác.^^

### Sự Ưu việt mang Tính Bối cảnh của MADM trong Quản trị

Mặc dù MODM có tính chặt chẽ cao về mặt tối ưu hóa toán học, nghiên cứu thực nghiệm chỉ ra rằng các mô hình MADM chiếm ưu thế áp đảo trong các ứng dụng quản lý, tài chính và chiến lược doanh nghiệp.^^ Xu hướng này xuất phát từ bản chất của các vấn đề quản trị.^^ Các nhà quản lý thường đối mặt với các quyết định mang tính chiến thuật hoặc chiến lược có sẵn các phương án thực thi thực tế (chọn địa điểm xây dựng nhà máy, lựa chọn nhà cung cấp, phê duyệt dự án đầu tư).^^ Việc mô hình hóa các quyết định này dưới dạng các thuộc tính rời rạc phù hợp với cấu trúc tư duy tự nhiên của con người hơn là việc thiết lập các hàm mục tiêu liên tục phức tạp.^^

Thêm vào đó, MODM đòi hỏi các hàm số liên tục cực kỳ chính xác về mối quan hệ giữa các biến.^^ Trong quản trị kinh doanh, các thông tin này thường bị mờ, định tính và không thể lượng hóa một cách hoàn hảo.^^ MADM cho phép tích hợp linh hoạt cả dữ liệu định lượng (chi phí, hiệu suất) lẫn dữ liệu định tính (uy tín, mức độ hài lòng) thông qua đánh giá của chuyên gia.^^

| **Tiêu chí So sánh**      | **Ra Quyết định Đa Thuộc tính (MADM)**                | **Ra Quyết định Đa Mục tiêu (MODM)**              |
| ---------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| **Không gian giải pháp**  | Rời rạc (Discrete)                                              | Liên tục (Continuous)                                       |
| **Số lượng phương án** | Hữu hạn, được xác định trước                            | Vô hạn, được tạo ra qua mô hình tối ưu              |
| **Mục tiêu cốt lõi**     | Lựa chọn, phân loại hoặc xếp hạng các phương án        | Thiết kế phương án tốt nhất thỏa mãn các mục tiêu |
| **Bản chất tiêu chí**    | Các thuộc tính (Attributes) mâu thuẫn nhau                   | Các hàm mục tiêu (Objective functions) mâu thuẫn        |
| **Yêu cầu Mô hình**      | Ma trận quyết định rời rạc                                  | Hàm mục tiêu liên tục và hệ ràng buộc                |
| **Ứng dụng điển hình**  | Quản lý chiến lược, tuyển chọn nhân sự, chuỗi cung ứng | Thiết kế kỹ thuật, lập lịch sản xuất tối ưu         |

## Triết học Quyết định: Bản đồ Phân rã Giữa Trường phái Mỹ và Trường phái Châu Âu

Sự phát triển của lý thuyết MCDM toàn cầu bị chia tách sâu sắc bởi hai luồng tư duy triết học lớn: Trường phái Mỹ và Trường phái Châu Âu.^^ Sự khác biệt này không chỉ nằm ở các thuật toán cụ thể mà còn ở cách thức nhìn nhận hành vi ra quyết định và cách xử lý sự bất định của thông tin.^^

### Trường phái Mỹ: Hướng Tiếp cận Chức năng và Tiêu chí Tổng hợp Duy nhất

Trường phái Mỹ (American School) tiếp cận bài toán quyết định dựa trên triết học duy lý chức năng và lý thuyết hữu dụng.^^ Trọng tâm của trường phái này là giả định rằng mọi tiêu chí đánh giá đều có thể được quy đổi về một thang đo giá trị hoặc độ hữu dụng tổng hợp duy nhất (single synthesized criterion).^^

Các phương pháp thuộc trường phái này xây dựng một hàm giá trị tổng hợp để đại diện cho mức độ ưu tiên của nhà quyết định.^^ Trường phái này thừa nhận tính bù trừ (compensatory), nghĩa là một điểm số rất kém ở tiêu chí này có thể được bù đắp hoàn toàn bởi một điểm số cực kỳ xuất sắc ở tiêu chí khác.^^ Các phương pháp tiêu biểu bao gồm Thuyết hữu dụng đa thuộc tính (MAUT), Quá trình phân tích cấp bậc (AHP), Quá trình phân tích mạng lưới (ANP), Kỹ thuật đánh giá đa thuộc tính đơn giản (SMART), và phương pháp khoảng cách như TOPSIS.^^

Hạn chế cố hữu của cách tiếp cận này là thường bỏ qua hoặc đơn giản hóa quá mức tính không nhất quán của dữ liệu, sự mơ hồ trong nhận thức và các rào cản về mặt ưu tiên của nhà quyết định, đồng thời giả định rằng nhà quyết định luôn có khả năng so sánh một cách nhất quán mọi phương án với nhau.^^

### Trường phái Châu Âu: Hướng Tiếp cận Quan hệ và Phương pháp Vượt trội

Trường phái Châu Âu (European School) bác bỏ giả định về tính bù trừ hoàn hảo và khả năng so sánh toàn diện của Trường phái Mỹ.^^ Dựa trên nền tảng của triết học quan hệ (relational concept), trường phái này cho rằng trong thực tế phức tạp, có những phương án hoàn toàn không thể so sánh được với nhau (incomparability) hoặc nhà quyết định có sự do dự không thể xóa bỏ.^^

Thay vì tổng hợp mọi tiêu chí thành một điểm số duy nhất, trường phái Châu Âu xây dựng các quan hệ vượt trội (outranking relations) giữa từng cặp phương án.^^ Phương án **$A$** được coi là vượt trội phương án **$B$** nếu có đủ bằng chứng chứng minh **$A$** tốt hơn **$B$** trên đa số các tiêu chí quan trọng (sự nhất trí - concordance) và không có tiêu chí nào mà tại đó **$A$** kém hơn **$B$** đến mức không thể chấp nhận được (sự không nhất trí - discordance).^^ Các dòng phương pháp tiêu biểu là ELECTRE (ÉLimination et Choix Traduisant la REalité) và PROMETHEE (Preference Ranking Organization Method for Enrichment of Evaluations).^^ Cách tiếp cận này phản ánh chân thực hành vi ra quyết định của con người khi đối mặt với các giới hạn nghiêm ngặt.^^

### Sự Hội tụ Học thuật qua các Mô hình Lai ghép

Nhằm tận dụng tối đa thế mạnh của cả hai tư duy triết học, các nghiên cứu đương đại đang chuyển dịch mạnh mẽ sang các phương pháp lai ghép (hybrid methods).^^ Sự tích hợp này giúp kết hợp khả năng mô hình hóa ưu tiên trực quan của trường phái Mỹ với khả năng xử lý sự mâu thuẫn và tính không bù trừ của trường phái Châu Âu.^^ Các mô hình tích hợp tiêu biểu bao gồm EVAMIX, QUALIFLEX, hay COMET.^^

| **Đặc tính Triết học** | **Trường phái Mỹ (American School)**                       | **Trường phái Châu Âu (European School)**       |
| --------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Triết học nền tảng**  | Duy lý chức năng, lý thuyết hữu dụng                          | Triết học quan hệ, chấp nhận sự không thể so sánh |
| **Cơ chế tích hợp**     | Tiêu chí tổng hợp duy nhất (Single synthesized criterion)       | Quan hệ vượt trội từng cặp (Outranking relations)    |
| **Mức độ bù trừ**      | Bù trừ hoàn toàn (Compensatory)^^                                | Phi bù trừ hoặc bù trừ một phần (Non-compensatory)  |
| **Phương pháp chính**   | MAUT, AHP, ANP, SMART, UTA, MACBETH, TOPSIS^^                        | ELECTRE, PROMETHEE, NAIADE, ORESTE, REGIME^^               |
| **Mô hình lai ghép**     | EVAMIX, QUALIFLEX, PCCA, MAPPAC, PRAGMA, PACMAN, IDRA, COMET, DRSA^^ |                                                            |

## Các Phương pháp Tham vấn và Kiến tạo Đồng thuận Chuyên gia

Bất kỳ một mô hình MCDM nào cũng chỉ có giá trị thực tiễn khi hệ thống tiêu chí đầu vào được xây dựng một cách khoa học.^^ Để đạt được điều này, các nhà nghiên cứu thường tích hợp các phương pháp tham vấn chuyên gia có cấu trúc nhằm loại bỏ định kiến cá nhân và kiến tạo sự đồng thuận nhóm.^^

### Phân tích Đối chiếu: Delphi Truyền thống và Kỹ thuật Nhóm Danh nghĩa (NGT)

Hai kỹ thuật kiến tạo đồng thuận cổ điển nhất là Kỹ thuật Delphi và Kỹ thuật Nhóm danh nghĩa (Nominal Group Technique - NGT).^^ Việc lựa chọn giữa hai phương pháp này phụ thuộc sâu sắc vào ranh giới địa lý của chuyên gia, thời gian nghiên cứu và mức độ nhạy cảm của chủ đề quyết định.^^

Kỹ thuật Delphi truyền thống vận hành dựa trên nguyên tắc ẩn danh hoàn toàn thông qua nhiều vòng khảo sát lặp đi lặp lại bằng bảng câu hỏi gửi qua thư điện tử.^^ Sau mỗi vòng, điều phối viên tổng hợp ý kiến, cung cấp phản hồi thống kê có kiểm soát để các chuyên gia điều chỉnh nhận định ở vòng tiếp theo cho đến khi đạt được sự hội tụ ý kiến.^^ Sự ẩn danh giúp triệt tiêu hoàn toàn hiệu ứng áp lực nhóm hoặc sự lấn át của các chuyên gia có vị thế cao.^^ Tuy nhiên, quy trình này đòi hỏi thời gian kéo dài (hàng tuần hoặc hàng tháng) và có nguy cơ cao gây ra sự mệt mỏi, nhàm chán cho chuyên gia qua các vòng lặp.^^

Kỹ thuật Nhóm Danh nghĩa (NGT) là một tiến trình tương tác trực tiếp (hoặc trực tuyến đồng thì) có cấu trúc chặt chẽ.^^ Quy trình bao gồm bốn giai đoạn độc lập: suy nghĩ độc lập (silent generation), chia sẻ vòng tròn (round-robin), thảo luận làm rõ (clarification), và bỏ phiếu xếp hạng (voting/ranking).^^ NGT tối ưu hóa sự tham gia bình đẳng của các thành viên trong một thời gian ngắn, thường hoàn thành trong một phiên họp duy nhất.^^ Tuy nhiên, do tính chất tương tác trực tiếp, NGT dễ bị ảnh hưởng bởi áp lực tuân thủ (groupthink) và bị giới hạn nghiêm ngặt bởi quy mô nhóm (thường dưới 7-14 chuyên gia).^^

Để tận dụng ưu điểm của cả hai phương pháp, các nhà nghiên cứu đã phát triển mô hình Panel lai ghép (Hybrid Panel) kết hợp Delphi và NGT.^^ Phương pháp này yêu cầu các chuyên gia đánh giá độc lập ở vòng đầu tiên để neo giữ ý kiến cá nhân dựa trên tri thức riêng biệt, sau đó tham gia thảo luận nhóm trực tiếp có cấu trúc để thu hẹp khoảng lệch phân phối đánh giá.^^

### Sự Đột phá của Phương pháp Delphi Mờ (Fuzzy Delphi Method - FDM)

Nhằm khắc phục triệt để các hạn chế của Delphi truyền thống—đặc biệt là gánh nặng thời gian do phải lặp lại nhiều vòng khảo sát và sự mơ hồ trong việc diễn đạt ý kiến bằng ngôn ngữ tự nhiên—phương pháp Delphi Mờ (FDM) đã được phát triển bằng cách tích hợp Lý thuyết Tập mờ của Zadeh (1965) và cải tiến của Ishikawa (1993).^^ FDM cho phép thu thập và xử lý toàn bộ nhận định của chuyên gia chỉ trong một vòng khảo sát mà vẫn đảm bảo tính nhất quán khoa học cao.^^

Quy trình toán học của FDM được thực hiện qua các bước nghiêm ngặt sau:

#### Bước 1: Ánh xạ biến ngôn ngữ sang Số mờ tam giác (TFN)

Các chuyên gia đánh giá tầm quan trọng của từng tiêu chí bằng các thang đo ngôn ngữ (ví dụ: Rất quan trọng, Quan trọng, Trung bình).^^ Các biến ngôn ngữ này được ánh xạ sang các Số mờ tam giác (Triangular Fuzzy Numbers - TFNs) ký hiệu là **$A = (l, m, u)$**, trong đó **$l, m, u$** lần lượt biểu thị giá trị cận dưới, giá trị trung bình và giá trị cận trên.^^

#### Bước 2: Thiết lập TFN tích hợp cho từng tiêu chí

Giả sử có **$H$** chuyên gia thực hiện đánh giá.^^ Đối với mỗi tiêu chí **$i$**, ta xác định các giá trị tích hợp dựa trên ý kiến của toàn bộ hội đồng chuyên gia ^^:

$$
A_i = (l_i, m_i, u_i)
$$

Trong đó, **$l_i = \min_{k=1 \dots H} (l_i^k)$** là giá trị nhỏ nhất trong tất cả các đánh giá cận dưới, **$m_i = \left( \prod_{k=1}^H m_i^k \right)^{1/H}$** là trung bình hình học của các giá trị trung bình, và **$u_i = \max_{k=1 \dots H} (u_i^k)$** là giá trị lớn nhất trong tất cả các đánh giá cận trên.^^

#### Bước 3: Kiểm tra mức độ đồng thuận chuyên gia

Để xác định xem ý kiến của các chuyên gia đã hội tụ hay chưa, người ta tính toán khoảng cách (distance - **$d$**) giữa đánh giá của từng chuyên gia **$k$** so với giá trị trung bình nhóm **$A_i$** ^^:

$$
d(A_i^k, A_i) = \sqrt{\frac{1}{3} \left[ (l_i^k - l_i)^2 + (m_i^k - m_i)^2 + (u_i^k - u_i)^2 \right]}
$$

Nếu khoảng cách **$d \le 0.2$** đối với tất cả các chuyên gia, sự đồng thuận nhóm chính thức được xác lập.^^ Đồng thời, tỷ lệ đồng thuận của chuyên gia cho mỗi tiêu chí phải đạt tối thiểu **$75.0\%$**.^^

Một hướng tiếp cận khác được đề xuất bởi Ishikawa (1993) sử dụng phương pháp cực đại - cực tiểu kết hợp phân phối tần suất lũy tích và điểm số mờ để kiểm tra tính đồng thuận.^^ Nếu tồn tại sự giao thoa quá lớn giữa số mờ bảo thủ và số mờ tích cực (vùng xám vượt quá ngưỡng cho phép), ý kiến của các chuyên gia bị coi là xung đột và quy trình khảo sát phải quay lại bước đầu tiên.^^

#### Bước 4: Giải mờ và Sàng lọc tiêu chí

Sau khi đạt đồng thuận, số mờ của tiêu chí **$i$** được giải mờ thành một số thực duy nhất **$G_i$** đại diện cho điểm số tầm quan trọng.^^ Phương pháp phổ biến nhất là ^^:

$$
G_i = \frac{l_i + m_i + u_i}{3}
$$

Để lọc các tiêu chí cuối cùng, một ngưỡng cắt (threshold - **$\theta$**) được thiết lập bằng cách tính trung bình hình học hoặc trung bình cộng của toàn bộ điểm số giải mờ của tất cả các tiêu chí.^^ Tiêu chí nào có **$G_i \ge \theta$** sẽ được giữ lại trong mô hình MCDM chính thức.^^

### Xu hướng Đương đại: Mô hình Delphi Lai ghép giữa Con người và Trí tuệ Nhân tạo (HAH-Delphi)

Trong bối cảnh công nghệ số phát triển vượt bậc, mô hình Delphi Lai ghép giữa Con người và AI (Human-AI Hybrid Delphi - HAH-Delphi) xuất hiện như một khung phân tích mới giúp tối ưu hóa quy trình đồng thuận.^^ Mô hình này tích hợp các mô hình ngôn ngữ lớn hoạt động như một thực thể hỗ trợ điều phối hoặc đóng vai trò như một "chuyên gia ảo" chạy song song với hội đồng chuyên gia con người.^^

Quy trình HAH-Delphi được thiết kế qua ba pha nghiêm ngặt:

1. **Pha tái lập hồi cứu (Retrospective replication):** AI kiểm chứng khả năng tái lập các kết luận đồng thuận từ các nghiên cứu đã công bố trong lịch sử.^^
2. **Pha so sánh đối chiếu (Prospective comparison):** AI hoạt động song song với các chuyên gia con người để đánh giá mức độ tương đồng trong định hướng nhận định.^^
3. **Pha triển khai thực tế (Applied deployment):** Tích hợp AI vào quá trình điều phối thời gian thực.^^

Hệ thống AI đóng vai trò như một khung đỡ kiến thức vững chắc, giúp giải quyết các bất đồng ý kiến nhanh chóng và thúc đẩy sự bão hòa chủ đề (thematic saturation) ngay cả khi quy mô panel chuyên gia con người thu hẹp xuống mức tối thiểu (khoảng 6 chuyên gia).^^

## Các Kỹ thuật Lượng hóa Trọng số Tiêu chí từ Đánh giá Chuyên gia

Sau khi hệ thống tiêu chí đã được định hình, việc xác định trọng số là bước đi quyết định ảnh hưởng trực tiếp đến kết quả xếp hạng phương án.^^ Bốn phương pháp phổ biến dưới đây đại diện cho các cách tiếp cận khác nhau về tải lượng tính toán và khả năng phản ánh tư duy chuyên gia.^^

### 1. Phương pháp Phân tích Cấp bậc (AHP)

AHP, do Saaty phát triển năm 1980, sử dụng ma trận so sánh cặp đối xứng để tính toán trọng số.^^ Chuyên gia tiến hành so sánh từng cặp tiêu chí sử dụng thang đo tỷ lệ từ 1 đến 9 để xây dựng ma trận so sánh cặp **$A = [a_{ij}]_{n \times n}$**.^^ Trọng số tiêu chí được xác định bằng cách tìm vectơ riêng chính của ma trận ứng với trị riêng lớn nhất **$\lambda_{\max}$**.^^

Để đảm bảo tính nhất quán của nhận định chuyên gia, AHP bắt buộc phải thực hiện kiểm tra tính nhất quán thông qua Tỷ số nhất quán (**$CR$**) ^^:

$$
CI = \frac{\lambda_{\max} - n}{n - 1}, \quad CR = \frac{CI}{RI}
$$

Trong đó **$RI$** là Chỉ số ngẫu nhiên tương ứng với kích thước ma trận **$n$**, và giá trị **$CR \le 0.1$** được coi là đạt yêu cầu.^^

Tuy nhiên, nếu số lượng tiêu chí lớn, số phép so sánh cặp tăng theo hàm số mũ **$n(n-1)/2$**, dễ gây ra mệt mỏi cho chuyên gia và làm mất tính nhất quán của ma trận.^^ Điều này dẫn đến sự ra đời của phương pháp Quá trình phân tích cấp bậc bỏ phiếu (Voting AHP - VAHP) hoặc phương pháp BM-AHP (AHP-EXPRESS) nhằm tối giản hóa số lượng đánh giá cần thiết.^^ Ngoài ra, phương pháp hỗn hợp AHP-SSM (Standard Scoring Method) cũng được đề xuất để loại bỏ hoàn toàn bước phân tích nhất quán bổ sung bằng cách tính toán trực tiếp dựa trên các công thức chuẩn hóa giá trị thực.^^

### 2. Phương pháp Tốt nhất - Tệ nhất (Best-Worst Method - BWM)

BWM được đề xuất bởi Rezaei vào năm 2015 nhằm giải quyết trực tiếp điểm yếu về tải lượng nhận thức và số phép so sánh của AHP.^^ Quy trình toán học của BWM bao gồm năm bước cơ bản ^^:

#### Bước 1: Xác định tập hợp tiêu chí quyết định

Hội đồng chuyên gia thiết lập tập hợp các tiêu chí **$\{C_1, C_2, \dots, C_n\}$** cần được đánh giá.^^

#### Bước 2: Định danh tiêu chí tốt nhất và tệ nhất

Chuyên gia tự chọn ra tiêu chí quan trọng nhất (Best - **$C_B$**) và tiêu chí ít quan trọng nhất (Worst - **$C_W$**) trong hệ thống.^^

#### Bước 3: So sánh cặp tiêu chí tốt nhất với các tiêu chí khác

Xây dựng vectơ Best-to-Others (**$A_B$**) sử dụng thang đo từ 1 đến 9 ^^:

$$
A_B = (a_{B1}, a_{B2}, \dots, a_{Bn})
$$

Trong đó **$a_{Bj}$** thể hiện mức độ ưu tiên của tiêu chí Best so với tiêu chí **$j$**.^^

#### Bước 4: So sánh cặp các tiêu chí khác với tiêu chí tệ nhất

Xây dựng vectơ Others-to-Worst (**$A_W$**) sử dụng thang đo từ 1 đến 9 ^^:

$$
A_W = (a_{1W}, a_{2W}, \dots, a_{nW})^T
$$

Trong đó **$a_{jW}$** thể hiện mức độ ưu tiên của tiêu chí **$j$** so với tiêu chí Worst.^^

#### Bước 5: Tính toán trọng số tối ưu và kiểm tra tính nhất quán

Trọng số tối ưu của các tiêu chí **$(w_1, w_2, \dots, w_n)$** được xác định bằng cách giải bài toán quy hoạch toán học tuyến tính hóa sau ^^:

$$
\min \xi
$$

$$
\text{Sự thỏa mãn các ràng buộc: } \left| \frac{w_B}{w_j} - a_{Bj} \right| \le \xi, \quad \forall j
$$

$$
\left| \frac{w_j}{w_W} - a_{jW} \right| \le \xi, \quad \forall j
$$

$$
\sum_{j=1}^n w_j = 1, \quad w_j \ge 0, \quad \forall j
$$

BWM chỉ yêu cầu **$2n - 3$** phép so sánh cặp.^^ Mặc dù nhiều nghiên cứu khẳng định BWM tạo ra kết quả nhất quán hơn AHP, một số nghiên cứu phản biện gần đây chỉ ra rằng việc giảm thiểu số lượng so sánh trong BWM có thể làm mất đi các thông tin kiểm chứng chéo và gây ra khó khăn trong việc đo lường chính xác chỉ số không nhất quán thực tế.^^

### 3. Phương pháp Phân tích Tỷ lệ Trọng số Từng bước (SWARA)

SWARA là một phương pháp xác định trọng số trực tiếp, cực kỳ trực quan và không đòi hỏi các phép so sánh cặp phức tạp.^^ Tiến trình tính toán của SWARA được thực hiện qua các bước sau ^^:

#### Bước 1: Sắp xếp thứ tự ưu tiên của tiêu chí

Các chuyên gia thảo luận và sắp xếp toàn bộ hệ thống tiêu chí theo thứ tự quan trọng giảm dần.^^

#### Bước 2: Xác định mức độ quan trọng tương đối (**$s_j$**)

Bắt đầu từ tiêu chí thứ hai (**$j = 2$**), chuyên gia đánh giá mức độ kém quan trọng của tiêu chí **$j$** so với tiêu chí ngay trước đó (**$j-1$**), ký hiệu là giá trị so sánh **$s_j$**.^^

#### Bước 3: Tính toán hệ số so sánh (**$k_j$**)

$$
k_j = \begin{cases} 1 & j = 1 \\ s_j + 1 & j > 1 \end{cases}
$$

^^

#### Bước 4: Tính toán trọng số chưa chuẩn hóa (**$q_j$**)

$$
q_j = \begin{cases} 1 & j = 1 \\ \frac{q_{j-1}}{k_j} & j > 1 \end{cases}
$$

^^

#### Bước 5: Tính toán trọng số chuẩn hóa cuối cùng (**$w_j$**)

$$
w_j = \frac{q_j}{\sum_{k=1}^n q_k}
$$

^^

SWARA đặc biệt thích hợp trong các bối cảnh chính sách công, quản lý rủi ro hoặc bảo tồn di sản bền vững, nơi các nhà hoạch định chính sách muốn tích hợp nhanh các định hướng ưu tiên thực tế của họ vào hệ thống đánh giá mà không bị cản trở bởi các thủ tục toán học phức tạp.^^

### 4. Phương pháp Phòng thí nghiệm Đánh giá và Thử nghiệm Quyết định (DEMATEL)

DEMATEL không chỉ đơn thuần tính toán trọng số mà còn có khả năng bóc tách cấu trúc tương tác và phân lập mối quan hệ nhân quả giữa các tiêu chí trong một hệ thống phức tạp.^^ Quy trình toán học của DEMATEL được thực hiện qua các giai đoạn sau ^^:

#### Giai đoạn 1: Thiết lập ma trận ảnh hưởng trực tiếp trung bình (**$A$**)

Hội đồng gồm **$H$** chuyên gia đánh giá mức độ ảnh hưởng trực tiếp của tiêu chí **$i$** lên tiêu chí **$j$** theo thang đo từ 0 (không ảnh hưởng) đến 4 (ảnh hưởng cực cao).^^ Ma trận ảnh hưởng trực tiếp trung bình **$A = [a_{ij}]_{n \times n}$** được tính bằng cách lấy trung bình cộng các đánh giá của các chuyên gia.^^

#### Giai đoạn 2: Chuẩn hóa ma trận ảnh hưởng trực tiếp

Xác định hệ số chuẩn hóa **$s$** ^^:

$$
s = \max \left( \max_{1 \le i \le n} \sum_{j=1}^n a_{ij}, \max_{1 \le j \le n} \sum_{i=1}^n a_{ij} \right)
$$

Ma trận chuẩn hóa **$D$** được tính bằng ^^:

$$
D = \frac{A}{s}
$$

#### Giai đoạn 3: Tính toán ma trận ảnh hưởng toàn diện (**$T$**)

Ma trận ảnh hưởng toàn diện **$T$** biểu thị cả ảnh hưởng trực tiếp và gián tiếp giữa các tiêu chí ^^:

$$
T = D(I - D)^{-1}
$$

Trong đó **$I$** là ma trận đơn vị.^^

#### Giai đoạn 4: Phân tích cấu trúc nhân quả

Tính toán tổng các hàng (**$D_i$**) và tổng các cột (**$R_i$**) của ma trận **$T$**.^^

* Trục hoành (**$D_i + R_i$**) được gọi là "Độ nổi bật" (Prominence), thể hiện tầm quan trọng tổng thể của tiêu chí trong hệ thống.^^
* Trục tung (**$D_i - R_i$**) được gọi là "Quan hệ" (Relation).^^ Nếu **$D_i - R_i > 0$**, tiêu chí thuộc nhóm Nguyên nhân (Cause group); nếu **$D_i - R_i < 0$**, tiêu chí thuộc nhóm Kết quả (Effect group).^^ Trọng số của tiêu chí có thể được xác định bằng cách chuẩn hóa các giá trị **$(D_i + R_i)$**.^^

### Các Phương pháp Xác định Trọng số Khác và Hướng Tiếp cận Lai ghép

Bên cạnh các phương pháp trên, các nhà nghiên cứu còn sử dụng nhiều kỹ thuật đo lường trọng số khác như: Phương pháp nhất quán hoàn toàn (FUCOM) giúp đạt được độ nhất quán cao với số lượng so sánh tối giản ^^; phương pháp CRITIC xác định trọng số khách quan dựa trên độ lệch chuẩn và hệ số tương quan giữa các tiêu chí ^^; hay phương pháp Trọng số Entropy dựa trên lý thuyết thông tin để đo lường mức độ phân tán của dữ liệu thực nghiệm.^^ Các phương pháp đơn giản hơn như Trọng số bằng nhau (Equal weight), Trọng số tâm thứ tự (Rank Order Centroid - ROC), hay Trọng số tổng thứ tự (Rank Sum - RS) cũng thường được áp dụng để so sánh đối chứng.^^

Trong các thiết kế nghiên cứu phức tạp, xu hướng lai ghép trọng số (hybrid weighting) đang trở nên phổ biến.^^ Việc kết hợp các phương pháp như BWM-AHP, SWARA-AHP, hay BM-AHP giúp tận dụng khả năng biểu diễn phân cấp cấu trúc của AHP nhưng đồng thời làm giảm đáng kể áp lực thời gian và mệt mỏi cho hội đồng chuyên gia.^^

## Các Thuật toán Đánh giá và Xếp hạng Phương án Lựa chọn

Sau khi đã thiết lập được ma trận quyết định và hệ thống trọng số của các tiêu chí, bước tiếp theo là áp dụng các mô hình toán học để xếp hạng các phương án lựa chọn.^^

### 1. Phương pháp TOPSIS (Hwang & Yoon, 1981)

TOPSIS vận hành dựa trên nguyên lý khoảng cách hình học.^^ Phương án tối ưu là phương án có khoảng cách ngắn nhất đến Giải pháp Lý tưởng Dương (Positive Ideal Solution - PIS) và đồng thời có khoảng cách xa nhất đối với Giải pháp Lý tưởng Âm (Negative Ideal Solution - NIS).^^

Trong lịch sử tích hợp phương pháp luận, sự kết hợp giữa AHP và TOPSIS là hướng đi phổ biến nhất trong nhóm các phương pháp dựa trên khoảng cách.^^ Nghiên cứu đầu tiên đề xuất mô hình tích hợp AHP-TOPSIS được công bố vào năm 2002 bởi Ye và cộng sự để đánh giá rủi ro hỏa hoạn đô thị, tiếp theo là phiên bản tích hợp Fuzzy AHP-TOPSIS của Chen và Tzeng vào năm 2004.^^

### 2. Phương pháp MARCOS (Stević và cộng sự, 2020)

MARCOS là một trong những công cụ xếp hạng mạnh mẽ và ổn định nhất hiện nay, có khả năng chống lại hiện tượng đảo ngược thứ hạng (Rank Reversal) vượt trội nhờ việc cố định các ranh giới tham chiếu lý tưởng.^^ Tiến trình toán học của MARCOS được thực hiện qua các bước cụ thể sau ^^:

#### Bước 1: Xây dựng ma trận quyết định mở rộng

Bổ sung Giải pháp Lý tưởng (**$AI$**) và Giải pháp Phản Lý tưởng (**$AAI$**) trực tiếp vào ma trận quyết định ban đầu có **$m$** phương án và **$n$** tiêu chí ^^:

$$
AAI = \{x_{aa1}, x_{aa2}, \dots, x_{aan}\}
$$

$$
AI = \{x_{ai1}, x_{ai2}, \dots, x_{ain}\}
$$

Trong đó, đối với tiêu chí lợi ích (**$B$**), **$x_{aij} = \max_i x_{ij}$** và **$x_{aaij} = \min_i x_{ij}$**; đối với tiêu chí chi phí (**$C$**), các giá trị này được xác định ngược lại.^^

#### Bước 2: Chuẩn hóa ma trận quyết định mở rộng

Các phần tử chuẩn hóa **$r_{ij}$** được xác định bằng cách so sánh trực tiếp với giải pháp lý tưởng ^^:

* Đối với tiêu chí lợi ích (**$B$**):

  $$
  r_{ij} = \frac{x_{ij}}{x_{aij}}
  $$

  ^^
* Đối với tiêu chí chi phí (**$C$**):

  $$
  r_{ij} = \frac{x_{aij}}{x_{ij}}
  $$

  ^^

#### Bước 3: Tính toán ma trận trọng số mở rộng

$$
v_{ij} = r_{ij} \cdot w_j
$$

^^

#### Bước 4: Tính toán tổng điểm hữu dụng cho từng phương án

Điểm hữu dụng tổng hợp **$S_i$** của phương án **$i$** được tính bằng tổng các dòng của ma trận trọng số mở rộng ^^:

$$
S_i = \sum_{j=1}^n v_{ij}
$$

Từ đó, xác định mức độ hữu dụng của phương án **$i$** so với giải pháp lý tưởng (**$K_i^+$**) và phản lý tưởng (**$K_i^-$**) ^^:

$$
K_i^- = \frac{S_i}{S_{aai}}, \quad K_i^+ = \frac{S_i}{S_{ai}}
$$

Trong đó **$S_{aai}$** và **$S_{ai}$** lần lượt là tổng điểm hữu dụng của giải pháp phản lý tưởng và lý tưởng.^^

#### Bước 5: Xác định hàm hữu dụng tổng hợp và Xếp hạng

Hàm hữu dụng tổng hợp **$f(K_i)$** được thiết lập nhằm dung hòa cả hai hướng khoảng cách ^^:

$$
f(K_i) = \frac{K_i^- + K_i^+}{1 + \frac{1 - f(K_i^+)}{f(K_i^+)} + \frac{1 - f(K_i^-)}{f(K_i^-)}}
$$

Trong đó:

$$
f(K_i^-) = \frac{K_i^+}{K_i^- + K_i^+}, \quad f(K_i^+) = \frac{K_i^-}{K_i^- + K_i^+}
$$

^^

Thứ hạng các phương án được sắp xếp theo chiều giảm dần của giá trị **$f(K_i)$**.^^

### 3. Phương pháp Phân tích Tương quan Xám (GRA)

GRA là một bộ phận cốt lõi của Lý thuyết Hệ thống Xám (Grey System Theory) do Deng Julong phát triển năm 1982.^^ GRA tiếp cận các bài toán quyết định có thông tin cực kỳ hạn chế (poor information) hoặc cỡ mẫu cực nhỏ mà các phương pháp thống kê truyền thống không thể xử lý.^^ GRA không tìm kiếm một giải pháp tối ưu tuyệt đối mà đánh giá mức độ tương đồng hình học giữa chuỗi số liệu của phương án khảo sát so với chuỗi số liệu tham chiếu lý tưởng.^^ Phương án nào có Cấp độ tương quan xám (Grey Relational Grade - GRG) cao nhất sẽ được chọn làm giải pháp tốt nhất cho hệ thống.^^

### Lịch sử và Xu hướng Tích hợp Phương pháp Luận

Việc kết hợp các phương pháp xác định trọng số (như AHP/ANP) với các phương pháp xếp hạng phương án (như TOPSIS, VIKOR, PROMETHEE, DEMATEL) dưới cả môi trường số rõ (crisp) và số mờ (fuzzy) đã trở thành một hệ hình nghiên cứu kinh điển.^^

| **Năm Công bố** | **Phương pháp Tích hợp** | **Tác giả Tiêu biểu** | **Ứng dụng Thực tiễn Điển hình**          |
| ------------------------ | ----------------------------------- | ------------------------------- | ------------------------------------------------------ |
| **1995**           | Crisp AHP + PROMETHEE               | Urli & Beaudry, 1995^^          | Đánh giá dự án đa tiêu chí phi bù trừ        |
| **2002**           | Crisp AHP + TOPSIS                  | Ye et al., 2002^^               | Đánh giá rủi ro hỏa hoạn đô thị               |
| **2004**           | Fuzzy AHP + TOPSIS                  | Chen & Tzeng, 2004^^            | Quyết định trong môi trường bất định          |
| **2010**           | Crisp AHP + DEMATEL                 | Wu et al., 2010^^               | Đánh giá dịch vụ hỗ trợ việc làm              |
| **2011**           | Fuzzy AHP + DEMATEL                 | Shahraki & Paghaleh, 2011^^     | Phân tích nhân quả trong môi trường mờ         |
| **2011**           | Fuzzy AHP + PROMETHEE               | Özgen et al., 2011^^           | Lựa chọn phương án logistics và chuỗi cung ứng |
| **2020**           | Fuzzy Delphi + BWM + MARCOS         | Stević et al., 2020^^          | Lựa chọn nhà cung cấp y tế bền vững             |
| **2024**           | Crisp AHP + SSM                     | Topaloğlu, 2024^^              | Tuyển chọn vị trí xây dựng cơ sở sản xuất    |

## Biểu diễn Sự Bất định và Các Không gian Số Mờ Mở rộng

Nhận thức của con người luôn chứa đựng sự mơ hồ, do dự và không nhất quán.^^ Việc ép buộc chuyên gia đưa ra các con số chính xác (crisp numbers) thường làm bóp méo thông tin đầu vào.^^ Do đó, các trường phái toán học mờ liên tục được phát triển và tích hợp vào MCDM.^^

### Từ Tập Mờ Cổ điển đến Tập Mờ Trực giác và Pythagorean

Tập Mờ Cổ điển (Fuzzy Sets - Zadeh, 1965) sử dụng hàm thành viên $\mu_A(x) \in $ để biểu diễn mức độ thuộc về một tập hợp của phần tử **$x$**.^^ Mô hình này giải quyết tốt sự mơ hồ về mặt ngôn ngữ, nhưng giả định rằng phần còn lại của nhận thức (**$1 - \mu_A(x)$**) hoàn toàn là độ không thành viên.^^

Tập Mờ Trực giác (Intuitionistic Fuzzy Sets - IFS - Atanassov, 1986) thực hiện cải tiến lớn bằng cách tách biệt độc lập hai trạng thái nhận thức: độ thành viên (**$\theta$**) và độ không thành viên (**$\phi$**), thỏa mãn ràng buộc tuyến tính **$\theta + \phi \le 1$**.^^ Phần còn thiếu hụt **$1 - (\theta + \phi)$** được định nghĩa là biên độ do dự (hesitation margin).^^

Tập Mờ Pythagorean (Pythagorean Fuzzy Sets - PFS) thả lỏng ràng buộc tuyến tính của IFS bằng cách áp đặt điều kiện bình phương: **$\theta^2 + \phi^2 \le 1$**.^^ Sự thay đổi này mở rộng không gian biểu diễn thông tin, cho phép chuyên gia mô tả các nhận định mang tính phân cực cao vốn không được chấp nhận trong IFS.^^

### Sự Ưu việt của Tập Trung tính (Neutrosophic Sets)

Tập trung tính (Neutrosophic Sets - NS - Smarandache, 1995) đại diện cho mức độ khái quát hóa cao nhất của lý thuyết bất định.^^ Neutrosophic chia tách nhận thức của con người thành ba hàm hoàn toàn độc lập và không phụ thuộc vào nhau: Độ Chân thực (Truth-membership - **$T(x)$**), Độ Trung tính/Mơ hồ (Indeterminacy-membership - **$I(x)$**), và Độ Giả tạo (Falsity-membership - **$F(x)$**).^^ Ràng buộc tổng thể được mở rộng trong không gian phi tiêu chuẩn:

$$
0 \le T(x) + I(x) + F(x) \le 3
$$

Sự độc lập hoàn toàn của hàm trung tính **$I(x)$** cho phép NS mô tả các trạng thái thông tin mâu thuẫn hoặc không nhất quán một cách hoàn hảo.^^ Để tăng cường khả năng xử lý thực tế, các nhà nghiên cứu đã phát triển các không gian mở rộng như Tập mềm Neutrosophic Pythagorean (Pythagorean Neutrosophic Soft Sets) với ràng buộc **$0 \le T(x)^2 + I(x)^2 + F(x)^2 \le 1$** ^^, và Tập mềm Neutrosophic Fermatean (Fermatean Neutrosophic Soft Sets) với ràng buộc **$0 \le T(x)^3 + I(x)^3 + F(x)^3 \le 1$**.^^

### Tiếp cận Hệ thống Xám (Grey System Theory) và GRA Đa Phân giải

Trong khi các lý thuyết mờ tập trung vào cấu trúc hàm thành viên chủ quan của con người, Lý thuyết Hệ thống Xám (Grey System Theory) tiếp cận sự bất định từ góc độ thông tin khuyết thiếu hoặc cỡ mẫu cực nhỏ.^^

Trong các mô hình quyết định phức tạp, phương pháp phân tích tương quan xám đa phân giải (grey relational analysis in multigranularity) sử dụng khái niệm "Số xám chuẩn" (normality grey number) kết hợp với các phép kiểm định phân phối để tự động phân cụm dữ liệu ở các mức độ phân giải khác nhau mà không cần dựa vào kinh nghiệm chủ quan của người đánh giá.^^ Điều này giúp mô hình duy trì tính khách quan tối đa khi xử lý các nguồn dữ liệu hỗn hợp và có biến động lớn.^^

| **Không gian Bất định**        | **Hàm lượng Nhận thức Biểu diễn**                                                           | **Ràng buộc Toán học**              | **Khả năng Xử lý Mâu thuẫn**                                         |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| **Fuzzy Set (1965)** ^^            | Độ thành viên (**$\theta$**)                                                                 | $\theta \in $                                 | Không thể biểu diễn sự do dự hoặc phản đối độc lập                  |
| **Intuitionistic Fuzzy (1986)** ^^ | Độ thành viên (**$\theta$**), Độ không thành viên (**$\phi$**)                  | **$\theta + \phi \le 1$**             | Biểu diễn được sự do dự nhưng hạn chế không gian đánh giá          |
| **Pythagorean Fuzzy** ^^           | Độ thành viên (**$\theta$**), Độ không thành viên (**$\phi$**)                  | **$\theta^2 + \phi^2 \le 1$**         | Mở rộng không gian đánh giá cho các nhận định phân cực               |
| **Neutrosophic Set (1995)** ^^     | Độ chân thực (**$T$**), Độ trung tính (**$I$**), Độ giả tạo (**$F$**) | **$0 \le T + I + F \le 3$** ^^        | Tối ưu; tách biệt hoàn toàn độ mơ hồ/trung tính khỏi độ chân/giả |
| **Pythagorean Neutrosophic** ^^    | Độ chân thực (**$T$**), Độ trung tính (**$I$**), Độ giả tạo (**$F$**) | **$0 \le T^2 + I^2 + F^2 \le 1$**     | Rất tốt; dung hòa giữa không gian Pythagorean và tính trung tính         |
| **Grey System (1982)** ^^          | Khoảng giá trị chưa biết (Số xám)                                                                 | Số thực thuộc khoảng đóng**$[l, u]$** | Tập trung vào dữ liệu khuyết thiếu và cỡ mẫu cực nhỏ                  |

## Kết luận

Sự tiến hóa của các phương pháp luận nghiên cứu trong trường phái MCDM phản ánh xu thế tích hợp đa ngành sâu sắc giữa toán học tối ưu, lý thuyết hành vi chuyên gia và khoa học dữ liệu bất định.^^ Một thiết kế nghiên cứu MCDM hiện đại không còn dựa trên các thuật toán đơn lẻ mang tính bù trừ cao, mà dịch chuyển rõ rệt sang các hệ thống lai ghép thông minh (Hybrid MCDM).^^

Quy trình nghiên cứu chuẩn tắc hiện nay thường được thiết lập theo một chuỗi logic chặt chẽ: (1) sử dụng Delphi Mờ hoặc mô hình lai ghép AI (HAH-Delphi) để lọc và xây dựng hệ thống tiêu chí một cách khách quan ^^; (2) áp dụng các phương pháp giảm thiểu tải lượng so sánh như BWM, SWARA hoặc DEMATEL để tính toán trọng số nhất quán và bóc tách cấu trúc nhân quả ^^; (3) mô hình hóa sự bất định bằng toán học mờ mở rộng (Pythagorean, Neutrosophic) hoặc hệ thống xám để bảo toàn tối đa tri thức chuyên gia ^^; và (4) thực hiện xếp hạng phương án bằng các thuật toán có độ ổn định cao như MARCOS để loại bỏ hoàn toàn các rủi ro đảo ngược thứ hạng.^^ Việc nắm vững bản chất triết học và kỹ thuật của các trường phái này là điều kiện tiên quyết để các nhà nghiên cứu kiến tạo nên các quyết định quản trị có tính minh bạch, nhất quán và khả thi cao trong thực tiễn phức tạp.^^
