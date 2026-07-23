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

## 2026-07-22 -- conditional forward multiscale cell-map bridge

### Established

- Corrected the metric bookkeeping to retain Propagators II's physical set
  \(\mathcal B\) and pull its metric back to a tagged cover through the
  tag-forgetting projection. The pullback is a pseudometric and inherits the
  source triangle inequality.
- Under the explicit cubical hypothesis \((\mathrm H_\rho)\), proved that the
  coordinatewise half-open ownership map obeys
  \[
  d_{\mathcal B}(\rho(z),\rho(z'))
  \le [d(L+2)+1]\operatorname {dist}_\eta(z,z').
  \]
  The interface route approaches the inner-owned surface through the outer
  collar, switches meshes on the surface, and takes its first coarse bond
  with open interior in the inner layer.
- Separated RG I's continuous contained-tree definition from the additional
  exact fine-bond lift \((\mathrm H_T)\). With its proximity error \(\tau\),
  the support/root halo premise \((\mathrm H_I)\), and mesh ratio \(b\),
  proved
  \[
  D_{\mathcal B}(q_p,Y)
  \le c_{\rm nn}
  [Mb\,d_{k,\sigma}(Y)+2dMb+2\tau+h+h_q].
  \]
- Combined the forward comparison with YM-RG-017's dual source convolution.
  Under common regulator-family margins, chart factors, kernel constants,
  and \(b\le b_*\), obtained the conditional all-layer auxiliary-\(J\)
  pullback with exponent budget
  \(a_*+\gamma c_{\rm nn}Mb_*\le a\).
- Ran two independent adversarial audits. They forced the on-surface switch,
  explicit same-layer bond admissibility, original-scale indexing, tagged
  pseudometric, exact tree-lift wording, and uniform-constant quantifiers;
  both latest-state re-audits passed.

### Not established

- Propagators II does not print \(\rho\), \((\mathrm H_\rho)\), or the
  constant \(d(L+2)+1\); the exact domain/bond geometry has not yet been
  shown to satisfy those premises uniformly.
- No uniform construction of the exact no-length-increase tree lift, output
  anchors, support halos, or mesh-ratio bound for the full shifted family.
- No physical nonlinear \(U\) pullback, one-fixed-partition connected marked
  sum, large-field estimate, RG iteration, continuum construction, infrared
  estimate, or Yang--Mills mass gap.

### Next decision

Either discharge \((\mathrm H_\rho)\), \((\mathrm H_T)\), and
\((\mathrm H_I)\) from the exact finite-regulator geometry, or keep them as
an interface specification and move to the one-fixed-partition rooted
connected mark. In parallel, the scaled \(U\)-chart theorem from Note 0018
remains the missing second chain-rule summand.

## 2026-07-22 -- one-mark Ursell identity on a fixed gas

### Established

- Rechecked RG II Eqs. (2.1)--(2.13). Equation (2.11) is an ordered
  hard-core gas with one exterior \(1/n!\); full wall contact is
  incompatible. Equations (2.12)--(2.13) use the connected-graph coefficient
  without an internal factorial and group clusters by their union.
- Proved YM-RG-020 for one fixed finite hard-core gas. Differentiating its
  logarithm produces one distinguished mark and \(1/n!\) for \(n\) unmarked
  occurrences. Repeated labels are required in the log even though they
  vanish from the hard-core partition function.
- Separated the exact finite numerator/denominator identity from the formal
  or absolutely convergent Ursell series. No convergence at arbitrary
  complex activities is inferred merely from finite volume and a nonzero
  partition function.
- Under an explicit canonical pinned Kotecky--Preiss condition,
  post-polymerization marked norm, and hull-weight crosswalk, proved the
  conditional rooted output bound
  \[
  \sup_p\sum_{R\supset Q_p}e^{a_{\rm out}d_\pi(R)}
  |\mathcal C_{p,\pi}^\bullet(R)|
  \le e^{A_0}\mathcal B_\bullet,
  \qquad a_{\rm out}+\epsilon\le a_\bullet.
  \]
- Version-pinned the pinned estimate to Fernandez--Procacci
  arXiv:math-ph/0605041v2 Eqs. (2.7), (2.14), and (2.15), with the exact
  \(\rho=|K|e^c\), \(a=A\) notation map; visually checked the relevant primary
  PDF pages.
- Proved by finite counterexample that bare shifted activities cannot in
  general be mixed before the connected map. Absent a proved common-gas
  embedding, branches must be completed on their own partitions before the
  normalized \(1/n_p\) average.
- Rechecked the unmarked source ledger:
  \((1-8\delta)(L/2)\kappa\) in Eq. (2.38) and
  \((1-10\delta)(L/2)\kappa\) in Eq. (2.41). The source does not print a
  marked analogue.
- Added executable coefficient checks for the one-species reciprocal,
  repeated labels, compatible-spectator cancellation, and the three-vertex
  star. Three independent AI audits passed after distinguishing the
  post-polymerization positive mark from Notes 0012--0014's pre-Section-2
  activity.

### Not established

- No construction of the post-conditioning marked activity through RG II
  Eqs. (2.2)--(2.10), and no identification of it with the earlier
  \(W_{k,p}^\sigma\).
- No common source disk, marked Lemma-3 norm, absolute KP convergence,
  wall-contact hull/\(d_k\) crosswalk, or positive numerical output exponent.
- No branchwise shifted source synchronization or common-gas embedding.
- No physical nonlinear \(U\) pullback, realization of Note 0019's premises,
  large-field estimate, RG iteration, continuum construction, infrared
  estimate, or Yang--Mills mass gap.

### Next decision

Carry the unique mark through Eqs. (2.2)--(2.10) on one fixed partition and
define the resulting \(W_p^{\rm post}\) before attempting a norm. Then prove
the wall-contact hull inequality and a marked analogue of the Lemma-3/KP
budget. Only after that fixed branch closes should the complete construction
be repeated uniformly for each admissible shift and averaged.

## 2026-07-22 -- one marked component through the RG-II Section-2 map

### Established

- Proved YM-RG-021 at one finite regulator and on one fixed compatible
  partition. The localized source factor is inserted before RG II Eq. (2.2)
  with the marked seed
  \(Y_0^\bullet=A\cup\bigcup_{Y\in D}Y\), including
  \(D=\varnothing\) and with no Mayer-subset factorial.
- Separated globally source-independent objects from seed-derived geometry.
  The global cutoff, Gaussian law, quadratic operator, fixed background/chart,
  partition, and unmarked potentials are not differentiated, but every
  marked cutoff split, \(P\)-sum, \(Z_0\), conditioned restriction,
  \(Z_0'\), weakening family, and admissible output is reconstructed using
  \(A\) in the seed.
- Defined the exact decorated linear image
  \[
  W_p^{\rm post}(C)
  =\sum_{A\supset Q_p}\mathcal T_{\pi;C,A}[W_{k,p}(A)]
  =-\partial_tH_{p,t}(C)|_{t=0}.
  \]
  Equation (2.8)'s weakening derivatives act on the entire transformed
  integrand and may hit the mark; those contributions are included rather
  than treating the mark as an untouched decoration.
- Proved the unique marked-component factorization and exact finite hard-core
  numerator. In a disconnected output, only the component containing the
  retained root carries \(W_p^{\rm post}\); every other component carries
  ordinary \(H\).
- Isolated a conditional marked Lemma-3 interface. Direct marked-integrand
  domination plus common conditioned domains and marked gluing would give the
  pointwise \((1-8\delta)(L/2)\kappa\) exponent. A rooted \(\ell^1\) norm
  must additionally pay output-animal entropy; one explicit delta-unit spend
  leaves \((1-9\delta)(L/2)\kappa\).
- Added exact-arithmetic tests for unique-component product differentiation,
  absence of leakage onto non-root components, the hard-core one-mark
  numerator, and the extra derivative created by a source-dependent auxiliary
  factor.

### Not established

- No direct marked conditioning/weakening majorant, common transformed
  complex domain, marked gluing theorem, output-animal constant, or actual
  post-polymerization norm for the Yang--Mills activities.
- No pinned Kotecky--Preiss verification, wall-contact hull crosswalk, common
  source disk, absolute convergence, or branchwise shifted synchronization.
- No physical nonlinear \(U\) pullback, discharge of YM-RG-019's premises,
  marginal projection, large-field estimate, RG iteration, continuum
  construction, axioms, infrared decay, or Yang--Mills mass gap.

### Next decision

Prove or falsify the direct marked-domination hypothesis at RG II Eq. (2.8),
where weakening derivatives can hit the transformed mark. In parallel, prove
the marked tree-gluing and wall-contact hull inequalities and pay the output
animal entropy explicitly. Only after that fixed-partition norm closes should
the construction be repeated uniformly on every admitted shifted branch.

## 2026-07-22 -- whole-integrand Cauchy reduction for the marked term

### Established

- Proved YM-RG-022 for one finite active Eq. (2.8) weakening set. The
  integrated mixed derivative is exactly the alternating endpoint difference
  and has the iterated contour representation
  \[
  \prod_{e\in S}(E_e^1-E_e^0)F
  =\frac1{(2\pi i)^{|S|}}
  \oint F(\zeta)
  \prod_{e\in S}\frac{d\zeta_e}{\zeta_e(\zeta_e-1)}.
  \]
- Under common \(L^1\)-holomorphy and one joint majorant, applying that
  contour to the complete marked integrand captures every weakening
  derivative that hits the mark or ordinary decorations. The price is exactly
  \(\prod_e(R_e-1)^{-1}\), with no additional \(2^{|S|}\),
  decoration-allocation factor, or factorial.
- If the marked term shares the source radius \(R=e^{\kappa_1}\), this is the
  ordinary weakening factor. A smaller marked radius incurs the explicit
  relative penalty
  \(((e^{\kappa_1}-1)/(R_*-1))^{|S|}\), which cannot be hidden as a fixed
  tree-exponent loss without a proved \(|S|\)-to-metric inequality.
- Reduced the conditional marked activity estimate to a positive
  seed-dependent kernel \(K_\pi(C,A)\). The remaining analytic input is one
  joint conditioned-contour relative Gaussian-moment envelope for the
  transformed mark and the ordinary Eq. (2.14) majorant.
- Corrected Note 0021's conditional loss bookkeeping. The marked branch,
  including every root and joint-moment loss, and the ordinary \(D/Y_0\)
  branch run in parallel; their weaker exponent is glued before the four
  later source losses. A total pre-gluing marked cost of at most two
  delta-units therefore still ends at
  \((1-8\delta)(L/2)\kappa\).
- Added exact-arithmetic tests for the mixed FTC identity, the product-rule
  allocation trap, failure of real-cube control, failure of multiplying
  separate integrated majorants, and loss outside a smaller analytic disk.

### Not established

- No proof that the actual conditioned, standardized plaquette argument stays
  in the Eq. (1.34) marked domain on the full complex weakening contour.
- No joint marked/unmarked Gaussian envelope, positive-kernel decay, marked
  gluing, output-animal constant, pinned Kotecky--Preiss condition, or hull
  crosswalk.
- No common source disk, absolute convergence, branchwise shifted
  synchronization, physical \(U/J\) pullback, large-field estimate, RG
  iteration, continuum construction, axioms, infrared decay, or Yang--Mills
  mass gap.

### Next decision

Audit the full conditioned Eq. (2.14) formula from a clean page image and
either prove the joint transformed-mark Gaussian envelope or record a sharp
counterexample for the actual argument. In parallel, close the fixed-output
wall-contact hull and animal geometry so that a successful kernel estimate
can enter the pinned connected expansion without another hidden loss.

## 2026-07-22 -- fixed-cubical hull, animal entropy, and pinned KP

### Established

- Proved YM-RG-023 in a declared standard cubical support model. For a
  connected occurrence tuple with cube-or-complete-wall incompatibility, its
  literal support union is the unique least admitted hull and
  \[
  d(R)\le d(A)+\sum_i d(X_i)+\sqrt{D+3}\,n.
  \]
  In four dimensions the safe contact charge is \(\sqrt7\). Three consecutive
  closed cells show that no universal zero contact charge can work.
- Proved the sharper contained-tree cube-count estimate
  \[
  N(Y)\le2^D\bigl(\lfloor2d(Y)\rfloor+1\bigr),
  \]
  and the rooted face-connected animal count \((2D)^{2m}\) for \(m\) added
  cubes.
- Grouped the count exactly into distance shells. With
  \(B=2^D\), \(q=2D\), and
  \(S_D=\sum_{j=0}^{B-1}q^{2j}\),
  \[
  C_{\rm an}(\eta)
  \le\frac{S_D}{1-q^{2B}e^{-\eta/2}}
  \]
  whenever \(\eta>2^{D+2}\log(2D)\). The four-dimensional sufficient
  threshold is \(64\log8\), not the earlier input cube-count margin
  \(\log64\).
- For one ordinary species per support, derived the explicit sufficient
  pinned-KP condition
  \[
  (2D+1)h e^{\alpha2^D+a\sqrt{D+3}}
  C_{\rm an}(\beta-a-\alpha2^{D+1})\le\alpha.
  \]
  The affine size split gives Note 0020's exact parameters
  \(A_0=\alpha2^D\) and \(\epsilon=\alpha2^{D+1}\).
- Combined the geometry with Note 0020's hull weight. In four dimensions,
  writing \(\lambda=(L/2)\kappa\), \(\Delta=\delta\lambda\), and taking the
  intended exponents \((1-8\delta)\lambda\),
  \((1-9\delta)\lambda\), and \((1-10\delta)\lambda\), a sufficient system
  is \(\Delta>64\log8\), \(0<32\alpha\le\Delta\), and the displayed strict
  KP smallness inequality.
- Added executable connector, seam, counterexample, small-animal, distance
  shell, threshold, and geometric-series tests. Three independent AI audits
  separately checked the hull connector, animal count, and KP constants;
  no independent human review was performed.

### Not established

- No immutable primary-source identification yet shows that the actual
  RG-II output class, special domains, periodic seams, \(d_{k+1}\) metric,
  literal-union closure, and decoration aggregation instantiate the declared
  model.
- The source's ordinary amplitude has not been identified with the \(h\) in
  Note 0023's model or verified against its strict parameter window; the
  required marked norm is also unproved.
- No joint transformed-mark Gaussian envelope, positive marked-kernel decay,
  marked gluing, common source disk, absolute convergence, or branchwise
  shifted synchronization.
- No physical \(U/J\) pullback, marginal projection, large-field estimate,
  RG iteration, continuum construction, axioms, infrared decay, or
  Yang--Mills mass gap.

### Next decision

Audit the exact source definition of the RG-II output polymers and
\(d_{k+1}\) from immutable page images. If it matches the standard-cube
model, verify the actual decoration count and the numerical ordinary
smallness inequality. In parallel, return to the decisive analytic gate:
prove or falsify the joint conditioned-contour Gaussian envelope and the
positive marked \(A\)-to-\(C\) kernel decay.

## 2026-07-22 -- final ordinary gas instantiation and explicit KP window

### Established

- Proved YM-RG-024 from immutable Project Euclid copies of RG I and RG II.
  The final connected ordinary gas after RG II Eq. (2.10) instantiates Note
  0023's quotient cubical model: \(\mathcal D_{k+1}\) is the full class of
  finite face-connected closed-cube supports, \(d_{k+1}\) is the normalized
  shortest contained-tree metric, incompatibility is exactly shared-cube or
  complete-wall contact, and Eq. (2.13) groups nonzero connected terms by
  their literal support union.
- Verified that the internal \(D,P,Z_0\) histories are summed into one
  ordinary analytic activity \(H(Z)\) per connected final support. The
  identification starts only after Eq. (2.10); it does not collapse the
  mixed-scale intermediate \(Y_0,Z_0,\widetilde Z_0,Z'_0,X_0\) objects into
  final polymers.
- Direct page-image inspection confirmed the \(8\delta\), \(9\delta\),
  \(10\delta\), and \(L/2\) factors in RG II Eqs. (2.38)--(2.41). The source
  prints the pointwise ordinary bound
  \[
  |H(Z)|\le C_3\varepsilon _1
  e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)}.
  \]
- Refined the source's displayed qualitative hierarchy explicitly. With
  \(\Delta=(L-2)\kappa/20\), choose
  \(\kappa>1280\log8/(L-2)\),
  \(\alpha=\Delta/64\), and then
  \[
  0<\varepsilon _1\le
  \frac{\Delta}
  {576C_3e^{\Delta/4+\sqrt7\kappa}
   C_{\rm an}^{\rm geom}(3\Delta/2)}.
  \]
  This makes Note 0023's ordinary D=4 pinned-KP inequality hold. The
  criterion is a repository sufficient refinement, not a formula printed by
  Balaban. Full source compatibility remains conditional on downward
  monotonicity of restrictions imported but not enumerated in RG I/II.
- Added exact-arithmetic and logarithmic regression tests for the source
  exponent ledger, animal threshold, and activity ceiling. Three independent
  AI audits were requested; no independent human review was performed.

### Not established

- No marked analogue of Lemma 3, joint transformed-mark Gaussian envelope,
  positive marked-kernel decay, marked gluing estimate, or decorated marked
  norm.
- No common external-source disk, differentiated absolute convergence, or
  branchwise shifted synchronization.
- No physical scaled \(U/J\) pullback, marginal projection, large-field
  estimate, RG iteration, continuum construction, axioms, infrared decay, or
  Yang--Mills mass gap.

### Next decision

Return to the first genuinely analytic marked gate. Transcribe the complete
RG II Eq. (2.14) conditioned integrand from the clean page image and either
prove a common transformed complex domain plus a relative Gaussian-moment
bound for the actual plaquette mark, or isolate the first precise obstruction.

## 2026-07-23 -- conditioned-mark routing correction

This entry explicitly supersedes the transformed-mark interpretation in the
2026-07-22 fixed-partition and whole-integrand entries above. Those entries
are retained as historical records of the route that triggered the source
audit.

### Established

- Direct inspection of the immutable RG II pages for Eqs. (2.3), (2.5),
  (2.6), (2.8), and (2.14) shows that conditioning leaves a localized factor
  as \(F(Z_0,B)\), on the conditional interior field \(B\). The change
  \(B'=(C^{(k)})^{1/2}X\) standardizes only the exterior variable.
- The second-stage weakening variables enter
  \(C^{(k)}(Z_0,\sigma)\), \((C^{(k)})^{1/2}(\sigma)\),
  \(\Delta_k(\sigma)\), and \(\Gamma_k(\sigma)\). The cutoffs,
  \(V_k(Y,B)\), and an inserted already-localized \(W_{k,p}(A,B)\) are
  \(\sigma\)-independent.
- With
  \(Y_0^\bullet=A\cup\bigcup_{Y\in D}Y\), the factor
  \(\chi_{k,Y_0^\bullet}\) forces
  \(g_k\|B\|_A<\varepsilon _1\). Note 0012's Eq. (1.34) norm therefore gives
  the pointwise marked bound on the entire fixed-term support.
- Proved YM-RG-025:
  \[
  \sup_{(\sigma,\tau)\in\mathcal C_\gamma}
  \int|\mathcal I_\gamma^\bullet(\sigma,\tau;B,X)|
  \,d\lambda_\gamma^\sigma(B,X)
  \le b_{p,A}q_\gamma^{(0)}.
  \]
  Here \(d\lambda_\gamma^\sigma\) is the fixed positive Gaussian comparison
  base and all determinant, cutoff, density, and ordinary factors remain in
  the integrand.
  The marked second-stage radius is unchanged,
  \(q_\gamma^\bullet=q_\gamma^{(0)}\),
  \(C_\bullet=1\), and \(r_{\rm mom}=0\).
- Corrected the Note-0021 ledger: a remaining geometric pre-gluing cost
  \(r_{\rm root}+r_{\rm other}\le2\) still reaches the conditional
  \((1-8\delta)(L/2)\kappa\) endpoint. The stale \(r\le1\) restriction was
  unnecessarily strong.
- Two independent AI source audits reached the same routing conclusion.
  No independent human review was performed.

### Correction impact

- The earlier unbounded-\(X\), common-transformed-domain, and relative
  Gaussian-moment obstruction was an artifact of the wrong argument map. It
  is retracted for the actual source-faithful localized plaquette mark.
- The general Note-0022 Cauchy and counterexample lemmas remain valid for a
  genuinely weakening-dependent or shifted mark. They are no longer the
  missing interface for this mark.
- The fixed-term result does not differentiate Balaban's unmarked Lemma-3
  bound. It inserts the mark into the finite conditioned formula and takes a
  pointwise cutoff bound before using the source's positive majorant.

### Not established

- No positive marked-seed \(A\)-to-output kernel decay through the
  \(D,P,Z_0,\widetilde Z'_0,Z\) resummations.
- No marked tree-gluing or \(k\)-to-\(k+1\) scale-conversion theorem, final
  decorated marked norm, common external-source disk, differentiated
  absolute convergence, or shifted synchronization.
- No physical scaled \(U/J\) pullback, marginal projection, large-field
  estimate, RG iteration, continuum construction, axioms, infrared decay,
  or Yang--Mills mass gap.

### Next decision

Transcribe and adapt RG II Eqs. (2.26)--(2.32). Combine the rooted input
weight \(b_{p,A}\) with the ordinary \(D\)-weights for the enlarged seed,
then prove or sharply delimit the first marked tree-gluing and scale
conversion inequality.

## 2026-07-23 -- fixed-partition marked-seed resummation

### Established

- Audited the immutable RG-II pp. 17--20 ledger for Eqs. (2.26)--(2.38).
  The source is unmarked; every coloured statement below is a repository
  corollary.
- Proved the exact finite-family collision identity for
  \(D\mapsto D\cup\{A\}\). Because Eq. (2.1) has no \(1/|D|!\), the two
  possible preimages cost a safe factor \(2\), yielding
  \[
  \varepsilon_\bullet
  =2\alpha _6^{-1}\mathcal B_\bullet
  \]
  at the \((1-4\delta)\kappa\) stage.
- Adapted the printed \(P,Y_0,Z_0\) positive estimates. The unique root has
  no empty-component case, the ordinary components retain
  \(\varepsilon _2\), and the marked coefficient survives to the
  \((1-5\delta)\kappa\) analogue of Eq. (2.35).
- Proved the whole scale step by coefficientwise colour erasure. For the
  finite positive majorant,
  \[
  \mathscr S^\bullet_{x,y}(Z)
  \le y\partial_x\mathscr S_x(Z)
  \le\frac{y}{2x}\mathscr S_{2x}(Z).
  \]
  Imposing every ordinary scale-stage smallness condition at
  \(2\varepsilon _2\) gives
  \[
  |W_p^{\rm post}(Z)|
  \le4K_{\rm lift}\alpha _6^{-1}\mathcal B_\bullet
  e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)}.
  \]
- Combined that pointwise estimate with the already proved animal,
  final-gas, and pinned-KP interfaces. The aggregated fixed-partition marked
  norm has exponent \((1-9\delta)(L/2)\kappa\), and the connected first
  derivative at \(t=0\) converges at output exponent \(\kappa\), under the
  separately imposed ordinary ceiling
  \(0<\varepsilon _1\le\varepsilon_{\rm KP}\).
- Corrected a source-metric overidentification found by the proof red-team.
  The auxiliary degenerate tree size satisfies
  \(d_{\rm aux}\le d_j\), while a direct contained-tree construction proves
  the same \(\sqrt7\) connector for \(d_j\). Note 0023's monotone-metric
  extension transfers the animal and KP constants without metric equality.
  Note 0013 now uses \(d_k(Y)\le m(Y)+1\), costing one overall \(e^a\)
  factor and avoiding an unsupported singleton convention.
- Added exact algebraic regressions and requested three independent AI
  audits. They found one missing rooted summation qualifier and the two
  final-stage premises just described; all were repaired. No fatal defect
  remained in their audited scope, and no independent human review was
  performed.

### Not established

- No nonvanishing common external-source disk or analytic control at
  \(t\ne0\).
- No branchwise shifted-partition synchronization, unit-translation
  covariance, or physical \(U/J\) pullback.
- No proof that every imported but unenumerated source restriction is
  preserved under the doubled-amplitude refinement.
- No derivation of the ordinary KP ceiling from the doubled-amplitude
  refinement; it remains a separate explicit smallness premise.
- No intrinsic/raw comparison, large-field estimate, RG iteration,
  continuum or infinite-volume construction, axioms, infrared decay, or
  Yang--Mills mass gap.

### Next decision

Use the fixed-partition theorem as a completed local input. Attack shifted
branch synchronization next: formulate each shifted gas on its own
\(\pi^\sigma\), prove uniform constants and a common \(t=0\) derivative
representation, and only then average the already connected branch
coefficients. In parallel, keep the physical \(U/J\) pullbacks and Note
0019's geometry premises as separate gates.

## 2026-07-23 -- nested shifted first-jet synchronization

### Established

- Audited the former \(H_{\rm sync}\) gate with three independent AI
  red-teams. Covariance of the bare mark was rejected as insufficient: a
  two-branch toy gas can be exactly equivariant while its denominators and
  logarithmic derivatives differ.
- Resolved the two-scale representative ambiguity. With \(LM\mid N\), lift
  every admitted input shift modulo \(M\) to all
  \(s\in(L\mathbb Z/LM\mathbb Z)^4\), transport the nested \(M\)- and
  \(LM\)-cubulations together, and retain the actual count
  \(\widetilde n_p=L^4n_p\).
- Restricted every fixed-\((U,J)\) projective comparison and shifted sum to
  the explicitly assumed nonempty common intersection of the finitely many
  transported branch domains, containing the physical real source-free
  point.
- Proved the shifted unmarked Lemma-2 identity by applying the standard
  identity to transported external fields and orthogonal fluctuation
  coordinates, then relabelling. The global cutoff and Gaussian measure are
  unchanged laws; the branch-conditioned covariances and determinants are
  exact coordinates obtained by inclusion--exclusion and Schur-complement
  conditioning.
- Ran the complete Section-2 construction over
  \(\mathbb C[\epsilon]/(\epsilon^2)\). Every branch reconstructs
  \[
  \mathscr I_p^{\mathbb D}
  =S_s(\mathcal Z_s-\epsilon\mathcal N_{p,s}),
  \]
  with \(S_s\ne0\) independent of \(\epsilon\). Hence every completed branch
  has the same projective ratio
  \(\mathcal N_{p,s}/\mathcal Z_s=-\partial_t\log\mathscr I_p(0)\).
- Transported YM-RG-026's norm uniformly and divided only after each branch
  connected map. The normalized lifted family has no orbit factor and obeys
  \[
  \sup_p
  \sum_{s\in\widetilde{\mathcal A}_{M,L}(p)}
  \sum_{R\supset\widehat Q_{p,s}}
  e^{\kappa d_{k+1,s}(R)}
  |\widehat{\mathcal C}_p^+(s,R)|
  \le
  e^{16\alpha}C_{\rm sec}C_{\rm an}^{\rm geom}(\Delta)\mathcal B_d.
  \]
- Corrected the open-disk wording. The exact selected-coordinate scalar ratio
  already has the Note-0007/0010 disk; for one plaquette its radius is
  \(\log2/4\). No source-dependent polymer activities or uniform KP theorem
  at nonzero source is inferred from scalar zero-freeness.
- Added exact-arithmetic/geometric regressions and an immutable-source
  transport audit. No independent human review was performed.

### Not established

- No source-dependent polymer-activity or connected-cluster theorem for
  \(t\ne0\).
- No unit-translation covariance moving the next coarse lattice.
- No uniform scaled nonlinear \(U\) pullback or discharge of Note 0019's
  all-layer \(J\)-geometry and common-chart premises.
- No intrinsic/unrestricted raw-law comparison, marginal projection,
  large-field estimate, RG iteration, continuum or infinite-volume
  construction, axioms, infrared decay, or Yang--Mills mass gap.

### Next decision

Use the synchronized independent-variable first jet as a completed local
input. Attack the physical pullback next: construct a concrete RG-scaled
nonlinear \(U\) collar and discharge the interface, tree-lift, support, mesh,
and uniform-chart hypotheses in Note 0019. Keep a nonzero-\(t\) polymer disk
as a separate analytic gate.
