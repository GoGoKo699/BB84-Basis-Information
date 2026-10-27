# Scientific map

[Repository overview](../README.md) · [Models](model.md) · [References](../references/RELATED_WORK.md) · [Verification](../verification/README.md)

## The central distinction

Basis information has a geometry, not just a bit count. Revealing one coordinate of a BB84 basis and revealing one parity can have different effects on two-recipient recovery. The first task is therefore to determine the security value from the full distribution. Only then can one optimize the amount of secret randomness or interpret leakage.

The account starts with an exact spectral characterization. For linear bases, symmetry turns the spectrum into a weight enumerator. A Fourier transform moves the same quantity to the dual code, where random setup and every retained coordinate set can be analyzed with one nonnegative certificate.

## Main proof route

| Step | Statement and role | File |
|---|---|---|
| 1 | Specify the independent-state monogamy game, honest BB84 splitting, and quantum-correlated preparation separately | [Models](model.md) |
| 2 | Prove the exact spectral value for arbitrary correlations between choices of two PVMs | [Spectral value](spectral_value.md) |
| 3 | Attain the BB84 optimum on an honest uniform input by a normalized physical measurement | [BB84 cloning](bb84_cloning.md) |
| 4 | Evaluate linear and affine basis sets; derive the exact random-code mean and optimal secret seed rate | [Codes and leakage](codes_and_leakage.md) |
| 5 | Convert the dual-code certificate into uniform subset moments and sharp agreed-error exponents | [Noise and loss](noise_and_loss.md) |
| 6 | Identify what changes when the basis is encoded in quantum side information | [Quantum side information](quantum_side_information.md) |
| 7 | Apply the exact value to precisely defined encryption and authentication tasks | [Encryption](applications.md) and [key recycling](key_recycling.md) |
| 8 | Compare secret randomness, quantum transmission, public setup and security definitions | [Interpretation](interpretation.md) |

## The theorem dependencies

**Theorem S** is the general two-PVM statement. Its upper bound uses projective dilation, the TFKW projector-overlap argument and a scalar block-Gram comparison. Its lower bound uses a pair of principal vectors attaining the maximal projector overlap.

**Theorem B** applies Theorem S to honest uniform-message BB84 preparation. Source replacement supplies the upper bound; a Pauli-covariant POVM supplies physical attainment. This second step is specific to BB84.

**Theorem C** evaluates Theorem S for a uniform linear or affine basis set. Constant row sums give the primal weight enumerator; a standard Fourier identity gives the dual form. **Theorem R** takes its exact mean under random public setup and combines it with two universal attacks to establish the optimal basis rate.

**Theorem N** applies Theorem C to every projected code, then expands the noise moment with nonnegative coefficients. A bound on the original dual enumerator controls all shortened duals. Classical Chernoff optimization gives the exponent; a product Breidbart attack shows asymptotic sharpness.

The quantum-side-information separation changes a load-bearing premise of Theorem S. It uses a direct forwarding strategy and a state-discrimination dual certificate. It is not a limiting case of the independent-state theorem.

The encryption results inherit their primitives and, for one-bit prediction, a separate existing compiler. The key-recycling calculation inherits the Fehr–Salvail protocol, MAC assumptions, domination inequality and sequential comparison argument. It replaces their minimum-distance relaxation with the exact independent-code value.

## Claims and their limits

| Established conclusion | Boundary needed to read it correctly |
|---|---|
| Arbitrary distribution over product choices of two projective measurements | Two fixed PVMs; finite referee dimension; initial state independent of the question |
| Exact physical BB84 recovery | Uniform encoded full string; basis disclosed after splitting; recipients cannot communicate |
| Optimal basis seed rate | This architecture and complete-string recovery exponent; public setup randomness is separate |
| Uniform loss and noise certificate | Agreement on accepted answers and independent branch states; a moment bound, not an exact finite-block noisy optimum |
| Additive quantum-leakage counterexample | Adversarial preparation with an $`n`$-qubit basis-correlated register |
| Full-message conjugate encryption | Perfect ordinary one-time privacy and exact random-message recovery; chosen-message unclonability fails |
| Compiled one-bit encryption | Secret common mask revealed after splitting; inherited quartic loss; one-time security |
| Improved key-recycling bound | Original noiseless sequential substitution model and refresh resources; not a global QKR optimality claim |

The [verification suite](../verification/README.md) checks finite implementations independently where possible. It does not certify novelty or replace the analytic arguments.
