# Kindred of the East: The Relentless Age — Searchable Index Bundle

This bundle lets Claude answer questions about this book without re-reading the original PDF.

## Files

- **`book_index.md`** — thematic index: chapter summaries, themes, key terms, cross-cutting arguments. Read this first, in full, for any broad/thematic question.
- **`book_chunks.db`** — SQLite database of paragraph-level chunks with full-text search, for precise fact lookup, exact figures, or quote verification. Query it, don't load it in full.
- **`scripts/query_chunks.py`** — command-line helper for querying the DB.

Book: *Kindred of the East: The Relentless Age* (fan-published via Storytellers Vault, built for V20; indicia reads "© 2017" but internal/metadata evidence points to 2023-2024 — see `book_index.md`'s warning section) — 196 printed pages (100 PDF pages, 2-page-spread layout), indexed 2026-08-16.

## Before you use this bundle: it is a different, non-canonical edition

This book is part of the **Kindred of the East library** (see the top-level `library_index.md` and `README.md`), but unlike this library's other five books, it is **not the same continuity**. It's a fan-made reimagining that renames the species ("Hungry Dead," not "Kuei-jin"), replaces the two-soul Hun/P'o system with four Virtues, restructures the Dharmas entirely, and gives "the Quincunx" a different history (a 1449-1979 empire toppled in 1979) than the original line's Quincunx (a 1304 CE treaty-born institution still standing in the modern nights). It also runs on V20 rules rather than the original *Vampire* rules the rest of the library assumes. See `book_index.md`'s "Important" section for the full list of contradictions before treating anything in this bundle as consistent with `kote-core`, `kote-companion`, `kote-shadow-war`, `kote-1000-hells`, or `kote-blood-silk`.

## Page-numbering convention (read before citing page numbers)

The source PDF is a **2-page-spread export**: 100 PDF pages, each rendered as two printed book pages side by side (printed pages run 1-197ish; PDF pages 1-3 are unnumbered front matter). Splitting each spread into its two individual pages during extraction proved unreliable for this file (its own internal 2-column layouts on many single pages made automated left/right cropping bleed content across the boundary), so **`book_chunks.db` stores one `page` value per spread — the lower/even printed page number** — and that entry's text can contain material from both that page and the next (odd) one.

**To look up a specific printed page:**
- Even printed page (e.g. 12) → query `--page 12` directly.
- Odd printed page (e.g. 13) → query `--page 12` (its spread-mate); page 12's results will include page 13's content too.

The conversion from PDF page number to printed page range, if you ever need to go back to the original file: for PDF page *N* (4 ≤ *N* ≤ 100), the spread covers printed pages `2N-4` and `2N-3`. PDF pages 1-3 (cover, poem/title spread, credits/TOC spread) are unnumbered front matter and are stored as `page=0`.

Chapter tagging in this bundle is applied at the spread level, with two exceptions (Appendix I→II and Appendix II→Errata) where the transition happens mid-spread with substantial text on both sides — those two spreads were split by `chunk_id` rather than by page so the chapter tag stays accurate.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation plus answers to most broad/thematic questions directly. **Read its "Important" warning section before cross-referencing this book against the rest of the library.**
2. For precise facts, exact numbers, or verifying a quote, query the chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 128
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter 6"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching (`term*`).
3. Cite page numbers from the chunk results when quoting or referencing specific facts — but remember each stored page number represents a 2-page spread (see above), not a single printed page.
4. Only fall back to the original PDF if both files fail to answer the question (e.g. the question is about a figure, chart, or visual layout that text extraction wouldn't have captured).
