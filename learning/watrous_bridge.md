# From Watrous to correlated BB84 bases

[Learning map](milestones.md) · [Project tutorial](tutorial.md) · [Scientific account](../science/README.md)

The educational anchor is John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the prepublication manuscript and errata. The section and theorem numbers below refer to the **standard-layout author manuscript**, checked on 27 October 2026. Page numbers are the printed numbers within that manuscript, not a PDF viewer's page count. The author permits personal use of the manuscript and prohibits redistribution; this repository links to it.

Watrous supplies the finite-dimensional language of states, channels, measurements, norms and discrimination. The project uses those tools to ask a specific question: how does a correlated distribution of measurement bases determine the probability that two separated recipients both recover the same encoded string? The [tutorial](tutorial.md) develops that question directly. Reading entire textbook chapters first is unnecessary.

## Preparation needed for the core argument

Use this table as a targeted reference when a definition or proof step needs more detail. The milestone IDs refer to the common [30-milestone map](milestones.md).

| Watrous location | Preparation to extract | Role in this project |
| --- | --- | --- |
| [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §§1.1.1–1.1.2, beginning on pp. 1 and 8 | Vectors, inner products, adjoints, positive operators, projections and tensor products | Read a BB84 state, an outcome effect and a compound register; M01–M03 |
| [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §1.1.3, p. 24; Theorems 1.3 and 1.6, pp. 25 and 28 | Spectral decomposition, singular values and operator norms | Relate a largest eigenvalue to a success bound, and compare a Gram matrix with its frame operator; M06 and M14–M16 |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.1; especially §§2.1.2–2.1.3 | Density operators, reduced states and purifications | Distinguish a joint state from a marginal and an honest source from an arbitrary referee state; M01, M03 and M05 |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.2.1, beginning on p. 72 | Completely positive, trace-preserving maps | Model the splitting operation without imposing a measurement or memory restriction; M04 |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.3.1–2.3.2, beginning on pp. 100 and 105 | Positive measurement effects, product measurements and projective measurements | Understand both the arbitrary player POVMs and the referee's fixed PVMs; M02–M05 |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Theorem 2.42 and Corollary 2.43, p. 109 | Naimark dilation, including a chosen fixed ancilla state | Replace each player POVM by projections on a common larger space; M05 and M14 |
| [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §1.2.2, beginning on p. 47 | Random variables, expectations and independence, focusing on finite distributions | Read public-setup averages and moment bounds; M10–M11. The project's specific Chernoff optimization is supplied locally. |

The last row has a precise purpose. Theorem 2.42 gives an isometric representation of a measurement. Corollary 2.43 expresses the same measurement using projections after adjoining a fixed pure ancilla. For finitely many question-dependent POVMs, pad their outcome sets to a common finite size and use that same initial ancilla for each dilation. The resulting projective measurements may differ with the question. They are not required to commute with one another. The project gives this step in [the common-dilation argument](../science/spectral_value.md#a-common-projective-dilation).

## Preparation for information leakage and applications

These tools are needed for the full project, although the exact independent-state spectral formula does not require a discrimination SDP.

| Watrous location | Preparation to extract | Role in this project |
| --- | --- | --- |
| [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §1.2.3, beginning on p. 53 | Primal and dual semidefinite programs, including the meaning of a feasible dual certificate | Certify a guessing-probability upper bound; M07–M08 and M25 |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.2.3, classical-register discussion on pp. 95–96 | Block-diagonal classical-quantum states and the role of dephasing | Distinguish classical posterior conditioning from operations on a quantum side register; M08 and M25 |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1, beginning on p. 125; Theorem 3.4, p. 128 | Optimal discrimination of two states through the Holevo–Helstrom theorem | Evaluate the one-qubit basis-guessing task and interpret trace-distance privacy; M07 and M25–M27 |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.2, beginning on p. 132; simplified primal and dual on p. 134 | Optimize a measurement on an ensemble, or bound every measurement by a dominating operator | Prove the product-ensemble discrimination bound and the quantum-side-information domination inequality; M08, M25 and M28 |

For an ensemble with subnormalized states $`p_x\rho_x`$, the useful dual certificate is an operator $`Y`$ satisfying $`Y\succeq p_x\rho_x`$ for every label. Every discrimination POVM then obeys

```math
\sum_xp_x\mathrm{Tr}(M_x\rho_x)
\le\sum_x\mathrm{Tr}(M_xY)
=\mathrm{Tr}\,Y.
```

This short inequality explains what the certificate does. The exact feasible operators needed here are constructed locally in [quantum side information](../science/quantum_side_information.md#exact-discrimination-on-the-full-cube) and [key recycling](../science/key_recycling.md).

### Optional depth

Watrous §2.2.2 develops equivalent representations of channels. It is useful for readers who want more detail about arbitrary splitting maps, but the project does not require switching between all of those representations. The rest of the book's channel-capacity and entropy machinery is not a prerequisite for this argument. Likewise, a numerical SDP solver is optional: the important discrimination bounds here have explicit analytic certificates.

## Notation and normalization

| In the anchor | In this repository | How to read the change |
| --- | --- | --- |
| A finite complex Euclidean space such as $`\mathcal X`$ | A finite Hilbert space such as $`\mathcal H`$ | The project stays finite-dimensional. No infinite-dimensional extension is being assumed. |
| $`A^*`$ | $`A^\dagger`$ | Both denote the conjugate transpose. |
| $`uv^*`$ | $`\lvert u\rangle\langle v\rvert`$ | These are the same rank-one operator. A ket is a column vector; its bra is its adjoint. |
| $`1_{\mathcal X}`$ | $`I`$ or a register-labelled identity | The identity operator on the indicated space. |
| Spectral norm, often written $`\lVert A\rVert`$ | $`\lVert A\rVert_\infty`$ | Largest singular value; for positive $`A`$, its largest eigenvalue. |
| Trace norm $`\lVert A\rVert_1`$ | The same trace norm | The sum of singular values. |
| The manuscript calls $`\lVert\rho-\sigma\rVert_1`$ trace distance in §1.1.3 | $`D(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$ | The project uses the half-normalized convention. With equal priors, optimal binary success is $`(1+D)/2`$. |
| A measurement may be denoted $`\mu`$ | $`\mu(\theta)`$ denotes a basis distribution | Project measurement effects are written $`P_a,Q_b,B_x^\theta,D_x^\theta`$ instead. |

Within the project, $`C`$ denotes a binary code; Charlie's register is therefore called $`D`$. The general overlap $`c=\max_{a,b}\|P_aQ_b\|_\infty`$ is **unsquared**. For BB84 it is $`1/\sqrt2`$. Neither $`c`$ nor $`c^2`$ is the one-coordinate game value: that value for unbiased BB84 is $`\beta=(1+c)/2`$.

The symbol $`D(\gamma\|q)`$ with a double bar denotes binary relative entropy, not trace distance. Its logarithms are natural, while $`\log_2`$ measures bits. These conventions matter when comparing exponential probabilities with seed lengths.

## What the project supplies beyond the anchor

The textbook is the foundation, not the source of the project's cryptographic statements. The following bridges are supplied in the repository, with primary research attribution retained in [related work](../references/RELATED_WORK.md).

| Missing connection | Local explanation and authoritative proof |
| --- | --- |
| From two separated guesses to overlapping winning subspaces | [Spectral theorem](../science/spectral_value.md#pairwise-overlap-of-winning-subspaces): the inherited TFKW projector argument |
| From those overlaps to an exact value for correlated questions | [Weighted block-Gram comparison](../science/spectral_value.md#weighted-block-gram-comparison) and [principal-vector attainment](../science/spectral_value.md#attainment-by-principal-vectors) |
| From an arbitrary referee state to honestly prepared BB84 qubits | [Source replacement](../science/bb84_cloning.md#upper-bound-by-source-replacement) and [the normalized Pauli measurement](../science/bb84_cloning.md#pauli-covariant-measurement) |
| From a linear set of bases to a weight enumerator | [Code formula and Fourier proof](../science/codes_and_leakage.md#exact-code-formula), including the attribution to the earlier Fehr–Salvail bound |
| From a random public code to a short secret seed | [Exact mean](../science/codes_and_leakage.md#exact-mean-of-a-random-code), [certificate](../science/codes_and_leakage.md#a-high-probability-certificate) and [converse](../science/codes_and_leakage.md#optimal-secret-basis-rate) |
| From every fixed retained set to one uniform noise guarantee | [Projection and shortening](../science/noise_and_loss.md#projection-and-shortening), positive moment expansion and [branchwise loss conditions](../science/noise_and_loss.md#loss-commitments-and-subnormalized-branches) |
| From classical posteriors to the different power of quantum side information | [The preparation counterexample](../science/quantum_side_information.md), using explicit state-discrimination certificates |
| From the search game to particular cryptographic protocols | [Encryption](../science/applications.md) and [noiseless key recycling](../science/key_recycling.md), with their separately stated protocol assumptions and inherited reductions |

In particular, linear-code duality and the Chernoff calculation are explained locally; they are not assigned as unmentioned textbook prerequisites. The one-bit encryption compiler and the authentication protocol remain research-level dependencies. The tutorial explains how their hypotheses match this project, while their complete imported proofs belong to the cited primary papers.

## Reading route

The [tutorial](tutorial.md) follows the settled map's two phases: M01–M13 assemble the objects and experiments, and M14–M30 connect the exact proof to coding, leakage, loss and applications. Use the tables above when a mathematical tool needs a deeper reference. For theorem checking, go directly to the [scientific map](../science/README.md); for finite checks and reproduction, use [verification](../verification/README.md).
