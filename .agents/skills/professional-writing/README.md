# Viết Chuyên Nghiệp 4.0 — README

Skill viết tiếng Việt chuyên nghiệp theo mô hình **tòa soạn báo AI**. Một Tổng Biên Tập (TBT) nhận đề bài, phân tích, thiết kế quy trình, rồi điều phối 6 ban chuyên trách để tạo ra sản phẩm viết chất lượng cao.

---

## Kiến trúc

```
Người dùng
    │
    ▼
┌─────────────────────────────────────────┐
│  SKILL.md — Tổng Biên Tập (TBT)        │
│  Phân tích → Chọn ban → Thiết kế GATE  │
└────────────┬────────────────────────────┘
             │
    ┌────────┼────────┬──────────┬──────────┬──────────┐
    ▼        ▼        ▼          ▼          ▼          ▼
research/ editorial/ review/  publishing/ archive/  development/
Ban       Ban       Ban       Ban         Ban        Ban
Thu thập  Biên tập  Kiểm     Xuất bản    Tư liệu   Phát triển
                    duyệt
```

**Phân quyền 3 tầng:**
- **TBT** giao MỤC TIÊU + thiết kế quy trình GATE
- **Lead** (trưởng ban) tự chọn staff, ước lượng độ dài, phân công nội bộ
- **Staff** (nhân viên) thực hiện chuyên môn cụ thể

---

## Quy trình TBT

| Bước | Hành động |
|------|-----------|
| 1 | Kiểm tra lịch sử — bài mới hay cập nhật? |
| 2 | Phân tích request — 6 câu hỏi (input, mục đích, độc giả, platform, fact-check, archive) |
| 3 | Lựa chọn ban — 🔴 Chủ trì · 🟡 Phối hợp · 🟢 Kiểm tra |
| 4 | Thiết kế quy trình GATE — kết hợp 4 mô hình luồng |

### 4 mô hình luồng

```
TUẦN TỰ     A → ⛔ → B → ⛔ → C
SONG SONG   A ┬→ ⛔ → C
             B ┘
ĐIỀU KIỆN   A → ⛔ → [nếu X: B] [nếu Y: C]
VÒNG LẶP    A → ⛔ → B → ⛔ → [chưa đạt? → quay lại A]
```

### Quy tắc GATE

Giữa mỗi bước có cổng bàn giao. Mỗi ban phải hoàn thành 3 việc trước khi ban tiếp theo được load:
1. **Làm xong** — cam kết hoàn thành nội bộ đạt
2. **Xuất ra** — viết sản phẩm vào file
3. **Ghi nhận** — log bàn giao: ban nào → ban nào, sản phẩm gì

---

## 6 Ban chi tiết

### 1. Ban Thu thập (`research/`)

Thu thập thông tin và phân tích data khi đề bài chưa đủ dữ liệu.

| File | Chức năng | Dòng |
|------|-----------|------|
| `lead.md` | Trưởng ban — dispatch research vs analysis vs literature | 37 |
| `research.md` | Thu thập topic xa lạ — 5W1H, 3-tier research, content brief | 58 |
| `analysis.md` | Phân tích data thô → insights — patterns, ICE scoring | 49 |
| `literature.md` | Literature review học thuật — metadata trích dẫn bắt buộc từ đầu | 83 |

**Output:** Content Brief (Core Message + Key Points + Supporting Materials, hoặc bảng nguồn trích dẫn nếu academic)

---

### 2. Ban Biên tập (`editorial/`)

Ban chủ trì chính cho đa số đề bài. Viết bài, xây câu chuyện, áp dụng kỹ thuật.

| File | Chức năng | Load | Dòng |
|------|-----------|------|------|
| `lead.md` | Trưởng ban — chọn staff, ước lượng độ dài | — | 50 |
| `story-core.md` | Insight + logic chain + show-don't-tell + vernacular translation + **self-proof** | 🔵 Mặc định | 85 |
| `hook-close.md` | 4 loại hook + **delayed reveal** + 3 loại closing | 🔵 Mặc định | 51 |
| `rhythm.md` | 70-20-10, emotional pacing, **đoạn siêu dài 8-12 câu** | 🔵 Mặc định | 47 |
| `metaphor.md` | Extended metaphor + callback, compounding forces, self-reinforcing loop | ⚪ Tùy chọn | 43 |
| `reframe.md` | Concept naming, **concept system**, paradox flip, parallel analogy | ⚪ Tùy chọn | 70 |
| `debunk.md` | Structured debunk 5 bước, gentle debunk, commentary, **trích dẫn tiếng Anh** | ⚪ Tùy chọn | 67 |
| `emphasis.md` | Lật khung nhìn, câu đơn tách dòng, strategic caps (**8-12 cho debunk**) | ⚪ Tùy chọn | 39 |
| `technical.md` | Viết kỹ thuật/academic — topic sentence, logic flow, heading | ⚪ Thay thế | 75 |
| `academic.md` | IMRaD, Abstract, citation in-text, hedging học thuật, song ngữ VN+EN — lớp bổ sung trên `technical.md` | ⚪ Thay thế | 86 |

