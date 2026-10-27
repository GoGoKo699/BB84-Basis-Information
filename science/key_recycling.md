# Refining noiseless authentication with key recycling

[Scientific map](README.md) · [Models](model.md) · [Resource interpretation](interpretation.md)

The exact code-dependent BB84 value can be substituted into the noiseless authentication analysis of [Fehr and Salvail](../references/RELATED_WORK.md#fs2017). The protocol, its quantum-side-information reduction and its sequential composition argument are theirs. The refinement replaces a minimum-distance estimate by the exact monogamy value and preserves the original constants.

This page pins the application to arXiv:1610.05614v3, dated 19 May 2017, specifically Theorem 4.1 and Proposition 5. Its title-page note identifies the EUROCRYPT proceedings/ePrint version with v2. The result below retains the protocol's assumptions; it does not assert a new general composition theorem or a replacement for its noisy analysis.

## 1. Protocol and hypotheses

Let $`C\subseteq\mathbb F_2^n`$ be a nonempty public basis code. Write $`\omega(C)`$ for the exact BB84 monogamy value with a uniform basis in $`C`$. For a linear code, the [code-spectrum formula](codes_and_leakage.md) is

```math
\omega(C)=\beta^n\sum_{v\in C^\perp}\kappa^{|v|},
\qquad
\beta=\cos^2(\pi/8),\quad
\kappa=\frac{1-\beta}{\beta}.
```

The following substitution also applies to a nonlinear code using the exact spectral value from [the BB84 cloning theorem](bb84_cloning.md).

Let

```math
\mathrm{MAC}:\mathcal K\times
(\mathcal M\times\mathbb F_2^n)\longrightarrow\mathcal T
```

be a one-time authentication code with substitution error $`\varepsilon_{\mathrm{MAC}}`$. For every fixed classical message $`m`$, the keyed function $`h_m(K,X)=\mathrm{MAC}(K,m\|X)`$ must satisfy the two properties used by FS:

- **Message independence.** With a uniform key, the distribution of $`h_m(K,x)`$ is independent of $`x`$.
- **Ideal key privacy.** For every state with uniform $`K`$ independent of $`X`$, tag $`T=h_m(K,X)`$, and Markov relation $`K\leftrightarrow XT\leftrightarrow F`$,

```math
\Delta(K\mid TF)
\le\frac12\sqrt{|\mathcal T|\,\mathrm{Guess}(X\mid TF)}.
```

Here $`\mathrm{Guess}`$ denotes optimal guessing probability with quantum side information, and

```math
\Delta(K\mid F)
=\frac12\left\|\rho_{KF}-U_{\mathcal K}\otimes\rho_F\right\|_1.
```

FS's suggested OTP-masked universal-hash constructions satisfy these requirements. Ordinary one-time MAC security alone is insufficient for the recycling conclusion.

The honest parties share a MAC key $`K`$ and basis key $`\Theta\in C`$. Alice samples fresh uniform $`X\in\mathbb F_2^n`$, prepares $`|X^\Theta\rangle`$, and sends the classical message $`m`$, the qubits, and $`T=\mathrm{MAC}(K,m\|X)`$. Bob measures the received qubits in basis $`\Theta`$ to get $`X'`$ and verifies the received classical message/tag against $`X'`$. Eve may arbitrarily modify the classical and quantum transmission and retain quantum information.

If Bob accepts, the parties retain both keys. If he rejects, they retain $`K`$ and replace $`\Theta`$ by fresh shared uniform $`\Theta'\in C`$. This refresh requires the reliable and private randomness resource assumed in FS; it is not obtained for free from the transmitted tag. The execution model includes a common accept/reject outcome and synchronized sequential use of the keys. Eve learns the decision.

For one execution, the initial state must be

```math
\rho_{K\Theta E}=U_{\mathcal K}\otimes\rho_{\Theta E},
```

where Eve's $`E`$ may be quantum and arbitrarily correlated with $`\Theta`$. The message is fixed, or chosen by measuring Eve's state before the execution. It must remain independent of the MAC key in the stated sense; superposition message queries are outside this model.

The proof through the one-execution estimates first fixes the message $`m`$. For a message chosen from Eve's information, every message-independence and Markov assertion below is applied conditional on that classical message. The averaging argument at the end of §4 treats this case explicitly.

## 2. Importing the exact value in the presence of quantum side information

Let $`g=\mathrm{Guess}(\Theta\mid E)`$ and write

```math
\rho_{\Theta E}
=\sum_{\theta\in C}|\theta\rangle\langle\theta|
\otimes\rho_E^\theta,
```

where the $`\rho_E^\theta`$ are subnormalized. The dual state-discrimination program has an optimal positive operator $`Y`$ such that $`Y\succeq\rho_E^\theta`$ for every $`\theta`$ and $`\mathrm{Tr}\,Y=g`$. Consequently, for $`\sigma_E=Y/g`$,

```math
\rho_{\Theta E}
\preceq g|C|\,U_C\otimes\sigma_E.
```

Apply an arbitrary channel from $`E`$ to referee and player registers $`A,B,D`$, followed by the referee's BB84 measurement, two local basis-dependent measurements, and the success test. Positivity preserves the operator inequality. On the comparison state $`U_C\otimes\sigma_E`$, the prepared quantum state is independent of the basis, so its success is at most $`\omega(C)`$. Therefore

```math
\Pr[X=X_B=X_D]\le g|C|\omega(C).
```

The same upper bound holds when only one player must guess the referee's outcome and is not given the basis. Measure that player's system before the basis is revealed and copy its classical answer to two recipients; this produces a valid strategy in the two-player game.

This is the domination argument already used in FS Corollaries 1 and 2. Its original independent-state bound was $`|C|^{-1}+2^{-d(C)/2}`$. The exact value replaces that bound, yielding the factor $`g|C|\omega(C)`$. This does not assert an exact formula for arbitrary quantum leakage about the basis.

## 3. One execution: the basis-key estimate

Let $`V\in\{0,1\}`$ be Bob's accept/reject bit. Let $`R`$ contain Eve's complete retained information, including the original tag and any classical changes she made. Her final side information is $`E'=VR`$.

After averaging the uniform MAC key, message independence makes the original tag independent of $`X,\Theta,E`$ and the prepared qubits. Averaging uniform $`X`$ makes the quantum ciphertext $`I/2^n`$, independently of $`\Theta,E`$. Data processing therefore gives

```math
\mathrm{Guess}(\Theta\mid R)
\le\mathrm{Guess}(\Theta\mid E)=g.
```

On rejection, $`\Theta'`$ is fresh uniform randomness. On acceptance, it equals $`\Theta`$. Decomposing guessing probability over the public decision gives

```math
\begin{aligned}
\mathrm{Guess}(\Theta'\mid VR)
&=\Pr[V=0]\frac1{|C|}
 +\Pr[V=1]\mathrm{Guess}(\Theta\mid R,V=1)\\
&\le\frac1{|C|}+\mathrm{Guess}(\Theta\mid R)\\
&\le g+\frac1{|C|}.
\end{aligned}
```

The middle inequality uses a subnormalized event: a measurement optimized on the accepted branch is also a valid measurement on the entire state, whose other contribution is nonnegative. This does not bound Eve's guessing probability conditioned on acceptance by itself.

## 4. One execution: MAC-key privacy and its constants

Define $`J`$ to indicate that Eve left the classical message and tag unchanged, and $`Q=1_{X=X'}`$. We may give $`J`$ to Eve, since she can retain the original and forwarded classical data. The ideal decision is $`\widetilde V=JQ`$. Let $`\widetilde\Theta'`$ retain the old basis exactly when $`\widetilde V=1`$ and otherwise use fresh independent refresh randomness.

### Replacing the real decision

The real and ideal decisions differ only if a modified authenticated input or tag is accepted. This event has probability at most $`\varepsilon_{\mathrm{MAC}}`$ by the assumed one-time MAC security. The physical side information used to generate a modification is independent of $`K`$ once the original MAC input and tag are fixed; granting the attacker that input cannot invalidate the MAC bound.

Coupling the refresh coins shows that the real and ideal joint output states are $`\varepsilon_{\mathrm{MAC}}`$-close. Their side-information marginals are equally close. The triangle inequality then gives a cost of $`2\varepsilon_{\mathrm{MAC}}`$ when comparing their distances from a product state with a uniform MAC key.

### Applying key privacy

Provide $`Q`$ as additional side information. Because $`\widetilde V`$ is determined by $`Q,R`$, it need not be counted again. The register

```math
F=(\widetilde\Theta',Q,R)
```

is produced from $`X,T`$ and key-independent initial systems, without acting directly on $`K`$. Thus $`K\leftrightarrow XT\leftrightarrow F`$, so ideal key privacy applies. The original tag $`T`$ is already included in $`R`$. We obtain

```math
\Delta(K\mid\widetilde\Theta'\widetilde V R)
\le\frac12\sqrt{|\mathcal T|\,\mathrm{Guess}
(X\mid\widetilde\Theta',Q,R)}.
```

In the expression above, $`|\mathcal T|`$ is the tag-space size. Keeping the tag explicitly avoids assuming that it can be removed after an arbitrary tag-dependent quantum channel.

Set $`B_0=g|C|\omega(C)`$. We bound the guessing probability inside the square root by $`2B_0`$, using its two $`Q`$ branches.

On $`Q=0`$, the refreshed basis is independent of everything else. The subnormalized branch contribution is therefore at most $`\mathrm{Guess}(X\mid R)`$. By data processing, it is at most the probability of guessing $`X`$ from the original ciphertext, original tag and $`E`$, without the basis. At that original input state the tag is independent, so it can be removed. The one-player bound in §2 gives at most $`B_0`$.

On $`Q=1`$, providing the original $`\Theta`$ is at least as informative as providing $`\widetilde\Theta'`$. Indeed, if $`J=1`$ these are identical; if $`J=0`$ the latter is fresh independent randomness, which can be simulated from the former and $`R`$. Thus this branch contributes at most

```math
\Pr[Q=1]\mathrm{Guess}(X\mid\Theta,R,Q=1).
```

For each basis, choose the measurement on Eve's register that optimizes this conditional guessing probability. It is a valid measurement on that register even when evaluated on the unconditional state. The displayed expression is the probability that Bob's measured $`X'`$ and Eve's answer both equal $`X`$. After averaging out $`K`$, the original tag is an independent channel input. The deferred EPR preparation and Eve's channel therefore fit the preparation map in §2, bounding this contribution by another $`B_0`$.

Combining the two branches and restoring the real decision proves

```math
\boxed{
\Delta(K\mid\Theta'E')
\le2\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}
\sqrt{g|C|\omega(C)|\mathcal T|}.
}
```

The factor $`1/\sqrt2`$ is the product of the $`1/2`$ in ideal key privacy and the square root of the two branch contributions. It has not been absorbed into an unspecified constant. For a $`\nu`$-key-private hash, this square-root term would be multiplied by $`\nu`$.

Together with §3, the one-execution result is

```math
\mathrm{Guess}(\Theta'\mid E')\le g+|C|^{-1},
\qquad
\Delta(K\mid\Theta'E')
\le2\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}\sqrt{g|C|\omega(C)|\mathcal T|}.
```

For a message $`M`$ selected by a measurement of Eve's initial system, let $`E_1`$ denote her remaining information, retain $`M`$ in that information, and write $`g_m=\mathrm{Guess}(\Theta\mid E_1,M=m)`$. Each conditional state still has an independent uniform MAC key. Apply the fixed-message proof to that branch. Data processing and the classical decomposition of guessing probability give

```math
\overline g=\sum_m\Pr[M=m]g_m
=\mathrm{Guess}(\Theta\mid M E_1)
\le\mathrm{Guess}(\Theta\mid E).
```

The basis-key estimates average linearly. For the MAC key, Jensen's inequality gives $`\sum_m\Pr[M=m]\sqrt{g_m}\le\sqrt{\overline g}`$, preserving the displayed square-root bound and every constant. This conditional argument is needed: the per-message hash hypotheses do not assert unconditional tag independence when the message itself is correlated with Eve's information.

## 5. Sequential reuse

Initially take $`K`$ and $`\Theta`$ uniform and independent of Eve. Define a comparison sequence in which the MAC key is freshly replaced by an independent uniform key before every execution, while retaining the comparison basis/adversary state. Denote by $`g_j`$ its basis guessing probability after $`j`$ executions. The first bound above gives

```math
g_j\le\frac{j+1}{|C|}.
```

The input to execution $`j`$ therefore has basis guessing probability at most $`j/|C|`$. Its MAC-key privacy error is bounded by

```math
\delta_j=
2\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}\sqrt{j\omega(C)|\mathcal T|}.
```

For completeness, let $`\rho_j`$ be the real state after $`j`$ executions and $`\tau_j`$ the comparison output before its next hypothetical MAC-key refresh. If $`\mathcal E_j`$ is the complete execution channel, including Eve's strategy, then

```math
\rho_j=\mathcal E_j(\rho_{j-1}),
\qquad
\tau_j=\mathcal E_j
\bigl(U_{\mathcal K}\otimes\tau_{j-1,\Theta E}\bigr).
```

Contractivity and the one-step key-privacy estimate imply

```math
\begin{aligned}
D\bigl(\rho_j,U_{\mathcal K}\otimes\tau_{j,\Theta E}\bigr)
&\le D(\rho_j,\tau_j)
 +D\bigl(\tau_j,U_{\mathcal K}\otimes\tau_{j,\Theta E}\bigr)\\
&\le D\bigl(\rho_{j-1},
U_{\mathcal K}\otimes\tau_{j-1,\Theta E}\bigr)+\delta_j.
\end{aligned}
```

Induction bounds this distance by $`\sum_{a\le j}\delta_a`$. Before execution $`i`$, the real state is consequently within $`\sum_{j<i}\delta_j`$ of an input with an independent uniform MAC key. A message substitution in that comparison execution is accepted with probability at most $`\varepsilon_{\mathrm{MAC}}`$. Hence

```math
\boxed{
\varepsilon_i\le
(2i-1)\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}\sqrt{\omega(C)|\mathcal T|}
\sum_{j=1}^{i-1}\sqrt j.
}
```

Here $`\varepsilon_i`$ is the probability of an accepted message substitution in execution $`i`$. It is not the probability of at least one failure over the whole sequence; that quantity can instead be bounded by summing the per-execution estimates. The theorem allows Eve to retain quantum memory and choose subsequent classical messages from her accumulated information within the stated execution model.

## 6. Concrete parameter refinement

Let $`\lambda\in\mathbb N`$ and choose a suitable MAC with

```math
\varepsilon_{\mathrm{MAC}}=2^{-\lambda},
\qquad |\mathcal T|=2^\lambda.
```

Sample a public linear code of dimension $`k=3\lambda`$ and length

```math
n=\left\lceil\frac{3\lambda}{-\log_2\beta}\right\rceil.
```

The [exact random-code mean](codes_and_leakage.md) gives

```math
\mathbb E_C\omega(C)
\le\beta^n+2^{-3\lambda}
\le2\cdot2^{-3\lambda}.
```

The fixed-code bound holds for every adversary, including one that knows the public code and selects its strategy accordingly. Jensen's inequality therefore yields

```math
\mathbb E_C\varepsilon_i
\le\left(2i-1+\sum_{j<i}\sqrt j\right)2^{-\lambda}.
```

This matches the displayed FS sequential-use guarantee, with the same $`3\lambda`$ fresh basis bits needed after a rejection. It is average security over honestly sampled public setup. A guarantee for most individual fixed codes follows from the weight-spectrum certificate with appropriate slack; it is a different statement from a worst-case guarantee for every public matrix.

### What the numerical comparison means

FS chooses $`|C|=2^{3\lambda}`$ and minimum distance $`d(C)=6\lambda`$ so that its estimate $`|C|^{-1}+2^{-d(C)/2}`$ is at most $`2\cdot2^{-3\lambda}`$. If this minimum-distance requirement is certified using the random-linear Gilbert–Varshamov tradeoff, the limiting code rate $`R=k/n`$ satisfies

```math
h_2(2R)+R=1,
\qquad R=0.141226986996\ldots.
```

The resulting asymptotic comparison is

| Certification method | Qubits for the stated FS parameters |
| --- | ---: |
| FS minimum-distance estimate with random-linear GV distance | $`21.2423989480\lambda+o(\lambda)`$ |
| Exact code spectrum with random public linear setup | $`13.1321662407\lambda+O(1)`$ |

The reduction is approximately $`38.18\%`$ for this comparison. It is a comparison between two analyses/instantiations, not a lower bound on every classical code or every key-recycling scheme. In particular, FS's observation $`n\ge9\lambda-1`$ follows from Singleton and is only a necessary bound, not an achievable binary-code construction. The comparison counts qubits and basis refresh bits; it does not assert that all other secret-key material has optimal length.

FS §5.5 distinguishes its goal of minimizing fresh basis randomness from the possible goal of minimizing quantum communication. The exact random-code calculation obtains the full independent-basis search exponent with asymptotically minimal basis randomness for that search task. This explains why retaining the complete weight spectrum changes the protocol's certified parameters.

## 7. Scope of the substitution

The substitution changes the factor

```math
1+|C|2^{-d(C)/2}
\quad\text{to}\quad |C|\omega(C)
```

in the noiseless one-step and sequential authentication bounds. The rest of the FS proof framework is retained.

Several restrictions matter:

- The ordinary MAC, message-independence and key-privacy requirements remain necessary premises. The accepted/rejected decision and private refresh resource must follow the stated protocol.
- The bounds concern synchronized sequential executions. The additional impersonation/application-interleaving issue discussed in FS §4.6 is not removed by replacing the monogamy constant.
- FS's noisy theorem accepts a Bob output close to $`X`$ while Eve guesses $`X`$ exactly. That differs from the common-output acceptance predicate in [the noise and loss theorem](noise_and_loss.md), so the latter is not a direct substitute.
- The encryption-with-recycling extension introduces additional extractor/sketch composition constants. Those are not inferred from the authentication theorem without a separate argument.
- Later QKR protocols use different recycling procedures and rate analyses. The comparison here is specifically to the stated FS minimum-distance instantiation, not a claim of the best rate among all QKR schemes.

The result is a sharper, fully quantified application of an existing protocol. It leaves the protocol's definitions and security model intact while replacing the guessing estimate at the two places where its proof uses code distance.
