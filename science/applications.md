# Two encryption applications with compressed basis keys

[Scientific map](README.md) · [Models](model.md) · [Resource interpretation](interpretation.md)

The exact BB84 cloning theorem has two different encryption consequences. The first is a refinement of conjugate one-time-pad encryption: it has perfect ordinary privacy and an exact bound on simultaneous recovery of a uniformly random message. The second applies the common-mask compiler of Coladangelo, Liu and Xie to obtain one-bit unclonable indistinguishability. Their plaintexts, privacy guarantees and reductions differ, so we specify the two constructions separately.

Throughout, fix a public full-rank binary matrix $`G\in\mathbb F_2^{n\times k}`$ and let $`C=\mathrm{im}\,G`$. A uniform seed $`U\in\mathbb F_2^k`$ chooses the basis string $`\Theta=GU`$. Write

```math
\beta=\cos^2(\pi/8),\qquad
\alpha=-\log_2\beta=0.2284466968\ldots,
\qquad \kappa=\frac{1-\beta}{\beta}.
```

The [physical BB84 cloning theorem](bb84_cloning.md) gives the exact optimum

```math
\omega(C)=2^{-k}\sum_{c\in C}2^{-|c|/2}
=\beta^n\sum_{v\in C^\perp}\kappa^{|v|}.
```

Here a splitting adversary receives an honestly prepared $`|X^{GU}\rangle`$ for uniform independent $`X,U`$, distributes systems to two recipients, and only then lets them learn $`U`$. Both must recover the complete $`X`$. The recipients may use arbitrary joint measurements on their own systems, and the splitting adversary may use entanglement. A measurement followed by broadcasting a classical outcome attains $`\omega(C)`$.

## 1. Full-message conjugate encryption

### Algorithms and ordinary privacy

The secret key is $`(U,P)`$, with independent uniform $`U\in\mathbb F_2^k`$ and $`P\in\mathbb F_2^n`$. To encrypt an $`n`$-bit classical message $`m`$, output

```math
\mathrm{Enc}_{U,P}(m)=|(m\oplus P)^{GU}\rangle.
```

Decryption measures the ciphertext in basis $`GU`$ and XORs the resulting string with $`P`$. Correctness is perfect. The quantum operations used by the honest parties are single-qubit preparations, Hadamards and computational-basis measurements. Computing $`GU`$ is a classical matrix multiplication.

For every fixed $`m,u`$, averaging the pad gives

```math
2^{-n}\sum_{p\in\mathbb F_2^n}
|(m\oplus p)^{Gu}\rangle\langle(m\oplus p)^{Gu}|
=\frac{I}{2^n}.
```