**Kỹ thuật mới (v3.1)** — in đậm trong bảng trên:
- **Self-Proof** — dùng kinh nghiệm bản thân làm bằng chứng cho insight
- **Concept System** — nhiều concept liên kết thành hệ thống (cộng → nhân → lũy thừa)
- **Delayed Reveal** — treo khái niệm rồi giải thích sau vài đoạn
- **Đoạn siêu dài** — 8-12 câu khi chuỗi logic/bằng chứng cần liền mạch
- **CAPS ngoại lệ** — 8-12 cụm cho debunk (mặc định 4-5)
- **Trích dẫn tiếng Anh** — giữ nguyên gốc khi debunk bóp méo thuật ngữ

---

### 3. Ban Kiểm duyệt (`review/`)

Cửa cuối — rà soát chất lượng trước khi xuất bản. 5 staff bắt buộc + 1 tùy chọn.

| File | Chức năng | Load | Dòng |
|------|-----------|------|------|
| `lead.md` | Trưởng ban — dispatch staff, quyết định duyệt/từ chối | — | 56 |
| `punctuation.md` | Dấu câu tiếng Việt — sát trước cách sau, cấm Oxford comma, cấm em-dash | 🔵 Bắt buộc | 68 |
| `capitalization.md` | Viết hoa — chỉ đầu câu + tên riêng, cấm Title Case | 🔵 Bắt buộc | 35 |
| `natural.md` | Tự nhiên hóa — cấm trộn tiếng Anh, chuyển bullet thành văn xuôi, **ngoại lệ bio** | 🔵 Bắt buộc | 56 |
| `anti-ai.md` | Phát hiện dấu vết AI — over-formatting, từ nối lặp, template rigidity | 🔵 Bắt buộc | 51 |
| `consistency.md` | Nhất quán — hierarchy giải quyết xung đột (review > editorial > publishing) | 🔵 Bắt buộc | 44 |
| `fact-check.md` | Kiểm chứng claims — phân loại risk, 5 phương pháp verify | ⚪ Tùy chọn | 50 |
| `academic-en.md` | Quy ước tiếng Anh học thuật — Oxford comma, Title Case, hedging (ngược VN) | ⚪ Tùy chọn, chỉ bản EN | 49 |
| `citation-check.md` | Đối chiếu citation ↔ danh mục tham khảo, tra cứu APA/IEEE/Chicago/Vancouver | ⚪ Tùy chọn, chỉ academic | 54 |
| `latex-check.md` | Cú pháp .tex/.bib — cân bằng môi trường, escape, tham chiếu, lỗi VN đã kiểm chứng compile thật | ⚪ Tùy chọn, chỉ output LaTeX | 87 |

---

### 4. Ban Xuất bản (`publishing/`)

Format sản phẩm cho kênh phân phối. Chỉ xử lý trình bày, không thay đổi nội dung.

| File | Chức năng | Dòng |
|------|-----------|------|
| `lead.md` | Trưởng ban — dispatch theo kênh | 38 |
| `facebook.md` | Format Facebook — IN HOA tiêu đề, khổ `===`, plaintext, ASCII typography | 47 |
| `academic.md` | Format Markdown/Word-style học thuật — giữ heading, references, caption bảng/hình | 50 |
| `latex.md` | Sinh .tex/.bib — document class, engine XeLaTeX, biblatex, preamble mẫu đã kiểm chứng compile thật | 133 |

---

### 5. Ban Tư liệu (`archive/`)

Lưu trữ bài mẫu và kho pattern tra cứu nhanh.

