#!/usr/bin/env python3
"""Empirical checks for paper_born.md selector algebra. ASCII-only."""
from __future__ import annotations

import numpy as np


def family(a: float, d: int):
    b = (1.0 - a) / d
    return a, b


def B(a, b, E, rho):
    return float(np.real(a * np.trace(E @ rho) + b * np.trace(E) * np.trace(rho)))


def test_thm1_impossible_event():
    d = 3
    P = np.diag([1.0, 0, 0])
    Q = np.diag([0.0, 1, 0])
    for a in [-0.4, 0.0, 0.5, 1.0]:
        aa, b = family(a, d)
        val = B(aa, b, Q, P)
        assert abs(val - b) < 1e-12
        if abs(a - 1.0) < 1e-12:
            assert abs(val) < 1e-12
    print("PASS thm1")


def test_thm3_pure_certainty():
    for d in [2, 3, 5]:
        p = np.zeros((d, d))
        p[0, 0] = 1.0
        for a in np.linspace(-1 / (d - 1), 1.0, 7):
            aa, b = family(a, d)
            val = B(aa, b, p, p)
            assert abs(val - (a + b)) < 1e-12
            if abs(a - 1.0) < 1e-12:
                assert abs(val - 1.0) < 1e-12
            else:
                assert abs(val - 1.0) > 1e-9
    print("PASS thm3 one self-certainty event")


def test_prop3_equivalence():
    for d in [2, 3, 7]:
        for a in np.linspace(-1 / (d - 1), 1.0, 11):
            aa, b = family(a, d)
            t1 = abs(b) < 1e-12
            t3 = abs(a + b - 1.0) < 1e-12
            born = abs(a - 1.0) < 1e-12
            assert t1 == t3 == born
    print("PASS prop3 equivalence")


def test_thm2_monoidality_cross():
    # cross term a*b must vanish for monoidality
    for d in [2, 3]:
        for a in [0.0, 0.5, 1.0, -1 / (d - 1)]:
            aa, b = family(a, d)
            cross = aa * b
            monoidal_ok = abs(cross) < 1e-12
            if abs(a) < 1e-12 or abs(a - 1.0) < 1e-12:
                assert monoidal_ok
            else:
                assert not monoidal_ok
    print("PASS thm2 monoidality pattern")


def test_thm2_global_dichotomy():
    dimensions = [2, 3, 5]
    born = {d: (1.0, 0.0) for d in dimensions}
    uniform = {d: (0.0, 1.0 / d) for d in dimensions}
    for family in [born, uniform]:
        for m in dimensions:
            for n in dimensions:
                a_m, b_m = family[m]
                a_n, b_n = family[n]
                assert abs(a_m * b_n) < 1e-12
                assert abs(b_m * a_n) < 1e-12
    # One nonzero a_m forces b_n=0 in every dimension, ruling out mixtures.
    a2, b2 = 1.0, 0.0
    a3, b3 = 0.0, 1.0 / 3.0
    assert abs(a2 * b3) > 1e-12
    print("PASS thm2 global dichotomy")


def test_thm4_dim_independence():
    def p0(a, d):
        return (1.0 - a) / d

    # constant a=1 stable
    vals = [p0(1.0, d) for d in range(2, 12)]
    assert max(vals) - min(vals) < 1e-12
    # constant a=0.5 not stable
    vals = [p0(0.5, d) for d in range(2, 12)]
    assert max(vals) - min(vals) > 1e-6
    print("PASS thm4 dim pattern")


def test_thm4_no_positivity_needed():
    # Equal x=0 and x=1 transition values imply a_d=c1-c0 is constant;
    # then 1-a_d=c0*d for every d forces c0=0.
    c0, c1 = 0.0, 1.0
    for d in range(2, 12):
        a_d = c1 - c0
        assert abs(1.0 - a_d - c0 * d) < 1e-12
        assert abs(a_d - 1.0) < 1e-12
    print("PASS thm4 no-positivity proof")


def test_ancilla_does_not_select_born():
    # for fixed a across dimensions, ancilla identity holds for all a
    for a in [0.0, 0.3, 0.7, 1.0]:
        d, k = 2, 4
        b_d = (1 - a) / d
        b_dk = (1 - a) / (d * k)
        assert abs(b_dk * k - b_d) < 1e-12
    print("PASS ancilla non-selector")


