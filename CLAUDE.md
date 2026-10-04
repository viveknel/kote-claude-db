# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not a software project — a searchable knowledge base of eight *Kindred of the East* (KotE)-related RPG books, produced by the book-indexer skill. There is no build, lint, or test tooling. Python 3 stdlib only (`sqlite3`). The original PDFs are not in the repo; only summaries and short paragraph-level excerpts are, so never present chunk text as the books' full text.

## Layout

Each book folder (`kote-core`, `kote-companion`, `kote-shadow-war`, `kote-1000-hells`, `kote-blood-silk`, `wind-from-the-east`, `hengeyokai`, `kote-relentless-age`) is a self-contained bundle:
- `book_index.md` — thematic index; read in full for broad questions.
- `book_chunks.db` — SQLite with `chunks(chunk_id, page, chapter, section, text)` plus an external-content FTS5 table `chunks_fts` (porter tokenizer, `content_rowid=chunk_id`). Query it, don't dump it.
- `README.md` — per-book quirks (page numbering, OCR issues).
- `scripts/query_chunks.py` — identical copy in every bundle, kept so a bundle can be copied out alone. If you change one, change all.

Top level: `library_index.md` (cross-book synthesis) and `scripts/query_library.py` (multi-DB search).

## Querying

```bash
# single book: full-text, or --page N, --range START END, --chapter "name", --limit N
python scripts/query_library.py kote-core/book_chunks.db kote-companion/book_chunks.db "search terms" --limit 5
python kote-core/scripts/query_chunks.py kote-core/book_chunks.db "search terms"
python kote-core/scripts/query_chunks.py kote-core/book_chunks.db --page 42
```

Queries use FTS5 syntax (`"phrase"`, `AND`/`OR`/`NOT`, `prefix*`). `query_library.py` takes the DB paths followed by the query as the last positional argument (its docstring's `--` separator is not needed) and shows top matches per book, not a merged ranking. Windows shell: use `python`, not `python3`.

## Continuity rules (the non-obvious part)

Answering well means keeping continuities separate; read `library_index.md`'s "Important" sections before cross-referencing:
- **Six same-continuity books**: `kote-core`, `kote-companion`, `kote-shadow-war`, `kote-1000-hells`, `kote-blood-silk` (1197 CE prequel), `wind-from-the-east` (a *Vampire: The Dark Ages* book shared with another library). `library_index.md`'s themes/agreements/disagreements cover only these.
- **`kote-relentless-age`** is a fan-made V20 reimagining ("Hungry Dead", four-Virtue soul system, different Dharmas, a 1449–1979 "Quincunx" vs. the 1304 CE Treaty of the Quincunx). Same names are false friends. Query it in isolation; if comparing, state which continuity each fact comes from. Its DB pages are 2-page spreads.
- **`hengeyokai`** is a *Werewolf* book (OCR-scanned, 1998) whose Kuei-jin material is thin; same continuity as the six core books but never mix it with `kote-relentless-age` in one query, and don't use it to cross-verify Kuei-jin facts.
- `kote-core/book_chunks.db` page numbers are PDF pages, one ahead of printed page numbers.

## Maintaining the library

Adding a book means running the book-indexer workflow on the new PDF to produce a new `<slug>/` bundle, then updating `README.md` (book table, tree, quick-start lists) and `library_index.md` (books list, synthesis sections, or a new "Important" warning if it's a different continuity/edition). Several statements ("eight databases", "six core books") are hard-coded in those two files and need updating together.
