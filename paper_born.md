# Selectors for the Born Pairing Among Simultaneously Unitarily Invariant Bilinear Pairings

**Author:** Paulina Janowska
**Affiliation:** Independent researcher, Poznan, Poland
**Date:** 2026-07-28
**Version:** 1.0 (public preprint)

---

## Abstract

Let $\widetilde B:\mathrm{Herm}_d\times\mathrm{Herm}_d\to\mathbb R$ be a real-bilinear form, invariant under simultaneous unitary conjugation, $\widetilde B(UEU^\dagger,U\rho U^\dagger)=\widetilde B(E,\rho)$, whose restriction to effects and normalized states $B:=\widetilde B|_{\mathrm{Eff}_d\times\mathcal D_d}$ takes values in $[0,1]$ and is normalized, $B(I,\rho)=1$ for $\rho\in\mathcal D_d$. Assume the standard representation-theoretic input made explicit in Section 5.2. Then every such form is
$$\widetilde B(E,\rho)=a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)\,\mathrm{Tr}(\rho)$$
with real $a,b$ and $a+bd=1$; positivity forces $a\in[-1/(d-1),1]$ (for $d\geq 2$). The Born rule $B(E,\rho)=\mathrm{Tr}(E\rho)$ corresponds to $a=1,b=0$, but is *not* selected by invariance, bilinearity, positivity, and normalization alone. We give a catalogue of elementary conditional results after the classification: Theorems 6.1, 6.3, and 6.4 select Born; Theorem 6.5 does so for $d\geq3$ with a qubit caveat; Theorem 6.2 is an exact Born/state-insensitive dichotomy.

- **Theorem 6.1 (one impossible event).** If $B$ vanishes on a single pair of orthogonal rank-one projectors $P,Q$ (i.e. $B(Q,P)=0$ with $PQ=0$), then $b=0$ and $B=\mathrm{Tr}(E\rho)$.
- **Theorem 6.2 (rank-one product monoidality dichotomy).** Every normalized rank-one product-monoidal family is exactly either the Born family or the state-insensitive family $B_d(E,\rho)=\mathrm{Tr}(E)/d$.
- **Theorem 6.3 (one pure self-certainty event).** If $B(P,P)=1$ for one rank-one projector $P$ (hence both an effect and a state), then $a=1$ and $B=\mathrm{Tr}(E\rho)$.
- **Theorem 6.4 (dimension-independence of pure transitions).** If the transition probability between two pure states depends only on the two states and not on the ambient dimension $d$ into which they are embedded, then $a_d=1$ for all $d\geq 2$.
- **Theorem 6.5 (perfect distinguishability).** If two pure states are perfectly distinguishable by some effect ($B(E,P)=1$ and $B(E,Q)=0$), then they are necessarily orthogonal; for $d\geq 3$ necessarily $a=1$ (Born); for $d=2$ one has $a\in\{1,-1\}$. The anti-Born endpoint $a=-1$ is excluded by either Theorem 6.1 or Theorem 6.3, and is incompatible with the monoidality hypothesis of Theorem 6.2.
- **Proposition 6.6 (unbounded ancilla stability).** If a positive normalized family is stable under adjoining arbitrary idle ancillas, then $a_d=c\in[0,1]$ is dimension-independent. This removes the negative branch, including anti-Born qubits, and also forbids dimension-varying families; it still does not by itself force Born.
- **Corollary 6.7 (stable one-bit selector).** If a positive normalized family is stable under arbitrary idle ancillas and has one exactly distinguishable pure-state pair in any dimension, then $B_d=\mathrm{Tr}(E\rho)$ in every dimension. This is a direct synthesis of Theorem 6.5 and Proposition 6.6, not a priority claim.

Conditional on that standard input, the remaining reduction and selector calculations are elementary. Theorems 6.1 and 6.3 are equivalent under the classification (Proposition 6.8). Theorems 6.1, 6.3, and 6.5 are elementary conditional selectors; Theorem 6.2 is an elementary dichotomy with a state-insensitive branch; no priority claim is made. Theorem 6.4 is a restricted restatement of Hossenfelder's dimension-independence argument [1]. We do not derive the Hermitian structure or quantum theory; Nakahira [2] already derives the full complex quantum package (including Born) from two OPT postulates, so the present selectors live one layer below that reconstruction.

---

## 1. Introduction

### 1.1 The question

The Born rule $p(E|\rho)=\mathrm{Tr}(E\rho)$ is the standard pairing of a quantum state $\rho$ with an effect $E$. It is *not* the unique bilinear, positive, unitarily invariant, normalized pairing: the one-parameter family $B_a(E,\rho)=a\,\mathrm{Tr}(E\rho)+(1-a)/d\cdot\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ with $a\in[-1/(d-1),1]$ satisfies all four conditions, and for $a\neq 1$ is not Born. This family is the full classification (Lemma 5.1 below). The question is: which simple additional condition selects Born?

### 1.2 What this paper is

This paper is:

- a classification of simultaneously unitarily invariant real-bilinear forms on $\mathrm{Herm}_d$ (Lemma 5.1), conditional on the standard irreducibility/commutant fact for the traceless adjoint component;
- **five elementary results (Theorems 6.1--6.5):** Theorems 6.1, 6.3, and 6.4 select Born; Theorem 6.5 does so above the qubit case; Theorem 6.2 gives an exact Born/state-insensitive dichotomy;
- Proposition 6.8: local equivalence of Theorems 6.1 and 6.3;
- a small classification lemma for the Gram map on complex amplitudes (Lemma 3.1), included as scaffolding;
- an honest statement of the circularity boundary and of the relation to Galley–Masanes [3] and Nakahira [2].

This paper is not:

- a derivation of the Born rule from operational principles;
- a derivation of the Hermitian structure, the effect cone, or the complex amplitude representation;
- a claim that the selectors are deep new theorems (they are elementary corollaries of the classification);
- a reconstruction of quantum theory.

### 1.3 Related prior work

