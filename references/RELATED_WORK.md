# Related work and attribution

The results concern the exact joint guessing probability when the referee chooses among products of two projective measurements. The BB84 specialization connects that probability to the distribution of the secret bases, a physical splitting attack, and the weight enumerator of a basis code. The sources below identify the previous results used in the proofs and the distinctions between their security models.

## TFKW2013

**Marco Tomamichel, Serge Fehr, Jędrzej Kaniewski and Stephanie Wehner.** “A monogamy-of-entanglement game with applications to device-independent quantum cryptography.” *New Journal of Physics* **15** (2013), 103002. [Paper](https://arxiv.org/abs/1210.4359) · [DOI](https://doi.org/10.1088/1367-2630/15/10/103002).

TFKW introduced the relevant monogamy game and proved the exact independent uniform BB84 value

```math
\left(\frac12+\frac1{2\sqrt2}\right)^n.
```

Their comparison of winning projectors supplies the key quantum inequality used here. If two basis strings differ in $`d_H(\theta,\phi)`$ coordinates, the overlap of their winning subspaces is at most $`2^{-d_H(\theta,\phi)/2}`$. The [spectral proof](../science/spectral_value.md) retains this pairwise information in a weighted scalar Gram matrix. The projector method and the uniform-basis result are inherited from TFKW.

## JMRW2016

**Nathaniel Johnston, Rajat Mittal, Vincent Russo and John Watrous.** “Extended non-local games and monogamy-of-entanglement games.” *Proceedings of the Royal Society A* **472** (2016), 20160003. [Journal](https://doi.org/10.1098/rspa.2016.0003) · [arXiv:1510.02083v2](https://arxiv.org/pdf/1510.02083).

JMRW prove that the quantum and unentangled values coincide for a single-copy monogamy game with two questions. They also obtain exact strong parallel repetition when the two referee measurements are projective and the questions are uniform. In the arXiv version of 28 October 2015, the relevant uniform repetition bound is Theorem 4.2, and the exact two-PVM value is Proposition 4.1. The journal uses different numbering.

The exact theorem here allows arbitrary correlated distributions on the question strings. Independent biased questions give the specialization

```math
\omega^*(G_t^{\otimes n})
=\left(\frac{1+\sqrt{(2t-1)^2+4t(1-t)c^2}}2\right)^n,
\qquad c=\max_{a,b}\|P_aQ_b\|_\infty.
```

Our $`c`$ is the unsquared overlap norm. This convention differs from sources that define the measurement overlap as its square.

## Russo2017

**Vincent Russo.** *Extended Nonlocal Games*. PhD thesis, University of Waterloo, 2017. [arXiv:1704.07375v1](https://arxiv.org/abs/1704.07375) · [Author PDF](https://vprusso.github.io/pdf/thesis.pdf).

Question 7.2, printed p. 108, asks whether the projective two-question repetition result persists for nonuniform question distributions. It separately asks about replacing projective measurements by general POVMs. The biased two-PVM formula above answers the first of these subquestions; the general-POVM question is outside the theorem.

Russo's [“Numerical tools for extended nonlocal games” slides](https://vprusso.github.io/pdf/numerical_enlg_slides.pdf), dated 24 June 2021, retain the uniform/projective restriction on slide 26 and ask for a nonuniform formula on slide 27. These sources document the particular question being addressed. They do not by themselves establish the absence of a later answer.

## FS2017

**Serge Fehr and Louis Salvail.** “Quantum Authentication and Encryption with Key Recycling.” *EUROCRYPT 2017, Part III*, LNCS 10212, pp. 311–338. [Conference PDF](https://ir.cwi.nl/pub/25750/EURO7412.pdf) · [DOI](https://doi.org/10.1007/978-3-319-56617-7_11) · [ePrint 2017/102](https://eprint.iacr.org/2017/102) · [Corrected author version](https://arxiv.org/html/1610.05614v3).

The analysis uses arXiv:1610.05614v3, dated 19 May 2017. Its title-page note identifies the proceedings and ePrint versions with v2.

FS17 already chooses BB84 bases from a code to reduce basis-key and refresh randomness. Proposition 1 bounds the simultaneous guessing probability by

```math
|C|^{-1}+2^{-d(C)/2}.
```

Its proof explicitly contains the full pairwise overlap $`2^{-d_H(\theta,\phi)/2}`$ before replacing distance by the minimum distance. For a linear code, retaining those distances in the same permutation bound already gives

```math
\omega(C)\le |C|^{-1}W_C(2^{-1/2}).
```

Thus coded bases and this linear-code upper bound are already present, explicitly or as an immediate refinement, in FS17. The [code analysis here](../science/codes_and_leakage.md) supplies equality, the arbitrary-prior spectral characterization, the resulting optimal basis-randomness exponent, and a common certificate for retained coordinate sets.

Corollaries 1–2 allow quantum side information before referee-state preparation. Remark 3 asks whether a sharper classical-side-information expression also holds for quantum information. The [counterexample here](../science/quantum_side_information.md) answers that stated extension negatively. It does not contradict the proved FS17 bound or constitute an attack on the FS17 protocol.

## Encryption and the security definition

### BL2020

**Anne Broadbent and Sébastien Lord.** “Uncloneable Quantum Encryption via Oracles.” *TQC 2020*, LIPIcs 158, pp. 4:1–4:22. [Proceedings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TQC.2020.4) · [arXiv:1903.00130](https://arxiv.org/abs/1903.00130).

Broadbent–Lord formalize an encryption task in which two separated recipients try to recover the same plaintext after receiving the key. Conjugate coding and monogamy bounds are ingredients in their constructions. The physical BB84 search experiment used here is in this two-recipient setting. The [physical attainment proof](../science/bb84_cloning.md) handles the honest input and its maximally mixed referee marginal explicitly.

### CLX2026

**Andrea Coladangelo, Qipeng Liu and Ziyi Xie.** “Unclonable encryption from BB84 states: a simultaneous Goldreich–Levin reduction.” [arXiv:2608.17629v2](https://arxiv.org/html/2608.17629), 5 October 2026.

Definition 3.1 allows an arbitrary joint distribution on a finite key and a hidden string. Definition 3.3 reveals a common uniformly random inner-product mask after splitting. Theorem 3.4 proves

```math
p_{\rm Search}\ge (2p_{\rm Pred}-1)^4.
```

Corollary 1.2 gives the one-bit BB84 encryption scheme with secret key $`(\theta,r)`$ and ciphertext $`(H^\theta|x\rangle,b\oplus\langle r,x\rangle)`$. The [application](../science/applications.md) uses this existing compiler with a coded basis. A $`k`$-bit basis seed and its independent $`n`$-bit mask require $`n+k`$ secret bits. The generic compiler and its fourth-power loss are credited to CLX. The sharp optimality statement in this project concerns the underlying search task's basis randomness, not the total key length or prediction exponent of arbitrary encryption schemes.

### Leermakers–Škorić2021

**Daan Leermakers and Boris Škorić.** “Qubit-based Unclonable Encryption with Key Recycling.” *Quantum Information and Computation* **21**(11–12) (2021), pp. 901–930. [Journal PDF](https://www.rintonpress.com/xxqic21/qic-21-1112/0901-0930.pdf) · [arXiv:2004.04084](https://arxiv.org/abs/2004.04084) · [ePrint 2020/172](https://eprint.iacr.org/2020/172).

The journal version was revised 27 June 2021; the served arXiv v2 is dated 28 April 2020. Definition 6 protects a message after an accepted honest decryption even if keys subsequently leak. Footnote a expressly distinguishes this from the Broadbent–Lord two-recipient definition. Its code encodes the payload, and Eq.(22) samples the full basis sequence uniformly. Theorems 1–3 establish asymptotic rate results using privacy amplification and key refresh.

The key-recycling and accepted-decryption rates in that paper are therefore different operational quantities from the exact joint search probability studied here. An improvement to the FS17 parameter instantiation should be compared within that protocol and security model.

## Loss, conditioning and composition

**Llorenç Escolà-Farràs and Florian Speelman.** “Lossy-and-Constrained Extended Non-Local Games with Applications to Quantum Cryptography.” *Quantum* **9** (2025), 1712. [Journal](https://quantum-journal.org/papers/q-2025-04-18-1712/) · [v2 manuscript, 9 April 2025](https://ir.cwi.nl/pub/35167/35167.pdf). This work studies constraints and loss using SDP hierarchies; §5.3.1 considers two-copy lossy BB84 repetition.

### Loss2026

**Llorenç Escolà-Farràs, Boris Škorić and Florian Speelman.** “Arbitrarily Loss-Tolerant Quantum Position Verification in a Single Execution.” [arXiv:2606.25037v2](https://arxiv.org/html/2606.25037v2), 1 October 2026. This work develops a protocol with commitments before classical challenges and uses instruments, subnormalized branches, nets and concentration in its analysis.

The [retained-set bound here](../science/noise_and_loss.md) is a monogamy statement under an explicit independence condition on the branch label and remaining quantum state. The standard subnormalized-branch summation is not a new protocol reduction. Any use in a concrete QPV protocol requires that protocol's timing, resource and conditioning assumptions.

**Christopher Portmann.** “(Quantum) Min-Entropy Resources.” [arXiv:1705.10595](https://arxiv.org/abs/1705.10595), 2017. Portmann gives a composable treatment of min-entropy resources and a modified FS17 protocol. The parameter substitution into the original FS17 sequential argument is not a new universal-composability theorem.

## Earlier correlated-basis and discrimination work

**L.-P. Lamoureux, H. Bechmann-Pasquinucci, N. J. Cerf, N. Gisin and C. Macchiavello.** “Reduced randomness in quantum cryptography with sequences of qubits encoded in the same basis.” *Physical Review A* **73** (2006), 032304. [Paper](https://arxiv.org/abs/quant-ph/0507058) · [DOI](https://doi.org/10.1103/PhysRevA.73.032304). This work studies repeated bases and cloning fidelities. Correlated BB84 bases and randomness reduction thus have earlier precedents; the success criterion here is exact simultaneous recovery of the entire hidden string.

The measurement-and-broadcast realization also belongs to the setting of state discrimination with information revealed after measurement. **D. Gopal and S. Wehner**, [“Using post-measurement information in state discrimination”](https://arxiv.org/abs/1003.0716), develop this general framework and SDP optimality conditions. The present analysis proves the specific BB84 value and exhibits a normalized covariant POVM attaining it.

## Educational foundation

**John Watrous.** *The Theory of Quantum Information*. Cambridge University Press, 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides a prepublication manuscript and errata. This is the project's single educational anchor for finite-dimensional operators, states, channels, measurements and state discrimination. The [source bridge](../learning/watrous_bridge.md) maps the relevant sections to the proofs here; the research citations above supply the separate monogamy and cryptographic ingredients.

## Mathematical ingredients and scope

The Gram/frame eigenvalue correspondence, operator-norm comparison, MacWilliams transform, random-subspace inclusion probabilities, Markov's inequality and subset-moment Chernoff argument are standard ingredients. They are proved or instantiated explicitly where used. The sharp spectral and coding statements should be distinguished from these tools.

The comparison above records the relevant statements in identified primary versions. It does not make an exhaustive priority claim. In particular, it neither introduces the coded-basis setting nor claims a new generic concentration theorem, universal encryption optimum, or unrestricted theorem for quantum basis leakage.
