# LaTeX — Xuất Bản Dạng .tex

**Module:** H3 — Platform
**Loại:** ⚪ Tùy chọn
**Mục đích:** Sinh file `.tex` + `.bib` cho bài academic, đúng cú pháp và convention trình bày học thuật. Chỉ SINH file — không tự rà soát cú pháp (việc đó thuộc `review/latex-check.md`).

---

## 1. Chọn document class

| Loại bài (từ SKILL.md Bước 2) | Document class |
|---|---|
| Báo cáo/tiểu luận, bài báo tổng quát | `article` |
| Bài báo IEEE (conference/journal) | `IEEEtran` |
| Toán/khoa học tự nhiên chuẩn AMS | `amsart` |
| Luận văn/báo cáo dài có chương | `report` |

## 2. Engine biên dịch

Dùng **XeLaTeX hoặc LuaLaTeX** cho cả bản tiếng Việt lẫn tiếng Anh (đồng bộ toolchain). Không dùng `pdfLaTeX` — xử lý Unicode tiếng Việt kém, cần `fontenc T5`/`vntex` phức tạp và dễ lỗi.

## 3. Xử lý ngôn ngữ

**Bản tiếng Việt:**
```latex
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{vietnamese}
\setmainfont{Times New Roman} % hoặc font khác đã XÁC NHẬN có sẵn — xem cảnh báo font bên dưới
```
Văn bản nguồn phải là Unicode NFC. Không dùng bảng mã cũ (VNI/TCVN3).

**⚠️ Cảnh báo font đã kiểm chứng bằng compile thật:** KHÔNG mặc định gợi ý "Noto Serif" — tên font phổ biến trong hướng dẫn nhưng không chắc có sẵn trên máy build (đã test thật: `\setmainfont{Noto Serif}` lỗi "font cannot be found" trên môi trường chỉ cài "Noto Serif SC"). Luôn kiểm tra trước bằng `fc-list | grep -i "<tên font>"` (Linux/Mac/Git Bash) trước khi chọn, hoặc dùng "Times New Roman" — phổ biến sẵn trên Windows và đã test thành công với dấu tiếng Việt đầy đủ.

**Bản tiếng Anh:**
```latex
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{english}
```

## 4. Trích dẫn

```latex
\usepackage[style=apa,backend=biber]{biblatex}
% style: apa | ieee | chicago-authordate | vancouver — theo lựa chọn ở SKILL.md Bước 2
\DeclareLanguageMapping{vietnamese}{american}
\addbibresource{references.bib}
```

**⚠️ Bắt buộc với bản tiếng Việt (đã kiểm chứng bằng compile thật):** `biblatex-apa` (và nhiều style khác) KHÔNG có file locale cho "vietnamese" — nếu thiếu dòng `\DeclareLanguageMapping{vietnamese}{american}`, lệnh `\parencite`/`\textcite` sẽ CRASH thật ("Undefined control sequence") ngay khi trích dẫn xuất hiện, không chỉ cảnh báo suông. Luôn thêm dòng này ngay sau khi load `biblatex` cho mọi bản tiếng Việt, bất kể style nào.

Sinh `references.bib` từ bảng nguồn trong Content Brief (`research/literature.md`). Mỗi entry cần đủ trường tương ứng loại nguồn (`@article`, `@inproceedings`, `@book`...). Ưu tiên `biblatex` hơn `natbib` vì đổi style chỉ cần đổi 1 tham số.

Cuối tài liệu:
```latex
\printbibliography
```

## 5. Trình bày đẹp — checklist bắt buộc

| Yếu tố | Package/quy tắc |
|---|---|
| Bảng | `booktabs` — dùng `\toprule/\midrule/\bottomrule`, KHÔNG kẻ dọc `\|` |
| Hình | `graphicx` + `\caption{}` + `\label{fig:...}` |
| Cross-reference | `cleveref` — dùng `\cref{}` thay vì `\ref{}` thô. **Phải load SAU `hyperref`** (ngược lại → lỗi "cleveref must be loaded after hyperref") |
| Công thức | `amsmath`, `amssymb`, `mathtools` |
| Kerning/justification | `microtype` |
| Lề trang | `geometry` — nhất quán toàn tài liệu |
| Liên kết | `hyperref` — load SAU CÙNG trong preamble |
| Heading | Title Case (tiếng Anh, theo APA/IEEE) hoặc chỉ viết hoa chữ đầu (tiếng Việt) |

## 6. Preamble mẫu (article + tiếng Việt + APA) — đã kiểm chứng bằng compile thật (xelatex + biber, 0 lỗi)

```latex
\documentclass{article}
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{vietnamese}
\setmainfont{Times New Roman}
\usepackage{geometry}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{microtype}
\usepackage[style=apa,backend=biber]{biblatex}
\DeclareLanguageMapping{vietnamese}{american}
\addbibresource{references.bib}
\usepackage{hyperref}
\usepackage[english]{cleveref}
\crefname{table}{Bảng}{Bảng}
\Crefname{table}{Bảng}{Bảng}
\crefname{figure}{Hình}{Hình}
\Crefname{figure}{Hình}{Hình}

\title{[Tiêu đề bài]}
\author{[Tác giả]}
\date{\today}

\begin{document}
\maketitle
\begin{abstract}
[150-250 từ theo editorial/academic.md mục 2]
\end{abstract}

\section{Giới thiệu}
...

\printbibliography
\end{document}
```

**3 điểm dễ sai đã bắt được qua compile thật, PHẢI làm đúng ngay từ đầu:**
1. `cleveref` phải load SAU `hyperref`, và cần option `[english]` — `polyglossia` không có bảng dịch tên tham chiếu cho "vietnamese" trong `cleveref`, thiếu option này sẽ crash ngay ở `\begin{document}`.
2. Sau khi ép `[english]`, PHẢI khai lại tên bằng `\crefname`/`\Crefname` cho từng loại (table, figure...) — nếu không, `\cref{}` sẽ in ra "table 1"/"figure 1" tiếng Anh giữa câu tiếng Việt.
3. Với `\caption{}`: polyglossia đã tự thêm tiền tố "Bảng N:"/"Hình N:" — KHÔNG viết tay "Bảng 1. ..." trong nội dung caption nữa, chỉ viết phần mô tả, nếu không sẽ bị lặp ("Bảng 1: Bảng 1. ...").

Đổi `\setmainlanguage{vietnamese}` → `english` (bỏ `\DeclareLanguageMapping` và các `\crefname` override vì không cần thiết khi tài liệu đã là tiếng Anh), và style biblatex theo citation style đã chọn, để có preamble cho các tổ hợp khác.

## 7. Escape ký tự đặc biệt

Khi chèn nội dung văn xuôi vào `.tex`, escape đúng: `% & _ # $ { } ~ ^ \` → xem bảng đầy đủ ở `review/latex-check.md`. Đây là bước SINH file — không bỏ qua escape rồi để review bắt lỗi, làm đúng ngay từ đầu để giảm vòng lặp GATE.

---

## Checklist

- [ ] Document class đúng loại bài
- [ ] Engine khuyến nghị XeLaTeX/LuaLaTeX, fontspec+polyglossia cho tiếng Việt
- [ ] biblatex+biber, style đúng citation style đã chọn
- [ ] booktabs cho bảng, cleveref cho tham chiếu, microtype, hyperref load cuối
- [ ] Đã escape ký tự đặc biệt khi sinh file (không để review bắt hết)
- [ ] Sinh kèm `.bib` đầy đủ từ Content Brief
