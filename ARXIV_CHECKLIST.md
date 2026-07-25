# arXiv submission checklist — Born selectors note

**Manuscript:** `paper_born.md` (source of truth) / `paper_born.tex` (pandoc export)  
**Version:** 4.5  
**Date:** 2026-07-24  
**Suggested arXiv categories:** quant-ph (primary), math-ph (secondary)

## Before upload

- [x] Mathematical claims verified (`verify_selectors.py` ALL PASS)
- [x] Lemma 2 self-contained (irrep decomposition + End=R)
- [x] Theorems 1--4 stated with proofs
- [x] Prop. 3 local selector equivalence
- [x] Ancilla non-selector recorded (negative result)
- [x] Hossenfelder [22] credited for dim-independence lineage
- [x] Nakahira [8] confronted; Conjecture 1 superseded as Born-route
- [x] No "derivation of Born from first principles" overclaim
- [x] OPSEC: no provider names
- [ ] Human pass on English / Polish typos
- [ ] Bibliography DOIs/page numbers spot-check (Massart-Absil, Busch, etc.)
- [ ] Decide author line: Paulina only vs Paulina + Gniewislawa AI disclosure
- [ ] Endorsement if first arXiv (Paulina has arXiv account per profile)
- [ ] Compile `pdflatex paper_born.tex` cleanly (may need manual amsmath polish on pandoc output)
- [ ] Optional: cut Lemma 1 / Sections 3--4 if wanting ultra-short note (selectors only)

## Recommended framing (title/abstract already OK)

Do say:
- elementary selectors inside invariant bilinear class
- classification via representation theory
- apparently-unrecorded corollaries (Thm 1--3)
- layer below Nakahira

Do not say:
- derivation of quantum theory
- new physical principle
- solution of Born-rule problem

## File set for submission folder

```
paper_born.md          # preferred editable source
paper_born.tex         # pandoc export (polish before upload)
verify_selectors.py    # empirical algebra checks
NOTE_nakahira_gap.md   # internal, do not upload
arxiv_src/*.pdf        # local refs, do not upload
```

## Estimated length

~8--12 pages when typeset with proofs; short-note scale.

## Residual risk

1. Priority risk on Thm 1/3: elementary; may exist as exercise/remark.
2. Lemma 2 Claim 1/3 still cites standard absolute-irreducibility facts rather than proving sl_d irreducibility from scratch — acceptable for quant-ph note, math referee may want a reference to Fulton-Harris or Weyl.
3. Pandoc tex is not journal-polished; expect manual pass.
