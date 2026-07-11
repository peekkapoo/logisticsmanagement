# Timeline dự án

> Nhóm trưởng điền deadline bằng cách tính lùi từ ngày nộp. Cột "Người phụ trách" điền theo mã task trong README mục 5.
>
> Ngày nộp báo cáo: `..../..../2026` · Ngày thuyết trình: `..../..../2026`

| Phase | Nội dung chính | Deadline | Người phụ trách | Trạng thái |
|---|---|---|---|---|
| 0 | Khởi động, chốt scope, rubric | | AI / Team | ✅ Xong |
| 1 | Literature review, bộ tiêu chí sơ bộ | | AI / Team | ✅ [Hoàn thành] |
| 2 | Phỏng vấn chuyên gia, hiệu chỉnh tiêu chí | | | ✅ [Hoàn thành] |
| 3 | Khảo sát Likert, chốt bộ tiêu chí cuối | | | ⏳ [Đang làm] |
| 4 | AHP, chốt trọng số | | | ⬜ Chưa làm |
| 5 | Dữ liệu laptop, TOPSIS, sensitivity | | | ⬜ Chưa làm |
| 6 | Báo cáo LaTeX EN, slide EN, nộp bài | | | ⬜ Chưa làm |

### Phase 1: Tổng quan tài liệu & Tiêu chí sơ bộ (Literature Review) 
**Trạng thái:** ✅ [Hoàn thành]
**Mục tiêu:** Trích xuất các tiêu chí kỹ thuật và trải nghiệm từ tối thiểu 15-20 bài báo học thuật.
**Tasks:**
- [x] T1.1 | Thu thập tài liệu (đầu vào: Scholar, Consensus, Elicit) | Thư mục `01_tai-lieu-tham-khao\`
- [x] T1.2 | Lọc tài liệu theo PRISMA (tiêu đề, tóm tắt) | Cập nhật file `.bib` và logs
- [x] T1.3 | Đọc từng bài, trích tiêu chí vào bảng tổng hợp kèm đủ tác giả, năm, tạp chí, DOI, số trang | `tong-hop-tieu-chi.md`
- [x] T1.4 | Nhập nguồn vào `references.bib` ngay khi đọc xong từng bài | `references.bib`
- [x] T1.5 | Gộp tiêu chí trùng lặp, phân nhóm (hiệu năng, giá, thiết kế, dịch vụ...), lập danh sách tiêu chí sơ bộ | `03_phan-tich\tieu-chi\`
- [x] T1.6 | Họp nhóm rà soát và chốt danh sách sơ bộ | *Chốt 11 tiêu chí sơ bộ; sau tinh chỉnh cuối Phase 1 thành 14 tiêu chí chính thức (`v5.0_final_user.md`)*

### Phase 2: Phỏng vấn chuyên gia & Thu thập dữ liệu (Expert Interview & Data Gathering)
**Trạng thái:** ✅ [Hoàn thành]

*Ký hiệu trạng thái: ⬜ Chưa làm · 🔄/⏳ Đang làm · ✅ Xong (đạt DoD + đã tạo ZIP sao lưu)*

**Tasks:**
- [x] T2.1 | Viết kịch bản phỏng vấn bán cấu trúc | Bản **v3.0 song ngữ VN-EN** tại `03_phan-tich/phong-van/` (13 câu, 5 phần + 3 phụ lục). Áp IPR Framework + Delphi–AHP + Cognitive Probing. Đã sửa 3 lỗi trích dẫn của bản v2.0 và hòa giải RQ với bộ RQ chính thức. Bản v1.0/v2.0 cũ lưu trữ.
- [x] T2.2 | Lập danh sách chuyên gia dự kiến | `00_quan-ly-du-an/bien-ban-hop/2026-07-05_danh-sach-chuyen-gia.md`
- [x] T2.3 | Phỏng vấn 5 chuyên gia thực tế (CG-01 đến CG-05: nhân viên hành chính, quản lý IT, nhân viên chứng từ, trưởng phòng phát triển sản phẩm, nhân viên tư vấn bán hàng) | `CG-01.docx`, `CG-02.docx` (gốc); kết quả trích xuất tại `03_phan-tich/phong-van/expert_result_01.md` đến `expert_result_05.md`
- [x] T2.4 | Tổng hợp, mã hóa dữ liệu phỏng vấn (Thematic Analysis), hiệu chỉnh bộ tiêu chí | `03_phan-tich/phong-van/2026-07-10_phan-tich-phong-van_v1.0_draft_AI.md`; tiêu chí hiệu chỉnh tại `03_phan-tich/tieu-chi/2026-07-11_danh-sach-tieu-chi-sau-phong-van_v2.0_draft_AI.md` (n=5, bản v1.0 cũ ở `_cu/`)
- [x] T2.5 | Chốt bộ tiêu chí sau phỏng vấn | **Chốt 14 tiêu chí** (loại GPU, giữ nguyên 13 tiêu chí còn lại + bổ sung "Tương thích phần mềm"), duyệt bởi user 2026-07-10

> ✅ **Đã chốt persona (2026-07-09):** toàn dự án dùng nhất quán **"nhân viên văn phòng"**; persona "thiết kế đồ họa" đã loại bỏ. Đã sửa `01-introduction.tex` cho khớp tiêu chí v5.0 và kịch bản v3.0.

### Phase 3: Khảo sát Likert & Chốt bộ tiêu chí cuối
**Trạng thái:** ⏳ [Đang làm]

**Tasks:**
- [x] T3.1 | Dựng Google Form thang Likert 5 điểm từ 14 tiêu chí sau phỏng vấn | `03_phan-tich/khao-sat/2026-07-10_kich-ban-khao-sat-likert_v1.0_draft_AI.md`
- [ ] T3.2 | Chạy thử với 5-10 người | —
- [ ] T3.3 | Xác định cỡ mẫu mục tiêu và kênh phát | —
- [ ] T3.4 | Thu thập phản hồi, xuất CSV | `02_du-lieu-tho/khao-sat/`
- [ ] T3.5 | Phân tích mean/độ lệch chuẩn từng tiêu chí | `03_phan-tich/tieu-chi/likert-thu-thap-phan-tich.xlsx`
- [ ] T3.6 | Chốt ngưỡng giữ/loại (mặc định 3.5) và bộ tiêu chí cuối cùng | `03_phan-tich/tieu-chi/`

## Phân công task chi tiết

Bảng dưới điền dần khi nhóm họp phân công. Mã task tra trong README mục 5.

| Mã task | Người làm | Deadline | Ghi chú |
|---|---|---|---|
| T0.1 - T0.4 | AI / Nhóm | 2026-07-04 | Đã hoàn thành (chốt rules, workspace, scope) |
| T1.1 | AI | 2026-07-04 | Đã tạo query tìm kiếm |
| T1.2 | AI | 2026-07-04 | Đã thu thập và đổi tên 17 bài báo |
| T1.3 | | | Đọc và trích xuất tiêu chí (NEXT) |
| T2.3 | AI | 2026-07-10 | Phỏng vấn 5 chuyên gia (CG-01 → CG-05) |
| T2.4 - T2.5 | AI / User | 2026-07-10/11 | Tổng hợp, chốt 14 tiêu chí sau phỏng vấn (v2.0) |
| T3.1 | AI | 2026-07-10 | Dựng kịch bản khảo sát Likert v1.0 |

## Mốc đã hoàn thành

| Ngày | Sự kiện |
|---|---|
| 2026-07-04 | Khởi tạo workspace, README, kế hoạch tổng thể, push GitHub |
| 2026-07-04 | Hoàn thành T1.1, T1.2: Thu thập 17 bài báo khoa học, phân loại vào `01_tai-lieu-tham-khao` |
| 2026-07-05 | Đóng Phase 1: chốt bộ 14 tiêu chí (`v5.0_final_user.md`) + Literature Review sau khi deep-read 15 bài |
| 2026-07-05 | T2.1 (v1.0) + T2.2: kịch bản phỏng vấn sơ bộ và danh sách chuyên gia |
| 2026-07-09 | T2.1 (v3.0 song ngữ VN-EN): viết mới kịch bản, sửa 3 lỗi trích dẫn, hòa giải RQ |
| 2026-07-10 | T2.3: hoàn thành phỏng vấn 5 chuyên gia (CG-01 → CG-05) |
| 2026-07-10/11 | T2.4-T2.5: tổng hợp Thematic Analysis, chốt bộ 14 tiêu chí sau phỏng vấn (v2.0, n=5) → đóng Phase 2 |
| 2026-07-10 | T3.1: dựng kịch bản khảo sát Likert v1.0 (14 tiêu chí), mở Phase 3 |
