# One code certificate for every retained subset

[Codes and leakage](codes_and_leakage.md) · [Models](model.md) · [Applications](applications.md)

Let bases be uniform on a binary linear code $`C`$, with dual $`R`$. The exact code value controls more than complete-string recovery. A single bound on $`W_R(\kappa)`$ simultaneously controls every retained coordinate set, without a union bound over those sets.

## Projection and shortening

For $`S\subseteq[n]`$, the projection $`C|_S`$ is a linear space. A uniform codeword projects uniformly because every fiber has the same size. Its dual is the shortened code

```math
R_S=\{r|_S:r\in R,\ \operatorname{supp}r\subseteq S\}.
```

To verify this identity, a vector on $`S`$ is orthogonal to all projected codewords exactly when its zero extension is orthogonal to $`C`$. Shortening, rather than simply projecting the dual, is the relevant operation.

Let $`W_i=\mathbf1[x_i=b_i=d_i]`$. Then every strategy obeys

```math
\mathbb E\prod_{i\in S}W_i
\le\omega(C|_S)
=\beta^{|S|}W_{R_S}(\kappa).
```

### Why knowledge of unused basis bits does not break this bound

The players receive the full basis, while the projected game appears to disclose only $`\theta|_S`$. Trace out the referee's unused registers; the remaining state $`\rho_{A_SBD}`$ is fixed independently of the full basis. Marginalize each player's output POVM to coordinates in $`S`$.

For a fixed used basis $`a=\theta|_S`$, every unused-basis context merely selects a pair of local POVMs on the **same state**. Each choice has success at most the supremum over all local POVM pairs for that $`a`$. Choices for different $`a`$ are independent strategic choices, so their suprema, or arbitrary approximations to them, constitute a valid projected-game strategy. Averaging over the uniform projected distribution is bounded by its optimal value.

This argument does not condition the quantum state on unused basis bits and does not assume independent wins or coordinatewise player measurements.

## Exact form of a moment upper bound

For a retained set $`J`$ of size $`h`$, put $`L_J=h-\sum_{i\in J}W_i`$. Define, for $`0\le s\le1`$,

```math
a_s=\beta+q_*s,\qquad b_s=q_*(1-s).
```

**Theorem N.** Every strategy satisfies

```math
\boxed{\mathbb E[s^{L_J}]
\le a_s^hW_{R_J}(b_s/a_s).}
```

At $`s=0`$, interpret the left side as the probability $`L_J=0`$, or take the limit from positive $`s`$.

### Proof by positive coefficients

Because $`s^{1-W_i}=s+(1-s)W_i`$,

```math
\mathbb E[s^{L_J}]
=\sum_{T\subseteq J}s^{h-|T|}(1-s)^{|T|}
\mathbb E\prod_{i\in T}W_i.
```

Every coefficient is nonnegative. Substitute the projected-game bound and identify shortened words with their zero extensions in $`J`$:

```math
\begin{aligned}
\mathbb E[s^{L_J}]
&\le\sum_{T\subseteq J}s^{h-|T|}[\beta(1-s)]^{|T|}
\sum_{r\in R_J:\operatorname{supp}r\subseteq T}\kappa^{|r|}\\
&=\sum_{r\in R_J}\kappa^{|r|}
\sum_{T:\operatorname{supp}r\subseteq T\subseteq J}
s^{h-|T|}[\beta(1-s)]^{|T|}\\
&=\sum_{r\in R_J}[\kappa\beta(1-s)]^{|r|}
[s+\beta(1-s)]^{h-|r|}\\
&=a_s^hW_{R_J}(b_s/a_s).
\end{aligned}
```

This is a moment **upper bound**. Exact saturation of every term by a common strategy is not required and is not claimed.

## Uniform certificate

Suppose the fixed code satisfies

```math
W_R(\kappa)\le1+\varepsilon.
```

Every shortened code is a subset of $`R`$ after zero extension, preserving weights. Also $`0\le b_s/a_s\le\kappa`$. Consequently, simultaneously for all $`J`$ and all $`s\in[0,1]`$,

```math
\boxed{\mathbb E[s^{L_J}]
\le(1+\varepsilon)(\beta+q_*s)^{|J|}.}
```

