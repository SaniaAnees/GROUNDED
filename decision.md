# Architecture Log
# GROUNDED — Architecture Log
Scope: RAG verification engine, built on personal CHIP-8 repo as corpus.
## Decision 1: Manual cosine similarity, no vector DB
Libraries like chromadb/faiss exist and could do this for me, but then
I'd never learn the actual math behind retrieval. Writing cosine
similarity by hand means I understand what's happening, not just
calling a black box.

## Decision 2: Generic ingestion, not CHIP-8-specific
If I hardcode this to only read CHIP-8 files, it only ever works for
one project. Building it to accept any folder + file extensions means
the same code works for any future project, not just this one.

## Decision 3: Local NLI model instead of a second Gemini call
API calls are rate-limited and slow (waiting on a live network response
takes real time). My tests need to check correctness in fractions of a
second, not wait on a live API response — so live-calling Gemini twice
per test would make tests slow and eventually fail from hitting rate
limits. A local model avoids both problems.