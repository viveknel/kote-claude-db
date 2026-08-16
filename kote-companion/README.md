# Kindred of the East Companion — Searchable Index Bundle

This bundle lets Claude answer questions about this book without re-reading the original PDF.

## Files

- **`book_index.md`** — thematic index: chapter summaries, themes, key terms, cross-cutting arguments. Read this first, in full, for any broad/thematic question.
- **`book_chunks.db`** — SQLite database of paragraph-level chunks with full-text search, for precise fact lookup, exact figures, or quote verification. Query it, don't load it in full.
- **`scripts/query_chunks.py`** — command-line helper for querying the DB.

Book: *Kindred of the East Companion* (White Wolf) — 127 pages, indexed 2026-08-15.

This book is part of the **Kindred of the East library** — see the top-level `library_index.md` and `library/` directory for the cross-book synthesis across all five books in this collection.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 47
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing specific facts — this is the audit trail back to the source PDF. Note: page numbers in the database are **PDF page numbers**, which run one page ahead of the book's own printed page numbers (e.g. printed page 5 = PDF/database page 6) due to unnumbered front matter.
4. Only fall back to the original PDF if both files fail to answer the question (e.g. the question is about a figure, chart, or visual layout that text extraction wouldn't have captured).
