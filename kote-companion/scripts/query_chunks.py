#!/usr/bin/env python3
"""
query_chunks.py — Query a book_chunks.db built by build_chunk_db.py.

Usage:
    python query_chunks.py DB_PATH "search terms"          # full-text search
    python query_chunks.py DB_PATH --page 42                # exact page dump
    python query_chunks.py DB_PATH --chapter "Chapter 3"     # all chunks in a chapter
    python query_chunks.py DB_PATH --range 40 45             # page range dump

Full-text search uses SQLite FTS5 (supports AND/OR/NOT, "phrase queries",
and prefix* matching). Results are ranked by relevance and include page
numbers for citation.
"""

import argparse
import sqlite3
import sys


def search(conn, query, limit=20):
    rows = conn.execute(
        """
        SELECT c.page, c.chapter, c.text, bm25(chunks_fts) AS rank
        FROM chunks_fts
        JOIN chunks c ON c.chunk_id = chunks_fts.rowid
        WHERE chunks_fts MATCH ?
        ORDER BY rank
        LIMIT ?
        """,
        (query, limit),
    ).fetchall()
    return rows


def by_page(conn, page):
    return conn.execute(
        "SELECT page, chapter, text FROM chunks WHERE page = ? ORDER BY chunk_id", (page,)
    ).fetchall()


def by_range(conn, start, end):
    return conn.execute(
        "SELECT page, chapter, text FROM chunks WHERE page BETWEEN ? AND ? ORDER BY chunk_id",
        (start, end),
    ).fetchall()


def by_chapter(conn, chapter):
    return conn.execute(
        "SELECT page, chapter, text FROM chunks WHERE chapter LIKE ? ORDER BY chunk_id",
        (f"%{chapter}%",),
    ).fetchall()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("db_path")
    ap.add_argument("query", nargs="?", help="Full-text search query")
    ap.add_argument("--page", type=int)
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--chapter")
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db_path)

    if args.page is not None:
        rows = by_page(conn, args.page)
    elif args.range:
        rows = by_range(conn, args.range[0], args.range[1])
    elif args.chapter:
        rows = by_chapter(conn, args.chapter)
    elif args.query:
        rows = search(conn, args.query, args.limit)
    else:
        sys.exit("Provide a search query, --page, --range, or --chapter")

    if not rows:
        print("No results.")
        return

    for row in rows:
        if len(row) == 4:  # search results include rank
            page, chapter, text, _rank = row
        else:
            page, chapter, text = row
        chap_label = f" [{chapter}]" if chapter else ""
        print(f"--- p.{page}{chap_label} ---")
        print(text)
        print()


if __name__ == "__main__":
    main()