The decomposition $\mathrm{Herm}_d=\mathbb RI\oplus\mathrm{Herm}_d^0$ and the uniqueness of invariant forms on irreducible representations are standard representation theory. Galley and Masanes [3] classify *all* alternatives to the measurement postulates that keep pure states as rays in $\mathbb{CP}^{d-1}$ and unitary dynamics, subject to finite-dimensional mixed-state spaces; their alternatives correspond to representations of the unitary group and are far broader than the bilinear class studied here. In particular, unrestricted non-Born alternatives in their catalogue violate bit symmetry. Our Lemma 5.1 is the thin slice of that landscape in which outcome probabilities extend to a real-bilinear form on $\mathrm{Herm}_d\times\mathrm{Herm}_d$: only the family $B_{a,b}$ survives. Theorems 6.1, 6.3, and 6.4 select Born inside that slice; Theorem 6.2 additionally gives a Born/state-insensitive dichotomy, and Theorem 6.5 has its explicit qubit caveat. Hossenfelder [1] uses dimension-independence of transition probabilities on the complex sphere (a pure-state continuous setting that already includes orthogonal vanishing). Lax [4] uses Fisher-non-expansion and Cramér-Rao bounds. Gleason [5] uses additivity over orthogonal decompositions; Busch [6] extends to POVMs and the qubit case. Chiribella, D'Ariano, and Perinotti [7] derive quantum theory from purification; Barnum and Wilce [8] from local tomography plus Jordan structure; Tull [9] and Selby, Scandolo, and Coecke [10] categorically; Nakahira [2] from two operational principles (local equivalence + ES purification), recovering the full complex package including Born — so our selectors are not a competing OPT reconstruction. Procesi [11] treats related $GL(V)$-equivariant polynomial maps on endomorphism variables. It provides invariant-theoretic context only; it neither contains nor formally implies Lemma 3.1, whose domain, symmetry group, regularity, and positivity hypotheses differ. Massart and Absil [12] treat the ... [truncated]

### 1.4 Outline

Section 2 fixes notation. Section 3 states and proves Lemma 3.1 (Gram map classification) as scaffolding. Section 4 records the fibre and quotient geometry. Section 5 states the classification of invariant bilinear pairings (Lemma 5.1), reducing the representation-theoretic step to an explicit standard input. Section 6 gives the selector catalogue and the monoidality dichotomy. Section 7 discusses limits, circularity, and the status of the results. Section 8 confronts an open conjecture with Nakahira's result. Section 9 briefly outlines the remaining amplitude-representation problem.

---

## 2. Preliminaries

Fix $d\geq 2$ (the case $d=1$ is trivial and excluded from the selectors). Write $\mathrm{Herm}_d$ for Hermitian $d\times d$ matrices, $\mathrm{PSD}_d$ for the positive semidefinite cone, $\mathcal D_d=\{\rho\succeq 0:\mathrm{Tr}\,\rho=1\}$ for density matrices, and $\mathrm{Eff}_d=\{E:0\leq E\leq I\}$ for effects. The unitary group $U(d)$ acts on $\mathrm{Herm}_d$ by simultaneous conjugation $E\mapsto UEU^\dagger$.

A key distinction: for a scalar-valued form $B(E,\rho)$, the condition $B(UEU^\dagger,U\rho U^\dagger)=B(E,\rho)$ is **invariance** (the value is unchanged), not covariance (covariance applies to operator-valued maps whose output transforms). We use "invariant" throughout.

---

## 3. The Gram map (scaffolding)

### 3.1 Statement

**Lemma 3.1 (Gram map uniqueness).** Let $q:M_{d\times r}(\mathbb C)\to\mathrm{Herm}_d$ be a continuous map satisfying, for every $W$, $M\in GL(d,\mathbb C)$, $U\in U(r)$:

1. $q(WU)=q(W)$ (right gauge invariance);
2. $q(MW)=M\,q(W)\,M^\dagger$ (left congruence covariance);
3. $q(W)\succeq 0$ (positivity).

Then $q(W)=c\,WW^\dagger$ for some $c\geq 0$.

### 3.2 Proof

First, $q(0)=q(M0)=Mq(0)M^\dagger$ for every $M\in GL(d,\mathbb C)$. Taking $M=2I$ gives $q(0)=4q(0)$, hence $q(0)=0$.

**Step 1 (rank reduction).** Let $k=\mathrm{rank}\,W$ and $J_k=\begin{pmatrix}I_k&0\\0&0\end{pmatrix}$. Every rank-$k$ matrix has a decomposition $W=MJ_kU$ with $M\in GL(d,\mathbb C)$, $U\in U(r)$ (full SVD, singular values absorbed into $M$). By (1) then (2), $q(W)=M\,q(J_k)\,M^\dagger$, so $q$ on the rank-$k$ stratum is determined by $q(J_k)$.

**Step 2 (stabilizer).** For $S=\begin{pmatrix}I_k&B\\0&C\end{pmatrix}$ with $B\in M_{k\times(d-k)}$, $C\in GL(d-k)$, we have $SJ_k=J_k$. By (2), $q(J_k)=Sq(J_k)S^\dagger$. Writing $q(J_k)=\begin{pmatrix}X&Y\\Y^\dagger&Z\end{pmatrix}$, the constraint for all $B,C$ forces $Z=0$ (from $CZC^\dagger=Z$) and then $Y=0$ (from $(Y+BZ)C^\dagger=Y$). So $q(J_k)=\begin{pmatrix}A_k&0\\0&0\end{pmatrix}$, $A_k\succeq 0$.

**Step 3 (Schur).** For $V\in U(k)$, $L_V=\mathrm{diag}(V,I_{d-k})$ and $R_V=\mathrm{diag}(V^\dagger,I_{r-k})$ satisfy $L_VJ_kR_V=J_k$. By (1),(2), $VA_kV^\dagger=A_k$ for all $V\in U(k)$. Since $U(k)$ acts irreducibly on $\mathbb C^k$, Schur's lemma gives $A_k=c_kI_k$.

**Step 4 (continuity).** $W_\varepsilon=\mathrm{diag}(s_1,\ldots,s_k,\varepsilon,0,\ldots)\to W_0=\mathrm{diag}(s_1,\ldots,s_k,0,\ldots)$ as $\varepsilon\to 0$. On the rank-$(k+1)$ stratum, $q(W_\varepsilon)=c_{k+1}W_\varepsilon W_\varepsilon^\dagger$. Hence continuity gives $c_{k+1}W_\varepsilon W_\varepsilon^\dagger=q(W_\varepsilon)\to q(W_0)=c_kW_0W_0^\dagger$, while $W_\varepsilon W_\varepsilon^\dagger\to W_0W_0^\dagger$. For nonzero $W_0$, $c_{k+1}=c_k$. Thus $q(W)=c\,WW^\dagger$. $\blacksquare$

### 3.3 Why unitary covariance is too weak

$q_n(W)=(WW^\dagger)^n$ is unitarily covariant for all $n\geq 1$ (conjugation commutes with powers) but fails full congruence covariance for $n>1$. Congruence under $GL(d,\mathbb C)$, not just $U(d)$, is what selects degree two.

---

## 4. Fibres and quotient geometry

**Proposition 4.1.** For $W,V\in M_{d\times r}(\mathbb C)$ with $WW^\dagger=VV^\dagger$, there exists $U\in U(r)$ with $V=WU$.