Thus the ciphertext has perfect ordinary one-time privacy, even conditioned on the basis seed alone. For a classical message correlated with an external reference, but independent of the secret key, the averaged ciphertext is also independent of that reference. This is the conjugate encryption architecture studied by [Broadbent and Lord](../references/RELATED_WORK.md#bl2020), with the basis string sampled from a public linear code.

### Exact random-message recovery probability

The recovery game samples an independent uniform message $`M\in\mathbb F_2^n`$. The adversary receives one ciphertext and splits it into systems $`B,D`$. The complete key $`(U,P)`$ is then disclosed to both noncommunicating recipients, which output $`M_B,M_D`$. They win exactly when $`M_B=M_D=M`$.

The change of variables $`X=M\oplus P`$ makes $`X,P,U`$ independent uniform strings. For each fixed pad $`p`$, XORing each recipient's final guess with $`p`$ turns the attack into a valid physical BB84 cloning strategy for $`X`$. This argument permits the final measurements themselves to depend on $`p`$. Since $`G`$ is injective and public, learning $`U`$ gives the same basis information as learning $`GU`$. Consequently every attack has success at most $`\omega(C)`$.

Conversely, run the matching physical cloning attack and XOR its two guesses with the revealed pad. This attains the same value. Therefore

```math
\Pr[\text{optimal simultaneous recovery of uniform }M]=\omega(C).
```

In the $`t`$-uncloneability convention of Broadbent–Lord, which bounds this probability by $`2^{-n+t}`$, the finite-code parameter is $`t=n+\log_2\omega(C)`$. This is a recovery guarantee for a uniformly random message; it is not the ideal $`t=0`$ guarantee.

### Why this construction fails unclonable indistinguishability

For $`n\ge2`$, choose challenge messages $`0^n`$ and $`1^n`$. Give the first ciphertext qubit to recipient $`B`$ and the second to recipient $`D`$. After the key is revealed, each measures its qubit in the prescribed basis and removes the corresponding pad bit. Each obtains the challenge bit exactly. Both distinguish the two messages perfectly without communicating.

The attack works for every $`G`$. Unclonable indistinguishability is therefore false for this construction. This is the same limitation described for the original conjugate encryption in [Broadbent–Lord, §4.1](../references/RELATED_WORK.md#bl2020). Perfect privacy before key revelation and resistance to complete random-message recovery after splitting are compatible with this failure.

## 2. One-bit encryption through a common-mask compiler

### The inherited search-to-prediction theorem

[Coladangelo, Liu and Xie](../references/RELATED_WORK.md#clx2026), in arXiv:2608.17629v2, Definition 3.3 and Theorem 3.4, prove a reduction for a general search game. Let $`p_{\mathrm{Search}}`$ be the optimal probability that both recipients recover a hidden string $`X`$. In the associated common-mask game, an independent uniform $`R\in\mathbb F_2^n`$ is disclosed to both recipients only after the split, together with the original search key. Both must predict $`R\cdot X`$. If their optimal success probability is $`p_{\mathrm{Pred}}`$, then

```math
p_{\mathrm{Search}}\ge(2p_{\mathrm{Pred}}-1)^4.
```

Their theorem allows an arbitrary distribution of the search key and hidden string. Apply it to the physical BB84 search game with key $`U`$, string $`X`$ and token $`|X^{GU}\rangle`$. Since its exact search value is $`\omega(C)`$,

```math
p_{\mathrm{Pred}}\le\frac12+\frac12\omega(C)^{1/4}.
```

The common-mask reduction and its quartic loss are inherited from CLX. Our substitution is the exact code-dependent search value. No tightness claim is made for this prediction bound.

### Algorithms and resources

The secret key is now $`(U,R)`$, with independent uniform $`U\in\mathbb F_2^k`$ and $`R\in\mathbb F_2^n`$. To encrypt a classical bit $`b`$, sample fresh uniform local randomness $`X\in\mathbb F_2^n`$ and output

```math
\mathrm{Enc}^{\mathrm{bit}}_{U,R}(b)
=\bigl(|X^{GU}\rangle,\ c=b\oplus R\cdot X\bigr).
```

The classical bit $`c`$ is public ciphertext. The mask $`R`$ is secret key material; it is not given to the splitting adversary. In the attack game, both recipients receive $`(U,R)`$ after splitting. Honest decryption measures in basis $`GU`$ to obtain $`X`$ and returns $`c\oplus R\cdot X`$.

This is the secret-mask construction of CLX Corollary 1.2 with compressed basis selection. It has perfect correctness, $`n+k`$ shared secret-key bits, $`n`$ ciphertext qubits and one classical ciphertext bit. Encryption additionally uses $`n`$ fresh local random bits. Those coins are not pre-shared key material.

### Reduction for a ciphertext-dependent splitting attack

The indistinguishability game uses a uniform hidden challenge bit $`b`$. Since $`c=b\oplus R\cdot X`$, the transformation

```math
(b,X,U,R)\longleftrightarrow(c,X,U,R)
```

preserves the uniform product distribution. In particular, $`c`$ is uniform and independent of $`X,U,R`$ and the quantum token. This fact is essential: the actual splitting strategy may depend on the visible $`c`$.

To simulate such an attacker in the common-mask prediction game, the splitter samples an independent uniform $`c`$, appends it to the token, and runs the attack's $`c`$-dependent splitting channel. It copies $`c`$ to both recipients. After $`U,R`$ are disclosed, run their original decoders to produce $`b_B,b_D`$, then return $`b_B\oplus c`$ and $`b_D\oplus c`$ as parity guesses. The displayed change of variables proves equality of the full joint distributions. Both parity guesses are correct precisely when both original guesses equal $`b`$.

Conversely, a common-mask prediction strategy ignores $`c`$ during splitting and XORs its final guesses with $`c`$. Therefore the optimal one-bit decision probability equals the optimal common-mask prediction probability, and

```math
\Pr[\text{both recipients recover the challenge bit}]
\le\frac12+\frac12\omega(C)^{1/4}.
```

This also covers the classical one-bit chosen-message formulation. If the two chosen messages coincide, the challenge bit is independent of the ciphertext. If they differ, the messages are a known ordering of $`0,1`$, so a deterministic relabeling gives the experiment above. Arbitrary initial quantum advice independent of the fresh secret key and challenge can be included in the splitting channel.

### Ordinary privacy is statistical, with an exact error

This one-bit construction does not have the perfect privacy of the full-message conjugate pad. Let $`d=2^n`$ and

```math
M_C=\mathbb E_{\theta\in C}|0^\theta\rangle\langle0^\theta|.
```

For $`X=0`$, the inner product $`R\cdot X`$ is always zero. For every nonzero $`X`$, averaging the uniform $`R`$ makes it a uniform bit. The ciphertext states averaged over the secret key and encryption coins are consequently

```math
\rho_b=
\frac{I-M_C}{2d}\otimes I_2
+\frac{M_C}{d}\otimes|b\rangle\langle b|.
```

Since $`M_C`$ is positive and has trace one,

```math
D(\rho_0,\rho_1)
=\frac12\|\rho_0-\rho_1\|_1
=2^{-n}.
```

Thus the optimal equal-prior ordinary distinguishing probability is $`1/2+2^{-n-1}`$. This error is exponentially small and independent of the choice of code. It must not be described as zero.

## 3. Public code setup and the randomness tradeoff

Sample $`G`$ uniformly among full-rank $`n\times k`$ binary matrices. Its image is a uniform $`k`$-dimensional subspace. With

```math
\eta_{n,k}=\frac{2^{n-k}-1}{2^n-1},
```

the [exact random-code calculation](codes_and_leakage.md) gives

```math
\mathbb E_C\omega(C)
=\beta^n+\eta_{n,k}(1-\beta^n)
\le\beta^n+2^{-k}.
```

The adversary may know the public matrix and choose its attack accordingly: the fixed-code bounds apply to every strategy for each matrix. For the full-message scheme, the displayed expectation is the exact average optimal recovery probability. For the one-bit scheme, Jensen's inequality gives the average advantage bound

```math
\mathbb E_C\left[p_{\mathrm{Pred}}(C)-\frac12\right]
\le\frac12
\left[\beta^n+\eta_{n,k}(1-\beta^n)\right]^{1/4}.
```

There is also a guarantee for most individual public setups. If

```math
k\ge\alpha n+\log_2\frac1{\varepsilon\delta},
```

then, with probability at least $`1-\delta`$, the sampled code satisfies

```math
\sum_{v\in C^\perp}\kappa^{|v|}\le1+\varepsilon.
```

Every such code has full-message recovery probability at most $`(1+\varepsilon)\beta^n`$ and one-bit decision advantage at most $`(1+\varepsilon)^{1/4}\beta^{n/4}/2`$. The same certificate also has the independent [retained-subset and noise consequences](noise_and_loss.md). The compiler does not automatically transfer those consequences to a noisy encryption scheme, because its search experiment requires exact recovery of $`X`$.

For example, $`k\ge\alpha n+2t`$ gives $`\varepsilon=\delta=2^{-t}`$. Choosing $`t=o(n)`$ yields $`n+k=(1+\alpha)n+o(n)`$ secret-key bits in either construction, compared with $`2n`$ when the basis string is sampled independently bit by bit. The first construction retains the full-basis search exponent $`\alpha`$; the second retains the full-basis exponent $`\alpha/4`$ certified by the inherited CLX reduction. Taking $`t=\omega(\log n)`$ additionally makes the exceptional-code probability negligible.

The expectation guarantee and the good-fixed-code guarantee answer different questions. Bounding the exceptional codes by their probability can lose the sharper exponent already supplied by the exact expectation. There is no assertion that every sampled code is good, or that its full weight-spectrum certificate can be checked efficiently.

For the underlying search task, the exponent is optimal within this basis-selection model: every distribution admits the Breidbart attack with probability $`\beta^n`$, and a distribution generated with $`k`$ random bits admits a basis-guessing attack with probability at least $`2^{-k}`$. Random linear codes match the larger of these floors to within a factor of two in expectation. This does not establish an optimal total encryption-key length, a tight one-bit decision exponent, or a necessary basis-key rate for unclonable indistinguishability itself.

## 4. The two guarantees at a glance

| Property | Conjugate pad | Common-mask bit construction |
| --- | --- | --- |
| Plaintext | $`n`$ classical bits | One classical bit |
| Ciphertext | $`n`$ qubits | $`n`$ qubits and one classical bit |
| Shared secret key | $`k`$ basis bits and $`n`$ pad bits | $`k`$ basis bits and $`n`$ mask bits |
| Ordinary one-time privacy | Perfect | Trace distance $`2^{-n}`$ between the two ciphertext states |
| Post-split guarantee | Exact random-message recovery probability $`\omega(C)`$ | Decision success at most $`1/2+\omega(C)^{1/4}/2`$ |
| Unclonable indistinguishability | False for $`n\ge2`$ | Follows from the inherited common-mask theorem |

These are one-time constructions. Neither analysis proves reuse of its secret key, multi-copy security, ciphertext authentication, or a multi-bit composition theorem for the one-bit construction. Reusable authentication requires the separate protocol and hypotheses in [the key-recycling analysis](key_recycling.md).
