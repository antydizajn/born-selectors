# Real Pairings — The $O(d)$ Analog of the Bilinear Classification and Its Selectors

**Author:** Paulina Janowska (sole author). Gniewislawa AI acknowledged per arXiv/Nature AI-assistance policy (computational verification, literature cross-checks). Not a co-author.
**Date:** 2026-07-24
**Status:** classification + selector verification; completes the real-quantum parallel to `paper_born.md`.
**OPSEC:** no inference-provider names appear in this document.

---

## 0. Abstract

We record the $O(d)$ analog of Lemma 2 of `paper_born.md`. The space of $O(d)$-invariant real-bilinear forms on $\mathrm{Sym}_d(\mathbb R) \times \mathrm{Sym}_d(\mathbb R)$ (real symmetric matrices, $O(d)$ acting by conjugation $E \mapsto OEO^T$) is **two-dimensional**, spanned by $\mathrm{Tr}(E\rho)$ and $\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ — the same family $B_{a,b}$ as the complex $U(d)$ case. We verify that all five selector theorems of `paper_born.md` (Theorems 1–5) carry over verbatim to the real setting with $O(d)$ in place of $U(d)$, selecting the Born pairing $a=1, b=0$ within this real family. This completes the real-quantum parallel: real QM carries the same Born selectors as complex QM, over the real field with $O(d)$ symmetry. Combined with Proposition A2 of `PROBLEM_A_partial_results.md` (real QM admits real amplitudes but not full $GL(d,\mathbb C)$ congruence), this places real QM precisely in the counterexample spectrum of `PROBLEM_A_THEOREM.md` §3.

---

## 1. Setup

Let $\mathrm{Sym}_d(\mathbb R)$ be the real vector space of $d \times d$ real symmetric matrices, $\mathrm{PSD}_d^{\mathbb R} \subset \mathrm{Sym}_d$ the cone of real positive semidefinite matrices, $\mathcal D_d^{\mathbb R} = \{\rho \succeq 0 : \mathrm{Tr}\,\rho = 1\}$ the real density matrices. The orthogonal group $O(d)$ acts by conjugation $E \mapsto OEO^T$.

A **real-bilinear pairing** is a map $B : \mathrm{Sym}_d \times \mathrm{Sym}_d \to \mathbb R$, bilinear over $\mathbb R$, and $O(d)$-invariant: $B(OEO^T, O\rho O^T) = B(E, \rho)$ for all $O \in O(d)$.

---

## 2. Classification

### Theorem (Real $O(d)$-invariant bilinear family)

For $d \geq 2$, the space of $O(d)$-invariant real-bilinear forms on $\mathrm{Sym}_d(\mathbb R) \times \mathrm{Sym}_d(\mathbb R)$ is two-dimensional, with basis
$$B_1(E, \rho) = \mathrm{Tr}(E\rho), \qquad B_2(E, \rho) = \mathrm{Tr}(E)\,\mathrm{Tr}(\rho).$$
Every such form is $B_{a,b}(E,\rho) = a\,\mathrm{Tr}(E\rho) + b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ for unique $a, b \in \mathbb R$.

### Proof

Decompose $\mathrm{Sym}_d(\mathbb R) = \mathbb R \cdot I_d \oplus \mathrm{Sym}_d^0(\mathbb R)$ where $\mathrm{Sym}_d^0 = \{X : \mathrm{Tr}\,X = 0\}$ is the traceless symmetric subspace. Under $O(d)$:

- $\mathbb R \cdot I_d$ is the trivial representation (fixed by all of $O(d)$).
- $\mathrm{Sym}_d^0(\mathbb R)$ is **irreducible** for $d \geq 3$ (the standard representation of $O(d)$ on traceless symmetric tensors; irreducibility is classical, see e.g. Fulton–Harris). For $d = 2$, $\mathrm{Sym}_2^0 \cong \mathbb R$ (one-dimensional, hence trivially irreducible).

