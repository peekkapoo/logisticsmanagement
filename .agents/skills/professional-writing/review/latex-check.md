# Kiểm Cú Pháp LaTeX — Latex Check

**Nhân viên:** latex-check.md
**Ban:** Kiểm duyệt (review/)
**Chuyên môn:** Rà soát cú pháp file `.tex`/`.bib` do `publishing/latex.md` sinh ra. Áp dụng chung cho cả bản tiếng Việt và tiếng Anh (đây là lỗi cú pháp, không phải lỗi ngôn ngữ).
**Phạm vi:** Chỉ dùng khi output = LaTeX. Chạy SAU CÙNG, cần bài đã hoàn chỉnh nội dung.

---

## Việc kiểm bắt buộc

### 1. Cân bằng cấu trúc

- Mọi `\begin{...}` phải có `\end{...}` tương ứng, đúng tên môi trường.
- Ngoặc `{}` cân bằng — đếm số `{` phải bằng số `}`.
- Môi trường math: `$...$` (inline) và `\[...\]`/`\begin{equation}...\end{equation}` (display) đóng mở đủ, không lồng `$` bên trong `$`.

### 2. Escape ký tự đặc biệt trong văn xuôi

Các ký tự sau PHẢI được escape khi xuất hiện trong văn bản thường (không phải trong lệnh LaTeX):

| Ký tự gốc | Viết đúng trong LaTeX |
|---|---|
| `%` | `\%` |
| `&` | `\&` |
| `_` | `\_` |
| `#` | `\#` |
| `$` | `\$` |
| `{` `}` | `\{` `\}` |
| `~` | `\textasciitilde{}` |
| `^` | `\textasciicircum{}` |
| `\` | `\textbackslash{}` |

**Lỗi phổ biến nhất khi viết LaTeX tự động:** quên escape `%` khi gõ số liệu phần trăm ("tăng 18%" → phải là "tăng 18\%") và quên escape `&` trong bảng hoặc khi viết "A và B" theo kiểu liệt kê.

### 3. Toàn vẹn tham chiếu

- Mọi `\ref{}`, `\cref{}`, `\eqref{}` phải có `\label{...}` tương ứng đã khai báo trước đó trong tài liệu.
- Mọi `\cite{key}` phải có `key` tồn tại trong file `.bib` — đối chiếu danh sách citation với `review/citation-check.md`, không tự kiểm trùng nội dung trích dẫn ở đây, chỉ kiểm khớp key.
- Không có `\label{}` trùng tên (2 label giống nhau → lỗi biên dịch hoặc tham chiếu sai).

### 4. Lỗi đặc thù bản tiếng Việt (đã kiểm chứng bằng compile thật — không phải suy đoán)

- **Thiếu `\DeclareLanguageMapping{vietnamese}{american}`** (hoặc locale khác được style hỗ trợ) sau khi load `biblatex` → `\parencite`/`\textcite` sẽ CRASH ngay khi trích dẫn xuất hiện (biblatex-apa không có file locale cho "vietnamese"). Đây là lỗi bắt buộc phải có, không phải tùy chọn.
- **`cleveref` load trước `hyperref`** → lỗi "cleveref must be loaded after hyperref". Kiểm thứ tự 2 package này trong preamble.
- **Thiếu `[english]` option cho `cleveref`** khi tài liệu dùng `\setmainlanguage{vietnamese}` → crash "Undefined control sequence" ngay ở `\begin{document}` (cleveref không có bảng dịch cho "vietnamese").
- **Thiếu `\crefname`/`\Crefname` override sau khi ép `[english]`** → `\cref{}` in ra "table 1"/"figure 1" tiếng Anh lẫn vào câu tiếng Việt — kiểm bằng mắt các câu có `\cref{}`, đảm bảo tên hiển thị (Bảng/Hình) khớp ngôn ngữ tài liệu.
- **`\caption{}` viết tay "Bảng 1. ..."** trong khi polyglossia đã tự thêm số — gây lặp "Bảng 1: Bảng 1. ...". Caption chỉ nên chứa phần mô tả.

### 5. Biên dịch thử (ưu tiên nếu có công cụ)

Nếu môi trường có sẵn toolchain LaTeX, biên dịch thử thật đáng tin cậy hơn đọc bằng mắt:

```bash
# Kiểm tra công cụ có sẵn không
command -v xelatex || command -v pdflatex || command -v latexmk

# Biên dịch thử (dùng thư mục tạm, không ghi đè bản gốc)
xelatex -interaction=nonstopmode -halt-on-error draft.tex
```

Nếu biên dịch lỗi → đọc log, chỉ ra dòng lỗi cụ thể, sửa rồi biên dịch lại. Nếu không có toolchain → rà soát thủ công theo mục 1-3 ở trên, ghi rõ "chưa biên dịch thử được, chỉ rà soát cú pháp tĩnh".

---

## Ví dụ lỗi cụ thể

```
❌ Dòng 42: "tăng 18% năng suất" — ký tự % chưa escape, sẽ biến phần còn lại của dòng thành comment LaTeX.
❌ \begin{table} ở dòng 30 không có \end{table} tương ứng.
❌ \ref{fig:result} ở dòng 55 nhưng không tìm thấy \label{fig:result} nào trong tài liệu.
```

---

## Checklist hoàn thành

- [ ] Mọi `\begin`/`\end` cân bằng, đúng tên môi trường
- [ ] Ngoặc `{}` cân bằng
- [ ] Không có ký tự đặc biệt (`% & _ # $ { } ~ ^ \`) chưa escape trong văn xuôi
- [ ] Mọi `\ref`/`\cref`/`\eqref` có `\label` tương ứng
- [ ] Mọi `\cite{key}` có key tồn tại trong `.bib`
- [ ] Bản tiếng Việt: có `\DeclareLanguageMapping{vietnamese}{...}` sau khi load biblatex?
- [ ] `cleveref` load sau `hyperref`, có option `[english]` nếu tài liệu tiếng Việt?
- [ ] Nếu ép `cleveref` `[english]`: đã override `\crefname`/`\Crefname` cho table/figure sang tiếng Việt?
- [ ] `\caption{}` không viết tay lặp lại "Bảng N."/"Hình N." đã được polyglossia tự thêm?
- [ ] Đã biên dịch thử nếu có toolchain, hoặc ghi rõ nếu chưa thể
