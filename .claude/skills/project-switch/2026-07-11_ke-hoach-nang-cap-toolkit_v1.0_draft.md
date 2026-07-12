# Kế hoạch nâng cấp toolkit — **CODEX-FIRST** (Codex chính, Claude Code phụ)

> **Trạng thái:** DRAFT v2.0 chờ duyệt · **Ngày:** 2026-07-11 · **Người soạn:** Claude (Opus 4.8)
> **Đổi hướng so với v1.0:** user xác nhận **sẽ dùng Codex là chủ yếu** → tối ưu toàn diện cho Codex; Claude Code hạ xuống vai phụ (vẫn giữ chạy được).
> **Quyết định đã chốt:** (1) Đích = **Codex + Claude Code**, bỏ Antigravity. (2) Tài liệu này **chỉ là plan, chưa thực thi**.

---

## 1. Codex thực sự vận hành thế nào (nền tảng của mọi quyết định dưới đây)

Khác biệt cốt lõi phải nắm trước khi tối ưu:

| | Claude Code | **Codex** |
|---|---|---|
| Nạp skill | **Autoload** `.claude/skills/*/SKILL.md` theo `description` | **KHÔNG autoload.** Chỉ đọc file khi được chỉ path |
| File luật | `CLAUDE.md` → `@AGENTS.md` | **`AGENTS.md`** (gốc **+ lồng trong thư mục con**) — nguồn chỉ dẫn chính |
| Subagent | Có (`.claude/agents/`) | **Không** — mọi thứ trong `.claude/agents/` vô hình |
| Điểm mạnh | Suy luận dài, điều phối skill | **Chạy lệnh CLI, thao tác file lặp, sửa code** |

**Hệ quả:** với Codex, "skill" không tự kích hoạt. Codex chỉ làm đúng nếu **`AGENTS.md` dẫn nó**: đọc routing → mở đúng `SKILL.md` theo path → **chạy script**. Vì vậy tối ưu Codex = làm 3 việc, KHÔNG phải dời thư mục:

1. **Biến `AGENTS.md` thành cẩm nang vận hành tự đủ** (routing có path tuyệt đối tới từng SKILL.md + lệnh CLI đi kèm).
2. **CLI-hóa mọi năng lực** có thể (Codex chạy lệnh giỏi hơn "đọc-hiểu-skill").
3. **Dùng `AGENTS.md` lồng nhau** trong các thư mục làm việc — tính năng Codex-native cho ngữ cảnh cục bộ.

> **Vì sao KHÔNG dời `.claude/skills/` đi chỗ khác:** Claude Code autoload *bắt buộc* đọc từ `.claude/skills/`. Tên thư mục `.claude` chỉ là cosmetic với Codex — Codex đọc theo path do `AGENTS.md` chỉ, không quan tâm folder tên gì. Giữ `.claude/skills/` làm **nguồn chân lý duy nhất** để Claude còn autoload; Codex tiếp cận qua `AGENTS.md`. Không nhân bản 14 skill.

---

## 2. Bản đồ trạng thái hiện tại (đã xác minh)

- **Luật:** `AGENTS.md` (gốc, chuẩn agents.md — Codex đọc thẳng) · `CLAUDE.md` (mỏng, chỉ import — Claude-only).
- **Skills:** `.claude/skills/` — 14 skill, phẳng 1 cấp (`data-pipeline` là bundle lồng có bảng điều phối nội bộ).
- **Subagents:** `.claude/agents/` — 3 (skill-smith, data-gatherer, office-docs). **Claude-only, Codex bỏ qua.**
- **Codex mirror:** `.codex/skills/` — 3 bản Codex-flavored (data-gatherer, skill-smith, project-switch).
- **CLI sẵn có** (điểm mạnh cho Codex): `mcdm-toolkit/scripts/{ahp,topsis}.py`, `likert-analysis/scripts/likert.py`, `data-pipeline` (`shared/scripts/validate.py` + `skills/*/scripts/*.py`), `professional-writing/scripts/{academic_parser,batch_parse}.py`, `pdf/pptx/xlsx/officecli` scripts.

---

## 3. Phát hiện chi tiết (giữ từ v1.0, sắp lại theo mức độ hại-cho-Codex)

