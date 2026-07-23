# Bałaban source-map audit — 2026-07-22

Status: theorem-level route audit; no novelty claim and no Yang–Mills solution
claim.

This audit distinguishes statements checked in full primary text from claims
seen only in bibliographic metadata or an abstract. Page numbers below are
printed journal pages, not PDF indices.

## Full-text-verified anchors

### RG I: small-field effective actions

T. Bałaban, *Renormalization group approach to lattice gauge field theories I:
Generation of effective actions in a small field approximation and a coupling
constant renormalization in four dimensions*, **CMP 109** (1987), 249–301,
[doi:10.1007/BF01215223](https://doi.org/10.1007/BF01215223).

- The abstract and pp. 249–250 explicitly restrict the analysis to the
  small-field approximation.
- A concrete restricted block transformation appears at Eq. (0.16), p. 255;
  the action/coupling recursions are Eqs. (0.17)–(0.20), pp. 255–256. The later
  full-density paper also says that the averaging operation may be either
  (0.4) or (0.12), subject to stated general properties, so “the Bałaban map”
  is not unique until one choice is pinned.
- The local remainder is represented by gauge-invariant analytic functions
  \(E^{(j)}(X,U)\) in Eqs. (0.24)–(0.25), p. 257, with exponential decay in
  the polymer-size function. Ward–Takahashi extraction of the action marginal
  and the resulting irrelevant bounds are summarized in Eqs. (0.28)–(0.30),
  pp. 258–259.
- The coarse action is evaluated through the constrained minimizing
  background: Eq. (1.1) and the paragraph following it, p. 260, define
  \(U_k(V)\) and state \(A_k(V)=A_k(U_k(V))\). Replacing this by a plain
  Wilson action of \(V\) is therefore an additional theorem, not a notational
  simplification.
- Eqs. (2.2)–(2.13), pp. 265–268, put the fluctuation integral on a complete
  independent-bond coordinate cube after analytically straightening and
  eliminating the averaging constraint. Eq. (2.16), p. 269, states that every
  Eq. (2.12) expression and its Gaussian measure are invariant under the
  displayed real coarse gauge transformations; the fixed cutoff is preserved
  by local orthogonal adjoint maps.
- Together with the variational paper's Proposition 9 branch and Eq. (181),
  those formulas give a patch-local jointly analytic selected-branch
  parameterization and exact transported-chart covariance. The intrinsic
  coarea consequence is [Note
  0009](../../research/notes/0009-parameterized-fixed-cube-kernel.md). This is
  not a global background atlas or an identification with the unrestricted
  raw group-delta fiber.
- Theorem 3, p. 264, is conditional on every effective coupling \(g_k\)
  remaining in a sufficiently small interval and gives the inductive
  small-field action structure for compact semisimple \(G\subset U(N)\) in
  \(d=4\).
- Important exclusion: Theorem 2, p. 259, states an \(SU(2)\) coupling-flow
  result, but the immediately following paragraph says its perturbative proof
  will be given in a separate paper. It is an announced result here, not a
  proved input, and no one-loop numerical coefficient is established by this
  paper.

### RG II: localization and cluster completion of the small-field step

T. Bałaban, *Renormalization group approach to lattice gauge field theories II:
Cluster expansions*, **CMP 116** (1988), 1–22,
[doi:10.1007/BF01239022](https://doi.org/10.1007/BF01239022).

- The abstract and introduction say this paper completes the small-field
  effective-action construction and the proof of RG I's Theorem 3.
- Lemma 2, p. 11, Eqs. (1.41)–(1.43), gives a local analytic
  fluctuation-action decomposition with gauge-invariance and decay bounds.
- Eqs. (2.12)–(2.13), p. 14, give the connected/exponentiated cluster
  expansion for the new effective interaction.
- Lemma 3, p. 20, Eq. (2.38), gives an exponentially decaying activity bound;
  the final paragraph on p. 22 closes the inductive proof.
- These are source-free activity bounds. The paper's \(J\) is an auxiliary
  gauge-field/derivative variable in the analytic induction, not a scalar
  observable source.
- The exact algebraic insertion seam is after Lemma 2 and before Section 2
  Eq. (2.1): [Note
  0011](../../research/notes/0011-one-mark-mayer-seam.md) inserts one
  background-centered plaquette mark and proves the finite one-mark Mayer
  identity there.
- RG II Eqs. (1.9)--(1.10) give the finite weakening-variable decomposition
  and root-component cancellation; Eqs. (1.17)--(1.21) give the weakened
  reconstruction and its common \(|s(\Delta)|\le e^{\kappa _1}\) analytic
  bound; Eq. (1.34) is the local independent-variable domain. [Note
  0012](../../research/notes/0012-rooted-plaquette-localization.md) applies
  those inputs to the centered plaquette trace and proves a repository
  mixed-difference corollary with a conditional cube-count norm for plaquettes
  interior to one fixed partition.
- RG II does not print that marked theorem. Note 0012 does not import the
  source-free cubic cancellation in Eqs. (1.39)--(1.40), and at that stage it
  left the minimizing-background pullback and connected marked bound open. [Note
  0013](../../research/notes/0013-rooted-dk-norm.md) combines RG I's p. 257
  shortest-tree definition with RG II Eq. (1.32) to close the \(d_k\)-weighted
  norm on the standard fixed-partition \(M\)-cube branch, conditional on the
  source-safe consequence \(\kappa _1-1\ge(1-\delta)\kappa\) and explicit
  repository entropy margin \(\delta\kappa>\log64\). The available text layers
  drop the exact printed leading prefactor; its visual transcription remains
  open. [Note 0014](../../research/notes/0014-equivariant-shifted-roots.md)
  averages the marked family over the RG-admitted \(L\)-spaced shifts, using a
  repository stabilizer average to make the intermediate weakening equivariant.
  It covers every plaquette and transports under the subgroup preserving the
  next coarse lattice, not under arbitrary unit translations.
- [Note 0015](../../research/notes/0015-fixed-patch-physical-composition.md)
  conditionally evaluates that shifted family on one common holomorphic
  physical \((U,J)\) chart. It preserves the exact identity, fluctuation
  centering/locality, and zeroth-order norm and records both chain-rule terms.
  [Note 0016](../../research/notes/0016-auxiliary-j-cauchy-tubes.md) then uses
  RG I Eqs. (1.8), (1.10), (1.15)--(1.16), and (3.10)--(3.11) to identify the
  physical auxiliary field exactly, including its local first-differential
  remainder. Full complex chart tubes give fixed-regulator rooted
  independent-variable derivative norms, and Eq. (190) gives qualitative
  auxiliary-field derivative decay on each fixed chart. These repository
  lemmas are not printed in RG II. [Note
  0017](../../research/notes/0017-strict-j-margin-metric-pullback.md) then
  uses RG I's strict smaller physical representative domain to give a direct
  \(J\) collar under a frozen hierarchy, proves the Eq. (190) source-density
  cancellation and dual weighted sum, and closes the auxiliary-\(J\)
  pullback on one matched layer. It also disproves a uniform reverse
  cross-layer bound. Note 0019 proves the forward all-layer \(J\)-summand
  implication only under explicit seam-aware ownership, source-admissible
  interface, discrete-tree-lift, support, mesh, and common-chart premises;
  the source does not print those premises. Note 0018 proves that the naive
  full raw and \(\xi\)-scaled bond-sup \(U\) collars collapse. A scaled \(U\)
  pullback and uniform realization of Note 0019's geometry remain open, so
  there is still no full regulator-uniform physical derivative or quasilocal
  norm.

### Convergent expansions: conditional complete-density scheme

T. Bałaban, *Convergent renormalization expansions for lattice gauge theories*,
**CMP 119** (1988), 243–285,
[doi:10.1007/BF01217741](https://doi.org/10.1007/BF01217741).

- The introduction, pp. 243–245, studies the unrestricted transformation
  \(T\) together with a separate large-field operation \(R\); it explicitly
  allows the alternative averaging maps (0.4) and (0.12) of RG I.
- Eq. (2.23), pp. 258–259, decomposes the source-free effective action into
  the basic action plus regular terms \(E_k\), \(R\)-operation terms \(R_k\),
  and boundary terms \(B_k\) near large-field regions, with the paper's stated
  localization, analyticity, and gauge-covariance structure.
- Theorem 1, p. 262, propagates the full inductive density assumptions under
  successive \(RT\) operations, conditional on the coupling sequence
  satisfying RG I's recursive equations and inequality (I.0.33), and
  conditional on the stated \(R\)-operation assumptions.
- Theorem 2, p. 263, gives localized effective-action bounds with a constant
  independent of the listed step/domain data and the torus. Corollary 3,
  p. 264, gives an ultraviolet-stability bound with constants independent of
  lattice spacing \(\eta\) and torus \(T\), but dependent on the effective
  coupling \(g_k\) and under Theorem 1's hypotheses.
- Scope warning: these uniformities concern the source-free
  effective-density/partition-function construction. They do not supply
  uniform bounds for source derivatives, Schwinger functions, an
  infinite-volume continuum measure, or a physical mass gap.

### Large Field I: construction begun, completion deferred

T. Bałaban, *Large field renormalization I: The basic step of the R operation*,
**CMP 122** (1989), 175–202,
[doi:10.1007/BF01257412](https://doi.org/10.1007/BF01257412).

- The abstract, p. 175, says the \(R\) operation removes the main obstacle to
  four-dimensional ultraviolet stability and explicitly defers completion to
  Part II.
- The concluding discussion, p. 202, likewise defers localization, polymer
  representation, and exponentiation of the remaining expression to the next
  paper.

## Abstract-only claim; not yet a theorem dependency

T. Bałaban, *Large field renormalization II: Localization, exponentiation, and
bounds for the R operation*, **CMP 122** (1989), 355–392,
[doi:10.1007/BF01238433](https://doi.org/10.1007/BF01238433).

The publisher abstract says the paper completes the proof of ultraviolet
stability of four-dimensional pure gauge theories “as formulated in Theorem
1.” The full theorem statement, hypotheses, equations, and proof have not yet
been audited here. Until that is done, record this only as an abstract-level
orientation claim; do not use it to close a dependency or to infer observable,
OS-positivity, continuum, or gap results.

## Capability matrix for Program 002

| Interface | Audit result |
|---|---|
| Source-free local polymers, analytic domains, gauge invariance, exponential decay | Verified in RG I/II at the anchors above |
| Selected fixed-cutoff branch: patch-local Borel kernel, analytic tests, real coarse-gauge covariance | Derived in Note 0009 from the verified RG-I/II and variational anchors; global chart compatibility and unrestricted-fiber comparison remain open |
| Exact normalized Eq. (2.13) Gaussian/cutoff coordinate law | Separately named and analyzed in Note 0010; no equality with the intrinsic coarea or unrestricted raw law is inferred |
| Small-/large-field density decomposition and conditional UV-stability bounds | Verified in the Convergent paper; final \(R\)-operation completion remains abstract-only in this audit |
| External scalar source \(zf\), propagation under a block map, and \(\partial_z\), \(\partial_z^2\) bounds | No theorem located in the audited texts |
| Source-jet norm, localized marginal projections, or volume-uniform first/second derivative bounds | No theorem located |
| Inserted-observable decomposition compatible with the constant-profile derivative | No theorem located; the raw first-jet identity itself is algebraic once a coupling-independent raw transform is fixed |
| One marked plaquette at the RG-II Mayer seam | Finite background split and Mayer algebra proved in Note 0011; Note 0012 proves the fixed-partition-interior mixed-difference/cube-count result; Note 0013 upgrades the standard \(M\)-cube branch to a conditional rooted \(d_k\) norm; Note 0014 covers every plaquette with a coarse-lattice-preserving shifted family; Note 0015 supplies fixed-chart physical composition; Note 0016 identifies the exact auxiliary field and supplies conditional fixed-regulator independent-variable derivative norms; Note 0017 supplies the strict representative-\(J\) collar, dual source convolution, and a homogeneous-layer \(J\)-summand pullback while disproving only the reverse uniform cross-layer bound; Note 0018 proves the naive raw \(U\) collars collapse and isolates a conditional scaled replacement; Note 0019 proves a conditional forward all-layer \(J\) bridge under unverified interface/tree/support/mesh/chart premises; unit translations, discharge of those premises, the scaled nonlinear \(U\) collar/pullback, one-fixed-partition compatibility, the full physical derivative norm, and the connected marked expectation remain open |
| One-loop coefficient in the source-inserted normalization | Not proved by RG I; its coupling theorem is deferred |
| Reflection positivity of gauge-fixed/RG effective actions | No theorem located |
| Continuum Schwinger functions, OS reconstruction, infinite-volume clustering, mass gap | Outside the verified scope |

“No theorem located” is a bounded negative search result, not proof of absence
from the literature. It is enough to keep `YM-RG-001` at E0 and to define the
next search target; it is not enough for a novelty claim.

## Crosswalks and unresolved dependencies

- Program 002's coefficient \(4g^{-2}\) versus Bałaban's inverse-coupling
  coefficient gives the working crosswalk \(g_B^{-2}=4g^{-2}\) after matching
  normalized-trace conventions. This is our convention translation, not a
  quoted Bałaban theorem, and must be rechecked against the finally selected
  block map.
- OCR commonly renders the \(R\) operation as `IR` or `U`, and \(SU(2)\) as
  `St/(2)`; normalized notation above follows the printed titles/context.
- RG I imports the averaging, regular-configuration/gauge-fixing,
  background-propagator, and constrained-minimizer machinery from earlier
  papers. The follow-up [imported-map
  audit](2026-07-22-balaban-imported-map.md) now checks those propositions,
  selects Eq. (0.12), and records RG II's complete-cube chart bound. Note 0008
  constructs the pointwise measure on that selected chart branch; comparison
  with the unrestricted raw fiber and exact norm transcription remain separate
  dependencies.
- Bibliographic metadata for the five papers and DOIs above is confirmed. The
  unresolved bibliographic item is the separate paper promised for RG I
  Theorem 2; this audit has not identified and verified it.

## Result

Bałaban supplies a strong source-free ultraviolet scaffold: gauge-covariant
blocking, fine minimizing backgrounds, localized analytic polymer actions,
and a conditional small-/large-field density scheme. The first genuinely
unclosed interface for this repository is still the one-block
observable/source extension with uniform derivative bounds. Even proving that
interface would remain an auxiliary result: it would not establish the
continuum theory or its mass gap.
