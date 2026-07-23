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
one-fixed-partition cluster compatibility remained open at that stage. Note
0015 subsequently supplied conditional fixed-chart physical composition,
exact chain rules, and preservation of the zeroth-order value norm. Note 0016
then identified the exact auxiliary field and supplied fixed-regulator
conditional independent-variable derivative norms. Note 0021 later supplied
the exact fixed-partition marked algebra. The uniform physical coarse-field
derivative norm, marked activity norm, shifted synchronization, and convergent
marked expectation remain open.

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

## 2026-07-22 — Proposition 9 Eq. (190) component audit

The primary scan of the [variational/background-field
article](https://doi.org/10.1007/BF01229381) ([Project Euclid
PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-102/issue-2/The-variational-problem-and-background-fields-in-renormalization-group-method/cmp/1104114383.pdf)),
CMP 102, pp. 307--308, was
inspected at Eqs. (182) and (190). With \(B=(1/i)\log V'\), Eq. (182)
differentiates the Landau-gauge relative minimizer \(\mathcal H(B)\) with
respect to a coarse bond coordinate. For \(x\in\Delta(y)\),
\(y\in\Lambda_j\), and
\(y'\in\Lambda_{j'}\), Eq. (190) simultaneously bounds that component kernel,
its spatial gradient, a \(\zeta\)-weighted Hoelder gradient, and its two listed
covariant second-derivative images.

The corresponding \(L^j\eta\) factors are \(-1\), \(-2\),
\(-2-\beta\) with multiplier \(\|\zeta\|_\beta^\xi+|\zeta|\), \(-3\), and
\(-3\). Every row also carries
\((L^{j'}\eta)^{-d}\exp[-\delta_0d(y,y')/8]\). The \(\zeta\)-weighted row
requires
\(\operatorname{supp}\zeta\subset\widetilde\Delta(y)\). The
\(\delta_0/8\) exponent must not be copied from Eq. (189), which has
\(\delta_0/4\).

This closes the literal component/scale transcription in Note 0004. By itself
it does not provide the physical auxiliary-\(J\) differential,
chart/differential factors, \(d_k\)-metric comparison, activity Cauchy margins,
convolution or animal entropy slack, one-fixed-partition compatibility, or a
connected marked expectation. Note 0015 uses none of these bounds for its
zeroth-order norm; Note 0016 supplies the exact \(J\)-reduction and only
fixed-regulator conditional Cauchy bounds.

## 2026-07-22 — auxiliary J, analytic tubes, and metric audit

The primary scan of [RG
I](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf)
was inspected at Eqs. (1.8), (1.10), (1.15)--(1.16), (3.1), and
(3.10)--(3.11). Equation (1.8) defines

\[
\mathscr J_\xi(U)=D_U^{\xi *}\xi^{-2}\pi\operatorname{im}(dU),
\qquad \operatorname{im}X=(X-X^{-1})/(2i),
\]

and Eqs. (1.15)--(1.16) evaluate it on the minimizing background. The map is
finite-stencil and holomorphic in the selected complex link chart. Equation
(1.10) specifies the adjoint transformation convention for the \((U,J)\)
pair, and substitution in the displayed definition gives covariance in that
convention. Differentiating Eq. (3.11) retains both the leading
\(D_U^{\xi *}D_U^\xi A\) term and the derivative at zero of the local remainder
\(F(U,A)\). The latter must not be dropped.