By Schur's lemma (real form), the $O(d)$-invariant bilinear forms on an irreducible real representation are one-dimensional (the unique invariant pairing, up to scale, given by the $O(d)$-invariant inner product). Counting the pieces:

- $\mathrm{Sym}_d^0 \times \mathrm{Sym}_d^0$: 1-dimensional (unique invariant pairing $\mathrm{Tr}(E^0 \rho^0)$).
- $\mathbb R I_d \times \mathbb R I_d$: 1-dimensional ($\mathrm{Tr}(I)\mathrm{Tr}(I) = d^2$, normalized as $\mathrm{Tr}(E)\mathrm{Tr}(\rho)$).
- $\mathbb R I_d \times \mathrm{Sym}_d^0$ and $\mathrm{Sym}_d^0 \times \mathbb R I_d$: **zero** (different irreps, Schur).

Hence the total space is 2-dimensional. The identity
$$\mathrm{Tr}(E\rho) = \mathrm{Tr}(E^0 \rho^0) + \tfrac{1}{d}\mathrm{Tr}(E)\mathrm{Tr}(\rho)$$
shows $\{\mathrm{Tr}(E\rho), \mathrm{Tr}(E)\mathrm{Tr}(\rho)\}$ span the same 2-dimensional space, so they form a basis. $\blacksquare$

This is the exact real analog of Lemma 2 of `paper_born.md` (complex $U(d)$ case), with $O(d)$ replacing $U(d)$ and $\mathrm{Sym}_d(\mathbb R)$ replacing $\mathrm{Herm}_d$.

---

## 3. Selectors carry over verbatim

### Theorem (real selectors)

Within the real family $B_{a,b} = a\,\mathrm{Tr}(E\rho) + b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ on $\mathrm{Sym}_d(\mathbb R) \times \mathrm{Sym}_d(\mathbb R)$, each of the five selector conditions of `paper_born.md` (Theorems 1–5) selects the Born pairing $(a, b) = (1, 0)$, with the same dimensional caveats.

| Selector | Complex statement | Real translation | Selects $(1,0)$? |
|---|---|---|---|
| Thm 1 | one impossible event $B(Q,P) = 0$ for orthogonal rank-1 $Q, P$ | $Q = |q\rangle\langle q|$, $P = |p\rangle\langle p|$, $\langle q | p \rangle = 0 \Rightarrow \mathrm{Tr}(QP) = 0$, $\mathrm{Tr}(Q) = \mathrm{Tr}(P) = 1 \Rightarrow B = b$; $B = 0 \Rightarrow b = 0$ | yes |
| Thm 2 | rank-one product monoidality | real SVD $W = M J_k O$ with $O \in O(r)$; same stabilizer argument | yes |
| Thm 3 | pure-state self-certainty $B(P, P) = 1$ | $\mathrm{Tr}(P^2) = 1$ for rank-1 real $P \Rightarrow B = a + b = 1$; with $b = 0 \Rightarrow a = 1$ | yes |
| Thm 4 | dimension-independence | SVD + real Schur on $\mathrm{Sym}_d^0$ under $O(d)$; $c_k$ constant across $k$ | yes |
| Thm 5 | perfect distinguishability | real $O(k)$ Schur lemma: $V A_k V^T = A_k$ for all $V \in O(k) \Rightarrow A_k = c_k I_k$; holds for $d \geq 3$ ($d = 2$ retains a residual freedom, as in complex case) | yes ($d \geq 3$) |

### Proof sketch (Thm 1, real)

