# Partial results toward Problem A

**Date:** 2026-07-24  
**Status:** partial / elementary — not the full Problem A

## Proposition A1 (classical obstruction)

Let $\mathcal C$ be finite classical probability theory (simplices as state spaces, deterministic extreme points, no purification of mixed states). Then $\mathcal C$ admits **no** Gram-like amplitude representation in the sense of `PROBLEM_A_amplitude_representations.md` with the ES-style requirement that every mixed state is $q(W)$ for some $W$ arising as a marginal of a pure amplitude on a composite.

*Reason.* ES purification fails classically (Nakahira Table I; standard). Any Gram-like lift $W\mapsto WW^\dagger$ on a composite produces purifications of mixed states. Hence no such representation exists.

## Proposition A2 (real QM admits real amplitudes, fails complex congruence) — with proof

Standard real quantum theory (states = real-symmetric density matrices on $\mathbb R^d$) admits a **real** Gram representation: every $\rho=\rho^T\succeq 0$ factors as $WW^T$ with $W\in M_{d\times r}(\mathbb R)$, unique up to $O(r)$ on the right.

It does **not** admit a complex amplitude representation whose left group contains full $GL(d,\mathbb C)$ acting by congruence while recovering only the real state space.

*Proof.* Let $\rho$ be real-symmetric, full rank, $\mathrm{Tr}\,\rho=1$. Take
$$M=\begin{pmatrix}1&i\\0&1\end{pmatrix}\oplus I_{d-2}\in GL(d,\mathbb C).$$
Then $\rho'=M\rho M^\dagger$ is Hermitian and positive, but
$$\rho'_{01}=\rho_{01}+i\rho_{11}$$
(up to the $2\times 2$ block computation), which is non-real whenever $\rho_{11}\neq 0$. Hence $\rho'$ is not real-symmetric. The $GL(d,\mathbb C)$-congruence orbit of a generic real state therefore exits the real state space. Any theory whose state space is exactly the real density matrices cannot carry the full complex congruence covariance of Lemma 1 in `paper_born.md`. $\square$

*Numeric check ($d=2$):* $\rho=\begin{pmatrix}0.7&0.1\\0.1&0.3\end{pmatrix}$, same $M$, yields $\mathrm{Im}(\rho'_{01})\approx 0.231\neq 0$.

## Proposition A2' (corollary for bilinear selectors)

The bilinear classification of Lemma 2 uses complex $\mathrm{Herm}_d$ and $U(d)$. The analogous classification on real-symmetric matrices with $O(d)$ yields a parallel family $a\,\mathrm{Tr}(E\rho)+b\,\mathrm{Tr}(E)\mathrm{Tr}(\rho)$ on real effects/states; the same selectors apply with $O(d)$ in place of $U(d)$. Real QM can host those real-bilinear selectors; it cannot host the complex congruence form of Lemma 1.

## Proposition A3 (quantum $\Rightarrow$ Gram amplitude representation)

If $\mathcal T$ is standard finite-dimensional complex QM, then the Kraus/purification data supply a Gram-like complex amplitude representation, and by Lemma 1 of `paper_born.md` this $q$ is the unique continuous positive right-$U(r)$-invariant left-$GL(d)$-equivariant choice.

*Proof.* Standard: any $\rho\succeq 0$ of rank $\leq r$ factors as $WW^\dagger$. Uniqueness of $q$ is Lemma 1. $\square$

## Corollary (location of difficulty)

Problems A1--A3 show:

- classical: no amplitude representation of ES/Gram type;
- real QM: real amplitudes yes, complex congruence no;
- complex QM: amplitudes yes and unique under Lemma 1 hypotheses.

The **open core of Problem A** is whether any *non-quantum* OPT admits a complex Gram-like amplitude representation with enough composition structure to be interesting — or whether amplitude+congruence+composition already force complex QM (making Problem A essentially equivalent to a reconstruction theorem).

## Proposition A4 (composition forces field constraints — heuristic)

Suppose systems $A,B$ have amplitude spaces $W_A,W_B$ over $\mathbb K$, and the composite has $W_{AB} \cong W_A \otimes W_B$ (Kronecker), with $q_{AB}(W_A\otimes W_B)=q_A(W_A)\otimes q_B(W_B)$ after normalization. Then for Gram-like $q(W)=WW^\dagger$ this holds over $\mathbb C$ and $\mathbb R$. Over exotic kernels without associative bilinear composition, Kronecker structure fails.

This is not yet a no-go for intermediate OPTs; it only says Gram monoidality is compatible with $\mathbb R$ and $\mathbb C$.

## What would count as a real theorem next

1. **Theorem candidate.** In a causal locally tomographic OPT with purification, existence of a complex amplitude representation with full left $GL(d,\mathbb C)$ action and monoidal $q$ implies the state spaces are complex quantum.  
   (If true: Problem A collapses to known reconstruction hypotheses.)

2. **Counterexample candidate.** A non-quantum OPT with a weird amplitude-like lift (e.g. restricted measurements on quantum states with a partial amplitude story).  
   (If found: Problem A is strictly weaker than full reconstruction.)

Until one of these is settled, Problem A remains open and correctly scoped.
