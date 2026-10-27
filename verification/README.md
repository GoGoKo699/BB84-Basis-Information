# Reproducible finite checks

[Scientific map](../science/README.md) · [Recorded output](expected_results.json) · [Verification program](run_all.py)

The mathematical claims are proved in the topic pages under `science/`. This suite checks independent finite constructions, enumerations, operator identities and numerical constants. It uses no network, optimization solver or external data.

## Run

Use Python 3.11 or newer with the pinned NumPy dependency. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The program prints a JSON report and exits with status zero only if every check passes. A failed check raises an assertion naming its section. To retain a fresh report separately from the committed reference output:

```bash
python3 verification/run_all.py --json /tmp/bb84-basis-results.json
```

The committed [expected output](expected_results.json) was produced with Python **3.12.14** and NumPy **2.3.5**. The default run uses fixed seed `20261027`, enumerates all binary linear subspaces of lengths one through four, and reports **36,017 checks** with status `PASS`.

## What is checked

| Check family | Independent constructions or comparisons | Scientific reference |
|---|---|---|
| Nonuniform BB84 | Gram and frame spectra, normalized Pauli effects, direct honest-input outcome probabilities | [Spectral value](../science/spectral_value.md), [physical attack](../science/bb84_cloning.md) |
| General PVMs | Higher-rank projectors, unequal outcome alphabets, principal vectors and direct player-measurement payoff operators | [Two-PVM theorem](../science/spectral_value.md) |
| All small codes | 90 linear codes, 372 affine cosets and 5,370 affine projections; primal/dual enumerators, shortening and exact random-code means | [Codes](../science/codes_and_leakage.md) |
| Noise and unused questions | Direct operator payoffs with full-question-dependent player measurements; positive subset expansion and shortened-dual moment formula | [Noise and loss](../science/noise_and_loss.md) |
| Quantum side information | One-qubit and tensor discrimination duals, physical forwarding, the eight-qubit counterexample and a finite positive-distance existence bound | [Separation](../science/quantum_side_information.md) |
| Application identities | Direct averaging of the one-bit ciphertext for all two-coordinate linear codes; its exact ordinary privacy distance; the GV equation and QKR comparison constants | [Encryption](../science/applications.md), [key recycling](../science/key_recycling.md) |

The code also checks the Chernoff optimization, basis-rate constants and a finite high-probability parameter choice. These are computational checks of the formulas, not numerical security proofs for the imported cryptographic reductions.

## Tolerances and interpretation

The equality test uses absolute error at most `2e-10 * (1 + max(abs(expected)))`. Positive-semidefinite and upper-bound tests allow the corresponding floating-point tolerance. The recorded maximum equality residual is approximately **2.53e-11**, including comparisons to rounded printed constants; the largest positive inequality residual is approximately **1.34e-15**. Small last-digit differences across supported numerical libraries are expected.

Some quantum payoff examples use fixed-seed random matrices. They test the implementation against nontrivial collective and full-question-dependent measurements. Sampling such measurements cannot upper-bound every quantum strategy. The projector/Gram proof supplies that upper bound analytically.

The enumeration through length four exhausts those small linear codes, not all block lengths or basis distributions. The direct moment bound need not be tight at finite block length; the output includes an example exhibiting this distinction.

The suite does not prove literature priority, an efficient construction of large certified codes, an efficient optimal adversarial circuit, the general common-mask compiler, or universal composability of a recycling protocol. The latter applications use the explicitly cited source theorems and the written reductions.

## Reproduction map

`run_all.py` contains its own small binary-code enumeration, projection, duality and BB84 matrix routines. `requirements.txt` pins the only third-party dependency. `expected_results.json` records the complete default result, including the examples, constants, counts and environment versions. No generated cache, local environment or private research record is required.
