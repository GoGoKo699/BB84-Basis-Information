# Models and the security question

[Scientific route](README.md) · [Exact spectral value](spectral_value.md) · [Physical BB84 splitting](bb84_cloning.md)

## What information about the basis matters?

BB84 encodes a bit in either the computational basis or the Hadamard basis. A recipient who learns the basis can recover the bit from the qubit. The cryptographic obstruction appears when an adversary must divide the qubit between two separated recipients **before** learning the basis, and both recipients must later recover the bit.

For independent uniform bases, the optimal probability that both recipients recover an entire $`n`$-bit string is $`\beta^n`$, where

```math
c=\frac1{\sqrt2},\qquad
\beta=\frac{1+c}{2}=\cos^2\frac\pi8,
\qquad q_*=1-\beta,
\qquad \kappa=\frac{q_*}{\beta}=3-2\sqrt2.
```

This independent-basis result and its basic projector argument are established by [Tomamichel, Fehr, Kaniewski and Wehner](../references/RELATED_WORK.md#tfkw2013). The question here is how the **whole distribution of bases**, including correlations and leaked linear information, determines the security value. A second question is how few secret basis bits retain the independent-basis exponent.

There are three different experiments. Their distinctions determine which conclusions can be transferred.

| Experiment | State supplied before basis revelation | Condition on the basis | Result |
|---|---|---|---|
| Abstract monogamy game | Arbitrary tripartite state supplied by the players | State independent of the sampled basis | Exact two-PVM spectral formula |
| Physical BB84 splitting | Honest uniform string encoded as BB84 qubits, then split | Basis distributed as specified; string uniform and independent | Same exact BB84 value, with a matching physical attack |
| Quantum basis side information | A channel receives a quantum register correlated with the basis and supplies the referee's state | Independence deliberately absent | Counterexample to a proposed additive leakage bound |

Here a PVM is a projective-valued measurement: a finite family of orthogonal projections summing to the identity. A POVM has positive effects summing to the identity and need not be projective.

## Abstract game

Fix two PVMs $`\{P_a\}_{a\in\mathcal A}`$ and $`\{Q_b\}_{b\in\mathcal B}`$ on a nonzero finite-dimensional Hilbert space $`\mathcal H`$. Their outcome alphabets and projector ranks may differ. Write

```math
c(P,Q)=\max_{a,b}\|P_aQ_b\|_\infty\in(0,1].
```

The norm is the operator norm. It is the **unsquared** overlap; some literature instead calls its square the measurement overlap.

The referee holds $`A=\mathcal H^{\otimes n}`$. Bob and Charlie may hold arbitrary finite-dimensional registers $`B,D`$; the letter $`D`$ avoids confusing Charlie's register with a binary code $`C`$.

1. The players prepare any density operator $`\rho_{ABD}`$ and deliver $`A`$ to the referee. They retain $`B`$ and $`D`$ and subsequently cannot communicate.
2. Independently of this state, the referee samples $`\theta\in\{0,1\}^n`$ from a specified distribution $`\mu`$. Coordinates of $`\theta`$ may be arbitrarily correlated and biased.
3. The referee measures coordinate $`i`$ with $`P`$ if $`\theta_i=0`$ and with $`Q`$ if $`\theta_i=1`$. Write $`F_x^\theta`$ for the corresponding product outcome projection.
4. Both players receive the entire string $`\theta`$ and use arbitrary local POVMs to return outcome strings $`b,d`$.
5. They win exactly when $`x=b=d`$.

Measurements may act collectively across all coordinates and depend on every bit of $`\theta`$. Shared entanglement and unlimited finite quantum memories are allowed. There is no computational restriction. The optimal success probability is $`\omega^*(\mu;P,Q)`$, or $`\omega(\mu)`$ for BB84.

For BB84, $`\mathcal H=\mathbb C^2`$ and

```math
|x^\theta\rangle=\bigotimes_{i=1}^n H^{\theta_i}|x_i\rangle,
\qquad F_x^\theta=|x^\theta\rangle\langle x^\theta|.
```

The Hadamard matrix is $`H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}`$ and $`H^0=I`$.

## Physical splitting experiment

Sample $`\Theta\sim\mu`$ and an independent uniform $`X\in\{0,1\}^n`$. Give $`|X^\Theta\rangle`$ to an arbitrary channel that distributes registers to Bob and Charlie. After distribution, disclose $`\Theta`$ to both. They cannot communicate and must both return the complete $`X`$.

The [physical attainment theorem](bb84_cloning.md) proves that this experiment has exactly the same value $`\omega(\mu)`$ as the abstract BB84 game. This equality requires a proof: the abstract game allows arbitrary referee marginals, while honest uniform BB84 preparation corresponds to a maximally mixed referee marginal. A Pauli-covariant measurement attains the abstract bound despite that restriction.

The general two-PVM spectral theorem is an abstract-game statement. The physical equality is proved here specifically for BB84, whose Pauli symmetry supplies the matching attack.

## Codes, seeds and classical leakage

Let $`C\le\mathbb F_2^n`$ be a binary linear code of dimension $`k`$, used as a **set of bases**. It is not an error-correcting encoding of the message. A public injective generator

```math
G:\mathbb F_2^k\longrightarrow\mathbb F_2^n
```

maps a uniform secret seed $`U`$ to $`\Theta=GU`$. The dual code is

```math
R=C^\perp=\{r\in\mathbb F_2^n:r\cdot c=0\text{ for every }c\in C\},
```

and the weight enumerator is $`W_C(t)=\sum_{c\in C}t^{|c|}`$.

Equivalently, start with a fully uniform basis and reveal a fixed public linear syndrome $`A\Theta`$ before the attack. Conditioned on the syndrome, the basis is uniform on an affine coset of $`\ker A`$. The attacker may adapt to the syndrome. The exact conditional and unconditional security values are given in [codes and leakage](codes_and_leakage.md).

Classical syndrome disclosure and a quantum system correlated with the basis are different resources. The [quantum-side-information separation](quantum_side_information.md) explains why small basis-guessing probability alone cannot replace the independence hypothesis.

## Errors and retained coordinates

For a retained set $`J\subseteq[n]`$, define

```math
W_i=\mathbf1[x_i=b_i=d_i],\qquad
L_J=|J|-\sum_{i\in J}W_i.
```

Thus $`L_J`$ counts coordinates where at least one player is wrong. The useful acceptance event is that the two returned strings **agree on the retained positions** and their common answer makes at most $`r`$ errors. It implies $`L_J\le r`$. Separate error tolerances without agreement imply only $`L_J\le2r`$.

For adversarially chosen retained sets, the [loss result](noise_and_loss.md#loss-commitments-and-subnormalized-branches) requires a basis-independent joint state of the branch label and quantum registers. Merely announcing a set before the basis is revealed does not prove this hypothesis. Honest uniform BB84 inputs admit the needed source-replacement argument; quantum basis leakage need not.

## Conventions and charged resources

All logarithms in relative entropy are natural; $`\log_2`$ denotes bits. Binary relative entropy is

```math
D(a\|b)=a\ln\frac ab+(1-a)\ln\frac{1-a}{1-b},
```

with the usual limiting conventions at zero. The binary entropy $`h_2`$ uses base-two logarithms.

The public generator requires $`O(nk)`$ bits to store and $`O(nk)`$ elementary binary operations to apply using a dense matrix. Honest quantum preparation and decryption use single-qubit BB84 operations. Sampling a uniformly random full-rank generator is a public randomized setup; it is distinct from the secret seed. No QRAM or computational hardness assumption enters the core results.

Optimal adversarial measurements need not have efficient implementations. Exact enumeration of a large code's weight enumerator is also not claimed efficient. The random-code theorem gives an ensemble guarantee and a high-probability certificate, not an efficient deterministic construction or universal certificate checker.

Continue with the [spectral theorem](spectral_value.md), then its [physical realization](bb84_cloning.md).
