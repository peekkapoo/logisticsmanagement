# Literature Review — Nghiên Cứu Học Thuật

**Module:** N3 — Content
**Loại:** ⚪ Tùy chọn
**Mục đích:** Thu thập nguồn cho bài viết/báo cáo học thuật — khác `research.md` (hướng journalism) ở chỗ bắt buộc thu đủ metadata trích dẫn ngay từ đầu, ưu tiên nguồn peer-reviewed.

---

## Khi Nào Dùng

- ✅ Đề bài là bài báo khoa học, báo cáo/tiểu luận học thuật (đã xác định ở SKILL.md Bước 2, câu 7)
- ✅ Cần trích dẫn có thể kiểm chứng, không chỉ "theo báo cáo X"
- ❌ Bài blog/Facebook cảm xúc → dùng `research.md` thay thế

---

## Quy Trình

### Bước 1: Xác định câu hỏi nghiên cứu và khoảng trống (gap)

```
Research question: [Câu hỏi cụ thể bài viết trả lời]
Đã biết (từ kiến thức nền): [...]
Gap: [Điều gì chưa rõ / chưa có ai trả lời đầy đủ]
```

### Bước 2: Phân loại và tìm nguồn theo tầng

| Tầng | Loại nguồn | Ưu tiên |
|------|-----------|---------|
| Primary | Bài báo peer-reviewed, dữ liệu gốc, báo cáo chính phủ/tổ chức quốc tế | Cao nhất |
| Secondary | Review paper, meta-analysis, sách chuyên khảo | Cao |
| Tertiary | Báo chí, blog chuyên ngành | Chỉ dùng làm ngữ cảnh, không dùng làm luận cứ chính |

Nếu môi trường có công cụ tìm kiếm học thuật (semantic search cho paper, hoặc web search), ưu tiên dùng để tìm nguồn có DOI/link gốc thay vì chỉ dựa kiến thức nội tại — đặc biệt với số liệu, năm công bố, tên tác giả.

### Bước 3: Thu thập — BẮT BUỘC ghi đủ metadata ngay lúc đọc nguồn

Không đợi viết xong mới bổ sung trích dẫn. Với mỗi nguồn:

```
- Tác giả: [Họ tên đầy đủ hoặc tổ chức]
- Năm: [YYYY]
- Tiêu đề: [Tên bài/báo cáo]
- Venue: [Tên tạp chí/hội nghị/nhà xuất bản]
- DOI/URL: [Nếu có]
- Loại nguồn: Primary/Secondary/Tertiary
- Điểm dùng trong bài: [Claim cụ thể nguồn này hỗ trợ]
```

Thiếu bất kỳ trường nào → `review/citation-check.md` ở bước sau sẽ không thể xác minh trích dẫn.

### Bước 4: Validate

- Recency: còn phù hợp thời điểm viết không? (một số lĩnh vực yêu cầu nguồn <5 năm)
- Cross-check: số liệu/claim quan trọng → ít nhất 2 nguồn độc lập xác nhận
- Loại bỏ nguồn không rõ tác giả/không truy được gốc

### Bước 5: Xuất Content Brief (kèm bảng nguồn)

```
## Content Brief: [Đề tài]

### Research Question
[...]

### Key Points
1. [Luận điểm + nguồn hỗ trợ]

### Nguồn (để dùng cho citation-check.md sau)
| Tác giả, Năm | Tiêu đề | Venue | DOI/URL | Loại |
|---|---|---|---|---|
```

---

## Anti-Patterns

```
❌ Trích dẫn mơ hồ "theo nghiên cứu gần đây" → ✅ Ghi rõ tác giả + năm ngay khi thu thập
❌ Chỉ dùng nguồn tertiary (báo chí) cho claim khoa học → ✅ Ưu tiên primary/secondary
❌ Bổ sung metadata sau khi viết xong → ✅ Thu thập đủ ngay từ Bước 3
```