The [random-code estimate](codes_and_leakage.md#a-high-probability-certificate) supplies this single certificate with explicit high probability. There is no additional cost for the number of subsets.

## Agreed-error acceptance and the sharp exponent

Suppose acceptance requires $`b|_J=d|_J`$ and $`d_H(x|_J,b|_J)\le r`$. Acceptance then implies $`L_J\le r`$. For $`0<s\le1`$,

```math
\Pr[\mathrm{accept}]
\le s^{-r}\mathbb E[s^{L_J}]
\le s^{-r}a_s^hW_{R_J}(b_s/a_s).
```

With the uniform certificate and $`\gamma=r/h<q_*`$, minimizing the right side uses

```math
s_* =\frac{\gamma\beta}{q_*(1-\gamma)}
```

and gives

```math
\boxed{\Pr[\mathrm{accept}]
\le\min\{1,(1+\varepsilon)e^{-hD(\gamma\|q_*)}\}.}
```

For $`\gamma=0`$, use $`s\downarrow0`$. If the specified tolerance is $`\gamma_0h`$, choose $`r=\lfloor\gamma_0h\rfloor`$ and $`\gamma=r/h`$ for the slightly sharper integer-radius result.

A product Breidbart strategy returns identical answers to both players. Conditional on any full basis string, its coordinate errors are independent with probability $`q_*`$, which is the same for every basis string. Thus its unconditional errors are also independent Bernoulli variables. For any fixed $`0\le\gamma<q_*`$, its lower-tail probability has exponent $`D(\gamma\|q_*)`$. The theorem therefore retains the optimal asymptotic exponent whenever $`\log(1+\varepsilon)=o(h)`$.

The threshold is

```math
q_* =\sin^2(\pi/8)=0.146446609406726\ldots.
```

At or above this error fraction, the Breidbart strategy prevents an exponentially vanishing guarantee of this form. The result does not assert an exact finite-block binomial-tail optimum.

Without agreement, two separately tolerated Hamming errors of radius $`r`$ imply only $`L_J\le2r`$. The argument then gives a bound using $`2r/h`$, when it is below $`q_*`$; the sharp unrestricted separate-error problem is not solved here.

## Loss commitments and subnormalized branches

Let $`Z`$ be a branch label, with retained set $`J_z`$, and suppose that before the basis is revealed the joint state has the form

```math
\rho_{\Theta ZABD}
=\sum_{\theta,z}\mu_C(\theta)
|\theta,z\rangle\langle\theta,z|\otimes\widetilde\rho^z_{ABD},
\qquad
\sum_z\operatorname{Tr}\widetilde\rho^z_{ABD}\le1.
```

Every subnormalized branch is independent of $`\Theta`$. Both players may know $`z`$. Apply the normalized theorem to each branch and multiply by its trace. If every accepted branch has $`|J_z|\ge h_0`$ and relative error tolerance at most $`\gamma<q_*`$, then

```math
\boxed{\Pr[\mathrm{accept}]
\le\min\{1,(1+\varepsilon)e^{-h_0D(\gamma\|q_*)}\}.}
```

Rejected or aborted branches need not have total trace one. Their weights are not divided out: the bound is for unconditional acceptance, rather than success conditioned on a rare postselection event.

### When the branch condition is satisfied

For honest uniform-string BB84 preparation and no additional basis-correlated side information, defer the referee's EPR measurement as in [source replacement](bb84_cloning.md#upper-bound-by-source-replacement). Any instrument acting before basis disclosure produces a fixed collection $`\widetilde\rho^z`$ independent of the later measurement basis, even though its branch label may depend on the encoded data. This proves the required condition.

The same reasoning works after fixing a disclosed classical syndrome: translate the affine basis coset and apply the theorem to its linear part. The attacker may choose its instrument according to the already disclosed syndrome.

Timing alone is insufficient if an attacker already has other information correlated with the unexposed basis. In particular, basis-dependent postselection does not satisfy the displayed factorization. Position-verification constructions with partial classical inputs require their own fixed-input/random-function reduction; the branch theorem is not a substitute for that reduction.

The general use of instruments and subnormalized branches in loss-tolerant position verification is credited in [related work](../references/RELATED_WORK.md#loss2026). The contribution here is the single code certificate that controls all retained subsets and noise parameters.
