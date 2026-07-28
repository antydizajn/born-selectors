# Citation Evidence Ledger for `paper_born.md`

**Audit date:** 2026-07-27
**Manuscript audited:** `paper_born.md` v1.0 (public preprint)
**Purpose:** distinguish metadata verification, source-level claim verification, and claims that must remain scoped.

## Verification levels

- **SOURCE-LEVEL VERIFIED:** the relevant source text was read locally or directly and supports the specific manuscript use.
- **METADATA VERIFIED:** title, author list, and existence were checked against a primary publisher, arXiv, or equivalent scholarly record; the exact manuscript claim still requires a source-level read before submission.
- **SCOPED / NON-LOAD-BEARING:** the reference is background only and must not carry a theorem claim in this manuscript.

## Load-bearing citations

| Manuscript ref. | Source | Status | Permitted use in this manuscript | Evidence checked |
|---|---|---|---|---|
| [1] | Hossenfelder, arXiv:2006.14175 | SOURCE-LEVEL VERIFIED | Restricted comparison for dimension-independence of pure-state transition probabilities. | Local `arxiv_src/hossenfelder.txt`, plus publisher/ADS metadata. |
| [2] | Nakahira, arXiv:2605.23217 | SOURCE-LEVEL VERIFIED | State the exact finite-dimensional causal OPT assumptions and reconstruction conclusion only as given in the source. Keep the preprint status and the manuscript caveat. | Local `arxiv_src/nakahira.txt`; arXiv record. |
| [3] | Galley and Masanes, arXiv:1610.04859 | SOURCE-LEVEL VERIFIED | Broader landscape of alternative measurement postulates. Do not promote the manuscript's bilinear slice to a classification of all alternatives. | Local `arxiv_src/galley_masanes.txt`, local `NOTE_galley_masanes.md`, and arXiv record. |
| [4] | Lax, arXiv:2604.27339 | SOURCE-LEVEL VERIFIED | Comparison to a different Fisher/Cramer-Rao route only. Do not use it as support for Lemma 2 or a novelty claim. | arXiv abstract read directly. |
| [5] | Gleason, J. Math. Mech. 6, 885-893, 1957 | METADATA VERIFIED | Classical comparison: additive measures on closed subspaces in dimension at least three. | Scholarly metadata and primary-paper search snippet; direct PDF fetch returned HTTP 403 in this audit. |
| [6] | Busch, Phys. Rev. Lett. 91, 120403, 2003 | SOURCE-LEVEL VERIFIED | POVM-based extension/comparison only. | arXiv abstract read directly; APS metadata cross-check. |
| [7] | Chiribella, D'Ariano, Perinotti, arXiv:1011.6451 | SOURCE-LEVEL VERIFIED | Example of an informational reconstruction, not a proof of any result here. | arXiv abstract read directly; ADS metadata cross-check. |
| [8] | Barnum and Wilce, arXiv:1202.4513 | SOURCE-LEVEL VERIFIED | Example of Jordan/local-tomography reconstruction literature. | arXiv abstract read directly. |
| [9] | Tull, arXiv:1804.02265 | SOURCE-LEVEL VERIFIED | Example of categorical reconstruction literature. | arXiv abstract read directly; LMCS record cross-check. |
| [10] | Selby, Scandolo, Coecke, arXiv:1802.00367 | SOURCE-LEVEL VERIFIED | Example of diagrammatic reconstruction literature. | arXiv abstract read directly. |
| [11] | Procesi, arXiv:2011.10820 | SOURCE-LEVEL VERIFIED | Context for polynomial equivariant maps only. Do not claim that it formally proves Lemma 1. | arXiv abstract read directly. |
| [12] | Massart and Absil, SIAM J. Matrix Anal. Appl. 41(1), 171-198, 2020 | METADATA VERIFIED | Context for fixed-rank PSD quotient geometry only. | Publisher and author-page metadata. |
| [13] | Hardy and Wootters, arXiv:1005.4870 | SOURCE-LEVEL VERIFIED | Real-vector-space QM fails local tomography in the standard composite setting. | arXiv abstract read directly and scholarly index metadata. |
| [14] | Barrett, arXiv:quant-ph/0508211 | SOURCE-LEVEL VERIFIED | GPT framework and Boxworld background only. | arXiv abstract read directly and ADS metadata. |

## Explicitly excluded claims

The manuscript must not claim any of the following from this bibliography:

1. A reconstruction of the Born rule or complex quantum theory from the selectors in `paper_born.md`.
2. Priority for Theorems 1, 2, 3, or 5.
3. A complete R/C/H classification or any theorem about the quaternionic branch.
4. That Lemma 2 is self-contained. It is conditional on the standard real irreducibility/scalar-commutant input stated in Section 5.2.
5. That Stinespring or Kraus theory resolves the operational uniqueness question called Problem B.
6. Priority for the strengthened Theorem 5. The statement removes a redundant orthogonality premise and derives it from the equality cases; it is recorded as a strengthened corollary, not a novelty claim.
7. That the former SVD proof of Proposition 1 remains valid. It was replaced in v5.3 by a rectangular-safe partial-isometry proof and a dedicated fibre verifier.
8. Priority for Proposition 4. It is an elementary positivity-limit argument inside the classified family and is presented without a novelty claim.

## Bibliography hygiene

The bibliography is now citation-ordered and contains only entries cited in the manuscript body: [1] through [14]. No unused entries remain.

## Verification record

- `python3 verify_selectors.py`: ALL PASS.
- Citation IDs in the manuscript body occur in first-citation order [1] through [14], exactly matching the bibliography.
- Bibliography numbering is citation-ordered and contiguous [1] through [14].
- `pandoc --from=markdown --to=latex`: PASS.

**Submission gate:** this ledger is an evidence record, not a substitute for reading every source. Any sentence that becomes load-bearing during revision must be upgraded to SOURCE-LEVEL VERIFIED before public submission.
