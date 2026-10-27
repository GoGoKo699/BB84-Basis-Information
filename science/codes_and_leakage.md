# Linear bases, leakage and the optimal seed rate

[Spectral theorem](spectral_value.md) · [Noise and loss](noise_and_loss.md) · [Resource interpretation](interpretation.md)

The exact spectral value becomes an explicit weight-enumerator identity when the bases form a linear space. Its dual form isolates the penalty caused by basis correlations and gives a sharp random-code analysis.

## Exact code formula

Let $`C\le\mathbb F_2^n`$ have dimension $`k`$, let $`R=C^\perp`$, and choose the basis uniformly from $`C`$ or an affine coset $`a+C`$.

**Theorem C.** In both the abstract BB84 game and the honest uniform-string splitting experiment,

```math
\boxed{\omega(a+C)=2^{-k}W_C(1/\sqrt2)
=\beta^nW_R(\kappa).}
```

The constants are $`\beta=(1+1/\sqrt2)/2`$ and $`\kappa=(1-\beta)/\beta`$. The full weight profile determines the value; minimum distance alone generally loses information.

### Constant row sums

For the uniform distribution on $`C`$, the spectral matrix has entries $`2^{-k}c^{|\theta+\phi|}`$. Translation by a codeword permutes $`C`$, so every row sum equals

```math
2^{-k}\sum_{z\in C}c^{|z|}=2^{-k}W_C(c).
```

The all-ones vector is an eigenvector with that eigenvalue, and the maximum absolute row sum bounds every eigenvalue. [Theorem S](spectral_value.md) therefore gives the first equality. Translating the code preserves all Hamming distances, so the value is identical for every affine coset. In the frame representation the translation conjugates by $`H^a`$.

An explicit normalized top frame eigenvector is

```math
|\psi_C\rangle=
\frac{\sum_{\theta\in C}|0^\theta\rangle}
{\sqrt{|C|W_C(1/\sqrt2)}}.
```

