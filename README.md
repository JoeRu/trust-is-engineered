# Trust is Engineered

> **DRAFT.** Work in progress, not peer reviewed and not empirically validated. Content, chapter numbers and references may change; some references have not yet been checked against the original (status notes in Chapter 16).

A dynamic, context-sensitive model of trust, distrust and decisions under uncertainty.

**Status:** research concept and mathematical model hypothesis, version 0.6 (12 October 2026). The model has not been empirically validated. From version 0.6 onward the English text is authoritative; the German original is kept unchanged in [`docs/de/`](docs/de/).

➡️ **[Read the paper: docs/trust-is-engineered.md](docs/trust-is-engineered.md)**

## What it is about

The model is a theoretical framework for two practical problems:

1. **Training people.** How do people learn to recognize abuse of trust, such as phishing and social engineering, with little effort and without rejecting legitimate requests across the board?
2. **Integrating machines.** How can trust between humans and agents, and between machines, be established and verified repeatedly?

Both problems share one structure: an entity has to decide which action it allows another entity to take on incomplete evidence.

![The gap between felt and justified trust is the attack surface](docs/figures/fig-06-architecture.png)

## Core ideas

- Trust is represented as a directed, context-dependent graph. Each edge carries trust, distrust and uncertainty separately.
- Evidence ages. Without new evidence, trust returns to the base rate and uncertainty grows.
- Groups act less on evaluation than on verification: whoever believes that others or IT are checking does not check. Verification needs a named role and a visible norm.
- Two accounts run in parallel: a normative one (as the evidence warrants) and a descriptive one (how people actually judge). Their difference is the calibration gap and thus the attack surface for social engineering.
- Permissions depend on the action and the size of its potential loss, not on trust in the person.

## Contents of the paper

| Chapter | Topic |
| --- | --- |
| 0 | Changes from the previous version |
| 1–3 | Objectives, concepts, graph model |
| 4–6 | Evidence model, psychological factors, decision layer |
| 7 | Groups and organizations: diffusion of responsibility, protection delegation, norms |
| 8 | Attacks as operations on model quantities |
| 9 | Application A: recognizing abuse of trust with little effort |
| 10 | Application B: human–agent and machine–machine trust |
| 11 | Core assumptions and hypotheses with evidence status |
| 12 | Derivable predictions |
| 13 | Trust dimensions and security objectives of information security |
| 14 | Practical implications for information security |
| 15–16 | Research plan, limitations, ethics and law, references |

## Companion papers

| Paper | Topic |
| --- | --- |
| [Case Study 1](docs/case-study-01-populist-techniques.md) | Populist argumentation techniques as calibration attacks on the macro level |

## How to read it

- The predictions (Chapter 12), the security rules (Chapter 14) and the worked examples are derived from the model and have not been tested empirically. Numbers in the figures are illustrative.
- Most references have not been verified against the full text. Entries marked "to be checked" must be checked against the original before publication.
- Identifiers are kept from the German original for stability: G = core assumption (*Grundannahme*), H = hypothesis, V = prediction (*Vorhersage*), S = security rule (*Sicherheitsregel*).
- The model is meant for self-reflection, training, simulation and the assessment of technical systems. It is not meant for rating people for decisions made by third parties.

## Repository layout

```
docs/trust-is-engineered.md                    the working paper (v0.6, English)
docs/case-study-01-populist-techniques.md      companion paper: Case Study 1
docs/figures/                                  Figures 1 to 10 (English)
docs/figures/src/make_figures.py               script that generates the figures
docs/de/                                       German original v0.6 (archived, not maintained)
LICENSE                                        license text CC BY 4.0
CITATION.cff                                   citation metadata (machine-readable)
```

## License and citation

Text and figures are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may use, share, translate and adapt the material, including commercially, provided you give credit to the author, link to the license and indicate whether changes were made.

Quotations from and content of the cited literature are not covered by this license; the rights of their respective authors apply.

**Suggested citation:**

> Rumpf, J. (2026). *Trust is Engineered* (Working paper, version 0.6, draft). https://github.com/JoeRu/trust-is-engineered

The metadata are available in machine-readable form in [`CITATION.cff`](CITATION.cff); GitHub shows them under "Cite this repository".
