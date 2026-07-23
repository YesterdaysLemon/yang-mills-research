# Literature and status search log

Searches record dates, sources, and scope. “No result found” never proves novelty.

## 2026-07-22 — official target and status

Sources checked:

1. [Jaffe and Witten, official problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
2. [Clay Yang–Mills problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
3. [Clay list of Millennium Prize Problems](https://www.claymath.org/millennium-problems/)
4. [Clay prize rules](https://www.claymath.org/millennium-problems/rules/)

Finding: Clay lists the problem as unsolved. The official target includes continuum existence, nontriviality, axiomatic strength, correct Yang–Mills short-distance structure, and a finite positive Hamiltonian gap for every compact simple gauge group.

## Required databases before any novelty claim

- MathSciNet
- zbMATH Open
- arXiv
- INSPIRE
- Crossref
- backward and forward citation chains from the closest primary papers

Every future search must record exact queries, date, identifiers, inclusion/exclusion criteria, and a theorem-level comparison. No claim in the current registry asserts novelty.

## 2026-07-22 — route-level primary-source scout

Queries covered Wilson lattice gauge theory, reflection positivity and transfer matrices, Bałaban's gauge-field renormalization group, the fixed-IR-cutoff constructive approach, strong-coupling functional inequalities, stochastic gauge-field constructions, and large-\(N\) expansions.

Provisional result: Wilson plus Bałaban provides the strongest existing gauge-invariant ultraviolet scaffold, but the reviewed sources do not claim the full local-observable continuum construction or a volume-uniform physical mass gap. A one-block source-insertion theorem was selected as a bounded first target. This is a route decision, not a novelty finding.

Primary identifiers added to `literature/primary-sources.md`. Next search must inspect the full Bałaban papers and their citation graph at theorem level; abstract-level comparison is insufficient.

## 2026-07-22 — Bałaban theorem-level source map

Full text checked:

1. [RG approach I](https://doi.org/10.1007/BF01215223), especially Eqs.
   (0.16)–(0.30), Eq. (1.1), and Theorems 2–3;
2. [RG approach II](https://doi.org/10.1007/BF01239022), especially Lemmas
   2–3 and Eqs. (1.41)–(1.43), (2.12)–(2.13), and (2.38);
3. [Convergent renormalization
   expansions](https://doi.org/10.1007/BF01217741), especially Eq. (2.23),
   Theorems 1–2, and Corollary 3;
4. [Large field renormalization
   I](https://doi.org/10.1007/BF01257412), abstract and concluding scope.

Abstract and bibliographic metadata only:

5. [Large field renormalization
   II](https://doi.org/10.1007/BF01238433).

Finding: the audited full texts provide source-free gauge-invariant analytic
polymer structure, small-field cluster completion, and a conditional
small-/large-field ultraviolet-stability framework. No theorem was located for
an external scalar plaquette source, its first two source derivatives, the
Program 002 localized source-jet norms/bounds, or reflection positivity of the resulting
effective actions. RG I's stated `SU(2)` coupling theorem is explicitly
deferred rather than proved there.

The exact page/equation map and scope cautions are in
`literature/audits/2026-07-22-balaban-source-map.md`. “No theorem located” is a
bounded negative search result, not a novelty proof. The imported averaging,
gauge-fixing, propagator, minimizer, and Large Field II dependencies remain to
be audited.

## 2026-07-22 — imported Bałaban block-map package

Full text checked:

1. [Averaging operations](https://doi.org/10.1007/BF01211042), especially
   Eqs. (10)–(15), Eq. (42), and Proposition 3;
2. [Regular configurations and gauge
   fixing](https://doi.org/10.1007/BF01466594), especially Eqs.
   (1.3)–(1.14), Theorems 2 and 8, and Proposition 6;
3. [Background propagators](https://doi.org/10.1007/BF01240355), especially
   Eqs. (3.35)–(3.48), Theorems 3.1–3.4, 3.12, 3.14, and 3.15;
4. [Variational problem/background
   fields](https://doi.org/10.1007/BF01229381), especially Theorem 1,
   Section G, Eq. (181), and Proposition 9;
5. RG I Eqs. (0.4)–(0.16) and Eq. (2.9), to connect those imports to its
   small-field step.

Decision: freeze RG I Eq. (0.12) for the first source experiment because it
uses the same Euclidean-symmetric contour mean as the paper's gauge fixing.
Use the pre-gauge-fixing delta pushforward as the raw transform, construct its
pointwise positive fiber measure separately, and keep normalizations and
cutoffs separate. For the first restricted theorem, use the fixed
\(\varepsilon_1\) cutoff rather than the explicitly offered coupling-dependent
alternative.

The unique object proved by the variational theorem is initially a minimizing
gauge orbit. Proposition 9 supplies an analytic, gauge-covariant,
exponentially quasilocal branch only after a local gauge is fixed. The
background-propagator decay is a finite-scale Gaussian/locality result, not an
interacting correlation decay or mass gap. The exact map and theorem anchors
are recorded in `literature/audits/2026-07-22-balaban-imported-map.md`.

Resulting gap: no audited paper controls the difference between the exact
conditional plaquette first jet and its minimizing-background value by a
source-marked, volume-uniform polymer expansion. This bounded gap is now
`YM-RG-004`; it is not a novelty claim.

## 2026-07-22 — pointwise fiber and constraint normal form

The formal group delta was separated from ordinary probability
disintegration. A regular conditional probability exists only relative to the
pushforward measure and only almost everywhere; the raw transform against
coarse Haar measure also needs its density \(T\mathbf 1(V)\).

The smooth coarea formula and proper-submersion fiber integration give a clean
conditional remedy, recorded as `YM-RG-005`: a proper smooth surjective map
with full rank has an everywhere finite positive raw fiber kernel. This is a
general finite-dimensional lemma, not yet a claim about the whole selected
cutoff.

Full text of RG I pp. 265–268 was then checked. Eqs. (2.2)–(2.4), the
right-inverse construction after Eq. (2.10), and Eq. (2.12) analytically
straighten the nonlinear constraint and eliminate one selected bond per coarse
bond. This proves the local submersion and positive precompact-fiber corollary
`YM-RG-006`. RG I alone does not close the whole support. RG II
Eqs. (1.19)–(1.20), however, show that every independent field in the complete
fixed-cutoff cube stays in the same selected analytic chart with an absolute
support-containment constant. The papers still do not identify this branch
with the unrestricted raw group fiber or provide a volume-independent scalar
determinant or total-mass lower bound.

## 2026-07-22 — raw mass versus normalized source control

The next audit separated an absolute raw cutoff mass from the normalized
source law. Multiplying a raw kernel by any positive source-independent
coarse-field factor changes its mass but not a normalized source ratio or any
source cumulant. An \(n\)-fold product cutoff can have raw mass \(q^n\to0\)
even with unit normal Jacobian and uniform per-coordinate geometry.

This refutes a volume-independent raw lower bound as the default Program 003
target. YM-RG-007 instead proves an explicit zero-free disk from bounded
observable range and identifies the centered density score as the
projectively invariant coarse-field derivative. Combining the complete-cube
support-containment bound with intrinsic coarea gives YM-RG-008, the pointwise
positive measure on the entire selected Eq. (0.12) fixed-cutoff chart branch. Equality
or comparison with the unrestricted raw fiber, cross-patch covariance,
coarse-field holomorphy, and marked-polymer locality remained open at that
audit stage. Notes 0009--0012 later supplied patch-local transported covariance,
local analytic-test continuation, and a conditional independent-variable
cube-count localization for one mark. Note 0013 subsequently supplied the
standard fixed-partition \(d_k\)-weighted upgrade under an explicit entropy
margin. At that stage global patch compatibility, shifted roots, the
minimizing-background pullback, and the connected marked expectation remained
open. Note 0014 subsequently supplied an all-plaquette RG-admitted shifted
cover and coarse-lattice-preserving transport. Unit translations and
one-fixed-partition cluster compatibility remain open.

## 2026-07-22 — RG-II Eq. (1.32) prefactor audit

The [RG-II article](https://doi.org/10.1007/BF01239022), Project Euclid record
`cmp/1104161193`, and [archived issue
scan](https://archive.org/details/sim_communications-in-mathematical-physics_1988-04_116_1)
were cross-checked for the hierarchy following Eq. (1.32). The accessible text
layers drop a leading glyph immediately before \((\kappa _1-1)\), while a
reproducible rendering of that page was not available in this audit. The exact
printed prefactor is therefore not transcribed as a repository fact.

Note 0013 uses only the weaker consequence
\(\kappa _1-1\ge(1-\delta)\kappa\), which is common to the candidate readings
identified by the audit. Its strict \(\delta\kappa>\log64\) margin is derived
repository bookkeeping, not a quotation of the paper. An archived visual
transcription remains an open source-audit item.

## 2026-07-22 — RG-I Eq. (2.17) shifted-root transport audit

RG I p. 269 was rechecked against the [primary
article](https://doi.org/10.1007/BF01215223). The sentence before Eq. (2.17)
restricts the Euclidean symmetry to one preserving
\(\mathbb T^{(k+1)}\); Eq. (2.17) defines the field pullback, and the discussion
after Eqs. (2.17)--(2.18) supplies the induced split and orthogonal fluctuation
transformation. It does not print covariance for arbitrary unit shifts or for
RG II's intermediate weakening variables.

Note 0014 therefore uses only translations by multiples of \(L\) and makes
the generalized-random-walk weakening equivariant by an explicit finite
stabilizer average. That Reynolds symmetrization is repository algebra: it
preserves the exact propagator sum, localization, and analytic bound, but is
not attributed to Bałaban as the printed expansion. Full unit-translation
covariance remains open.
