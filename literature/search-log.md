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
\(s_{j'}^d\), which cancels Eq. (190)'s \(s_{j'}^{-d}\) source-density factor.
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
some digits and fractions, but the immutable Project Euclid page images were
subsequently checked in Note 0024 and directly confirm the \(8\delta\),
\(9\delta\), \(10\delta\), and \(L/2\) factors. RG II prints no marked
analogue. Note 0021 subsequently carries
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

## 2026-07-22 -- Eq. (2.8) whole-integrand Cauchy audit

[RG II Cluster
Expansions](https://doi.org/10.1007/BF01239022) applies the Section-1
weakening decomposition to the complete standardized function in Eq. (2.8).
The Section-1 discussion uses complex weakening variables on
\(|s(\Delta)|\le e^{\kappa_1}\) and represents the derivatives by Cauchy
contours. Section 2 then treats each Eq. (2.14) term as analytic in the
complex weakening and Mayer parameters before estimating the whole
conditioned Gaussian expression.

Under the stated common \(L^1\)-holomorphy and joint-majorant hypotheses,
Note 0022 records the exact repository consequence for a distinguished mark:
the integrated mixed derivative equals an alternating endpoint difference
and one iterated contour of the complete marked integrand. The bound has
\(\prod_e(R_e-1)^{-1}\), with no added \(2^{|S|}\),
decoration-allocation factor, or factorial. Expanding product rules before
taking absolute values would introduce those factors artificially.

This does not import the unmarked Eq. (2.14) estimate for the mark. The
earlier Eq. (1.34) marked norm controls the original fluctuation-field domain,
whereas the conditioned and standardized formula evaluates the marked factor
at a transformed argument involving an unbounded Gaussian variable and
complex weakening parameters. A common transformed holomorphy domain and one
joint relative Gaussian-moment envelope remain to be proved from the full
formula. Separate marked and unmarked integrated bounds are insufficient.
The OCR does not cleanly settle every transformed cutoff glyph. If a sharp
cutoff depends on the weakening variables and lacks a holomorphic extension,
it must be kept outside the contour and controlled by a separate valid
real-derivative estimate with its allocation loss exposed.

## 2026-07-22 -- fixed-cubical hull, animal, and pinned-KP audit

[RG II Cluster
Expansions](https://doi.org/10.1007/BF01239022) Eqs. (2.11)--(2.13) supply
the convention being modeled: sharing a cube or a complete cube wall is
incompatible, and a connected tuple is grouped by its literal union. They do
not print a contained-tree hull theorem, a rooted-animal constant, or the
numerical Kotecky--Preiss criterion below.

[Note
0023](../research/notes/0023-fixed-cubical-hull-animals-kp.md) proves those
statements in a declared standard model of closed cubes on one fixed
cubulation. For the side-length-normalized piecewise-linear contained-tree metric,
the literal union of one marked and \(n\) ordinary occurrences obeys

\[
d(R)\le d(A)+\sum_i d(X_i)+\sqrt{D+3}\,n.
\]

The proof uses one connector for each edge of an occurrence-graph spanning
tree; in \(D=4\), the safe shared-cube and full-wall costs are \(2\) and
\(\sqrt7\). It treats periodic seams in the quotient cubical complex and
retains repeated occurrences in the cluster sum even though they do not
enlarge the union.

The same model gives \(N(Y)\le2^D+2^{D+1}d(Y)\). Combining this with a
depth-first rooted-animal encoding yields, in four dimensions,

\[
C_{\rm an}^{\rm geom}(\eta)
\le
\frac{(8^{32}-1)/63}{1-8^{32}e^{-\eta/2}},
\qquad
\eta>64\log8.
\]

With an ordinary pointwise bound \(h e^{-\beta d(X)}\), pinned weight
\(A(X)=\alpha N(X)\), and hull weight
\(c(X)=a(d(X)+\sqrt7)\), Note 0023 then gives the explicit sufficient
condition

\[
9h\,e^{16\alpha+a\sqrt7}
C_{\rm an}^{\rm geom}(\beta-a-32\alpha)\le\alpha.
\]

This is theorem-level repository geometry. Subsequent Note 0024 identifies
the final connected ordinary RG-II gas with this model and supplies an
explicit displayed-hierarchy-compatible ordinary smallness window. The
intermediate support families, decorated marked norm, conditioned-contour
bound, external source disk, differentiated convergence, and shifted-branch
synchronization remain open.

## 2026-07-22 -- Balaban final-gas and explicit ordinary KP audit

The immutable Project Euclid copies of RG I and RG II were downloaded and
hashed; the exact files and page map are recorded in the [dedicated
audit](audits/2026-07-22-balaban-final-gas-kp-map.md). Direct page inspection
establishes the following narrow source-to-model crosswalk:

- RG I's \(\mathcal D_j\) is the class of finite face-connected unions of
  closed regular cubes in Euclidean space or the quotient torus.
- Its \(d_j\) is the cube-side-normalized shortest continuous contained tree
  meeting every cube, with an equivalent shortest cube-edge graph.
- After RG II Eq. (2.10) factorizes disconnected preactivities, Eq. (2.11)
  has one aggregated ordinary \(H(Z)\) per connected support, incompatibility
  exactly through a shared cube or complete wall, and Eq. (2.13) groups by the
  literal union.

This does not identify the intermediate
\(Y_0,Z_0,\widetilde Z_0,Z'_0,X_0\) objects with final polymers. Their
mixed-scale completion and disconnected-component rules remain distinct.

The same images confirm Lemma 3's ordinary decay exponent
\((1-8\delta)(L/2)\kappa\), the subsequent \(9\delta\) and \(10\delta\)
spends, and the final choice
\(\delta=\frac1{10}(1-2L^{-1})\). Combining the printed
\(h=C_3\varepsilon _1\) with Note 0023 gives a concrete sufficient
refinement:

\[
 \kappa>\frac{1280\log8}{L-2},
 \qquad
 \alpha=\frac{(L-2)\kappa}{1280},
\]

followed by the explicit positive upper bound on \(\varepsilon _1\) in Note
0024. This is a repository KP criterion contained inside the **displayed**
"\(\kappa\) sufficiently large, \(\varepsilon _1\) sufficiently small"
hierarchy, not a criterion printed by Balaban. Full source compatibility is
conditional on downward monotonicity of the restrictions imported but not
enumerated in RG I/II. No marked activity estimate or physical connected
observable follows.

## 2026-07-23 -- conditioned-mark routing correction

The immutable Project Euclid RG II PDF was rechecked at printed pp. 12--15;
its SHA-256 is
`EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`.
The exact page map and formulas are recorded in the
[conditioned-routing
audit](audits/2026-07-23-balaban-conditioned-mark-routing.md).

This audit corrects the preceding 2026-07-22 fixed-partition and
whole-integrand entries. Equation (2.5) leaves the localized factor as
\(F(Z_0,B)\) inside the restricted Gaussian. Equation (2.6) standardizes
only the exterior variable \(B'=(C^{(k)})^{1/2}X\). Equation (2.8) inserts
its weakening variables only into the covariance, its square root, and
\(\Delta_k\); Eq. (2.14) confirms that both cutoff factors and
\(V_k(Y,B)\) remain on the same conditional interior \(B\) and have no
\(\sigma\)-argument.

For the repository marked seed
\[
Y_0^\bullet=A\cup\bigcup_{Y\in D}Y,
\]
the interior cutoff controls all fluctuation coordinates of the already
localized \(W_{k,p}(A,B)\). Thus
\[
\chi_{k,Y_0^\bullet}(B)\ne0
\Longrightarrow
|W_{k,p}(A,B)|
\le
\sup_{\mathrm{Eq.\ (1.34)}|_A}|W_{k,p}(A)|.
\]
The fixed marked Eq. (2.14) term is bounded by this input norm times the
ordinary positive majorant for the enlarged seed. No transformed marked
argument, relative Gaussian moment, smaller second-stage radius, or
weakening derivative of the mark occurs.

This is YM-RG-025, a repository corollary; Balaban's paper remains unmarked.
The first remaining estimate is the positive resummation of the enlarged
seed through the source's Eqs. (2.26)--(2.32), including marked tree gluing
and scale conversion. No final marked activity norm or physical connected
observable follows yet.

## 2026-07-23 -- marked-seed resummation through the RG-II scale step

The same immutable RG-II PDF was inspected at printed pp. 17--20, Eqs.
(2.26)--(2.38); its SHA-256 remains
`EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`.
The exact source ledger and repository/source boundary are recorded in the
[marked-resummation
audit](audits/2026-07-23-balaban-marked-resummation.md).

The source sum in Eq. (2.1) is over finite subfamilies, with no
\(1/|D|!\). For the enlarged marked seed this creates two possible
preimages under \(D\mapsto D\cup\{A\}\) when an ordinary support equals the
marked support. Combining this exact collision count with Eqs.
(2.27)--(2.29) yields the rooted coefficient
\[
\varepsilon_\bullet=2\alpha _6^{-1}\mathcal B_\bullet
\]
at exponent \((1-4\delta)\kappa\). The printed \(P,Y_0,Z_0\) estimates then
preserve that coefficient and reach the marked analogue of Eq. (2.35).

From Eq. (2.35) onward, erasing the colour maps every marked scale-stage
history to an ordinary history with one eligible raw component
distinguished. For the finite positive majorant
\(\mathscr S_x(Z)=\sum_Na_N(Z)x^N\),
\[
\mathscr S^\bullet_{x,y}(Z)
\le y\partial_x\mathscr S_x(Z)
\le\frac{y}{2x}\mathscr S_{2x}(Z).
\]
Rerunning the termwise-positive scale inequalities at doubled abstract
amplitude gives
\[
|W_p^{\rm post}(Z)|
\le4K_{\rm lift}\alpha _6^{-1}\mathcal B_\bullet
e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)}.
\]
This doubling and the envelope \(K_{\rm lift}\) are repository refinements,
not formulas printed by Balaban.

Note 0026 uses the previously audited animal/KP interface to obtain the
\((1-9\delta)(L/2)\kappa\) rooted marked norm and the absolutely convergent
connected first derivative at \(t=0\) on one fixed gas, with output exponent
\(\kappa\). It does not construct a common source disk, synchronize shifted
partitions, prove physical \(U/J\) pullbacks, or advance any continuum or
mass-gap gate.

## 2026-07-23 -- singleton-metric and final-KP correction

A proof red-team found that the earlier source-identification wording was too
strong. Note 0023's auxiliary animal metric explicitly admits a degenerate
one-vertex tree, whereas Balaban does not state that singleton convention and
RG II Eq. (2.30) uses a positive volume-to-\(d_j\) comparison. Note 0024 now
uses only the rigorous one-sided facts

\[
d_{\pi_j}^{\rm aux}(Y)\le d_j(Y)
\]

and

\[
d_j(R)\le d_j(A)+\sum_i d_j(X_i)+\sqrt{D+3}\,n.
\]

The first follows because a shortest source cube-edge graph is admitted by
the auxiliary infimum; the second is proved directly by joining source
minimizers inside shared or face-adjacent cubes. Note 0023's new
monotone-metric extension therefore transfers its cube-count, animal, hull,
and KP constants without asserting metric equality. Consistently, Note 0013
now uses the source-convention-safe bound \(d_k(Y)\le m(Y)+1\), retaining the
singleton term at the cost of one overall \(e^a\) factor.

The same red-team also found that Note 0026's connected Eq. (41) must import
Note 0024's separate ordinary-gas premise
\(0<\varepsilon _1\le\varepsilon_{\rm KP}\). The doubled-\(\varepsilon _2\)
conditions control the marked scale susceptibility but do not imply pinned
KP. Both premises are now explicit. The post-polymer marked estimate and
animal norm were unaffected; the final connected conclusion is valid only
under the additionally stated ordinary ceiling.

## 2026-07-23 -- shifted first-jet transport and source-disk correction

No new external paper was needed. The immutable RG-I and RG-II PDFs were
reused and their hashes were pinned in the
[shifted-transport
audit](audits/2026-07-23-balaban-shifted-first-jet-transport.md).

RG II Lemma 2 Eq. (1.41) and Eqs. (2.1)--(2.13) form an exact finite
source-free identity chain. Applying that chain to transported fields proves
the shifted unmarked reconstruction; cutoff inclusion--exclusion and Gaussian
conditioning are exact coordinates for one fixed global integral. The second
localization uses side-\(LM\) cubes, which required lifting the input shifts
modulo \(M\) to nested two-scale shifts modulo \(LM\).

The resulting YM-RG-027 theorem is a repository dual-number and transport
corollary, not a marked theorem printed by Bałaban. It closes only the
first-jet synchronization gate. Earlier ledger phrases saying that a
"common source disk" remained open conflated two objects: Notes 0007 and 0010
already give the selected-coordinate scalar zero-free disk, whereas
source-dependent polymer activities and uniform KP convergence at nonzero
source remain unproved.

## 2026-07-23 -- contained-tree endpoint bridge

The immutable RG-I and Propagators-II records were reused in the
[endpoint audit](audits/2026-07-23-endpoint-distance-bridge.md).
The correct Propagators-II Project Euclid PDF was separately pinned as
`tmp/pdfs/propagators-ii.pdf`, with SHA-256
`6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F`.
It is distinct from `tmp/pdfs/rg-ii.pdf`, SHA-256
`EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`,
which is the later RG-II cluster-expansion paper and does not contain Eqs.
(2.45)--(2.54).

RG I p. 257 supplies the side-length-normalized continuous contained-tree
metric. Propagators II Eqs. (2.45)--(2.54) supply the multiscale labels,
contour metric, and triangle inequality. Neither source states a discrete
fine-bond realization of the contained tree or the periodic endpoint
comparison used here.

YM-RG-028 is therefore a repository quotient-geometry corollary. Lifting the
complete continuous route to the periodic cover converts Euclidean tree
length to fine-lattice endpoint distance with the safe factor \(\sqrt d\).
Applying Note 0019's already conditional ownership estimate only afterward,
to a separate fine geodesic, removes \((\mathrm H_T)\) and \(\tau\) without
assigning an ownership label to off-lattice tree points.

The first-stage zero-halo result is likewise a repository application of
Note 0012's independent-variable interior locality. It is not a source
theorem about the external-\(J\) support of completed Section-2 connected
coefficients. The ownership/interface hypothesis, bounded mesh, common
analytic constants, nonlinear \(U\) pullback, and every continuum or
mass-gap gate remain open.

## 2026-07-23 -- completed external-J support

The immutable RG-I and RG-II PDFs were reused and their pinned digests are
recorded in the
[completed-support
audit](audits/2026-07-23-balaban-completed-external-j-support.md).

RG I printed p. 251 defines the bonds induced by a continuous region as the
nearest-neighbor intervals which intersect it; printed p. 262 then defines
both \(U\) and \(J\) at the bonds of a localization domain. Thus the source
restriction convention is bond intersection, not full-bond containment in
the interior and not assignment by one endpoint.

At the start of Section 2, Bałaban suppresses the external gauge fields from
the notation. Immediately after Eq. (2.9), printed p. 14, the paper states
that the final \(H(Z)\) is localized in \(\operatorname {int}Z\) with
respect to those fields. The next page explicitly names the analytic
variables as \((U,J)\). Equation (2.10) factors disconnected outputs, and
Eq. (2.13) groups connected tuples by their literal union.

YM-RG-029 combines those printed unmarked facts with Notes 0012, 0021, and
0025's repository marked map. Running the same support-preserving operations
over the dual numbers shows that both \(H_s(C)\) and
\(W_{p,s}^{\rm post}(C)\) depend only on external fields in
\(\operatorname {int}C\). The field-independent Ursell coefficient,
literal-union grouping, absolute convergence, and post-connected shift
normalization then preserve locality on \(R\).

This closes only the support anchor:
\[
I^{\rm conn}_{J,p,s}(R)
\subset\{b:|b|\cap\operatorname {int}R\ne\varnothing\}.
\]
The admitted shifted cubulations have integer current-lattice walls and
closed cubes, so every nearest-neighbor bond in this support set lies in the
closed union \(R\). Hence deterministic anchors give
\[
h=h_q=0.
\]
It does not give a regulator-uniform full \(\ell^\infty\) \(J\)-tube or a
tube-uniform connected norm. Those quantitative inputs remain necessary for
a no-volume-loss Cauchy derivative estimate and the physical \(J\)
pullback.

## 2026-07-23 -- completed affine-J tube

No new external paper was needed. The immutable RG-I and RG-II PDFs were
reused; their hashes and the exact page map are recorded in the
[completed-tube
audit](audits/2026-07-23-balaban-completed-j-cauchy-tube.md).

RG I printed p. 262 separates its domain conditions: (i) and (ii) involve
\(U\), (iii) gives the direct independent-\(J\) ceiling, and (iv) tests a
\(J_n\) derived from \(U\). Printed p. 263 gives the qualitative smaller
physical domain that motivates Note 0017's explicit
\((\mathrm H_J)\). It does not provide simultaneous representative
compatibility across every overlapping chart in a completed shifted branch.

RG II Eq. (1.34) retains the direct ceiling \(\alpha _0\), Lemma 2 puts the
localized potentials on that domain, and printed p. 15 places the
potentials, quadratic forms, covariances, final activities, and connected
output on the corresponding external \((U,J)\) analytic spaces. Lemma 3 is
uniform throughout the fixed-output domain.

YM-RG-030 is a repository corollary. Under its stronger completed
compatibility hypothesis \((\mathrm H_J^{\rm conn})\), restriction and
shifted relabelling preserve the full affine radius
\(\Delta_J=\alpha _0-\bar\alpha _0\). The marked and connected positive
estimates must then be rerun in local \(H^\infty\) norms. This gives the sum
of coefficientwise tube suprema with
\(B_{\rm conn}^{\rm tube}=B_{\rm conn}\); a pointwise support-sum estimate
alone has the wrong quantifier order. Banach-line Cauchy and YM-RG-029
locality give the full dual \(\ell^\infty\) derivative norm without a bond
count.

The result remains conditional on \((\mathrm H_J^{\rm conn})\). It is a
transverse independent-\(J\) tube, not a nonzero plaquette-source polymer
disk.
\((\mathrm H_\rho)\), bounded mesh matching, common kernel/chart constants,
the scaled nonlinear \(U\) pullback, and every later Yang--Mills gate remain
open.

## 2026-07-23 -- support-anchored physical-J pullback

No new source theorem is asserted. The directly inspected variational-paper
Eq. (190) transcription from Notes 0004 and 0017 and the pinned
Propagators-II convolution were reused. The latter PDF has SHA-256

```text
6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F
```

The source formula is coordinatewise: an output coordinate tagged by
\(\widetilde y_b=(j_b,y_b)\) has exponential decay to the source label
\(\widetilde y'=(j',y')\). It does not require a global nearest-neighbor
ownership map merely to state that kernel estimate.
On the disjoint tagged space, YM-RG-032 explicitly uses the pulled-back
pseudometric
\(d_{\widetilde{\mathcal B}}((j,y),(j',y'))
=d_{\mathcal B}(y,y')\).

YM-RG-032 is a repository reweighting. For the structural completed support
from YM-RG-029, form
\[
S_{p,s,R}=\{\widetilde y_b:b\in I^{\rm conn}_{J,p,s}(R)\}.
\]
The tautology
\[
d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')
\le d_{\widetilde{\mathcal B}}(\widetilde y_b,\widetilde y')
\]
allows the unchanged Eq. (190) convolution to be summed against the exact
finite-dimensional completed \(J\)-dual norm. This yields a
support-anchored physical-\(J\) norm without
\((\mathrm H_\rho)\), mesh matching, an endpoint allowance, or a spend from
the polymer exponent.

The resulting norm is not rooted solely at the marked plaquette. The
stronger target follows from the aggregate endpoint inequality
\[
\sup_{\widetilde y\in S_{p,s,R}}
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y)
\le A d_{k+1,s}(R)+B,
\]
or from an analytic coefficient-weighted substitute. A one-coordinate
countermodel shows that no positive-\(\gamma\) rooted estimate follows from
the unweighted derivative and kernel bounds alone. The endpoint condition is
therefore worst-case sharp as a geometry-only route, not logically minimal
for every coefficient family.

Common kernel/chart constants, the completed tube input, the physical
\(U\) pullback, and all later construction and mass-gap gates remain open.

## 2026-07-23 -- quotient-localized physical-U pullback

No new external theorem is asserted. The Proposition 9 Eq. (190)
transcription in Notes 0004, 0016, and 0017 was rechecked against the
existing source audit. The five printed rows remain

\[
K,\quad \nabla K,\quad \zeta\nabla K,\quad
D_{U_k}^{\eta *}D_{U_k}^{\eta}K,\quad
\Delta_{U_k}^{\eta}K,
\]

with output weights \(s_j^{-1},s_j^{-2},s_j^{-2-\beta},s_j^{-3},s_j^{-3}\)
and common source factor
\(s_{j'}^{-d}e^{-(\delta _0/8)d_{\mathcal B}(y,y')}\).
The source measure \(s_{j'}^d\) algebraically cancels the inverse density.
The Propagators-II PDF used for the convolution retains SHA-256

```text
6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F
```

The source does not print the assembled four-feature operator estimate
needed by Note 0031's covariant \(U\) norm. Raw RG and operator features can
use \(K\) after chart conversion; the covariant gradient uses \(K\) and
\(\nabla K\). The covariant curl still needs an exact transported
four-link identity with the correct \(\xi^{-1}\) normalization. The printed
\(D^*D K\) and \(\Delta K\) rows belong to the auxiliary-\(J\) differential
and are not curl substitutes. A multi-link feature also needs a bounded
decomposition into tagged Eq. (190) output terms; \(x\in\Delta(y)\) does not
place an entire stencil in one cell.

YM-RG-033 first proves a repository operator-duality corollary. At
\(\gamma=0\), common converted feature rows and a global scale envelope map
the source \(\ell^\infty\) ball into Note 0031's global \(U\) ball. Source
phase duality then gives the unweighted physical-\(U\) sum without a
coordinate or volume factor.

For positive source weight, Note 0029's completed external-\(U\) locality
lets the coefficient derivative descend isometrically to the restriction
quotient \(X_{\bar U,\xi}/N_I\). The weighted quotient-synthesis operator
norm is exactly the sharp coefficient-independent missing kernel moment. A
feature-support-anchored estimate follows from the separately named local
extension hypothesis \((\mathrm H_{\rm ext}^U)\); active-bond anchoring
also pays a separately assumed collar halo.

The common converted feature rows, covariant-curl identity, global and local
scale envelopes, local extension theorem, and
\((\mathrm H_{\rm rc})\) for the actual minimizing family remain open.
Nothing in this audit establishes nonzero-source polymer activities, a
large-field step, iteration, a continuum theory, infrared decay, or a mass
gap.

## 2026-07-23 -- transported curl and physical-width extension audit

Primary files:

- `tmp/pdfs/gauge-fixing-conditions.pdf`,
  SHA-256
  `7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB`;
- `tmp/pdfs/rg-i-full.pdf`,
  SHA-256
  `1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A`.

The rendered pages visually checked for YM-RG-034 were gauge-fixing printed
p. 76 Eq. (1.1), p. 82 Eq. (1.36), pp. 84--85 Eqs. (1.47)--(1.50), and
RG I printed p. 262 Eqs. (1.11)--(1.14).

Gauge-fixing Eq. (1.1) fixes the scaled two-point convention
\[
D_{U,\mu}^{\eta}F
=
\eta^{-1}\bigl(\operatorname{Ad}_{U_\mu}F(\,\cdot+\eta e_\mu)-F\bigr).
\]
Equation (1.36) supplies the raw and covariant-gradient scale shapes
\((L^j\eta)^{-1}\) and \((L^j\eta)^{-2}\). Equation (1.47) places the
normalized covariant plaquette curl in the linear relative-plaquette term as
\(i\eta^2D_U^\eta A\), and Eqs. (1.49)--(1.50) separate it from quadratic
commutators. RG I Eq. (1.13) controls the same raw/gradient pair for the
complex relative field \(U'=\exp(i\xi A')\).

The source does not print the new theorem. Repository prefix transport gives
the exact curvature-corrected identity
\[
\mathcal D_{\bar U}^{\xi}a
=
D_\mu^\xi a_\nu-D_\nu^\xi a_\mu
+\xi^{-1}(I-\operatorname{Ad}_{d\bar U(p)})
(a_\nu+T_\nu a_\mu).
\]
Under \((\mathrm H_{\rm rc})\), the \(O(\xi^2)\) curvature margin makes the
full Note 0031 norm uniformly equivalent to the source's raw/gradient pair.
The variational paper's \(D^*D K\) and \(\Delta K\) rows are not curl
substitutes.

An exact cutoff product rule on the two-point gradient graph proves the
restriction-quotient extension with constant
\[
C_{\rm eq}(\xi)
\left(1+\frac{c_{\rm Ad}^{\rm RG}}{m\xi}\right).
\]
Taking \(m=\lceil\rho/\xi\rceil\) is uniform. A normalized scalar flat
abelian longitudinal path has zero curl and exact endpoint quotient norm
\(\max\{1,2/(N\xi)\}\), which rules out a uniform fixed-layer collar for
arbitrary active sets. Its embedding along a fixed commuting generator
changes only fixed matrix-norm constants.

The audit therefore removes an independent curl row and the abstract
feature-collar extension premise. It does not prove the converted
\(K,\nabla K\) rows, a regulator-compatible scale envelope, the
active-label metric halo, or \((\mathrm H_{\rm rc})\) for the physical
family. In particular, the source measure cancels only the input-density
factor, not the output-scale powers, so the naive raw/gradient envelope can
diverge at the finest output scale. The chart normalization has no unused
\(\xi\) factor under the current bounded conversion hypotheses. All
nonzero-source, large-field, iteration, continuum, reconstruction, infrared,
and mass-gap gates remain open.

## 2026-07-23 -- scale-balanced physical-\(U\) renorming audit

Primary files:

- `tmp/pdfs/gauge-fixing-conditions.pdf`,
  SHA-256
  `7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB`;
- `tmp/pdfs/rg-i-full.pdf`,
  SHA-256
  `1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A`;
- `tmp/pdfs/propagators-ii.pdf`,
  SHA-256
  `6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F`.

Gauge-fixing Eq. (1.36) supplies the matching raw and covariant-gradient
scale shapes. Separately, variational-paper Proposition-9 Eq. (190) carries
the corresponding output powers \(s_j^{-1}\) and \(s_j^{-2}\) together with
the input density \(s_{j'}^{-d}\). The source measure cancels only the last
factor.
On the one-step specialization \(\eta=\xi\), weighting raw output
occurrences by \(s_j\) and gradient output occurrences by \(s_j^2\)
therefore cancels the two printed output powers algebraically. The printed
formulas attach \(j\) to an output occurrence; they do not by themselves
provide one globally consistent tag for every shared bond or stencil in the
completed shifted family.

No new theorem is attributed to the papers. YM-RG-035 proves from the
two-point product rule that the corresponding physical-width quotient
constant is
\[
1+\frac{c_{\rm Ad}^{\rm RG}\Theta}{\rho},
\qquad
\Theta=\sup_e\frac{t_e^2}{\min(r_{e,-},r_{e,+})},
\]
and a weighted scalar path shows that the \(\Theta/\rho\) dependence is
order-sharp.

The same renorming fails the analytic-domain test. On a homogeneous finest
patch, an isolated complex Cartan bond has bounded row-balanced norm but
changes an adjacent plaquette by \(O(1)\), whereas RG I condition (iii)
allows only \(O(\xi^2)\) curvature. A curl-free longitudinal step separately
violates RG I condition (ii). Hence a full row-balanced chart ball has radius
at most \(O(\xi^2)\), and the exact one-dimensional inclusion/Cauchy model
restores the \(\xi^{-2}\) dual loss.

This closes only the diagonal-renorming branch. Direct smoothing or
cancellation for the assembled synthesis, a two-norm completed derivative
theorem, a justified weighted physical-source target, or a proof that the
offending finest output rows are absent remains open. So do
\((\mathrm H_{\rm rc})\), the completed feature-tag atlas, nonzero-source
activities, large fields, iteration, continuum construction, infrared
decay, and the mass gap.
