"""
lit_search_sciverse.py — Script CLI tìm kiếm tài liệu học thuật qua Sciverse API
Dành cho Phase 1 (Literature Review) của dự án MADM/MCDM.

Usage:
    python lit_search_sciverse.py "AHP TOPSIS laptop selection" --year_min 2018 --top 20
    python lit_search_sciverse.py --meta "analytic hierarchy process" --sort citation
    python lit_search_sciverse.py --expand doi:10.1016/j.eswa.2022.xxx --relation CITATIONS

Output:
    - In kết quả Markdown ra stdout
    - Lưu file .md vào 03_phan-tich/lit_search/ theo timestamp
"""

import os
import sys
import argparse
import json
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Thêm thư mục scripts vào path
_here = Path(__file__).parent
sys.path.insert(0, str(_here))
from sciverse_client import SciverseClient, format_hits_markdown, format_results_markdown


OUTPUT_DIR = Path(r"d:\LogManagement\03_phan-tich\lit_search")


def cmd_agentic(args, client: SciverseClient):
    """Chạy agentic-search (ngữ nghĩa) với tuỳ chọn lọc theo năm."""
    print(f"[Sciverse] agentic-search: '{args.query}'", file=sys.stderr)

    filters = {}
    if args.year_min or args.year_max:
        year_filter = {}
        if args.year_min:
            year_filter["gte"] = args.year_min
        if args.year_max:
            year_filter["lte"] = args.year_max
        filters["publication_published_year"] = year_filter
    if args.lang:
        filters["lang"] = args.lang

    hits = client.agentic_search(
        query=args.query,
        top_k=args.top,
        sub_queries=args.sub_queries,
        filters=filters or None,
    )

    print(f"[Sciverse] Tìm thấy {len(hits)} chunks.\n", file=sys.stderr)

    # Header
    lines = [
        f"# Literature Search: {args.query}",
        f"",
        f"**Phương pháp:** Agentic Search (ngữ nghĩa)  ",
        f"**Năm:** {args.year_min or ''}–{args.year_max or 'nay'}  ",
        f"**Số kết quả:** {len(hits)}  ",
        f"**Ngày chạy:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"---",
        f"",
    ]
    lines.append(format_hits_markdown(hits))

    md = "\n".join(lines)
    return md, hits


