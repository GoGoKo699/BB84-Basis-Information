# What the basis information costs

[Scientific map](README.md) · [Codes and leakage](codes_and_leakage.md) · [Encryption](applications.md) · [Key recycling](key_recycling.md)

## A spectrum rather than a minimum distance

The exact linear-code value has two equivalent forms:

```math
\omega(C)=\frac1{|C|}\sum_{c\in C}2^{-|c|/2}
=\beta^n\left(1+\sum_{r\in C^\perp\setminus\{0\}}\kappa^{|r|}\right).
```

The first form averages all overlaps with a reference basis. The second expresses the excess above the independent-basis benchmark. Low-weight dual relations carry much larger penalties than long parities because $`\kappa=3-2\sqrt2\approx0.171573`$.

A minimum-distance estimate replaces every nonzero primal overlap by the largest permitted overlap. That is convenient but discards most of the distribution. An exact random-code average can therefore certify a better rate without introducing a new quantum operation or relying on a new hardness assumption.

## What is optimal

The two unavoidable strategies are guessing a likely basis and using a basis-independent Breidbart measurement. They impose respectively $`2^{-k}`$ and $`\beta^n`$ lower bounds. Random linear bases have average value at most their sum. Thus

```math
-\log_2\omega_{\mathrm{best}}(n,k)
=\min\{k,\alpha n\}+O(1),
\qquad \alpha=-\log_2\beta.
```

Here the optimization is over basis distributions generated with at most $`k`$ uniform seed bits in the stated complete-string recovery architecture. This is a sharp exponent statement. It is not a lower bound on the total key of every quantum encryption scheme or on security in every unclonability game.

With a public random code, the attacker may adapt to the code. Average security is still bounded by the exact expected optimized value. If a fixed code must have a near-unit multiplicative penalty, the separate high-probability certificate quantifies the seed slack and exceptional setup probability.

For example, at $`n=1024`$, taking $`k=298`$ gives $`k\ge\alpha n+64`$. At least a fraction $`1-2^{-32}`$ of honestly sampled codes satisfy $`W_R(\kappa)\le1+2^{-32}`$. Every such code retains the complete-string bound and all the subset/noise bounds. The finite setup uses 298 secret basis bits; the asymptotic rate 0.2284467 is approached as the relative slack decreases.

## Resources in the applications

| Construction or task | Secret resources | Communication or input | Security statement |
|---|---|---|---|
| Bare BB84 recovery game | $`k`$ hidden basis-seed bits | $`n`$ BB84 qubits | Exact joint recovery value $`\omega(C)`$ |
| Full-message conjugate encryption | $`k+n`$ bits: basis seed and independent pad | $`n`$ qubits carrying an $`n`$-bit plaintext | Perfect ordinary one-time privacy; exact random-message recovery |
| One-bit common-mask encryption | $`k+n`$ bits: basis seed and secret mask | $`n`$ qubits and one classical bit; fresh local $`n`$-bit randomness | Joint bit recovery at most $`1/2+\omega(C)^{1/4}/2`$ by the inherited compiler |
| Noiseless Fehr–Salvail authentication | Original MAC key plus basis seed; fresh shared seed on rejection | $`n`$ qubits, original message/tag and original protocol resources | Sharper one-step recycling and sequential substitution bounds |

All rows also use the public generator. Its $`O(nk)`$ storage and dense multiplication cost are charged classical resources, separate from secret key length. The attack value is information theoretic, so the spectral state or POVM need not have a small circuit.

## What survives losses and errors

The dual certificate has a monotonicity property: shortening the dual only removes terms, and the noise moment evaluates the remaining enumerator at an argument no larger than $`\kappa`$. Therefore a single scalar condition controls all subsets at once.

The loss theorem is an unconditional acceptance bound over subnormalized instrument branches. It does not renormalize a rare successful branch, and it does not allow a retained set to encode information about the unexposed basis. Source replacement supplies the needed independence for honest uniform BB84 data under a pre-disclosure instrument.

The noise threshold $`q_*=14.6447\ldots\%`$ concerns **agreed answers**. Below it, the relative-entropy exponent matches a physical Breidbart attack. It is distinct from finite-block exact noise optimization and from predicates that separately allow different errors for the two players.

## Classical and quantum basis information

Classical leakage selects a posterior basis distribution, which the spectral formula evaluates. A quantum system can instead be used coherently as a correctly aligned referee state while concealing much of the classical basis label. This distinction explains the side-information separation.

The separation does not make quantum side information unmanageable. In the key-recycling application, state-discrimination duality gives a valid **multiplicative** domination bound. What fails is the proposed stronger additive formula in the adversarial-preparation setting.

## The quantitative key-recycling comparison

Under the specific noiseless Fehr–Salvail parameter choice $`k=3\lambda`$, tag length $`\lambda`$ and MAC error $`2^{-\lambda}`$, exact random-code averaging gives

```math
n\sim\frac3\alpha\lambda
=13.13216624\ldots\,\lambda.
```

Their minimum-distance choice, combined with a random-linear Gilbert–Varshamov distance certification, has threshold rate $`R_0`$ solving $`R_0+h_2(2R_0)=1`$. Its corresponding asymptotic qubit coefficient is $`3/R_0=21.24239895\ldots`$. The reduction for **these two certification routes** is about 38.18%.

This is neither a lower bound on all codes nor a comparison to the best rate of every later key-recycling or accepted-decryption encryption protocol. The [application proof](key_recycling.md) states the original resources and gives the exact finite security inequality from which the coefficients follow.

## Bounded conclusions

The account provides a complete characterization of the exact independent-state two-PVM game and the specified BB84 recovery task. General referee POVMs, arbitrary larger measurement families, efficient optimal attack synthesis, deterministic optimal basis-code constructions, unrestricted separate-error noise, and arbitrary basis-dependent erasures require additional arguments.

These boundaries leave the main mechanism intact: the full basis distribution has an exact spectral value, and linear geometry turns that value into a sharp secret-randomness tradeoff with a uniform robustness certificate.
