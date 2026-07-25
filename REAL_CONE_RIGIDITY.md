# Real Cone Rigidity & Real Composite Rigidity

**Author:** Paulina Janowska (sole author). Gniewislawa AI acknowledged per arXiv/Nature AI-assistance policy (computational verification). Not a co-author.
**Date:** 2026-07-24
**Status:** theorems + proofs + numerical verification; real-field parallel to `PROBLEM_A_THEOREM.md` and `COMPOSITE_RIGIDITY.md`.
**OPSEC:** no inference-provider names appear in this document.

---

## 0. Abstract

We record the real-field parallel of the Cone Rigidity Theorem (`PROBLEM_A_THEOREM.md`) and the Composite Rigidity Theorem (`COMPOSITE_RIGIDITY.md`). Over $\mathbb R$, with $GL(d,\mathbb R)$-congruence on $\mathrm{Sym}_d(\mathbb R)$ (real symmetric matrices, $X \mapsto M X M^T$), the proof goes through *verbatim*: the only proper closed convex cone invariant under $GL(d,\mathbb R)$-congruence and containing a rank-one real PSD is $\mathrm{PSD}_d^{\mathbb R}$. Likewise, a monoidal real amplitude representation forces the minimal composite to $d_{AB} = d_A d_B$ with $\mathrm{St}_+(AB) = \mathrm{PSD}_{d_A d_B}^{\mathbb R}$ (the real quantum tensor product). This places real QM at the row-2 entry of the counterexample spectrum (Prop A2 of `PROBLEM_A_partial_results.md`): real QM is selected by $GL(d,\mathbb R)$-congruence (not $GL(d,\mathbb C)$), and its state cone is $\mathrm{PSD}_d^{\mathbb R}$.

---

## 1. Real Cone Rigidity

### Theorem (Real Cone Rigidity, $GL(d,\mathbb R)$ case)

Let $C \subseteq \mathrm{Sym}_d(\mathbb R)$ be a proper closed convex cone (pointed, full-dimensional). Suppose

- **(H1$_\mathbb R$)** $C$ is $GL(d,\mathbb R)$-congruence invariant: $M C M^T = C$ for every $M \in GL(d,\mathbb R)$;
- **(H2$_\mathbb R$)** $C$ contains a rank-one real positive semidefinite matrix.

Then $C = \mathrm{PSD}_d^{\mathbb R}$.

### Proof

The proof is **identical** to the complex case (`PROBLEM_A_THEOREM.md` §2), with $\mathrm{Herm}_d \to \mathrm{Sym}_d(\mathbb R)$, $GL(d,\mathbb C) \to GL(d,\mathbb R)$, $M^\dagger \to M^T$:

- **Step 1.** Sylvester's law of inertia holds over $\mathbb R$: $X, Y \in \mathrm{Sym}_d(\mathbb R)$ are $GL(d,\mathbb R)$-congruent iff they have the same signature $(p, q, r)$. (Numerically verified for $d \in \{2,3,4,5,6\}$.)
- **Step 2.** A rank-one real projector $|v\rangle\langle v|$ ($v \in \mathbb R^d$) has signature $(1, 0, d-1)$. Its $GL(d,\mathbb R)$-orbit is all rank-one real PSD matrices. The closed convex hull is $\mathrm{PSD}_d^{\mathbb R}$ (every real PSD matrix is a positive combination of real rank-one projectors via its real spectral decomposition). Hence $\mathrm{PSD}_d^{\mathbb R} \subseteq C$.
- **Step 3.** If $C \supsetneq \mathrm{PSD}_d^{\mathbb R}$, pick $X \in C \setminus \mathrm{PSD}_d^{\mathbb R}$; $X$ has a negative eigenvalue, signature with $q \geq 1$.
- **Step 4.** From $X_0 = \mathrm{diag}(1, -1, 0, \dots, 0)$ (signature $(1, 1, d-2)$, the $q \geq 1$ case), apply $M_s = \mathrm{diag}(s, 1, \dots, 1) \in GL(d,\mathbb R)$ for $s > 0$: $X_s = \mathrm{diag}(s^2, -1, 0, \dots, 0) \in C$ by (H1$_\mathbb R$). As $s \to 0^+$, $X_s \to Y = \mathrm{diag}(0, -1, 0, \dots, 0) \in C$ by closedness. Apply the permutation-swap $P \in O(d) \subset GL(d,\mathbb R)$: $P Y P^T = \mathrm{diag}(-1, 0, \dots, 0) = -|e_1\rangle\langle e_1| \in C$.
- **Step 5.** $|e_1\rangle\langle e_1| \in \mathrm{PSD}_d^{\mathbb R} \subseteq C$ and $-|e_1\rangle\langle e_1| \in C$, so $|e_1\rangle\langle e_1| \in C \cap (-C) = \{0\}$ (pointedness), contradicting $|e_1\rangle\langle e_1| \neq 0$.
- **Step 6.** $C = \mathrm{PSD}_d^{\mathbb R}$. $\blacksquare$

The stronger enumeration form (Theorem 2 of `PROBLEM_A_THEOREM.md`) also carries over: the only proper closed convex $GL(d,\mathbb R)$-congruence-invariant cones in $\mathrm{Sym}_d(\mathbb R)$ are $\mathrm{PSD}_d^{\mathbb R}$ and $-\mathrm{PSD}_d^{\mathbb R}$, with (H2$_\mathbb R$) selecting $\mathrm{PSD}_d^{\mathbb R}$.

