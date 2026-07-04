# Dự án MADM/MCDM - Bộ tiêu chí ra quyết định mua laptop (Logistics Management)

Đồ án nhóm: xây bộ tiêu chí mua laptop (literature → phỏng vấn chuyên gia → khảo sát Likert), tính trọng số bằng AHP, xếp hạng bằng TOPSIS. Sản phẩm nộp: báo cáo LaTeX tiếng Anh + slide tiếng Anh. Ngôn ngữ làm việc nội bộ: tiếng Việt.

## Kho skill và định tuyến (bắt buộc)

Toàn bộ skill của dự án nằm ở `skill\<ten-skill>\SKILL.md` (KHÔNG dùng `.claude\skills\` — nhóm đã chọn một thư mục duy nhất). Vì skill không được nạp tự động, quy tắc là: **khi nhận việc khớp mô tả trong bảng dưới, PHẢI đọc file SKILL.md tương ứng trước khi làm.**

Mọi yêu cầu công việc của dự án đi qua `skill\task-processor\SKILL.md` trước (định vị phase/task → làm rõ → Task Brief → điều phối). Ngoại lệ: câu hỏi kiến thức thuần túy không tạo/sửa file.

| Khi việc liên quan đến... | Đọc skill |
|---|---|
| Bất kỳ task dự án nào (điểm vào mặc định) | `skill\task-processor\` |
| Viết văn bản VN/EN, literature review, LaTeX, citation | `skill\professional_writing\` |
| Tính AHP, TOPSIS, CR, sensitivity | `skill\mcdm-toolkit\` |
| Thu thập dữ liệu laptop, benchmark PassMark | `skill\crawl-laptop-data\` |
| Phân tích khảo sát Likert, sàng lọc tiêu chí | `skill\likert-analysis\` |
| Dựng slide PowerPoint | `skill\pptx\` |
| Đọc/ghi/sửa Excel, CSV | `skill\xlsx\` |
| Trích xuất text/bảng từ PDF | `skill\pdf\` |
| Câu hỏi logistics/SCM chuyên sâu | `skill\supply-chain-consultant\` |
| Tạo skill mới, sửa skill, kiểm định an toàn skill | `skill\skill-creator\`, `skill\writing-skills\`, `skill\audit-skills\` |

## Luật vàng về file (không có ngoại lệ)

1. `02_du-lieu-tho\` là vùng đóng băng: file vào rồi thì không sửa, không xóa. Xử lý dữ liệu = copy sang `03_phan-tich\` rồi làm trên bản copy.
2. `06_nop-bai\` chỉ chứa bản nộp cuối đã được nhóm duyệt. Không bao giờ tự ghi vào đây.
3. File mới đặt tên theo quy ước README mục 4 (`YYYY-MM-DD_ten_vX.Y_trangthai_nguoi.ext`); dữ liệu thị trường/benchmark bắt buộc kèm ngày thu thập.

## Quy ước kỹ thuật

- Báo cáo `04_bao-cao-latex\`: biên dịch bằng **XeLaTeX + biber** (không dùng pdflatex). Bảng dùng booktabs, không kẻ dọc.
- Tính AHP/TOPSIS: luôn chạy script trong `skill\mcdm-toolkit\scripts\`, không tính tay. CR > 0.1 là ma trận hỏng, phải báo.
- Viết học thuật: nháp tiếng Việt trước, bản tiếng Anh viết lại độc lập từ Content Brief (không dịch máy từng câu) — theo skill `professional_writing`.
- Khi người dùng nói "lưu phiên bản báo cáo": git commit với message mô tả nội dung vừa làm. Khi nói "khôi phục báo cáo": tìm commit theo mô tả/ngày và restore, hỏi xác nhận trước khi ghi đè.

## Tài liệu định hướng

- `README.md` — sổ tay vận hành: bản đồ thư mục, workflow 7 phase với task T0.1→T6.8, DoD, backup.
- `KE-HOACH-DU-AN.md` — kế hoạch tổng thể và lý do các quyết định thiết kế.
- `00_quan-ly-du-an\timeline.md` — deadline và trạng thái từng phase.
