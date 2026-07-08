# Timeline dự án

> Nhóm trưởng điền deadline bằng cách tính lùi từ ngày nộp. Cột "Người phụ trách" điền theo mã task trong README mục 5.
>
> Ngày nộp báo cáo: `..../..../2026` · Ngày thuyết trình: `..../..../2026`

| Phase | Nội dung chính | Deadline | Người phụ trách | Trạng thái |
|---|---|---|---|---|
| 0 | Khởi động, chốt scope, rubric | | AI / Team | ✅ Xong |
| 1 | Literature review, bộ tiêu chí sơ bộ | | AI / Team | ✅ [Hoàn thành] |
| 2 | Phỏng vấn chuyên gia, hiệu chỉnh tiêu chí | | | ⏳ [Đang làm] |
| 3 | Khảo sát Likert, chốt bộ tiêu chí cuối | | | ⬜ Chưa làm |
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
- [x] T1.6 | Họp nhóm rà soát và chốt danh sách sơ bộ | *Chốt 11 tiêu chí*

### Phase 2: Phỏng vấn chuyên gia & Thu thập dữ liệu (Expert Interview & Data Gathering)
**Trạng thái:** ⏳ [Đang làm]

*Ký hiệu trạng thái: ⬜ Chưa làm · 🔄/⏳ Đang làm · ✅ Xong (đạt DoD + đã tạo ZIP sao lưu)*

**Tasks:**
- [x] T2.1 | Viết kịch bản phỏng vấn bán cấu trúc | Bản **v3.0 song ngữ VN-EN** tại `03_phan-tich/phong-van/` (13 câu, 5 phần + 3 phụ lục). Áp IPR Framework + Delphi–AHP + Cognitive Probing. Đã sửa 3 lỗi trích dẫn của bản v2.0 và hòa giải RQ với bộ RQ chính thức. Bản v1.0/v2.0 cũ lưu trữ. **⏳ chờ nhóm duyệt + pilot test.**
- [x] T2.2 | Lập danh sách chuyên gia dự kiến | `00_quan-ly-du-an/bien-ban-hop/2026-07-05_danh-sach-chuyen-gia.md`
- [ ] T2.3 | Phỏng vấn 3-5 chuyên gia thực tế (sau khi pilot test kịch bản) | Ghi chú lưu `02_du-lieu-tho/phong-van/`
- [ ] T2.4 | Tổng hợp, mã hóa dữ liệu phỏng vấn, hiệu chỉnh bộ tiêu chí | `03_phan-tich/`
- [ ] T2.5 | Họp nhóm chốt bộ tiêu chí sau phỏng vấn | —

> ⚠️ **Việc treo cần thống nhất:** persona nghiên cứu — `01-introduction.tex` (problem statement) ghi "người thiết kế đồ họa", lệch với "nhân viên văn phòng" ở tiêu chí v5.0 và kế hoạch Phase 2. Kịch bản v3.0 dùng nhất quán "nhân viên văn phòng".

## Phân công task chi tiết

Bảng dưới điền dần khi nhóm họp phân công. Mã task tra trong README mục 5.

| Mã task | Người làm | Deadline | Ghi chú |
|---|---|---|---|
| T0.1 - T0.4 | AI / Nhóm | 2026-07-04 | Đã hoàn thành (chốt rules, workspace, scope) |
| T1.1 | AI | 2026-07-04 | Đã tạo query tìm kiếm |
| T1.2 | AI | 2026-07-04 | Đã thu thập và đổi tên 17 bài báo |
| T1.3 | | | Đọc và trích xuất tiêu chí (NEXT) |

## Mốc đã hoàn thành

| Ngày | Sự kiện |
|---|---|
| 2026-07-04 | Khởi tạo workspace, README, kế hoạch tổng thể, push GitHub |
| 2026-07-04 | Hoàn thành T1.1, T1.2: Thu thập 17 bài báo khoa học, phân loại vào `01_tai-lieu-tham-khao` |
| 2026-07-05 | Đóng Phase 1: chốt bộ 14 tiêu chí (`v5.0_final_user.md`) + Literature Review sau khi deep-read 15 bài |
| 2026-07-05 | T2.1 (v1.0) + T2.2: kịch bản phỏng vấn sơ bộ và danh sách chuyên gia |
| 2026-07-09 | T2.1 (v3.0 song ngữ VN-EN): viết mới kịch bản, sửa 3 lỗi trích dẫn, hòa giải RQ; chờ pilot test |
