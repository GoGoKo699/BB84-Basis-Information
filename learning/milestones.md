# Thirty milestones for BB84 Basis Information

[Repository overview](../README.md) · [Watrous bridge](watrous_bridge.md) · [Connected tutorial](tutorial.md) · [Scientific map](../science/README.md)

This map follows the scientific question: **how does the distribution of BB84 bases determine what two separated recipients can recover, and which cryptographic conclusions follow from that recovery value?** Each milestone specifies a conceptual understanding target and the sources that support it.

The allocation is **13 background/preliminaries milestones and 17 narrative/innovation milestones**. The background connects individual states and measurements to joint systems, spectral optimization, classical coding, and precisely defined security experiments. Its final milestone assembles the three models used in the project. The narrative then builds the spectral proof, its physical realization, the code and robustness consequences, and the separately justified cryptographic applications. Its final milestone integrates the claims, resources, and limits.

The single educational anchor is **John Watrous, The Theory of Quantum Information**, using the [author's chapter PDFs](https://cs.uwaterloo.ca/~watrous/TQI/). Chapters 1–3 provide the relevant operator, state, channel, measurement, and discrimination foundations. The [bridge](watrous_bridge.md) explains the notation and missing steps. Coding identities, monogamy arguments, concentration steps, and cryptographic reductions are supplied by the linked project pages and their research references; they are not attributed to the textbook.

The map gives a connected understanding of the project without claiming to enumerate every technical lemma or neighboring topic. The topic pages under [science](../science/README.md) remain the authoritative statements and proofs.

| Phase | Milestones | Local-to-global development |
|---|---|---|
| Background/preliminaries | M01–M13 | A prepared qubit → joint quantum systems and information timing → mathematical tools → the complete security-model distinction |
| Narrative/innovation | M14–M30 | Projector overlaps → an attained spectral value → code geometry and robustness → bounded encryption and authentication consequences |

<a id="background"></a>

## Phase I — Background and preliminaries

<a id="m01"></a>

### M01. States, preparations, and classical labels

**Phase:** Background/preliminaries.

**Central question:** What does a BB84 state describe, and which information remains in the classical labels used to prepare it?

**Understanding target:** Distinguish a pure-state vector, its density operator, and an ensemble with a retained classical label. Explain why averaging a uniform encoded bit can hide information that becomes available after a basis is disclosed.

**Dependencies and story role:** No earlier milestone. Establishes the local physical objects from which every experiment is built.

**Conceptual connection:** Separates the quantum token from the message and basis variables, preventing a mixture of preparations from being mistaken for knowledge of its hidden label.

**Source pointers:** [Watrous §2.1.2, quantum states][W-states]; [the BB84 setting](../science/model.md#what-information-about-the-basis-matters); [physical splitting experiment](../science/model.md#physical-splitting-experiment); [tutorial: qubits and BB84](tutorial.md#qubits-and-bb84).

<a id="m02"></a>

### M02. Measurements, bases, and overlap

**Phase:** Background/preliminaries.

**Central question:** How does the chosen measurement determine which classical outcome can be recovered from a state?

**Understanding target:** Explain outcome probabilities for PVMs and POVMs, the meaning of an outcome projection's range, and the difference between rank-one and higher-rank outcomes. Interpret the unsquared projector overlap used by this project.

**Dependencies and story role:** M01. Moves from state descriptions to the measurement geometry underlying the recovery obstruction.

**Conceptual connection:** Connects computational and Hadamard measurements to the more general problem involving two fixed projective measurements.

**Source pointers:** [Watrous §§2.3.1–2.3.2, measurements][W-measurements]; [abstract-game measurements and overlap](../science/model.md#abstract-game); [tutorial: qubits and BB84](tutorial.md#qubits-and-bb84).

<a id="m03"></a>

### M03. Joint systems and reduced states

**Phase:** Background/preliminaries.

**Central question:** What changes when a measured register is part of a correlated tripartite quantum system?

**Understanding target:** Distinguish a tensor-product space from a product state. Explain partial trace, entanglement across registers, and collective measurements within one player's system. Recognize that discarding a register and conditioning on its measured outcome are different operations.

**Dependencies and story role:** M01–M02. Extends the local measurement picture to the referee and both recipients.

**Conceptual connection:** Supplies the language needed to allow arbitrary collective attacks while later removing unused referee coordinates without introducing postselection.

**Source pointers:** [Watrous §1.1.1, tensor products][W1]; [Watrous §2.1.3, reductions and purifications][W-reductions]; [abstract game](../science/model.md#abstract-game); [tutorial: joint systems and timing](tutorial.md#joint-systems-and-timing).

<a id="m04"></a>

### M04. Channels and the timing of information

**Phase:** Background/preliminaries.

**Central question:** Which operations and information are available before and after the adversary splits the token?

**Understanding target:** Represent preparation, splitting, storage, and processing by quantum channels. Explain why the two recipients may share prior entanglement and use basis-dependent local measurements, yet cannot communicate after separation. Distinguish an information-theoretic attack model from an efficient-circuit restriction.

**Dependencies and story role:** M01 and M03. Places the joint state inside an operational sequence with explicit access to information.

**Conceptual connection:** Makes disclosure timing a model assumption rather than an informal statement that a key is “secret.”

**Source pointers:** [Watrous §2.2.1, channels][W-channels]; [abstract game](../science/model.md#abstract-game); [physical splitting experiment](../science/model.md#physical-splitting-experiment); [charged resources](../science/model.md#conventions-and-charged-resources); [tutorial: joint systems and timing](tutorial.md#joint-systems-and-timing).

<a id="m05"></a>

### M05. Equivalent descriptions and their constraints

**Phase:** Background/preliminaries.

**Central question:** Why can a larger-system description simplify an experiment without changing its observed probabilities?

**Understanding target:** Explain fixed-ancilla projective dilation and deferred EPR preparation. Identify what each preserves: a common ancilla does not reveal the question, and source replacement embeds honest uniform BB84 preparation into a game with a maximally mixed referee marginal. Recognize that this embedding alone does not prove equality with the unrestricted abstract optimum.

**Dependencies and story role:** M02–M04. Completes the operational tools needed to move between measurements and preparation models.

**Conceptual connection:** Links the future universal upper bound to a separate physical attainability requirement.

**Source pointers:** [Watrous §2.3.2, Theorem 2.42 and Corollary 2.43][W-dilation]; [Watrous §2.1.3][W-reductions]; [common projective dilation](../science/spectral_value.md#a-common-projective-dilation); [source replacement](../science/bb84_cloning.md#upper-bound-by-source-replacement); [tutorial: joint systems and timing](tutorial.md#joint-systems-and-timing).

<a id="m06"></a>

### M06. Spectra, operator norms, and Gram matrices

**Phase:** Background/preliminaries.

**Central question:** How can optimizing a quantum success probability become a spectral calculation?

**Understanding target:** Relate the largest eigenvalue of a positive payoff operator to optimization over states. Explain operator norm, singular values, and the shared nonzero spectrum of a weighted vector family's Gram and frame operators.

**Dependencies and story role:** M02–M03. Introduces the mathematical language that turns many possible states into one optimizable quantity.

**Conceptual connection:** Prepares both the scalar-matrix upper bound and the construction of a state attaining it; the Gram/frame identification is supplied explicitly in the project proof.

**Source pointers:** [Watrous §1.1.3, decompositions and norms, including Theorem 1.3][W-operators]; [weighted block-Gram comparison](../science/spectral_value.md#weighted-block-gram-comparison); [frame-operator construction](../science/spectral_value.md#attainment-by-principal-vectors); [tutorial: operators and overlap](tutorial.md#operators-and-overlap).

<a id="m07"></a>

### M07. Guessing probability and ordinary privacy

**Phase:** Background/preliminaries.

**Central question:** How is the best probability of learning a hidden classical label from a quantum system quantified?

**Understanding target:** Describe discrimination of a weighted ensemble, a measurement attaining a lower bound, and a positive-operator dual certificate giving an upper bound. Explain the operational relation between trace distance and equal-prior binary distinguishing.

**Dependencies and story role:** M02 and M06. Adds an information measure with an explicit operational task.

**Conceptual connection:** Provides the foundations for both the quantum-basis counterexample and the exact ordinary-privacy calculation for the one-bit construction.

**Source pointers:** [Watrous §3.1.1 and Theorem 3.4][W-pairs]; [Watrous §3.1.2, ensemble discrimination][W-ensemble]; [Watrous §1.2.3, semidefinite programming][W-sdp]; [full-cube discrimination](../science/quantum_side_information.md#exact-discrimination-on-the-full-cube); [tutorial: guessing and conditioning](tutorial.md#guessing-and-conditioning).

<a id="m08"></a>

### M08. Classical–quantum information and legitimate conditioning

**Phase:** Background/preliminaries.

**Central question:** When does conditioning on information preserve the independent-state model needed by a security argument?

**Understanding target:** Read a classical–quantum state as a family of weighted quantum states. Distinguish a classical posterior, a quantum register correlated with a basis, a discarded register, and an accepted instrument branch. Keep each branch's probability weight when reasoning about unconditional events.

**Dependencies and story role:** M03–M04 and M07. Turns the meaning of side information into an explicit state-level distinction.

**Conceptual connection:** Prepares the different treatment of classical syndrome leakage, quantum basis programs, and loss commitments.

**Source pointers:** [Watrous §2.2.3, classical registers and classical–quantum states][W-cq]; [three experiment models](../science/model.md#what-information-about-the-basis-matters); [loss-branch hypothesis](../science/noise_and_loss.md#loss-commitments-and-subnormalized-branches); [tutorial: guessing and conditioning](tutorial.md#guessing-and-conditioning).

<a id="m09"></a>

### M09. Binary codes as basis sources

**Phase:** Background/preliminaries.

**Central question:** How can a binary linear space describe both compressed basis randomness and disclosed parity information?

**Understanding target:** Explain a generator, a dual code, parity orthogonality, a syndrome, and an affine coset. Distinguish a binary code used to select measurement bases from an error-correcting encoding of a message, and distinguish binary vector spaces from the quantum Hilbert spaces they label.

**Dependencies and story role:** M01 and M08. Introduces the classical geometric structure attached to the basis variable.

**Conceptual connection:** Unifies secret-seed generation and classical leakage as two descriptions of the same residual basis distribution.

**Source pointers:** [codes, seeds, and classical leakage](../science/model.md#codes-seeds-and-classical-leakage); [linear syndrome leakage](../science/codes_and_leakage.md#linear-syndrome-leakage); [tutorial: codes as basis sources](tutorial.md#codes-as-basis-sources). These coding definitions are supplied locally.

<a id="m10"></a>

### M10. Weight profiles, Fourier duality, and public averaging

**Phase:** Background/preliminaries.

**Central question:** What information is retained by a whole code-weight profile that a minimum-distance estimate discards?

**Understanding target:** Interpret a weight enumerator as a sum over every codeword, and understand how binary characters convert a primal sum into a dual sum. Distinguish averaging the basis inside a fixed public code from averaging over the public code itself.

**Dependencies and story role:** M06 and M09. Prepares the algebraic and probabilistic tools for the exact code value and setup analysis.

**Conceptual connection:** Connects symmetry, Fourier orthogonality, and expectation without presuming that minimum distance determines the recovery value.

**Source pointers:** [Fourier derivation](../science/codes_and_leakage.md#fourier-proof-of-the-dual-form); [random-code counting](../science/codes_and_leakage.md#exact-mean-of-a-random-code); [Watrous §1.2.2, probability language][W-probability]; [tutorial: codes as basis sources](tutorial.md#codes-as-basis-sources). The coding transform and subspace count are local derivations.

<a id="m11"></a>

### M11. Positive moments and probability exponents

**Phase:** Background/preliminaries.

**Central question:** How can a bound on a nonnegative moment control a rare event without assuming independent wins?

**Understanding target:** Explain the direction of a moment-to-tail inequality, the role of nonnegative expansion coefficients, and why a Chernoff optimization requires an established moment bound. Distinguish a finite probability inequality from its asymptotic exponent.

**Dependencies and story role:** M01 and M10. Supplies the probability framework needed to convert exact subset information into robustness bounds.

**Conceptual connection:** Separates valid moment reasoning from an unjustified replacement of correlated outcomes by independent Bernoulli variables.

**Source pointers:** [Watrous §1.2.2][W-probability]; [relative-entropy conventions](../science/model.md#conventions-and-charged-resources); [positive-coefficient argument](../science/noise_and_loss.md#proof-by-positive-coefficients); [agreed-error optimization](../science/noise_and_loss.md#agreed-error-acceptance-and-the-sharp-exponent); [tutorial: moments and predicates](tutorial.md#moments-and-security-predicates). The specific concentration calculation is supplied by the project.

<a id="m12"></a>

### M12. Security predicates and charged resources

**Phase:** Background/preliminaries.

**Central question:** Which event and which available information does a stated security probability actually describe?

**Understanding target:** Distinguish ordinary privacy before key revelation, complete recovery of a uniform message after splitting, joint prediction of a challenge bit, and accepted message substitution. Identify secret key bits, public setup, fresh local randomness, transmitted systems, and the time at which each is accessible.

**Dependencies and story role:** M04, M07–M08, and M11. Puts the mathematical quantities into their different cryptographic experiments.

**Conceptual connection:** Explains why a strong result for one recovery predicate does not automatically establish another security definition.

**Source pointers:** [the two encryption guarantees](../science/applications.md#4-the-two-guarantees-at-a-glance); [authentication protocol and hypotheses](../science/key_recycling.md#1-protocol-and-hypotheses); [resources in the applications](../science/interpretation.md#resources-in-the-applications); [Watrous §3.1.1, the binary decision foundation][W-pairs]; [tutorial: moments and predicates](tutorial.md#moments-and-security-predicates).

<a id="m13"></a>

### M13. The complete model distinction

**Phase:** Background/preliminaries.

**Central question:** What must be fixed before a claim about “basis information” has a definite mathematical meaning?

**Understanding target:** Assemble the independent-state monogamy game, honest uniform-string splitting, and quantum-correlated preparation into one comparison. For each, identify who chooses the state, which variables are independent, what the players learn, and what event counts as success.

**Dependencies and story role:** M01–M12. Integrates the background phase into the exact framework needed for the scientific narrative.

**Conceptual connection:** Links operator descriptions, classical coding, timing, and security definitions while preserving the differences between the three experiments.

**Source pointers:** [models](../science/model.md#what-information-about-the-basis-matters); [theorem dependencies](../science/README.md#the-theorem-dependencies); [claims and their limits](../science/README.md#claims-and-their-limits); [tutorial: three experiments](tutorial.md#three-experiments).

<a id="narrative"></a>

## Phase II — Narrative and innovation

<a id="m14"></a>

### M14. From local overlap to winning subspaces

**Phase:** Narrative/innovation.

**Central question:** Why does a difference in referee questions limit the overlap of the corresponding exact-winning subspaces?

**Understanding target:** Explain the enlargement of each winning projector and the block decomposition on the two players' outcome spaces. Identify why tensor-product overlap multiplies across differing coordinates, even for higher-rank referee projections and collective player strategies.

**Dependencies and story role:** M02–M03, M05–M06, and M13. Begins the proof with the local operator mechanism that survives arbitrary attacker dimensions.

**Conceptual connection:** Carries the established projector-overlap method into a form that can be weighted by an arbitrary correlated question distribution.

**Source pointers:** [pairwise winning-subspace overlap](../science/spectral_value.md#pairwise-overlap-of-winning-subspaces); [TFKW attribution](../references/RELATED_WORK.md#tfkw2013); [Watrous §§1.1.2–1.1.3, operator foundations][W1]; [tutorial: exact spectral value](tutorial.md#the-exact-spectral-value).

<a id="m15"></a>

### M15. The weighted Gram upper bound

**Phase:** Narrative/innovation.

**Central question:** How does one scalar matrix control every quantum strategy for a correlated question distribution?

**Understanding target:** Explain the weighted block-row operator, its Gram operator, and the comparison with the scalar matrix whose entries contain square-root question weights and Hamming-distance overlaps. Recognize that the comparison proves an upper bound without independent question coordinates.

**Dependencies and story role:** M06 and M14. Converts the local overlap estimate into the global spectral upper bound.

**Conceptual connection:** Uses finite-dimensional spectral reasoning to eliminate the unbounded choice of finite player memory from the numerical expression for the bound.

**Source pointers:** [weighted block-Gram comparison](../science/spectral_value.md#weighted-block-gram-comparison); [Theorem S](../science/spectral_value.md#theorem-one-scalar-matrix-gives-the-exact-value); [Watrous §1.1.3][W-operators]; [tutorial: exact spectral value](tutorial.md#the-exact-spectral-value).

<a id="m16"></a>

### M16. Attainment and the exact two-PVM theorem

**Phase:** Narrative/innovation.

**Central question:** What makes the spectral bound an exact value rather than only an estimate?

**Understanding target:** Explain how a principal-vector pair realizes all required product overlaps with compatible positive phases. For higher-rank projections, distinguish domination of a rank-one frame from equality of operators. Deduce biased independent-question repetition and identify why the argument is restricted to two PVMs.

**Dependencies and story role:** M02, M06, and M15. Completes the upper/lower-bound pair and integrates the first part of the narrative.

**Conceptual connection:** Connects geometric attainability to an optimal referee state, deterministic player answers, and the tensor-product formula for independent biases.

**Source pointers:** [principal-vector attainment](../science/spectral_value.md#attainment-by-principal-vectors); [independent biased questions](../science/spectral_value.md#independent-biased-questions); [Russo question and scope](../references/RELATED_WORK.md#russo2017); [Watrous §1.1.3][W-operators]; [tutorial: exact spectral value](tutorial.md#the-exact-spectral-value).

<a id="m17"></a>

### M17. An optimal attack on honestly prepared BB84 data

**Phase:** Narrative/innovation.

**Central question:** Can the abstract optimum be attained when the attacker receives an honest unknown uniform string?

**Understanding target:** Explain the Pauli-covariant POVM's normalization, its classical broadcast output, and the basis-dependent decoding rule. Follow the direct success calculation that attains the spectral value despite the honest-source marginal constraint.

**Dependencies and story role:** M05, M13, and M16. Establishes the operational bridge needed before applying the abstract theorem to ciphertexts.

**Conceptual connection:** Shows how symmetry converts an optimal abstract state into a physical measurement. It also distinguishes having no retained quantum memory from having an efficiently implementable or coordinatewise attack.

**Source pointers:** [Pauli-covariant measurement](../science/bb84_cloning.md#pauli-covariant-measurement); [direct success calculation](../science/bb84_cloning.md#direct-success-calculation); [attack resources](../science/bb84_cloning.md#what-the-attack-does-and-costs); [Watrous §§2.3.1–2.3.2][W-measurements]; [tutorial: honest-qubit attack](tutorial.md#an-attack-on-honest-qubits).

<a id="m18"></a>

### M18. The exact code value and leakage geometry

**Phase:** Narrative/innovation.

**Central question:** Why can two equally long classical disclosures have different effects on recovery security?

**Understanding target:** Explain how constant row sums evaluate the spectral matrix for a uniform linear code, and how Fourier duality gives its dual weight profile. Relate affine-coset invariance to syndrome leakage, and compare coordinate disclosure with a long parity.

**Dependencies and story role:** M09–M10 and M16–M17. Turns the exact quantum value into a concrete classical geometric quantity.

**Conceptual connection:** Connects the basis distribution's full geometry to operational leakage cost, while retaining the distinction between worst-rank leakage and suitable dense maps.

**Source pointers:** [exact code formula](../science/codes_and_leakage.md#exact-code-formula); [Fourier dual form](../science/codes_and_leakage.md#fourier-proof-of-the-dual-form); [syndrome leakage](../science/codes_and_leakage.md#linear-syndrome-leakage); [coordinate/parity example](../science/codes_and_leakage.md#a-small-comparison); [tutorial: code formula](tutorial.md#the-code-formula-and-a-worked-example).

<a id="m19"></a>

### M19. Honest public setup and a good-code certificate

**Phase:** Narrative/innovation.

**Central question:** What does a random public code guarantee when the adversary sees it and adapts its attack?

**Understanding target:** Derive the exact mean by counting nonzero dual-word inclusion. Explain why the optimized value is averaged after the code is revealed, and why Markov's inequality applies to the nonnegative excess. Separate ensemble security, a high-probability certificate, and a guarantee for every fixed code.

**Dependencies and story role:** M10–M11 and M18. Converts the code formula into quantitative setup guarantees.

**Conceptual connection:** Treats public randomness as part of the security experiment, without making it secret or silently discarding exceptional codes.

**Source pointers:** [exact random-code mean](../science/codes_and_leakage.md#exact-mean-of-a-random-code); [high-probability certificate](../science/codes_and_leakage.md#a-high-probability-certificate); [setup and efficiency](../science/codes_and_leakage.md#setup-and-efficiency); [Watrous §1.2.2][W-probability]; [tutorial: random codes and rate](tutorial.md#random-codes-and-the-optimal-seed-rate).

<a id="m20"></a>

### M20. The matching basis-seed converse

**Phase:** Narrative/innovation.

**Central question:** In what precise sense is the secret basis rate optimal?

**Understanding target:** Combine the most-likely-basis attack with the basis-independent Breidbart attack. Explain how the random-code mean matches the resulting exponent within a constant factor, and how additional seed slack gives a near-unit multiplicative penalty with high probability.

**Dependencies and story role:** M12, M17, and M19. Completes the randomness tradeoff with both an achievable bound and unavoidable attacks.

**Conceptual connection:** Identifies the approximately 0.228447 secret basis bits per qubit threshold while keeping total encryption key length, public generator cost, and other security predicates outside that converse.

**Source pointers:** [optimal secret basis rate](../science/codes_and_leakage.md#optimal-secret-basis-rate); [what is optimal](../science/interpretation.md#what-is-optimal); [charged setup resources](../science/codes_and_leakage.md#setup-and-efficiency); [tutorial: random codes and rate](tutorial.md#random-codes-and-the-optimal-seed-rate).

<a id="m21"></a>

### M21. Scoring a subset while disclosing the full basis

**Phase:** Narrative/innovation.

**Central question:** Why do unused basis coordinates not invalidate the bound for a fixed retained subset?

**Understanding target:** Explain the fixed reduced-state argument and the maximization over local measurement pairs for each used basis. Identify the projected primal code and shortened dual code, and distinguish this reduction from conditioning the state or choosing the subset after seeing the basis.

**Dependencies and story role:** M03, M08, and M18. Establishes the load-bearing bridge from exact full-string recovery to subset moments.

**Conceptual connection:** Joins an operational information argument to the coding identity that projection of the primal corresponds to shortening of the dual.

**Source pointers:** [projection and shortening](../science/noise_and_loss.md#projection-and-shortening); [unused-basis argument](../science/noise_and_loss.md#why-knowledge-of-unused-basis-bits-does-not-break-this-bound); [Watrous §2.1.3][W-reductions]; [tutorial: subsets and noise](tutorial.md#one-certificate-for-subsets-and-noise).

<a id="m22"></a>

### M22. One weight-profile certificate for all moments

**Phase:** Narrative/innovation.

**Central question:** How can one code property control every retained subset and every relevant noise parameter?

**Understanding target:** Follow the positive subset expansion and the interchange of subset and dual-word sums. Explain why shortening only removes nonnegative terms and why the noise argument of the weight enumerator does not exceed the certificate's argument. Retain the status of the result as a moment upper bound.

**Dependencies and story role:** M11 and M21. Builds the uniform robustness certificate from the projected exact values.

**Conceptual connection:** Makes the absence of an exponential subset-count penalty a consequence of monotonicity, rather than an independence assumption or a claim of simultaneous saturation.

**Source pointers:** [moment upper bound](../science/noise_and_loss.md#exact-form-of-a-moment-upper-bound); [positive-coefficient proof](../science/noise_and_loss.md#proof-by-positive-coefficients); [uniform certificate](../science/noise_and_loss.md#uniform-certificate); [tutorial: subsets and noise](tutorial.md#one-certificate-for-subsets-and-noise).

<a id="m23"></a>

### M23. Agreed errors and the sharp asymptotic threshold

**Phase:** Narrative/innovation.

**Central question:** Which noisy acceptance rule has the relative-entropy exponent, and why is its threshold sharp?

**Understanding target:** Relate agreement plus a common error radius to the count of coordinates where at least one player is wrong. Explain the Chernoff optimizer, integer-radius convention, and matching Breidbart exponent. Distinguish asymptotic sharpness from an exact finite-block optimum and from separate error tolerances.

**Dependencies and story role:** M11–M12, M17, and M22. Gives the certificate its operational noisy-recovery meaning.

**Conceptual connection:** Connects the relative-entropy tail calculation to a physical attack whose error law is independent of the full basis string, even when the bases are correlated.

**Source pointers:** [agreed-error acceptance and exponent](../science/noise_and_loss.md#agreed-error-acceptance-and-the-sharp-exponent); [error predicates](../science/model.md#errors-and-retained-coordinates); [Watrous §1.2.2, probability foundation][W-probability]; [tutorial: subsets and noise](tutorial.md#one-certificate-for-subsets-and-noise).

<a id="m24"></a>

### M24. Loss commitments and branchwise independence

**Phase:** Narrative/innovation.

**Central question:** Under what state-level condition can adversarially selected retained sets be combined into an unconditional soundness bound?

**Understanding target:** Read the factorization into a basis distribution and subnormalized branch states. Explain why branch traces are multiplied and summed, why rare branches are not renormalized away, and when source replacement supplies the required independence. Recognize that pre-disclosure timing alone is insufficient.

**Dependencies and story role:** M04–M05, M08, and M22–M23. Integrates fixed-subset robustness with a legitimate instrument model.

**Conceptual connection:** Links physical timing to an explicit independence premise, preserving the distinction between this branch theorem and a complete position-verification reduction.

**Source pointers:** [loss commitments and branches](../science/noise_and_loss.md#loss-commitments-and-subnormalized-branches); [when the condition is satisfied](../science/noise_and_loss.md#when-the-branch-condition-is-satisfied); [Watrous §2.3.2, measurement and residual-state descriptions][W-measurement-notions]; [tutorial: loss independence](tutorial.md#loss-and-branch-independence).

<a id="m25"></a>

### M25. Using a quantum basis program without identifying it

**Phase:** Narrative/innovation.

**Central question:** Can quantum side information enable perfect winning while leaving the classical basis difficult to guess?

**Understanding target:** Explain the forwarding construction, the product discrimination certificate, the finite eight-qubit violation, and the positive-distance family. Identify exactly which independence premise changes and which proposed additive bound fails.

**Dependencies and story role:** M07–M08, M13, and M16. Tests the boundary of the independent-state theorem with an explicit operational separation.

**Conceptual connection:** Distinguishes identifying a classical basis label from using an aligned quantum state, without claiming a break of honest-input recovery or the proved authentication protocol.

**Source pointers:** [perfect winning strategy](../science/quantum_side_information.md#a-perfect-winning-strategy); [full-cube discrimination](../science/quantum_side_information.md#exact-discrimination-on-the-full-cube); [positive rate and distance](../science/quantum_side_information.md#positive-rate-and-linear-distance); [scope](../science/quantum_side_information.md#interpretation-and-scope); [Watrous §3.1.2][W-ensemble]; [tutorial: quantum basis information](tutorial.md#quantum-basis-information).

<a id="m26"></a>

### M26. Full-message encryption and the limit of search security

**Phase:** Narrative/innovation.

**Central question:** How can perfect ordinary privacy and an exact random-message recovery bound coexist with failure of unclonable indistinguishability?

**Understanding target:** Explain the conjugate-pad algorithms, the uniform-message change of variables, and the matching recovery attack, including pad-dependent final measurements. Follow the two-coordinate chosen-message counterattack and identify why it does not contradict complete random-message recovery security.

**Dependencies and story role:** M12, M17–M18, and M20. Applies the physical theorem while exposing the importance of the winning predicate.

**Conceptual connection:** Connects a mathematically exact search value to a concrete encryption construction without promoting it to a stronger decision guarantee.

**Source pointers:** [ordinary privacy](../science/applications.md#algorithms-and-ordinary-privacy); [exact random-message recovery](../science/applications.md#exact-random-message-recovery-probability); [indistinguishability counterattack](../science/applications.md#why-this-construction-fails-unclonable-indistinguishability); [tutorial: encryption applications](tutorial.md#two-encryption-applications).

<a id="m27"></a>

### M27. A separate one-bit application through the CLX compiler

**Phase:** Narrative/innovation.

**Central question:** What additional theorem and timing condition turn a search bound into a one-bit joint-decision guarantee?

**Understanding target:** Explain the inherited common-mask reduction, its quartic loss, and the requirement that the shared random mask remain secret until after splitting. Follow the simulation of a ciphertext-dependent splitter, distinguish statistical ordinary privacy from perfect privacy, and account separately for shared key and local encryption coins.

**Dependencies and story role:** M07, M12, M19, and M26. Adds the valid decision application through an explicitly separate reduction.

**Conceptual connection:** Shows how the exact code value enters an inherited compiler while leaving its exponent loss, one-time scope, and noise-transfer limitations intact.

**Source pointers:** [imported search-to-prediction theorem](../science/applications.md#the-inherited-search-to-prediction-theorem); [ciphertext-dependent reduction](../science/applications.md#reduction-for-a-ciphertext-dependent-splitting-attack); [exact ordinary-privacy error](../science/applications.md#ordinary-privacy-is-statistical-with-an-exact-error); [CLX source](../references/RELATED_WORK.md#clx2026); [Watrous §3.1.1][W-pairs]; [tutorial: encryption applications](tutorial.md#two-encryption-applications).

<a id="m28"></a>

### M28. The exact value inside noiseless authentication

**Phase:** Narrative/innovation.

**Central question:** How can the independent-state value remain useful when a recycling adversary holds quantum information about the basis?

**Understanding target:** Explain the discrimination-dual domination bound and its valid multiplicative side-information factor. Identify the Fehr–Salvail MAC, message-independence, key-privacy, and refresh hypotheses. Follow the basis-key and MAC-key one-execution estimates without dropping tag-dependent information or conditioning away branch weights.

**Dependencies and story role:** M07–M08, M18, and M25. Uses the quantum-side-information distinction constructively within an existing protocol.

**Conceptual connection:** Replaces a minimum-distance relaxation at the points where the protocol needs a guessing bound, while preserving the protocol and its additional cryptographic premises.

**Source pointers:** [protocol and hypotheses](../science/key_recycling.md#1-protocol-and-hypotheses); [multiplicative domination](../science/key_recycling.md#2-importing-the-exact-value-in-the-presence-of-quantum-side-information); [one-execution basis estimate](../science/key_recycling.md#3-one-execution-the-basis-key-estimate); [MAC-key privacy](../science/key_recycling.md#4-one-execution-mac-key-privacy-and-its-constants); [Watrous §3.1.2, discrimination dual][W-ensemble]; [tutorial: noiseless recycling](tutorial.md#noiseless-key-recycling).

<a id="m29"></a>

### M29. Sequential reuse and the meaning of the parameter gain

**Phase:** Narrative/innovation.

**Central question:** How does a one-execution improvement propagate through repeated authentication without changing the claimed security model?

**Understanding target:** Explain the comparison sequence with hypothetically refreshed MAC keys, trace-distance accumulation, and the bound for an accepted substitution in a specified execution. Distinguish that event from any failure across the sequence. Relate random-code averaging to the stated qubit coefficients and the restricted GV comparison.

**Dependencies and story role:** M11, M19–M20, and M28. Connects the local substitution to a quantified protocol-level consequence.

**Conceptual connection:** Joins composition, public setup, and resource accounting while retaining synchronized noiseless executions, private refresh resources, and the separate status of noisy or encryption-with-recycling variants.

**Source pointers:** [sequential reuse](../science/key_recycling.md#5-sequential-reuse); [parameter refinement](../science/key_recycling.md#6-concrete-parameter-refinement); [comparison meaning](../science/key_recycling.md#what-the-numerical-comparison-means); [scope](../science/key_recycling.md#7-scope-of-the-substitution); [Watrous §3.1.1, operational distance foundation][W-pairs]; [tutorial: noiseless recycling](tutorial.md#noiseless-key-recycling).

<a id="m30"></a>

### M30. The complete scientific picture

**Phase:** Narrative/innovation.

**Central question:** What is the complete chain from basis geometry to cryptographic consequences, and where does each implication stop?

**Understanding target:** Assemble the exact spectral theorem, physical attack, code profile, optimal seed exponent, uniform robustness certificate, quantum-side-information separation, and two application routes into one dependency account. Distinguish exact values, moment upper bounds, asymptotic exponents, imported reductions, and finite verification. Account for secret, public, local-randomness, communication, and refresh resources.

**Dependencies and story role:** M13–M29. Integrates the narrative phase into a single bounded scientific explanation.

**Conceptual connection:** Explains how one exact independent-state quantity supports several consequences without identifying their security predicates or extending them beyond their assumptions.

**Source pointers:** [theorem dependencies](../science/README.md#the-theorem-dependencies); [claims and limits](../science/README.md#claims-and-their-limits); [resource interpretation](../science/interpretation.md#resources-in-the-applications); [bounded conclusions](../science/interpretation.md#bounded-conclusions); [verification limits](../verification/README.md#tolerances-and-interpretation); [tutorial: complete picture](tutorial.md#the-complete-scientific-picture).

[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W-operators]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=24
[W-probability]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47
[W-sdp]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=53
[W-states]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4
[W-reductions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10
[W-channels]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15
[W-cq]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=38
[W-measurements]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=43
[W-measurement-notions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=48
[W-dilation]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=52
[W-pairs]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=2
[W-ensemble]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=9
