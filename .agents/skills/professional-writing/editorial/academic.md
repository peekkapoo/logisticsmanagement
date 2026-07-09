# Academic — Viết Bài Báo/Báo Cáo Học Thuật

**Module:** V4 — Style
**Loại:** ⚪ Thay thế (dùng CÙNG `technical.md`, KHÔNG dùng cùng `story-core.md`)
**Mục đích:** Bổ sung phần academic-specific lên trên nền `technical.md` — cấu trúc IMRaD/báo cáo, Abstract, trích dẫn, hedging học thuật.

**Kế thừa:** Toàn bộ nguyên tắc đoạn văn (topic sentence, độ dài biến thiên), dòng chảy logic, hạn chế bullet, và heading của `technical.md` vẫn áp dụng. File này KHÔNG lặp lại các quy tắc đó — chỉ thêm phần academic không có trong `technical.md`.

---

## 1. Cấu trúc tài liệu

Chọn theo loại đã xác định ở SKILL.md Bước 2, câu 7:

**IMRaD đầy đủ** (bài báo khoa học):
```
Abstract → Introduction → Literature Review → Methodology → Results → Discussion → Conclusion → References
```

**Báo cáo/tiểu luận linh hoạt** (không cần đủ IMRaD):
```
Giới thiệu → [Các mục theo logic đề tài] → Kết luận → Tài liệu tham khảo
```

Không ép cấu trúc IMRaD vào báo cáo không cần — hỏi lại TBT/user nếu chưa rõ loại.

## 2. Abstract

150-250 từ, theo công thức: Purpose (mục đích) → Method (phương pháp) → Result (kết quả chính) → Conclusion (ý nghĩa).

```
✅ "Nghiên cứu này xem xét [purpose]. Bằng phương pháp [method], kết quả cho thấy [result].
    Phát hiện này gợi ý [conclusion]."
```

Không viết Abstract như đoạn mở bài storytelling — không hook, không ẩn dụ.

## 3. Research Question / Thesis Statement / Gap Statement

Mỗi bài academic cần nêu rõ:
- Câu hỏi nghiên cứu hoặc luận điểm chính (thesis) — 1 câu, đặt cuối phần Giới thiệu
- Gap: khoảng trống trong hiểu biết hiện có mà bài viết lấp vào (lấy từ Content Brief của `research/literature.md`)

## 4. Tích hợp trích dẫn vào câu văn

Trích dẫn phải nằm trong cấu trúc câu, không phải chú thích rời:

```
✅ "Nguyễn và Trần (2024) ghi nhận mức tăng năng suất 12-18% ở các doanh nghiệp ứng dụng AI."
✅ "Việc ứng dụng AI có thể liên quan đến mức tăng năng suất 12-18% (Nguyễn & Trần, 2024)."
❌ "AI giúp tăng năng suất. [1]" (chú thích rời, không rõ nguồn nói gì cụ thể)
```

Định dạng in-text theo citation style đã chọn (SKILL.md Bước 2, câu 7) — tra `review/citation-check.md` để đúng format APA/IEEE/Chicago/Vancouver.

## 5. Hedging học thuật — KHÔNG phải lỗi AI

**Ngoại lệ quan trọng với `review/anti-ai.md`:** khi context = academic, các cụm sau là quy ước bắt buộc, KHÔNG bị coi là "cautious hedging" cần loại bỏ:

| Tiếng Việt | Tiếng Anh |
|---|---|
| có thể, có khả năng | may, might, could |
| kết quả cho thấy, dữ liệu gợi ý | results suggest, data indicate |
| dường như, có xu hướng | appears to, tends to |

Lý do: academic writing phải phân biệt rõ "đã chứng minh" (established) và "gợi ý từ dữ liệu hiện có" (suggestive) — bỏ hedging tức là phóng đại mức độ chắc chắn của claim, một lỗi học thuật nghiêm trọng hơn nhiều so với "nghe giống AI".

**Giới hạn:** hedging hợp lệ khi gắn với 1 claim cụ thể có dữ liệu/nguồn đứng sau. Hedging tràn lan không gắn claim nào ("có thể nói rằng nhìn chung...") vẫn là lỗi mơ hồ, không được ngoại lệ.

## 6. Song ngữ VN + EN (khi SKILL.md Bước 2 câu 8 = 2 bản song song)

Bản thứ hai **viết lại độc lập** từ Content Brief + cấu trúc đã chốt ở bản thứ nhất — KHÔNG dịch từng câu:
1. Giữ nguyên: Research Question, cấu trúc mục, danh sách nguồn trích dẫn, số liệu.
2. Viết lại: câu văn, cách diễn đạt, ví dụ minh hoạ — theo văn phong bản địa của ngôn ngữ đích (xem `review/academic-en.md` cho quy ước tiếng Anh).
3. Bản tiếng Anh áp dụng toàn bộ mục 1-5 ở trên, nhưng KHÔNG áp dụng `review/natural.md` (quy tắc đó chỉ dành cho tiếng Việt).

---

## Checklist

- [ ] Cấu trúc đúng loại đã chọn (IMRaD hoặc linh hoạt)?
- [ ] Abstract đủ 4 thành phần, 150-250 từ?
- [ ] Có Research Question/Thesis rõ ràng cuối phần Giới thiệu?
- [ ] Mọi trích dẫn tích hợp trong câu, đúng citation style đã chọn?
- [ ] Hedging gắn với claim cụ thể, không tràn lan vô nghĩa?
- [ ] Nếu song ngữ: bản 2 là viết lại độc lập, không phải dịch câu-đối-câu?
