# 2h session deliverable — Born programme

**Window start:** 2026-07-24 12:11 CEST  
**Status file:** living  
**Main MS:** `paper_born.md` **v4.7** (410 lines)

## What was produced

| Artifact | Role |
|----------|------|
| `paper_born.md` v4.7 | Main mathematical note |
| `paper_born.tex` | pandoc export for arXiv polish |
| `verify_selectors.py` | 8/8 PASS algebra checks |
| `NOTE_nakahira_gap.md` | Nakahira supersedes Conjecture 1 as Born-route |
| `NOTE_galley_masanes.md` | bilinear slice vs full alternative landscape |
| `PROBLEM_A_amplitude_representations.md` | residual open problem |
| `PROBLEM_A_partial_results.md` | classical/real/complex obstructions |
| `ARXIV_CHECKLIST.md` | submission checklist |
| `arxiv_src/*.pdf` | local PDFs Nakahira/Hossenfelder/Galley-Masanes |

## Mathematical gains this session

1. **Prop. 3:** Thm1 ≡ Thm3 ≡ Born under Lemma 2 + normalization.
2. **Thm 5 (new):** perfect distinguishability of orthogonal pures by an effect  
   - $d\geq 3$: forces Born alone  
   - $d=2$: allows anti-Born $a=-1$, killed by Thm1/3  
3. **Failed ancilla-independence** recorded (does not select Born).
4. **Nakahira honesty:** Conjecture 1 superseded as OPT-level Born derivation.
5. **Galley–Masanes honesty:** we study bilinear *slice*, not full alternative classification.
6. **Hossenfelder honesty:** Thm4 = dim-indep step only; her paper also uses orthogonal vanishing.

## Selector catalogue (final)

```
Lemma 2: bilinear + U-invariant => B = a Tr(E rho) + b Tr(E)Tr(rho)
         a + b d = 1, a in [-1/(d-1), 1]

Thm1/3 (equivalent local): impossible event / pure self-certainty => Born
Thm2: rank-one product monoidality + nontrivial => Born
Thm4: dimension independence => Born  [Hossenfelder lineage]
Thm5: perfect distinguishability => Born (d>=3); a in {1,-1} (d=2)
FAIL: ancilla independence => only a stable across dim
```

## Honest grade (no sugar)

| Criterion | Score |
|-----------|------:|
| Correctness of selectors | 9/10 |
| Novelty depth | 5/10 |
| Foundational impact | 3/10 |
| arXiv short-note readiness | 8/10 |
| Overclaim risk | low if framing held |

This is a **solid short mathematical note**, not a breakthrough and not a derivation of QM. Best title energy: selector catalogue inside invariant bilinear pairings.

## Commits

- `8ab62e08` v4.5 package
- `52f8e172` v4.6 Galley-Masanes
- `0b1e0a28` v4.7 Thm 5

## Still open for remaining minutes / later

- [ ] Human English pass
- [ ] Manual amsmath polish of `.tex` (no pdflatex on machine)
- [ ] Problem A hard theorem (OPT + complex amplitudes => QM?)
- [ ] Optional: cut Gram scaffolding for ultra-short note
