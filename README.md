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

## Papers

The long version is split into three self-contained papers for submission. Each derives its content from the long version, keeps its identifiers and evidence status, and comes with a related-work document that compares it with prior work and names the main overlap risks.

| Paper | Contribution | Related work |
| --- | --- | --- |
| [Paper 1: An Evidence Model of Trust, Distrust and the Calibration Gap](papers/01-evidence-model/paper.md) | evidence model with trust, distrust and uncertainty, temporal decay, source dependence, normative vs. descriptive account | [related-work.md](papers/01-evidence-model/related-work.md) |
| [Paper 2: Verification as a Public Good](papers/02-verification-in-organizations/paper.md) | groups act on verification; protection delegation; action-bound rules; trust dimensions × security objectives | [related-work.md](papers/02-verification-in-organizations/related-work.md) |
| [Paper 3: Engineering Calibrated Trust between Humans, Agents and Machines](papers/03-human-agent-trust/paper.md) | evidence accounts, decay and re-verification for agents and machines; utility as a risk dimension | [related-work.md](papers/03-human-agent-trust/related-work.md) |

All references are in [`bib/references.bib`](bib/references.bib) with their verification status; see [`bib/README.md`](bib/README.md) and the open points in [`bib/check-report.md`](bib/check-report.md).

## Building the PDFs

A GitHub Actions workflow ([`.github/workflows/latex.yml`](.github/workflows/latex.yml)) runs on every push and pull request:

1. `python3 tools/build_papers.py check` matches every author–year citation and every reference-list entry against [`bib/references.bib`](bib/references.bib) and fails on references that are missing or ambiguous.
2. `python3 tools/build_papers.py build --pdf` converts the papers, the long version and Case Study 1 with pandoc to LaTeX and builds PDFs with LuaLaTeX and biber. The reference lists are generated from the bibliography, and the verification status of each entry (e.g. "to be checked") is printed after it.

The PDFs and, per document, a self-contained LaTeX folder (`.tex`, the document's own `.bib`, preamble and figures) are available as a workflow artifact; for version tags (`v*`) the PDFs are attached to the release. Locally the same commands work with pandoc, LuaLaTeX, latexmk and biber installed; output goes to `build/`.

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
papers/0N-*/paper.md                           Papers 1-3 derived from the long version
papers/0N-*/related-work.md                    related-work document per paper
bib/references.bib                             bibliography with verification status
tools/build_papers.py                          citation check and LaTeX/PDF build
LICENSE                                        license text CC BY 4.0
CITATION.cff                                   citation metadata (machine-readable)
```

## License and citation

Text and figures are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may use, share, translate and adapt the material, including commercially, provided you give credit to the author, link to the license and indicate whether changes were made.

Quotations from and content of the cited literature are not covered by this license; the rights of their respective authors apply.

**Suggested citation:**

> Rumpf, J. (2026). *Trust is Engineered* (Working paper, version 0.6, draft). https://github.com/JoeRu/trust-is-engineered

The metadata are available in machine-readable form in [`CITATION.cff`](CITATION.cff); GitHub shows them under "Cite this repository".