def cmd_meta(args, client: SciverseClient):
    """Chạy meta-search (cấu trúc) — lọc theo field, sort theo citation."""
    print(f"[Sciverse] meta-search: '{args.meta_query}'", file=sys.stderr)

    filters = []
    if args.year_min:
        filters.append({
            "field": "publication_published_year",
            "operator": "FILTER_OP_GTE",
            "value": args.year_min,
        })
    if args.year_max:
        filters.append({
            "field": "publication_published_year",
            "operator": "FILTER_OP_LTE",
            "value": args.year_max,
        })
    if args.lang:
        filters.append({
            "field": "language",
            "operator": "FILTER_OP_EQ",
            "value": args.lang,
        })
    if args.venue:
        filters.append({
            "field": "publication_venue_name_unified",
            "operator": "FILTER_OP_MATCH_PHRASE",
            "value": args.venue,
        })
    if args.topic_domain:
        filters.append({
            "field": "topics.dimensions.primary_topic_domain",
            "operator": "FILTER_OP_EQ",
            "value": args.topic_domain,
        })

    # Sort
    sort = None
    if args.sort == "citation":
        sort = [{"field": "citation_count", "order": "SORT_ORDER_DESC"}]
    elif args.sort == "year":
        sort = [{"field": "publication_published_year", "order": "SORT_ORDER_DESC"}]
    elif args.sort == "fwci":
        sort = [{"field": "fwci", "order": "SORT_ORDER_DESC"}]

    # freshness/impact boost (chỉ khi không có sort)
    freshness_boost = "NONE"
    impact_boost = "NONE"
    if not sort:
        freshness_boost = args.freshness_boost.upper() if args.freshness_boost else "NONE"
        impact_boost = args.impact_boost.upper() if args.impact_boost else "NONE"

    resp = client.meta_search(
        query=args.meta_query,
        filters=filters or None,
        sort=sort,
        fields=["title", "doi", "abstract", "author", "publication_published_year",
                "publication_venue_name_unified", "citation_count", "language",
                "unique_id", "doc_id", "keywords"],
        page_size=min(args.top, 200),
        freshness_boost=freshness_boost,
        impact_boost=impact_boost,
    )

    results = resp.get("results", [])
    total = resp.get("total_count", 0)
    print(f"[Sciverse] Tìm thấy {total} bài, trả về {len(results)} bài.\n", file=sys.stderr)

    # Header
    sort_label = args.sort or ("freshness" if freshness_boost != "NONE" else "relevance")
    query_label_meta = args.meta_query or ""
    lines = [
        f"# Literature Search: {query_label_meta}",
        f"",
        f"**Phương pháp:** Meta Search (cấu trúc)  ",
        f"**Năm:** {args.year_min or ''}–{args.year_max or 'nay'}  ",
        f"**Sort:** {sort_label}  ",
        f"**Tổng tìm thấy:** {total} | **Hiển thị:** {len(results)}  ",
        f"**Ngày chạy:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"---",
        f"",
        format_results_markdown(results),
        f"",
        f"---",
        f"",
        f"## Danh sách chi tiết",
        f"",
    ]

    for i, r in enumerate(results, 1):
        title = r.get("title", "Unknown")
        authors = r.get("author", [])
        if isinstance(authors, list):
            author_names = [a.get("name", str(a)) if isinstance(a, dict) else str(a) for a in authors[:3]]
            author_str = ", ".join(author_names)
            if len(authors) > 3:
                author_str += " et al."
        else:
            author_str = str(authors)
        year = r.get("publication_published_year", "")
        venue = r.get("publication_venue_name_unified", "")
        cite = r.get("citation_count", "")
        doi = r.get("doi", "")
        abstract = (r.get("abstract") or "")[:300]
        keywords = ", ".join(r.get("keywords") or [])
        doc_id = r.get("doc_id", "")
        unique_id = r.get("unique_id", "")

        lines.append(f"### [{i}] {title}")
        lines.append(f"**Authors:** {author_str}  ")
        lines.append(f"**Year:** {year} | **Venue:** {venue}  ")
        lines.append(f"**Citations:** {cite} | **DOI:** {doi}  ")
        if keywords:
            lines.append(f"**Keywords:** {keywords}  ")
        if doc_id:
            lines.append(f"**doc_id:** `{doc_id}`  ")
        if unique_id:
            lines.append(f"**unique_id:** `{unique_id}`  ")
        if abstract:
            lines.append(f"\n> {abstract}...\n")
        lines.append("")

    md = "\n".join(lines)
    return md, results


def cmd_expand(args, client: SciverseClient):
    """Mở rộng từ một unique_id — xem bài nào cite nó hoặc nó cite ai."""
    print(f"[Sciverse] paper-relations: '{args.expand}' ({args.relation})", file=sys.stderr)

    resp = client.paper_relations(
        unique_id=args.expand,
        relation=args.relation,
        page_size=min(args.top, 200),
    )

    items = resp.get("items", [])
    total = resp.get("total_count", 0)

    relation_label = {
        "CITATIONS": "bài nào đã cite bài này",
        "REFERENCES": "bài này đã cite ai",
        "RELATED_WORKS": "các bài liên quan",
    }.get(args.relation, args.relation)

    lines = [
        f"# Paper Relations: {args.expand}",
        f"",
        f"**Loại quan hệ:** {relation_label} ({args.relation})  ",
        f"**Tổng:** {total} | **Hiển thị:** {len(items)}  ",
        f"**Ngày chạy:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"---",
        f"",
    ]
    for i, item in enumerate(items, 1):
        lines.append(f"| {i} | {item.get('title', '')} | {item.get('id', '')} ({item.get('id_type', '')}) |")

    md = "\n".join(lines)
    return md, items


