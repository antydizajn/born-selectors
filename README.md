# Born-Rule Selectors under Simultaneous Unitary Invariance and Bilinearity

**Version 1.0 public preprint**
**Author:** Paulina Janowska
**Affiliation:** Independent researcher, Poznan, Poland

## Scope

This repository contains a scoped mathematical-foundations note. It classifies real-bilinear state-effect pairings on `Herm_d` that are invariant under simultaneous unitary conjugation, positive on effects and normalized states.

Within that already assumed complex-Hermitian setting, the pairing has the form

`B(E,rho) = a Tr(E rho) + b Tr(E) Tr(rho)`, with `a + bd = 1`.

The manuscript records elementary conditions that select the Born pairing inside this class, together with explicit limits:

- one impossible orthogonal event;
- one pure self-certainty event;
- dimension-independence of pure transitions;
- perfect distinguishability, with a stated qubit caveat;
- rank-one product monoidality, which gives a Born/state-insensitive dichotomy;
- unbounded idle-ancilla stability, which classifies stable families; combined with one perfect bit, it selects Born globally.

This is **not** a reconstruction of quantum theory or of the Hermitian state/effect structure from operational principles. The manuscript states its representation-theoretic input and its relationship to prior reconstruction work explicitly.

## Canonical files

- `paper_born.md` - canonical public manuscript, Version 1.0.
- `THEOREM_LEDGER.md` - theorem-status and scope ledger.
- `CITATION_EVIDENCE_LEDGER.md` - citation verification record.
- `verify_selectors.py` - deterministic algebraic regression checks.
- `verify_fibres.py` - rectangular and rank-deficient Gram-fibre checks.

The legacy TeX and short-form files in this repository are not the Version 1.0 canonical manuscript and should not be cited as its source.

## Verification

```bash
python3 -m py_compile verify_selectors.py verify_fibres.py
python3 verify_selectors.py
python3 verify_fibres.py
pytest -q verify_selectors.py verify_fibres.py
pandoc --from=markdown --to=latex --output=/dev/null paper_born.md
```

Version 1.0 verification result:

- 14 targeted pytest checks passed;
- both deterministic verifier scripts passed;
- Markdown-to-LaTeX parsing passed;
- `git diff --check` passed before publication.

## Public-claim boundary

The note makes no priority claim for the elementary selector corollaries. In particular, its results classify or select within a pre-specified invariant-bilinear complex-Hermitian family; they do not solve the general Born-rule problem.

## License and citation

A formal license and archival DOI have not yet been attached. Until then, cite the repository URL and the Version 1.0 manuscript date:

`Paulina Janowska, Born-Rule Selectors under Simultaneous Unitary Invariance and Bilinearity, Version 1.0 public preprint (2026-07-28).`
