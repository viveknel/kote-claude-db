#!/usr/bin/env python3
"""
query_library.py — Full-text search across multiple per-book chunk
databases (each built by build_chunk_db.py) at once.

Use this when you have several single-book bundles (Option B: separate
per-book bundles) and want to search across all of them for a cross-book
question, without merging the databases.

Usage:
    python query_library.py book1.db book2.db book3.db -- "search terms"
    python query_library.py *.db -- "search terms" --limit 10

Results are grouped by book (database file) and ranked within each book
by relevance. This does NOT merge rankings across books — it shows the
top matches per book so you can see which books discuss the topic and
how, side by side.
"""

import argparse
import sqlite3
import sys
from pathlib import Path


def search_one(db_path: str, query: str, limit: int):
    conn = sqlite3.connect(db_path)
    try:
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
    except sqlite3.OperationalError as e:
        print(f"  (query error on {db_path}: {e})", file=sys.stderr)
        rows = []
    finally:
        conn.close()
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("db_paths", nargs="+", help="Paths to book_chunks.db files")
    ap.add_argument("query", help="Full-text search query (FTS5 syntax)")
    ap.add_argument("--limit", type=int, default=5, help="Max results per book (default 5)")
    args = ap.parse_args()

    for db_path in args.db_paths:
        book_label = Path(db_path).parent.name or Path(db_path).stem
        rows = search_one(db_path, args.query, args.limit)
        print(f"=== {book_label} ({db_path}) ===")
        if not rows:
            print("  (no matches)")
        for page, chapter, text, _rank in rows:
            chap_label = f" [{chapter}]" if chapter else ""
            print(f"  --- p.{page}{chap_label} ---")
            for line in text.strip().splitlines():
                print(f"  {line}")
        print()


if __name__ == "__main__":
    main()