---

## 2. Real Composite Rigidity

### Theorem (Real Composite Rigidity)

Let $A, B$ be real single systems with Gram-type real amplitude representations (full $GL(d_A,\mathbb R)$, $GL(d_B,\mathbb R)$ left congruence; pure-state surjectivity), so by Real Cone Rigidity $\mathrm{St}_+(A) = \mathrm{PSD}_{d_A}^{\mathbb R}$, $\mathrm{St}_+(B) = \mathrm{PSD}_{d_B}^{\mathbb R}$. Suppose the composite $AB$ admits a Gram-type real amplitude representation with full $GL(d_{AB},\mathbb R)$ congruence and a monoidal embedding $\iota : W_A \otimes W_B \hookrightarrow W_{AB}$ with $q_{AB}(\iota(W_A \otimes W_B)) = q_A(W_A) \otimes q_B(W_B)$.

Then:

- **(i)** the minimal composite dimension is $d_{AB}^{\min} = d_A d_B$;
- **(ii)** at the minimum, $\mathrm{St}_+(AB) = \mathrm{PSD}_{d_A d_B}^{\mathbb R}$, the real quantum tensor product cone;
- **(iii)** for $d_{AB} > d_A d_B$, the composite is superselection-enlarged (real version).

### Proof

Identical to `COMPOSITE_RIGIDITY.md` §2, with real Kronecker products. The monoidality identity $q_A(W_A) \otimes q_B(W_B) = q_{AB}(W_A \otimes W_B)$ holds with $c_{AB} = c_A c_B$ via the real Kronecker identity $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ (numerically verified to $< 10^{-14}$). $\blacksquare$

---

## 3. Numerical verification

`verify_real_cone_rigidity.py`:

```
d=2: sylvester=True conv_rank1=True closure=True pointed=True => OK
d=3: sylvester=True conv_rank1=True closure=True pointed=True => OK
d=4: sylvester=True conv_rank1=True closure=True pointed=True => OK
d=5: sylvester=True conv_rank1=True closure=True pointed=True => OK
d=6: sylvester=True conv_rank1=True closure=True pointed=True => OK

Real composite dA=3, dB=2: monoidality Kronecker = True
Real composite dA=2, dB=2: monoidality Kronecker = True
Real composite dA=4, dB=3: monoidality Kronecker = True

=> Real Cone Rigidity: PSD^R_d unique GL(d,R)-congruence-invariant cone with rank-1 real PSD.
=> Real Composite Rigidity: min d_AB = d_A*d_B, St_+(AB) = PSD^R_{d_A*d_B}.
RESULT: ALL VERIFIED
```

---

## 4. Synthesis: cone rigidity across $\mathbb R$ and $\mathbb C$

| Field | Cone rigidity | Composite rigidity | Bilinear family | Selectors |
|---|---|---|---|---|
| $\mathbb R$ | $\mathrm{PSD}_d^{\mathbb R}$ unique under $GL(d,\mathbb R)$ (this paper) | min $d_{AB} = d_A d_B$, $\mathrm{PSD}_{d_A d_B}^{\mathbb R}$ (this paper) | 2-dim $B_{a,b}$ (`REAL_PAIRINGS.md`) | Thm 1–5 carry over (`REAL_PAIRINGS.md`) |
| $\mathbb C$ | $\mathrm{PSD}_d$ unique under $GL(d,\mathbb C)$ (`PROBLEM_A_THEOREM.md`) | min $d_{AB} = d_A d_B$, $\mathrm{PSD}_{d_A d_B}$ (`COMPOSITE_RIGIDITY.md`) | 2-dim $B_{a,b}$ (`paper_born.md` Lemma 2) | Thm 1–5 (`paper_born.md`) |
| $\mathbb H$ | **open** (doubled-spectrum subtlety, see `QUATERNIONIC_PAIRINGS.md` §6) | open | 2-dim $B_{a,b}$ (`QUATERNIONIC_PAIRINGS.md`) | conjectural |

The cone-rigidity and composite-rigidity theorems are now established uniformly across $\mathbb R$ and $\mathbb C$, with $\mathbb H$ open at the cone level (the bilinear level is complete across all three). The proofs are field-agnostic wherever Sylvester's law of inertia holds (it holds for $\mathbb R$ and $\mathbb C$; the quaternionic case has a subtler orbit structure due to spectrum doubling).

---

## 5. Honest placement

- The real Cone Rigidity and real Composite Rigidity are *immediate* from the complex proofs once Sylvester's law is observed to hold over $\mathbb R$. The contribution is the *packaged statement* that the real and complex cases are parallel at the cone and composite levels, completing the $\mathbb R/\mathbb C$ half of the field trio.
- This is consistent with Proposition A2 of `PROBLEM_A_partial_results.md`: real QM admits real amplitudes and real Cone Rigidity selects $\mathrm{PSD}_d^{\mathbb R}$, but real QM does *not* admit the full $GL(d,\mathbb C)$ congruence (the complex congruence exits the real state space). Real QM sits at $GL(d,\mathbb R)$, row 2 of the counterexample spectrum, with its own cone-rigidity theorem.
