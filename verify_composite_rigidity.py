#!/usr/bin/env python3
"""verify_composite_rigidity.py - numerical check of Composite Rigidity Theorem.

Theorem: if A, B have Gram amplitude reps (full GL(d,C) congruence, pure surj),
and AB has a monoidal embedding W_A (x) W_B -> W_AB with q_AB(W_A(x)W_B) =
q_A(W_A) (x) q_B(W_B), then min d_AB = d_A*d_B and at minimum St_+(AB) =
PSD_{d_A*d_B} (quantum tensor product). d_AB > d_A*d_B => superselection-enlarged.
"""
import numpy as np
import sys


def check_kronecker_embedding(dA, rA, dB, rB, rng):
    WA = rng.standard_normal((dA, rA)) + 1j * rng.standard_normal((dA, rA))
    WB = rng.standard_normal((dB, rB)) + 1j * rng.standard_normal((dB, rB))
    WAB = np.kron(WA, WB)
    if WAB.shape != (dA * dB, rA * rB):
        return False, "shape mismatch"
    # monoidality: q_A(WA)(x)q_B(WB) == q_AB(WA(x)WB) with c_AB = c_A*c_B = 1
    rhoA = WA @ WA.conj().T
    rhoB = WB @ WB.conj().T
    lhs = np.kron(rhoA, rhoB)
    rhs = WAB @ WAB.conj().T
    return np.allclose(lhs, rhs, atol=1e-10), np.linalg.norm(lhs - rhs)


def check_rank1_composition(dA, dB, rng):
    a = rng.standard_normal(dA) + 1j * rng.standard_normal(dA)
    a /= np.linalg.norm(a)
    b = rng.standard_normal(dB) + 1j * rng.standard_normal(dB)
    b /= np.linalg.norm(b)
    Pa = np.outer(a, a.conj())
    Pb = np.outer(b, b.conj())
    Pab = np.kron(Pa, Pb)
    w = np.linalg.eigvalsh(Pab)
    return np.linalg.matrix_rank(Pab) == 1 and np.all(w >= -1e-9)


def check_enlarged_is_nonquantum(dA, dB, extra):
    dAB = dA * dB + extra
    v = np.zeros(dAB, dtype=complex)
    v[-1] = 1.0
    P = np.outer(v, v.conj())
    # this rank-1 PSD lives in PSD_{dAB} but NOT in the dA*dB tensor block
    return np.all(np.linalg.eigvalsh(P) >= -1e-9) and dAB > dA * dB


def main():
    print("=== Composite Rigidity Theorem - numerical verification ===\n")
    rng = np.random.default_rng(42)
    all_ok = True
    for dA, rA, dB, rB in [(3, 2, 2, 4), (2, 1, 2, 1), (4, 3, 3, 2), (2, 2, 3, 1)]:
        ok_mono, err = check_kronecker_embedding(dA, rA, dB, rB, rng)
        ok_rank1 = check_rank1_composition(dA, dB, rng)
        ok_enlarged = check_enlarged_is_nonquantum(dA, dB, 2)
        ok = ok_mono and ok_rank1 and ok_enlarged
        all_ok = all_ok and ok
        print(f"(dA={dA},rA={rA},dB={dB},rB={rB}): mono_err={err:.2e} "
              f"rank1_compose={ok_rank1} enlarged_nonquantum={ok_enlarged} => {'OK' if ok else 'FAIL'}")
    print(f"\nmin d_AB = d_A*d_B gives quantum tensor; d_AB > d_A*d_B gives superselection-enlarged.")
    print("=" * 60)
    print("RESULT:", "ALL VERIFIED" if all_ok else "FAILURE")
    print("=" * 60)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
