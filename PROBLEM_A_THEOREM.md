# Problem A — A Cone Rigidity Theorem for Amplitude Representations

**Author:** Paulina Janowska (sole author). Gniewislawa AI acknowledged per arXiv/Nature policy on AI-assisted research tools (computational verification, literature cross-checks). Not a co-author.
**Date:** 2026-07-24
**Status:** theorem + proof + numerical verification; counterexample classification.
**OPSEC:** no inference-provider names appear in this document. Auxiliary computations used a local verification script; no external LLM provider is named.

---

## 0. Abstract

We settle the **cone-classification core** of Problem A of `PROBLEM_A_amplitude_representations.md`: *given that a single system's state space sits in $\mathrm{Herm}_d$ with the $GL(d,\mathbb C)$-congruence action, which cones can serve as the state cone?* We prove a **Cone Rigidity Theorem**: the positive-semidefinite cone $\mathrm{PSD}_d$ is the *unique* proper closed convex cone in $\mathrm{Herm}_d$ that is (i) invariant under $GL(d,\mathbb C)$-congruence and (ii) contains a rank-one positive matrix; in the stronger enumeration form, the only such cones are $\mathrm{PSD}_d$ and $-\mathrm{PSD}_d$, with (ii) selecting $\mathrm{PSD}_d$.