*Proof.* Put $A:=WW^\dagger=VV^\dagger$. The left polar decompositions give partial isometries $S_W,S_V:\mathbb C^r\to\mathbb C^d$ such that
$$W=A^{1/2}S_W,\qquad V=A^{1/2}S_V.$$
Both partial isometries have final space $\operatorname{supp}A$ and initial spaces $(\ker S_W)^\perp$ and $(\ker S_V)^\perp$, respectively. Therefore $S_W^\dagger S_V$ is a unitary isomorphism from $(\ker S_V)^\perp$ onto $(\ker S_W)^\perp$. Moreover,
$$\dim\ker S_W=\dim\ker S_V=r-\operatorname{rank}A.$$
Choose any unitary isomorphism $U_0:\ker S_V\to\ker S_W$ and define $U\in U(r)$ as $S_W^\dagger S_V$ on $(\ker S_V)^\perp$ and $U_0$ on $\ker S_V$. Then $S_WU=S_V$, so
$$WU=A^{1/2}S_WU=A^{1/2}S_V=V.$$
This construction works for rectangular matrices and arbitrary degeneracies. $\square$

Thus $M_{d\times r}(\mathbb C)/U(r)\cong\{\rho\succeq 0:\mathrm{rank}\,\rho\leq r\}$ (all ranks), standard quotient geometry [12].

**Proposition 4.2 (monoidality after normalization).** With $\mathrm{Tr}\,q(W)=\mathrm{Tr}(WW^\dagger)$ forcing $c=1$, $q(W)=WW^\dagger$ is strictly monoidal: $q(W_A\otimes W_B)=q(W_A)\otimes q(W_B)$.

---

## 5. Classification of invariant bilinear pairings

### 5.1 Statement

**Lemma 5.1.** Assume the standard representation-theoretic input stated in Section 5.2. Let $\widetilde B:\mathrm{Herm}_d\times\mathrm{Herm}_d\to\mathbb R$ be real-bilinear and invariant under simultaneous unitary conjugation: $\widetilde B(UEU^\dagger,U\rho U^\dagger)=\widetilde B(E,\rho)$ for all $U\in U(d)$. Then there exist real $a,b$ (depending on $d$) such that
$$\widetilde B(E,\rho)=a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)\,\mathrm{Tr}(\rho).$$

### 5.2 Reduction to a standard representation-theoretic input

Decompose $\mathrm{Herm}_d=\mathbb RI\oplus\mathrm{Herm}_d^0$, where $\mathbb RI=\{\lambda I\}$ and $\mathrm{Herm}_d^0=\{H\in\mathrm{Herm}_d:\mathrm{Tr}\,H=0\}$. Under $U(d)$ conjugation, $\mathbb RI$ carries the trivial representation and $\mathrm{Herm}_d^0$ carries the adjoint representation.

**Standard representation-theoretic input.** We use the standard fact that the conjugation representation of $U(d)$ on $\mathrm{Herm}_d^0$ is real-irreducible and has scalar commutant,
$$\mathrm{End}_{U(d)}(\mathrm{Herm}_d^0)\cong\mathbb R.$$
Equivalently, after complexification, this is the irreducibility of the adjoint representation on $\mathfrak{sl}_d(\mathbb C)$; see, for example, the standard highest-weight treatment in Fulton and Harris [15]. This paper treats the resulting real irreducibility/scalar-commutant statement as an explicit assumption rather than re-proving it. It is the only non-elementary input in Lemma 5.1. The remaining reduction is included explicitly below.

**Claim 5.2 (no cross-terms).** Any invariant bilinear form $\widetilde B$ satisfies $\widetilde B(S,T_0)=\widetilde B(T_0,S)=0$ for $S\in\mathbb RI$, $T_0\in\mathrm{Herm}_d^0$.

*Proof of Claim 5.2.* Fix $S=\lambda I\in\mathbb RI$. The map $\phi_\lambda:\mathrm{Herm}_d^0\to\mathbb R$, $\phi_\lambda(T_0)=\widetilde B(\lambda I,T_0)$, is $U(d)$-equivariant (by invariance of $\widetilde B$: $\widetilde B(U\lambda IU^\dagger,UT_0U^\dagger)=\widetilde B(\lambda I,T_0)$, and $U\lambda IU^\dagger=\lambda I$). Since $\mathbb RI$ carries the trivial representation, $\phi_\lambda$ is an intertwiner from the adjoint (non-trivial irreducible) to the trivial representation. By Schur's lemma (real form: any equivariant linear map between non-isomorphic irreducible real representations is zero), $\phi_\lambda=0$, giving $\widetilde B(S,T_0)=0$. The reversed cross-term $\widetilde B(T_0,S)$ vanishes by the same argument with the two slots interchanged (or by symmetry of the invariant form, if $B$ is symmetric; in general, apply the argument to $\widetilde B'(E,\rho):=\widetilde B(\rho,E)$, which is also invariant). $\square$

**Claim 5.3 (uniqueness on each component).** The space of invariant bilinear forms on $\mathbb RI\times\mathbb RI$ is one-dimensional, and on $\mathrm{Herm}_d^0\times\mathrm{Herm}_d^0$ is one-dimensional.

*Proof of Claim 5.3.* On $\mathbb RI\times\mathbb RI$: identify $\mathbb RI\cong\mathbb R$ via $\lambda I\mapsto\lambda$; the trivial action leaves any bilinear form $\lambda\mu\mapsto c\lambda\mu$ invariant, a one-dimensional space.

On $\mathrm{Herm}_d^0\times\mathrm{Herm}_d^0$: let $V:=\mathrm{Herm}_d^0$. The adjoint representation of $U(d)$ on $V$ is absolutely irreducible (complexification $\mathfrak{sl}_d$ is complex-irreducible), so by the real Schur lemma its commutant is $\mathrm{End}_{U(d)}(V)\cong\mathbb R$ (scalar endomorphisms only). The trace form $\langle A,B\rangle:=\mathrm{Tr}(AB)$ is a non-degenerate $U(d)$-invariant bilinear form on $V$ (invariance by cyclicity: $\mathrm{Tr}(UAU^\dagger\,UBU^\dagger)=\mathrm{Tr}(AB)$), hence gives a $U(d)$-equivariant isomorphism $\psi:V\to V^*$, $\psi(A)=\langle A,\cdot\rangle$. Now any invariant bilinear form $B_0$ on $V$ corresponds, via $\psi^{-1}$ on the second slot, to a $U(d)$-equivariant endomorphism $\Phi:V\to V$ defined by $B_0(A,B)=\langle\Phi(A),B\rangle=\mathrm{Tr}(\Phi(A)B)$. (Equivariance of $\Phi$ follows from invariance of $B_0$ and $\langle\cdot,\cdot\rangle$.) Since $\mathrm{End}_{U(d)}(V)=\mathbb R$, $\Phi=\alpha\,\mathrm{id}$ for some $\alpha\in\mathbb R$, giving $B_0(A,B)=\alpha\,\mathrm{Tr}(AB)$. Thus the space of invariant bilinear forms on $V\times V$ is one-dimensional, spanned by the trace form. $\square$