### Nhóm A — Tham chiếu chết / sai path (Codex đọc path chết là hỏng ngay)
| # | File:dòng | Sửa |
|---|---|---|
| A1 | `.claude/skills/task-processor/SKILL.md:57` | `.agents/skills/` → `.claude/skills/` |
| A2 | `.claude/skills/data-pipeline/README.md:16-20` | Bỏ hướng dẫn cài Antigravity |
| A3 | `README.md:272` | `@[.agents/skills/...]` → `.claude/skills/...` |
| A4 | `README.md` mục 2 & 8 | Đồng bộ `.agents\`→`.claude\`, `professional_writing`→`professional-writing` |
| A5 | `.claude/skills/writing-skills/SKILL.md:12` | Xác nhận path Codex = `.codex/skills/` |

### Nhóm B — Frontmatter (với Codex ít quan trọng hơn, nhưng vẫn dọn)
- B1 `skill-creator` description cắt cụt "..." → viết lại đầy đủ.
- B2 `writing-skills` description mỏng → bổ sung trigger.
- B3/B4 `audit-skills`, `skill-creator`: bỏ field không-chức-năng (`tools:[gemini,gpt]`, `category/risk/...`) khỏi frontmatter, dời provenance xuống thân bài.
> Ghi chú: autoload là cơ chế của Claude; Codex không dùng `description` để kích hoạt. Nhưng dọn frontmatter vẫn cần cho Claude-phụ + để `AGENTS.md` trích mô tả nhất quán.

### Nhóm C — Kiến trúc & hiệu năng
- C1 `data-pipeline` lồng skill: chạy được (SKILL.md cha có bảng path). Thêm ghi chú "sub-skill không autoload, luôn vào qua data-pipeline".
- C2 `professional-writing/models/` (harness-detect, đã gitignore một phần): rà giữ/xóa để nhẹ.
- C3 Smoke-test 4 nhóm script với `examples/`; pin `requirements.txt`.

---

## 4. Kế hoạch thực thi CODEX-FIRST (6 giai đoạn)

### GĐ 0 — Chốt baseline an toàn
Commit trạng thái di trú hiện tại thành 1 mốc sạch (message: "hoàn tất migrate `.agents`→`.claude`, chuyển sang mô hình Codex-first"). Mọi thay đổi sau diff/rollback được.

### GĐ 1 — 🎯 Biến `AGENTS.md` thành cẩm nang vận hành tự đủ cho Codex *(giá trị cao nhất)*
Đây là đòn bẩy lớn nhất cho Codex-first.
- **Thêm "Codex Quickstart" đầu file:** 5–7 dòng dạy Codex vòng lặp chuẩn — *đọc `task_log.md` → tra bảng routing mục 5 → mở đúng `SKILL.md` theo path → chạy CLI ở mục 4 → cập nhật log*. Nói rõ: **"skill KHÔNG tự kích hoạt; bạn PHẢI chủ động đọc file SKILL.md tương ứng trước khi làm loại việc đó."**
- **Nâng cấp bảng routing mục 5 thành "địa chỉ tuyệt đối":** mỗi dòng có **path đầy đủ tới `SKILL.md`** + **lệnh CLI entry** (nếu có). Ví dụ: `AHP/TOPSIS → đọc .claude/skills/mcdm-toolkit/SKILL.md · chạy python .claude/skills/mcdm-toolkit/scripts/ahp.py <csv>`.
- **Mục 4 (catalog CLI) thành nguồn năng lực chính của Codex:** bổ sung mọi script còn thiếu (data-pipeline `validate.py`, `academic_parser.py`, các `collect_*.py`), kèm cú pháp + input mẫu `examples/`. Codex ưu tiên chạy lệnh hơn đọc prose.
- **Đánh dấu rõ phần Claude-only:** thêm 1 dòng ở mục subagent — *"`.claude/agents/` chỉ Claude Code dùng; Codex bỏ qua, làm việc tương đương bằng cách đọc skill được bọc + chạy CLI"* — để Codex không phí công.

### GĐ 2 — 🎯 `AGENTS.md` lồng nhau trong thư mục làm việc *(Codex-native, Claude không cần)*
Codex đọc `AGENTS.md` ở thư mục con khi làm việc trong đó → ngữ cảnh cục bộ, không phải nhồi hết vào file gốc. Tạo các file nhỏ (5–15 dòng):
| File | Nội dung cốt lõi |
|---|---|
| `02_du-lieu-tho/AGENTS.md` | "VÙNG ĐÓNG BĂNG — không sửa/xóa. Xử lý = copy sang `03_phan-tich/`." + quy ước tên file có ngày |
| `03_phan-tich/AGENTS.md` | Vùng làm việc; input từ đâu, output đi đâu; nhắc chạy CLI mcdm/likert |
| `04_bao-cao-latex/AGENTS.md` | Build **XeLaTeX + biber** (không pdflatex); bảng LaTeX booktabs vào `tables/`; nháp VN→viết lại EN |
| `06_nop-bai/AGENTS.md` | "CHỈ bản nộp cuối đã duyệt. KHÔNG ghi tạm." |
| `08_new_knowledge/AGENTS.md` | Chuẩn tech-blog 5 bước, không tiền tố số ở H1 |
> Mỗi file cực ngắn, không lặp luật gốc — chỉ nhắc điều đặc thù của thư mục đó. Đây là thứ giúp Codex "tự biết luật" ngay tại chỗ làm.

### GĐ 3 — CLI-first: bịt lỗ hổng năng lực chạy-lệnh
- **Audit script entry:** liệt kê skill nào đã có CLI chạy được, skill nào thuần suy luận (task-processor, supply-chain-consultant — không CLI-hóa được, giữ nguyên).
- **Thêm wrapper mỏng nếu cần:** ví dụ 1 lệnh gộp `data-pipeline` chạy validate; hoặc script "export sheet Excel AHP ra CSV" để Codex khỏi thao tác tay (nối `xlsx` → `mcdm-toolkit`).
- **Smoke-test** toàn bộ CLI với `examples/`, ghi lệnh + output mẫu vào AGENTS.md mục 4 để Codex copy chạy.
- **Pin `requirements.txt`** (đặc biệt `academic_parser`: docling/pymupdf4llm/pypdf) để Codex `pip install -r` một phát chạy được.

### GĐ 4 — Dọn Nhóm A + frontmatter (Nhóm B) + ghi chú kiến trúc (C1/C2)
- Sửa hết path chết A1–A5.
- Chuẩn hóa frontmatter tối thiểu (mục 5) cho 14 skill.
- Thêm ghi chú C1; quyết định C2 (giữ/xóa `models/`).

### GĐ 5 — Công cụ chống trôi dạt + chốt tài liệu
- **`scripts/validate-toolkit.py`** (read-only): kiểm (a) không còn path `.agents/` sót, (b) mọi path trong bảng routing `AGENTS.md` **tồn tại thật**, (c) frontmatter parse được + `name` khớp thư mục, (d) mọi lệnh CLI liệt kê trong AGENTS.md mục 4 trỏ tới script có thật. Đây là "test" hợp đồng Codex.
- **`scripts/sync-codex-mirrors.py`** (read-only): báo drift `.codex/skills/*` vs bản Claude nguồn.
- **Chốt:** entry mới trong `upgrade-log.md` (giải quyết mâu thuẫn lịch sử, mô tả mô hình Codex-first cuối cùng) → đồng bộ 3 nơi (routing `task-processor` ↔ `AGENTS.md` mục 5 ↔ `upgrade-log.md`) → cập nhật `README.md` & `task_log.md` (timestamp).

---

## 5. Chuẩn frontmatter tối thiểu (áp mọi SKILL.md)
```yaml
---
name: <kebab, khớp tên thư mục>
description: >
  <1 đoạn, <1024 ký tự, KHÔNG "…">. Nêu KHI NÀO dùng + KHI NÀO KHÔNG,
  kèm trigger words VN/EN. (Với Codex: mô tả này được AGENTS.md trích lại ở bảng routing.)
---
```
Bỏ khỏi frontmatter: `category, risk, source, author, date_added, tags, tools:[...]`. Giữ `license:` cho skill Anthropic. Subagent giữ `name/description/tools/skills/model`.

---

## 6. Verification (nghiệm thu)
- **GĐ 1:** đọc `AGENTS.md` — Codex Quickstart có; bảng routing mọi dòng có path + CLI; `validate-toolkit.py` xác nhận path tồn tại.
- **GĐ 2:** `find . -name AGENTS.md` liệt kê đủ file lồng; mở thử vài file thấy ngắn, đúng đặc thù.
- **GĐ 3:** `pip install -r requirements.txt` sạch; `python .claude/skills/mcdm-toolkit/scripts/ahp.py .../examples/ahp-vidu-3x3.csv` ra trọng số+CR; tương tự topsis/likert/validate.
- **GĐ 4:** `grep -rn "\.agents/\|professional_writing" .claude README.md` → rỗng; `validate-toolkit.py` frontmatter pass.
- **GĐ 5:** `validate-toolkit.py` exit 0; `sync-codex-mirrors.py` 0 drift; 3 nơi routing khớp.
- **🔬 Kiểm thử thật quan trọng nhất:** mở project bằng **Codex trong VSCode**, giao 1 việc mẫu (vd "tính AHP từ file X") → xác nhận Codex tự đọc `AGENTS.md`, tìm đúng CLI, chạy ra kết quả **mà không cần mình chỉ tay từng bước**. Đây là thước đo "đã tối ưu cho Codex" hay chưa.

---

## 7. Điểm cần user quyết khi thực thi
1. **AGENTS.md lồng nhau (GĐ 2):** đồng ý rải file nhỏ vào 5 thư mục làm việc? (Claude không hại gì; Codex hưởng lợi nhiều.)
2. **C2 `professional-writing/models/`:** còn dùng detect harness hay xóa cho nhẹ?
3. **Wrapper CLI (GĐ 3):** có muốn tôi tạo thêm script nối `xlsx→mcdm` (xuất sheet AHP ra CSV tự động) không?
4. **`.codex/skills/` phạm vi:** giữ nguyên 3 mirror (subagent-equivalents + project-switch), hay mở rộng thêm skill nào Codex hay dùng?

---

## 8. Thứ tự khuyến nghị khi được duyệt
GĐ 0 → **GĐ 1** (AGENTS.md tự đủ — đòn bẩy lớn nhất) → **GĐ 2** (AGENTS.md lồng) → GĐ 3 (CLI-first) → GĐ 4 (dọn) → GĐ 5 (validate + chốt). Dừng xin duyệt cuối mỗi GĐ. Nếu muốn nhanh thấy hiệu quả: làm GĐ 1+2 trước rồi kiểm thử bằng Codex ngay (mục 6 🔬).
