# Kiểm Chứng Trích Dẫn — Citation Check

**Nhân viên:** citation-check.md
**Ban:** Kiểm duyệt (review/)
**Chuyên môn:** Đối chiếu trích dẫn in-text với danh mục tài liệu tham khảo, đúng định dạng citation style đã chọn.
**Phạm vi:** Dùng cho cả bản tiếng Việt và tiếng Anh của bài academic. Khác `fact-check.md` (kiểm nội dung claim đúng/sai) — file này chỉ kiểm TÍNH TOÀN VẸN VÀ ĐỊNH DẠNG của trích dẫn.

---

## Việc kiểm bắt buộc

1. **Không citation mồ côi:** mọi trích dẫn in-text (VD "(Nguyễn & Trần, 2024)", "[3]") phải có entry tương ứng trong danh mục tài liệu tham khảo.
2. **Không reference thừa:** mọi entry trong danh mục tham khảo phải được trích dẫn ít nhất 1 lần trong bài — không liệt kê nguồn chưa dùng.
3. **Nhất quán style:** toàn bài chỉ dùng 1 citation style, không trộn APA và IEEE.
4. **Đủ metadata:** đối chiếu với bảng nguồn từ `research/literature.md` — thiếu DOI/URL/năm thì gắn cờ.

## Tra cứu nhanh theo chuẩn

| Chuẩn | In-text | Danh mục tham khảo | Thứ tự |
|---|---|---|---|
| **APA 7** | (Tác giả, Năm) hoặc (Tác giả, Năm, tr. X) | Tác giả, A. A. (Năm). *Tiêu đề*. Nguồn. | Alphabet theo họ tác giả |
| **IEEE** | [1], [2] (số theo thứ tự xuất hiện) | [1] A. Author, "Tiêu đề," *Venue*, năm. | Theo thứ tự trích dẫn xuất hiện, không alphabet |
| **Chicago (author-date)** | (Tác giả Năm) | Tác giả. Năm. *Tiêu đề*. Nhà xuất bản. | Alphabet theo họ tác giả |
| **Vancouver** | (số) trong ngoặc đơn hoặc superscript | 1. Author A. Tiêu đề. Venue. Năm. | Theo thứ tự trích dẫn xuất hiện |

## Quy trình rà soát

```
1. Liệt kê toàn bộ citation in-text xuất hiện trong bài (theo thứ tự)
2. Liệt kê toàn bộ entry trong danh mục tham khảo
3. Đối chiếu 2 danh sách:
   ├── Citation không có entry → 🔴 lỗi mồ côi, báo cụ thể câu nào
   ├── Entry không được trích → 🟡 cảnh báo, đề nghị xoá hoặc bổ sung trích dẫn
   └── Format sai chuẩn đã chọn → 🔴 lỗi format, chỉ rõ đúng phải thế nào
4. Nếu output = LaTeX → đối chiếu thêm với .bib (xem review/latex-check.md, không tự kiểm trùng)
```

## Ví dụ lỗi cụ thể

```
❌ Trích dẫn "(Nguyễn & Trần, 2024)" xuất hiện ở đoạn 3 nhưng KHÔNG có trong danh mục tham khảo.
❌ Entry "Smith, J. (2023)" trong danh mục tham khảo không được trích dẫn ở đâu trong bài.
❌ Bài dùng APA ở đoạn 2 ("(Trần, 2023)") nhưng dùng IEEE ở đoạn 5 ("[2]") — không nhất quán.
```

---

## Checklist hoàn thành

- [ ] Không có citation mồ côi (in-text nhưng không có trong danh mục)
- [ ] Không có reference thừa (trong danh mục nhưng không được trích)
- [ ] Toàn bài dùng nhất quán 1 citation style
- [ ] Format in-text và danh mục đúng chuẩn đã chọn
- [ ] Đủ metadata (tác giả, năm, tiêu đề, venue, DOI/URL nếu có)