**Remark.** Conditional on the stated standard input, the trace form is a non-degenerate invariant bilinear form giving $V\cong V^*$, and the argument above forces every invariant bilinear form on $V$ to be a scalar multiple of the trace. This separates the standard representation-theoretic premise from the elementary reduction used by the selector theorems.

Combining the decomposition, the stated standard input, and Claims 5.2--5.3: $\widetilde B(E,\rho)=b\,(\mathrm{Tr}(E)/d)(\mathrm{Tr}(\rho)/d)\cdot d^2 + a\,\mathrm{Tr}(E_0\rho_0)$ where $E_0,\rho_0$ are traceless parts; using $\mathrm{Tr}(E\rho)=\mathrm{Tr}(E_0\rho_0)+\mathrm{Tr}(E)\mathrm{Tr}(\rho)/d$ and absorbing the constant into the definition of $b$, we obtain $\widetilde B(E,\rho)=a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)$. $\blacksquare$

### 5.3 Positivity and normalization

Restrict to $B:=\widetilde B|_{\mathrm{Eff}_d\times\mathcal D_d}$. Normalization $B(I,\rho)=1$ for $\mathrm{Tr}\,\rho=1$ gives $a+bd=1$, so $b=(1-a)/d$. Positivity on all effects and normalized states forces $a\in[-1/(d-1),1]$. If $a<0$, then
$$B(E,\rho)\geq a\lambda_{\max}(E)+b\,\mathrm{Tr}(E)\geq(a+b)\lambda_{\max}(E),$$
because $b>0$ and $\mathrm{Tr}(E)\geq\lambda_{\max}(E)$. Thus $a+b\geq0$ is sufficient; rank-one $E$ with $\rho$ in its one-eigenspace shows it is necessary. Substituting $b=(1-a)/d$ gives $a\geq-1/(d-1)$. If $a\geq0$, positivity requires $b\geq0$ (again test rank-one $E$ against an orthogonal pure state), hence $a\leq1$; conversely $B(E,\rho)\geq b\,\mathrm{Tr}(E)\geq0$. Finally $B(E,\rho)\leq1$ follows from $B(I-E,\rho)\geq0$.

The Born rule is $a=1$ (so $b=0$). It is *not* selected by invariance, bilinearity, positivity, and normalization alone.

---

## 6. Selector theorems

**Standing convention for this section.** Every theorem and proposition below assumes Lemma 5.1, including the standard representation-theoretic input stated in Section 5.2. Thus the results in this section are conditional selector statements inside the classified invariant-bilinear family.

### 6.1 Theorem 6.1: one impossible event

**Theorem 6.1.** Under the standing convention, let $d\geq 2$ and let $\widetilde B:\mathrm{Herm}_d\times\mathrm{Herm}_d\to\mathbb R$ be real-bilinear and unitarily invariant, with $B:=\widetilde B|_{\mathrm{Eff}_d\times\mathcal D_d}$ normalized ($B(I,\rho)=1$ for $\rho\in\mathcal D_d$). Suppose there exist two orthogonal rank-one projectors $P,Q$ (i.e. $PQ=0$) such that $B(Q,P)=0$. Then $B(E,\rho)=\mathrm{Tr}(E\rho)$ on $\mathrm{Eff}_d\times\mathcal D_d$.

*Proof.* By Lemma 5.1, $B(E,\rho)=a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ with $a+bd=1$. For rank-one projectors $P,Q$ with $PQ=0$: $\mathrm{Tr}(QP)=0$, $\mathrm{Tr}(Q)=\mathrm{Tr}(P)=1$. So $B(Q,P)=a\cdot 0+b\cdot 1\cdot 1=b$. The hypothesis $B(Q,P)=0$ forces $b=0$, hence $a=1$, hence $B(E,\rho)=\mathrm{Tr}(E\rho)$. $\blacksquare$

**Remark.** The hypothesis is stated for a single pair $P,Q$. By unitary invariance, $B$ vanishes on every pair of orthogonal rank-one projectors (any such pair is $UPU^\dagger,UQU^\dagger$ for some $U$). So one calibrated impossible event — "this measurement returns zero on a state orthogonal to it" — selects Born within the invariant bilinear class.

### 6.2 Theorem 6.2: rank-one product monoidality

**Definition (rank-one product monoidality).** A family $\{B_d\}_{d\geq 2}$ is *rank-one product monoidal* if for every $d_A,d_B\geq 2$, every normalized $\rho_A\in\mathcal D_{d_A}$, $\rho_B\in\mathcal D_{d_B}$, and rank-one projectors $P_A=|e\rangle\langle e|$, $P_B=|f\rangle\langle f|$,
$$B_{d_Ad_B}(P_A\otimes P_B,\;\rho_A\otimes\rho_B) = B_{d_A}(P_A,\rho_A)\,B_{d_B}(P_B,\rho_B).$$

**Theorem 6.2.** Under the standing convention, let $\{B_d\}_{d\geq 2}$ be a family of normalized restrictions of unitarily invariant real-bilinear forms on $\mathrm{Herm}_d$. If the family is rank-one product monoidal, exactly one of the following holds:

1. $a_d=1$, $b_d=0$ for every $d\geq2$, so $B_d(E,\rho)=\mathrm{Tr}(E\rho)$ (Born);
2. $a_d=0$, $b_d=1/d$ for every $d\geq2$, so $B_d(E,\rho)=\mathrm{Tr}(E)/d$ on normalized states (state-insensitive pairing).

*Proof.* Fix $d_A,d_B\geq 2$. Set $X=\langle e|\rho_A|e\rangle\in[0,1]$, $Y=\langle f|\rho_B|f\rangle\in[0,1]$ (these vary independently as $\rho_A,\rho_B$ range over $\mathcal D$). For rank-one projectors, $\mathrm{Tr}(P_A\rho_A)=X$, $\mathrm{Tr}(P_B\rho_B)=Y$, $\mathrm{Tr}(P_A)=\mathrm{Tr}(P_B)=1$, $\mathrm{Tr}(\rho_A)=\mathrm{Tr}(\rho_B)=1$. The monoidality identity becomes
$$a_{d_Ad_B}XY + b_{d_Ad_B}\cdot 1\cdot 1 = (a_{d_A}X+b_{d_A})(a_{d_B}Y+b_{d_B}).$$
Expanding the right side: $a_{d_A}a_{d_B}XY+a_{d_A}b_{d_B}X+b_{d_A}a_{d_B}Y+b_{d_A}b_{d_B}$. Matching coefficients of the polynomial in $X,Y\in[0,1]$ (the identity holds for all such $X,Y$, so coefficients match):
- $XY$: $a_{d_Ad_B}=a_{d_A}a_{d_B}$;
- $X$: $0=a_{d_A}b_{d_B}$;
- $Y$: $0=b_{d_A}a_{d_B}$;
- const: $b_{d_Ad_B}=b_{d_A}b_{d_B}$.