| File | Chức năng | Dòng |
|------|-----------|------|
| `lead.md` | Trưởng ban — cơ chế tra cứu + cập nhật | 28 |
| `pattern-catalog.md` | 42 patterns · 7 nhóm (mở bài, cấu trúc, dẫn chứng, tương phản, ngôn ngữ, kết bài, nâng cao) | 72 |

**Tra cứu khi:** TBT phân tích request (câu 6), Editorial cần reference, Review cần đối chiếu.
**Cập nhật khi:** Bài qua review duyệt, hoặc Development phân tích bài bên ngoài.

---

### 6. Ban Phát triển (`development/`)

Nâng cấp skill — phân tích phong cách, rút pattern, quản trị nhân sự.

| File | Chức năng | Dòng |
|------|-----------|------|
| `lead.md` | Trưởng ban — dispatch, quy trình phân tích bài viết mẫu | 71 |
| `style-audit.md` | Phân tích phong cách — 4 bước (staged assessment → cấu trúc → nội dung → style DNA) | 96 |
| `upgrade.md` | Tự nâng cấp — so sánh registry, format 5 thành phần, changelog | 86 |
| `research-framework.md` | Framework nghiên cứu phong cách viết — template, tracking, 26 nguồn | 111 |
| `research-results.md` | Kết quả nghiên cứu — 42 patterns từ 14 bài, 8 nguồn | 25 |

**Nguyên tắc:** Ban Phát triển PHÂN TÍCH + ĐỀ XUẤT. Cập nhật thực tế nằm ở file skill đích.

---

## Thống kê

| Mục | Số lượng |
|-----|----------|
| Tổng files | 37 (Markdown + 2 scripts Python phụ trợ) |
| Tổng dòng | ~3.200 |
| Số ban | 6 |
| Số lead | 6 |
| Số staff | 31 |
| Patterns trong catalog | 42 (8 nhóm, nhóm Học thuật chưa có pattern) |
| Max load/lượt | ≤ 200 dòng (1 lead + 1-2 staff, academic+LaTeX có thể vượt nhẹ) |
| Max module size | ≤ 300 dòng |

---

## Changelog gần nhất (2026-07-08)

| Thay đổi | Nguồn |
|----------|-------|
| **Merge cải tiến từ Claude (v4.0)** — Sửa toàn bộ tham chiếu nội bộ lỗi thời từ trước refactor v3.0 (`quality/`→`review/`, `style/`→`editorial/`, `platform/`→`publishing/`, `meta/`→`development/`, `examples/`→`archive/`) rải rác ở ~25 file; viết lại `description` trong SKILL.md để liệt kê rõ tình huống kích hoạt; cập nhật metadata header các staff file. GIỮ NGUYÊN `scripts/` (academic_parser.py) cho Antigravity | Merge từ professional-writing-improved 2026-07-08 |
| **Mở rộng Academic + LaTeX** — +7 file mới (research/literature.md, editorial/academic.md, review/academic-en.md + citation-check.md + latex-check.md, publishing/academic.md + latex.md), song ngữ VN+EN viết độc lập, citation style linh hoạt (APA/IEEE/Chicago/Vancouver), ngoại lệ hedging/headers cho academic trong anti-ai.md/natural.md | Yêu cầu user mở rộng viết học thuật 2026-07-04 |
| SKILL.md v3.1 — 4 mô hình luồng, quy trình GATE evidence, routing tham chiếu | Redesign TBT |
| story-core.md — §3.2 Self-Proof | 3 bài viết tác giả |
| reframe.md — §1.1 Concept System | 3 bài viết tác giả |
| hook-close.md — §2.1 Delayed Reveal | 3 bài viết tác giả |
| rhythm.md — §1.1 đoạn siêu dài 8-12 câu | 3 bài viết tác giả |
| emphasis.md — ngoại lệ CAPS 8-12 cho debunk | 3 bài viết tác giả |
| debunk.md — trích dẫn nguyên văn tiếng Anh | 3 bài viết tác giả |
| natural.md — ngoại lệ format bio/profile | 3 bài viết tác giả |
| editorial/lead.md — nhận ước lượng độ dài | Redesign v3.1 |
| archive/lead.md — cơ chế tra cứu + cập nhật | Redesign v3.1 |
| SKILL.md, editorial+review lead — quy tắc GATE bàn giao | Feedback quy trình |

Xem changelog đầy đủ tại `development/upgrade.md`.

---

**Version:** 4.0 · **Cập nhật:** 2026-07-08 · **Kiến trúc:** Tòa soạn báo (TBT → Lead → Staff)
