# Claim and review governance

This repository distinguishes the truth of a bounded mathematical statement from the status of the full Millennium problem. A proved auxiliary lemma never promotes the project automatically.

## Two labels per item

Each registry item has a semantic kind—such as `Definition`, `Known Theorem`, `Lemma`, `Conditional Theorem`, `Conjecture`, `Heuristic`, or `Numerical Observation`—and an evidence level.

| Level | Minimum meaning | Permitted wording |
|---|---|---|
| E0 | Idea, target, open question, or informal argument | Exploratory |
| E1 | Heuristic, perturbative, symbolic, or numerical evidence | Evidence; not proof |
| E2 | Complete repo proof of a bounded subcase or auxiliary lemma | Partial result with exact scope |
| E3 | Self-contained manuscript purporting to prove the official statement | Unverified candidate proof |
| E4 | Clean internal adversarial audit and clean reproduction | Internally audited candidate |
| E5 | Three independent reports, two by relevant experts, with no major objection open | Proposed complete proof / candidate solution |
| E6 | Refereed publication in an apparently qualifying outlet | Published proposed solution |
| E7 | At least two years of rigorous scrutiny and strong evidence of broad acceptance | Community-supported proposal; Clay pending |
| E8 | Public Clay determination | CMI-recognized solution |

The project cannot self-promote beyond E4. Repository stars, press, citations, AI review, and author-selected testimonials are not independent mathematical validation.

## Promotion gates

E3 requires a self-contained manuscript passing every mathematical gate in [STATUS.json](STATUS.json): all groups, continuum and infinite-volume construction, nontriviality, local/UV structure, axioms, and a finite positive spectral gap. E5 additionally requires conflict-free independent review. E6–E8 require the external publication, time, acceptance, and Clay gates in sequence.

No single numerical experiment, formal manipulation, or computer check can promote the full problem. A proof assistant may verify encoded mathematics but its model-to-problem correspondence and axioms remain audit obligations.

## Proof-audit rules

Every repo-originated theorem must state:

1. quantifiers and scope;
2. all external hypotheses;
3. a stable proof anchor;
4. dependencies by claim ID;
5. known limitations and falsification tests;
6. provenance and any computational trust boundary;
7. review state and open objections.

All cited results must be version-pinned and their hypotheses mapped. Limit exchanges, constant dependence, regulator uniformity, operator domains, and exceptional sets must be explicit. “Standard” is never enough for a central bridge.

## Independent review

Promotion to E5 requires at least three conflict-free reports tied to an immutable manuscript hash. At least two reviewers must have relevant expertise in constructive or axiomatic QFT, gauge theory, renormalization, or spectral analysis. One report audits official-statement coverage, one audits the analysis line by line, and one actively searches for counterexamples, hidden regulator dependence, and circularity. Every fatal or major objection must be resolved and re-reviewed.

AI systems, including those used to develop this repository, never count as independent reviewers.

## Corrections and retractions

- **S0 editorial:** ordinary correction.
- **S1 local:** patch, document the dependency impact, and recheck downstream claims.
- **S2 major gap:** immediately downgrade affected claims and withdraw candidate-solution wording.
- **S3 fatal:** mark the affected release retracted, preserve it, publish a linked explanation, and notify known reviewers/publication venues.

Released tags and criticism are never silently deleted. A repaired proof receives a new immutable release and repeats the applicable gates.

## Announcement language

Before E5, the repository may describe only scoped partial results. At E5 the strongest allowed wording is: “We are releasing a proposed complete proof for independent scrutiny; it has not been validated by Clay.” Definitive “problem solved” language is reserved for E8.
