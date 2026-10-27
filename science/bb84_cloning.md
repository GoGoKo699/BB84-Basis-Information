# A physical attack attaining the BB84 spectral value

[Models](model.md) · [Spectral theorem](spectral_value.md) · [Applications](applications.md)

## Theorem: honest preparation has the same value

In the physical experiment, an honest source prepares $`|x^\theta\rangle`$ with uniform $`x\in\{0,1\}^n`$ and independent $`\theta\sim\mu`$. An adversary splits this state, and two noncommunicating recipients then learn $`\theta`$ and must both recover $`x`$.

**Theorem B.** For every basis distribution $`\mu`$, the optimal joint recovery probability is

```math
\omega(\mu)
=\lambda_{\max}(K_\mu)
=\|M_\mu\|_\infty,
\qquad
M_\mu=\sum_\theta\mu(\theta)|0^\theta\rangle\langle0^\theta|.
```

A measurement followed by broadcasting classical data attains it. Hence allowing quantum memories at the two recipients cannot improve the optimum in this experiment.

## Upper bound by source replacement

Let $`d=2^n`$ and $`|\Phi_d\rangle=d^{-1/2}\sum_x|x\rangle|x\rangle`$. Measuring one half of $`|\Phi_d\rangle`$ in the real BB84 basis $`\theta`$ produces a uniform outcome $`x`$ and prepares $`|x^\theta\rangle`$ on the other half.

Apply the splitting channel to the second half before this referee measurement. The resulting tripartite state is independent of $`\theta`$, and the subsequent experiment has exactly the honest-source statistics. It is a strategy in the abstract monogamy game with referee marginal $`I/d`$. [Theorem S](spectral_value.md#theorem-one-scalar-matrix-gives-the-exact-value) therefore gives the upper bound.

An abstract optimal state need not have that marginal. The following construction proves that the bound is nevertheless physically attainable.

## Pauli-covariant measurement

Take a unit top eigenvector $`\psi`$ of the real symmetric matrix $`M_\mu`$. It can be chosen real. For $`u,v\in\mathbb F_2^n`$, let

```math
P_{uv}=X^uZ^v,
\qquad
E_{uv}=\frac1dP_{uv}|\psi\rangle\langle\psi|P_{uv}^\dagger.
```

Here $`X^u=\bigotimes_iX^{u_i}`$ and similarly for $`Z^v`$. The Pauli twirl identity gives

```math
\sum_{u,v}P_{uv}|\psi\rangle\langle\psi|P_{uv}^\dagger=dI,
\qquad \sum_{u,v}E_{uv}=I.
```

For completeness, the twirl kills every nonidentity Pauli coefficient of an operator and retains its identity coefficient. A trace-one operator has identity coefficient $`1/d`$; there are $`d^2`$ summands. Thus the effects are a normalized POVM.

Measure this POVM and send the classical pair $`(u,v)`$ to both recipients. On receiving $`\theta`$, each returns

```math
g_i(u,v,\theta)=
\begin{cases}
u_i,&\theta_i=0,\\
v_i,&\theta_i=1.
\end{cases}
```

## Direct success calculation

Fix $`\theta,x`$. Exactly $`d`$ pairs $`(u,v)`$ obey $`g(u,v,\theta)=x`$: in each coordinate one Pauli bit is fixed and the other is free. For each such pair,

```math
P_{uv}^\dagger|x^\theta\rangle
=e^{i\varphi}|0^\theta\rangle
```

for an irrelevant phase. The corresponding measurement probability is therefore

```math
\langle x^\theta|E_{uv}|x^\theta\rangle
=\frac1d|\langle\psi|0^\theta\rangle|^2.
```

Summing the $`d`$ successful outcomes gives $`|\langle\psi|0^\theta\rangle|^2`$. This expression is independent of $`x`$. Averaging over $`\theta`$ gives

```math
p_{\mathrm{win}}
=\sum_\theta\mu(\theta)|\langle\psi|0^\theta\rangle|^2
=\langle\psi,M_\mu\psi\rangle
=\|M_\mu\|_\infty.
```

This proves attainment using an honest input, without assuming that the adversary can choose the referee's marginal. Equivalently, in source replacement the Pauli outcomes generate the appropriate eigenstate ensemble while averaging to $`I/d`$.

## What the attack does and costs

The attack produces only classical outputs, but its POVM can be a collective measurement on all $`n`$ input qubits. It is not generally a tensor product of single-qubit measurements. Correlated bases can make $`\psi`$ entangled across coordinates.

The theorem characterizes information-theoretic security. It does not promise a polynomial-size circuit for the optimal adversarial POVM or an efficient algorithm for diagonalizing $`M_\mu`$. Honest preparation from a public linear basis generator remains efficient.

For independent uniform bases, $`\psi`$ is a product Breidbart state, with

```math
|\psi_{\mathrm B}\rangle
=\cos(\pi/8)|0\rangle+\sin(\pi/8)|1\rangle.
```

A local Breidbart measurement yields a common bit guess with success $`\beta`$ in either basis. Using it independently gives probability $`\beta^n`$ for every basis distribution, which supplies one part of the [universal converse](codes_and_leakage.md#optimal-secret-basis-rate).

## Classical leakage known before splitting

If classical information $`L`$ about the basis is available before the split, condition on $`L=\ell`$ and use the conditional distribution $`\mu_\ell`$. A different splitting measurement can be chosen for every $`\ell`$, so the exact unconditional value is

```math
\sum_\ell\Pr[L=\ell]\,\omega(\mu_\ell),
```

provided $`X`$ remains uniform and independent of $`(\Theta,L)`$. For a linear syndrome of a uniform basis, all posteriors are affine cosets with the same value; the [dual weight enumerator](codes_and_leakage.md) evaluates it exactly.

The construction does not model arbitrary quantum side information about the basis. That changes the available preparation correlations, as shown by the [separation](quantum_side_information.md).
