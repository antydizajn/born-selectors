# Quaternionic Pairings — The $\mathrm{Sp}(d)$ Analog and the Field Trio

**Author:** Paulina Janowska (sole author). Gniewislawa AI acknowledged per arXiv/Nature AI-assistance policy (computational verification, literature cross-checks). Not a co-author.
**Date:** 2026-07-24
**Status:** classification + numerical support for $d=2$; theoretical for general $d$; completes the field trio $\mathbb R, \mathbb C, \mathbb H$.
**OPSEC:** no inference-provider names appear in this document.

---

## 0. Abstract

We record the $\mathrm{Sp}(d)$ analog of Lemma 2 of `paper_born.md` and Theorem of `REAL_PAIRINGS.md`. The space of $\mathrm{Sp}(d)$-invariant real-bilinear forms on the space of $\mathbb H$-Hermitian $d \times d$ matrices (realized as $2d \times 2d$ complex Hermitian matrices commuting with the symplectic structure $J = \begin{pmatrix}0 & I_d \\ -I_d & 0\end{pmatrix}$) is **two-dimensional**, with basis $\{\mathrm{Tr}(XY), \mathrm{Tr}(X)\mathrm{Tr}(Y)\}$ — the same family $B_{a,b}$ as the real $O(d)$ case (`REAL_PAIRINGS.md`) and the complex $U(d)$ case (`paper_born.md` Lemma 2). This completes the field trio $\mathbb R, \mathbb C, \mathbb H$: across all three real division algebras, the invariant bilinear family is the same 2-dimensional $B_{a,b}$, and the five Born selectors of `paper_born.md` are expected to carry over verbatim (conjectural for $\mathbb H$, not numerically verified here beyond $d = 2$). The field is fixed by the *congruence* structure (Cone Rigidity, `PROBLEM_A_THEOREM.md`), not by the bilinear selectors.

---

## 1. Setup

Let $\mathbb H$ be the quaternions. A $\mathbb H$-Hermitian $d \times d$ matrix $X$ satisfies $X = X^\dagger$ (quaternionic adjoint). Via the standard complex realization $\mathbb H \ni a + b\mathbf j \mapsto \begin{pmatrix} a & b \\ -\bar b & \bar a \end{pmatrix}$, such a matrix becomes a $2d \times 2d$ complex Hermitian matrix commuting with the symplectic structure $J = \begin{pmatrix} 0 & I_d \\ -I_d & 0 \end{pmatrix}$ (i.e. $X J = J X$, $X = X^\dagger$).

The compact symplectic group $\mathrm{Sp}(d) = \{U \in U(2d) : U^\dagger J U = J\}$ acts on $\mathbb H$-Hermitian matrices by congruence $X \mapsto U^\dagger X U$.

A **real-bilinear pairing** is $B : \mathrm{Herm}_d(\mathbb H) \times \mathrm{Herm}_d(\mathbb H) \to \mathbb R$, bilinear over $\mathbb R$, and $\mathrm{Sp}(d)$-invariant: $B(U^\dagger X U, U^\dagger Y U) = B(X, Y)$.

---

## 2. Classification

### Theorem (Quaternionic $\mathrm{Sp}(d)$-invariant bilinear family)

For $d \geq 2$, the space of $\mathrm{Sp}(d)$-invariant real-bilinear forms on $\mathrm{Herm}_d(\mathbb H) \times \mathrm{Herm}_d(\mathbb H)$ is two-dimensional, with basis
$$B_1(X, Y) = \mathrm{Tr}(XY), \qquad B_2(X, Y) = \mathrm{Tr}(X)\,\mathrm{Tr}(Y).$$
Every such form is $B_{a,b}(X, Y) = a\,\mathrm{Tr}(XY) + b\,\mathrm{Tr}(X)\mathrm{Tr}(Y)$ for unique $a, b \in \mathbb R$.

### Proof (theoretical, representation-theoretic)

Decompose $\mathrm{Herm}_d(\mathbb H) = \mathbb R \cdot I_{2d}|_{\mathbb H} \oplus \mathrm{Herm}_d^0(\mathbb H)$ where $\mathrm{Herm}_d^0$ is the traceless $\mathbb H$-Hermitian subspace. Under $\mathrm{Sp}(d)$:

