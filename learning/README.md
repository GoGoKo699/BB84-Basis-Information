# Learning guide

[Repository overview](../README.md) · [Scientific map](../science/README.md) · [Milestones](milestones.md) · [Watrous bridge](watrous_bridge.md) · [Tutorial](tutorial.md)

The question is concrete: an adversary receives a BB84-encoded string and must divide it between two recipients before learning the bases. How much hidden basis randomness is needed to keep both recipients from recovering the entire string?

The answer connects three ideas. Quantum measurement geometry determines an exact matrix of overlaps. Linear codes turn its largest eigenvalue into a weight enumerator. A dual-code identity then exposes the cost of basis correlations and controls every retained subset with the same certificate.

## One anchor and the local bridge

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the prepublication manuscript and chapter PDFs.

Use the [source bridge](watrous_bridge.md) to select the operator, state, measurement and discrimination material relevant to the current question. It maps the textbook's notation to the repository and identifies where the monogamy proof, binary-code calculation and cryptographic reductions enter. The project does not require reading the whole book first.

## Choose a reading route

| Aim | Route |
|---|---|
| Understand the whole argument | Read the [worked tutorial](tutorial.md), using the [milestone map](milestones.md) to keep track of conceptual dependencies. |
| Build the quantum foundations | Follow the relevant sections in the [Watrous bridge](watrous_bridge.md), then the background phase of the [map](milestones.md). |
| Inspect an exact theorem or its assumptions | Start at the [scientific map](../science/README.md) and follow the authoritative topic page. |
| Compare cryptographic security claims | Read the [models](../science/model.md), then [encryption](../science/applications.md), [key recycling](../science/key_recycling.md) and [resource interpretation](../science/interpretation.md). |
| Reproduce a finite example | Use the [verification account](../verification/README.md); its checks complement the written proofs. |

## The 30-milestone structure

The [shared map](milestones.md) contains exactly **30 milestones**. The first **13** build from local quantum objects and binary linear relations to a complete understanding of the recovery experiment. The remaining **17** build the proof mechanism, its resource consequences, the changes of model and the final cryptographic synthesis.

Each milestone states a central question, an understanding target, earlier dependencies, its role in the argument and precise source pointers. The allocation reflects the project's connection between operator theory, coding and security definitions. It is an understanding map for the project, independent of any reader's pace or prior preparation.

## Keep the models in view

The spectral theorem starts with a state independent of the chosen bases. Honest BB84 attainment additionally uses a uniform encoded string. A public random basis code is available to the attacker, while its secret seed is disclosed only after splitting. The rate counts that seed; encryption has additional key resources.

Agreement is part of the sharp noisy acceptance rule. Loss branches need independence from the unexposed basis. Quantum-correlated referee preparation changes that premise. The encryption and key-recycling pages state the additional assumptions of their respective reductions.

The [related-work account](../references/RELATED_WORK.md) separates textbook foundations, inherited research ingredients and the conclusions developed here. The complete scientific proofs have one authoritative home under [science/](../science/README.md).
