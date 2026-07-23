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
- [Note 0007: projective source kernels](research/notes/0007-projective-source-kernels.md)
- [Note 0008: complete fixed-cutoff chart branch](research/notes/0008-full-fixed-cutoff-branch.md)
- [Note 0009: parameterized fixed-cube branch kernel](research/notes/0009-parameterized-fixed-cube-kernel.md)
- [Note 0010: exact normalized RG-I coordinate law](research/notes/0010-exact-rg-coordinate-law.md)
- [Note 0011: one marked insertion at the Mayer seam](research/notes/0011-one-mark-mayer-seam.md)
- [Note 0012: rooted cube-count localization of one plaquette mark](research/notes/0012-rooted-plaquette-localization.md)
- [Note 0013: rooted d-k-weighted norm for one interior mark](research/notes/0013-rooted-dk-norm.md)
- [Note 0014: RG-admitted shifted-root cover for every plaquette](research/notes/0014-equivariant-shifted-roots.md)
- [Note 0015: fixed-patch physical composition of one rooted mark](research/notes/0015-fixed-patch-physical-composition.md)
- [Note 0016: exact auxiliary J and fixed-regulator Cauchy tubes](research/notes/0016-auxiliary-j-cauchy-tubes.md)
- [Note 0017: strict auxiliary J margin and dual metric pullback](research/notes/0017-strict-j-margin-metric-pullback.md)
- [Note 0018: raw U collar obstruction and scaled repair target](research/notes/0018-raw-u-collar-obstruction.md)
- [Note 0019: conditional forward multiscale cell-map bridge](research/notes/0019-forward-multiscale-cell-map.md)
- [Note 0020: one-mark Ursell identity on a fixed polymer gas](research/notes/0020-one-mark-ursell-identity.md)
- [Bałaban theorem-level source map](literature/audits/2026-07-22-balaban-source-map.md)
- [Bałaban imported-map audit](literature/audits/2026-07-22-balaban-imported-map.md)

Programs 002 and 003 are open theorem specifications, not results. The notes prove elementary conditional spectral, finite-regulator differentiation, and patch-local selected-branch consequences. They separately name both the intrinsic positive Borel branch kernel and the exact normalized RG-I Gaussian/cutoff coordinate law; neither is identified with the unrestricted raw fiber. A first marked insertion now has an exact background split, finite Mayer identity, rooted decomposition, a conditional RG-II \(d_k\)-weighted norm, and a normalized RG-admitted shifted-root cover for every plaquette in independent variables. On one common physical \((U,J)\) background chart, Note 0015 composes that family and records the exact chain rules; Note 0016 identifies \(J\) with RG I's finite-stencil holomorphic field and proves conditional independent-variable derivative norms on explicit complex tubes at fixed regulator. Note 0017 uses RG I's strict smaller physical representative domain to give a direct-\(J\) sup-norm collar, proves the exact source-measure cancellation and dual \(d_{\mathcal B}\) kernel sum, and obtains a conditional no-volume-loss pullback for the auxiliary-\(J\) chain-rule summand on one matched homogeneous layer. It also shows that the reverse fixed-scale/multiscale bound is not uniform across arbitrary layers. Note 0019 proves the forward all-layer extension under explicit seam-aware ownership, source-admissible interface, exact discrete-tree-lift, support-halo, mesh, and common-chart hypotheses; none of those new premises is silently attributed to the source. Note 0018 proves that a full complex raw per-bond \(U\)-log collar must collapse as \(O(\xi^2)\), and as \(O(\xi)\) in the scaled \(U_A=e^{i\xi A}U\) coordinate, even at the flat background; it replaces that impossible premise by explicit conditional hypotheses for a stronger RG-scaled regularity norm. This still does not prove physical coarse-field quasilocality: the concrete scaled \(U\) collar and pullback, uniform realization of Note 0019's premises, and full chart coefficients remain open. The cover remains covariant only under finite-lattice symmetries preserving the next coarse lattice; full fine-lattice translation covariance, compatibility with one fixed cluster partition, the full physical coarse-derivative norm, and the connected marked expansion remain open. The later work is to close that marked expansion, iterate to the dynamically generated scale, construct the continuum theory, and obtain regulator-uniform estimates while preserving nontrivial Yang--Mills ultraviolet behavior. No such Yang--Mills estimate is claimed here.

Note 0020 now settles the exact distinguished-vertex Ursell formula,
including its \(1/n!\) coefficient, repeated labels, and a conditional pinned
cluster bound, for one fixed hard-core gas. It does not carry the physical
plaquette mark through RG II's cutoffs, conditioning, weakening, and final
polymerization. The post-polymerization marked norm, wall-contact hull
crosswalk, convergence, and branchwise shift synchronization remain part of
the open connected marked expansion above.

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
