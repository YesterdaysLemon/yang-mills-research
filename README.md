# Yang–Mills existence and mass gap: an open research ledger

> **Official problem status: UNSOLVED** (checked 2026-07-22)
>
> **Repository status: EXPLORATORY — NOT A SOLUTION**
>
> Full-problem evidence level: **E0**. The highest individual item is an **E2 auxiliary lemma**, not progress through the central construction.

This is a public, versioned attempt to reason carefully about the four-dimensional Yang–Mills existence and mass-gap problem. Its purpose is to make every claim, dependency, failed route, and correction inspectable. Git history records work; it does not certify mathematics.

## The target

For every compact simple gauge group \(G\), construct a nontrivial quantum Yang–Mills theory on \(\mathbb R^4\) with axiomatic strength at least matching the frameworks cited by Jaffe and Witten, and prove that its Hamiltonian has a finite positive spectral gap.

The exact scope and the ways an apparent result can miss it are frozen in [PROBLEM.md](PROBLEM.md). The canonical source is the [Clay Mathematics Institute problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).

## Current work

The main route is a Wilson lattice regulator followed by gauge-covariant renormalization, construction of local gauge-invariant observables, Osterwalder–Schrader reconstruction, and a still-missing nonperturbative infrared bridge. The first bounded target is one source-inserted RG step; supporting notes isolate both its elementary raw source identities and the final gap certificate:

- [Chosen route and dependency map](ROADMAP.md)
- [Program 002: one-block observable RG theorem](research/programs/002-one-block-observable-rg.md)
- [Program 003: first source-jet remainder](research/programs/003-first-source-jet-remainder.md)
- [Program 001: continuum gap transfer](research/programs/001-continuum-gap-transfer.md)
- [Note 0001: dense-state semigroup criterion](research/notes/0001-dense-state-gap-criterion.md)
- [Note 0002: OS gap-transfer criterion](research/notes/0002-os-gap-transfer.md)
- [Note 0003: raw-block source jets](research/notes/0003-raw-block-source-jets.md)
- [Note 0004: fixed-background source jet](research/notes/0004-fixed-background-source-jet.md)
- [Note 0005: pointwise coarea kernels](research/notes/0005-pointwise-coarea-kernels.md)
- [Note 0006: local Bałaban fiber chart](research/notes/0006-local-balaban-fiber-chart.md)
- [Bałaban theorem-level source map](literature/audits/2026-07-22-balaban-source-map.md)
- [Bałaban imported-map audit](literature/audits/2026-07-22-balaban-imported-map.md)

Programs 002 and 003 are open theorem specifications, not results. The notes prove elementary conditional spectral, finite-regulator differentiation, and fixed-background consequences. The unsolved work is to control the source-marked fluctuation expansion, RG iteration to the dynamically generated scale, the continuum theory, and the required regulator-uniform estimates while preserving nontrivial Yang–Mills ultraviolet behavior. No such Yang–Mills estimate is claimed here.

## Evidence discipline

- [CLAIMS.json](CLAIMS.json) is the authoritative claim registry.
- [STATUS.json](STATUS.json) records full-problem gates separately from partial lemmas.
- [GOVERNANCE.md](GOVERNANCE.md) defines evidence levels E0–E8, promotion rules, corrections, and announcement language.
- [audit/checklist.md](audit/checklist.md) tracks the obligations of the official problem.
- [audit/objections.json](audit/objections.json) preserves unresolved attacks and defects.
- [research/LOG.md](research/LOG.md) is the chronological research ledger.

Run the repository checks with:

```text
python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

The checks enforce metadata and claim-governance invariants. They do **not** verify deep mathematical truth.

## Non-claims

This repository does not currently construct a four-dimensional continuum Yang–Mills QFT, remove its regulators, verify the full axioms, prove nontriviality, or establish a mass gap. Numerical evidence, fixed-lattice strong-coupling results, lower-dimensional models, and perturbation theory alone would not settle the stated problem.

## Participate critically

Proof-breaking is more valuable than cheerleading. Open an issue with the exact claim ID, the first invalid step, and a counterexample or missing hypothesis when possible. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Official status and prize process

Clay currently lists the problem as unsolved. A prize candidate must be published in a qualifying outlet, survive at least two years of rigorous community examination, achieve general acceptance, and then pass Clay's process. Clay does not accept direct submissions. See the [official rules](https://www.claymath.org/millennium-problems/rules/).

## License

Code and original repository text are released under the [MIT License](LICENSE). External sources retain their own rights.
