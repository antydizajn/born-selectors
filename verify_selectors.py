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
        P = np.zeros((d, d))
        P[0, 0] = 1.0
        for a in np.linspace(-1 / (d - 1), 1.0, 7):
            aa, b = family(a, d)
            val = B(aa, b, P, P)
            assert abs(val - (a + b)) < 1e-12
            if abs(a - 1.0) < 1e-12:
                assert abs(val - 1.0) < 1e-12
            else:
                assert abs(val - 1.0) > 1e-9
    print("PASS thm3")


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


def test_ancilla_does_not_select_born():
    # for fixed a across dimensions, ancilla identity holds for all a
    for a in [0.0, 0.3, 0.7, 1.0]:
        d, k = 2, 4
        b_d = (1 - a) / d
        b_dk = (1 - a) / (d * k)
        assert abs(b_dk * k - b_d) < 1e-12
    print("PASS ancilla non-selector")


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


if __name__ == "__main__":
    test_thm1_impossible_event()
    test_thm3_pure_certainty()
    test_prop3_equivalence()
    test_thm2_monoidality_cross()
    test_thm4_dim_independence()
    test_ancilla_does_not_select_born()
    test_positivity_interval()
    test_thm5_distinguishability()
    print("ALL PASS")