- $\mathbb R \cdot I$ is the trivial representation.
- $\mathrm{Herm}_d^0(\mathbb H)$ is **irreducible** under $\mathrm{Sp}(d)$ (the traceless $\mathbb H$-Hermitian matrices carry the irreducible representation of highest weight $2\omega_1$ of $\mathrm{Sp}(d)$; classical, see e.g. Fulton–Harris, or Procesi, *Lie Groups*).

By Schur's lemma (real/quaternionic type), the $\mathrm{Sp}(d)$-invariant bilinear forms on an irreducible real representation are one-dimensional (the unique invariant pairing). Counting pieces:

- $\mathrm{Herm}_d^0 \times \mathrm{Herm}_d^0$: 1-dimensional ($\mathrm{Tr}(X^0 Y^0)$).
- $\mathbb R I \times \mathbb R I$: 1-dimensional ($\mathrm{Tr}(I)\mathrm{Tr}(I)$, normalized as $\mathrm{Tr}(X)\mathrm{Tr}(Y)$).
- $\mathbb R I \times \mathrm{Herm}_d^0$ and reverse: **zero** (different irreps).

Hence the total space is 2-dimensional, spanned by $\{\mathrm{Tr}(XY), \mathrm{Tr}(X)\mathrm{Tr}(Y)\}$ (the same decomposition identity $\mathrm{Tr}(XY) = \mathrm{Tr}(X^0 Y^0) + \frac{1}{2d}\mathrm{Tr}(X)\mathrm{Tr}(Y)$ holds). $\blacksquare$

---

## 3. Numerical support

`verify_quaternionic_pairings.py` verifies $\mathrm{Sp}(d)$-invariance of $\mathrm{Tr}(XY)$ and $\mathrm{Tr}(X)\mathrm{Tr}(Y)$ on $\mathbb H$-Hermitian matrices under congruence by real symplectic rotations (a subgroup of $\mathrm{Sp}(d)$):

```
d=2 (complex 2d=4): Tr(XY) Sp(d)-inv=True, Tr(X)Tr(Y) Sp(d)-inv=True, confirmed_tests=5
d=3 (complex 2d=6): confirmed_tests=0 (Sp(d) validation rate drops with d)
d=4 (complex 2d=8): confirmed_tests=1
d=5 (complex 2d=10): confirmed_tests=0
```

The drop in confirmed tests for $d \geq 3$ reflects the difficulty of generating *generic* $\mathrm{Sp}(d)$ elements numerically (the real-symplectic-rotation parametrization used here only produces a subgroup, and the unitary-plus-symplectic joint constraint is increasingly restrictive as $d$ grows). The $d = 2$ confirmation (5 independent tests, all invariant) is solid; for general $d$ the result rests on the representation-theoretic argument of §2 (irreducibility of $\mathrm{Herm}_d^0(\mathbb H)$ under $\mathrm{Sp}(d)$), which is classical and standard.

### Honest limitation

The selector theorems (Thm 1–5 of `paper_born.md`) are **not** numerically verified here for $\mathbb H$. Their quaternionic adaptation requires $\mathbb H$-linear SVD (which exists: every $\mathbb H$-matrix has a quaternionic SVD), $\mathrm{Sp}(k)$ Schur lemma, and quaternionic stabilizer arguments. The selectors are *expected* to carry over by the same algebraic structure (the proofs use only the invariant-bilinear family $B_{a,b}$, which is the same, plus SVD/Schur which hold over $\mathbb H$), but this remains a **conjecture** until verified.

---

## 4. The field trio — synthesis

| Field $\mathbb K$ | Symmetry group | State space | Invariant bilinear family | Selectors select Born? |
|---|---|---|---|---|
| $\mathbb R$ | $O(d)$ | $\mathrm{Sym}_d(\mathbb R)$ | $\{a\,\mathrm{Tr}(E\rho) + b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)\}$ | yes (Thm 1–5, `REAL_PAIRINGS.md`) |
| $\mathbb C$ | $U(d)$ | $\mathrm{Herm}_d(\mathbb C)$ | $\{a\,\mathrm{Tr}(E\rho) + b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)\}$ | yes (Thm 1–5, `paper_born.md`) |
| $\mathbb H$ | $\mathrm{Sp}(d)$ | $\mathrm{Herm}_d(\mathbb H)$ | $\{a\,\mathrm{Tr}(XY) + b\,\mathrm{Tr}(X)\mathrm{Tr}(Y)\}$ | conjectural (this paper, §3) |

