# Sổ tay vận hành dự án MADM/MCDM - Bộ tiêu chí ra quyết định mua laptop

> **Trạng thái:** bản nháp chờ nhóm trưởng duyệt. Cấu trúc thư mục mô tả trong tài liệu này sẽ được khởi tạo sau khi kế hoạch tổng thể ([KE-HOACH-DU-AN.md](KE-HOACH-DU-AN.md)) được chốt.
>
> **Cập nhật:** 2026-07-04

## 1. Dự án này là gì

Đây là đồ án nhóm môn Logistics Management. Nhóm xây dựng bộ tiêu chí ra quyết định mua laptop qua ba giai đoạn nghiên cứu, gồm tổng quan tài liệu khoa học, phỏng vấn chuyên gia và khảo sát diện rộng. Sau đó nhóm dùng phương pháp AHP để tính trọng số các tiêu chí, rồi dùng TOPSIS để xếp hạng các mẫu laptop thực tế trên thị trường trong tình huống giả định "nhân viên văn phòng cần mua laptop phục vụ công việc". Dự án không khóa trước một mức giá cụ thể; giá cả/ngân sách được xem là một tiêu chí hoặc một rule lọc dữ liệu sẽ chốt riêng nếu cần.

Sản phẩm nộp gồm hai thứ. Thứ nhất là báo cáo học thuật viết bằng tiếng Anh, soạn bằng LaTeX. Thứ hai là bộ slide thuyết trình tiếng Anh. Toàn bộ quá trình làm việc nội bộ của nhóm vẫn dùng tiếng Việt, chỉ hai sản phẩm cuối mới chuyển sang tiếng Anh, và bản tiếng Anh được viết lại độc lập chứ không dịch máy từng câu.

## 2. Bản đồ thư mục

Nguyên tắc xuyên suốt của hệ thống thư mục là dữ liệu chảy một chiều, từ thô đến xử lý rồi đến bản nộp. Số thứ tự đầu tên thư mục phản ánh đúng trình tự pipeline nghiên cứu, nhìn vào là thấy được dự án đang đi đến đâu.

| Muốn tìm... | Vào thư mục |
|---|---|
| Kế hoạch, timeline, biên bản họp, brainstorm | `00_quan-ly-du-an\` |
| Bài báo khoa học, ghi chú tổng hợp tiêu chí | `01_tai-lieu-tham-khao\` |
| Dữ liệu gốc (khảo sát, phỏng vấn, dữ liệu laptop crawl về) | `02_du-lieu-tho\` |
| File tính toán đang làm dở (Likert, AHP, TOPSIS) | `03_phan-tich\` |
| Báo cáo LaTeX tiếng Anh | `04_bao-cao-latex\` |
| Slide thuyết trình | `05_slide\` |
| Bản nộp cuối cùng | `06_nop-bai\` |
| Các bản sao lưu ZIP theo mốc | `07_sao-luu\` |
| Kho tàng kiến thức AI & Công nghệ | `08_new_knowledge\` |
| Công cụ AI hỗ trợ (skill) | `.claude\skills\` (Claude Code) / `.codex\skills\` (Codex) |

Cây thư mục đầy đủ:

```
d:\LogManagement\
├── README.md                      ← tài liệu này
├── KE-HOACH-DU-AN.md              ← kế hoạch tổng thể
├── 00_quan-ly-du-an\
│   ├── brainstorm.md
│   ├── timeline.md                ← mốc thời gian từng phase, nhóm điền deadline
│   └── bien-ban-hop\
├── 01_tai-lieu-tham-khao\
│   ├── MADM.pdf
│   ├── bai-bao\                   ← PDF paper, tên dạng TacGia_Nam_TuKhoa.pdf
│   └── tong-hop-tieu-chi.md       ← bảng trích tiêu chí từ từng paper
├── 02_du-lieu-tho\                ← vùng ĐÓNG BĂNG
│   ├── _HUONG-DAN.md
│   ├── inbox\                     ← file thành viên gửi về, chưa phân loại
│   ├── khao-sat\
│   ├── phong-van\
│   └── laptop-thi-truong\
├── 03_phan-tich\                  ← vùng làm việc
│   ├── tieu-chi\                  ← likert-thu-thap-phan-tich.xlsx
│   ├── ahp\                       ← ahp-thu-thap-chuyen-gia.xlsx
│   ├── du-lieu-sach\
│   └── topsis\
├── 04_bao-cao-latex\
│   ├── main.tex
│   ├── chapters\  ├── figures\  ├── tables\
│   └── references.bib
├── 05_slide\
│   └── outline-slide.md
├── 06_nop-bai\                    ← vùng THIÊNG LIÊNG
├── 07_sao-luu\
├── 08_new_knowledge\              ← kho tàng kiến thức AI & Công nghệ
├── AGENTS.md                      ← luật dự án (dùng chung Claude Code + Codex)
├── CLAUDE.md                      ← điểm vào Claude Code (import @AGENTS.md)
├── .claude\
│   ├── skills\                    ← các module kỹ năng (Claude Code tự nạp)
│   └── agents\                    ← subagent (skill-smith, data-gatherer, office-docs)
└── .codex\
    └── skills\                    ← mirror cho Codex (không có subagent, đọc trực tiếp)
