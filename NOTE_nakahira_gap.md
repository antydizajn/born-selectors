# Nakahira gap map and revised research programme

**Date:** 2026-07-24  
**Source:** arXiv:2605.23217v1 (Kenji Nakahira, 22 May 2026), full PDF read via pdftotext  
**Related:** `paper_born.md` v4.5 Section 8

## Nakahira in one paragraph

In a finite-dimensional causal OPT, **local equivalence** (channels identified by local I/O stats) + **ES purification** (every state purified on AA~ with A~ equivalent to A, unique up to reversible dynamics on A~) force the *entire* finite-dimensional complex quantum package: Hilbert spaces, all density matrices, all POVMs, Born rule, tensor products, CPTP channels, and derived measurement no-restriction. Neither postulate alone suffices (classical: local eq only; real QM: ES purif only).

## What this kills

| Original ambition | Status after Nakahira |
|-------------------|----------------------|
| Derive Born from operational axioms via amplitude geometry | **Superseded.** Nakahira already derives Born without amplitudes. |
| Conjecture 1 as path to Born | **Superseded as Born-route.** Residual content is representation theory. |
| Claim that fibre-orbit forces complex QM | **Too weak / redundant** if Nakahira is accepted. |

## What this does *not* kill

| Residual content | Why it still matters |
|------------------|----------------------|
| Lemma 1 (Gram map uniqueness under congruence+gauge) | Clean invariant-theory classification inside amplitude coordinates. |
| Theorems 1--4 (Born selectors in bilinear class) | Valid math one layer below Hilbert space; pedagogical + catalogue value. |
| Prop. 3 (local selector equivalence) | Structural clarity: impossible-event ≡ pure-certainty under the class. |
| Failed ancilla-independence | Negative result prevents a natural error. |

## Revised open problems

### Problem A (hard, potentially new)
Characterize OPTs that admit an **amplitude representation**:
a structure assigning to systems spaces $W_A \subseteq M_{d\times r}(\mathbb C)$ (or analogous) with right unitary gauge and left invertible-filter action, such that the quotient by gauge recovers the state space and the induced pairing is Born.

This is *not* answered by Nakahira, who never introduces amplitudes.

### Problem B (likely standard)
Once Hilbert space exists, is Gram factorization of mixed states forced beyond Stinespring?  
**Working answer:** yes — it is the standard purification/Kraus coordinate system. Not a research frontier.

### Problem C (selector catalogue)
Is the list {local certainty/impossible event, monoidality, dim-independence} complete for natural operational selectors of Born inside the invariant bilinear class? Are there others of independent interest (e.g. Cencov/Fisher monotonicity a la Lax 2604.27339)?

## Layer diagram

```
OPT postulates (local eq + ES purif)
        |  Nakahira 2026
        v
Complex QM package (H, density ops, POVMs, Born, tensor, CPTP)
        |  representation choice
        v
Amplitude coordinates W |-> WW^dagger   [Lemma 1 classifies this map]
        |
        v
Bilinear invariant pairings on Herm_d   [Lemma 2]
        |  selectors Thm 1--4
        v
Born pairing uniquely selected
```

## Honest publication framing

- Do **not** title or abstract as "derivation of the Born rule from first principles".
- Do frame as: "elementary selectors for the Born pairing inside the unitarily invariant bilinear class; Gram-map classification; honest comparison with Nakahira/Hossenfelder/Gleason".
- arXiv categories: quant-ph, math-ph (primary quant-ph).

## Action items done in paper v4.5

- Section 8 rewritten with full Nakahira confrontation
- Conjecture 1 marked superseded as Born-route
- Problems A/B stated
- Prop. 3 local selector equivalence added