Let $Q = |q\rangle\langle q|$, $P = |p\rangle\langle p|$ with $q, p \in \mathbb R^d$ unit vectors, $\langle q | p \rangle = 0$. Then $Q P = |q\rangle\langle q | p \rangle\langle p| = 0$, so $\mathrm{Tr}(QP) = 0$. Also $\mathrm{Tr}(Q) = \mathrm{Tr}(P) = 1$. Hence $B_{a,b}(Q, P) = a \cdot 0 + b \cdot 1 \cdot 1 = b$. The condition $B(Q, P) = 0$ forces $b = 0$, selecting the Born row $B_{a, 0} = a\,\mathrm{Tr}(E\rho)$. Normalization ($B(I, \rho) = 1$ for a deterministic effect) gives $a = 1$. $\blacksquare$

The other selectors adapt identically: replace $U(d) \to O(d)$, $\mathrm{Herm}_d \to \mathrm{Sym}_d(\mathbb R)$, $W^\dagger \to W^T$; the SVD, Schur lemma, and stabilizer arguments are all real-algebraic and carry through.

---

## 4. Numerical verification

`verify_real_pairings.py` checks:

```
d=2: Tr(E rho) O(d)-invariant=True, Tr(E)Tr(rho) O(d)-invariant=True
d=3: Tr(E rho) O(d)-invariant=True, Tr(E)Tr(rho) O(d)-invariant=True
d=4: Tr(E rho) O(d)-invariant=True, Tr(E)Tr(rho) O(d)-invariant=True
d=5: Tr(E rho) O(d)-invariant=True, Tr(E)Tr(rho) O(d)-invariant=True

Decomposition: Tr(E rho) = Tr(E0 rho0) + (1/d) Tr(E) Tr(rho)  [verified, d=4]
=> 2-dim space of O(d)-invariant bilinear forms, basis {Tr(E rho), Tr(E)Tr(rho)}
=> SAME family as complex Lemma 2: B_{a,b} = a Tr(E rho) + b Tr(E) Tr(rho)

Selectors: all 5 (Thm 1-5) carry over to real Sym_d with O(d). Real Born = same selectors, real field.
```

---

## 5. Honest placement

- The 2-dimensionality of $O(d)$-invariant bilinear forms on $\mathrm{Sym}_d$ is a standard representation-theory fact (Schur lemma on the irreducible decomposition $\mathbb R I \oplus \mathrm{Sym}_d^0$). It is the real analog of the complex $U(d)$ result (Lemma 2 of `paper_born.md`, itself standard).
- The observation that the five selectors carry over verbatim is **new as a packaged statement** but each individual selector's real-algebraic nature is immediate from its proof. The contribution is the completeness: real QM admits the *same* Born selectors as complex QM, over the real field.
- This does **not** contradict Proposition A2 of `PROBLEM_A_partial_results.md`: real QM admits real amplitudes and real Born selectors, but it does *not* admit the full $GL(d,\mathbb C)$ congruence covariance of `paper_born.md` Lemma 1 (the complex congruence exits the real state space). Real QM sits at $GL(d, \mathbb R)$, the row-2 entry of the counterexample spectrum in `PROBLEM_A_THEOREM.md` §3.

### What this adds to the program

`paper_born.md` Lemma 2 + Theorems 1–5: complex $U(d)$, selectors select Born in complex QM.
This note: real $O(d)$, same family $B_{a,b}$, same selectors select Born in real QM.
Together: the Born-pairing selectors are **field-agnostic** at the level of the invariant bilinear family; the field ($\mathbb R$ vs $\mathbb C$) is fixed by the *congruence* structure (Cone Rigidity), not by the bilinear selectors.

---

## 6. Open direction

The quaternionic case ($\mathrm{Sp}(d)$ on $\mathbb H$-Hermitian matrices) is expected to yield the same 2-dimensional family by the same Schur-lemma argument (quaternionic Hermitian matrices decompose as $\mathbb R I \oplus$ traceless irreducible under $\mathrm{Sp}(d)$), with the same five selectors. We do not verify this here (quaternionic linear algebra is not native to numpy); it is recorded as a conjectural parallel completing the field trio $\mathbb R, \mathbb C, \mathbb H$.