If there exists one dimension $m$ with $a_m\neq0$, then $0=a_m b_n$ for every $n\geq2$, so $b_n=0$ for every $n$ and normalization gives $a_n=1$ for every $n$: case 1. Otherwise $a_n=0$ for every $n$, and normalization gives $b_n=1/n$: case 2. The two cases are mutually exclusive and both satisfy the coefficient identities. $\blacksquare$

**Remark.** The second branch is not classical probability. It is a completely depolarized, state-insensitive pairing: it ignores the alignment between the effect and the state. The theorem therefore needs no system-by-system non-triviality hypothesis.

### 6.3 Theorem 6.3: one pure self-certainty event

**Theorem 6.3.** Under the standing convention, let $d\geq 2$ and let $B$ be as in Theorem 6.1 (normalized restriction of a unitarily invariant real-bilinear form). Suppose there exists one rank-one projector $P$ such that
$$B(P,P)=1.$$
Then $B(E,\rho)=\mathrm{Tr}(E\rho)$.

*Proof.* A pure state is a rank-one projector $P$, which is both an effect and a normalized state. By Lemma 5.1, $B(P,P)=a\,\mathrm{Tr}(P^2)+b\,\mathrm{Tr}(P)^2=a\cdot 1+b\cdot 1=a+b$. The hypothesis $B(P,P)=1$ gives $a+b=1$. Combined with normalization $a+bd=1$:
$$a+b=a+\frac{1-a}{d}=\frac{a(d-1)+1}{d}=1\quad\Rightarrow\quad a(d-1)+1=d\quad\Rightarrow\quad a(d-1)=d-1.$$
Since $d\geq 2$, $a=1$, hence $b=0$. $\blacksquare$

**Remark.** Operationally: one pure state is certain about itself. Measuring the projector $P$ on the state $P$ must return "yes" with probability 1. This single diagonal event kills the entire $b$-family and is the exact on-diagonal analogue of Theorem 6.1's single off-diagonal zero. Note that $P$ must be admissible both as effect and as state; this is automatic for rank-one projectors in the standard setup.

### 6.4 Theorem 6.4: dimension-independence of pure transitions

**Definition (dimension-independence).** A family $\{B_d\}_{d\geq 2}$ is *dimension-independent on pure transitions* if, whenever two pure states $\psi,\phi$ of a $d_0$-dimensional system are embedded isometrically into $\mathbb C^d$ for any $d\geq d_0$ (as $\iota(\psi),\iota(\phi)$), the transition probability is independent of $d$:
$$B_d(\iota(\phi),\iota(\psi))=B_{d_0}(\phi,\psi).$$

**Theorem 6.4.** Under the standing convention, let $\{B_d\}_{d\geq 2}$ be a family of normalized restrictions of unitarily invariant real-bilinear forms. If the family is dimension-independent on pure transitions, then $a_d=1$ and $B_d=\mathrm{Tr}(E\rho)$ for every $d\geq 2$.

*Proof.* Let $P,Q$ be rank-one projectors in $\mathbb C^2$ with $\mathrm{Tr}(PQ)=x\in[0,1]$. Embed them into $\mathbb C^d$ for any $d\geq 2$. Then
$$B_d(Q,P)=a_d\,x+b_d\cdot 1\cdot 1=a_d\,x+\frac{1-a_d}{d}.$$
Dimension-independence requires that $a_d\,x+(1-a_d)/d$ is independent of $d$ for all $x\in[0,1]$ and all $d\geq 2$. Taking two values of $x$ (e.g. $x=0$ and $x=1$):
- $x=0$: $(1-a_d)/d = c_0$ (constant in $d$);
- $x=1$: $a_d+(1-a_d)/d = c_1$ (constant in $d$).

Subtracting the two constant expressions gives $a_d=c_1-c_0$, independent of $d$. Hence $1-a_d=c_0d$ has a constant left-hand side and a right-hand side linear in every $d\geq2$. Thus $c_0=0$, so $a_d=1$ for all $d$. This proof uses normalization and dimension-independence only; it does not need the positivity interval. $\blacksquare$

**Remark.** This is a restricted restatement of Hossenfelder's dimension-independence argument [1], placed *after* the invariant bilinear classification. Hossenfelder works directly with continuous unitarily invariant transition probabilities $P_N$ on the complex unit sphere, assumes $N$-independence and basis consistency (which already includes $P=0$ on orthogonal pairs — our Theorem 6.1 — and $\sum_i P(\Psi\to e_i)=1$), and concludes $P=|\langle\Psi|\Phi\rangle|^2$. Our Theorem 6.4 isolates only the dimension-independence step inside the coarser bilinear class $B_{a,b}$, where the orthogonal-vanishing step is separated as Theorem 6.1. We include Theorem 6.4 for catalogue completeness and to make the relation to [1] explicit, not as an independent claim of priority.

### 6.5 Theorem 6.5: perfect distinguishability

**Definition (perfect distinguishability).** Two pure states $P,Q$ are *perfectly distinguishable* by an effect $E\in\mathrm{Eff}_d$ if $B(E,P)=1$ and $B(E,Q)=0$.

**Theorem 6.5.** Under the standing convention, let $d\geq 2$ and let $B$ be a normalized restriction of a unitarily invariant real-bilinear form as in Lemma 5.1, with $a\in[-1/(d-1),1]$. Suppose there exist pure states $P,Q$ and an effect $E$ such that $B(E,P)=1$ and $B(E,Q)=0$. Then:

1. $P$ and $Q$ are orthogonal;
2. if $d\geq 3$, necessarily $a=1$ (hence $B$ is Born);
3. if $d=2$, necessarily $a\in\{1,-1\}$; the anti-Born endpoint $a=-1$ (so $b=1$) satisfies distinguishability via $E=Q$, but is excluded by either local selector Theorem 6.1 or Theorem 6.3 (e.g. $B(P,P)=a+b=0\neq 1$), and is also incompatible with rank-one product monoidality because Theorem 6.2 permits only the Born and state-insensitive families.

*Proof.* Write $B(E,\rho)=a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)$ with $b=(1-a)/d$ and $\mathrm{Tr}\,\rho=1$. The two equations are
$$a\langle p|E|p\rangle+b\,\mathrm{Tr}(E)=1,\qquad a\langle q|E|q\rangle+b\,\mathrm{Tr}(E)=0.$$
Subtracting yields $a\bigl(\langle p|E|p\rangle-\langle q|E|q\rangle\bigr)=1$. For $0\leq E\leq I$ the difference of expectations on pure states lies in $[-1,1]$. Hence $|a|\geq 1$. Intersecting with the positivity interval $a\in[-1/(d-1),1]$:

- $a=1$ is always admissible; take $E=P$ when $PQ=0$: $B(P,P)=1$, $B(P,Q)=b=0$.
- $a=-1/(d-1)$ requires the difference of expectations to equal $1/a=-(d-1)$. This lies in $[-1,1]$ if and only if $d-1\leq 1$, i.e. $d=2$. For $d=2$, $a=-1$, $b=1$, and $E=Q$ works: $B(Q,P)=1$, $B(Q,Q)=0$.

