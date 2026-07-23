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
- Eq. (2.11), p. 14, is the ordered hard-core gas with one exterior
  \(1/n!\). Its compatibility is zero when two polymers share a cube or a
  complete cube wall. Eqs. (2.12)–(2.13) use the connected-graph coefficient
  with no internal factorial and group the logarithm by
  \(X=\bigcup_i Z_i\).
- Lemma 3, p. 20, Eq. (2.38), gives the unmarked bound
  \(C_3\varepsilon_1
  e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)}\). Equation (2.41) spends two more
  delta units and gives
  \(O(1)C_3\varepsilon_1
  e^{-(1-10\delta)(L/2)\kappa d_{k+1}(X)}\). The induction then chooses
  \((1-10\delta)L/2=1\). The Project Euclid page images were subsequently
  inspected directly in Note 0024 and confirm the \(8\delta\), \(9\delta\),
  \(10\delta\), and \(L/2\) glyphs.
- These are source-free activity bounds. The paper's \(J\) is an auxiliary
  gauge-field/derivative variable in the analytic induction, not a scalar
  observable source.
- The exact algebraic insertion seam is after Lemma 2 and before Section 2
  Eq. (2.1): [Note
  0011](../../research/notes/0011-one-mark-mayer-seam.md) inserts one
  background-centered plaquette mark and proves the finite one-mark Mayer
  identity there.
- [Note
  0020](../../research/notes/0020-one-mark-ursell-identity.md) differentiates
  the exact fixed-gas connected formula and proves the distinguished-slot
  \(1/n!\) coefficient, the need for repeated polymer labels, and a
  conditional pinned Kotecky--Preiss implication. RG II does not print this
  marked theorem, and its unmarked Lemma 3 does not bound the differentiated
  activity. [Note
  0021](../../research/notes/0021-one-mark-section2-factorization.md) then
  reruns Eqs. (2.1)--(2.10) with the localized support in the seed, defines
  the decorated post-conditioning mark, proves the unique marked-component
  factorization, and obtains the exact finite hard-core numerator. This is a
  repository corollary, not a theorem printed by RG II.
- In the marked corollary, the global cutoff, Gaussian law, quadratic
  operator, fixed background/chart, partition, and unmarked potentials remain
  source-parameter independent. The seed-derived cutoff split, exterior-bond
  family, \(Z_0\), conditioned restriction, \(Z_0'\), weakening family, and
  allowed \(Z\)'s nevertheless depend combinatorially on the marked support
  and must be reconstructed. Equation (2.8) weakens the entire transformed
  integrand, so its derivatives may hit the mark. Direct marked domination,
  the hull metric, convergence, and branchwise shifted construction remain
  separate hypotheses.
- [Note
  0022](../../research/notes/0022-whole-integrand-marked-cauchy.md) observes
  that Eq. (2.8) applies the Section-1 decomposition to the complete
  standardized integrand. Under common \(L^1\)-holomorphy and a joint
  majorant, one iterated contour for that whole marked integrand captures
  every derivative placement with no extra Leibniz or decoration-allocation
  multiplicity, and with the ordinary Cauchy-radius factors if the marked
  term shares the source radius. This repository corollary still requires a
  common transformed complex domain and one joint relative Gaussian-moment
  majorant; the source's unmarked Eq. (2.14) estimate and the earlier
  Eq. (1.34) marked input norm do not by themselves prove either.
  The accessible OCR also does not settle every transformed sharp-cutoff
  glyph. A weakening-dependent nonholomorphic cutoff cannot be placed under
  the marked contour without a separate source-valid derivative estimate.
- [Note
  0023](../../research/notes/0023-fixed-cubical-hull-animals-kp.md) takes
  Eqs. (2.11)--(2.13)'s cube-or-complete-wall incompatibility and
  literal-union grouping only as a convention anchor. On a separately
  declared fixed cubulation by closed cubes, it proves a literal-union hull
  inequality with contact charge \(\sqrt{D+3}\), a volume-uniform geometric
  animal sum, and an explicit sufficient pinned Kotecky--Preiss condition.
  In \(D=4\), its coarse size slope is \(32\), its safe wall-contact charge is
  \(\sqrt7\), and its sufficient animal threshold is \(64\log8\). These
  constants and the piecewise-linear contained-tree model are repository results,
  not statements printed by RG II. [Note
  0024](../../research/notes/0024-balaban-final-gas-instantiation.md) then
  identifies the final connected ordinary source gas with that model and
  gives a displayed-hierarchy-compatible sufficient ordinary KP window. The
  intermediate objects and decorated marked species remain excluded.
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
| One marked plaquette at the RG-II Mayer seam | Finite background split and Mayer algebra proved in Note 0011; Note 0012 proves the fixed-partition-interior mixed-difference/cube-count result; Note 0013 upgrades the standard \(M\)-cube branch to a conditional rooted \(d_k\) norm; Note 0014 covers every plaquette with a coarse-lattice-preserving shifted family; Note 0015 supplies fixed-chart physical composition; Note 0016 identifies the exact auxiliary field and supplies conditional fixed-regulator independent-variable derivative norms; Note 0017 supplies the strict representative-\(J\) collar, dual source convolution, and a homogeneous-layer \(J\)-summand pullback while disproving only the reverse uniform cross-layer bound; Note 0018 proves the naive raw \(U\) collars collapse and isolates a conditional scaled replacement; Note 0019 proves a conditional forward all-layer \(J\) bridge under unverified interface/tree/support/mesh/chart premises; Note 0020 proves the fixed-gas connected algebra; Note 0021 carries one localized mark through the exact fixed-partition Section-2 map and component factorization. Unit translations, discharge of the geometric and scaled-\(U\) premises, the actual marked conditioning/weakening norm, shifted synchronization, the full physical derivative norm, and the convergent connected marked expectation remain open |
| Whole-integrand control of marked Eq. (2.8) weakening derivatives | Under common \(L^1\)-holomorphy and a joint majorant, Note 0022 proves the exact mixed-difference contour with no extra derivative-allocation entropy, and with the ordinary Cauchy-radius factor if that radius is shared. The actual common transformed domain, joint Gaussian envelope, marked kernel decay, and gluing estimates remain open |
| Fixed-cubical hull, animals, and pinned KP | Note 0023 proves the literal-union connector inequality, a uniform geometric animal bound, and a sufficient pinned-KP system for one declared closed-cube model. Note 0024 verifies from primary pages that the final connected ordinary RG-II gas instantiates its support class, quotient seams, metric, incompatibility, literal union, and aggregated one-species convention, and gives an explicit displayed-hierarchy-compatible ordinary smallness window. The intermediate objects and decorated marked norm remain open |
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
