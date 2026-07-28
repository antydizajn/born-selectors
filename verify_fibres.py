#!/usr/bin/env python3
"""Checks for the rectangular right-unitary fibre construction in Proposition 1."""
from __future__ import annotations

import numpy as np


def random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    return q @ np.diag(np.conj(phases))


def rank_matrix(d: int, r: int, rank: int, rng: np.random.Generator) -> np.ndarray:
    left = random_unitary(d, rng)
    right = random_unitary(r, rng)
    singular = np.linspace(0.7, 1.7, rank)
    sigma = np.zeros((d, r), dtype=complex)
    sigma[:rank, :rank] = np.diag(singular)
    return left @ sigma @ right.conj().T


def partial_isometry(x: np.ndarray, rank: int) -> tuple[np.ndarray, np.ndarray]:
    u, _, vh = np.linalg.svd(x, full_matrices=True)
    s = u[:, :rank] @ vh[:rank, :]
    kernel_basis = vh[rank:, :].conj().T
    return s, kernel_basis


def recover_right_unitary(w: np.ndarray, v: np.ndarray, rank: int) -> np.ndarray:
    sw, kw = partial_isometry(w, rank)
    sv, kv = partial_isometry(v, rank)
    return sw.conj().T @ sv + kw @ kv.conj().T


def test_rectangular_fibres() -> None:
    rng = np.random.default_rng(20260728)
    cases = [(3, 5, 1), (3, 5, 2), (5, 3, 1), (5, 3, 3), (4, 4, 1), (4, 4, 3)]
    for d, r, rank in cases:
        w = rank_matrix(d, r, rank, rng)
        u_true = random_unitary(r, rng)
        v = w @ u_true
        recovered = recover_right_unitary(w, v, rank)
        assert np.allclose(recovered.conj().T @ recovered, np.eye(r), atol=1e-10)
        assert np.allclose(w @ recovered, v, atol=1e-10)
        assert np.allclose(w @ w.conj().T, v @ v.conj().T, atol=1e-10)
    print("PASS rectangular and degenerate fibre construction")


if __name__ == "__main__":
    test_rectangular_fibres()
    print("ALL PASS")
