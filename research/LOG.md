# Research log

Entries are append-only apart from explicit corrections linked to the original entry.

## 2026-07-22 — bootstrap

### Established

- Froze the exact official scope in `PROBLEM.md`.
- Added an E0–E8 evidence ladder and machine-readable solution gates.
- Proved the elementary auxiliary claim `YM-SPEC-001` and listed its failure checks.
- Opened Program 001 to isolate regulator-uniform correlation decay from the spectral deduction.
- Compared major routes and selected Wilson lattice plus gauge-covariant RG as the main scaffold.
- Opened `YM-RG-001`, a deliberately bounded one-block local-observable theorem specification.

### Not established

- No continuum Yang–Mills construction.
- No regulator removal, nontriviality theorem, axiom verification, or Yang–Mills mass gap.
- No independent human review.

### Next decision

Pin the exact Bałaban block-map definitions and norms, then perform a theorem-level comparison against `YM-RG-001`. Rewrite or close the target if the literature already proves it. In parallel, refine Program 001 into an exact limit theorem. No novelty claim is permitted during this extraction phase.

## 2026-07-22 — first source audit and exact gap-transfer bridge

### Established

- Proved the conditional auxiliary claim `YM-SPEC-002`: a total family of
  reflected centered OS forms determines the bottom of the nonvacuum spectrum,
  and a precisely uniform regulator estimate transfers to a continuum gap.
- Fixed the order of limits and quantifiers: first pass regulator correlations
  at fixed physical time, then take the spectral large-time limit.
- Audited RG I, RG II, the convergent-expansion paper, and Large Field I at
  theorem/equation level; recorded Large Field II only at abstract level.
- Verified source-free local analytic polymers and a conditional
  small-/large-field ultraviolet scaffold at the cited anchors.
- Proved the finite-regulator auxiliary claim `YM-RG-002`: for a positive
  coupling-independent raw block kernel, logarithmic source jets are
  conditional cumulants and the constant-profile coupling identity is exact.
- Selected RG I Eq. (0.12), its group mean/contour variables, and the positive
  raw delta pushforward as the first exact block-map interface.
- Audited the imported regular-field/gauge-chart, background-propagator, and
  variational-minimizer papers with theorem/equation anchors.
- Proved `YM-RG-003`: evaluating a finitely supported plaquette insertion on
  the fixed source-free minimizing orbit is representative independent,
  coarse-gauge invariant, and analytic on the proved patch. Kept the exact
  Eq. (190) decay specialization open pending index/norm transcription.
- Opened `YM-RG-004` for the fluctuation difference between that background
  value and the exact conditional first jet.
- Proved the general finite-dimensional coarea corollary `YM-RG-005`: a proper
  smooth surjective submersion has an everywhere positive finite raw fiber
  kernel, while sharp-cutoff positivity and coarse analyticity require extra
  map-specific work.
- Proved the local map-specific corollary `YM-RG-006`: RG I's analytic
  constraint straightening makes the selected map a submersion at every
  admitted background and gives a positive finite precompact fiber ball. The
  full sharp cutoff and every uniform constant remain open.
- Proved YM-RG-007: normalized source ratios are invariant under positive
  coarse-field rescaling of the raw kernel, and bounded observable range gives
  an explicit common zero-free source disk. The absolute SU(2) plaquette bound
  then gives crude uniform first/second-jet bounds once a pointwise finite
  nonzero kernel exists.
- Proved YM-RG-008: RG II Eqs. (1.19)–(1.20) keep the complete fixed-cutoff
  independent-bond cube in one regular chart, so intrinsic coarea gives a
  pointwise finite nonzero positive measure on the entire selected
  near-identity branch.
- Proved YM-RG-009 on one relatively compact Proposition 9 patch: the complete
  selected-branch parameterization is jointly real analytic; its intrinsic
  coarea restrictions form a positive finite Borel kernel with analytic test
  integrals and local holomorphic test-integral continuations; and real coarse
  gauge transformations give an exact pushforward identity between
  equivariantly transported charts.
- Proved YM-RG-010 for the separately named exact RG-I Eq. (2.13)
  Gaussian/cutoff coordinate law: fixed-regulator positivity and normalization,
  patch-local analytic test and source dependence, the centered-score
  background derivative, and exact real transported-chart covariance. No
  equality with the intrinsic coarea or unrestricted raw laws is inferred.
- Proved YM-RG-011 at the RG-II Mayer seam: one real plaquette insertion into
  the exact RG-coordinate law splits into its fixed-background term and one
  bounded centered mark, whose first log-source jet and finite one-mark Mayer
  identity are exact. The mark's rooted localization and decay remain open.

### Corrections forced by the audit

- Bałaban's `J` is an auxiliary analytic field, not the scalar observable
  source in Program 002; the new source is named `z`.
- The marginal action is evaluated on a constrained fine minimizing
  background, not automatically as a plain Wilson action of the coarse field.
- RG I announces but defers the proof of its `SU(2)` coupling-flow theorem; it
  is not evidence for the displayed one-loop coefficient.
- Extending the local positive fiber ball to the entire fixed-cutoff raw
  transform, a zero-free source disk, and explicit identity/action-density
  counterterms are now theorem obligations.
- A scalar energy renormalization factor is no longer assumed for arbitrary
  profiles; every symmetry-allowed profile/operator mixing term must be
  classified.

### Not established

- No quasilocal source propagation or source-marked first/second-derivative
  bound beyond Note 0007's range-only selected-branch estimates.
- No regulator-uniform control of the raw conditional cumulants; their exact
  identities alone do not imply locality or smallness.
- The selected full-cutoff chart branch now has a patch-local Borel kernel and
  exact covariance between equivariantly transported real charts, but equality
  or comparison with the unrestricted raw fiber and compatibility across
  independently selected patches remain open. Note 0007 shows that a uniform
  absolute raw lower bound is generally the wrong target for normalized
  responses.
- No source-marked connected-cluster expansion for the first-jet fluctuation
  remainder.
- No completed full-text audit of Large Field II or source-marked prior-art
  coverage beyond the imported block-map package.
- No continuum Schwinger functions, corrected OS reconstruction, uniform
  physical decay estimate, infrared bridge, or Yang–Mills mass gap.

### Next decision

Prove a per-plaquette rooted analogue of RG II Lemma 2 on Eq. (1.34), with
strict decay slack, then carry the unique mark through Eqs. (2.2)–(2.13) and
prove the rooted connected sum converges. Track raw vacuum mass separately.
Refute or rewrite YM-RG-004 if the marked remainder fails quasilocality,
analyticity, or volume uniformity.
