# Understanding BB84 basis information

[Repository overview](../README.md) · [30-milestone map](milestones.md) · [Watrous bridge](watrous_bridge.md) · [Complete proofs](../science/README.md)

A classical encrypted file can be copied before its key arrives. Once the key is disclosed, both copies can be read. A quantum encoding can behave differently: an adversary must distribute a quantum system before learning how it should be measured, and the two recipients may be unable to recover the same complete message.

This project asks how the **distribution of those measurement instructions** affects that obstruction. The instructions are BB84 basis choices. They may be biased, correlated, generated from a short seed, or partially disclosed. The answer depends on their full geometry. Counting the undisclosed bits alone loses information.

The selected educational anchor is [Watrous, *The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/). The [source bridge](watrous_bridge.md) gives exact sections and translates notation. This tutorial follows the settled map: the first thirteen milestones assemble the mathematical objects and security models; the remaining seventeen connect the exact argument to codes, noise, leakage and applications. The authoritative theorem statements and complete proofs remain in `science/`.

## Qubits and BB84

**Milestones [M01](milestones.md#m01)–[M02](milestones.md#m02).**

A qubit has a two-dimensional state space. The column vectors

```math
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}
```

form the computational basis. The notation $`|v\rangle`$ denotes a vector, while $`\langle v|`$ denotes its conjugate transpose. A pure state is a unit vector, or equivalently the rank-one density operator $`|v\rangle\langle v|`$. A general density operator $`\rho`$ is positive semidefinite and has trace one. It includes probabilistic mixtures of pure states.

A measurement is described by positive operators $`E_a`$ summing to the identity. Outcome $`a`$ has probability $`\mathrm{Tr}(E_a\rho)`$. Such a family is a POVM. If its effects are orthogonal projections, it is a PVM. For a basis measurement, the effects are the projections onto its basis vectors.

BB84 uses two bases. Its second basis is

```math
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
```

The Hadamard operator $`H`$ maps $`|0\rangle`$ to $`|+\rangle`$ and $`|1\rangle`$ to $`|-\rangle`$. Write

```math
|x^\theta\rangle=H^\theta|x\rangle,
\qquad x,\theta\in\{0,1\}.
```

Here $`x`$ is the encoded data bit and $`\theta`$ is the basis instruction. Measuring in the prescribed basis recovers $`x`$ with certainty. Measuring a computational-basis state in the Hadamard basis instead gives two equally likely outcomes. The amplitude overlap between either vector from one basis and either vector from the other has magnitude $`c=1/\sqrt2`$; the corresponding probability is $`c^2=1/2`$.

For an $`n`$-bit string, the honest source prepares the product state

```math
|x^\theta\rangle=\bigotimes_{i=1}^nH^{\theta_i}|x_i\rangle.
```

The product describes honest preparation. It does not restrict the adversary to separate attacks on individual qubits. The general measurement language is needed precisely because a collective operation might exploit correlations among the basis choices. These objects and the exact game are defined in [the model](../science/model.md).

## Joint systems and timing

**Milestones [M03](milestones.md#m03)–[M05](milestones.md#m05).**

The tensor product combines systems. A state $`\rho_{ABD}`$ describes the referee's register $`A`$ and two recipient registers $`B,D`$. A joint state need not factor as a product of three states. Ignoring $`D`$ produces the reduced state $`\mathrm{Tr}_D\rho_{ABD}`$, where the partial trace is the operation that preserves all measurement statistics on the retained systems.

A quantum channel is a completely positive, trace-preserving linear map. Complete positivity means it remains a valid positive map when an untouched auxiliary system is included. A splitting channel can consume all input qubits, use private ancillary systems, and produce arbitrarily entangled outputs $`B,D`$. After the split, Bob and Charlie can each measure their entire local register. They cannot communicate with one another.

Timing determines the information available to that channel. In the physical experiment, $`X`$ is uniform and independent of $`\Theta\sim\mu`$. The splitter receives $`|X^\Theta\rangle`$. Only **after** distributing its outputs do both recipients learn the complete $`\Theta`$. Success means that both return the complete $`X`$. Their final measurements may depend on every basis bit.

Two standard tools put this experiment into a convenient mathematical form.

First, **Naimark dilation** replaces a POVM by a projective measurement on a larger system with an initially fixed ancilla. For finitely many question-dependent measurements, the ancilla can be chosen in the same initial state for every question. Different questions still select different projections. This tool simplifies the proof without restricting the player's original measurement choices; see [Watrous Theorem 2.42 and Corollary 2.43](watrous_bridge.md#preparation-needed-for-the-core-argument).

Second, **source replacement** starts with a maximally entangled pair,

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{x\in\{0,1\}^n}|x\rangle_A|x\rangle_S,
\qquad d=2^n.
```

Measuring $`A`$ in a real BB84 basis produces a uniform outcome $`x`$ and prepares $`|x^\theta\rangle`$ on $`S`$. Since a channel on $`S`$ commutes with a measurement on $`A`$, the splitting channel can be placed before that measurement. The resulting $`ABD`$ state is independent of the later basis choice. This is a proof representation of the honest source; the real-valued BB84 vectors make the prepared state equal to the desired vector without a conjugation change. The [full source-replacement argument](../science/bb84_cloning.md#upper-bound-by-source-replacement) also explains its limitation: the referee marginal in this representation is fixed to $`I/d`$.

## Operators and overlap

**Milestone [M06](milestones.md#m06).**

An operator norm measures the largest factor by which a linear map can enlarge a vector:

```math
\|A\|_\infty=\max_{\|v\|=1}\|Av\|.
```

For a positive operator $`M`$, this norm equals its largest eigenvalue and its largest expectation in a state:

```math
\|M\|_\infty=\lambda_{\max}(M)
=\max_{\|v\|=1}\langle v|M|v\rangle.
```

This converts an optimization over states into an eigenvalue problem. A success operator is positive; a top eigenvector is the state that maximizes its expectation.

For two projections $`P,Q`$, $`\|PQ\|_\infty`$ measures how well their subspaces can align. For rank-one projections onto unit vectors $`u,v`$, it equals $`|\langle u,v\rangle|`$. Tensor products multiply operator norms, so a sequence of coordinates on which two bases differ produces a product of overlap factors.

A second useful observation concerns a collection of vectors $`v_j`$. Put those vectors into the columns of a matrix $`V`$. Its **Gram matrix** $`V^\dagger V`$ records all pairwise inner products; its **frame operator** $`VV^\dagger`$ is the sum $`\sum_j|v_j\rangle\langle v_j|`$. They have the same nonzero eigenvalues. For example, if $`V^\dagger Vz=\lambda z`$ with $`\lambda>0`$, then $`Vz\ne0`$ and $`VV^\dagger(Vz)=\lambda Vz`$.

The spectral theorem uses this identity twice: a block Gram operator supplies an upper bound for every strategy, and a scalar Gram matrix supplies a matching state. Watrous §1.1.3 provides the underlying spectral and singular-value tools; [the project proof](../science/spectral_value.md) supplies their particular combination.

## Guessing and conditioning

**Milestones [M07](milestones.md#m07)–[M08](milestones.md#m08).**

Suppose a label $`Z`$ is chosen with probability $`p_z`$, and someone receives a quantum state $`\rho_z`$. Their optimal probability of identifying the label is

```math
P_{\mathrm{guess}}(Z|E)
=\max_{\{M_z\}}\sum_zp_z\mathrm{Tr}(M_z\rho_z).
```

The maximization is over POVMs. Giving more usable information can increase this quantity; processing or discarding information cannot increase it. A useful upper bound comes from any operator $`Y`$ dominating each weighted state $`p_z\rho_z`$: the guessing probability is then at most $`\mathrm{Tr}\,Y`$. This is the dual-certificate view of state discrimination explained in [the source bridge](watrous_bridge.md#preparation-for-information-leakage-and-applications).

For two states with equal prior probabilities, the optimal success is

```math
\frac12+\frac14\|\rho_0-\rho_1\|_1
=\frac{1+D(\rho_0,\rho_1)}2,
\qquad D(\rho_0,\rho_1)=\frac12\|\rho_0-\rho_1\|_1.
```

The trace norm is the sum of singular values. The half-normalized trace distance $`D`$ measures how well a measurement can distinguish two alternatives. This interpretation will let us state ordinary encryption privacy separately from two-recipient recovery.

Classical information can be handled by ordinary conditioning. If a classical label $`L`$ is disclosed before the attack, the attacker can choose a strategy for each value $`\ell`$. The overall optimal success is the probability-weighted average of the conditional optima.

A quantum register is different. The joint description

```math
\rho_{\Theta E}
=\sum_\theta p_\theta|\theta\rangle\langle\theta|\otimes\rho_E^\theta
```

is called a classical-quantum state: $`\Theta`$ is classical, while $`E`$ may contain nonorthogonal quantum states. The register $`E`$ need not reveal a classical value that can simply be conditioned on. Measuring it first may discard useful capabilities. Later we will see an example in which $`E`$ is difficult to use for identifying $`\Theta`$ but immediately useful for preparing a winning referee state.

Conditioning on an event also changes normalization. A rare accepted branch may have a large conditional success probability. Security statements that count its occurrence must retain its probability weight. This distinction is essential for loss and key recycling.

## Codes as basis sources

**Milestones [M09](milestones.md#m09)–[M10](milestones.md#m10).**

Binary arithmetic takes place in $`\mathbb F_2`$: addition is XOR. A binary linear code $`C\le\mathbb F_2^n`$ is a vector subspace. If its dimension is $`k`$, it contains $`2^k`$ vectors. Here those vectors specify **bases**. The data string itself is not being error-corrected by this code.

A public full-column-rank matrix $`G`$ maps a uniform secret seed $`U\in\mathbb F_2^k`$ to a basis string $`\Theta=GU`$. Because $`G`$ is injective, every codeword is equally likely. Thus $`k`$ shared secret bits select the bases of $`n`$ qubits.

The dual code contains the parity checks that every codeword satisfies:

```math
C^\perp=\{r\in\mathbb F_2^n:r\cdot c=0\text{ for all }c\in C\}.
```

The dot product is modulo two. If instead a fully uniform basis is sampled and a fixed syndrome $`A\Theta`$ is disclosed, each posterior basis set is an affine coset of $`\ker A`$. A coset is a translate $`a+C`$ of a linear code; translation preserves pairwise Hamming distances.

For a string $`c`$, its Hamming weight $`|c|`$ counts its ones. The Hamming distance $`d_H(c,c')`$ counts the positions where two strings differ. The weight enumerator

```math
W_C(t)=\sum_{c\in C}t^{|c|}
```

records the entire weight profile. A minimum distance records only the smallest nonzero weight. Keeping the whole enumerator will produce an exact value.

The duality calculation uses binary characters $`(-1)^{r\cdot x}`$. Summing these signs over $`C^\perp`$ yields $`|C^\perp|`$ when $`x\in C`$ and zero otherwise. This converts a sum over one code into a weighted sum over its dual. The [local Fourier derivation](../science/codes_and_leakage.md#fourier-proof-of-the-dual-form) supplies the calculation; coding theory is not an additional educational-anchor requirement.

## Moments and security predicates

**Milestones [M11](milestones.md#m11)–[M12](milestones.md#m12).**

A moment bound can control an unlikely error event without assuming independent errors. If $`L`$ counts failures and $`0<s<1`$, a small value of $`L`$ makes $`s^L`$ large. Consequently,

```math
\Pr[L\le r]\le s^{-r}\mathbb E[s^L].
```

This is Markov's inequality applied to a nonnegative random variable. The useful question is how to bound $`\mathbb E[s^L]`$. In this project, products of success indicators connect it to exact guessing probabilities on subsets. The proof never infers a concentration bound from single-coordinate success probabilities alone.

The event called success also matters. Complete recovery requires both recipients to identify every bit. Agreed-error recovery allows a bounded number of errors but requires their answers to agree. One-bit prediction asks for one specified function of the hidden string. Authentication asks whether an altered message is accepted. These events have different reductions and different quantitative guarantees.

Resources must be counted with the same care. The secret seed, a public code description, ciphertext qubits, a message pad, and a later-disclosed mask are different resources. A small basis seed does not by itself establish a small total encryption key. The [resource interpretation](../science/interpretation.md) keeps these distinctions explicit.

## Three experiments

**Milestone [M13](milestones.md#m13).**

The preliminary ideas now determine three precise experiments.

| Experiment | What is supplied before the basis is disclosed? | Load-bearing condition |
| --- | --- | --- |
| Abstract monogamy game | The players supply any state on referee and recipient registers | The joint state is independent of the sampled basis |
| Honest BB84 splitting | An honest source supplies a uniform data string encoded in the chosen bases | The data string is independent of the basis; the split precedes basis disclosure |
| Quantum basis information | A preparation channel receives a quantum register already correlated with the basis | The independence condition of the first experiment is absent |

The first experiment has the broadest choice of referee states under independence. Source replacement places the second inside it, giving an upper bound. A separate physical construction will prove equality for BB84. The third changes the premise and can behave differently.

The shared story is about how much a physical system can support **two correct later answers**. The exact source, available side information, disclosure timing and winning event specify which theorem applies. [The model page](../science/model.md) is the canonical statement of these choices.

## The exact spectral value

**Milestones [M14](milestones.md#m14)–[M16](milestones.md#m16).**

Take any two fixed PVMs $`P=\{P_a\}`$ and $`Q=\{Q_b\}`$ on a nonzero finite-dimensional space. Their ranks and outcome alphabets may differ. Define their unsquared overlap

```math
c=\max_{a,b}\|P_aQ_b\|_\infty.
```

For an integer $`n\ge1`$, each coordinate is measured with one of these two PVMs. The question string $`\theta\in\{0,1\}^n`$ has any specified distribution $`\mu`$, independent of the initial state. The two recipients may use arbitrary finite-dimensional systems and shared entanglement. They learn the whole question and use arbitrary local measurements, with no communication between them. They win when both answer the entire referee outcome correctly.

The exact optimal value is

```math
\omega^*(\mu;P,Q)=\lambda_{\max}(K_\mu),
\qquad
(K_\mu)_{\theta,\phi}
=\sqrt{\mu(\theta)\mu(\phi)}\,c^{d_H(\theta,\phi)}.
```

Only basis strings with nonzero probability need index the matrix. The diagonal records their probabilities. An off-diagonal entry combines their probability weights with an overlap penalty for every coordinate on which they disagree. This is [Theorem S](../science/spectral_value.md#theorem-one-scalar-matrix-gives-the-exact-value).

### Why this bounds every strategy

After dilating the player measurements, each question has a winning projection $`\Pi_\theta`$. The inherited [TFKW overlap argument](../references/RELATED_WORK.md#tfkw2013) bounds

```math
\|\Pi_\theta\Pi_\phi\|_\infty
\le c^{d_H(\theta,\phi)}.
```

The two separate player registers are important. One can enlarge the winning projection for $`\theta`$ by dropping Charlie's correctness condition, and enlarge the one for $`\phi`$ by dropping Bob's. The resulting product is block diagonal in the player outcomes; each referee block is a product of outcome projections. The tensor-product overlap bound then applies.

To combine all questions, form the block row operator $`T`$ whose block for $`\theta`$ is $`\sqrt{\mu(\theta)}\Pi_\theta`$. Then $`TT^\dagger`$ is the average winning operator. Each block of $`T^\dagger T`$ is bounded in norm by the corresponding scalar entry of $`K_\mu`$. Replacing the vector in each block by its length gives

```math
\left\|\sum_\theta\mu(\theta)\Pi_\theta\right\|_\infty
\le\lambda_{\max}(K_\mu).
```

This controls arbitrary states, shared entanglement and collective local measurements. The complete inequalities appear in [the upper-bound proof](../science/spectral_value.md#upper-bound).

### Why equality is possible

Choose one outcome subspace of each PVM that attains $`c`$. Their principal vectors can be chosen as unit vectors $`u,v`$ with $`\langle u,v\rangle=c`$. For each question string, tensor together $`u`$ at zero positions and $`v`$ at one positions. These product vectors have pairwise inner products exactly $`c^{d_H(\theta,\phi)}`$.

Both recipients give fixed answers naming the chosen subspaces. A top eigenvector of the resulting frame operator is an optimal referee state. Its weighted Gram matrix is exactly $`K_\mu`$, so it reaches the upper bound. The referee state may be entangled across coordinates, even though the recipients need no quantum registers in this attaining strategy.

Two fixed PVMs allow this compatible family of overlaps. A third measurement or nonprojective referee effects are outside the theorem; their maximum pairwise overlaps do not automatically give a jointly attainable Gram matrix.

For independently sampled questions with common probability $`p`$ of choosing $`P`$, the kernel is a tensor power of

```math
\begin{pmatrix}
p&c\sqrt{p(1-p)}\\
c\sqrt{p(1-p)}&1-p
\end{pmatrix}.
```

Its exact $`n`$-coordinate value is therefore

```math
\left[\frac{1+\sqrt{(2p-1)^2+4p(1-p)c^2}}2\right]^n.
```

For unbiased BB84, $`p=1/2`$ and $`c=1/\sqrt2`$. Define

```math
\beta=\frac{1+c}{2}=\cos^2(\pi/8),\qquad
q_*=1-\beta,\qquad
\kappa=\frac{q_*}{\beta}=3-2\sqrt2.
```

The value becomes $`\beta^n`$. The [related-work account](../references/RELATED_WORK.md#russo2017) locates the nonuniform two-projective-question problem and the inherited uniform results.

## An attack on honest qubits

**Milestone [M17](milestones.md#m17).**

An abstract optimal referee state need not have marginal $`I/2^n`$. Source replacement alone therefore proves only an upper bound for honest BB84 splitting. To obtain an exact physical value, the project constructs a valid measurement on the honestly supplied qubits.

For BB84, put

```math
M_\mu=\sum_\theta\mu(\theta)|0^\theta\rangle\langle0^\theta|,
\qquad \omega(\mu)=\|M_\mu\|_\infty.
```

Take a normalized top eigenvector $`\psi`$. Let $`\mathsf X|b\rangle=|b\oplus1\rangle`$ and $`\mathsf Z|b\rangle=(-1)^b|b\rangle`$ be the Pauli operators. For two $`n`$-bit strings $`u,v`$, write $`P_{uv}=\mathsf X^u\mathsf Z^v`$. The proposed measurement effects are

```math
E_{uv}=\frac1dP_{uv}|\psi\rangle\langle\psi|P_{uv}^\dagger,
\qquad d=2^n.
```

There are $`d^2`$ effects. Their sum is the identity because averaging a trace-one operator over all Pauli conjugations gives $`I/d`$. Thus this is a normalized physical POVM.

The splitter measures it and broadcasts the classical pair $`(u,v)`$ to both recipients. After learning $`\theta`$, each outputs $`u_i`$ at computational-basis positions and $`v_i`$ at Hadamard-basis positions. For any fixed input $`|x^\theta\rangle`$, exactly $`d`$ outcomes give the correct string. Summing their probabilities yields $`|\langle\psi|0^\theta\rangle|^2`$. Averaging over $`\theta`$ gives $`\langle\psi|M_\mu|\psi\rangle=\omega(\mu)`$.

This proves [Theorem B](../science/bb84_cloning.md#theorem-honest-preparation-has-the-same-value). Quantum memories at the recipients cannot improve the optimum in this particular honest-source experiment. The attaining measurement can nevertheless be collective and computationally expensive. No efficient implementation of the optimal adversarial POVM is asserted.

For independent uniform bases, $`\psi`$ is a product of single-qubit Breidbart vectors, halfway between the two zero-labelled basis vectors. The corresponding local measurement guesses a bit correctly with probability $`\beta`$ in either basis. Its product version succeeds with probability $`\beta^n`$ for **every** basis distribution, supplying a universal attack later used in the converse.

## The code formula and a worked example

**Milestone [M18](milestones.md#m18).**

Let the basis be uniform on a binary linear code $`C`$ of dimension $`k`$. Translation by any codeword permutes the code. Every row of its spectral kernel consequently has the same sum,

```math
2^{-k}\sum_{c\in C}2^{-|c|/2}.
```

The all-ones vector is an eigenvector with this value, and the maximum row sum bounds all eigenvalues. The exact result is

```math
\omega(C)=2^{-k}W_C(1/\sqrt2)
=\beta^nW_{C^\perp}(\kappa).
```

The second expression follows by inserting the character identity from the preliminary discussion and factoring over coordinates. It separates the independent-basis value $`\beta^n`$ from a nonnegative penalty due to dual-code words. The zero dual word contributes one; every nonzero word contributes $`\kappa^{|r|}`$. Since $`\kappa<1`$, short dual words contribute much more than long ones. [Theorem C](../science/codes_and_leakage.md#exact-code-formula) gives both derivations and credits the linear-code upper bound already latent in Fehr–Salvail's proof.

### Two qubits controlled by one shared basis bit

Take $`C=\{00,11\}`$. A uniform one-bit seed selects either the computational basis on both qubits or the Hadamard basis on both. Each individual basis bit is uniform, but the two bits are perfectly correlated. The kernel is

```math
K=\frac12\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
```

Its eigenvectors are the equal and opposite combinations of the two indices. Their eigenvalues are $`3/4`$ and $`1/4`$, so the exact simultaneous recovery probability is $`3/4`$.

The code formula gives the same answer: its weights are zero and two, hence $`W_C(t)=1+t^2`$ and

```math
\omega(C)=\frac12(1+c^2)=\frac34.
```

The physical construction is explicit. Its top frame vector is

```math
|\psi_C\rangle=\frac{|00\rangle+|++\rangle}{\sqrt3}.
```

The denominator follows from $`\langle00|++\rangle=1/2`$. Use this vector in the sixteen-outcome Pauli POVM, with each effect scaled by $`1/4`$. Send its two two-bit labels $`u,v`$ to both recipients. If the later basis is $`00`$, both return $`u`$; if it is $`11`$, both return $`v`$. The previous success calculation gives $`3/4`$ on the honest uniform data string.

Independent uniform bases instead use two seed bits and give $`\beta^2\approx0.728553`$. Their one-coordinate basis distributions are identical to those of the correlated example. The full basis distribution is what determines the difference.

### One leaked coordinate versus one leaked parity

For three qubits, revealing one basis coordinate leaves success $`\beta^2\approx0.728553`$. Revealing the parity of all three bases leaves each posterior on a coset of

```math
C=\{000,011,101,110\},\qquad C^\perp=\{000,111\}.
```

Its value is $`(1+3c^2)/4=5/8`$. Both revelations are one classical bit. Their effects differ because one introduces a weight-one dual word, while the other introduces a weight-three word. More generally, a disclosed parity supported on $`w`$ coordinates, with $`1\le w\le n`$, gives $`\beta^n(1+\kappa^w)`$. This is the operational meaning of basis-information geometry.

## Random codes and the optimal seed rate

**Milestones [M19](milestones.md#m19)–[M20](milestones.md#m20).**

Sample a public code uniformly from all $`k`$-dimensional subspaces of $`\mathbb F_2^n`$. Its dual has dimension $`n-k`$. Every nonzero vector has the same probability of belonging to that dual. Counting its $`2^{n-k}-1`$ nonzero members among the $`2^n-1`$ possibilities gives

```math
p_{n,k}=\frac{2^{n-k}-1}{2^n-1}.
```

Average the dual enumerator one word at a time. Since $`\sum_r\kappa^{|r|}=(1+\kappa)^n=\beta^{-n}`$, the exact mean is

```math
\mathbb E_C\omega(C)
=\beta^n+p_{n,k}(1-\beta^n)
\le\beta^n+2^{-k}.
```

The adversary knows the public code and can optimize separately for each realization. The expectation already averages those optimized values; it is not a bound for an attacker forced to ignore setup information.

Define $`\alpha=-\log_2\beta\approx0.2284467`$. For every $`\varepsilon>0`$, Markov's inequality applied to the nonnegative quantity $`W_{C^\perp}(\kappa)-1`$ gives

```math
\Pr_C[W_{C^\perp}(\kappa)>1+\varepsilon]
\le\varepsilon^{-1}2^{\alpha n-k}.
```

Thus, whenever the integer dimension satisfies $`\alpha n+2t\le k\le n`$, all but a fraction $`2^{-t}`$ of public codes have $`\omega(C)\le(1+2^{-t})\beta^n`$. This is a guarantee for most fixed setups. The exact mean is a separate, often sharper guarantee when setup remains part of the security experiment.

Two attacks show the rate is optimal within this basis-selection architecture. A source with at most $`2^k`$ possible bases has a most likely basis of probability at least $`2^{-k}`$. Measuring in that guessed basis and copying the resulting string succeeds whenever the guess is correct. Independently, the product Breidbart attack succeeds with probability $`\beta^n`$ for every distribution. Therefore

```math
\omega(\mu)\ge\max\{2^{-k},\beta^n\}.
```

The random-code mean is at most the sum of these two unavoidable terms. Their maximum and sum differ by at most a factor of two. The largest achievable negative logarithm of complete-string success consequently differs from $`\min\{k\ln2,-n\ln\beta\}`$ by at most $`\ln2`$. Dividing by $`n`$ gives the optimal exponent per qubit in the asymptotic limit.

Retaining the full independent-basis exponent requires asymptotically at least $`\alpha n`$ secret basis bits; random linear bases attain that rate with sublinear slack. A multiplicative penalty tending to one with high probability requires growing slack, for example $`k\ge\alpha n+2t_n`$ with $`t_n\to\infty`$ and $`t_n=o(n)`$.

The public generator has $`O(nk)`$ bits and can be sampled and applied with polynomial classical work. It must come from the stated honest setup distribution. The theorem does not provide an efficient test of the full weight enumerator, an explicit optimal deterministic family, or an optimal key length for every quantum encryption architecture. These distinctions are part of [Theorem R and its converse](../science/codes_and_leakage.md#exact-mean-of-a-random-code).

## One certificate for subsets and noise

**Milestones [M21](milestones.md#m21)–[M23](milestones.md#m23).**

Suppose only positions in $`J`$ are retained. A uniform codeword projects uniformly onto $`C|_J`$. Its dual consists of dual words supported entirely inside $`J`$, restricted to those positions:

```math
R_J=\{r|_J:r\in C^\perp,\ \mathrm{supp}\,r\subseteq J\}.
```

This is **shortening** the dual. Simply projecting every dual word would impose constraints that need not hold on the retained coordinates.

The recipients still receive the full basis. To use a projected-game bound, trace out the unused referee systems. The remaining state is independent of every basis bit. For each fixed retained basis, each possible unused-basis context selects a pair of local measurements on that same state. Averaging these choices cannot outperform the best pair available for the retained basis. This proves the [subset reduction](../science/noise_and_loss.md#why-knowledge-of-unused-basis-bits-does-not-break-this-bound) without assuming coordinatewise attacks.

Let $`W_i`$ indicate that the referee and both recipients agree correctly at position $`i`$. On $`J`$, let

```math
L_J=|J|-\sum_{i\in J}W_i.
```

This counts positions on which at least one recipient is wrong. For $`0\le s\le1`$, expand $`s^{L_J}=\prod_{i\in J}[s+(1-s)W_i]`$. All coefficients are nonnegative. Each product of indicators is controlled by a projected-code value. Collecting the resulting terms gives [Theorem N](../science/noise_and_loss.md#exact-form-of-a-moment-upper-bound):

```math
\mathbb E[s^{L_J}]
\le a_s^{|J|}W_{R_J}(b_s/a_s),
\qquad
a_s=\beta+q_*s,\quad b_s=q_*(1-s).
```

It is a moment upper bound, not a claim that every noisy event has an exact known optimum. Because $`R_J`$ is contained in the original dual after zero extension and $`b_s/a_s\le\kappa`$, the single certificate

```math
W_{C^\perp}(\kappa)\le1+\varepsilon
```

implies $`\mathbb E[s^{L_J}]\le(1+\varepsilon)(\beta+q_*s)^{|J|}`$ for every retained set and every such $`s`$. No union bound over the exponentially many sets is needed.

Now suppose both recipients must return the **same** answer on $`J`$, and that answer may have at most $`r`$ errors. Acceptance implies $`L_J\le r`$. For $`h=|J|>0`$ and $`\gamma=r/h<q_*`$, minimizing the moment bound over $`s`$ gives

```math
\Pr[\mathrm{accept}]
\le\min\{1,(1+\varepsilon)e^{-hD(\gamma\|q_*)}\},
```

where

```math
D(\gamma\|q)=\gamma\ln\frac\gamma q
+(1-\gamma)\ln\frac{1-\gamma}{1-q}.
```

The minimizer is $`s=\gamma\beta/[q_*(1-\gamma)]`$; at zero errors, take its limit. The formula explains why the relevant error threshold is $`q_*\approx0.1464466`$.

The product Breidbart attack returns identical answers. Its errors are independent with probability $`q_*`$ even after conditioning on an arbitrary full basis string. Its lower tail has the same exponent. Thus the exponent is asymptotically sharp when $`\log(1+\varepsilon)=o(h)`$. This does not establish an exact finite-block binomial-tail optimum.

Agreement is a substantive condition. If the recipients may make different errors and each is allowed $`r`$, their union of error positions can have size $`2r`$. The argument then uses $`2r/h`$, rather than $`r/h`$, when that fraction is below $`q_*`$. The sharp unrestricted separate-error problem is outside the result.

## Loss and branch independence

**Milestone [M24](milestones.md#m24).**

A loss decision can select a retained set. Let $`Z=z`$ identify a branch with retained set $`J_z`$. The sufficient hypothesis is that, before basis disclosure, the joint state factors branch by branch as

```math
\rho_{\Theta ZABD}
=\sum_{\theta,z}\mu_C(\theta)
|\theta,z\rangle\langle\theta,z|
\otimes\widetilde\rho^z_{ABD},
\qquad \sum_z\mathrm{Tr}\,\widetilde\rho^z_{ABD}\le1.
```

The trace of each subnormalized state is its branch weight. Its quantum content does not depend on $`\theta`$. Apply the previous theorem to each normalized branch and multiply back by that weight. If every accepted branch retains at least $`h_0`$ positions and allows agreed error fraction at most $`\gamma<q_*`$, their total unconditional acceptance is at most

```math
\min\{1,(1+\varepsilon)e^{-h_0D(\gamma\|q_*)}\}.
```

Source replacement establishes the factorization for an instrument acting on honest uniform-string BB84 inputs before basis disclosure, with no additional basis-correlated information. It also works after fixing an already disclosed classical syndrome and using the corresponding affine basis set.

The timing of an announcement alone does not establish independence. An attacker with basis-correlated side information might choose a branch using that information. Nor can one divide by a small acceptance probability and retain the same unconditional bound. The [branch theorem](../science/noise_and_loss.md#loss-commitments-and-subnormalized-branches) states exactly what is required; position-verification protocols need their own reduction to that setting.

## Quantum basis information

**Milestone [M25](milestones.md#m25).**

Consider the basis-correlated register

```math
\rho_{\Theta E}
=\frac1{|C|}\sum_{\theta\in C}
|\theta\rangle\langle\theta|\otimes|0^\theta\rangle\langle0^\theta|.
```

A preparation channel forwards $`E`$ unchanged to the referee and gives the two recipients no quantum systems. Both recipients always answer $`0^n`$. The referee measures in the actual basis $`\theta`$ and obtains $`0^n`$ with certainty. The success probability is one.

Yet $`E`$ need not identify the basis well. For the full cube, identifying one basis bit means distinguishing $`|0\rangle`$ from $`|+\rangle`$ with equal priors. The Holevo–Helstrom formula gives success $`\beta`$. The full-string discrimination value is exactly $`\beta^n`$.

The upper bound in that last assertion has an explicit certificate. With $`\rho_0=|0\rangle\langle0|`$ and $`\rho_1=|+\rangle\langle+|`$, set

```math
Y=\frac14\bigl(\rho_0+\rho_1+|\rho_0-\rho_1|\bigr).
```

It dominates both $`\rho_0/2`$ and $`\rho_1/2`$ and has trace $`\beta`$. Its tensor power dominates every weighted product state, so any joint discrimination measurement succeeds with probability at most $`\beta^n`$. Product optimal measurements attain this value. The argument does not assume a general multiplicativity principle without proof.

This separates **identifying a basis** from **using a quantum state aligned with it**. It refutes the proposed additive extension $`p_{\mathrm{win}}\le P_{\mathrm{guess}}(\Theta|E)+2^{-d(C)/2}`$ asked about in Fehr–Salvail's Remark 3: for the full cube, $`d(C)=1`$, and at $`n=8`$ the proposed right side is about $`0.988845<1`$. The [scientific page](../science/quantum_side_information.md) also gives a positive-distance family where both terms tend to zero exponentially.

The example uses an $`n`$-qubit side register and an adversarial referee-preparation channel. It does not give perfect cloning of an honestly supplied unknown uniform BB84 message. It leaves the proved multiplicative FS bound and authentication protocol intact. The independence hypothesis of the exact spectral theorem is simply absent.

## Two encryption applications

**Milestones [M26](milestones.md#m26)–[M27](milestones.md#m27).**

The exact recovery value enters two different one-time encryption constructions. Their full derivations and primary attributions are in [applications](../science/applications.md).

### A full-message conjugate pad

Share independent uniform keys $`U\in\mathbb F_2^k`$ and $`P\in\mathbb F_2^n`$. Encrypt an $`n`$-bit classical message $`m`$ as

```math
|(m\oplus P)^{GU}\rangle.
```

Averaging $`P`$ produces $`I/2^n`$ for every fixed message and basis. Ordinary one-time privacy is therefore perfect. For an independent uniform random message $`M`$, the variable $`X=M\oplus P`$ is uniform and independent of the keys. After a split and full key disclosure, both recipients recovering $`M`$ is exactly the BB84 search task, after relabelling their answers by $`P`$. Its optimal success is $`\omega(C)`$.

This does not imply unclonable indistinguishability for chosen messages. For $`n\ge2`$, choose $`0^n`$ and $`1^n`$. Give one ciphertext qubit to each recipient. After the key is disclosed, each recovers one plaintext bit, which identifies the chosen message perfectly. The distinction between complete random-message recovery and one-bit decision is operational, not merely terminological.

### One bit through the inherited common-mask theorem

Now use secret key $`(U,R)`$, with $`R\in\mathbb F_2^n`$ uniform and independent. To encrypt a bit $`b`$, sample fresh local uniform $`X`$ and send

```math
\bigl(|X^{GU}\rangle,\ c=b\oplus R\cdot X\bigr).
```

The visible $`c`$ is ciphertext; $`R`$ remains secret until after the split. The [CLX common-mask theorem](../references/RELATED_WORK.md#clx2026) relates joint prediction of $`R\cdot X`$ to full recovery:

```math
p_{\mathrm{Search}}\ge(2p_{\mathrm{Pred}}-1)^4.
```

Substituting $`p_{\mathrm{Search}}=\omega(C)`$ gives decision success at most $`1/2+\omega(C)^{1/4}/2`$.

The visible ciphertext bit needs care. For uniform challenge $`b`$, changing variables from $`b`$ to $`c`$ makes $`c`$ independent of $`X,U,R`$. A prediction-game splitter can therefore sample $`c`$ itself, run any $`c`$-dependent encryption attack, and let both recipients XOR $`c`$ into their final answers. This exactly preserves simultaneous success; the reduction does not assume the attacker ignores the classical ciphertext.

Ordinary privacy here is statistical. When $`X=0`$, the parity is always zero; for every nonzero $`X`$, averaging $`R`$ makes it uniform. The two key-averaged ciphertext states have exact trace distance $`2^{-n}`$, independently of the code. Their optimal ordinary distinguishing success is $`1/2+2^{-n-1}`$.

Both constructions use $`n+k`$ shared secret-key bits. At the optimal basis rate this is $`(1+\alpha)n+o(n)`$; the second also uses $`n`$ fresh local random coins and a one-bit classical ciphertext. The first retains the full search exponent; the second retains the exponent divided by four that the inherited compiler certifies. This is not a proof that the one-bit exponent is tight or that this basis rate is necessary for every indistinguishability scheme. Key reuse, noisy encryption and multibit composition require separate arguments.

## Noiseless key recycling

**Milestones [M28](milestones.md#m28)–[M29](milestones.md#m29).**

The authentication application refines the analysis of an existing protocol. In Fehr–Salvail authentication, the parties share a classical MAC key $`K`$ and a basis key $`\Theta\in C`$. Alice chooses fresh uniform $`X`$, sends $`|X^\Theta\rangle`$, and authenticates $`m\|X`$ with a classical tag. Bob measures in basis $`\Theta`$ and verifies the received message and tag using his outcome.

Acceptance retains both keys. Rejection retains $`K`$ and replaces $`\Theta`$ using fresh shared uniform randomness from a reliable private refresh resource. Eve learns the decision and may retain quantum information. The model requires synchronized sequential use.

The MAC needs more than ordinary one-time substitution security. For every fixed message $`m`$, its tag $`T=\mathrm{MAC}(K,m\|X)`$ must have a distribution independent of $`X`$ under a uniform key. It must also satisfy **ideal key privacy**: whenever $`K`$ is uniform and independent of $`X`$, and side information $`F`$ obeys $`K\leftrightarrow XT\leftrightarrow F`$,

```math
\Delta(K|TF)\le\frac12\sqrt{|\mathcal T|\,P_{\mathrm{guess}}(X|TF)}.
```

Here $`\mathcal T`$ is the tag set, and $`\Delta(K|F)=\tfrac12\|\rho_{KF}-U_{\mathcal K}\otimes\rho_F\|_1`$ measures distance from an independent uniform MAC key. The Markov relation means that, conditional on $`X,T`$, the state of $`F`$ does not depend further on $`K`$. Thus limited information about $`X`$ implies limited information about $`K`$ even when the tag is known. The [protocol hypotheses](../science/key_recycling.md#1-protocol-and-hypotheses) identify suitable constructions; ordinary MAC security alone does not imply this property.

Write $`g=P_{\mathrm{guess}}(\Theta|E)`$ for Eve's initial basis knowledge, and require $`K`$ initially uniform and independent of $`\Theta,E`$. A state-discrimination dual certificate gives a normalized state $`\sigma_E`$ such that

```math
\rho_{\Theta E}\preceq g|C|\,U_C\otimes\sigma_E.
```

Apply the physical operations and the success test to both sides. On the right, basis and preparation are independent, so the exact code value applies. The resulting simultaneous-guessing bound is $`g|C|\omega(C)`$. This is a multiplicative quantum-information reduction, consistent with the preceding separation.

The one-use analysis retains the original tag throughout Eve's side information. An idealized decision accepts only an unchanged message/tag and a correct decoded $`X`$. Replacing the real decision incurs the MAC-forgery error. In the ideal analysis, the two branches $`X=X'`$ and $`X\ne X'`$ each contribute at most $`g|C|\omega(C)`$ to the relevant subnormalized guessing probability used by key privacy. Together with the basis-key argument, this gives the one-use estimates

```math
P_{\mathrm{guess}}(\Theta'|E')\le g+|C|^{-1},
```

```math
\Delta(K|\Theta'E')
\le2\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}\sqrt{g|C|\omega(C)|\mathcal T|}.
```

The final information $`E'`$ includes the decision, original tag and Eve's remaining system. The coefficient $`1/\sqrt2`$ comes from the two guessing branches and the one-half factor in key privacy. For a message selected by measuring Eve's prior state, the proof conditions on that classical message and averages using data processing and Jensen's inequality. The [complete one-use proof](../science/key_recycling.md#4-one-execution-mac-key-privacy-and-its-constants) handles these details explicitly.

To analyze round $`i`$, compare the real process with one that hypothetically replaces the MAC key by a fresh independent key before each round. Starting with both keys uniform and independent of each other and of Eve, the incoming basis guessing probability in that comparison sequence at round $`j`$ is at most $`j/|C|`$. Trace-distance errors accumulate only over earlier rounds. The accepted substitution probability in round $`i`$ is therefore bounded by

```math
\varepsilon_i\le(2i-1)\varepsilon_{\mathrm{MAC}}
+\frac1{\sqrt2}\sqrt{\omega(C)|\mathcal T|}
\sum_{j=1}^{i-1}\sqrt j.
```

This is a per-round statement. The probability of any failure over many rounds needs the corresponding aggregation.

For example, for a positive integer $`\lambda`$, choose $`\varepsilon_{\mathrm{MAC}}=2^{-\lambda}`$, $`|\mathcal T|=2^\lambda`$, $`k=3\lambda`$ and $`n=\lceil3\lambda/\alpha\rceil`$. Under the honest random public setup, the exact mean and Jensen yield

```math
\mathbb E_C\varepsilon_i
\le\left(2i-1+\sum_{j=1}^{i-1}\sqrt j\right)2^{-\lambda}.
```

This uses about $`13.1322\lambda`$ qubits. The comparison in [the parameter analysis](../science/key_recycling.md#6-concrete-parameter-refinement) uses the earlier minimum-distance choice with a random-linear Gilbert–Varshamov certification, which gives about $`21.2424\lambda`$ qubits. The approximately 38.18% reduction compares those two certification routes. It is not a lower bound on other codes or on all recycling protocols.

The refinement keeps the noiseless FS protocol, tag assumptions, refresh resource and sequential comparison argument. The agreement-noise theorem cannot simply replace the noisy FS argument, whose joint success event is different. Nor does this analysis justify arbitrary later uses of the retained MAC key outside the specified protocol.

## The complete scientific picture

**Milestone [M30](milestones.md#m30).**

The result is a connected chain with distinct reasons at each step.

| Connection | Mathematical reason | Essential boundary |
| --- | --- | --- |
| Correlated questions to exact value | Projector overlaps, a weighted Gram bound and matching principal vectors | Two fixed finite-dimensional referee PVMs; basis-independent preparation |
| Abstract value to honest BB84 splitting | Source replacement and a normalized Pauli POVM | Uniform data independent of the basis; disclosure after splitting |
| Linear basis sets to short seeds | Constant row sums, dual enumerators and exact random-subspace counting | Honest public setup; optimality concerns this complete-string basis architecture |
| One code to all retained sets and agreed noise | Shortened duals and a positive moment expansion | Agreement on answers and the stated branch independence |
| Quantum basis information to a separation | Forwarding a correctly aligned state can avoid identifying its basis | Adversarial preparation, rather than perfect cloning of an unknown honest message |
| Recovery value to encryption or authentication | Explicit protocol reductions with separately charged resources | The stated one-time or noiseless sequential model |

The broad conclusion is that basis information has an operational geometry. The spectral matrix retains that geometry, the code identities expose it, and the applications use it only after their information flow and success predicates have been matched to the correct game.

For a theorem-focused continuation, use [the scientific map](../science/README.md). For attribution and imported proof dependencies, use [related work](../references/RELATED_WORK.md). For the worked finite checks and their limits, use [verification](../verification/README.md). The [milestone map](milestones.md) records the common understanding targets independently of any reader's study history.
