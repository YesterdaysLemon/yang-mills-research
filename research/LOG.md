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
  coarse-gauge invariant, and analytic on the proved patch. Eq. (190)'s five
  component derivative bounds are now transcribed with their
  \(j\), \(j'\), \(\zeta\), and \(\delta_0/8\) factors; the physical-chart and
  activity-norm crosswalk remains open.
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
  identity are exact. This note alone does not localize the mark.
- Proved YM-RG-012 on RG-II's independent-variable domain: for each plaquette
  interior to a fixed-partition cube, finite mixed differences give an exact
  root-connected decomposition, and
  Cauchy decay plus a bounded-degree animal count gives a conditional,
  cube-count norm uniform over plaquettes interior to one fixed partition.
  At that stage shifted roots, the \(d_k\) upgrade, minimizing-background
  pullback, full Euclidean covariance, and the connected marked expectation
  remained open.
- Proved YM-RG-013 on the standard wall-adjacent \(M\)-cube branch: RG I's
  shortest-tree definition gives \(d_k(Y)\le m(Y)\), and the source-safe
  hierarchy consequence plus the explicit entropy condition
  \(\delta\kappa>\log64\) upgrade Note 0012 to a rooted
  \((1-2\delta)\kappa d_k\)-weighted norm. This threshold is repository
  bookkeeping, not a printed Bałaban constant. The exact leading prefactor
  dropped by the available RG II Eq. (1.32) text layers remains visually
  unaudited.
- Proved YM-RG-014 for \(M=L^m\), \(m\ge2\): the RG-admitted translations by
  multiples of \(L\) give every plaquette at least \((M/L-1)^4\) interior
  roots. A normalized shifted-family average preserves the Note 0013 weighted
  norm without an orbit factor. A finite stabilizer average of the generalized
  random-walk terms supplies exact weakened transport under the subgroup
  preserving the next coarse lattice. This does not prove unit-translation
  covariance or compatibility with one fixed Section-2 cluster partition.
- Proved YM-RG-015 on one common holomorphic physical \((U,J)\) chart:
  evaluation of the shifted family preserves the exact
  all-plaquette identity, joint holomorphy, strict fluctuation locality,
  zero-fluctuation centering, transported real-chart covariance, and the
  zeroth-order \(d_k\) norm. The exact chain rule keeps both the \(U\)- and
  \(J\)-derivative terms.
- Proved YM-RG-016 at fixed regulator. RG I defines
  \(J=\mathscr J_\xi(U)=D_U^{\xi *}\xi^{-2}\pi\operatorname{im}(dU)\), so the
  physical auxiliary field is a finite-stencil holomorphic equivariant
  function of the minimizing background. Its exact first differential is the
  covariant Laplacian term plus the derivative of RG I's local remainder.
  Compact containment in full complex chart tubes gives conditional rooted
  operator-norm bounds \(\mathcal B_d/r_U\) and \(\mathcal B_d/r_J\) for the
  independent-variable activity derivatives. Proposition 9 Eq. (190) also
  gives qualitative exponential decay for the composed auxiliary-field
  derivative on each fixed chart, with a deliberately nonuniform constant.

### Corrections forced by the audit

- Bałaban's `J` is an auxiliary analytic field, not the scalar observable
  source in Program 002; the new source is named `z`.
- RG I actually defines that auxiliary field and its gauge law explicitly;
  treating the physical \(J\)-lift as an independent holomorphy hypothesis was
  too conservative. The correction does not supply uniform chart radii or a
  physical activity derivative norm.
- Proposition 9's decay uses the multiscale distance \(d_{\mathcal B}\), not
  the rooted polymer distance \(d_{k,\sigma}\). No equality or uniform
  comparison between them is assumed.
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
  expectation bound. Notes 0012--0014 control the pre-integration mark in
  independent variables, including its standard-branch \(d_k\) norm and an
  all-plaquette shifted cover. Notes 0015--0016 supply fixed-chart physical
  composition, the exact auxiliary-field reduction, and conditional
  fixed-regulator independent-variable derivative norms, but not a uniform
  physical coarse-background derivative tail, one-fixed-partition cluster
  compatibility, or the connected expectation.
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

Quantify full complex tube radii and all chart/differential-of-exponential
factors uniformly, then prove the \(d_{\mathcal B}\)-to-\(d_{k,\sigma}\)
comparison and exponential convolution budget needed to turn Notes 0015--0016
into a summable physical coarse-field derivative norm. Then reconcile the
shift family with one Section-2 partition, carry the unique mark through Eqs.
(2.2)–(2.13), and prove the rooted connected sum converges. Track raw
vacuum mass separately.
Refute or rewrite YM-RG-004 if the marked remainder fails quasilocality,
analyticity, or volume uniformity.

## 2026-07-22 — strict \(J\) margin and source-metric pullback

### Established

- Rechecked RG I Eqs. (1.11)--(1.16) and the printed p. 263 smaller-domain
  discussion. The direct independent \(J\) bound is condition (iii), while
  condition (iv) uses auxiliary fields derived from \(U\) and is unchanged
  by an independent \(J\) perturbation.
- Proved YM-RG-017 under one explicitly frozen strict physical
  representative hierarchy. The direct bond-sup \(J\) coordinate has the
  full complex collar
  \(\Delta_J=\alpha_0-\bar\alpha_0\), and the rooted activity derivative norm
  is \(\mathcal B_d/\Delta_J\). This refinement does not use regulator-family
  compactness and does not create a \(U\) collar.
- Put Proposition 9 Eq. (190) in its source-density normalization. The
  \(s_{j'}^d\) source measure cancels the printed \(s_{j'}^{-d}\) kernel
  factor exactly. Propagators-II Lemma 2.1 then gives a dual
  \(d_{\mathcal B}\)-weighted source row sum at every
  \(0\le\gamma<\delta_0/8\).
- Used finite-dimensional \(\ell^\infty\)-\(\ell^1\) duality before summing
  output cells. This composes the Eq. (190) kernel with the Cauchy activity
  derivative without a polymer-volume factor.
- On one scale-matched homogeneous layer, proved the contained-tree
  comparison
  \(D_{\mathcal B}(q,Y)\le M d_{k,\sigma}(Y)+2d(M+1)\) and the conditional
  auxiliary-\(J\) pullback norm with exponent budget
  \(a_*+\gamma M\le a\).
- Proved that no uniform reverse metric bound follows: travel \(r-r_0\)
  layers coarser changes the fixed-scale/multiscale ratio by
  \(L^{r-r_0}/M\). This does not obstruct the forward inequality needed by
  the pullback. That direction remains unproved because interface charges
  and alignment of generic Note 0014 shifts have not been controlled.

### Not established

- No regulator-uniform nonlinear \(U\)-activity collar or
  \(D_U\widehat W[D\mathcal U\,h]\) pullback.
- No uniform bound for every differential-of-exponential,
  gauge-restoration, and local auxiliary-\(J\) coefficient across the chart
  family.
- No cross-layer network norm compatible with the full shifted family.
- No one-fixed-partition connected marked expectation, RG iteration,
  continuum construction, infrared estimate, or Yang--Mills mass gap.

### Next decision

Prove the one-sided cross-layer interface bound needed by the pullback, define
a multiscale network norm using the Propagators-II layer weights and interface
penalties, or prove that the marked construction can be confined to one
matched layer. In
parallel, derive a quantitative stability theorem for the scaled relative
\(U\)-chart constraints; only then combine both chain-rule summands and enter
the fixed Section-2 connected expansion.

## 2026-07-22 -- raw \(U\)-collar obstruction

### Established

- Rechecked that RG II Eq. (1.34)'s first parameter makes RG I condition
  (iii) read \(|dU-1|<(1+\beta)\alpha_0\xi^2\) on the full complex \(U\),
  while membership remains existential over its complex gauge orbit.
- Proved YM-RG-018 at the identity physical pair. A four-link semisimple
  complex plaquette direction has holonomy \(e^{4tH}\). Its spectrum is
  unchanged by every \(SL(2,\mathbb C)\) gauge transformation, so a full raw
  operator-sup log ball can have radius at most
  \[
  \frac14\log\left(1+
  \frac{(1+\beta)\alpha_0\xi^2}{c_{\rm RG}}\right)=O(\xi^2).
  \]
- Converted the result to the relative coordinate
  \(U_A=e^{i\xi A}U\): its naive per-bond operator-sup radius is at most
  \(O(\xi)\). Thus neither radius can be uniform as \(\xi\downarrow0\).
- Isolated the only viable positive replacement currently justified: a
  shared split representative with strict smaller-domain margins and uniform
  Eq. (1.13) plus scaled-plaquette Lipschitz estimates in a stronger
  RG-scaled Banach norm. Under those unproved hypotheses, the p. 263
  inclusion and Banach-space Cauchy formula give the desired collar and
  \(D_U\)-activity bound.

### Not established

- No concrete RG-scaled \(U\) norm or uniform Eq. (1.13) BCH estimate.
- No common shifted representative atlas, physical \(U\)-chain pullback, or
  uniform chart coefficients.
- No connected marked expansion, large-field estimate, RG iteration,
  continuum construction, infrared estimate, or Yang--Mills mass gap.

### Next decision

Define the smallest scaled regularity norm that controls both RG I
Eq. (1.13) and \(\xi^{-2}\Delta(dU)\), or close the fixed-partition rooted
connected expansion first. The naive raw-radius route is now closed rather
than merely unaudited.