For $d\geq 3$ the negative endpoint is therefore impossible under distinguishability, leaving only $a=1$. It remains to prove the orthogonality conclusion, which also covers the qubit endpoints. If $a=1$, then $b=0$, so the two exact-outcome equations give $\langle p|E|p\rangle=1$ and $\langle q|E|q\rangle=0$. Since $0\leq E\leq I$, positivity of $I-E$ and of $E$ implies $(I-E)|p\rangle=0$ and $E|q\rangle=0$. Thus $E|p\rangle=|p\rangle$, $E|q\rangle=0$, and $\langle p|q\rangle=\langle Ep|q\rangle=\langle p|Eq\rangle=0$. If $d=2$ and $a=-1$, then $b=1$; the same two equations force $\langle p|E|p\rangle=0$ and $\langle q|E|q\rangle=1$, hence $E|p\rangle=0$ and $E|q\rangle=|q\rangle$, again giving $\langle p|q\rangle=0$. For $d=2$ the residual anti-Born point $a=-1$ fails pure self-certainty ($B(P,P)=0\neq 1$) and fails the impossible-event condition in the Born direction ($B(P,Q)=1\neq 0$). $\blacksquare$

**Remark.** Theorem 6.5 is operationally natural: existence of a yes/no test that accepts one pure state with certainty and rejects another with certainty. Orthogonality is a conclusion, not an extra premise. For qutrits and higher this single requirement forces Born inside the bilinear class. The qubit retains a single exotic anti-Born bilinear pairing, killed by the local selectors of Theorems 6.1 and 6.3. This is a strengthening of the statement, not a priority claim.

**Remark (failure of pure-state bits).** Equivalently: for $d\geq 3$ and $a\in(-1/(d-1),1)$, *no* pair of pure states is perfectly distinguishable by any effect. The theory cannot encode a classical bit in a pair of pure states with a yes/no test. This is a sharp operational defect of the non-Born bilinear pairings, independent of bit symmetry in the sense of Galley–Masanes [3] (which concerns reversible maps between distinguishable pairs). Here the defect is more primitive: the distinguishable pairs do not exist at all.

### 6.6 Proposition 6.6: unbounded ancilla stability classifies stable families

Let $\{B_m\}_{m\geq2}$ be a family of positive normalized pairings in the classified form, with $b_m=(1-a_m)/m$. Assume **unbounded idle-ancilla stability**:
$$B_{dk}(E\otimes I_k,\rho\otimes\sigma)=B_d(E,\rho)$$
for every $d,k\geq2$, every effect $E$, and all normalized states $\rho,\sigma$. Then there is one constant $c\in[0,1]$ such that $a_d=c$ for every $d\geq2$.

*Proof.* The left-hand side expands to
$$a_{dk}\,\mathrm{Tr}(E\rho)+\frac{1-a_{dk}}{d}\,\mathrm{Tr}(E).$$
Equality with the right-hand side for all $E,\rho$ forces $a_{dk}=a_d$. Reversing the roles of $d$ and $k$ gives $a_{dk}=a_k$, hence $a_d=a_k$ for every $d,k\geq2$. Write this common value as $c$. Positivity in dimension $m$ gives $c\in[-1/(m-1),1]$ for every $m\geq2$. Letting $m\to\infty$ yields $c\in[0,1]$. $\blacksquare$

**Sharpness.** This is not a Born selector. For every fixed $c\in[0,1]$, the family $a_m=c$, $b_m=(1-c)/m$ is positive, normalized, and idle-ancilla stable in all dimensions. Thus Proposition 6.6 exactly classifies the stable families and leaves a full non-Born interval $0\leq c<1$.

### 6.7 Corollary 6.7: stable one-bit selector

Let $\{B_d\}_{d\geq2}$ satisfy the hypotheses of Proposition 6.6. Suppose additionally that in one dimension $d_\ast\geq2$ there exist pure states $P,Q$ and an effect $E$ with
$$B_{d_\ast}(E,P)=1,\qquad B_{d_\ast}(E,Q)=0.$$
Then $a_d=1$ and hence $B_d(E,\rho)=\mathrm{Tr}(E\rho)$ for every $d\geq2$.

*Proof.* Proposition 6.6 gives one constant $a_d=c\in[0,1]$ in every dimension. If $d_\ast\geq3$, Theorem 6.5 applied to the stipulated perfect bit gives $c=a_{d_\ast}=1$. If $d_\ast=2$, Theorem 6.5 gives $c=a_2\in\{1,-1\}$, while Proposition 6.6 gives $c\geq0$; therefore again $c=1$. Thus $a_d=1$ in every dimension, and normalization gives $b_d=0$. $\blacksquare$

**Remark.** This corollary does not escape the Hermitian bilinear setup. Its content is that unbounded stability turns a single perfect bit into a global selector by synchronizing all dimensions. We make no priority claim.

### 6.8 Proposition 6.8: equivalence of the local selectors

**Proposition 6.8 (local selector equivalence).** Assume Lemma 5.1 and normalization $a+bd=1$ for $d\geq 2$. The following are equivalent:

1. there exist orthogonal rank-one projectors $P,Q$ with $B(Q,P)=0$ (hypothesis of Theorem 6.1);
2. there exists a rank-one projector $P$ with $B(P,P)=1$ (hypothesis of Theorem 6.3);
3. $b=0$;
4. $a=1$;
5. $B(E,\rho)=\mathrm{Tr}(E\rho)$ for all effects and normalized states.

*Proof.* Under the classification, $B(Q,P)=b$ for any orthogonal rank-one pair and $B(P,P)=a+b$ for any rank-one $P$. Normalization gives $b=(1-a)/d$. Thus (1)$\Leftrightarrow b=0\Leftrightarrow a=1\Leftrightarrow a+b=1\Leftrightarrow$(2)$\Leftrightarrow$(5). $\blacksquare$

**Corollary.** Theorems 6.1 and 6.3 are two operational readings of the *same* algebraic condition $b=0$. One is a single off-diagonal vanishing (impossible event); the other is a single on-diagonal certainty (pure self-prediction). They are not independent axioms once bilinearity, unitary invariance, and normalization are granted.

Theorem 6.4 and the $d\geq3$ branch of Theorem 6.5 are independent routes to Born; Theorem 6.2 instead yields Born after an additional condition excludes its state-insensitive branch. Monoidality uses the tensor product structure of a family $\{B_d\}$; dimension-independence uses embeddings across dimensions; distinguishability uses the existence of a perfect yes/no test. Local selectors (Theorems 6.1 and 6.3) use only a single system and are mutually equivalent.

### 6.9 Status of the selectors