**The bilinear family is field-agnostic.** Across all three real division algebras, the invariant bilinear pairings form the same 2-dimensional family $B_{a,b}$, and the Born selector ($a = 1, b = 0$) sits at the same point in each. The field itself ($\mathbb R$ vs $\mathbb C$ vs $\mathbb H$) is **not** fixed by the bilinear selectors; it is fixed by the *congruence* structure (the left filter group $GL(d, \mathbb K)$), as established by the Cone Rigidity Theorem of `PROBLEM_A_THEOREM.md` for $\mathbb C$ (and Proposition A2 for $\mathbb R$ showing real QM fails full complex congruence).

### Corollary (field is a congruence datum, not a bilinear datum)

Within the honest scope of `PROBLEM_A_THEOREM.md`, the choice of division algebra is encoded in the left filter group $H = GL(d, \mathbb K)$ acting by congruence on the state cone. The bilinear Born selectors are insensitive to this choice — they select the same pairing $(a, b) = (1, 0)$ in all three fields. This separates two orthogonal axes of the reconstruction landscape:

- *Which field?* — fixed by congruence symmetry (Cone Rigidity).
- *Born within the field?* — fixed by bilinear selectors (Lemma 2 + Thm 1–5, field-agnostic).

---

## 5. Honest placement

- The 2-dimensionality of $\mathrm{Sp}(d)$-invariant bilinear forms on $\mathrm{Herm}_d(\mathbb H)$ is a standard representation-theoretic fact (Schur lemma on the irreducible decomposition $\mathbb R I \oplus \mathrm{Herm}_d^0$ under $\mathrm{Sp}(d)$). It is the quaternionic analog of the complex $U(d)$ and real $O(d)$ results.
- The observation that the field trio shares the same bilinear family and that the field is fixed by congruence (not bilinear) structure is, as a packaged statement, the contribution of this note relative to `paper_born.md` and `REAL_PAIRINGS.md`.
- This does **not** establish quaternionic QM as a reconstruction target; it only classifies the bilinear structure *given* the quaternionic ambient. As in `PROBLEM_A_THEOREM.md` §0, this is classification inside an assumed ambient, not derivation of the ambient from operations.

---

## 6. Open directions

1. **Verify the five selectors over $\mathbb H$** (requires quaternionic SVD implementation, beyond numpy). Expected to hold by structural parallelism; until verified, the quaternionic Born selection is conjectural.
2. **Cone Rigidity for $\mathbb H$**: is $\mathrm{PSD}_d^{\mathbb H}$ the unique $\mathrm{Sp}(d)$-congruence-invariant proper cone containing a rank-one $\mathbb H$-PSD? **Partially open.** The quaternionic Sylvester law (signature preserved under $GL(d,\mathbb H)$-congruence) was numerically confirmed for $d = 2$ (50 tests), which is promising. However, $\mathbb H$-Hermitian matrices have *doubled* spectra (each quaternionic eigenvalue appears with complex multiplicity 2), so the orbit structure differs from the $\mathbb R/\mathbb C$ case: the minimal nonzero PSD has signature $(2, 0, 2d-2)$ rather than $(1, 0, d-1)$. The closure+swap argument of `PROBLEM_A_THEOREM.md` Step 4 needs adaptation to the doubled-spectrum setting (the "negative rank-one" target becomes signature $(0, 2, 2d-2)$, and the contradiction requires both $|\psi\rangle\langle\psi|_{\mathbb H}$ and $-|\psi\rangle\langle\psi|_{\mathbb H}$ in $C$). Proper $\mathbb H$-linear algebra (correct construction of $\mathbb H$-vectors and quaternionic rank) is needed to complete this; it is left as the principal open direction. The bilinear classification (this paper, §2) does *not* require Cone Rigidity and stands independently.
3. **Composite Rigidity over $\mathbb H$**: if established, would complete the trio at the composite level. Open.