```

## 3. Ba luật vàng

Ba luật này là hợp đồng làm việc của cả nhóm. Vi phạm luật nào cũng dẫn đến hậu quả giống nhau là mất dấu dữ liệu gốc và không truy lại được kết quả.

**Luật 1 - File thô là bất khả xâm phạm.** Mọi file đưa vào `02_du-lieu-tho\` được coi là đóng băng vĩnh viễn. Muốn xử lý, làm sạch hay tính toán thì copy sang `03_phan-tich\` rồi làm trên bản copy. Lý do rất đơn giản, nếu kết quả tính sai thì luôn còn bản gốc để làm lại từ đầu.

**Luật 2 - Vùng nộp bài chỉ chứa bản nộp.** `06_nop-bai\` không bao giờ chứa bản nháp. File chỉ được copy vào đây khi cả nhóm đã duyệt và đó chính xác là thứ sẽ nộp cho giảng viên.

**Luật 3 - Mọi file từ thành viên đi qua inbox.** Thành viên gửi file qua kênh chat hay Drive, nhóm trưởng lưu vào `02_du-lieu-tho\inbox\` trước, sau đó mới đổi tên đúng quy ước và phân loại vào thư mục đích. Cách này tránh được tình trạng mỗi người bỏ file một nơi.

## 4. Quy ước đặt tên file

Bản nháp và file làm việc đặt tên theo mẫu sau, ngày đứng trước để thư mục tự sắp xếp theo thời gian:

```
YYYY-MM-DD_<ten-tai-lieu>_v<X.Y>_<trangthai>_<tennguoi>.<duoi>