Lemma 5.1 is conditional on the standard irreducibility/commutant input stated in Section 5.2. Conditional on Lemma 5.1, the selectors are elementary coefficient eliminations.

| Selector | Operational content | Forces | Relation | Prior art |
|----------|---------------------|--------|----------|-----------|
| Thm. 6.1: one impossible event | $B(Q,P)=0$ for one orthogonal pair | $b=0$ | $\Leftrightarrow$ Thm. 6.3 (Prop. 6.8) | no priority claim |
| Thm. 6.3: one pure self-certainty event | $B(P,P)=1$ for one pure $P$ | $a=1$ | $\Leftrightarrow$ Thm. 6.1 (Prop. 6.8) | no priority claim |
| Thm. 6.2: rank-one monoidality | product probabilities factor | Born or state-insensitive family | global dichotomy | no priority claim |
| Thm. 6.4: dim-independence | pure transitions ignore ambient $d$ | $a_d=1$ | independent route | Hossenfelder [1] (stronger setting) |
| Thm. 6.5: perfect distinguishability | exists $E$ with $B(E,P)=1$, $B(E,Q)=0$ | $a=1$ ($d\geq 3$); $a\in\{1,-1\}$ ($d=2$) | independent; $d=2$ needs Thm. 6.1/6.3 | no priority claim |
| Prop. 6.6: unbounded ancilla stability | idle ancilla irrelevant in every extension | $a_d=c\in[0,1]$ | classifies stable families; not Born selector | no priority claim |
| Cor. 6.7: stable one bit | Prop. 6.6 plus one exact pure bit in any dimension | $a_d=1$ for all $d$ | direct consequence of Prop. 6.6 and Thm. 6.5 | no priority claim |

Theorems 6.1, 6.3, and 6.5 are recorded here as elementary conditional selectors within the invariant bilinear class. We make no priority claim for them: results of this simplicity may already occur as remarks or exercises. Theorem 6.4 is a restricted restatement of the dimension-independence idea of Hossenfelder [1], who works directly with continuous unitarily invariant transition probabilities on the complex sphere (a stronger setup than the bilinear class).

Within the already-classified invariant bilinear class, the orthogonal-support condition (Theorem 6.1) is substantially narrower than full Gleason additivity: Gleason requires additivity over arbitrary orthogonal decompositions, while Theorem 6.1 requires only vanishing on a single orthogonal projector pair (extended to all such pairs by invariance). We do not claim a global ordering of axiom strength between the two frameworks, which operate under different background assumptions.

---

## 7. Limits and discussion

### 7.1 Examples outside the scope

The following familiar theories are not countermodels to the selector theorems: they fail the complex-Hermitian ambient assumptions before any selector is applied.

- **Classical probability:** simplex state spaces do not furnish the full complex-Hermitian state/effect space with simultaneous $U(d)$ conjugation.
- **Real-vector-space QM [13]:** its state/effect spaces are real symmetric matrices rather than $\mathrm{Herm}_d(\mathbb C)$; its failure of local tomography is a separate reconstruction-level distinction.
- **Quaternionic QM:** it has a different scalar field and composite structure, not the assumed complex-Hermitian ambient space.
- **Boxworld [14]:** its local gbit has a polyhedral square state space rather than a PSD cone of complex Hermitian matrices.

These are exclusions by the *setup*, not by the selectors alone. Purification and local tomography matter for broader OPT reconstruction programs, not as hypotheses of Lemma 5.1 or the selector results here.

### 7.2 What is genuinely here

- Lemma 3.1: Gram map classification for rectangular amplitudes. Procesi [11] provides related polynomial invariant theory, but does not directly subsume this continuous, positive, $GL(d)\times U(r)$-equivariant statement.
- Proposition 4.1: standard quotient geometry [12].
- Lemma 5.1: conditional classification of invariant bilinear pairings via the explicit representation-theoretic input in Section 5.2.
- **Theorems 6.1--6.5, Proposition 6.6, and Corollary 6.7:** scoped selectors within the invariant bilinear class; Theorems 6.1 and 6.3 are equivalent (Proposition 6.8); Theorem 6.2 has an exact Born/state-insensitive dichotomy; Theorem 6.5 is the distinguishability selector ($d\geq 3$ forces Born alone); Proposition 6.6 and Corollary 6.7 are direct cross-dimensional consequences.
- Theorem 6.4: dimension-independence step isolated from Hossenfelder [1].
- Exact classification under unbounded idle-ancilla stability: it synchronizes the family but needs one perfect bit to select Born (Section 6.6--6.7).
- Honest supersession of Conjecture 1 as a Born-route by Nakahira [2] (Section 8); residual open Problem A (amplitude representations of OPTs).

### 7.3 Relation to Gleason

Gleason [5] derives the Born probability rule from noncontextual additive measures on projectors ($d\geq 3$); Busch [6] extends to POVMs including $d=2$. Lemma 3.1 is complementary (state-formation map vs probability rule). Theorem 6.1 is a *different selector within a different framework*: after the invariant bilinear classification, a single vanishing condition selects Born. We do not claim Theorem 6.1 subsumes Gleason or is globally "weaker"; only that within the classified class, it is a narrower additional requirement.

### 7.4 The circularity boundary

Theorems 6.1, 6.3, and 6.4 select Born *given* the Hermitian structure of states and effects, the unitary invariance, and the bilinear setup; Theorem 6.5 does so for $d\geq3$, while Theorem 6.2 is a Born/state-insensitive dichotomy. None derives these structures. The circularity is the same as Lemma 3.1: a uniqueness result within an assumed geometry.

### 7.5 Positioning relative to Galley–Masanes

Galley and Masanes [3] keep pure states as rays and unitary dynamics, and classify *all* finite-parameter alternatives to the measurement postulates. That landscape is large: non-Born theories exist, and unrestricted ones violate bit symmetry. The present paper studies only the **bilinear mixed-state extension** of outcome probabilities — the class containing the standard Born pairing $\mathrm{Tr}(E\rho)$ as a bilinear form on effects and states. Lemma 5.1 collapses that class to $B_{a,b}$; the stated selector conditions identify the Born pairing under their respective additional hypotheses. We do not claim to classify general alternatives to Born, nor to improve on [3]. The contribution is a clean conditional-result catalogue *inside* the bilinear slice, with explicit comparisons to Hossenfelder [1], Gleason [5], and Nakahira [2].

---

## 8. Confronting Conjecture 1 with Nakahira

**Conjecture 1 (informal, original form).** In a finite-dimensional causal operational theory admitting purification, with ancillary stability and a suitable noncontextuality condition, the state-formation map from amplitudes to states is forced to be congruence-covariant and gauge-invariant, and hence (by Lemma 3.1) of the Gram form.

Nakahira [2] (arXiv:2605.23217, May 2026) proves a stronger reconstruction theorem that must be confronted honestly.

### 8.1 What Nakahira proves

