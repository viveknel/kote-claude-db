# Kindred of the East Library — Searchable Library

A searchable index of seven *Kindred of the East*-related sourcebooks/documents, built so that questions can be answered without re-reading the original PDFs. Each book has its own self-contained bundle (thematic index + full-text search database), and a top-level synthesis layer ties themes together across the six books that share one continuity.

Built with Anthropic's book-indexer skill (Claude reads each source PDF once, extracts and tags its text, then writes a thematic index and a queryable chunk database from it).

## Before you use this library: two things that aren't obvious from the file list

1. **`kote-relentless-age/` is not the same continuity as the other six books.** It's a separate, fan-made reimagining of *Kindred of the East* for V20 — different species name ("Hungry Dead"), a four-Virtue soul system instead of Hun/P'o, a fully restructured Dharma roster, and a "Quincunx" that means something different (a 1449-1979 empire, not the other books' 1304 CE treaty-born institution still standing today). It shares this shelf because it shares the *Kindred of the East* name and broad premise, not because it agrees with the other six books on any fact. See `library_index.md`'s "Important: kote-relentless-age is a different, non-canonical edition" section before cross-referencing it against anything else here, and see its own `kote-relentless-age/README.md` for a page-numbering quirk specific to that book's source file (a 2-page-spread PDF export).
2. **`wind-from-the-east/` is deliberately shared with a second, separate library.** It's a *Vampire: The Dark Ages* book (not a *Kindred of the East* line title) that this library includes because it cross-references and builds on `kote-blood-silk`, but it may also belong to a separate Vampire: The Masquerade/Dark Ages library built in a future session. See `library_index.md`'s "Important: a book shared between two libraries" section.

## What's in here

| Book | Folder | Pages | Continuity |
|---|---|---|---|
| *Kindred of the East* (White Wolf, 1998) | `kote-core/` | 229 | Core line |
| *Kindred of the East Companion* (White Wolf) | `kote-companion/` | 127 | Core line |
| *Shadow War* (White Wolf, 1999) | `kote-shadow-war/` | 103 | Core line |
| *The Thousand Hells* (White Wolf, 1999) | `kote-1000-hells/` | 121 | Core line |
| *World of Darkness: Blood & Silk* (White Wolf, 2000) | `kote-blood-silk/` | 177 | Core line (1197 CE prequel) |
| *Wind from the East* (White Wolf, 2000) | `wind-from-the-east/` | 98 | *Vampire: The Dark Ages* — shared with core line, see note above |
| *Kindred of the East: The Relentless Age* (fan-published, ~2023-2024, V20) | `kote-relentless-age/` | 196 | **Separate, non-canonical reimagining — see note above** |

```
.
├── README.md                  ← you are here
├── library_index.md           ← cross-book synthesis: themes,
│                                  agreements, and disagreements
│                                  (covers the six core-continuity books only)
├── scripts/
│   └── query_library.py       ← search several books' databases at once
├── kote-core/
│   ├── book_index.md          ← thematic index (read this for broad questions)
│   ├── book_chunks.db         ← full-text search database (query for exact facts/quotes)
│   ├── README.md               ← usage instructions for this book's bundle
│   └── scripts/
│       └── query_chunks.py    ← search this book's database alone
├── kote-companion/
│   └── (same four items)
├── kote-shadow-war/
│   └── (same four items)
├── kote-1000-hells/
│   └── (same four items)
├── kote-blood-silk/
│   └── (same four items)
├── wind-from-the-east/
│   └── (same four items)
└── kote-relentless-age/
    └── (same four items)
```

Every book folder is a complete, self-contained bundle — any one of them can be copied out and used entirely on its own, with its own README explaining how.

## Quick start

**Broad or thematic question about one book** — read that book's `book_index.md` directly; it's small enough to load in full and answers most questions without any querying.

**Exact quote, precise fact, or page-number lookup** — query that book's chunk database:

```bash
python3 kote-core/scripts/query_chunks.py kote-core/book_chunks.db "search terms here"
python3 kote-core/scripts/query_chunks.py kote-core/book_chunks.db --page 42
python3 kote-core/scripts/query_chunks.py kote-core/book_chunks.db --chapter "Chapter Name"
```

(swap in any other book's folder name — `kote-companion`, `kote-shadow-war`, `kote-1000-hells`, `kote-blood-silk`, `wind-from-the-east`, or `kote-relentless-age`)

**Question that spans the six core-continuity books** — read `library_index.md` first, then search across the specific books it names if you need exact wording:

```bash
python3 scripts/query_library.py kote-core/book_chunks.db kote-companion/book_chunks.db "search terms"
```

**Question about `kote-relentless-age` specifically** — read its own `book_index.md` and query its own `book_chunks.db` in isolation; don't fold it into a multi-book `query_library.py` call alongside the other six unless the question is explicitly about *comparing* the two continuities (in which case, say clearly which continuity each result comes from).

Full-text search (all scripts) supports phrase queries (`"exact phrase"`), boolean operators (`term1 AND term2`, `term1 NOT term2`), and prefix matching (`term*`).

## Requirements

Python 3 with the standard library only (`sqlite3` is built in — no extra packages to install).

## Notes on scope

- These bundles contain **summaries and short paragraph-level excerpts** for search/citation purposes, not the original books' full text. They're a research aid for someone who already owns the source PDFs, not a substitute for them.
- Mechanically dense chapters/sections are noted in each `book_index.md` as reference material rather than summarized exhaustively — query the relevant `book_chunks.db` directly for that content.
- Where the six core-continuity books genuinely disagree with each other, `library_index.md` calls this out explicitly rather than silently picking one version — see its "Points of disagreement or tension" section.
- `kote-relentless-age` isn't a "disagreement" in that sense — it's a different work entirely that happens to share a name and premise. See the note at the top of this file.
- `kote-core/book_chunks.db` page numbers are PDF page numbers (one ahead of the book's own printed page numbers — see that bundle's README). `kote-relentless-age/book_chunks.db` page numbers represent 2-page printed spreads, not single pages — see that bundle's README before citing a page number from it.

## Adding another related book later

Bring the new PDF plus this repo's `library_index.md` and each existing book's `book_index.md` (chunk databases and original PDFs aren't needed again). Run the indexing workflow on just the new book to produce its own `<slug>/` bundle, then update `library_index.md`'s synthesis sections to fold in what the new book adds, confirms, or complicates — or, if the new book turns out to be a different continuity/edition like `kote-relentless-age`, give it its own "Important" warning section instead of folding it into the synthesis. Re-zip and re-verify the whole library before presenting it again — see `references/cross_book_index.md` in the book-indexer skill for the exact packaging steps.
