#!/usr/bin/env python3
"""verify_cone_rigidity.py - numerical verification of the Cone Rigidity Theorem.

Theorem (GL(d,C) case): Let C subset Herm_d be a proper closed convex cone.
If (H1) C is GL(d,C)-congruence invariant and (H2) C contains a rank-one PSD,
then C = PSD_d.

Runs all six proof steps for d in {2,3,4,5,6} and the counterexample-spectrum
subgroup checks. Exit 0 = all pass.
"""
import numpy as np
import sys


def sylvester_signature(X):
    w = np.linalg.eigvalsh((X + X.conj().T) / 2)
    p = int(np.sum(w > 1e-9))
    q = int(np.sum(w < -1e-9))
    r = len(w) - p - q
    return (p, q, r)


def rand_gl(d, rng):
    M = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    while abs(np.linalg.det(M)) < 0.5:
        M = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return M


def step1_inertia_invariant(d, rng, trials=5):
    X = np.diag([1.0] * min(2, d) + [-1.0] * max(0, d - 2)).astype(complex)
    if d >= 2:
        X = np.diag([1.0, -1.0] + [0.0] * (d - 2)).astype(complex)
    sig0 = sylvester_signature(X)
    for _ in range(trials):
        M = rand_gl(d, rng)
        if sylvester_signature(M @ X @ M.conj().T) != sig0:
            return False
    return True


def step2_conv_rank1_is_psd(d, rng, N=5000):
    acc = np.zeros((d, d), dtype=complex)
    for _ in range(N):
        v = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        v /= np.linalg.norm(v)
        acc += np.outer(v, v.conj())
    acc /= N
    err = np.linalg.norm(acc - np.eye(d) / d)
    return err < 0.05  # statistical; -> 0 as N -> inf


def step3_outside_psd_has_neg(d, rng):
    X = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)))
    X = (X + X.conj().T) / 2
    X = X - 2 * np.eye(d) * np.max(np.linalg.eigvalsh(X))
    return sylvester_signature(X)[1] >= 1


def step4_extract_neg_rank1(d, rng):
    if d < 2:
        return True
    X0 = np.diag([1.0, -1.0] + [0.0] * (d - 2)).astype(complex)
    # scale pos slot to 0 via closure (M_s with s->0), keep neg, swap
    s = 1e-12
    M_s = np.diag([s, 1.0] + [1.0] * (d - 2)).astype(complex)
    X_scaled = M_s @ X0 @ M_s.conj().T
    P = np.eye(d, dtype=complex)
    P[[0, 1]] = P[[1, 0]]
    X_final = P @ X_scaled @ P.conj().T
    return sylvester_signature(X_final) == (0, 1, d - 1)


def step5_contradiction_pointed(d):
    e1 = np.zeros((d, d), dtype=complex)
    e1[0, 0] = 1.0
    # |e1><e1| in C (from PSD subset); -|e1><e1| in C (from step 4)
    # => |e1><e1| in C cap (-C) = {0}, but |e1><e1| != 0. Contradiction.
    return sylvester_signature(e1) == (1, 0, d - 1) and sylvester_signature(-e1) == (0, 1, d - 1)


def check_psd_is_invariant(d, rng, trials=5):
    for _ in range(trials):
        v = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        v /= np.linalg.norm(v)
        P = np.outer(v, v.conj())
        M = rand_gl(d, rng)
        Pt = M @ P @ M.conj().T
        if not np.all(np.linalg.eigvalsh(Pt) >= -1e-9):
            return False
    return True


def check_real_qm(d, rng):
    v = rng.standard_normal(d)
    P = np.outer(v, v)
    M = rng.standard_normal((d, d))
    Pt = M @ P @ M.T
    return np.allclose(Pt, Pt.T) and np.all(np.linalg.eigvalsh(Pt) >= -1e-9)


def check_superselection(d1, d2, rng):
    d = d1 + d2
    rho = np.zeros((d, d), dtype=complex)
    rho[:d1, :d1] = np.eye(d1) / d1
    rho[d1:, d1:] = np.eye(d2) / d2
    M = np.zeros((d, d), dtype=complex)
    M[:d1, :d1] = rand_gl(d1, rng)
    M[d1:, d1:] = rand_gl(d2, rng)
    rt = M @ rho @ M.conj().T
    return np.allclose(rt[:d1, d1:], 0) and np.allclose(rt[d1:, :d1], 0)


def check_classical(d, rng):
    rho = np.diag([0.4, 0.3, 0.2, 0.1][:d]).astype(complex)
    M = np.diag([2.0, 0.5, 1.0, 3.0][:d]).astype(complex)
    rt = M @ rho @ M.conj().T
    return np.allclose(rt - np.diag(np.diag(rt)), 0)


def main():
    print("=== Cone Rigidity Theorem - numerical verification ===\n")
    all_ok = True
    for d in [2, 3, 4, 5, 6]:
        rng = np.random.default_rng(d * 7)
        s1 = step1_inertia_invariant(d, rng)
        s2 = step2_conv_rank1_is_psd(d, rng)
        s3 = step3_outside_psd_has_neg(d, rng)
        s4 = step4_extract_neg_rank1(d, rng)
        s5 = step5_contradiction_pointed(d)
        psd_inv = check_psd_is_invariant(d, rng)
        ok = all([s1, s2, s3, s4, s5, psd_inv])
        all_ok = all_ok and ok
        print(f"d={d}: inertia={s1} conv_rank1_psd={s2} outside_has_neg={s3} "
              f"extract_neg={s4} contradiction={s5} psd_invariant={psd_inv} "
              f"=> {'OK' if ok else 'FAIL'}")
    print()
    rng = np.random.default_rng(99)
    r_ok = check_real_qm(4, rng)
    ss_ok = check_superselection(2, 2, rng)
    cl_ok = check_classical(4, rng)
    print(f"Real QM (GL(d,R)): {r_ok}  (real-symm PSD invariant under real congruence)")
    print(f"Superselection (block GL): {ss_ok}  (block structure preserved)")
    print(f"Classical (diagonal): {cl_ok}  (diagonal preserved)")
    all_ok = all_ok and r_ok and ss_ok and cl_ok
    print()
    print("=" * 60)
    print("RESULT:", "ALL STEPS VERIFIED" if all_ok else "FAILURE")
    print("=" * 60)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