The numerator has squared norm $`|C|W_C(1/\sqrt2)`$, and the frame operator multiplies it by $`W_C(1/\sqrt2)/|C|`$. Inserting this vector into the [Pauli measurement](bb84_cloning.md#pauli-covariant-measurement) specifies a matching physical attack. This expression does not imply efficient preparation of the collective measurement.

### Fourier proof of the dual form

The standard binary character identity is

```math
\mathbf1_C(x)=\frac1{|R|}\sum_{r\in R}(-1)^{r\cdot x}.
```

Inserting it into the weight sum and factoring coordinatewise gives

```math
\begin{aligned}
W_C(t)
&=\frac1{|R|}\sum_{r\in R}\sum_{x\in\mathbb F_2^n}
(-1)^{r\cdot x}t^{|x|}\\
&=\frac1{|R|}\sum_{r\in R}(1-t)^{|r|}(1+t)^{n-|r|}\\
&=\frac{(1+t)^n}{|R|}
W_R\!\left(\frac{1-t}{1+t}\right).
\end{aligned}
```

This is the binary MacWilliams identity, included here with its elementary proof. Since $`|C||R|=2^n`$, setting $`t=c=1/\sqrt2`$ proves the second equality.

The linear-code upper bound is already available by retaining the pairwise distances in [Fehr–Salvail's Proposition 1 proof](../references/RELATED_WORK.md#fs2017). Exact attainment and the consequences below should be read with that attribution.

## Linear syndrome leakage

Suppose $`\Theta`$ is initially uniform on $`\mathbb F_2^n`$ and a specified public full-row-rank map $`A:\mathbb F_2^n\to\mathbb F_2^\ell`$ reveals $`L=A\Theta`$ before the attack. Each posterior is a uniform affine coset of $`C=\ker A`$. The exact conditional value is independent of the revealed syndrome, hence

```math
p_{\mathrm{win}}=\omega(\ker A)
=\beta^nW_{\mathrm{row}(A)}(\kappa).
```

The attack may depend on $`L`$. In the physical formulation the encoded data remains uniform and independent of $`(\Theta,L)`$.

### Worst rank-limited leakage

For every $`\ell`$-dimensional subspace $`R`$, choose an information set of $`\ell`$ coordinates. After row reduction, each $`r\in R`$ is uniquely determined by a vector $`z\in\mathbb F_2^\ell`$ on that set and satisfies $`|r|\ge|z|`$. Because $`0\le\kappa\le1`$,

```math
W_R(\kappa)\le\sum_{z\in\mathbb F_2^\ell}\kappa^{|z|}
=(1+\kappa)^\ell=\beta^{-\ell}.
```

Thus

```math
\max_{\mathrm{rank}\,A=\ell}p_{\mathrm{win}}=\beta^{n-\ell}.
```

Revealing $`\ell`$ individual basis coordinates attains this maximum. This worst-case bound also follows by retaining an information set and applying ordinary BB84 parallel repetition. The new rate conclusion below concerns honestly sampled dense linear spaces, not all maps of a given rank.

### A small comparison

For $`n=3`$, revealing one coordinate gives $`\beta^2\approx0.728553`$. Revealing the parity of all three bases instead gives

```math
C=\{000,011,101,110\},\qquad R=\{000,111\},
\qquad \omega(C)=\frac{1+3c^2}{4}=\frac58.
```

Both disclosures contain one classical bit. Their operational effects differ because the location of low-weight vectors in the row space differs. For a single parity on $`w`$ coordinates, with $`1\le w\le n`$, the exact value is $`\beta^n(1+\kappa^w)`$.

## Exact mean of a random code

Sample $`C`$ uniformly from the $`k`$-dimensional subspaces of $`\mathbb F_2^n`$. Its dual is a uniform $`(n-k)`$-dimensional subspace. Symmetry and counting show that any fixed nonzero vector belongs to the dual with probability

```math
p_{n,k}=\frac{2^{n-k}-1}{2^n-1}.
```

Indeed, every dual contains exactly $`2^{n-k}-1`$ nonzero vectors and all $`2^n-1`$ possible nonzero vectors have the same inclusion probability.

**Theorem R.** The optimized value averaged over public setup is exactly

```math
\boxed{\mathbb E_C\omega(C)
=\beta^n+p_{n,k}(1-\beta^n)
\le\beta^n+2^{-k}.}
```

To prove it, separate the zero dual word and use

```math
\sum_{r\in\mathbb F_2^n}\kappa^{|r|}
=(1+\kappa)^n=\beta^{-n}.
```

Then $`\mathbb E[W_R(\kappa)-1]=p_{n,k}(\beta^{-n}-1)`$, which gives the displayed formula after multiplication by $`\beta^n`$.

The attacker knows the public code and can choose a different optimal strategy for each code. The expectation is taken **after optimizing each fixed code**, so public revelation of the setup does not invalidate the result.

## A high-probability certificate

Put $`\alpha=-\log_2\beta=0.228446696836388\ldots`$. Markov's inequality applied to the nonnegative dual excess gives, for every $`\varepsilon>0`$,

```math
\boxed{\Pr_C[W_R(\kappa)>1+\varepsilon]
\le\frac{p_{n,k}(\beta^{-n}-1)}{\varepsilon}
\le\varepsilon^{-1}2^{\alpha n-k}.}
```

In particular, for $`t>0`$ and an integer $`k\ge\alpha n+2t`$ with $`k\le n`$, all but a fraction $`2^{-t}`$ of public codes satisfy

```math
W_R(\kappa)\le1+2^{-t},\qquad
\omega(C)\le(1+2^{-t})\beta^n.
```

The same certificate controls **every retained subset and every relevant noise moment**, as proved in [noise and loss](noise_and_loss.md). The bad-setup probability is distinct from conditional attack success for a good code. If the setup remains part of the security experiment, use the exact ensemble mean instead of silently treating a high-probability property as certain.

## Optimal secret basis rate

Every basis source supported on at most $`2^k`$ strings has two universal attacks:

- Guess its most likely basis, giving success at least $`\max_\theta\mu(\theta)\ge2^{-k}`$.
- Use a product Breidbart strategy, giving success $`\beta^n`$ for every basis distribution.

Both attacks are physical splitting attacks. Therefore

```math
\omega(\mu)\ge\max\{2^{-k},\beta^n\}.
```

The random-code mean is at most the sum of these two quantities. A deterministic code attaining at most the mean also exists. Hence the best value for a source with $`k`$ seed bits is determined within a factor of two:

```math
\max\{2^{-k},\beta^n\}
\le\inf_{|\mathrm{supp}\,\mu|\le2^k}\omega(\mu)
\le\beta^n+2^{-k}.
```

Equivalently, the optimal exponential rate is $`\min\{k\ln2,-n\ln\beta\}`$. To retain the full independent-basis exponent, one needs $`k\ge\alpha n-o(n)`$; random linear bases achieve that exponent with $`k=\alpha n+o(n)`$ and nonnegative slack. For a multiplicative factor tending to one with high probability, choose slack tending to infinity, for example $`k\ge\alpha n+2t_n`$ with $`t_n\to\infty`$ and $`t_n=o(n)`$.

Thus the optimal asymptotic secret basis rate in this family is

```math
\boxed{\alpha=0.228446696836388\ldots\quad\text{bits per qubit}.}
```

The equivalent dense-syndrome interpretation allows asymptotic rank fraction $`1-\alpha\approx0.7715533`$ while preserving the original exponent for an honestly sampled map. Coordinate leakage demonstrates why this is not an arbitrary-leakage guarantee.

## Setup and efficiency

Uniformly sampling an $`n\times k`$ binary matrix conditioned on full column rank gives a uniform $`k`$-dimensional image: every subspace has the same number of ordered bases. Rank testing and dense encoding are polynomial-time classical operations; storage and each basis-generation multiplication cost $`O(nk)`$. Rejection sampling has bounded expected repetitions, since the full-rank probability is $`\prod_{j=0}^{k-1}(1-2^{j-n})`$, bounded away from zero for $`k\le n`$.

The setup must be sampled according to the stated distribution. A malicious setup provider could select a poor code. This account does not claim an efficient method to certify the exact weight enumerator of an arbitrary large code or an explicit deterministic family at the optimal rate.

Basis-seed optimality does not imply optimal total encryption key length. The perfectly private full-message application also uses an independent $`n`$-bit pad; see [applications](applications.md).
