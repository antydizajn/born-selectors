# Theorem Ledger — Born / Amplitude Program

**Date:** 2026-07-24
**Purpose:** single source of truth for verification status. This ledger overrides any stronger status language in earlier notes.

## Status vocabulary

- **PROVED:** proof in local Markdown has been adversarially repaired; the corresponding script tests the relevant finite-dimensional algebraic identities.
- **CONDITIONAL:** conclusion follows only with explicitly named extra assumptions.
- **STANDARD-FACT DEPENDENT:** local derivation reduces to a known representation-theory fact not source-verified in this session.
- **EXPLORATORY / WITHDRAWN:** not evidence; must not appear in a public claim.

---

## A. Complex Cone Rigidity

**File:** `PROBLEM_A_THEOREM.md`

**Claim:** Let $C\subseteq\mathrm{Herm}_d$ be proper, closed, convex, full-dimensional, $GL(d,\mathbb C)$-congruence invariant, and contain a rank-one PSD matrix. Then $C=\mathrm{PSD}_d$.

**Status:** **PROVED** (finite-dimensional linear algebra).

**Proof dependencies:**
1. Sylvester law of inertia for Hermitian forms under complex congruence.
2. Closed convex hull of rank-one PSD matrices is $\mathrm{PSD}_d$.
3. Pointedness of a proper cone.

**Repair applied:** Step 4 now treats both signatures with positive and negative directions and the previously omitted negative-semidefinite branch $p=0$. Each branch uses only a limit of invertible congruences, never a singular transform.

**Verification:** `python3 WORKSPACE/fizyka/verify_cone_rigidity.py` tests both Step-4 branches for $d=2,3,4,5,6`.

**Scope:** classification inside an assumed $\mathrm{Herm}_d$ ambient with full congruence. It does **not** derive that ambient or congruence action from OPT axioms.

---

## B. Real Cone Rigidity

**File:** `REAL_CONE_RIGIDITY.md`

**Claim:** The real analogue holds on $\mathrm{Sym}_d(\mathbb R)$ under $GL(d,\mathbb R)$ congruence: a proper closed convex invariant cone containing rank-one real PSD is $\mathrm{PSD}_d^{\mathbb R}$.

**Status:** **PROVED** (same Sylvester/closure proof, including both Step-4 branches).

**Verification:** `python3 WORKSPACE/fizyka/verify_real_cone_rigidity.py`.

---

## C. Complex composite compatibility

**File:** `COMPOSITE_RIGIDITY.md`

**Claim:** If $A,B,AB$ each satisfy the complex Cone Rigidity hypotheses, the OPT is **locally tomographic**, and the standard Kronecker Gram realization is monoidal, then $d_{AB}=d_A d_B$ and the composite cone is $\mathrm{PSD}_{d_A d_B}$.

**Status:** **CONDITIONAL.**

**Valid dimension proof:** $\dim_\mathbb R\mathrm{Herm}_d=d^2$ and local tomography give
$$d_{AB}^2=d_A^2d_B^2,$$
hence $d_{AB}=d_A d_B$.

**Explicitly withdrawn claim:** a bare linear injection
$$M_{d_A\times r_A}\otimes M_{d_B\times r_B}\hookrightarrow M_{d_{AB}\times r_{AB}}$$
does **not** imply $d_{AB}\ge d_A d_B$; it only constrains the product $d_{AB}r_{AB}$. The previous "minimal dimension from embedding" proof was invalid.

**Explicitly withdrawn terminology:** $d_{AB}>d_A d_B$ was wrongly called "superselection-enlarged." Such a model is merely a non-locally-tomographic extension unless further operational structure is supplied.

**Verification:** `python3 WORKSPACE/fizyka/verify_composite_rigidity.py` verifies Kronecker monoidality and the conditional dimension identity; it does not prove local tomography.

---

## D. Real composite obstruction

**File:** `REAL_CONE_RIGIDITY.md`

**Claim:** Standard real quantum theory is not locally tomographic for two nontrivial systems.

**Status:** **PROVED.**

For $m=d_A,n=d_B$:
$$\dim\mathrm{Sym}_{mn}(\mathbb R)=\frac{mn(mn+1)}2,$$
while products of local effects have dimension
$$\frac{m(m+1)}2\frac{n(n+1)}2.$$
Equality holds iff $(m-1)(n-1)=0$. Thus two rebits give $10\ne9$.

**Consequent correction:** there is no "Real Composite Rigidity" theorem in this work. The real Kronecker Gram identity is true but does not restore local tomography.

---

## E. Complex bilinear selector family

**File:** `paper_born.md`

**Claim:** Under the explicitly stated complex Hermitian/bilinear/unitary-invariance assumptions, $B_{a,b}(E,\rho)=a\operatorname{Tr}(E\rho)+b\operatorname{Tr}(E)\operatorname{Tr}(\rho)$ and listed selectors pick Born inside that family.

**Status:** **STANDARD-FACT DEPENDENT / scoped.** The representation-theoretic decomposition is standard; this ledger does not elevate it into a global derivation of Born.

**v5.2 refinement:** Theorem 6.5 now assumes only exact binary discrimination of two pure states by one effect; it derives their orthogonality from the equality cases of $0\leq E\leq I$. For $d\geq3$ it still forces $a=1$; for $d=2$ the anti-Born endpoint remains. This is a strengthened scoped corollary, not a priority claim.

**v5.11 refinement:** Proposition 6.6 adds unbounded idle-ancilla stability for a positive normalized dimension-indexed family. Using both orderings of the stability law, it proves $a_d=a_{dk}=a_k$, hence $a_d=c\in[0,1]$ is one dimension-independent constant. It classifies stable families but does not select Born: constant families $a_m=c\in[0,1)$ remain countermodels. Corollary 6.7 requires one exact pure bit in any single dimension; with Proposition 6.6 plus Theorem 6.5 it selects $c=1$ globally. Theorem 6.2 is an exact Born/state-insensitive dichotomy, not an unconditional Born selector. Theorem 6.3 needs only one diagonal certainty event, symmetric to Theorem 6.1's one off-diagonal zero. Theorem 6.4 no longer depends on positivity. All manuscript-wide summary and discussion language now preserves these distinct scopes. All remain scoped and carry no priority claim.

---

## F. Real bilinear selector family

**File:** `REAL_PAIRINGS.md`

**Claim:** The $O(d)$-invariant bilinear family on $\mathrm{Sym}_d(\mathbb R)$ is the same two-parameter family $B_{a,b}$.

**Status:** **STANDARD-FACT DEPENDENT.** The local proof reduces it to irreducibility of traceless symmetric tensors under $O(d)$ and Schur's lemma. Thm 1's orthogonal-rank-one selector is explicitly verified; broad claims that all five selectors transfer need line-by-line proof before publication.

---

## G. Quaternionic material

**File:** `QUATERNIONIC_PAIRINGS.md`

**Status:** **EXPLORATORY / WITHDRAWN FROM PROMOTION.**

The draft's complex realization conventions, trace normalization, highest-weight statement, and numerical group sampler were not source-verified. No public theorem claim is authorized from this file. It remains a research notebook for a future source-first treatment.

---

## Publication rule

A public artifact may use only claims marked **PROVED** or **CONDITIONAL** with their conditions written in the theorem statement. It must not say "derivation of the Born rule," "field trio complete," "Conjecture 1 settled," or "superselection-enlarged" on the basis of these notes.