In a finite-dimensional causal OPT, two postulates suffice:

1. **Local equivalence:** channels are completely identified by local input-output statistics (equivalent to local discriminability).
2. **ES purification:** every state of system $A$ is the marginal of a pure state on $A\tilde A$ with $\tilde A$ *equivalent* to $A$, and any two such purifications are related by a reversible channel on $\tilde A$.

**Theorem (Nakahira).** Under these two postulates the theory *is* standard finite-dimensional complex quantum theory: each system has a finite-dimensional complex Hilbert space; states are exactly all density matrices; measurements are exactly POVMs; composites are tensor products; channels are exactly CPTP maps; the Born rule holds; measurement no-restriction is *derived*.

Neither postulate alone suffices: classical theory has local equivalence but not ES purification; real quantum theory has ES purification but not local equivalence (Nakahira Table I).

### 8.2 What this does to Conjecture 1

Nakahira does **not** construct the amplitude space $M_{d\times r}(\mathbb C)$ or the $GL(d,\mathbb C)\times U(r)$ bimodule. He constructs Hilbert spaces, density matrices, and the Born pairing $\mathrm{Tr}(E\rho)$ directly.

Consequences for our programme:

1. **Born itself is no longer an open reconstruction target at the OPT level.** If Nakahira's theorem is accepted, the Born rule is already forced by local equivalence + ES purification. Our result catalogue lives one level *down*: Theorems 6.1, 6.3, and 6.4 select Born inside the already Hermitian bilinear class, Theorem 6.5 does so above the qubit case, and Theorem 6.2 is a dichotomy. The results remain valid mathematics, but they are not a competing derivation of Born from operational first principles.

2. **The amplitude/bimodule question is a representation question, not a reconstruction question.** Once Hilbert space is given, every density matrix of rank $\leq r$ admits a Gram factorization $\rho=WW^\dagger$ with $W\in M_{d\times r}(\mathbb C)$, unique up to right $U(r)$ (Proposition 4.1). Congruence covariance under invertible filters is the standard conjugation action. Lemma 3.1 then says: if one *starts* from complex amplitudes and imposes gauge + congruence + positivity + continuity, the only state-formation map is the Gram map. That is a classification *inside* the complex amplitude representation, not a derivation *of* that representation.

3. **Revised open problem (replaces Conjecture 1).**  
   **Problem A.** Characterize which OPTs admit an *amplitude representation*: a functor assigning to each system a space $M_{d\times r}$ with a $GL(d)\times U(r)$ action whose quotient recovers the state space.  
   **Problem B.** Among theories that already have Hilbert-space structure (e.g. by Nakahira), is the Gram representation of mixed states forced by any additional operational principle beyond Stinespring/purification uniqueness, or is it merely a convenient coordinate system?  
   We do not resolve Problem B here. Standard Stinespring/Kraus theory supplies dilations once Hilbert-space quantum theory is assumed, but does not by itself establish the requested operational uniqueness claim. The non-trivial direction is Problem A.

4. **What remains of our circularity boundary.** Lemma 3.1 and the bilinear-pairing result catalogue never claim to derive the Hermitian structure. Nakahira derives that structure from OPT postulates. The two results sit at different layers:
   - Nakahira: OPT postulates $\to$ complex QM package (including Born);
   - This paper: classified Hermitian bilinear invariant pairings $\to$ Born under the stated selector conditions; and complex amplitudes + congruence $\to$ Gram map.

### 8.3 Honest status

Conjecture 1 in its original form is **superseded** as a route to Born: Nakahira already gets Born (and everything else) without amplitudes. The residual mathematical content of Lemma 3.1 is a clean classification of congruence-covariant continuous positive maps on amplitude matrices — valuable as linear algebra / invariant theory, not as a foundational derivation of quantum probability. We keep Lemma 3.1 as scaffolding and reframe the open direction as Problem A above.

---

## 9. Outlook

The open amplitude-representation programme requires a genuinely operational definition of the relevant interface and of its admissible reversible gauge transformations. Hidden-interface fibres from discarding a system and observational fibres from restricted tests are possible ingredients, but this manuscript proves no unifying principle about them. We therefore leave this only as an outlook; it is not used by any result above.

---

## Acknowledgements

The author used generative AI systems for conceptual exploration, drafting, structural editing, and preliminary mathematical analysis. The author reviewed and takes responsibility for the final manuscript.

---

## References

[1] S. Hossenfelder, "A derivation of Born's rule from symmetry," *Ann. Phys.* **425**, 168394 (2021). arXiv:2006.14175.

[2] K. Nakahira, "Two operational principles single out quantum theory," arXiv:2605.23217 (2026, preprint).

[3] T. D. Galley and L. Masanes, "Classification of all alternatives to the Born rule in terms of informational properties," *Quantum* **1**, 15 (2017). arXiv:1610.04859. doi:10.22331/q-2017-07-14-15.

[4] A. Lax, "The Born Rule for Projective Measurements from Metric Non-Expansion and Calibration," arXiv:2604.27339 (2026, updated 2026-07-23).

[5] A. Gleason, "Measures on the closed subspaces of a Hilbert space," *J. Math. Mech.* **6**, 885-893 (1957).

[6] P. Busch, "Quantum states and generalized observables: A simple proof of Gleason's theorem," *Phys. Rev. Lett.* **91**, 120403 (2003). arXiv:quant-ph/9909073.

[7] G. Chiribella, G. M. D'Ariano, and P. Perinotti, "Informational derivation of quantum theory," *Phys. Rev. A* **84**, 012311 (2011). arXiv:1011.6451.

[8] H. Barnum and A. Wilce, "Local tomography and the Jordan structure of quantum theory," *Found. Phys.* **44**, 946-979 (2014). arXiv:1202.4513.

[9] S. Tull, "A categorical reconstruction of quantum theory," *Log. Methods Comput. Sci.* **16**, 1 (2020). arXiv:1804.02265.

[10] J. H. Selby, C. M. Scandolo, and B. Coecke, "Reconstructing quantum theory from diagrammatic postulates," arXiv:1802.00367 (2018).

[11] C. Procesi, "Tensor fundamental theorems of invariant theory," arXiv:2011.10820 (2020).

[12] E. Massart and P.-A. Absil, "Quotient geometry with simple geodesics for the manifold of fixed-rank positive-semidefinite matrices," *SIAM J. Matrix Anal. Appl.* **41**(1), 171-198 (2020).

[13] L. Hardy and W. K. Wootters, "Limited holism and real-vector-space quantum theory," *Found. Phys.* **42**, 454-471 (2012). arXiv:1005.4870.

[14] J. Barrett, "Information processing in generalized probabilistic theories," *Phys. Rev. A* **75**, 032304 (2007). arXiv:quant-ph/0508211.

[15] W. Fulton and J. Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129, Springer (1991).

---

*End of manuscript.*