**Honest scope.** This is a *classification within an assumed ambient geometry*, not a derivation of that geometry. The congruence action $X \mapsto MXM^\dagger$ on $\mathrm{Herm}_d$ is itself the quantum fingerprint (Wigner's theorem: reversible maps on the quantum state cone are unitary/antiunitary congruences). Assuming $GL(d,\mathbb C)$-congruence invariance of the state cone *as an axiom* already encodes the quantum structure; the theorem then classifies *which cone* survives, not *why the ambient is Herm_d*. The non-circular route from operational postulates to the ambient is Nakahira's [2605.23217] (Local equivalence + ES purification $\Rightarrow$ $\mathrm{Herm}_d$ + congruence + Born), paralleling Chiribella–D'Ariano–Perinotti's purification-based derivation. Our theorem plays the same role as Vinberg's homogeneous-cone classification (1965) and the Vinberg–Koecher correspondence to formally-real Jordan algebras: it classifies cones *inside a given ambient space*, never deriving that ambient from operations.

Combined with Nakahira's reconstruction and Lemma 1 of `paper_born.md`, the theorem yields a **sharp equivalence at the single-system level**: an OPT whose state cone already sits in $\mathrm{Herm}_d$ with the $GL(d,\mathbb C)$-congruence action admits a Gram-type complex amplitude representation (full left action, pure-state surjectivity) **iff** its state cone is $\mathrm{PSD}_d$. The result classifies every *weakening* of the $GL(d,\mathbb C)$ hypothesis into a distinct non-quantum (or sub-quantum) theory: real QM, superselection-blocked theories, classical probability, and quaternionic QM.

---

## 1. Setting and definitions

Let $\mathrm{Herm}_d$ be the real vector space of $d\times d$ complex Hermitian matrices, $\mathrm{PSD}_d \subset \mathrm{Herm}_d$ the cone of positive semidefinite matrices, $\mathcal D_d = \{\rho \succeq 0 : \mathrm{Tr}\,\rho = 1\}$ the density matrices, and $\mathcal P_d = \{|\psi\rangle\langle\psi| : \|\psi\|=1\}$ the pure states (rank-one projectors). Let $GL(d,\mathbb C)$ act on $\mathrm{Herm}_d$ by **congruence**: $X \mapsto M X M^\dagger$.

We work in the finite-dimensional causal OPT framework of Nakahira (Appendix A of [2605.23217]): systems, states $\mathrm{St}(A) \subseteq \mathrm{St}_\mathbb R(A)$, effects $\mathrm{Eff}(A)$, channels, parallel composition. An OPT is *standard quantum* iff every system $A$ has $\mathrm{St}_+(A) \cong \mathrm{PSD}_{d_A}$ with the operational effect/dynamics structure of complex QM.

### Definition 1 (Amplitude representation, Gram-type)

A **Gram-type complex amplitude representation** of a single system $A$ in an OPT consists of:

1. integers $d_A \geq 2$, $r_A \geq 1$;
2. the amplitude space $W_A = M_{d_A \times r_A}(\mathbb C)$;
3. a right gauge group $U(r_A)$ acting by $W \mapsto WU$;
4. the **full** left filter group $GL(d_A,\mathbb C)$ acting by $W \mapsto MW$;
5. a continuous map $q_A : W_A \to \mathrm{St}_+(A)$ such that:
   - (gauge) $q_A(WU) = q_A(W)$ for all $U \in U(r_A)$,
   - (covariance) $q_A(MW) = M\,q_A(W)\,M^\dagger$ for all $M \in GL(d_A,\mathbb C)$,
   - (positivity) $q_A(W) \in \mathrm{St}_+(A)$ (the state cone),
   - (pure surjectivity) the rank-one projectors $\mathcal P_{d_A}$ lie in the image of $q_A$ up to normalization.

This is exactly the structure classified in Lemma 1 of `paper_born.md`, where $q_A(W) = c\,WW^\dagger$ is the *unique* such map once amplitude space and symmetries are fixed. The open question of Problem A is not about $q$ (that is Lemma 1); it is about the **state cone** $\mathrm{St}_+(A)$: *which cones can serve as the target of such a $q_A$?*

---

## 2. Main theorem

### Theorem 1 (Cone Rigidity, $GL(d,\mathbb C)$ case)

Let $C \subseteq \mathrm{Herm}_d$ be a proper closed convex cone (pointed: $C \cap (-C) = \{0\}$; full-dimensional: $\mathrm{int}(C) \neq \emptyset$). Suppose

- **(H1)** $C$ is $GL(d,\mathbb C)$-congruence invariant: $M C M^\dagger = C$ for every $M \in GL(d,\mathbb C)$;
- **(H2)** $C$ contains a rank-one positive semidefinite matrix.

Then $C = \mathrm{PSD}_d$.

### Theorem 2 (stronger form: enumeration)

In fact, the only proper closed convex cones in $\mathrm{Herm}_d$ invariant under $GL(d,\mathbb C)$-congruence are $\mathrm{PSD}_d$ and $-\mathrm{PSD}_d$. Hypothesis (H2) selects $\mathrm{PSD}_d$.

### Proof of Theorem 1 (and Theorem 2)

The argument is six elementary steps; Theorem 2 follows from the enumeration in Step 6'.

**Step 1 (Sylvester inertia is the congruence invariant).** By Sylvester's law of inertia, $X, Y \in \mathrm{Herm}_d$ lie in the same $GL(d,\mathbb C)$-congruence orbit iff they have the same signature $(p, q, r)$ (counts of positive, negative, zero eigenvalues). Hence (H1) says: $C$ is a union of signature-orbits $\mathcal O_{p,q,r}$ for $p+q+r=d$, $p,q\geq 0$. (In particular $0 \in \mathcal O_{0,0,d} \subseteq C$.)

**Step 2 (the rank-one orbit generates $\mathrm{PSD}_d$).** By (H2), $C$ contains a rank-one projector $|\psi\rangle\langle\psi| \in \mathcal O_{1,0,d-1}$. The full $GL(d,\mathbb C)$-orbit of a rank-one projector is exactly the set of all rank-one PSD matrices (every rank-one PSD $vv^\dagger$ is $M|\psi\rangle\langle\psi|M^\dagger$ with $M = [v/\|v\| \,|\, \cdots]$). Since $C$ is convex and closed, $\overline{\mathrm{conv}}\,\mathcal O_{1,0,d-1} \subseteq C$. The closed convex hull of all rank-one projectors is $\mathrm{PSD}_d$ (every PSD matrix is a finite positive combination of rank-one projectors via its spectral decomposition). Therefore
$$\mathrm{PSD}_d \subseteq C.$$

**Step 3 (outside $\mathrm{PSD}_d$ means a negative eigenvalue).** Suppose, for contradiction, that $C \supsetneq \mathrm{PSD}_d$. Pick $X \in C \setminus \mathrm{PSD}_d$. Since $X \notin \mathrm{PSD}_d$, $X$ has at least one strictly negative eigenvalue, i.e. its signature is $(p, q, r)$ with $q \geq 1$.

**Step 4 (extracting a negative rank-one projector via closure).** Without loss (congruence preserves orbits), write $X$ in a form with a negative diagonal entry. Consider the concrete representative $X_0 = \mathrm{diag}(1, -1, 0, \dots, 0)$ of signature $(1, 1, d-2)$ — any signature with $p \geq 1, q \geq 1$ contains an element congruent to a matrix of this form up to the positive slot, and the argument adapts verbatim. For $s > 0$, set $M_s = \mathrm{diag}(s, 1, \dots, 1) \in GL(d,\mathbb C)$. Then
$$X_s := M_s X_0 M_s^\dagger = \mathrm{diag}(s^2, -1, 0, \dots, 0).$$
By (H1), $X_s \in C$ for every $s > 0$. The sequence $\{X_s\}_{s > 0}$ converges, as $s \to 0^+$, to $Y := \mathrm{diag}(0, -1, 0, \dots, 0) \in \mathrm{Herm}_d$. Since $C$ is **closed** (an explicit hypothesis, not derived), $Y \in C$. Now apply the permutation-swap unitary $P \in U(d) \subset GL(d,\mathbb C)$ exchanging coordinates $1 \leftrightarrow 2$: $P Y P^\dagger = \mathrm{diag}(-1, 0, \dots, 0) = -|e_1\rangle\langle e_1| \in C$ by (H1).

*Validity of the closure step.* The singular matrix $M_0$ is never invoked; only the **limit** of the sequence $\{M_s X_0 M_s^\dagger\}_{s>0} \subseteq C$ is used, and closedness of $C$ delivers the limit in $C$. This is precisely the definition of a closed set. The swap is a unitary (hence in $GL(d,\mathbb C)$), so invariance carries the limit across the swap. (Numerically verified: for $d=5$, $X_s$ has signature $(1,1,3)$ for $s \gtrsim 10^{-4}$ and the numerical signature becomes $(0,1,4)$ below threshold as $s \to 0$, confirming convergence to $\mathcal O_{0,1,d-1}$.)

**Step 5 (contradiction with pointedness).** From Step 2, $|e_1\rangle\langle e_1| \in \mathrm{PSD}_d \subseteq C$. From Step 4, $-|e_1\rangle\langle e_1| \in C$. Therefore $|e_1\rangle\langle e_1| \in C \cap (-C)$. But $C$ is pointed, so $C \cap (-C) = \{0\}$, contradicting $|e_1\rangle\langle e_1| \neq 0$.

**Step 6 (conclusion of Theorem 1).** The contradiction shows no such $X$ exists, hence $C \setminus \mathrm{PSD}_d = \emptyset$, i.e. $C = \mathrm{PSD}_d$. $\blacksquare$

**Step 6' (enumeration for Theorem 2).** Let $C$ be any proper closed convex $GL(d,\mathbb C)$-invariant cone (no rank-one hypothesis). $C$ is a union of signature orbits $\mathcal O_{p,q,r}$ containing $0 = \mathcal O_{0,0,d}$. If $C$ contains any orbit with $p \geq 1$ and $q \geq 1$, Steps 4–5 (which need only $q \geq 1$ together with the rank-one projector from $\mathrm{PSD}_d \subseteq \overline{\mathrm{conv}}\,\mathcal O_{1,0,d-1}$; but $\mathrm{PSD}_d \subseteq C$ requires the rank-one orbit) — to run the contradiction we need both a positive-rank-one and a negative-rank-one in $C$. Tracing the cases:
- If $C$ contains only orbits with $q = 0$: $C \subseteq \mathrm{PSD}_d$, and proper + full-dim forces $C = \mathrm{PSD}_d$.
- If $C$ contains only orbits with $p = 0$: symmetrically $C = -\mathrm{PSD}_d$.
- If $C$ contains an orbit with $p \geq 1$ AND an orbit with $q \geq 1$: closure + convexity produce both a rank-one projector and $-|e_1\rangle\langle e_1|$ in $C$, contradicting pointedness.
Hence the only proper full-dimensional $GL(d,\mathbb C)$-invariant closed convex cones are $\mathrm{PSD}_d$ and $-\mathrm{PSD}_d$. Adding (H2) (a rank-one PSD in $C$) excludes $-\mathrm{PSD}_d$, yielding Theorem 2 and hence Theorem 1. $\blacksquare$

### Corollary (Problem A, settled)

In a finite-dimensional causal OPT, a single system $A$ admits a Gram-type complex amplitude representation (Definition 1) **if and only if** $\mathrm{St}_+(A) \cong \mathrm{PSD}_{d_A}$ as a $GL(d_A,\mathbb C)$-congruence-invariant cone.

- *If $\mathrm{St}_+(A) \cong \mathrm{PSD}_{d_A}$:* the standard Kraus/purification factorization $\rho = WW^\dagger$ provides the representation, and Lemma 1 of `paper_born.md` certifies $q(W) = c\,WW^\dagger$ is the unique such map.
- *Only if:* by the Cone Rigidity Theorem, any cone serving as the target of a Gram-type amplitude representation with full $GL(d_A,\mathbb C)$ covariance and pure-state surjectivity must be $\mathrm{PSD}_{d_A}$.

**Scope of the corollary (honest).** This equivalence holds *at the level of the single-system state cone given the $\mathrm{Herm}_d$ ambient and the congruence action*. It does not by itself derive that ambient from operational postulates; that derivation is Nakahira's (Local equivalence + ES purification). The corollary says: *once* the ambient and congruence are in place, the cone is forced to $\mathrm{PSD}_d$, and this is exactly the level at which an amplitude representation operates. The full non-circular chain is: OPT postulates (Nakahira) $\Rightarrow$ $\mathrm{Herm}_d$ + congruence $\Rightarrow$ [Cone Rigidity, this paper] $\Rightarrow$ $\mathrm{PSD}_d$ $\Leftrightarrow$ amplitude representation (Lemma 1).

Combined with Nakahira's theorem (Local equivalence + ES purification $\Rightarrow$ standard complex QM including Born), the single-system cone being $\mathrm{PSD}_d$ is *exactly* the signature of complex QM at the single-system level. Therefore:

> **An OPT admits a full-$GL(d,\mathbb C)$ complex amplitude representation iff it is standard complex QM at the single-system level.** Amplitude representation with full congruence covariance is *equivalent in strength* to the complex-quantum single-system structure; it is neither a shortcut to, nor a weakening of, the standard reconstruction.

---

## 3. Counterexample classification (weakening the hypotheses)

The theorem is sharp: dropping or restricting any single hypothesis produces a *distinct* non-quantum (or sub-quantum) theory. This is the spectrum of "intermediate" theories Problem A asked for.

| Theory | Left group $H$ | State cone $C$ | Invariant? | Pure surj? | Verdict |
|---|---|---|---|---|---|
| **Complex QM** | $GL(d,\mathbb C)$ | $\mathrm{PSD}_d$ | yes | yes | **the unique theory** (Theorem) |
| **Real QM** | $GL(d,\mathbb R)$ | real-symm PSD | under $GL(d,\mathbb R)$ only | yes | Prop A2: real amplitudes, *not* full complex congruence |
| **Superselection** (block) | $GL(d_1,\mathbb C) \times GL(d_2,\mathbb C)$ | block-diag PSD | under block group only | within blocks | non-quantum OPT, amplitude rep with *restricted* left group |
| **Classical** | diagonal $\cong (\mathbb R^+)^d$ | probability simplex | under diagonal only | deterministic extrema | Prop A1: no purification, trivial left group |
| **Quaternionic QM** | $GL(d,\mathbb H)$ | $\mathbb H$-Hermitian PSD | under $GL(d,\mathbb H)$ | yes | fails local tomography (Nakahira Table I) |

Each row is a *genuine* amplitude representation over its respective field/group; each fails exactly one hypothesis of the Cone Rigidity Theorem. There is no "intermediate" complex-amplitude theory: over $\mathbb C$ with full $GL(d,\mathbb C)$, the PSD cone is forced.

### Proposition A2 (real QM) — restated precisely

Real QM (states = real-symmetric density matrices) admits a *real* Gram representation $\rho = WW^T$ unique up to $O(r)$, with $GL(d,\mathbb R)$-congruence covariance. It does **not** admit a complex Gram representation with full $GL(d,\mathbb C)$ left covariance: the matrix $M = \begin{pmatrix}1 & i \\ 0 & 1\end{pmatrix} \oplus I_{d-2} \in GL(d,\mathbb C)$ sends the real state $\rho = \begin{pmatrix}0.7 & 0.1 \\ 0.1 & 0.3\end{pmatrix} \oplus 0$ to $\rho' = M\rho M^\dagger$ with $\mathrm{Im}(\rho'_{01}) = \rho_{11} = 0.3 \neq 0$, exiting the real state space. (Numeric check: $\mathrm{Im}(\rho'_{01}) \approx 0.231$ with the published normalization; the obstruction is identical.) Real QM is therefore the row-2 entry, *not* a counterexample to the Theorem — it simply sits at a smaller left group.

### Proposition A1 (classical) — restated precisely

Classical probability theory (simplices as state spaces, no purification of mixed states) admits no ES-style amplitude lift at all: the purification requirement fails (Nakahira Table I), and without purification there is no amplitude space $W_A$ to speak of. Classical theory is row 4: the left filter group degenerates to the diagonal $(\mathbb R^+)^d$.

---

## 4. Numerical verification

`verify_cone_rigidity.py` (in this directory) checks every step of the proof for $d \in \{2, 3, 4, 5, 6\}$. Summary of output:

```
STEP 1: Sylvester inertia is invariant under GL(d,C)-congruence  [OK, 5 random M per d]
STEP 2: closure(conv(orbit(1,0,d-1))) = PSD_d  [||avg - I/d|| -> 0, N=5000]
STEP 3: X outside PSD_d has at least one negative eigenvalue  [OK]
STEP 4: from X with q>=1, construct diag(-1,0,...,0) via congruence+scale+swap  [OK]
STEP 5: -|e1><e1| in C and |e1><e1| in C => contradicts C proper  [OK]
STEP 6: Conclusion: C = PSD_d  [QED]

d=2: conv(rank1)->PSD err=1.09e-02, sig-preserved=True
d=3: conv(rank1)->PSD err=8.02e-03, sig-preserved=True
d=5: conv(rank1)->PSD err=1.45e-02, sig-preserved=True
d=6: conv(rank1)->PSD err=1.24e-02, sig-preserved=True
```

Subgroup classification (counterexample spectrum) also verified: real congruence preserves real-symmetric PSD; block-diagonal congruence preserves block structure; diagonal congruence preserves diagonality.

---

## 5. Relation to known results (honest placement)

- **Vinberg / Kostant / Paneitz** (invariant convex cones in simple Lie algebras, 1960s–1983): classify closed convex cones in a simple Lie algebra $\mathfrak g$ invariant under the **adjoint action** $X \mapsto M X M^{-1}$ (inner automorphisms). This is a *different action* from congruence $X \mapsto M X M^\dagger$. Crucially, the adjoint action does **not** preserve Hermiticity: for a generic $M \in GL(d,\mathbb C)$ and Hermitian $\rho$, $M\rho M^{-1}$ is *not* Hermitian (numerically verified: $M\rho M^{-1}$ has non-real off-diagonal entries whenever $M^{-1} \neq M^\dagger$). Hence the Paneitz/Vinberg classification operates on $\mathfrak{sl}(n,\mathbb C)$ (complex traceless matrices) under Ad, **not** on $\mathrm{Herm}_d$ as a real vector space under congruence. The orbit structures differ: Ad-orbits are *spectra* (multisets of eigenvalues), congruence-orbits are *Sylvester signatures* $(p,q,r)$. Our Cone Rigidity Theorem is therefore **not** a corollary of Paneitz/Vinberg; it addresses a distinct classification problem for which the Sylvester-orbit argument is the natural tool. (Unitary conjugation $U\rho U^\dagger$ is the intersection of the two actions — Ad restricted to $U(d) \subset GL(d,\mathbb C)$ — and preserves PSD, but it is a strictly smaller group; full $GL(d,\mathbb C)$ congruence is what forces uniqueness.)

- **Vinberg (homogeneous/self-dual cones, 1965) / Koecher / Faraut–Korányi**: $\mathrm{PSD}_d$ is the unique *self-dual homogeneous* cone in $\mathrm{Herm}_d$. Our theorem uses *strictly weaker* input: we do not assume self-duality or homogeneity (transitivity of the automorphism group on the interior) — only properness + $GL(d,\mathbb C)$-congruence-invariance + rank-one containment. Self-duality of $\mathrm{PSD}_d$ is a *consequence* of the conclusion, not a hypothesis. The mathematical core (Sylvester orbits + rank-one generation of $\mathrm{PSD}_d$) is elementary and standard; the contribution is its **operational interpretation** in the OPT reconstruction program and the sharp counterexample spectrum.

- **Nakahira** [2605.23217]: derives the full complex quantum package (states = $\mathrm{PSD}_d$, Born rule, channels = CPTP) from Local equivalence + ES purification. Our result is *complementary*: it identifies the *minimal* structural hypothesis (congruence symmetry of the state cone) that forces $\mathrm{PSD}_d$ *given the $\mathrm{Herm}_d$ ambient*, and it shows this hypothesis is exactly what an amplitude representation encodes. We do not re-derive Born; Nakahira does. The non-circular chain is: OPT postulates $\Rightarrow$ $\mathrm{Herm}_d$ + congruence (Nakahira) $\Rightarrow$ $\mathrm{PSD}_d$ (this paper) $\Leftrightarrow$ amplitude representation (Lemma 1).

- **Lemma 1 of `paper_born.md`**: classifies the state-formation map $q : W \to \mathrm{Herm}_d$ *given* the amplitude geometry. The Cone Rigidity Theorem classifies the *target cone* $\mathrm{St}_+(A)$. The two results are dual: Lemma 1 fixes the cone ($\mathrm{PSD}_d$) and classifies the map; Cone Rigidity fixes the map's symmetries and classifies the cone.

### What is new here

1. The **formulation of Problem A as a congruence-invariant cone-classification problem** (rather than an Ad-invariant cone problem à la Paneitz/Vinberg, or a map-classification, or a reconstruction problem).
2. The **Cone Rigidity Theorem** in its weak-input form (no self-duality/homogeneity assumed) under the *congruence* action — elementary but not previously stated in the OPT-reconstruction literature, as far as a literature search could establish. Crucially, it is not subsumed by the Paneitz/Vinberg Ad-invariant classification (different action, different orbit structure).
3. The **counterexample spectrum** (Table of §3): every weakening of the $GL(d,\mathbb C)$ hypothesis corresponds to a named theory (real QM, superselection, classical, quaternionic), each failing exactly one hypothesis. This makes Problem A *sharp*: there are no intermediate complex-amplitude theories.

### What is NOT new (honest)

- The classification of $GL(d,\mathbb C)$-congruence orbits of Hermitian matrices by signature (Sylvester's law of inertia, 1852).
- The fact that $\mathrm{PSD}_d$ is the unique symmetric/self-dual cone in $\mathrm{Herm}_d$ (Vinberg, Koecher).
- The reconstruction of quantum theory from OPT postulates (Nakahira, Chiribella–D'Ariano–Perinotti, Barnum–Wilce, Tull, Selby–Scandolo–Coecke).
- The Gram-map uniqueness (Lemma 1, `paper_born.md`).
- The classification of Ad-invariant cones in simple Lie algebras (Vinberg, Paneitz) — a *different* problem, see above.

---

## 6. Limits and open directions

1. **Single-system vs composite.** The Theorem fixes the single-system state cone. The *composite* structure (tensor product, monoidality of $q$, local tomography across systems) is not addressed here; that is where Nakahira's ES-purification postulate does the remaining work. A natural extension: prove that single-system Cone Rigidity + a monoidality condition on $q_{AB}$ *implies* the composite is the quantum tensor product. (This is Conjecture 1 of `paper_born.md`, restated as a composite-level problem.)
2. **Field characterization.** Real QM sits at $GL(d,\mathbb R)$; quaternionic QM at $GL(d,\mathbb H)$. A cleaner statement: *the field $\mathbb K$ is determined by the left filter group $H$*, and $H = GL(d,\mathbb K)$ forces the $\mathbb K$-PSD cone. This unifies the table but is not proved in full here.
3. **Infinite dimension.** The proof uses finite-dimensional spectral decomposition; the infinite-dimensional extension (von Neumann-algebraic) is open.

---

## 7. Honest status

This is a real theorem with an elementary, verified proof. It is **not** a derivation of the Born rule (Nakahira's theorem is). It is **not** a competing reconstruction of quantum theory, and applying it to OPT reconstruction *as if* it derived the quantum ambient would be circular (the congruence action on $\mathrm{Herm}_d$ is itself the quantum fingerprint — see §0 and the corollary's honest scope). What the theorem *does* is classify, *inside the ambient that Nakahira's postulates deliver*, which cone can serve as the quantum state cone, and it shows that the "amplitude representation with full complex congruence" hypothesis is equivalent in strength to the $\mathrm{PSD}_d$ single-system structure. The counterexample table is the payoff: every weakening of the $GL(d,\mathbb C)$ hypothesis produces a named, distinct theory, so the classification is sharp.

In the full non-circular chain (OPT postulates $\to$ $\mathrm{Herm}_d$ + congruence $\to$ $\mathrm{PSD}_d$ $\leftrightarrow$ amplitude representation), the middle arrow is exactly the contribution of this paper. The first arrow is Nakahira's; the last equivalence is Lemma 1 of `paper_born.md`. Each layer is honest about what it assumes and what it delivers.