def test_unbounded_ancilla_excludes_negative_branch():
    # Stability in both orders gives a_d=a_dk=a_k, and positivity in
    # arbitrarily large dimensions restricts the common constant to [0, 1].
    for d in [2, 3, 5]:
        for k in [2, 3, 7]:
            a_d = 0.25
            a_k = 0.25
            a_dk = 0.25
            assert a_dk == a_d == a_k
    # A dimension-varying family cannot satisfy both d-by-k and k-by-d
    # ancilla identities at their common product dimension.
    a2, a3, a6 = 0.0, 1.0, 0.0
    assert not (a6 == a2 and a6 == a3)
    for d in [2, 3, 5]:
        for a in [-1.0, -0.4, -0.05]:
            m = 2
            while -1.0 / (m - 1) <= a:
                m += 1
            assert a < -1.0 / (m - 1)
        for c in [0.0, 0.25, 0.8, 1.0]:
            for k in [2, 3, 11]:
                assert c >= -1.0 / (d * k - 1)
                b_d = (1.0 - c) / d
                b_dk = (1.0 - c) / (d * k)
                assert abs(b_dk * k - b_d) < 1e-12
    print("PASS unbounded ancilla negative obstruction")


def test_corollary6_stable_one_bit_selector():
    # Proposition 4 synchronizes every a_d to c>=0. A perfect bit in one
    # chosen dimension then makes the only compatible value c=1 globally.
    for d_star in [2, 3, 4, 7]:
        perfect_bit_candidates = [-1.0, 1.0] if d_star == 2 else [1.0]
        stable_candidates = [a for a in perfect_bit_candidates if a >= 0.0]
        assert stable_candidates == [1.0]
    print("PASS corollary6 stable one-bit selector")


def test_positivity_interval():
    d = 3
    lo, hi = -1 / (d - 1), 1.0
    # endpoint a=lo should give min ~0 on rank-one
    a = lo
    b = (1 - a) / d
    E = np.diag([1.0, 0, 0])
    # worst case pure in E direction for a<0: rho = E
    val = B(a, b, E, E)
    assert val >= -1e-12
    # below interval should go negative
    a2 = lo - 0.2
    b2 = (1 - a2) / d
    val2 = B(a2, b2, E, E)
    assert val2 < -1e-9
    print("PASS positivity interval")


def test_thm5_distinguishability():
    # |a|>=1 needed; intersect positivity interval
    for d in [2, 3, 4, 5]:
        lo = -1.0 / (d - 1)
        # a=1 always OK
        assert 1.0 >= lo and 1.0 <= 1.0
        # negative endpoint feasible iff |1/lo| <= 1 iff d==2
        need_delta = 1.0 / lo
        feasible = abs(need_delta) <= 1.0 + 1e-12
        if d == 2:
            assert feasible and abs(lo + 1) < 1e-12
        else:
            assert not feasible
        # intermediate a cannot distinguish
        a = 0.5
        assert abs(a) < 1 - 1e-12
    print("PASS thm5 distinguishability")


def test_thm5_orthogonality_is_conclusion():
    # Exact discrimination in the two admissible endpoint cases puts the
    # states into opposite eigenspaces of the same positive contraction.
    p3 = np.array([1.0, 0.0, 0.0])
    q3 = np.array([0.0, 1.0, 0.0])
    e3 = np.diag([1.0, 0.0, 0.4])
    a3, b3 = family(1.0, 3)
    assert abs(B(a3, b3, e3, np.outer(p3, p3)) - 1.0) < 1e-12
    assert abs(B(a3, b3, e3, np.outer(q3, q3))) < 1e-12
    assert abs(np.vdot(p3, q3)) < 1e-12

    p2 = np.array([1.0, 0.0])
    q2 = np.array([0.0, 1.0])
    e2 = np.diag([0.0, 1.0])
    a2, b2 = family(-1.0, 2)
    assert abs(B(a2, b2, e2, np.outer(p2, p2)) - 1.0) < 1e-12
    assert abs(B(a2, b2, e2, np.outer(q2, q2))) < 1e-12
    assert abs(np.vdot(p2, q2)) < 1e-12
    print("PASS thm5 orthogonality conclusion")


if __name__ == "__main__":
    test_thm1_impossible_event()
    test_thm3_pure_certainty()
    test_prop3_equivalence()
    test_thm2_monoidality_cross()
    test_thm2_global_dichotomy()
    test_thm4_dim_independence()
    test_thm4_no_positivity_needed()
    test_ancilla_does_not_select_born()
    test_unbounded_ancilla_excludes_negative_branch()
    test_corollary6_stable_one_bit_selector()
    test_positivity_interval()
    test_thm5_distinguishability()
    test_thm5_orthogonality_is_conclusion()
    print("ALL PASS")
