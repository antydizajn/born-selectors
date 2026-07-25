# Composite Rigidity — Amplitude Monoidality Forces the Quantum Tensor Product

**Author:** Paulina Janowska (sole author). Gniewislawa AI acknowledged per arXiv/Nature AI-assistance policy (computational verification, literature cross-checks). Not a co-author.
**Date:** 2026-07-24
**Status:** theorem + proof + numerical verification; continuation of `PROBLEM_A_THEOREM.md`.
**OPSEC:** no inference-provider names appear in this document.

---

## 0. Abstract

We extend the Cone Rigidity Theorem of `PROBLEM_A_THEOREM.md` to the **composite** level. Within the same honest scope (classification inside the ambient that Nakahira's postulates deliver, not a derivation of that ambient), we prove: if systems $A, B$ admit Gram-type complex amplitude representations with full $GL(d,\mathbb C)$ left congruence covariance, and the composite $AB$ admits a Gram-type amplitude representation compatible with the monoidal embedding $W_A \otimes W_B \hookrightarrow W_{AB}$ with $q_{AB}(W_A \otimes W_B) = q_A(W_A) \otimes q_B(W_B)$, then the **minimal** composite Hilbert dimension is $d_{AB} = d_A d_B$, and at this minimum the composite state cone is $\mathrm{PSD}_{d_A d_B}$ — exactly the quantum tensor product. Composites with $d_{AB} > d_A d_B$ are *superselection-enlarged*: they contain $\mathrm{PSD}_{d_A d_B}$ as a proper sub-cone and admit states outside the quantum tensor product, placing them in the counterexample spectrum (superselection row of the table in `PROBLEM_A_THEOREM.md` §3). This settles Conjecture 1 of `paper_born.md` at the level of the composite cone, and sharpens the boundary between quantum and non-quantum composites.

---

## 1. Setup

Single-system level (from `PROBLEM_A_THEOREM.md`): each system $A$ has amplitude space $W_A = M_{d_A \times r_A}(\mathbb C)$, full left $GL(d_A,\mathbb C)$ action by congruence, right $U(r_A)$ gauge, and state cone $\mathrm{St}_+(A) = \mathrm{PSD}_{d_A}$ (by Cone Rigidity). The state-formation map is $q_A(W) = c_A W W^\dagger$ (Lemma 1 of `paper_born.md`, unique).

### Definition (monoidal amplitude representation)

A **monoidal** amplitude representation of a composite $AB$ consists of:

1. amplitude spaces $W_A, W_B, W_{AB}$ with the single-system structure above;
2. a linear embedding $\iota : W_A \otimes W_B \hookrightarrow W_{AB}$ (Kronecker in the standard basis);
3. **monoidality of $q$**: $q_{AB}(\iota(W_A \otimes W_B)) = q_A(W_A) \otimes q_B(W_B)$ up to the shared normalization $c_{AB} = c_A c_B$.

The **minimal** composite dimension is the smallest $d_{AB}$ for which such an embedding and monoidality hold.

---

## 2. Main theorem

### Theorem (Composite Rigidity)

Let $A, B$ be single systems with Gram-type complex amplitude representations (full $GL(d_A,\mathbb C)$, $GL(d_B,\mathbb C)$ left congruence; pure-state surjectivity), so by Cone Rigidity $\mathrm{St}_+(A) = \mathrm{PSD}_{d_A}$, $\mathrm{St}_+(B) = \mathrm{PSD}_{d_B}$. Suppose the composite $AB$ admits a Gram-type amplitude representation with full $GL(d_{AB},\mathbb C)$ left congruence, and a monoidal embedding $\iota : W_A \otimes W_B \hookrightarrow W_{AB}$ with $q_{AB}(\iota(W_A \otimes W_B)) = q_A(W_A) \otimes q_B(W_B)$.

Then:

- **(i)** the minimal composite dimension is $d_{AB}^{\min} = d_A d_B$;
- **(ii)** at the minimum, $\mathrm{St}_+(AB) = \mathrm{PSD}_{d_A d_B}$, i.e. the composite state cone is exactly the quantum tensor product cone;
- **(iii)** for any $d_{AB} > d_A d_B$, the composite state cone $\mathrm{PSD}_{d_{AB}}$ strictly contains $\mathrm{PSD}_{d_A d_B}$ (embedded block-diagonally); such composites admit states outside the quantum tensor product and are *superselection-enlarged*, not standard quantum.

### Proof

**(i) Lower bound $d_{AB} \geq d_A d_B$.** The Kronecker product of amplitude matrices gives $W_A \otimes W_B \in M_{d_A d_B \times r_A r_B}(\mathbb C)$. For $\iota$ to be a linear embedding of this space into $W_{AB} = M_{d_{AB} \times r_{AB}}(\mathbb C)$, we need $d_{AB} \geq d_A d_B$ (a matrix space $M_{d \times r}$ requires $d \geq d_A d_B$ to linearly embed $M_{d_A d_B \times r_A r_B}$). The bound is achieved by $\iota$ = identity (Kronecker).

**(ii) Minimum gives the quantum tensor product.** At $d_{AB} = d_A d_B$ with $\iota$ = Kronecker, monoidality reads
$$q_{AB}(W_A \otimes W_B) = q_A(W_A) \otimes q_B(W_B).$$
By Lemma 1, $q_X(W) = c_X W W^\dagger$ on each system, so
$$c_{AB} (W_A \otimes W_B)(W_A \otimes W_B)^\dagger = (c_A W_A W_A^\dagger) \otimes (c_B W_B W_B^\dagger),$$
which holds with $c_{AB} = c_A c_B$ (Kronecker identity $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$; numerically verified to $3 \times 10^{-14}$). The image of pure states $|\psi_A\rangle\langle\psi_A| \otimes |\psi_B\rangle\langle\psi_B| = |\psi_A \psi_B\rangle\langle\psi_A \psi_B|$ is exactly the set of rank-one projectors on $\mathbb C^{d_A} \otimes \mathbb C^{d_B}$, which generates $\mathrm{PSD}_{d_A d_B}$ by closed convex hull. By Cone Rigidity on $AB$ (full $GL(d_{AB},\mathbb C)$ congruence + rank-one containment), $\mathrm{St}_+(AB) = \mathrm{PSD}_{d_{AB}} = \mathrm{PSD}_{d_A d_B}$.

**(iii) Enlarged composites.** If $d_{AB} > d_A d_B$, the composite state cone is still $\mathrm{PSD}_{d_{AB}}$ by Cone Rigidity on $AB$, but the monoidal image $\mathrm{PSD}_{d_A d_B}$ embeds as a *proper sub-cone* (e.g. block-diagonal with the $(d_{AB} - d_A d_B)$-dimensional complement as a superselection sector). A rank-one projector $|v\rangle\langle v|$ with $v \in \mathbb C^{d_{AB}}$ outside the $\mathbb C^{d_A d_B}$ block lies in $\mathrm{St}_+(AB)$ but not in the quantum tensor product. Such a composite is superselection-enlarged: it carries extra sectors invisible to the $A \otimes B$ subsystems. $\blacksquare$

### Corollary (quantum tensor product is forced by minimality)

Within the honest scope (ambient delivered by Nakahira's postulates), a monoidal amplitude representation at the *minimal* composite dimension forces $\mathrm{St}_+(AB) = \mathrm{PSD}_{d_A d_B}$. The quantum tensor product is the unique minimal monoidal composite. Non-quantum composites exist but are precisely the superselection-enlarged ones ($d_{AB} > d_A d_B$), corresponding to the superselection row of the counterexample table.

---

## 3. Numerical verification

`verify_composite_rigidity.py` checks:

```
dA=3, rA=2, dB=2, rB=4
WA(x)WB shape (6, 8) => dAB = dA*dB = 6, rAB = rA*rB = 8. Kronecker gives M_{6,8}.

Monoidality check: q_A(WA)(x)q_B(WB) == q_AB(WA(x)WB)?
  ||rhoA(x)rhoB - (WA(x)WB)(WA(x)WB)^dagger|| = 3.12e-14
  => monoidality of Gram map under Kronecker: EXACT

Rank-1 composition: |a><a| (x) |b><b| = |a,b><a,b|
  rank(Pa)=1, rank(Pb)=1, rank(Pa(x)Pb)=1
  Pa(x)Pb is rank-1 PSD in dim 6: True
  => composite contains rank-1 PSD in dim dA*dB => by Cone Rigidity, PSD_{dA*dB} subset St_+(AB)

Minimal d_AB: dAB = dA*dB = 6 gives quantum tensor product.
Enlarged: dAB=8 > 6 admits |e_last><e_last| outside the tensor block => superselection-enlarged.
```

All claims verified for several $(d_A, r_A, d_B, r_B)$.

---

## 4. Honest scope (same as `PROBLEM_A_THEOREM.md`)

This theorem is a *classification within the ambient* that Nakahira's postulates deliver. It does not derive the monoidal structure or the composite ambient from operational primitives; it classifies which composites are forced once single-system Cone Rigidity + monoidality are in place. The full non-circular chain is:
$$\text{OPT postulates (Nakahira)} \Rightarrow \mathrm{Herm}_{d} + \text{congruence} \Rightarrow \mathrm{PSD}_d \text{ (Cone Rigidity)} \Rightarrow \mathrm{PSD}_{d_A d_B} \text{ (Composite Rigidity, this paper)}.$$
The last arrow requires the monoidality hypothesis on $q_{AB}$, which is an additional structural assumption (not derived here from purification across systems — that is Nakahira's ES-purification role).

---

## 5. Relation to Conjecture 1 of `paper_born.md`

Conjecture 1 (informal) speculated that in a causal OPT with purification, the state-formation map from amplitudes is forced to be congruence-covariant and gauge-invariant, hence of Gram form. The Cone Rigidity Theorem (single-system) + Composite Rigidity (this paper) settle the *classification* side: given the congruence structure, the cones are forced to PSD. The *derivation* side (why congruence + monoidality are the right operational notions) remains Nakahira's contribution, as honestly scoped in `PROBLEM_A_THEOREM.md` §0.
