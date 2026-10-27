# Exact value for correlated choices of two projective measurements

[Models](model.md) · [Physical BB84 splitting](bb84_cloning.md) · [Codes and leakage](codes_and_leakage.md)

## Theorem: one scalar matrix gives the exact value

Use the abstract game and the unsquared overlap $`c=c(P,Q)`$ from [the model](model.md#abstract-game). For any distribution $`\mu`$ on $`\{0,1\}^n`$, form the matrix indexed by its support,

```math
(K_\mu)_{\theta,\phi}
=\sqrt{\mu(\theta)\mu(\phi)}\,c^{d_H(\theta,\phi)}.
```

**Theorem S.** For any pair of finite-dimensional PVMs, including higher-rank projectors and different outcome alphabets,

```math
\boxed{\omega^*(\mu;P,Q)=\lambda_{\max}(K_\mu).}
```

The maximum is attained with trivial player quantum registers and deterministic answers depending on the question. The optimal referee state may be entangled across its $`n`$ registers. The result allows arbitrary correlations in $`\mu`$ and arbitrary collective player strategies.

The proof combines the established monogamy projector-overlap argument with a weighted block-Gram comparison and a matching family of principal vectors. The [related-work account](../references/RELATED_WORK.md) identifies the inherited ingredients and the nonuniform two-question problem.

## Upper bound

### A common projective dilation

There are finitely many possible question strings. Every local POVM can be dilated on a common enlarged player space with one fixed ancilla state: choose a sufficiently large outcome register, implement each POVM by its own unitary, and conjugate the computational-basis projections by that unitary. The initial ancilla embedding is the same for all questions. Thus one may take the player effects $`B_x^\theta,D_x^\theta`$ to be projections without changing the outcome probabilities. This does not assert that the different question measurements commute.

For each question define the winning projector

```math
\Pi_\theta=
\sum_xF_x^\theta\otimes B_x^\theta\otimes D_x^\theta.
```

The summands are orthogonal projections. A fixed strategy succeeds with probability

```math
\operatorname{Tr}\!\left[\rho_{ABD}
\sum_\theta\mu(\theta)\Pi_\theta\right].
```

### Pairwise overlap of winning subspaces

For two questions introduce larger projections

```math
S_\theta=\sum_xF_x^\theta\otimes B_x^\theta\otimes I_D,
\qquad
T_\phi=\sum_yF_y^\phi\otimes I_B\otimes D_y^\phi.
```

Since $`\Pi_\theta\le S_\theta`$ and $`\Pi_\phi\le T_\phi`$,

```math
\Pi_\theta\Pi_\phi
=\Pi_\theta S_\theta T_\phi\Pi_\phi,
\qquad
\|\Pi_\theta\Pi_\phi\|_\infty
\le\|S_\theta T_\phi\|_\infty.
```

The product on the right is block diagonal on the mutually orthogonal player subspaces $`B_x^\theta\otimes D_y^\phi`$, with referee blocks $`F_x^\theta F_y^\phi`$. Tensor-product multiplicativity of the operator norm gives

```math
\|\Pi_\theta\Pi_\phi\|_\infty
\le\max_{x,y}\|F_x^\theta F_y^\phi\|_\infty
\le c^{d_H(\theta,\phi)}.
```

A coordinate with the same measurement contributes at most one, and a coordinate with different measurements contributes at most $`c`$. Higher projector rank causes no change. This is the overlap step inherited from [TFKW](../references/RELATED_WORK.md#tfkw2013).

### Weighted block-Gram comparison

Write $`\mathcal V=A\otimes B\otimes D`$ and define

```math
T:\bigoplus_\theta\mathcal V\longrightarrow\mathcal V,
\qquad
T((v_\theta)_\theta)=\sum_\theta\sqrt{\mu(\theta)}\Pi_\theta v_\theta.
```

Then $`TT^\dagger=\sum_\theta\mu(\theta)\Pi_\theta`$. For any block vector $`v`$, the overlap inequality and Cauchy–Schwarz imply

```math
\begin{aligned}
\langle v,T^\dagger Tv\rangle
&\le\sum_{\theta,\phi}
\sqrt{\mu(\theta)\mu(\phi)}\,
c^{d_H(\theta,\phi)}\|v_\theta\|\|v_\phi\|\\
&\le\lambda_{\max}(K_\mu)\sum_\theta\|v_\theta\|^2.
\end{aligned}
```

The first line bounds absolute values of the summands if necessary. Therefore

```math
\left\|\sum_\theta\mu(\theta)\Pi_\theta\right\|_\infty
=\|T^\dagger T\|_\infty
\le\lambda_{\max}(K_\mu).
```

This bounds every state and every local strategy.

## Attainment by principal vectors

Choose outcomes $`a_0,b_0`$ attaining $`\|P_{a_0}Q_{b_0}\|=c`$. There are unit vectors

```math
u\in\operatorname{ran}P_{a_0},\qquad
v\in\operatorname{ran}Q_{b_0},\qquad
\langle u,v\rangle=c.
```

For example, take a unit top eigenvector $`v`$ of $`Q_{b_0}P_{a_0}Q_{b_0}`$ in $`\operatorname{ran}Q_{b_0}`$, with eigenvalue $`c^2`$, and put $`u=P_{a_0}v/c`$. This also handles $`c=1`$.

Let $`w_0=u,w_1=v`$ and $`w_\theta=\bigotimes_iw_{\theta_i}`$. Both players answer $`a_0`$ in every zero-question coordinate and $`b_0`$ in every one-question coordinate. The success projection $`F_{f(\theta)}^\theta`$ contains $`w_\theta`$, so

```math
F_{f(\theta)}^\theta\ge|w_\theta\rangle\langle w_\theta|.
```

The weighted vectors $`\sqrt{\mu(\theta)}w_\theta`$ have Gram matrix exactly $`K_\mu`$, because $`\langle w_\theta,w_\phi\rangle=c^{d_H(\theta,\phi)}`$. Their frame operator

```math
M_\mu=\sum_\theta\mu(\theta)|w_\theta\rangle\langle w_\theta|
```

has the same nonzero eigenvalues as $`K_\mu`$. Preparing a top eigenvector of $`M_\mu`$ gives success at least $`\lambda_{\max}(K_\mu)`$. The upper bound makes this an equality and completes the proof.

The positive simultaneous overlaps are essential to this attainment argument. For an arbitrary family of three or more measurements, a matrix of pairwise maximum overlaps need not be jointly attainable. The theorem also does not extend the referee PVMs to arbitrary POVMs.

## BB84 form

For BB84 one may choose $`u=|0\rangle`$, $`v=|+\rangle`$. In this rank-one case the success projection is precisely the chosen frame projection, giving

```math
\boxed{\omega(\mu)=\lambda_{\max}(K_\mu)
=\left\|\sum_\theta\mu(\theta)|0^\theta\rangle\langle0^\theta|\right\|_\infty.}
```

This equality is the entry point for the [matching physical attack](bb84_cloning.md).

## Independent biased questions

If coordinate $`i`$ uses $`P`$ with probability $`t_i`$ independently, then $`K_\mu`$ is a tensor product of two-by-two matrices

```math
K_i=
\begin{pmatrix}
t_i&c\sqrt{t_i(1-t_i)}\\
c\sqrt{t_i(1-t_i)}&1-t_i
\end{pmatrix}.
```

Consequently

```math
\omega^*(\mu;P,Q)
=\prod_{i=1}^n
\frac{1+\sqrt{(2t_i-1)^2+4t_i(1-t_i)c^2}}2.
```

With a common bias $`t`$, this is exact strong parallel repetition of the biased one-coordinate value. It covers the nonuniform two-projective-question case identified in [Russo's Question 7.2](../references/RELATED_WORK.md#russo2017). The separate general-POVM question remains outside the result.

For uniform independent BB84 bases, $`t_i=1/2`$ and the value reduces to the established $`\beta^n`$.

## A correlated example

Take $`\mu(00)=\mu(11)=1/2`$ and zero elsewhere. Each individual basis bit is uniform, but the two are equal. Then

```math
K_\mu=\frac12
\begin{pmatrix}1&c^2\\c^2&1\end{pmatrix},
\qquad \omega(\mu)=\frac{1+c^2}{2}=\frac34.
```

Independent uniform bases instead give $`\beta^2\approx0.728553`$. Identical one-coordinate marginals therefore do not determine the security value. The full distribution enters the spectral matrix.

The [verification suite](../verification/README.md) checks nonuniform examples and a higher-rank PVM construction. Those finite checks validate implementations; the argument above establishes the general result.
