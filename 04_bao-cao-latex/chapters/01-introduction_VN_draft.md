# Chương 1 — Giới thiệu (Bản nháp tiếng Việt để nhóm review)

> Bản này KHÔNG đưa vào luồng biên dịch LaTeX. Bản tiếng Anh chính thức nằm ở `01-introduction.tex`, được viết lại độc lập (không dịch máy) từ nội dung dưới đây. Trích dẫn ghi theo APA để đối chiếu; khi chuyển sang `.tex` sẽ thay bằng `\textcite{}` / `\parencite{}`.

## 1.1. Bối cảnh và động lực nghiên cứu

Máy tính xách tay đã trở thành công cụ lao động cơ bản trong phần lớn các ngành nghề, kéo theo quy mô tiêu thụ liên tục mở rộng ở cấp độ toàn cầu. Thống kê được Sönmez Çakır và Pekkaya (2020) tổng hợp cho thấy đã có 161,6 triệu máy tính xách tay được bán ra trong năm 2017, cao hơn khoảng 65% so với lượng máy tính để bàn. Xu hướng này tiếp tục được củng cố trong giai đoạn đại dịch, khi Gaur (2023) ghi nhận sản lượng tiêu thụ tăng lên 218 triệu máy vào năm 2020 (tương ứng mức tăng 26%) và đạt 225 triệu máy trong năm 2021. Nhu cầu duy trì ở mức cao đi kèm với vòng đời sản phẩm tương đối ngắn, thường được ước tính khoảng năm năm (Sönmez Çakır & Pekkaya, 2020), khiến việc lựa chọn thiết bị trở thành một quyết định lặp lại đối với cả cá nhân lẫn tổ chức.

Đi cùng với quy mô thị trường là sự phân mảnh nhanh chóng của danh mục sản phẩm. Mỗi thế hệ máy bổ sung thêm các cấu hình và tính năng mới, làm gia tăng số lượng thương hiệu, mẫu mã và biến thể mà người mua phải cân nhắc (Sönmez Çakır & Pekkaya, 2020). Người mua vì thế phải đối chiếu đồng thời nhiều thông số kỹ thuật vốn được biểu diễn trên các thang đo khác nhau và thường xung đột với nhau, chẳng hạn giữa hiệu năng và thời lượng pin, hay giữa độ bền và trọng lượng. Trong điều kiện đó, việc dựa thuần túy vào kinh nghiệm hoặc so sánh trực giác khó bảo đảm tính nhất quán, bởi các tiêu chí không thể quy đổi trực tiếp về một đơn vị chung để đánh đổi.

Bài toán lựa chọn với nhiều tiêu chí xung đột thuộc phạm vi của các phương pháp ra quyết định đa tiêu chí (Multi-Criteria Decision-Making — MCDM). Rà soát hệ thống của Basílio và cộng sự (2022) cho thấy nhóm phương pháp này được ứng dụng rộng rãi qua nhiều lĩnh vực, trong đó Analytic Hierarchy Process (AHP) và Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) nằm trong số các kỹ thuật được sử dụng phổ biến nhất, một kết luận cũng được Zyoud và Fuchs-Hanusch (2017) ghi nhận qua phân tích trắc lượng thư mục. Việc kết hợp AHP để xác định trọng số tiêu chí và TOPSIS để xếp hạng phương án là một tổ hợp được vận dụng thường xuyên trong thực tiễn nghiên cứu (Tighnavard Balasbaneh et al., 2025), nhờ khả năng tách biệt giữa bước lượng hóa mức độ quan trọng của tiêu chí và bước đánh giá các phương án cụ thể.

## 1.2. Phát biểu bài toán

Nghiên cứu này đặt trọng tâm vào tình huống một nhân viên văn phòng tại Việt Nam cần lựa chọn máy tính xách tay phục vụ công việc. Trong bối cảnh này, giá cả không được cố định trước mà tham gia như một tiêu chí định khung: ngân sách thu mua của khối văn phòng thường dao động trong khoảng 8 đến 15 triệu đồng, qua đó giới hạn không gian lựa chọn trước khi người mua cân nhắc các thông số phần cứng còn lại. Ràng buộc chi phí này đặt giá cả vào thế đánh đổi thường trực với hiệu năng, độ bền, tính di động và trải nghiệm sử dụng, khiến quyết định cuối cùng phụ thuộc vào cách cân bằng giữa các nhóm tiêu chí thay vì tối ưu một chỉ tiêu đơn lẻ.

Mặc dù lựa chọn máy tính xách tay đã được nghiên cứu bằng công cụ MCDM, các công trình hiện có bộc lộ hai khoảng trống đáng chú ý đối với bối cảnh Việt Nam. Thứ nhất, phần lớn nghiên cứu về lựa chọn laptop dừng lại ở AHP hoặc các biến thể mờ đơn lẻ để xếp hạng tiêu chí (Sönmez Çakır & Pekkaya, 2020; Elnatan & Tannady, n.d.), trong khi mô hình tích hợp AHP–TOPSIS chuẩn lại chủ yếu được kiểm chứng trên đối tượng điện thoại di động (Lam et al., 2023); việc áp dụng tổ hợp này trên dữ liệu laptop thực tế của thị trường Việt Nam vẫn còn hạn chế. Thứ hai, thứ tự ưu tiên tiêu chí rút ra từ các nghiên cứu quốc tế không hoàn toàn tương thích với điều kiện sử dụng trong nước; chẳng hạn, thời lượng pin thường được xác định là tiêu chí có trọng số cao nhất trong tài liệu nước ngoài (Lam et al., 2023), nhưng dữ liệu phỏng vấn chuyên gia trong nước cho thấy mức 4 đến 7 giờ đã đáp ứng nhu cầu do hạ tầng điện phổ biến tại văn phòng, đồng thời tiêu chí trọng lượng lại được nhấn mạnh hơn do đặc thù di chuyển bằng xe máy. Từ hai khoảng trống này, nghiên cứu hướng đến việc xây dựng và vận dụng một mô hình AHP–TOPSIS được hiệu chỉnh theo thực tiễn Việt Nam để hỗ trợ quyết định lựa chọn laptop cho nhân viên văn phòng.

