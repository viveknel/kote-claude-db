# Wind from the East — Searchable Index Bundle

This bundle lets Claude answer questions about this book without re-reading the original PDF.

## Files

- **`book_index.md`** — thematic index: chapter summaries, themes, key terms, cross-cutting arguments. Read this first, in full, for any broad/thematic question.
- **`book_chunks.db`** — SQLite database of paragraph-level chunks with full-text search, for precise fact lookup, exact figures, or quote verification. Query it, don't load it in full.
- **`scripts/query_chunks.py`** — command-line helper for querying the DB.

Book: *Wind from the East* (White Wolf, 2000) — 98 pages, indexed 2026-08-16.

## Important: this book belongs to two different libraries

*Wind from the East* is a **Vampire: The Dark Ages** sourcebook, not a *Kindred of the East* title — but it draws heavily on the *Kindred of the East* line and its historical companion *World of Darkness: Blood & Silk*, so it's included here as part of the **Kindred of the East library** (see the top-level `library_index.md` and `library/` directory for the cross-book synthesis across all six books in this collection).

This same bundle is also intended to be folded into a separate **Vampire: The Masquerade / Vampire: The Dark Ages library**, which may be built and read alongside this one in a future session. If both libraries are present together in a conversation, this book is the connective tissue between them — treat it as relevant to cross-library questions about either line, and expect it to be cited from both `library_index.md` files if both exist.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation plus answers to most broad/thematic questions directly.
2. For precise facts, exact numbers, or verifying a quote, query the chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 50
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Two"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing specific facts — this is the audit trail back to the source PDF. Note: page numbers in the database are **PDF page numbers**, which run two pages ahead of the book's own printed page numbers (e.g. printed page 6 = PDF/database page 8) due to unnumbered front matter. `book_index.md` cites the book's own printed page numbers throughout, not PDF page numbers — subtract 2 from a `book_index.md` page reference to get the matching database page.
4. This PDF is OCR-scanned (Adobe Acrobat Capture) rather than a native digital text layer, and many full-page illustrations and stylized chapter-divider pages produced no extractable text at all — this is expected and not a sign of missing content. A handful of running headers and cover/credits text also came through with OCR garbling; the chunk database and index were built and verified around this.
5. Only fall back to the original PDF if both files fail to answer the question (e.g. the question is about a figure, chart, or visual layout that text extraction wouldn't have captured).