def cmd_fulltext(args, client: SciverseClient):
    """Đọc full text của một doc_id."""
    print(f"[Sciverse] content: '{args.fulltext}'", file=sys.stderr)
    text = client.get_full_text(args.fulltext, chunk_size=4000)
    return text, text


def save_output(md: str, query: str) -> Path:
    """Lưu file Markdown ra 03_phan-tich/lit_search/."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = "".join(c if c.isalnum() else "_" for c in query[:40]).strip("_")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = OUTPUT_DIR / f"{ts}_{slug}.md"
    fname.write_text(md, encoding="utf-8")
    return fname


def main():
    parser = argparse.ArgumentParser(
        description="Sciverse literature search cho MADM/MCDM project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Tìm kiếm ngữ nghĩa — evidence chunks
  python lit_search_sciverse.py "AHP TOPSIS laptop selection" --year_min 2019 --top 15

  # Tìm kiếm cấu trúc — danh sách bài sort theo citation
  python lit_search_sciverse.py --meta "multi-criteria decision making" --sort citation --year_min 2018

  # Sort theo freshness (bài gần đây nhất)
  python lit_search_sciverse.py --meta "consumer electronics purchase criteria" --freshness_boost STRONG

  # Xem citations của một bài (dùng unique_id từ meta-search)
  python lit_search_sciverse.py --expand "paper:10.1016/j.eswa.2022.xxx" --relation CITATIONS

  # Đọc full text
  python lit_search_sciverse.py --fulltext "af638b09e29619e6784e..."
        """,
    )

    # Mode
    parser.add_argument("query", nargs="?", help="Tìm kiếm ngữ nghĩa (agentic-search)")
    parser.add_argument("--meta", type=str, dest="meta_query",
                        help="Tìm kiếm cấu trúc (meta-search) theo keyword")
    parser.add_argument("--expand", type=str, help="Xem relations của unique_id")
    parser.add_argument("--fulltext", type=str, help="Đọc full text của doc_id")


    # Filters
    parser.add_argument("--year_min", type=int, default=None)
    parser.add_argument("--year_max", type=int, default=None)
    parser.add_argument("--lang", type=str, default="en")
    parser.add_argument("--venue", type=str, default=None, help="Tên tạp chí/hội nghị")
    parser.add_argument("--topic_domain", type=str, default=None,
                        help="Physical Sciences / Social Sciences / Health Sciences / Life Sciences")

    # Sort & boost
    parser.add_argument("--sort", choices=["citation", "year", "fwci"],
                        default=None, help="Sort field (meta-search only)")
    parser.add_argument("--freshness_boost", choices=["NONE", "MILD", "STRONG"],
                        default="NONE", help="Ưu tiên bài gần đây (meta-search, không sort)")
    parser.add_argument("--impact_boost", choices=["NONE", "MILD", "STRONG"],
                        default="NONE", help="Ưu tiên bài nhiều citations (meta-search, không sort)")

    # Options
    parser.add_argument("--top", type=int, default=20, help="Số kết quả tối đa")
    parser.add_argument("--sub_queries", type=int, default=1,
                        help="Số query cải viết (agentic-search, 0–4)")
    parser.add_argument("--relation", choices=["CITATIONS", "REFERENCES", "RELATED_WORKS"],
                        default="CITATIONS")
    parser.add_argument("--no_save", action="store_true",
                        help="Không lưu file output")

    args = parser.parse_args()

    if not args.query and not args.meta_query and not args.expand and not args.fulltext:
        parser.print_help()
        sys.exit(1)

    client = SciverseClient()

    if args.fulltext:
        md, _ = cmd_fulltext(args, client)
    elif args.expand:
        md, _ = cmd_expand(args, client)
    elif args.meta_query:
        md, _ = cmd_meta(args, client)
    else:
        md, _ = cmd_agentic(args, client)

    # Print
    print(md)

    # Save
    if not args.no_save:
        query_label = args.query or args.meta_query or args.expand or args.fulltext or "search"
        saved = save_output(md, query_label)
        print(f"\n[Sciverse] Đã lưu: {saved}", file=sys.stderr)


if __name__ == "__main__":
    main()
