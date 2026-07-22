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

### Corrections forced by the audit

- Bałaban's `J` is an auxiliary analytic field, not the scalar observable
  source in Program 002; the new source is named `z`.
- The marginal action is evaluated on a constrained fine minimizing
  background, not automatically as a plain Wilson action of the coarse field.
- RG I announces but defers the proof of its `SU(2)` coupling-flow theorem; it
  is not evidence for the displayed one-loop coefficient.
- A raw coupling-independent block transform, a zero-free source disk, and
  explicit identity/action-density counterterms are now theorem obligations.
- A scalar energy renormalization factor is no longer assumed for arbitrary
  profiles; every symmetry-allowed profile/operator mixing term must be
  classified.

### Not established

- No scalar source propagation or first/second source-derivative bound.
- No completed audit of Large Field II or the imported block-map papers.
- No continuum Schwinger functions, corrected OS reconstruction, uniform
  physical decay estimate, infrared bridge, or Yang–Mills mass gap.

### Next decision

Pin one exact averaging map and every imported domain/norm. Then compute the
first source jet of the raw one-block transform, including its complete
localized projection, before attempting volume-uniform derivative estimates. Refute or rewrite
`YM-RG-001` if that jet fails locality, analyticity, or volume uniformity.