## 1.3. Khoảng trống nghiên cứu và đóng góp

Hai hạn chế nêu trên xác định không gian mà nghiên cứu này chiếm giữ. Các công trình chọn laptop trước đây hoặc dừng ở bước xác định trọng số tiêu chí mà không xếp hạng phương án cụ thể (Sönmez Çakır & Pekkaya, 2020), hoặc áp dụng mô hình tích hợp AHP–TOPSIS cho nhóm sản phẩm khác ngoài laptop (Lam et al., 2023); hơn nữa, chưa có nghiên cứu nào hiệu chỉnh bộ tiêu chí và thứ tự ưu tiên theo điều kiện làm việc của nhân viên văn phòng Việt Nam. Nhằm lấp các khoảng trống này, nghiên cứu đóng góp trên hai phương diện. Thứ nhất, nghiên cứu xây dựng một bộ tiêu chí gắn với bối cảnh cụ thể cho laptop văn phòng tại Việt Nam bằng cách kết hợp tổng quan tài liệu với phỏng vấn chuyên gia, làm rõ những điểm mà thực tiễn trong nước lệch khỏi thứ tự ưu tiên trong tài liệu quốc tế. Thứ hai, nghiên cứu vận hành một mô hình quyết định AHP–TOPSIS hoàn chỉnh trên dữ liệu thị trường thực tế, dùng AHP để xác định trọng số tiêu chí và TOPSIS để xếp hạng các mẫu laptop cụ thể, qua đó chuyển bộ tiêu chí đã hiệu chỉnh thành một quy trình xếp hạng có thể áp dụng.

## 1.4. Mục tiêu và câu hỏi nghiên cứu

Xuất phát từ bài toán trên, nghiên cứu theo đuổi ba mục tiêu tương ứng với ba giai đoạn triển khai. Giai đoạn thứ nhất nhằm xác lập một bộ tiêu chí đánh giá phù hợp với nhân viên văn phòng Việt Nam, thông qua tổng quan tài liệu kết hợp phỏng vấn chuyên gia. Giai đoạn thứ hai lượng hóa mức độ quan trọng của các tiêu chí bằng phương pháp AHP dựa trên dữ liệu so sánh cặp thu thập từ chuyên gia. Giai đoạn thứ ba vận dụng TOPSIS để xếp hạng các mẫu laptop thực tế trên thị trường theo bộ trọng số đã xác định. Ba mục tiêu này được cụ thể hóa thành ba câu hỏi nghiên cứu:

1. **CH1:** Những tiêu chí nào phù hợp để đánh giá máy tính xách tay cho nhân viên văn phòng tại Việt Nam?
2. **CH2:** Trọng số của các tiêu chí đó là bao nhiêu khi được xác định bằng phương pháp AHP?
3. **CH3:** Mẫu laptop nào là lựa chọn phù hợp nhất theo bộ tiêu chí và trọng số đã xác lập khi xếp hạng bằng TOPSIS?

## 1.5. Phạm vi và cấu trúc báo cáo

Nghiên cứu giới hạn ở phân khúc máy tính xách tay văn phòng trên thị trường Việt Nam, với dữ liệu sản phẩm được thu thập từ nhà bán lẻ CellphoneS tại thời điểm khảo sát. Đối tượng thụ hưởng của mô hình là nhân viên văn phòng, phân biệt với các nhóm người dùng có nhu cầu chuyên biệt như thiết kế đồ họa hay chơi game. Bộ tiêu chí được sử dụng gồm mười bốn tiêu chí thuộc sáu nhóm, phản ánh các khía cạnh kinh tế, năng lực phần cứng, thiết kế và trải nghiệm, tính di động và độ bền, tiện ích hệ sinh thái, cùng giá trị niềm tin và hậu mãi. Nghiên cứu không hướng đến việc tổng quát hóa cho mọi phân khúc người dùng hay mọi kênh phân phối, mà tập trung vào tình huống ra quyết định đã xác định.

Phần còn lại của báo cáo được tổ chức thành năm chương. Chương 2 tổng quan cơ sở lý thuyết về MCDM cùng hai phương pháp AHP và TOPSIS, đồng thời điểm lại các nghiên cứu trước về lựa chọn laptop nhằm định vị khoảng trống. Chương 3 trình bày phương pháp nghiên cứu, bao gồm quy trình xây dựng tiêu chí, thu thập dữ liệu và các bước tính toán. Chương 4 báo cáo kết quả về trọng số tiêu chí và thứ hạng các phương án. Chương 5 thảo luận ý nghĩa của kết quả trong đối sánh với tài liệu hiện có, và Chương 6 tổng kết đóng góp cùng những giới hạn của nghiên cứu.

---

### Nguồn trích dẫn dùng trong chương (citekey ↔ APA)
- `sonmez_cakir_determination_2020` — Sönmez Çakır & Pekkaya (2020)
- `gaur_application_2023` — Gaur (2023)
- `basilio_systematic_2022` — Basílio et al. (2022)
- `zyoud_bibliometric-based_2017` — Zyoud & Fuchs-Hanusch (2017)
- `tighnavard_balasbaneh_systematic_2025` — Tighnavard Balasbaneh et al. (2025)
- `elnatan_alternatif_nodate` — Elnatan & Tannady (n.d.)
- `weng_siew_lam_evaluation_2023` — Lam et al. (2023)
