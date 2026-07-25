# Problem A — Amplitude representations of OPTs (formal sketch)

**Status:** open problem statement, not a theorem  
**Date:** 2026-07-24  
**Context:** After Nakahira, Born is derived at OPT level. Amplitude geometry is a *representation* question.

## Definition (draft)

An **amplitude representation** of a finite-dimensional causal OPT $\mathcal T$ assigns to each system $A$:

1. integers $d_A \geq 1$, $r_A \geq 1$;
2. a set $W_A \subseteq M_{d_A \times r_A}(\mathbb K)$ with $\mathbb K \in \{\mathbb R,\mathbb C,\mathbb H\}$;
3. a right action of a compact group $G_A$ (intended: $U(r_A)$ or analogue) on $W_A$ by right multiplication;
4. a left action of a group $H_A$ (intended: $GL(d_A,\mathbb K)$ or the reversible-filter group of $A$) by left multiplication;
5. a continuous map $q_A: W_A \to \mathrm{St}_+(A)$ (unnormalized states) that is:
   - constant on $G_A$-orbits (gauge),
   - equivariant under $H_A$ in the sense that filters act as the operational filter group on states,
   - surjective onto the interior of the state cone (or onto all states of rank $\leq r_A$).

The representation is **Gram-like** if $q_A(W)=c\,WW^\dagger$ (or the $\mathbb K$-appropriate Gram form).

## Questions

1. **Existence.** Which OPTs admit an amplitude representation over $\mathbb C$? Over $\mathbb R$? Over $\mathbb H$?
2. **Uniqueness of field.** Can local equivalence + ES purification (Nakahira) be rephrased as: the only field admitting an amplitude representation compatible with both postulates is $\mathbb C$?
3. **Functoriality.** Does the assignment $A \mapsto W_A$ extend to channels (Stinespring-style)?
4. **No-go samples.**
   - Classical probability: no non-trivial purification $\Rightarrow$ no ES-style amplitude lift.
   - Real QM: admits real amplitudes; fails local equivalence (Nakahira Table I).
   - Boxworld: no purification in the strong sense $\Rightarrow$ no amplitude representation of Gram type.

## Partial observation (not a theorem)

If $\mathcal T$ is already standard complex QM, then the standard purification/Kraus data supply a Gram-like amplitude representation, and Lemma 1 of `paper_born.md` says this $q$ is the unique continuous positive gauge-invariant congruence-covariant choice. So existence is free *after* quantum theory; the hard direction is existence *before* quantum theory.

## Why this is the right residual problem

Nakahira: OPT $\to$ QM.  
Lemma 1: amplitudes+symmetry $\to$ Gram.  
Problem A: OPT $\to$ amplitudes (possibly equivalent to OPT $\to$ QM).

If Problem A is equivalent in strength to Nakahira's theorem, it is not a shortcut. If it is strictly weaker or yields intermediate theories, it is interesting. Either answer is a result.

## Next attack (future session)

1. Formalize OPT axioms used (match Nakahira appendix A).
2. Show that an amplitude representation over $\mathbb C$ with full $H_A=GL(d)$ left action + local tomography forces complex Jordan structure / self-duality.
3. Or find a non-quantum OPT with a weird amplitude representation (counterexample to "amplitudes $\Rightarrow$ QM").
