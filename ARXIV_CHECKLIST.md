# arXiv submission checklist - Born selectors note

**Canonical manuscript:** `paper_born.md`
**Public repository version:** 1.0 (2026-07-28)
**Suggested categories:** quant-ph (primary), math-ph (secondary)

## Verified for the public preprint

- [x] Main claims bounded by `THEOREM_LEDGER.md`.
- [x] Selector algebra: `verify_selectors.py` passed.
- [x] Gram-fibre construction: `verify_fibres.py` passed.
- [x] Targeted pytest suite: 14 passed.
- [x] Markdown-to-LaTeX parse passed.
- [x] Citation evidence ledger present.
- [x] Public-source OPSEC scan found no credentials, provider endpoints, or model RIDs.
- [x] No claim of a reconstruction of quantum theory or the Born rule from first principles.

## Still required before an arXiv upload

- [ ] Produce and inspect a clean canonical LaTeX/PDF artifact. The legacy `paper_born.tex` in this repository is not synchronized with Version 1.0.
- [ ] Human English and bibliography proofread.
- [ ] Decide author/disclosure line for the submission metadata.
- [ ] Confirm arXiv endorsement/account workflow if needed.
- [ ] Choose an archival DOI/release policy.

## Public claim boundary

Say: a scoped classification and selector catalogue within a complex-Hermitian, unitarily invariant, real-bilinear family.

Do not say: derivation of quantum theory, derivation of the Hermitian ambient structure, or a solution of the general Born-rule problem.
