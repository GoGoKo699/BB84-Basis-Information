# Quantum basis information can prepare a winning state

[Models](model.md) · [Classical syndrome leakage](codes_and_leakage.md#linear-syndrome-leakage) · [Related work](../references/RELATED_WORK.md#fs2017)

The exact spectral theorem assumes that the initial tripartite state is independent of the basis. Classical leakage can be handled by conditioning on the resulting basis distribution. A quantum register correlated with the basis can have a different effect: it may supply a correctly aligned state without allowing the basis to be identified.

## The proposed additive bound

[Fehr–Salvail, Corollaries 1–2 and Remark 3](../references/RELATED_WORK.md#fs2017), consider a cq state $`\rho_{\Theta E}`$ with $`\Theta`$ taking values in a basis code $`C`$. A channel $`\mathcal Q:E\to ABD`$ prepares the referee and player systems. After the referee's BB84 measurement, the players receive the basis and try to guess the outcome.

Write

```math
g=P_{\mathrm{guess}}(\Theta|E)
=\max_{\{M_\theta\}}
\sum_\theta p_\theta\mathrm{Tr}(M_\theta\rho_E^\theta).
```

Their proved bound is $`g(1+|C|2^{-d(C)/2})`$. Remark 3 establishes an improvement for **classical** $`E`$ and asks whether the same expression also holds for quantum $`E`$:

```math
p_{\mathrm{win}}\stackrel{?}{\le}g+2^{-d(C)/2}.
```

The construction below refutes this proposed extension in its stated generality. It does not refute the proved multiplicative bound or the authentication protocol.

## A perfect winning strategy

Take a uniform basis on any code $`C`$ and the cq state

```math
\rho_{\Theta E}
=\frac1{|C|}\sum_{\theta\in C}
|\theta\rangle\langle\theta|\otimes
|0^\theta\rangle\langle0^\theta|_E.
```

The channel forwards the $`n`$-qubit register $`E`$ unchanged to the referee as $`A`$. The players retain trivial registers and always answer $`0^n`$. Measuring $`|0^\theta\rangle`$ in basis $`\theta`$ returns $`0^n`$ with certainty. Therefore

```math
\boxed{p_{\mathrm{win}}=1.}
```

No classical description of $`\theta`$ is needed by the channel. The quantum register is used directly as a state in the appropriate basis.

## Exact discrimination on the full cube

For $`C=\mathbb F_2^n`$, the basis-guessing task is discrimination of an independent product ensemble with one-qubit states $`\rho_0=|0\rangle\langle0|`$ and $`\rho_1=|+\rangle\langle+|`$, each with probability one half.

For one qubit define

```math
Y=\frac14(\rho_0+\rho_1+|\rho_0-\rho_1|).
```

The operator inequalities $`|A|\ge A`$ and $`|A|\ge-A`$ for Hermitian $`A`$ show that $`Y\ge\rho_0/2`$ and $`Y\ge\rho_1/2`$. Also $`\mathrm{Tr}\,Y=(2+\sqrt2)/4=\beta`$.

Tensor products preserve these positive-operator inequalities, so for every $`\theta`$,

```math
Y^{\otimes n}\ge2^{-n}|0^\theta\rangle\langle0^\theta|.
```

For any discrimination POVM,

```math
2^{-n}\sum_\theta
\mathrm{Tr}(M_\theta|0^\theta\rangle\langle0^\theta|)
\le\sum_\theta\mathrm{Tr}(M_\theta Y^{\otimes n})
=\beta^n.
```

The product of the optimal one-qubit Helstrom measurements attains that value. Hence

```math
\boxed{P_{\mathrm{guess}}(\Theta|E)=\beta^n.}
```

This is an explicit dual certificate and a matching measurement, rather than an assumption that state-discrimination optima always multiply.

The full cube has minimum distance one. At $`n=8`$, the proposed additive right side is

```math
\beta^8+2^{-1/2}=0.9888448508760549\ldots<1,
```

already contradicting the perfect winning probability.

## Positive rate and linear distance

The separation can also make both terms in the proposed bound exponentially small. For any subset $`C\subseteq\mathbb F_2^n`$ of size $`2^k`$, extend a POVM for the restricted ensemble by assigning zero effects to all labels outside $`C`$. The full-cube discrimination probability is $`2^{k-n}`$ times the restricted probability. The preceding upper bound therefore gives

```math
P_{\mathrm{guess},C}(\Theta|E)
\le2^{n-k}\beta^n.
```

Choose $`k=\lfloor0.9n\rfloor`$. A random $`k`$-dimensional binary code has expected number of nonzero words of weight below $`0.01n`$ at most

```math
\frac{2^k-1}{2^n-1}
\sum_{1\le j<0.01n}\binom nj
\le2^{1-[0.1-h_2(0.01)]n}.
```

Since $`h_2(0.01)=0.0807931358959\ldots<0.1`$, the expectation tends to zero. For all sufficiently large $`n`$, codes exist with that dimension and $`d(C)\ge0.01n`$. For these codes,

```math
P_{\mathrm{guess},C}(\Theta|E)
\le2\cdot2^{-0.128446696836388\ldots n},
\qquad
2^{-d(C)/2}\le2^{-0.005n},
```

while $`p_{\mathrm{win}}=1`$ remains exact.

## Interpretation and scope

The construction uses $`n`$ qubits of quantum side information and an adversarial referee-preparation channel. It is a separation between identifying the basis and using quantum information aligned with it. It is not an attack achieving perfect recovery of an honest unknown uniform BB84 message.

The high-rate example does not lie in Fehr–Salvail's motivating low-rate regime where distance is much larger than code dimension. The proposed extension, as stated, does not impose that restriction. The finite full-cube example and the positive-distance family refute the unqualified expression; they do not settle every possible restricted reformulation.

The proved multiplicative bound remains consistent: its factor can be large in these examples. Likewise, there is no contradiction with [Theorem S](spectral_value.md), whose basis-independence hypothesis is absent here.

The [key-recycling application](key_recycling.md) retains quantum side information through a multiplicative factor $`g|C|\omega(C)`$; it never substitutes the false additive expression.
