# BB84 Basis Information

**How much secret basis information is needed to prevent two separated recipients from recovering the same BB84-encoded string?** This project determines the exact security value for every distribution of BB84 bases and shows that **0.2284467 secret basis bits per qubit** suffice asymptotically to retain the full independent-basis recovery exponent. The rate is optimal within this basis-selection model.

The source encodes a uniform $`n`$-bit string in BB84 qubits. An adversary must split the state before the basis is revealed; both recipients then learn the basis and must recover the complete string without communicating. Arbitrary collective attacks and finite quantum memories are allowed.

For any basis distribution $`\mu`$, define

```math
(K_\mu)_{\theta,\phi}
=\sqrt{\mu(\theta)\mu(\phi)}\,2^{-d_H(\theta,\phi)/2}.
```

The optimal joint recovery probability is exactly

```math
\boxed{\omega(\mu)=\lambda_{\max}(K_\mu).}
```

A Pauli-covariant measurement followed by sharing classical data attains this value. The corresponding abstract monogamy theorem holds for any fixed pair of finite-dimensional projective measurements, with their maximum projector-overlap norm replacing $`1/\sqrt2`$.

## Principal results

Write $`\beta=\cos^2(\pi/8)`$, $`q_*=1-\beta`$ and $`\kappa=q_*/\beta`$. For a binary basis code $`C`$ of dimension $`k`$, let $`R=C^\perp`$ and $`W_R(t)=\sum_{r\in R}t^{|r|}`$.

| Question | Result | Authoritative account |
|---|---|---|
| Arbitrary correlated or biased bases | Exact largest-eigenvalue formula, attained without player quantum memory | [Spectral value](science/spectral_value.md) and [physical attack](science/bb84_cloning.md) |
| Uniform linear or affine basis set | Exact value from the complete code weight profile | [Codes and leakage](science/codes_and_leakage.md) |
| Minimum secret basis seed | Optimal asymptotic rate **0.2284467 bits per qubit**, with explicit finite-size bounds | [Seed rate](science/codes_and_leakage.md#optimal-secret-basis-rate) |
| Retained positions and noise | One dual-code certificate controls every subset; agreed-error threshold **14.6447%** with the sharp asymptotic exponent | [Noise and loss](science/noise_and_loss.md) |
| Quantum basis side information | A counterexample to the additive extension proposed in Fehr–Salvail Remark 3 | [Quantum side information](science/quantum_side_information.md) |
| Encryption and authentication | Exact random-message recovery, an inherited one-bit compiler application, and a sharper noiseless key-recycling analysis | [Encryption](science/applications.md) and [key recycling](science/key_recycling.md) |

The exact code identity is

```math
\omega(C)=2^{-k}W_C(1/\sqrt2)=\beta^nW_R(\kappa).
```

For a uniformly sampled public $`k`$-dimensional code,

```math
\mathbb E_C\omega(C)
=\beta^n+\frac{2^{n-k}-1}{2^n-1}(1-\beta^n)
\le\beta^n+2^{-k}.
```

Every basis source supported on at most $`2^k`$ strings has value at least $`\max\{\beta^n,2^{-k}\}`$. The two bounds determine the optimal exponent and the basis-seed threshold

```math
\alpha=-\log_2\beta=0.228446696836388\ldots.
```

This average already allows the attacker to know and adapt to the public code. A separate high-probability bound controls a fixed setup: if $`k\ge\alpha n+2t`$, all but a fraction $`2^{-t}`$ of codes satisfy $`W_R(\kappa)\le1+2^{-t}`$. That same certificate applies to all retained subsets, without an additional union bound.

## Read the science

Start with the [scientific map](science/README.md) and [models](science/model.md). The main proof route is **spectral value → physical attainment → code identity → optimal seed rate → uniform noise/loss certificate**. The [resource interpretation](science/interpretation.md) connects these statements to their cryptographic costs.

The exact independent-basis BB84 value and projector-overlap method are prior work of Tomamichel, Fehr, Kaniewski and Wehner. Fehr and Salvail already use coded bases, and their intermediate proof contains the linear-code upper bound before a minimum-distance relaxation. The [related-work account](references/RELATED_WORK.md) and [bibliography](references/references.bib) distinguish these ingredients from the exact attainability and resource conclusions developed here.

[The LLM reading guide](llms.txt) maps questions to the canonical statements and proofs.

## Reproduce the finite checks

From the repository root, install the documented dependency and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification account](verification/README.md) identifies the small instances, algebraic identities, physical POVM normalization and constants checked by the suite. Numerical agreement verifies implementations and examples; the written arguments establish the all-dimension theorems and asymptotic claims.

## Scope and resources

The optimal rate counts **secret basis bits**. A perfectly private one-time $`n`$-bit encryption scheme additionally needs an independent $`n`$-bit pad. The distinct one-bit compiler application uses an $`n`$-bit secret inner-product mask and imports its search-to-prediction reduction from Coladangelo–Liu–Xie.

Public dense generators require $`O(nk)`$ storage and classical encoding work. Honest quantum operations are single-qubit BB84 operations. The core is information theoretic and assumes no QRAM or computational hardness. Efficient sampling does not imply efficient exact weight-enumerator certification, and the mathematically optimal adversarial measurement need not be efficient.

The sharp noise result requires agreement of the accepted answers. Adversarial losses require basis-independent subnormalized branches, as supplied by source replacement for honest uniform BB84 inputs before basis revelation. Arbitrary quantum basis leakage and basis-dependent postselection change the model. The side-information counterexample concerns adversarial referee preparation and is not a break of the proved Fehr–Salvail protocol.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
