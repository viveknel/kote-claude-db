# Hengeyokai: Shapeshifters of the East — Searchable Index Bundle

This bundle lets Claude answer questions about this book without
re-reading the original PDF.

## Files

- **`book_index.md`** — thematic index: chapter summaries, themes, key
  terms, cross-cutting arguments. Read this first, in full, for any
  broad/thematic question.
- **`book_chunks.db`** — SQLite database of paragraph-level chunks with
  full-text search, for precise fact lookup, exact figures, or quote
  verification. Query it, don't load it in full.
- **`scripts/query_chunks.py`** — command-line helper for querying the DB.

Book: *Hengeyokai: Shapeshifters of the East* (White Wolf, 1998) — 174
pages, indexed 2026-08-20.

## Important: an earlier-edition crossover book, shared between two libraries

This book was written to pair with the **original, pre-W20 edition of
*Werewolf: The Apocalypse*** and the **original 1998 *Kindred of the
East*** line. It is likely somewhat inconsistent with *Werewolf: The
Apocalypse 20th Anniversary Edition* (W20) and very likely
significantly inconsistent with *Kindred of the East: The Relentless
Age* — see `book_index.md`'s "Important" section (the very first thing
in that file) for the full detail before treating anything in this book
as consistent with either of those later editions.

This same bundle is intended to be included in **both** a *Werewolf:
The Apocalypse* library and a *Kindred of the East* library. It's a
crossover book in the same spirit as *Wind from the East* (which
crosses *Kindred of the East* into *Vampire: The Dark Ages* from the
other direction) — a *Werewolf* book that treats the Kuei-jin as a
constant offstage rival/antagonist presence throughout. If both
libraries are present together in a conversation, expect this book to
be cited from both top-level `library_index.md` files.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full — it's small and gives you orientation
   plus answers to most broad/thematic questions directly. Read its
   "Important" section first.
2. For precise facts, exact numbers, or verifying a quote, query the
   chunk database instead of guessing from the summary:

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "search terms here"
   python3 scripts/query_chunks.py book_chunks.db --page 60
   python3 scripts/query_chunks.py book_chunks.db --chapter "Chapter Three: Lords of the Beast Courts"
   ```

   Full-text search supports phrase queries (`"exact phrase"`), boolean
   operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching
   (`term*`). Chapter names must match exactly as tagged — see
   `book_index.md` for the full list.
3. Cite page numbers from the chunk results when quoting or referencing
   specific facts — this is the audit trail back to the source PDF.
4. This PDF is an OCR scan (FineReader), not a native digital text
   layer. The book's decorative, hand-lettered chapter-title fonts did
   not OCR at all — chapter boundaries in this bundle were verified by
   visually inspecting each chapter's title page (rasterizing and
   reading it directly), not by searching for chapter-name text, since
   that text isn't reliably present in the extracted text. A handful of
   running headers, footers, and stylized pull-quotes also came through
   garbled; body text is generally clean. Only fall back to the
   original PDF if both this bundle's files fail to answer the
   question.
