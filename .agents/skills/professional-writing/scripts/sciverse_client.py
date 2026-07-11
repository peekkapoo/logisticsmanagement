"""
sciverse_client.py — Python client cho Sciverse API (https://api.sciverse.space)
Bao gồm tất cả 7 endpoints: agentic-search, meta-search, meta-catalog,
meta-count, meta-paper-relations, content, resource.

Usage:
    import os
    from sciverse_client import SciverseClient

    client = SciverseClient(token=os.environ["SCIVERSE_API_TOKEN"])

    # Tìm kiếm ngữ nghĩa
    hits = client.agentic_search("AHP TOPSIS laptop selection criteria")

    # Tìm kiếm có cấu trúc
    results = client.meta_search(
        query="multi-criteria decision making",
        filters=[{"field": "publication_published_year", "operator": "FILTER_OP_GTE", "value": 2020}],
        sort=[{"field": "citation_count", "order": "SORT_ORDER_DESC"}]
    )
"""

import os
import sys
import time
import json
import requests
from pathlib import Path
from typing import Optional, List, Dict, Any, Union


BASE_URL = "https://api.sciverse.space"


class SciverseClient:
    """Sciverse API client — bọc tất cả 7 endpoint."""

    def __init__(self, token: Optional[str] = None, timeout: int = 30):
        self.token = token or os.environ.get("SCIVERSE_API_TOKEN", "")
        if not self.token:
            raise ValueError(
                "SCIVERSE_API_TOKEN chưa được set. "
                "Tạo key tại https://sciverse.opendatalab.com/tokens "
                "rồi set: $env:SCIVERSE_API_TOKEN='your_token'"
            )
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        })

    def _get(self, path: str, params: dict = None) -> dict:
        """HTTP GET với retry đơn giản."""
        url = f"{BASE_URL}{path}"
        for attempt in range(3):
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout)
                if resp.status_code == 429:
                    wait = int(resp.headers.get("Retry-After", 10)) + 1
                    print(f"[Sciverse] Rate limited, chờ {wait}s...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp.json()
            except requests.exceptions.Timeout:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        raise RuntimeError("Max retries exceeded")

    def _post(self, path: str, body: dict) -> dict:
        """HTTP POST với retry đơn giản."""
        url = f"{BASE_URL}{path}"
        for attempt in range(3):
            try:
                resp = self.session.post(url, json=body, timeout=self.timeout)
                if resp.status_code == 429:
                    wait = int(resp.headers.get("Retry-After", 10)) + 1
                    print(f"[Sciverse] Rate limited, chờ {wait}s...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp.json()
            except requests.exceptions.Timeout:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        raise RuntimeError("Max retries exceeded")

    # ------------------------------------------------------------------
    # 1. AGENTIC-SEARCH
    # ------------------------------------------------------------------
    def agentic_search(
        self,
        query: str,
        top_k: int = 10,
        sub_queries: int = 0,
        filters: Optional[Dict] = None,
    ) -> List[Dict]:
        """
        Tìm kiếm ngữ nghĩa — trả về evidence chunks có thể trích dẫn.

        Args:
            query: Câu hỏi/chủ đề tìm kiếm (tối đa 4096 ký tự)
            top_k: Số lượng chunks trả về (1–100), mặc định 10
            sub_queries: Số lần cải viết query để tăng recall (0–4)
            filters: Dict lọc theo metadata, ví dụ:
                {
                    "lang": "en",
                    "publication_published_year": {"gte": 2020},
                    "publication_venue_name_unified": "Expert Systems with Applications"
                }
        
        Returns:
            List[Dict] — danh sách hits, mỗi hit có:
                chunk_id, chunk, doc_id, title, abstract, score, offset,
                page_no, author[], citation_count, publication_published_year,
                publication_venue_name_unified, primary_topic_domain
        """
        body = {"query": query, "top_k": top_k, "sub_queries": sub_queries}
        if filters:
            body["filters"] = filters
        data = self._post("/agentic-search", body)
        return data.get("hits", [])

    # ------------------------------------------------------------------
    # 2. META-SEARCH
    # ------------------------------------------------------------------
    def meta_search(
        self,
        query: Optional[str] = None,
        filters: Optional[List[Dict]] = None,
        sort: Optional[List[Dict]] = None,
        fields: Optional[List[str]] = None,
        page: int = 1,
        page_size: int = 25,
        cursor: Optional[str] = None,
        freshness_boost: str = "NONE",
        impact_boost: str = "NONE",
        collection: str = "papers",
    ) -> Dict:
        """
        Tìm kiếm có cấu trúc theo field — metadata bài báo, phân trang.

        Args:
            query: Full-text BM25 fuzzy search. Khi kết hợp với sort thì
                   query chỉ làm filter, không ảnh hưởng xếp hạng.
            filters: List[FilterItem] — [{field, operator, value}]
                Operators: FILTER_OP_EQ/NE/GT/GTE/LT/LTE/IN/NIN/CONTAINS/MATCH/MATCH_PHRASE
                Filterable fields: publication_published_year, citation_count,
                    language, doi, author, publication_venue_name_unified,
                    publication_venue_type, keywords, topics.dimensions.primary_topic_domain
            sort: List[SortItem] — [{field, order}]
                Sortable: citation_count, publication_published_year, fwci,
                    reference_count, influential_citation_count
                order: SORT_ORDER_ASC / SORT_ORDER_DESC
            fields: Danh sách field cần trả (projection). doc_id luôn trả.
            page: Trang hiện tại (≥1). Không kết hợp với cursor.
            page_size: Số record mỗi trang (1–200, mặc định 25)
            cursor: Deep pagination — dùng next_cursor từ response trước.
                    Không kết hợp với page>1.
            freshness_boost: NONE/MILD/STRONG — ưu tiên bài gần đây.
                    Chỉ có hiệu lực khi có query và không có sort.
            impact_boost: NONE/MILD/STRONG — ưu tiên bài được cite nhiều.
                    Chỉ có hiệu lực khi có query và không có sort.
            collection: papers (default) / authors / sources

        Returns:
            Dict: {results, total_count, page, page_size, total_pages,
                   search_time_ms, next_cursor}

        Notes:
            - Phân trang nông: page * page_size ≤ 10,000
            - Phân trang sâu (>10,000): dùng cursor
            - freshness_boost/impact_boost bị bỏ qua khi có sort
        """
        body: Dict[str, Any] = {
            "collection": collection,
            "page": page,
            "page_size": page_size,
        }
        if query:
            body["query"] = query
        if filters:
            body["filters"] = filters
        if sort:
            body["sort"] = sort
        if fields:
            body["fields"] = fields
        if cursor:
            body["cursor"] = cursor
        if freshness_boost != "NONE":
            body["freshness_boost"] = freshness_boost
        if impact_boost != "NONE":
            body["impact_boost"] = impact_boost

        return self._post("/meta-search", body)

    def meta_search_all(
        self,
        query: Optional[str] = None,
        filters: Optional[List[Dict]] = None,
        sort: Optional[List[Dict]] = None,
        fields: Optional[List[str]] = None,
        max_results: int = 200,
        collection: str = "papers",
    ) -> List[Dict]:
        """
        Tiện ích: gọi meta_search và tự paginate qua cursor cho đến khi
        đủ max_results hoặc hết dữ liệu.
        """
        results = []
        cursor = None
        while len(results) < max_results:
            batch_size = min(200, max_results - len(results))
            resp = self.meta_search(
                query=query, filters=filters, sort=sort, fields=fields,
                page_size=batch_size, cursor=cursor, collection=collection,
            )
            batch = resp.get("results", [])
            results.extend(batch)
            cursor = resp.get("next_cursor")
            if not cursor or not batch:
                break
        return results[:max_results]

    # ------------------------------------------------------------------
    # 3. META-CATALOG
    # ------------------------------------------------------------------
    def meta_catalog(
        self,
        collection: str = "papers",
        include_sample_values: bool = False,
    ) -> Dict:
        """
        Xem schema field và khả năng filter/sort của meta-search.

        Args:
            collection: papers / authors / sources
            include_sample_values: Trả về sample values cho enum fields

        Returns:
            Dict: {fields[], default_fields[], filter_operators[]}
        """
        params = {
            "collection": collection,
            "include_sample_values": "true" if include_sample_values else "false",
        }
        return self._get("/meta-catalog", params=params)

    # ------------------------------------------------------------------
    # 4. META-COUNT
    # ------------------------------------------------------------------
    def meta_count(
        self,
        query: Optional[str] = None,
        filters: Optional[List[Dict]] = None,
        collection: str = "papers",
    ) -> int:
        """
        Lấy số lượng bài báo khớp điều kiện (vượt giới hạn 10,000 của meta-search).

        Args:
            query: Full-text fuzzy query (BM25), có thể bỏ qua
            filters: Cùng cú pháp FilterItem[] với meta-search
            collection: papers / authors / sources

        Returns:
            int — số lượng chính xác
        """
        body: Dict[str, Any] = {"collection": collection}
        if query:
            body["query"] = query
        if filters:
            body["filters"] = filters
        data = self._post("/meta-count", body)
        return data.get("count", 0)

    # ------------------------------------------------------------------
    # 5. META-PAPER-RELATIONS
    # ------------------------------------------------------------------
    def paper_relations(
        self,
        unique_id: str,
        relation: str = "CITATIONS",
        page: int = 1,
        page_size: int = 25,
    ) -> Dict:
        """
        Lấy danh sách trích dẫn/bị trích dẫn/related works của một bài báo.

        QUAN TRỌNG: Dùng `unique_id` (dạng "paper:10.1038/xxx"),
        KHÔNG phải `doc_id`! unique_id lấy từ meta_search results.

        Args:
            unique_id: Từ meta_search result, dạng "paper:10.xxxx/xxx"
            relation: "CITATIONS" (ai cite tôi) | "REFERENCES" (tôi cite ai)
                      | "RELATED_WORKS" (bài liên quan)
            page: Trang (≥1)
            page_size: Số item/trang (1–200, default 25)

        Returns:
            Dict: {items[], total_count, page, page_size, total_pages}
        """
        body = {
            "unique_id": unique_id,
            "relation": relation,
            "page": page,
            "page_size": page_size,
        }
        return self._post("/meta-paper-relations", body)

    # ------------------------------------------------------------------
    # 6. CONTENT
    # ------------------------------------------------------------------
    def get_content(
        self,
        doc_id: str,
        offset: Optional[int] = None,
        limit: int = 700,
    ) -> Dict:
        """
        Đọc nội dung full text theo doc_id, hỗ trợ phân đoạn.

        Args:
            doc_id: Từ agentic_search hoặc meta_search results
            offset: Vị trí ký tự bắt đầu đọc (Unicode code points).
                    Nếu None → trả toàn bộ full text.
            limit: Số ký tự tối đa mỗi lần (Unicode), mặc định 700.
                   Chỉ có hiệu lực khi offset được truyền.

        Returns:
            Dict: {text, chars_returned, next_offset, more}
        """
        params: Dict[str, Any] = {"doc_id": doc_id}
        if offset is not None:
            params["offset"] = offset
            params["limit"] = limit
        return self._get("/content", params=params)

    def get_full_text(self, doc_id: str, chunk_size: int = 4000) -> str:
        """
        Tiện ích: đọc toàn bộ full text bằng cách paginate tự động.

        Args:
            doc_id: ID văn bản
            chunk_size: Số ký tự mỗi lần gọi (mặc định 4000)

        Returns:
            str — toàn bộ nội dung Markdown
        """
        parts = []
        offset = 0
        while True:
            result = self.get_content(doc_id, offset=offset, limit=chunk_size)
            text = result.get("text", "")
            parts.append(text)
            if not result.get("more"):
                break
            offset = result.get("next_offset", offset + chunk_size)
        return "".join(parts)

    # ------------------------------------------------------------------
    # 7. RESOURCE
    # ------------------------------------------------------------------
    def get_resource(self, file_name: str, save_path: Optional[str] = None) -> bytes:
        """
        Download hình ảnh, figure hoặc tài liệu nhị phân từ Sciverse.

        QUAN TRỌNG: file_name phải là đường dẫn tương đối từ Sciverse
        (ví dụ: "papers/2025/abcd/fig1.png"), KHÔNG được dùng URL đầy đủ,
        absolute path, ".." hoặc backslash.

        Args:
            file_name: Đường dẫn tương đối resource (từ content Markdown)
            save_path: Nếu cung cấp, lưu file vào đường dẫn này

        Returns:
            bytes — nội dung nhị phân
        """
        url = f"{BASE_URL}/resource"
        resp = self.session.get(
            url, params={"file_name": file_name}, timeout=60
        )
        resp.raise_for_status()
        if save_path:
            Path(save_path).parent.mkdir(parents=True, exist_ok=True)
            Path(save_path).write_bytes(resp.content)
        return resp.content


# ---------------------------------------------------------------------------
# Helper: format hits thành Markdown dễ đọc
# ---------------------------------------------------------------------------
def format_hits_markdown(hits: List[Dict]) -> str:
    """Format agentic_search hits thành Markdown để dễ đọc và trích dẫn."""
    lines = []
    for i, h in enumerate(hits, 1):
        title = h.get("title", "Unknown")
        authors = ", ".join(h.get("author", [])[:3])
        if len(h.get("author", [])) > 3:
            authors += " et al."
        year = h.get("publication_published_year", "")
        venue = h.get("publication_venue_name_unified", "")
        cite = h.get("citation_count", "")
        doc_id = h.get("doc_id", "")
        chunk = h.get("chunk", "")
        score = h.get("score", 0)

        lines.append(f"### [{i}] {title}")
        lines.append(f"**Authors:** {authors} | **Year:** {year} | **Venue:** {venue}")
        if cite:
            lines.append(f"**Citations:** {cite} | **Score:** {score:.3f} | **doc_id:** `{doc_id}`")
        lines.append(f"\n> {chunk}\n")
    return "\n".join(lines)


def format_results_markdown(results: List[Dict]) -> str:
    """Format meta_search results thành Markdown table."""
    lines = [
        "| # | Title | Year | Venue | Citations | DOI |",
        "|---|-------|------|-------|-----------|-----|",
    ]
    for i, r in enumerate(results, 1):
        title = (r.get("title") or "")[:60] + ("..." if len(r.get("title", "")) > 60 else "")
        year = r.get("publication_published_year", "")
        venue = (r.get("publication_venue_name_unified") or "")[:30]
        cite = r.get("citation_count", "")
        doi = r.get("doi", "")
        lines.append(f"| {i} | {title} | {year} | {venue} | {cite} | {doi} |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Quick-test CLI
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse
    sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Sciverse API Client Test")
    parser.add_argument("--test", action="store_true", help="Chạy quick test")
    parser.add_argument("--search", type=str, help="Tìm kiếm ngữ nghĩa")
    parser.add_argument("--meta", type=str, help="Meta-search theo keyword")
    parser.add_argument("--top_k", type=int, default=5)
    args = parser.parse_args()

    client = SciverseClient()

    if args.test:
        print("=== TEST: agentic_search ===")
        hits = client.agentic_search(
            "AHP TOPSIS multi-criteria decision making laptop selection",
            top_k=3,
            filters={"lang": "en", "publication_published_year": {"gte": 2018}},
        )
        print(f"Found {len(hits)} hits")
        for h in hits:
            print(f"  - [{h.get('publication_published_year')}] {h.get('title','')[:80]}")
            print(f"    Citations: {h.get('citation_count')} | doc_id: {h.get('doc_id','')[:20]}...")

        print("\n=== TEST: meta_search ===")
        resp = client.meta_search(
            query="analytic hierarchy process criteria weights",
            filters=[
                {"field": "publication_published_year", "operator": "FILTER_OP_GTE", "value": 2019},
                {"field": "language", "operator": "FILTER_OP_EQ", "value": "en"},
            ],
            sort=[{"field": "citation_count", "order": "SORT_ORDER_DESC"}],
            page_size=5,
        )
        print(f"Total: {resp.get('total_count')} | Returned: {len(resp.get('results', []))}")
        for r in resp.get("results", []):
            print(f"  - [{r.get('publication_published_year')}] {r.get('title','')[:70]}")
            print(f"    Citations: {r.get('citation_count')} | doi: {r.get('doi','')}")

    elif args.search:
        hits = client.agentic_search(args.search, top_k=args.top_k)
        print(format_hits_markdown(hits))

    elif args.meta:
        resp = client.meta_search(
            query=args.meta,
            filters=[{"field": "publication_published_year", "operator": "FILTER_OP_GTE", "value": 2018}],
            sort=[{"field": "citation_count", "order": "SORT_ORDER_DESC"}],
            page_size=args.top_k,
        )
        print(format_results_markdown(resp.get("results", [])))
        print(f"\nTotal found: {resp.get('total_count')}")
