#!/usr/bin/env python3
"""Deterministic, self-contained numerical checks for BB84 Basis Information.

Run:
    python3 verification/run_all.py
    python3 verification/run_all.py --json result.json

Requires Python >= 3.11 with the pinned NumPy dependency. No network, SDP solver,
or data files are used.
The default enumerates every binary linear subspace through length four, every
affine coset, and every coordinate projection. Fixed-seed matrix examples check
the operator statements independently of the scalar formulas.

These finite floating-point checks are not proofs. In particular, sampling
player measurements cannot establish an upper bound on all quantum strategies.
The topic pages under science/ supply the dimension-independent proofs.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import itertools
import json
import math
import os
from pathlib import Path
import sys

# Keep these small matrix checks inexpensive on machines with threaded BLAS.
for _variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_variable, "1")

import numpy as np


TOL = 2e-10
SEED = 20261027
C_BB84 = 1 / math.sqrt(2)
BETA = (1 + C_BB84) / 2
QSTAR = 1 - BETA
KAPPA = QSTAR / BETA
ALPHA = -math.log2(BETA)
I2 = np.eye(2, dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


class Audit:
    def __init__(self) -> None:
        self.section = "initialization"
        self.counts: Counter[str] = Counter()
        self.max_equality_residual = 0.0
        self.max_positive_inequality_residual = 0.0
        self.details: dict[str, object] = {}

    def check(self, condition: bool, label: str) -> None:
        self.counts[self.section] += 1
        if not condition:
            raise AssertionError(f"{self.section}: {label}")

    def equal(self, actual: object, expected: object, label: str) -> None:
        lhs, rhs = np.asarray(actual), np.asarray(expected)
        residual = float(np.max(np.abs(lhs - rhs))) if lhs.size else 0.0
        scale = 1 + (float(np.max(np.abs(rhs))) if rhs.size else 0.0)
        self.max_equality_residual = max(self.max_equality_residual, residual)
        self.check(residual <= TOL * scale, f"{label}: residual {residual:.3g}")

    def upper(self, actual: float, bound: float, label: str) -> None:
        residual = float(actual - bound)
        self.max_positive_inequality_residual = max(
            self.max_positive_inequality_residual, residual
        )
        self.check(
            residual <= TOL * (1 + abs(bound)),
            f"{label}: actual {actual:.16g}, bound {bound:.16g}",
        )

    def psd(self, matrix: np.ndarray, label: str) -> None:
        self.equal(matrix, matrix.conj().T, f"{label}, Hermitian")
        self.upper(-float(np.linalg.eigvalsh(matrix)[0]), 0, f"{label}, PSD")


def herm(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def top(matrix: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(herm(matrix))[-1])


def outer(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def tensor(factors: object) -> np.ndarray:
    result = np.array([1.0 + 0.0j])
    for factor in factors:
        result = np.kron(result, factor)
    return result


def bits(word: int, n: int) -> tuple[int, ...]:
    return tuple((word >> (n - 1 - i)) & 1 for i in range(n))


def selected_positions(mask: int, n: int) -> tuple[int, ...]:
    return tuple(i for i, bit in enumerate(bits(mask, n)) if bit)


def project(word: int, mask: int, n: int) -> int:
    result = 0
    word_bits = bits(word, n)
    for i in selected_positions(mask, n):
        result = (result << 1) | word_bits[i]
    return result


def submasks(mask: int):
    current = mask
    while True:
        yield current
        if current == 0:
            return
        current = (current - 1) & mask


@lru_cache(maxsize=None)
def bb84_vector(theta: int, answer: int, n: int) -> np.ndarray:
    return tensor(
        (H if theta_i else I2)[:, answer_i]
        for theta_i, answer_i in zip(bits(theta, n), bits(answer, n))
    )


def kernel(words: tuple[int, ...], weights: np.ndarray, c: float) -> np.ndarray:
    roots = np.sqrt(weights)
    return np.array(
        [
            [roots[i] * roots[j] * c ** ((a ^ b).bit_count())
             for j, b in enumerate(words)]
            for i, a in enumerate(words)
        ],
        dtype=float,
    )


@lru_cache(maxsize=None)
def uniform_bb84_value(words: tuple[int, ...]) -> float:
    return top(kernel(words, np.full(len(words), 1 / len(words)), C_BB84))


def random_unitary(dimension: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    unitary, triangular = np.linalg.qr(raw)
    phases = np.diag(triangular)
    phases = phases / np.abs(phases)
    return unitary * phases.conj()[None, :]


def pvm_from_ranks(
    ranks: tuple[int, ...], rng: np.random.Generator, rotated: bool = True
) -> list[np.ndarray]:
    d = sum(ranks)
    unitary = random_unitary(d, rng) if rotated else np.eye(d, dtype=complex)
    result, start = [], 0
    for rank in ranks:
        columns = unitary[:, start:start + rank]
        result.append(columns @ columns.conj().T)
        start += rank
    return result


def player_pvm(
    dimension: int, outcomes: int, rng: np.random.Generator
) -> list[np.ndarray]:
    unitary = random_unitary(dimension, rng)
    result = [np.zeros((dimension, dimension), dtype=complex) for _ in range(outcomes)]
    labels = rng.permutation(outcomes)
    for j in range(dimension):
        result[int(labels[j % outcomes])] += outer(unitary[:, j])
    return result


def player_povm(
    dimension: int, outcomes: int, rng: np.random.Generator
) -> list[np.ndarray]:
    raw = []
    for _ in range(outcomes):
        matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
            size=(dimension, dimension)
        )
        raw.append(matrix @ matrix.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(sum(raw))
    inverse_root = (eigenvectors * (1 / np.sqrt(eigenvalues))) @ eigenvectors.conj().T
    return [herm(inverse_root @ effect @ inverse_root) for effect in raw]


def check_measurement(audit: Audit, effects: list[np.ndarray], projective: bool) -> None:
    audit.equal(sum(effects), np.eye(len(effects[0])), "measurement normalization")
    for effect in effects:
        audit.psd(effect, "measurement effect")
        if projective:
            audit.equal(effect @ effect, effect, "projection idempotence")
    if projective:
        for i, left in enumerate(effects):
            for right in effects[i + 1:]:
                audit.equal(left @ right, np.zeros_like(left), "orthogonal outcomes")


def check_nonuniform_bb84_and_physical(audit: Audit) -> None:
    audit.section = "nonuniform Gram, frame, and physical POVM"
    cases = [
        (1, [1, 4]), (1, [1, 0]), (1, [1, 1]),
        (2, [1, 7, 2, 5]), (2, [0, 1, 3, 0]),
        (3, [1, 0, 4, 2, 7, 1, 3, 5]),
    ]
    physical_values = []
    for n, raw_weights in cases:
        d = 1 << n
        words = tuple(range(d))
        weights = np.asarray(raw_weights, dtype=float)
        weights /= weights.sum()
        weighted_vectors = np.column_stack(
            [math.sqrt(weights[t]) * bb84_vector(t, 0, n) for t in words]
        )
        gram = kernel(words, weights, C_BB84)
        frame = weighted_vectors @ weighted_vectors.conj().T
        audit.equal(weighted_vectors.conj().T @ weighted_vectors, gram, "Gram entries")
        audit.equal(np.linalg.eigvalsh(frame), np.linalg.eigvalsh(gram), "Gram/frame spectrum")
        value, psi = np.linalg.eigh(frame)
        psi = psi[:, -1]
        expected = float(value[-1])

        effects, paulis, labels = [], [], []
        for u in words:
            for v in words:
                pauli = tensor(
                    np.linalg.matrix_power(X, ui) @ np.linalg.matrix_power(Z, vi)
                    for ui, vi in zip(bits(u, n), bits(v, n))
                )
                paulis.append(pauli)
                labels.append((u, v))
                effects.append(outer(pauli @ psi.conj()) / d)
        check_measurement(audit, effects, projective=False)
        direct_success = 0.0
        for theta in words:
            probability_table = np.array(
                [
                    [
                        float(np.vdot(bb84_vector(theta, x, n),
                                      effect @ bb84_vector(theta, x, n)).real)
                        for x in words
                    ]
                    for effect in effects
                ]
            )
            audit.equal(probability_table.sum(axis=0), np.ones(d), "input probability sum")
            audit.equal(probability_table.mean(axis=1), np.full(d * d, 1 / (d * d)),
                        "POVM outcome independent of basis after uniform plaintext")
            for index, ((u, v), pauli) in enumerate(zip(labels, paulis)):
                guess = 0
                for ti, ui, vi in zip(bits(theta, n), bits(u, n), bits(v, n)):
                    guess = (guess << 1) | (vi if ti else ui)
                success_projection = outer(bb84_vector(theta, guess, n))
                audit.equal(pauli.conj().T @ success_projection @ pauli,
                            outer(bb84_vector(theta, 0, n)), "Pauli outcome covariance")
                direct_success += weights[theta] * probability_table[index, guess] / d
        audit.equal(direct_success, expected, "direct prepare-and-measure success")
        physical_values.append({"n": n, "value": expected})

    # All deterministic common-answer tables for two nonuniform two-qubit games.
    # This compares a separate maximization with the proposed spectral value.
    for raw in ([1, 7, 2, 5], [0, 1, 3, 0]):
        weights = np.array(raw, dtype=float) / sum(raw)
        expected = top(kernel(tuple(range(4)), weights, C_BB84))
        best = 0.0
        for answers in itertools.product(range(4), repeat=4):
            payoff = sum(weights[t] * outer(bb84_vector(t, answers[t], 2))
                         for t in range(4))
            value = top(payoff)
            audit.upper(value, expected, "deterministic table upper bound")
            best = max(best, value)
        audit.equal(best, expected, "exhaustive deterministic optimum")

    for n in (1, 2, 3, 4):
        for t in (0.0, 0.17, 0.5, 0.89, 1.0):
            weights = np.array([t ** (n - word.bit_count()) *
                                (1 - t) ** word.bit_count()
                                for word in range(1 << n)])
            one = (1 + math.sqrt((2 * t - 1) ** 2 +
                                 4 * t * (1 - t) * C_BB84 ** 2)) / 2
            audit.equal(top(kernel(tuple(range(1 << n)), weights, C_BB84)),
                        one ** n, "biased independent question value")
    audit.details["physical_examples"] = physical_values


def check_general_pvms(audit: Audit, rng: np.random.Generator) -> None:
    audit.section = "general higher-rank PVMs and quantum player measurements"
    examples = [
        (pvm_from_ranks((2, 2), rng, False), pvm_from_ranks((2, 2), rng),
         2, np.array([0.1, 0.2, 0.3, 0.4])),
        (pvm_from_ranks((2, 1), rng, False), pvm_from_ranks((1, 1, 1), rng),
         1, np.array([0.31, 0.69])),
    ]
    results = []
    for pvm_p, pvm_q, n, weights in examples:
        check_measurement(audit, pvm_p, True)
        check_measurement(audit, pvm_q, True)
        overlaps = np.array([[np.linalg.norm(p @ q, ord=2) for q in pvm_q]
                             for p in pvm_p])
        a0, b0 = np.unravel_index(np.argmax(overlaps), overlaps.shape)
        c = float(overlaps[a0, b0])
        audit.check(0 < c < 1 - 1e-6, "nontrivial principal angle in test example")
        p, q = pvm_p[a0], pvm_q[b0]
        _, vectors = np.linalg.eigh(herm(q @ p @ q))
        v = q @ vectors[:, -1]
        v /= np.linalg.norm(v)
        u = p @ v / c
        audit.equal(np.linalg.norm(u), 1, "principal vector normalization")
        audit.equal(p @ u, u, "principal vector in P range")
        audit.equal(q @ v, v, "principal vector in Q range")
        audit.equal(np.vdot(u, v), c, "positive principal-vector overlap")

        words = tuple(range(1 << n))
        gram = kernel(words, weights, c)
        target = top(gram)
        weighted_vectors, successful_projections, referee_measurements = [], [], []
        for theta in words:
            coordinates = [pvm_q if bit else pvm_p for bit in bits(theta, n)]
            outcome_tuples = list(itertools.product(*(range(len(x)) for x in coordinates)))
            referee_measurements.append([
                tensor(coordinates[i][answer[i]] for i in range(n))
                for answer in outcome_tuples
            ])
            weighted_vectors.append(math.sqrt(weights[theta]) *
                                    tensor(v if bit else u for bit in bits(theta, n)))
            successful_projections.append(tensor(q if bit else p for bit in bits(theta, n)))
        columns = np.column_stack(weighted_vectors)
        frame = columns @ columns.conj().T
        deterministic_payoff = sum(weights[t] * successful_projections[t] for t in words)
        audit.equal(columns.conj().T @ columns, gram, "general principal-vector Gram")
        audit.psd(deterministic_payoff - frame, "higher-rank payoff dominates frame")
        audit.equal(top(frame), target, "general frame value")
        audit.equal(top(deterministic_payoff), target, "higher-rank attained value")

        best_table = 0.0
        for answers in itertools.product(*(range(len(m)) for m in referee_measurements)):
            value = top(sum(weights[t] * referee_measurements[t][answers[t]] for t in words))
            audit.upper(value, target, "general deterministic table")
            best_table = max(best_table, value)
        audit.equal(best_table, target, "general exhaustive deterministic optimum")

        # Optimize the initial tripartite state exactly for each sampled family
        # of fully question-dependent local measurements, including genuine POVMs.
        for projective in (True, False):
            payoffs = []
            constructor = player_pvm if projective else player_povm
            for referee_pvm in referee_measurements:
                bob = constructor(2, len(referee_pvm), rng)
                charlie = constructor(2, len(referee_pvm), rng)
                check_measurement(audit, bob, projective)
                check_measurement(audit, charlie, projective)
                payoff = sum(tensor((f, b, z)) for f, b, z in zip(referee_pvm, bob, charlie))
                payoffs.append(payoff)
                if projective:
                    audit.equal(payoff @ payoff, payoff, "winning operator is projection")
            audit.upper(top(sum(weights[t] * payoffs[t] for t in words)), target,
                        "sampled quantum measurement family, exact state optimization")
            if projective:
                for theta in words:
                    for phi in words:
                        audit.upper(float(np.linalg.norm(payoffs[theta] @ payoffs[phi], ord=2)),
                                    c ** ((theta ^ phi).bit_count()),
                                    "pairwise winning-projection overlap")
        for t in (0.07, 0.31, 0.5, 0.93):
            product_weights = np.array([t ** (n - w.bit_count()) *
                                        (1 - t) ** w.bit_count() for w in words])
            single = (1 + math.sqrt((2 * t - 1) ** 2 + 4 * t * (1 - t) * c * c)) / 2
            audit.equal(top(kernel(words, product_weights, c)), single ** n,
                        "general biased independent question product")
        results.append({"referee_dimension": len(pvm_p[0]), "n": n, "c": c, "value": target})
    audit.details["higher_rank_examples"] = results


@lru_cache(maxsize=None)
def all_subspaces(n: int) -> tuple[tuple[int, ...], ...]:
    levels = {(0,)}
    result = []
    for dimension in range(n + 1):
        result.extend(sorted(levels))
        if dimension == n:
            break
        next_level = set()
        for code in levels:
            code_set = set(code)
            for word in range(1 << n):
                if word not in code_set:
                    next_level.add(tuple(sorted(code_set | {x ^ word for x in code})))
        levels = next_level
    return tuple(result)


def dual(code: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(word for word in range(1 << n)
                 if all((word & x).bit_count() % 2 == 0 for x in code))


def cosets(code: tuple[int, ...], n: int):
    remaining = set(range(1 << n))
    while remaining:
        offset = min(remaining)
        affine = tuple(sorted(offset ^ x for x in code))
        remaining.difference_update(affine)
        yield offset, affine


def weight_sum(code: tuple[int, ...], parameter: float) -> float:
    return sum(parameter ** word.bit_count() for word in code)


def shortened(dual_code: tuple[int, ...], mask: int, n: int) -> tuple[int, ...]:
    return tuple(sorted(project(word, mask, n) for word in dual_code if (word & ~mask) == 0))


def mgf_formula(dual_code: tuple[int, ...], mask: int, n: int, s: float) -> float:
    a = BETA + QSTAR * s
    b = QSTAR * (1 - s)
    return a ** mask.bit_count() * weight_sum(shortened(dual_code, mask, n), b / a)


def check_codes(audit: Audit, max_n: int) -> None:
    audit.section = "all small codes, affine cosets, projections, and MGF coefficients"
    code_count = coset_count = affine_projection_count = 0
    means = []
    for n in range(1, max_n + 1):
        codes = all_subspaces(n)
        by_dimension: dict[int, list[tuple[tuple[int, ...], float, float]]] = defaultdict(list)
        for code in codes:
            code_count += 1
            k = len(code).bit_length() - 1
            dual_code = dual(code, n)
            value = uniform_bb84_value(code)
            primal = weight_sum(code, C_BB84) / len(code)
            dual_value = BETA ** n * weight_sum(dual_code, KAPPA)
            audit.equal(value, primal, "Gram eigenvalue versus primal weight enumerator")
            audit.equal(value, dual_value, "MacWilliams dual weight enumerator")
            audit.check(len(code) * len(dual_code) == 1 << n, "dual dimension")
            by_dimension[k].append((dual_code, value, weight_sum(dual_code, KAPPA) - 1))
            projected_values: dict[int, float] = {}
            projections: dict[int, tuple[int, ...]] = {}
            for mask in range(1 << n):
                h = mask.bit_count()
                projection = tuple(sorted({project(x, mask, n) for x in code}))
                projections[mask] = projection
                fibers = Counter(project(x, mask, n) for x in code)
                audit.check(set(fibers.values()) == {len(code) // len(projection)},
                            "uniform fibers of a linear projection")
                short = shortened(dual_code, mask, n)
                audit.check(dual(projection, h) == short, "projection dual equals shortening")
                projected_values[mask] = uniform_bb84_value(projection)
                audit.equal(projected_values[mask], BETA ** h * weight_sum(short, KAPPA),
                            "projected exact game value")
            for offset, affine in cosets(code, n):
                coset_count += 1
                audit.equal(uniform_bb84_value(affine), value, "affine translation value")
                frame = sum(outer(bb84_vector(theta, 0, n)) for theta in affine) / len(affine)
                audit.equal(top(frame), value, "affine physical frame value")
                for mask in range(1 << n):
                    affine_projection_count += 1
                    projected = tuple(sorted({project(x, mask, n) for x in affine}))
                    expected = tuple(sorted(project(offset, mask, n) ^ x
                                            for x in projections[mask]))
                    audit.check(projected == expected, "affine projection identity")
                    fibers = Counter(project(x, mask, n) for x in affine)
                    audit.check(set(fibers.values()) == {len(affine) // len(projected)},
                                "uniform fibers of an affine projection")
                    audit.equal(uniform_bb84_value(projected), projected_values[mask],
                                "affine projected game value")
            certificate = weight_sum(dual_code, KAPPA)
            for mask in range(1 << n):
                h = mask.bit_count()
                for s in (0.0, 0.17, 0.5, 0.83, 1.0):
                    expanded = sum(
                        s ** (h - subset.bit_count()) *
                        (1 - s) ** subset.bit_count() * projected_values[subset]
                        for subset in submasks(mask)
                    )
                    closed = mgf_formula(dual_code, mask, n, s)
                    audit.equal(expanded, closed, "subset coefficient expansion")
                    audit.upper(closed, certificate * (BETA + QSTAR * s) ** h,
                                "one certificate controls all subsets and s")

        # Exact rational inclusion frequencies and an independent average over
        # enumerated spectral values verify the random-code mean.
        for k, entries in sorted(by_dimension.items()):
            probability = Fraction((1 << (n - k)) - 1, (1 << n) - 1)
            for word in range(1, 1 << n):
                actual = Fraction(sum(word in item[0] for item in entries), len(entries))
                audit.check(actual == probability, "exact random-dual inclusion frequency")
            mean_value = float(np.mean([item[1] for item in entries]))
            expected = BETA ** n + float(probability) * (1 - BETA ** n)
            audit.equal(mean_value, expected, "exact random-code mean")
            excess_mean = float(probability) * (BETA ** (-n) - 1)
            audit.equal(float(np.mean([item[2] for item in entries])), excess_mean,
                        "random certificate excess mean")
            for epsilon in (0.01, 0.1, 0.5, 2.0):
                failure = sum(item[2] > epsilon + TOL for item in entries) / len(entries)
                audit.upper(failure, min(1.0, excess_mean / epsilon), "Markov certificate bound")
            means.append({"n": n, "k": k, "codes": len(entries),
                          "mean": mean_value, "formula": expected})
    audit.details["enumeration"] = {
        "maximum_length": max_n,
        "linear_codes": code_count,
        "affine_cosets": coset_count,
        "affine_projections": affine_projection_count,
    }
    audit.details["random_code_means"] = means


def check_unused_basis_and_noise(audit: Audit, rng: np.random.Generator) -> None:
    audit.section = "unused basis context and direct noise payoff operators"
    n = 3
    full_mask = (1 << n) - 1
    code = (0, 3, 5, 6)  # Even parity: unused basis coordinates are correlated.
    dual_code = dual(code, n)
    dimension = (1 << n) * 2 * 2
    bins = [np.zeros((dimension, dimension), dtype=complex) for _ in range(1 << n)]
    for theta in code:
        # Full-question-dependent joint answer measurements. Only two output
        # labels have nonzero projections, but each labels an entire 3-bit string.
        bob = player_pvm(2, 1 << n, rng)
        charlie = player_pvm(2, 1 << n, rng)
        active_b = [(label, effect) for label, effect in enumerate(bob)
                    if np.linalg.norm(effect) > 0.5]
        active_c = [(label, effect) for label, effect in enumerate(charlie)
                    if np.linalg.norm(effect) > 0.5]
        for answer in range(1 << n):
            referee = outer(bb84_vector(theta, answer, n))
            for b, effect_b in active_b:
                for z, effect_c in active_c:
                    correct_mask = full_mask ^ ((answer ^ b) | (answer ^ z))
                    bins[correct_mask] += tensor((referee, effect_b, effect_c)) / len(code)
    audit.equal(sum(bins), np.eye(dimension), "joint outcome operators sum to identity")
    for mask in range(1 << n):
        projection = tuple(sorted({project(x, mask, n) for x in code}))
        moment_operator = sum(effect for correct, effect in enumerate(bins)
                              if correct & mask == mask)
        audit.upper(top(moment_operator), uniform_bb84_value(projection),
                    "subset upper bound with access to all correlated basis coordinates")
        for s in (0.0, 0.25, 0.5, 0.75, 1.0):
            direct_operator = sum(
                s ** ((mask & ~correct).bit_count()) * effect
                for correct, effect in enumerate(bins)
            )
            audit.upper(top(direct_operator), mgf_formula(dual_code, mask, n, s),
                        "direct weighted-noise operator, arbitrary initial state")

    # Product Breidbart states have the same product error distribution for
    # every basis, even when the distribution over bases is correlated.
    breidbart = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)], dtype=complex)
    product = tensor([breidbart] * n)
    for theta in range(1 << n):
        for answer in range(1 << n):
            actual = abs(np.vdot(bb84_vector(theta, answer, n), product)) ** 2
            expected = BETA ** (n - answer.bit_count()) * QSTAR ** answer.bit_count()
            audit.equal(actual, expected, "basis-independent product error distribution")

    # The code MGF is only claimed as an upper bound. On this small example,
    # even the best initial state for the all-zero deterministic answers has a
    # strict gap, so tests must not silently replace the bound by an equality.
    s = 0.5
    noisy_z = s * I2 + (1 - s) * outer(np.array([1, 0], dtype=complex))
    noisy_x = s * I2 + (1 - s) * outer(np.array([1, 1], dtype=complex) / math.sqrt(2))
    actual = top((np.kron(noisy_z, noisy_z) + np.kron(noisy_x, noisy_x)) / 2)
    bound = mgf_formula((0, 3), 3, 2, s)
    audit.upper(actual, bound, "nontrivial code noise example")
    audit.check(bound - actual > 1e-4, "retain strict upper-bound status of code MGF")
    audit.details["noise_bound_example"] = {
        "code": ["00", "11"], "s": s,
        "best_state_with_constant_answers": actual, "moment_bound": bound,
    }


def binary_entropy(x: float) -> float:
    if x in (0.0, 1.0):
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def binary_relative_entropy(x: float, p: float) -> float:
    left = 0.0 if x == 0 else x * math.log(x / p)
    right = 0.0 if x == 1 else (1 - x) * math.log((1 - x) / (1 - p))
    return left + right


def check_constants_and_quantum_counterexample(audit: Audit) -> None:
    audit.section = "constants, Chernoff optimization, and quantum leakage counterexample"
    audit.equal(BETA, math.cos(math.pi / 8) ** 2, "BB84 beta")
    audit.equal(QSTAR, math.sin(math.pi / 8) ** 2, "BB84 noise threshold")
    audit.equal(KAPPA, (math.sqrt(2) - 1) ** 2, "dual weight parameter")
    audit.equal(ALPHA, 0.22844669683638807, "seed rate")
    for gamma in (0.001, 0.01, 0.05, 0.1, 0.14):
        s = gamma * BETA / (QSTAR * (1 - gamma))
        audit.check(0 < s < 1, "Chernoff optimizer in domain")
        actual = -gamma * math.log(s) + math.log(BETA + QSTAR * s)
        audit.equal(actual, -binary_relative_entropy(gamma, QSTAR), "KL exponent")
        audit.equal(-gamma / s + QSTAR / (BETA + QSTAR * s), 0, "stationary point")
        for alternative in (s / 2, (s + 1) / 2, 1):
            alternative_value = -gamma * math.log(alternative) + math.log(
                BETA + QSTAR * alternative
            )
            audit.upper(actual, alternative_value, "Chernoff minimum")

    rho0 = outer(np.array([1, 0], dtype=complex))
    rho1 = outer(np.array([1, 1], dtype=complex) / math.sqrt(2))
    eigenvalues, eigenvectors = np.linalg.eigh(rho0 - rho1)
    absolute_difference = (eigenvectors * np.abs(eigenvalues)) @ eigenvectors.conj().T
    dual_one = (rho0 + rho1 + absolute_difference) / 4
    helstrom0 = outer(eigenvectors[:, np.argmax(eigenvalues)])
    helstrom1 = I2 - helstrom0
    audit.psd(dual_one - rho0 / 2, "one-copy discrimination dual, label zero")
    audit.psd(dual_one - rho1 / 2, "one-copy discrimination dual, label one")
    audit.equal(np.trace(dual_one), BETA, "one-copy dual objective")
    audit.equal((np.trace(helstrom0 @ rho0) + np.trace(helstrom1 @ rho1)) / 2,
                BETA, "one-copy Helstrom primal")
    for n in (1, 2, 3):
        dual_n = tensor([dual_one] * n)
        direct_success = 0.0
        for theta in range(1 << n):
            state = outer(bb84_vector(theta, 0, n))
            audit.psd(dual_n - state / (1 << n), "product discrimination dual constraint")
            measurement = tensor(helstrom1 if bit else helstrom0 for bit in bits(theta, n))
            direct_success += float(np.trace(measurement @ state).real) / (1 << n)
            audit.equal(np.trace(state @ state), 1, "forwarded quantum program wins")
        audit.equal(direct_success, BETA ** n, "full-cube product discrimination optimum")
        for code in all_subspaces(n):
            k = len(code).bit_length() - 1
            restricted_dual = (2 ** (n - k)) * dual_n
            for theta in code:
                audit.psd(restricted_dual - outer(bb84_vector(theta, 0, n)) / len(code),
                          "restricted-code discrimination dual")

    first_violation = next(n for n in range(1, 100) if BETA ** n + C_BB84 < 1)
    audit.check(first_violation == 8, "first full-cube additive-bound violation")
    finite_rhs = BETA ** 8 + C_BB84
    audit.equal(finite_rhs, 0.988844850876055, "eight-qubit counterexample value")
    for theta in range(256):
        vector = bb84_vector(theta, 0, 8)
        audit.equal(abs(np.vdot(vector, vector)) ** 2, 1, "eight-qubit program acceptance")

    # A finite existence check illustrates the positive-rate, positive-distance
    # family. It does not claim to exhibit a particular generator matrix.
    n, k, distance = 400, 360, 4
    low_weight_count = sum(math.comb(n, j) for j in range(1, distance))
    inclusion = Fraction((1 << k) - 1, (1 << n) - 1)
    bad_word_mean = inclusion * low_weight_count
    audit.check(bad_word_mean < 1, "positive-rate code of distance four exists")
    code_rhs = 2 ** (n - k) * BETA ** n + 2 ** (-distance / 2)
    audit.check(code_rhs < 1, "positive-rate finite additive-bound violation")
    audit.check(binary_entropy(0.01) < 0.1, "asymptotic distance-existence margin")
    audit.check(0.9 - 1 + ALPHA > 0, "asymptotic guessing decay rate")

    n, t = 64, 6
    k = math.ceil(ALPHA * n + 2 * t)
    probability = ((1 << (n - k)) - 1) / ((1 << n) - 1)
    failure_bound = probability * (BETA ** (-n) - 1) / (2 ** (-t))
    audit.upper(failure_bound, 2 ** (-t), "high-probability seed-rate parameters")
    audit.details["constants"] = {
        "beta": BETA, "q_star": QSTAR, "kappa": KAPPA,
        "alpha": ALPHA, "unchanged_exponent_syndrome_rate": 1 - ALPHA,
        "binary_entropy_0.01": binary_entropy(0.01),
    }
    audit.details["quantum_leakage_counterexample"] = {
        "full_cube_n": 8, "actual_win": 1, "proposed_upper_bound": finite_rhs,
        "positive_rate_existence_n": 400, "positive_rate_dimension": 360,
        "minimum_distance": 4, "expected_bad_words": float(bad_word_mean),
        "positive_rate_proposed_bound": code_rhs,
    }
    audit.details["high_probability_example"] = {
        "n": n, "k": k, "t": t, "failure_bound": failure_bound,
        "certificate_epsilon": 2 ** (-t),
    }


def check_application_formulas(audit: Audit) -> None:
    """Check only the concrete privacy identity and stated GV comparison.

    This does not numerically establish the inherited common-mask compiler,
    its quartic reduction, or the sequential key-recycling theorem.
    """
    audit.section = "one-bit ordinary privacy and QKR comparison constants"
    n = 2
    d = 1 << n
    classical = [outer(I2[:, bit]) for bit in (0, 1)]
    privacy_results = []
    for code in all_subspaces(n):
        frame = sum(outer(bb84_vector(theta, 0, n)) for theta in code) / len(code)
        ciphertexts = []
        for message in (0, 1):
            direct = np.zeros((2 * d, 2 * d), dtype=complex)
            for theta in code:
                for plaintext in range(d):
                    quantum = outer(bb84_vector(theta, plaintext, n))
                    for mask in range(d):
                        ciphertext_bit = message ^ ((mask & plaintext).bit_count() % 2)
                        direct += np.kron(quantum, classical[ciphertext_bit]) / (
                            len(code) * d * d
                        )
            formula = np.kron((np.eye(d) - frame) / (2 * d), I2) + np.kron(
                frame / d, classical[message]
            )
            audit.equal(direct, formula, "direct average over basis, X, and secret mask")
            audit.psd(direct, "averaged one-bit ciphertext")
            audit.equal(np.trace(direct), 1, "averaged ciphertext normalization")
            ciphertexts.append(direct)
        difference = herm(ciphertexts[0] - ciphertexts[1])
        distance = float(np.abs(np.linalg.eigvalsh(difference)).sum() / 2)
        audit.equal(distance, 1 / d, "exact ordinary ciphertext trace distance")
        reading_classical_bit = sum(
            float(np.trace(np.kron(np.eye(d), classical[message]) @
                           ciphertexts[message]).real) / 2
            for message in (0, 1)
        )
        audit.equal(reading_classical_bit, 0.5 + 1 / (2 * d),
                    "reading only the classical bit attains ordinary guessing value")
        privacy_results.append({
            "n": n, "code": list(code), "trace_distance": distance,
            "ordinary_guess_probability": reading_classical_bit,
        })

    # The stated comparison uses the unique R in (0, 1/4) satisfying
    # R + h_2(2R) = 1, not a lower bound on arbitrary codes or protocols.
    low, high = 0.0, 0.25
    for _ in range(80):
        middle = (low + high) / 2
        if middle + binary_entropy(2 * middle) < 1:
            low = middle
        else:
            high = middle
    rate = (low + high) / 2
    old_coefficient = 3 / rate
    new_coefficient = 3 / ALPHA
    reduction = 1 - new_coefficient / old_coefficient
    audit.equal(rate + binary_entropy(2 * rate), 1, "GV comparison equation")
    audit.equal(rate, 0.1412269869961669, "GV threshold rate")
    audit.equal(old_coefficient, 21.2423989480, "old GV-certified qubit coefficient")
    audit.equal(new_coefficient, 13.1321662407, "exact-average qubit coefficient")
    audit.equal(reduction, 0.381794576363, "relative certification-cost reduction")
    audit.check(298 >= ALPHA * 1024 + 64, "public 1024-qubit high-probability example")
    for security_bits in (1, 16, 64):
        block_length = math.ceil(3 * security_bits / ALPHA)
        audit.upper(-ALPHA * block_length, -3 * security_bits,
                    "finite exact-average QKR parameter ceiling")
    audit.details["application_formula_checks"] = {
        "ordinary_privacy_examples": privacy_results,
        "gv_rate": rate,
        "old_qubits_per_security_bit": old_coefficient,
        "new_qubits_per_security_bit": new_coefficient,
        "relative_reduction": reduction,
        "limitation": "Only density-operator identities and constants are checked here; "
                      "the compiler and recycling proofs are not numerically verified.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-code-n", type=int, choices=range(1, 6), default=4,
                        help="enumerate every subspace up to this length (default 4)")
    parser.add_argument("--json", type=Path, help="optional machine-readable result file")
    args = parser.parse_args()
    audit = Audit()
    rng = np.random.default_rng(SEED)
    check_nonuniform_bb84_and_physical(audit)
    check_general_pvms(audit, rng)
    check_codes(audit, args.max_code_n)
    check_unused_basis_and_noise(audit, rng)
    check_constants_and_quantum_counterexample(audit)
    check_application_formulas(audit)
    report = {
        "status": "PASS",
        "interpretation": "Finite numerical checks support, but do not prove, the analytic results.",
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "seed": SEED,
        "relative_scale_tolerance": TOL,
        "checks": sum(audit.counts.values()),
        "checks_by_section": dict(audit.counts),
        "max_absolute_equality_residual": audit.max_equality_residual,
        "max_positive_inequality_residual": audit.max_positive_inequality_residual,
        **audit.details,
    }
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