[RG II](https://doi.org/10.1007/BF01239022) Eq. (1.34) was rechecked for a
Cauchy collar. The activity domain enlarges its first two regular-field
parameters by \(1+\beta\), but does not print a full additive Banach-ball
radius in representative \(U\) coordinates, and its third parameter is not
enlarged. Thus it does not by itself give a uniform \(J\)-radius. At fixed
regulator, compact containment in explicitly chosen open representative
charts does give positive, generally nonuniform full complex tube radii. This
is the scope used in Note 0016.

Finally, [*Propagators and renormalization transformations for lattice gauge
theories II*](https://projecteuclid.org/download/pdf_1/euclid.cmp/1103941783),
CMP 96, pp. 230--234, was inspected at Eqs. (2.45)--(2.48), (2.54), and
(2.59)--(2.63). These define the multiscale contour distance
\(d_{\mathcal B}\), prove its triangle inequality, and give an exponential
summation lemma under the paper's strengthened separation condition. This is
not the rooted polymer metric \(d_{k,\sigma}\). A uniform cell/scale map,
layer-interface comparison, physical chain-rule convolution, and explicit
entropy budget remain open.

## 2026-07-22 — strict \(J\) interior and metric-density audit

[RG I](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf)
pp. 262--263 was rechecked at Eqs. (1.11)--(1.16) and the paragraph following
the definition of \(\mathcal U_j^c\). Condition (iii), Eq. (1.14), contains
the independent direct bound \(\lVert J\rVert_\infty<\gamma_0\), normally
with \(\gamma_0=\alpha_0\). Condition (iv) tests
\((U_n(M^j(U)),J_n(M^j(U)))\), where \(J_n\) is derived from \(U\) by
Eq. (1.8); it does not depend on the independent input \(J\).

The next paragraph chooses smaller constants
\(\alpha_0'<\alpha_0\), \(\alpha_1'<\alpha_1\), states that Proposition 9
makes condition (iv) hold for sufficiently small \(\alpha_0'\), and then
specializes to physical auxiliary fields satisfying
\(\lVert J\rVert_\infty<\alpha_0'\). RG I declares the outer constants
independent of \(X,j\), and Theorem 3 chooses the hierarchy for fixed \(M\).
Thus a frozen strict representative hierarchy gives the formal direct
\(J\)-margin \(\alpha_0-\alpha_0'\). The source does not turn this into a
nonlinear \(U\)-chart radius.

The Eq. (190) audit was then combined with [Propagators
II](https://doi.org/10.1007/BF01240221) Lemma 2.1. With
\(s_j=L^j\eta\), the functional derivative acts with source measure
\(s_{j'}^d\), which cancels Eq. (190)'s \(s_{j'}^{-d}\) target-density factor.
For \(0\le\gamma<\delta_0/8\), the remaining exponent is
\(\alpha_\gamma\delta_0\), where
\(\alpha_\gamma=1/8-\gamma/\delta_0\). This gives the dual weighted source
row sum used in Note 0017.

On a matched homogeneous layer, Eq. (2.46) measures lattice length in
\(s_r\) units while RG I's \(d_k\) measures the same contained-tree length
in \(M s_r\) units. The tree metrics therefore differ by \(M\), up to bounded
endpoint paths. Across layers, a segment \(r-r_0\) levels coarser has
fixed-scale/multiscale ratio \(L^{r-r_0}/M\), so this example rules out only
the reverse comparison \(d_k\lesssim d_{\mathcal B}\). A later visual and
text-layer recheck corrected an earlier description of Eq. (2.57): it is a
lower bound on actual travel between distinct layer surfaces used in the
Eq. (2.58) summation, not an additive interface toll in the definition of
\(d_{\mathcal B}\). The forward comparison
\(d_{\mathcal B}\lesssim d_k+1\) therefore remains viable and reduces to an
explicit local cell-map, support-halo, and root-anchor lemma; it is not
refuted by shifted-grid misalignment.

## 2026-07-22 -- full complex \(U\)-collar audit

[RG I](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf)
Eqs. (1.10)--(1.16) and printed pp. 262--263 were rechecked together with
[RG II](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf)
Eqs. (1.34)--(1.35. The outer activity domain requires the full complex
field to satisfy
\(|dU-1|<(1+\beta)\alpha_0\xi^2\) in some complex gauge representative.
The union-of-orbits wording does not create a raw collar: plaquette holonomy
is changed only by similarity, so its spectrum is invariant.

At the flat pair, four independent complex plaquette logs of norm \(t\) can
be chosen so that the holonomy is \(e^{4tH}\). This gives the exact
operator-norm condition-(iii) threshold
\(\frac14\log(1+(1+\beta)\alpha_0\xi^2)\), with an explicit
finite-dimensional norm-comparison constant for the retained paper norm.
Consequently the raw log radius is \(O(\xi^2)\), and the radius in
\(U_A=e^{i\xi A}U\) is \(O(\xi)\). RG I's p. 263 smaller-domain paragraph
still gives a conditional route in a norm controlling Eq. (1.13) and the
scaled plaquette increment, but it supplies neither that norm nor its
uniform chart constants.

## 2026-07-22 -- forward multiscale cell-map audit

[Propagators
II](https://projecteuclid.org/download/pdf_1/euclid.cmp/1103941783)
Eqs. (2.45)--(2.54) were rechecked against the forward direction isolated
above. Equation (2.45) gives the physical union \(\mathcal B\), Eq. (2.46)
defines the layer-normalized admissible-contour metric, Eq. (2.47) decomposes
an already admissible contour, Eq. (2.53) identifies \(\Delta(y)=B^j(y)\),
and Eq. (2.54) gives the triangle inequality. These equations do not define
a seam-aware fine-site ownership map or prove a nearest-neighbor interface
route.

The source-compatible candidate used in Note 0019 approaches an inner-owned
surface through an outer collar, touches it only at a common coarse-grid
endpoint, switches meshes there, and takes the first coarse bond with open
interior in the inner layer. Under that route and the other named cubical
premises, the local cost is \(d+dL+1+d=d(L+2)+1\). This numerical lemma is
repository bookkeeping, not a constant printed in the paper.

[RG I](https://doi.org/10.1007/BF01215223) p. 257 defines \(d_k\) through a
continuous contained tree. It does not make that minimizer an identical
finest-bond tree. Note 0019 therefore retains an exact no-length-increase
discrete lift and a proximity error as separate hypotheses, along with
bounded site/bond/plaquette support anchors and mesh ratio. The resulting
all-layer auxiliary-\(J\) pullback is a proved implication from those
premises, not evidence that the primary sources establish them uniformly.

## 2026-07-22 -- fixed-gas one-mark cluster audit

[RG II Cluster
Expansions](https://doi.org/10.1007/BF01239022) Eqs. (2.1)--(2.13), Lemma 3
Eq. (2.38), and Eq. (2.41) were rechecked at formula level. Equation (2.11)
uses an ordered hard-core gas with one exterior \(1/n!\); sharing a full cube
wall is incompatible. Equations (2.12)--(2.13) use the unnormalized connected
graph coefficient and group by the union of the tuple.

Differentiating the fixed-gas logarithm selects one distinguished slot, so an
\(r\)-vertex marked term has \(1/(r-1)!\), not \(1/r!\) and not both
\(1/(r-1)!\) and a separate slot sum. Repeated polymer labels remain necessary
in the logarithm even though reflexive incompatibility removes them from the
partition function. Note 0020 records this exact algebra and a conditional
pinned Kotecky--Preiss consequence.

That pinned consequence was version-pinned to Fernandez--Procacci,
[*Cluster expansion for abstract polymer models. New bounds from an old
approach*](https://arxiv.org/abs/math-ph/0605041v2), version 2. Equation
(2.7) is exactly the positive pinned Ursell series, Eq. (2.15) is the
Kotecky--Preiss condition after
\(\rho(X)=|K(X)|e^{c(X)}\) and \(a=A\), and Eqs. (2.14)--(2.15) give
\(\Pi_Y(\rho)\le e^{A(Y)}\). Pages 3--4 of the primary PDF were rendered and
visually checked. The publication DOI is
[10.1007/s00220-007-0279-2](https://doi.org/10.1007/s00220-007-0279-2);
the original Kotecky--Preiss article is
[10.1007/BF01211762](https://doi.org/10.1007/BF01211762).

The source decay ledger is unmarked:
\[
|H(Z)|\le C_3\varepsilon_1
e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)}
\]
and then
\[
|E^{(k+1)}(X)|\le O(1)C_3\varepsilon_1
e^{-(1-10\delta)(L/2)\kappa d_{k+1}(X)}.
\]
The induction chooses \((1-10\delta)L/2=1\). The primary text layer corrupts
some digits and fractions; the surrounding primary equations and an
independent clean transcription agree, but an immutable page-image audit is
still open. RG II prints no marked analogue. Note 0021 subsequently carries
the plaquette mark through the finite fixed-partition algebra. Proving its
actual norm and hull crosswalk and synchronizing each shifted gas remain open.

## 2026-07-22 -- fixed-partition marked Section-2 audit

[RG II Cluster
Expansions](https://doi.org/10.1007/BF01239022) Eqs. (2.1)--(2.10) were
rechecked specifically for the operations encountered by one distinguished
localized source mark. Equation (2.1) uses an unordered Mayer subset with no
factorial. Equation (2.2)'s unmarked seed must be replaced by
\(A\cup\bigcup_{Y\in D}Y\) before Eq. (2.3)'s cutoff split and exterior-bond
inclusion--exclusion. The \((-1)^{|P|}\) sign remains unmarked.

The global cutoff, Gaussian law, quadratic operator, fixed background/chart,
partition, and unmarked potentials are source-parameter independent at Note
0011's seam. The derived split, allowed \(P\)'s, smallest \(Z_0\), conditioned
restriction, \(Z_0'\), weakening family, and allowed outputs nevertheless
depend on \(A\) through the marked seed and must be reconstructed. Equation
(2.8) weakens the entire transformed integrand, so its derivatives can hit
the mark through transformed fluctuation arguments.

Equation (2.10)'s component factorization then has exactly one marked factor:
the root-retaining component carries the decorated derivative and every other
component carries ordinary \(H\). Note 0021 records this finite algebra and
the exact hard-core numerator. RG II remains unmarked and supplies no direct
marked conditioning/weakening estimate. The accessible scan corrupts some
operator glyphs in Eqs. (2.3), (2.5), (2.6), and (2.8); their operation types
and support rules are clear, but a clean immutable page-image transcription
is still required before quoting every symbol verbatim.