Ví dụ: 2026-07-10_kich-ban-phong-van_v2.1_draft_an.docx
```

Cách dùng từng thành phần:

- `vX.Y` - X tăng khi thay đổi lớn (viết lại cả tài liệu, đổi phương pháp), Y tăng khi sửa nhỏ.
- `<trangthai>` - `draft` là đang viết, `review` là chờ nhóm góp ý, `final` là đã chốt. File đã `final` không sửa nữa, muốn sửa phải tạo phiên bản mới.
- Bản cũ không xóa mà chuyển vào thư mục con `_cu\` ngay tại chỗ, để thư mục làm việc chỉ hiện bản mới nhất.
- Cấm tuyệt đối các tên kiểu `final_final2.docx`, `bansua_moinhat.docx`.

Riêng file PDF bài báo khoa học đặt tên `TacGia_Nam_TuKhoa.pdf`, ví dụ `Nguyen_2023_LaptopSelectionAHP.pdf`, để khớp với khóa trích dẫn trong file `references.bib`.

## 5. Workflow bảy phase

Dự án chia thành bảy phase nối tiếp nhau, đầu ra của phase trước là đầu vào của phase sau. Mỗi task có mã số để nhóm trưởng phân công. Cuối mỗi phase có tiêu chí hoàn thành (Definition of Done, viết tắt DoD), đạt đủ mới chuyển phase và tạo một bản sao lưu ZIP.

### Phase 0 - Khởi động

Mục tiêu của phase này là cả nhóm hiểu giống nhau về đề bài và cách làm việc trước khi bắt tay vào nghiên cứu.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T0.1 | Gặp giảng viên chốt phạm vi đề tài, xin rubric chấm điểm và yêu cầu độ dài báo cáo, số slide | `00_quan-ly-du-an\` |
| T0.2 | Điền deadline từng phase vào `timeline.md`, tính lùi từ ngày nộp | `00_quan-ly-du-an\timeline.md` |
| T0.3 | Cả nhóm đọc README này, thống nhất quy ước đặt tên và kênh gửi file | Biên bản họp |
| T0.4 | Phân công task các phase dựa trên hệ thống mã T | `timeline.md` |

**DoD:** rubric đã lưu, timeline có ngày cụ thể, mọi thành viên xác nhận đã đọc README.

### Phase 1 - Tổng quan tài liệu (Literature review)

Phase này thu thập tiêu chí từ các nghiên cứu đã công bố. Nguyên tắc quan trọng nhất là ghi đủ thông tin trích dẫn ngay lúc đọc, không để dồn đến lúc viết báo cáo mới truy lại nguồn.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T1.1 | Xây chuỗi từ khóa tìm kiếm (laptop selection criteria, AHP, TOPSIS, MCDM, consumer electronics purchase decision) | `01_tai-lieu-tham-khao\` |
| T1.2 | Thu thập 10-15 bài báo từ nguồn uy tín (ScienceDirect, Springer, Scopus, Google Scholar), ưu tiên bài có DOI | `01_tai-lieu-tham-khao\bai-bao\` |
| T1.3 | Đọc từng bài, trích tiêu chí vào bảng tổng hợp kèm đủ tác giả, năm, tạp chí, DOI, số trang | `tong-hop-tieu-chi.md` |
| T1.4 | Nhập nguồn vào `references.bib` ngay khi đọc xong từng bài | `04_bao-cao-latex\references.bib` |
| T1.5 | Gộp tiêu chí trùng lặp, phân nhóm (hiệu năng, giá, thiết kế, dịch vụ...), lập danh sách tiêu chí sơ bộ | `03_phan-tich\tieu-chi\` |
| T1.6 | Họp nhóm rà soát và chốt danh sách sơ bộ | Biên bản họp |

**Công cụ:** Scholar Gateway (tìm paper), skill `professional-writing` mô-đun `research/literature.md` (quy trình trích metadata), skill `pdf` (trích bảng từ paper).

**DoD:** có ít nhất 10 paper trong thư mục, bảng tổng hợp đầy đủ metadata cho từng tiêu chí, file .bib chạy không lỗi.

### Phase 2 - Phỏng vấn chuyên gia

Bộ tiêu chí từ tài liệu quốc tế chưa chắc khớp với bối cảnh Việt Nam, nên cần chuyên gia hiệu chỉnh. Số lượng chuyên gia ít (3-5 người) không đủ đại diện thống kê, vì vậy kết quả phase này chỉ dùng để điều chỉnh danh sách tiêu chí chứ không dùng để kết luận.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T2.1 | Thiết kế kịch bản phỏng vấn bán cấu trúc từ danh sách tiêu chí sơ bộ | `02_du-lieu-tho\phong-van\` |
| T2.2 | Chọn 3-5 chuyên gia theo lấy mẫu đa cực biến thiên (người bán laptop, kỹ thuật viên, nhân viên văn phòng...) | Biên bản họp |
| T2.3 | Tiến hành phỏng vấn, ghi chú, xin phép nếu ghi âm | `02_du-lieu-tho\phong-van\` |
| T2.4 | Tổng hợp ý kiến, điều chỉnh danh sách tiêu chí (thêm, bớt, đổi tên) | `03_phan-tich\tieu-chi\` |
| T2.5 | Ghi lại lý do của từng thay đổi để sau này viết chương Methodology | `03_phan-tich\tieu-chi\` |

**DoD:** đủ số cuộc phỏng vấn, ghi chú đã lưu vào vùng dữ liệu thô, danh sách tiêu chí sau hiệu chỉnh kèm lý do thay đổi.

### Phase 3 - Khảo sát Likert

Khảo sát diện rộng giúp sàng lọc tiêu chí bằng dữ liệu định lượng. Ngưỡng giữ hay loại tiêu chí phải có nguồn trích dẫn chống lưng, không tự đặt tùy tiện.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T3.1 | Dựng Google Form thang Likert 5 điểm từ danh sách tiêu chí sau phỏng vấn | Link lưu trong biên bản họp |
| T3.2 | Chạy thử với 5-10 người, sửa câu chữ khó hiểu trước khi phát chính thức | Biên bản họp |
| T3.3 | Xác định cỡ mẫu mục tiêu và kênh phát (nhóm sinh viên, hội nhóm nhân viên văn phòng...) | Biên bản họp |
| T3.4 | Thu thập phản hồi, xuất CSV | `02_du-lieu-tho\khao-sat\` |
| T3.5 | Dán dữ liệu vào file Excel phân tích, đọc mean và độ lệch chuẩn từng tiêu chí | `03_phan-tich\tieu-chi\likert-thu-thap-phan-tich.xlsx` |
| T3.6 | Chốt ngưỡng giữ/loại (mặc định 3.5, kèm nguồn trích dẫn cho ngưỡng), chốt bộ tiêu chí cuối cùng | `03_phan-tich\tieu-chi\` |

**Công cụ:** skill `likert-analysis` (sẽ tạo), file Excel có công thức sẵn.

**DoD:** đạt cỡ mẫu mục tiêu, bảng phân tích mô tả hoàn chỉnh, bộ tiêu chí cuối được cả nhóm duyệt. Đây là mốc quan trọng nhất nửa đầu dự án, vì mọi thứ phía sau đều xây trên bộ tiêu chí này.

### Phase 4 - Tính trọng số bằng AHP

AHP chuyển phán đoán chủ quan "tiêu chí nào quan trọng hơn" thành trọng số định lượng. Điểm chết người của phase này là chỉ số nhất quán CR, vượt 0.1 là ma trận không dùng được và phải nhờ người điền xem lại.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T4.1 | Cập nhật file Excel AHP theo đúng số tiêu chí đã chốt ở Phase 3 | `03_phan-tich\ahp\ahp-thu-thap-chuyen-gia.xlsx` |
| T4.2 | Gửi bảng so sánh cặp cho chuyên gia hoặc nhóm điền (thang Saaty 1-9, có hướng dẫn trong file) | `03_phan-tich\ahp\` |
| T4.3 | Tính trọng số và CR cho từng ma trận. Ma trận nào CR vượt 0.1 thì gửi lại người điền kèm chỉ dẫn cặp nào đang mâu thuẫn | `03_phan-tich\ahp\` |
| T4.4 | Tổng hợp các ma trận hợp lệ bằng trung bình nhân (geometric mean), ra bộ trọng số cuối | `03_phan-tich\ahp\` |
| T4.5 | Xuất bảng trọng số dạng LaTeX (booktabs) để cắm thẳng vào báo cáo | `04_bao-cao-latex\tables\` |

**Công cụ:** skill `mcdm-toolkit` (sẽ tạo), file Excel tự tính CR và báo đỏ khi vượt ngưỡng.

**DoD:** mọi ma trận sử dụng đều có CR không vượt 0.1, bảng trọng số cuối kèm file tính toán tái lập được.

### Phase 5 - Dữ liệu laptop và xếp hạng TOPSIS

Phase này trả lời câu hỏi của tình huống giả định. Dữ liệu thị trường thay đổi liên tục nên mọi thứ crawl về đều phải kèm ngày thu thập, coi như ảnh chụp thị trường tại một thời điểm.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T5.1 | Crawl danh sách laptop văn phòng từ CellphoneS kèm thông số (AI hỗ trợ), ghi ngày crawl và phạm vi lọc nếu có vào tên file | `02_du-lieu-tho\laptop-thi-truong\` |
| T5.2 | Tra điểm benchmark cho CPU và GPU từ một nguồn duy nhất (PassMark), ghi ngày truy cập | `02_du-lieu-tho\laptop-thi-truong\` |
| T5.3 | Xây rubric chấm điểm cho tiêu chí định tính (thương hiệu, ngoại hình) trước khi chấm, cả nhóm chấm độc lập rồi lấy trung bình | `03_phan-tich\du-lieu-sach\` |
| T5.4 | Làm sạch dữ liệu, ghép benchmark, dựng ma trận quyết định hoàn chỉnh | `03_phan-tich\du-lieu-sach\` |
| T5.5 | Chạy TOPSIS với trọng số từ Phase 4, ra bảng xếp hạng | `03_phan-tich\topsis\` |
| T5.6 | Phân tích độ nhạy, thử thay đổi trọng số xem thứ hạng có đổi không | `03_phan-tich\topsis\` |
| T5.7 | Diễn giải kết quả, viết ghi chú vì sao máy đứng đầu thắng, chuẩn bị luận giải "vì sao giai đoạn này dùng TOPSIS thay vì AHP" | `03_phan-tich\topsis\` |

**Công cụ:** skill `data-pipeline` (crawl + làm sạch) và `mcdm-toolkit`, skill `xlsx`.

**DoD:** ma trận quyết định đầy đủ nguồn gốc từng con số, bảng xếp hạng kèm phân tích độ nhạy, ghi chú diễn giải đã viết xong.

### Phase 6 - Báo cáo và slide

Đây là phase duy nhất làm việc bằng tiếng Anh. Quy trình viết theo skill `professional-writing` gồm hai lượt, viết nháp tiếng Việt trước để cả nhóm góp ý nhanh, sau đó viết lại bản tiếng Anh độc lập từ dàn ý và dữ liệu đã chốt.

| Mã | Task | Kết quả lưu tại |
|---|---|---|
| T6.1 | Viết nháp từng chương bằng tiếng Việt theo sườn có sẵn trong `chapters\` | `04_bao-cao-latex\chapters\` (nhánh nháp) |
| T6.2 | Viết lại bản tiếng Anh độc lập từng chương, không dịch máy từng câu | `04_bao-cao-latex\chapters\` |
| T6.3 | Dựng hình và bảng từ kết quả Phase 4 và 5 | `figures\`, `tables\` |
| T6.4 | Rà soát trích dẫn, đối chiếu từng citation với `references.bib` | `04_bao-cao-latex\` |
| T6.5 | Biên dịch XeLaTeX + biber, sửa lỗi cú pháp, xuất PDF hoàn chỉnh | `04_bao-cao-latex\` |
| T6.6 | Dựng slide tiếng Anh theo `outline-slide.md`, ưu tiên hình và số liệu thay vì chữ | `05_slide\` |
| T6.7 | Tổng duyệt thuyết trình, canh thời gian, phân vai người nói | Biên bản họp |
| T6.8 | Chạy checklist rà soát cuối, copy bản nộp vào `06_nop-bai\`, tạo ZIP sao lưu cuối | `06_nop-bai\`, `07_sao-luu\` |

**Công cụ:** skill `professional-writing` (viết, citation-check, latex-check), skill `pptx` và `dataviz` (slide).

**DoD:** PDF báo cáo biên dịch không lỗi, mọi trích dẫn khớp danh mục, slide đã tổng duyệt, `06_nop-bai\` chứa đúng bộ file nộp.

## 6. Sao lưu và quản lý phiên bản

Chiến lược sao lưu gồm ba lớp, mỗi lớp chống một loại rủi ro khác nhau.

**Lớp 1 - Quy ước đặt tên** (mục 4) chống rủi ro ghi đè nhầm bản cũ khi nhiều người cùng sửa một tài liệu.

**Lớp 2 - Git & GitHub** chống rủi ro "hôm qua còn chạy được, hôm nay lỗi mà không biết đã sửa gì". Hãy tham khảo tài liệu [02_kien-thuc-he-thong.md](08_new_knowledge/02_kien-thuc-he-thong.md) để biết cách quản lý đa vũ trụ qua Add, Commit và Push.

**Lớp 3 - Snapshot ZIP theo mốc** chống rủi ro hỏng máy, mất ổ cứng. Kết thúc mỗi phase, nén toàn bộ workspace (trừ `.claude\skills\`, cache model và file tạm) thành file đặt trong `07_sao-luu\` theo mẫu `YYYY-MM-DD_phase<N>_<ten-moc>.zip`, sau đó upload thủ công lên Google Drive của nhóm. Thư mục này chỉ chứa ZIP, tuyệt đối không giải nén đè ngược lại workspace.

### Checklist kết thúc phase

- [ ] Mọi task của phase đạt DoD
- [ ] File thô liên quan đã nằm trong `02_du-lieu-tho\` đúng chỗ
- [ ] Nhờ AI "lưu phiên bản báo cáo" nếu phase có đụng vào `04_bao-cao-latex\`
- [ ] Tạo ZIP snapshot vào `07_sao-luu\`
- [ ] Upload ZIP lên Google Drive nhóm
- [ ] Cập nhật `timeline.md` (đánh dấu phase xong, xác nhận deadline phase sau)

## 7. Hướng dẫn biên dịch báo cáo LaTeX

Báo cáo dùng engine XeLaTeX với biber. Thay vì chạy lệnh thủ công rườm rà, dự án đã được cấu hình tự động trên nền tảng **Antigravity IDE**:

1. Cài đặt extension **LaTeX Workshop** (`James-Yu.latex-workshop`).
2. Hệ thống đã được cấu hình sẵn trong `.vscode/settings.json` để tự động dùng `xelatex` + `biber`.
3. Bạn chỉ cần mở file `.tex`, bấm biểu tượng **View PDF** (hình kính lúp) ở góc phải. Mỗi khi bấm `Ctrl+S` (Lưu), PDF sẽ tự động biên dịch và xem trước ngay lập tức (Live Preview).

## 8. Công cụ AI của dự án

Dự án chạy song song **Claude Code** và **Codex**. Skill nằm ở `.claude\skills\<tên>\SKILL.md` — Claude Code tự nạp (autoload), Codex đọc trực tiếp khi được `AGENTS.md` mục 5 trỏ tới. Ba việc tốn ngữ cảnh (tạo/audit skill, crawl dữ liệu, xử lý Office file dài) tách thành **subagent** ở `.claude\agents\` (chạy phòng riêng); Codex không có cơ chế subagent nên dùng mirror ở `.codex\skills\<tên>\`. Luật dự án dùng chung nằm ở `AGENTS.md` gốc — sửa luật thì sửa ở đó, không rải rác.

| Skill / Subagent | Dùng cho | Nguồn |
|---|---|---|
| `task-processor` (skill) | Điểm vào mặc định: phân tích yêu cầu, điều phối skill khác | Tạo riêng cho dự án |
| `professional-writing` (skill) | Viết học thuật/blog chuyên nghiệp, đọc sâu paper, ép buộc trích dẫn (citation-check) | Tạo riêng cho dự án |
| `mcdm-toolkit`, `data-pipeline`, `likert-analysis` (skill) | Tính AHP/TOPSIS, thao tác dữ liệu lẻ, phân tích khảo sát | Tạo riêng cho dự án (kèm script đã kiểm thử + file mẫu trong `examples\`) |
| `data-gatherer` (subagent) | Crawl/làm mới dữ liệu laptop khối lượng lớn (CellphoneS + PassMark) | Tạo riêng cho dự án |
| `pptx`, `xlsx`, `pdf` (skill) | Dựng slide, xử lý Excel, trích bảng từ paper PDF | Hệ sinh thái skill công khai |
| `officecli` (skill) | Tạo/đọc/sửa/QA file .docx/.xlsx/.pptx qua CLI | Adapter cho binary ngoài |
| `office-docs` (subagent) | Xử lý Office file dài/nhiều file cần cô lập ngữ cảnh | Tạo riêng cho dự án |
| `supply-chain-consultant` (skill) | Tư vấn chuyên môn logistics/SCM | Có sẵn |
| `skill-smith` (subagent), bọc `skill-creator`/`writing-skills`/`audit-skills` | Tạo, viết chuẩn, kiểm định an toàn skill | Có sẵn |
| `project-switch` (skill) | Bối cảnh hoá toolkit khi bê sang project mới | Tạo riêng cho dự án |

Chi tiết phân tích và lý do chọn từng skill nằm trong [KE-HOACH-DU-AN.md](KE-HOACH-DU-AN.md), Phần 3.

## 9. Kho tàng kiến thức Vibecoding (08_new_knowledge)

Đây là "bộ não thứ hai" đúc kết lại các bài học, lỗi kỹ thuật, và kiến thức mới sinh ra trong quá trình thực hiện dự án. Vì đối tượng đọc là người có background Non-IT, tất cả bài viết trong thư mục `08_new_knowledge\` BẮT BUỘC tuân thủ:
- **Cấu trúc 5 bước:** Hook (Nỗi đau) -> Analogy (Ẩn dụ đời thường) -> Root Cause (Bản chất học thuật) -> Solution (Cách giải quyết) -> Citations (Trích dẫn).
- **Văn phong:** Sử dụng ngôn từ đồng cảm, tránh lạm dụng thuật ngữ (de-jargonize), luôn có mô hình tư duy (Mental Model) đi kèm.
- **Quy trình:** Phải được tạo bởi skill `professional-writing` để đảm bảo chất lượng nghiên cứu, biên tập và trích dẫn chuẩn mực.
(Xem chi tiết Luật vàng số 5 trong file `AGENTS.md`, mục 8)

## 10. Hướng dẫn Prompting cho User (Best Practices)

Để giao việc cho Agent một cách hiệu quả, đặc biệt trong các tác vụ viết học thuật và báo cáo (Phase 1 & Phase 6), người dùng (User) nên sử dụng các bộ prompt mẫu dưới đây nhằm tránh việc AI trả về kết quả quá "máy móc", lạm dụng gạch đầu dòng, hoặc sai lệch về chuẩn mực trích dẫn.

### 10.1. Mẫu Prompt viết/sửa Literature Review (Tiếng Việt)
> *"Sử dụng skill @[.claude/skills/professional-writing], viết [hoặc sửa lại] phần [Tên nội dung] theo chuẩn học thuật. Yêu cầu bắt buộc: KHÔNG dùng gạch đầu dòng hay đánh nhãn in đậm kiểu máy móc. Hãy viết thành các đoạn văn nối tiếp mượt mà, phân tích rõ sự đồng thuận/trái chiều (agreements/disagreements) của các tác giả. BẮT BUỘC thực hiện cross-ref check để đảm bảo 100% in-text citation khớp với danh mục References ở cuối bài."*

### 10.2. Mẫu Prompt biên dịch sang Tiếng Anh (Phase 6)
> *"Viết lại phần [Tên file nháp tiếng Việt] sang tiếng Anh học thuật để dùng cho báo cáo LaTeX. Yêu cầu bắt buộc: Dịch độc lập theo ý, KHÔNG dịch word-by-word. Linh hoạt thay đổi cấu trúc câu và thì ngữ pháp (Tenses) cho tự nhiên. Các trích dẫn phải được tích hợp mượt mà vào câu (ví dụ: Smith et al. (2024) argued that...). Cuối bài bắt buộc check lại Cross-Reference với file .bib."*

*Lưu ý: Bạn có thể copy-paste thẳng các câu lệnh này vào chat để kích hoạt "chế độ nghiêm ngặt" của Agent.*
