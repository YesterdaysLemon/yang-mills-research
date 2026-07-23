# Program 002: one-block local-observable RG theorem

Claim ID: `YM-RG-001`

Status: Open theorem specification

Evidence: E0

Initial group: \(SU(2)\)

Novelty: not claimed pending theorem-level prior-art comparison

## Setup

On an oriented four-dimensional periodic lattice, assign \(U_e\in SU(2)\) to
each positive link and \(U_{\bar e}=U_e^{-1}\). For a plaquette \(p\), let

\[
U_p=\prod_{e\in\partial p}U_e,
\qquad
s(U_p)=1-\tfrac12\operatorname{ReTr}U_p.
\]

Write \(x=g^{-2}\). For a real profile \(f\), introduce

\[
S_{x,z,f}(U)=4\sum_p\bigl(x+zf_p\bigr)s(U_p).
\]

Here \(z\) is a new complex source parameter. It is deliberately not called
\(J\), because \(J\) already denotes Bałaban's auxiliary derivative field in
the small-field induction. Two profile classes have different jobs:

- the normalized class supported in one coarse block, with
  \(\|f\|_{C^6_{\rm disc}}\le1\), tests locality and polymer decay;
- the finite-volume profile \(f\equiv1\) is used only for a first-derivative
  consistency test at \(z=0\), not for the local-profile norm.

Freeze the Euclidean-symmetric average in RG I Eq. (0.12), with the group
average and contour variables of Eqs. (0.5)–(0.11), and the raw group-delta
transform in Eq. (10) of the earlier averaging paper. The exact
selection and imported hypotheses are recorded in the [imported-map
audit](../../literature/audits/2026-07-22-balaban-imported-map.md). The block
factor retains RG I's odd-\(L>11\) assumption.

Write \(\mathcal T_L^{\rm raw}\) for this raw unnormalized linear transform,
whose kernel is fixed independently of \(x\) and \(z\). Any
coupling-dependent normalization, small-field threshold, or large-field
operation is a separate displayed factor. Define

\[
\mathcal R_{x,z,f}(V)
=\frac{\mathcal T_L^{\rm raw}(e^{-S_{x,z,f}})(V)}
{\mathcal T_L^{\rm raw}(e^{-S_{x,0,f}})(V)}.
\]

The ratio prevents source-free irrelevant terms from being mislabeled as
source responses. For fixed admitted \(g,L\), the normalized local profile
class, and every admissible coarse field \(V\), the target must prove a common
zero-free disk \(|z|\le z_0(g,L)\). Its radius must be independent of cutoff,
torus size, source location, \(f\) in the normalized class, and \(V\) in the
stated field domain. Use the analytic branch fixed by
\(\log\mathcal R_{x,0,f}=0\).

[Note 0003](../notes/0003-raw-block-source-jets.md) proves the pointwise
finite-regulator cumulant identities for any positive coupling-independent raw
kernel. It supplies no uniform radius, locality, mixing, or large-field bound;
those remain the content of this program.

[Note 0007](../notes/0007-projective-source-kernels.md) sharpens the source
radius issue: once the exact pointwise kernel gives a positive finite
source-free weighted partition function, bounded range of the one-block
plaquette observable gives an explicit common zero-free source disk and, using
its absolute SU(2) bound, crude uniform
first/second-jet bounds. A strictly smaller radius gives the closed disk
required below. No
volume-independent lower bound on the raw cutoff mass is required. Matching
the exact RG coordinate weight, the profile norm, quasilocality,
projection/mixing, and large fields remain open.

[Note 0008](../notes/0008-full-fixed-cutoff-branch.md) now supplies that
pointwise measure for the complete selected Eq. (2.9) near-identity branch.
[Note 0009](../notes/0009-parameterized-fixed-cube-kernel.md) promotes it on
one relatively compact background patch to a Borel kernel with analytic test
integrals, local holomorphic test-integral continuations, and exact real
coarse-gauge covariance between transported charts. Neither note identifies
the branch with the unrestricted raw group-delta transform, builds a global
compatible atlas, or matches the intrinsic density term by term to RG I
Eq. (2.12).

[Note 0010](../notes/0010-exact-rg-coordinate-law.md) avoids that unmatched
identification by separately naming the exact normalized RG I
Eqs. (2.12)–(2.13) Gaussian/cutoff law. It proves positivity, patch-local
analytic-test dependence, a centered-score background derivative, the bounded
source disk, and real gauge covariance for that operational law. The marked
selected-branch subtheorem in Program 003 must use this named law and must not
relabel it as the intrinsic or unrestricted conditional measure. Program
002's eventual unrestricted target still requires a separate density/complement
comparison.

[Note 0011](../notes/0011-one-mark-mayer-seam.md) inserts one real plaquette
source into that exact law, splits off the fixed background, and proves the
finite-regulator one-mark Mayer identity immediately after RG II Lemma 2. It
does not itself localize the marked insertion. [Note
0012](../notes/0012-rooted-plaquette-localization.md) separately proves an
exact independent-variable rooted decomposition and conditional cube-count
norm for fixed-partition interior plaquettes. [Note
0013](../notes/0013-rooted-dk-norm.md) upgrades that norm on the standard
\(M\)-cube branch under an explicit entropy margin. [Note
0014](../notes/0014-equivariant-shifted-roots.md) gives an RG-admitted
shifted-family cover for every plaquette and transport under the subgroup
preserving the next coarse lattice. [Note
0015](../notes/0015-fixed-patch-physical-composition.md) conditionally composes
that family on one common physical \((U,J)\) chart and preserves its
zeroth-order value norm. [Note
0016](../notes/0016-auxiliary-j-cauchy-tubes.md) identifies RG I's exact
finite-stencil physical auxiliary field and proves conditional rooted
independent-variable derivative norms on full complex tubes at fixed
regulator. [Note
0017](../notes/0017-strict-j-margin-metric-pullback.md) adds a strict
direct-\(J\) representative collar, the dual source-metric kernel sum, and a
conditional homogeneous-layer pullback for the auxiliary-\(J\) chain-rule
summand; it also disproves a uniform reverse cross-layer bound while leaving
the forward direction unresolved in that note. Note 0019 proves the
all-layer \(J\)-summand implication under explicit interface, tree-lift,
support, mesh, and common-chart premises, without deriving those premises
from the source. Note 0018 proves that naive raw and \(\xi\)-scaled bond-sup
\(U\) collars collapse and leaves the RG-scaled replacement conditional.
[Note 0020](../notes/0020-one-mark-ursell-identity.md) proves the exact
distinguished-vertex Ursell formula and a conditional pinned bound on one
fixed hard-core gas. [Note
0021](../notes/0021-one-mark-section2-factorization.md) constructs the exact
decorated post-conditioning activity and unique marked-component
factorization on one compatible fixed partition. [Note
0022](../notes/0022-whole-integrand-marked-cauchy.md) proves that one contour
of the complete marked weakening integrand, under common \(L^1\)-holomorphy
and a joint majorant, has no extra derivative-allocation multiplicity and has
the ordinary radius price if that radius is shared. It reduces the estimate
to a joint conditioned-contour Gaussian envelope and positive seed-dependent
kernel. [Note
0023](../notes/0023-fixed-cubical-hull-animals-kp.md) proves a literal-union
hull, a volume-uniform animal bound, and an explicit sufficient pinned
Kotecky--Preiss/hull-weight package for a separately declared standard
closed-cube model with one species per support. [Note
0024](../notes/0024-balaban-final-gas-instantiation.md) identifies the final
connected ordinary RG-II gas with that model and gives a
displayed-hierarchy-compatible ordinary KP-smallness window. The actual
transformed marked envelope and kernel decay, decorated marked norm,
differentiated absolute convergence, and shifted-branch synchronization
remain unproved.
Unit-translation covariance, the scaled nonlinear \(U\) collar and pullback,
uniform realization of Note 0019's premises,
the actual single-partition marked estimate, the full physical
coarse-background derivative norm, and a physical rooted connected bound
remain open.

## Target statement

For admitted regular \(V\), the variational theorem gives a unique minimizing
**gauge orbit** \([U_1(V)]\), not initially a global single-valued map. Define

\[
\mathcal E^{\mathrm{bg}}_f(V)
=4\sum_p f_p\,s\!\left(U_1(V)_p\right).
\]

This is representative independent because the plaquette trace is gauge
invariant. Any analyticity or quasilocality assertion in \(V\) must use the
specific local gauge-fixed branch and domain in Proposition 9 of the
variational paper. [Note 0004](../notes/0004-fixed-background-source-jet.md)
records exactly what that source-free background theorem supplies.

Derive a localized projection \(\Pi_{\rm rel}\) onto **all**
source-dependent relevant and marginal directions permitted by the residual
lattice symmetries and the profile class. Then prove a decomposition

\[
\log\mathcal R_{x,z,f}(V)
=M_{\rm rel}(V;z,f)
+\sum_X K_X^{\mathrm{irr}}(V;z,f),
\qquad
M_{\rm rel}=\Pi_{\rm rel}\log\mathcal R.
\]

The first source jet must be displayed rather than assumed to close on one
scalar coefficient. In general it may have the form

\[
\left.\partial_zM_{\rm rel}(V;z,f)\right|_{z=0}
=c_{\mathbf1}(x,L;f)
-\mathcal E^{\mathrm{bg}}_{\mathsf Z_E(x,L)f}(V)
+\sum_{\alpha\in\mathcal A}
c_\alpha(x,L;f)\,\mathcal O^{\mathrm{bg}}_\alpha(V).
\]

Here \(\mathsf Z_E\) is allowed to mix plaquette positions and orientations,
and \(\mathcal A\) contains any additional symmetry-allowed relevant or
marginal operators. The proof must classify this list. A scalar
\(\mathsf Z_E=Z_E\mathbf1\), or an empty \(\mathcal A\), may be concluded only
after a symmetry/mixing argument or after restricting to a proved invariant
profile. Higher source jets must likewise display every projected counterterm.
Replacing the fine-background insertion by the plain coarse Wilson action of
\(V\) requires a separate theorem.

The normalization must account for the fact that this \(SU(2)\) convention
has coefficient \(4x\), whereas Bałaban's normalized-trace action gives the
working crosswalk \(x_B=4x\). That translation must be rechecked for the
finally selected map.

The required properties are:

1. the localization scheme defines \(\Pi_{\rm rel}\) polymerwise, each
   \(K_X^{\mathrm{irr}}\) vanishes at \(z=0\) and obeys
   \(\Pi_{\rm rel}K_X^{\mathrm{irr}}=0\), and every activity is
   coarse-gauge invariant, localized to a connected polymer \(X\), and
   analytic on the proved common source disk;
2. for the normalized local profile class, **both** the projected sector and
   the irrelevant sector through two source derivatives obey volume-, cutoff-,
   and source-location-independent estimates. In particular, the kernels of
   \(\mathsf Z_E\), every coefficient \(c_\alpha\), and all higher projected
   source jets must have summable or proved quasilocal decay away from
   \(\operatorname{supp}f\). The irrelevant activities obey estimates such as
   \[
   \|\partial_zK^{\mathrm{irr}}(0;f)\|_{\kappa,h}
   \le C_1(g,L)\|f\|_{C^6_{\rm disc}},
   \qquad
   \|\partial_z^2K^{\mathrm{irr}}(0;f)\|_{\kappa,h}
   \le C_2(g,L)\|f\|_{C^6_{\rm disc}}^2;
   \]
   the exact norm, constants, coupling range, and any useful smallness in
   \(g,L\) must be derived. These are source-to-remainder bounds, not by
   themselves a contraction of an RG map on incoming activities;
3. the proof identifies its exact small-field domain, and the full version
   includes the large-field complement with an explicit nonperturbative bound
   instead of importing it from a small-field theorem;
4. for the separate finite-volume test \(f\equiv1\), raw linearity gives the
   exact first-jet identity
   \[
   \left.\partial_z\log
   \mathcal T_L^{\rm raw}(e^{-S_{x,z,1}})(V)\right|_{z=0}
   =\partial_x\log
   \mathcal T_L^{\rm raw}(e^{-S_{x,0,1}})(V).
   \]
   No higher-derivative or local-polymer assertion for \(f\equiv1\) is made.
   A later normalized density \(\widehat{\mathcal T}_x
   =N_x\mathcal T_L^{\rm raw}\) has separate normalization derivatives that
   must be included in its own coupling bookkeeping; they do not alter the
   raw identity. Note 0003 proves this algebraic statement under the displayed
   raw-kernel hypotheses; matching those hypotheses to the selected Bałaban
   operation remains open;
5. the one-loop change of inverse coupling matches the universal
   asymptotically free coefficient in the chosen normalization.

For \(SU(2)\), \(b_0=11/(24\pi^2)\). For fixed \(L\) as \(g\to0\), or in a
separately proved regime with \(g^2\log L\ll1\), the consistency target is

\[
x_L=x-2b_0\log L+O(g^2\log L).
\]

RG I defines a recursive beta term but explicitly defers the perturbative
evaluation of its stated coupling-flow theorem. It cannot be cited as already
proving this coefficient.

## Why this is useful and bounded

The plaquette energy is gauge invariant and arises by differentiating the
action with respect to inverse coupling. Source derivatives test whether the
RG construction controls local observables rather than only the partition
function. One step is small enough for a line-by-line audit while addressing a
missing interface in this proposed constructive route.

Even a complete proof would remain an auxiliary E2 result. It would prove no
continuum limit, no iteration through strong coupling, no OS reconstruction,
and no mass gap.

## Work packets

- [x] Freeze RG I Eq. (0.12) and the raw group-delta transform;
  record the imported map, chart, propagator, and minimizer anchors.
- [ ] Transcribe every selected field domain, norm, and constant dependency
  into the one-step proof without alteration.
- [ ] Complete the theorem-by-theorem prior-art matrix: the imported map papers
  are now audited, but Large Field II remains abstract-only.
- [x] Derive the finite-regulator raw source-cumulant and constant-profile
  coupling identities; see Note 0003.
- [x] Separate almost-everywhere disintegration from the raw pointwise density
  and prove the selected constraint has a positive local fiber ball; see Notes
  0005–0006.
- [x] Use RG II's complete-cube estimate to construct a pointwise finite
  nonzero positive measure on the full selected fixed-cutoff chart branch; see
  Note 0008. Equality with the unrestricted transform remains open.
- [x] Prove patch-local joint branch analyticity, Borel-kernel regularity,
  analytic-test continuation, and transported-chart real gauge covariance;
  see Note 0009. Global chart compatibility and the intrinsic-to-RG density
  match remain open.
- [x] Name the exact normalized RG-I Eq. (2.13) coordinate law and prove its
  finite-regulator positivity, fixed-domain analytic-test dependence,
  centered-score derivative, source disk, and real gauge covariance; see Note
  0010. Matching to the intrinsic or unrestricted raw law remains open.
- [x] Derive the exact background-centered first mark and its finite Mayer
  identity at the RG-II Section 2 seam; see Note 0011.
- [x] Prove the exact independent-variable decomposition for each
  fixed-partition interior plaquette and a conditional cube-count norm uniform
  over those plaquettes; see Note 0012. The \(d_k\) upgrade is checked in the next
  item, the shifted cover in the item after it, and fixed-chart physical
  composition after that; quantitative coarse-field locality and connected
  bounds remain open.
- [x] Upgrade the standard wall-adjacent \(M\)-cube branch to a rooted
  \((1-2\delta)\kappa d_k\)-weighted norm under the explicit entropy margin;
  see Note 0013. The shifted cover and fixed-chart composition are checked in
  the next two items; the derivative pullback norm and connected bound remain
  open.
- [x] Cover every plaquette by the normalized RG-admitted shifted family with
  no additional orbit entropy and prove transport under the subgroup
  preserving the next coarse lattice; see Note 0014. Unit translations and
  synchronized fixed-partition cluster compatibility for every shift remain
  open; Note 0021 proves only the exact algebra on one compatible branch.
- [x] On one common holomorphic physical \((U,J)\) chart,
  compose the shifted family, preserve its exact identity, fluctuation
  locality, centering, covariance, and zeroth-order norm, and record the full
  chain rules; see Note 0015.
- [x] Identify the exact physical auxiliary field from RG I, retain its local
  differential remainder, and prove conditional rooted \(D_U\)- and
  \(D_J\)-operator norms on explicit full complex tubes at fixed regulator;
  see Note 0016. Uniform radii/chart constants, the
  source realization of Note 0019's conditional
  \(d_{\mathcal B}\)-to-\(d_{k,\sigma}\) bridge and the full physical
  Eq. (190) derivative norm remain open.
- [x] Use RG I's strict smaller physical representative domain to obtain the
  direct-\(J\) sup-norm collar, prove the dual Eq. (190) source convolution,
  and close the auxiliary-\(J\) pullback on one matched homogeneous layer;
  see Note 0017. Note 0018 closes the naive raw-\(U\) radius route and
  specifies the missing scaled chart estimates. Note 0019 extends the
  \(J\)-summand conditionally across layers. Its interface/tree/support
  premises and the scaled nonlinear \(U\) pullback remain open.
- [x] Prove the exact one-mark connected-graph formula, repeated-label
  convention, and conditional pinned Kotecky--Preiss implication for one
  fixed hard-core gas; see Note 0020.
- [x] Carry the localized mark through the finite RG II Eqs. (2.1)--(2.10)
  algebra on one fixed compatible partition, define its decorated
  post-polymerization image, and prove the unique marked-component and exact
  hard-core numerator identities; see Note 0021. Proving the direct marked
  domination, rooted norm, differentiated convergence, and synchronized
  shifted construction remains open.
- [x] Apply one multivariable contour to the complete marked Eq. (2.8)
  integrand under explicit common \(L^1\)-holomorphy and joint-majorant
  hypotheses, retain no added product-rule multiplicity and the ordinary
  Cauchy-radius factor if that radius is shared, reduce the estimate to one
  positive seed-dependent kernel, and correct the conditional exponent ledger
  to a parallel fork; see Note 0022. The actual transformed-mark Gaussian
  envelope, kernel decay, and gluing estimates remain open.
- [x] In a separately declared standard closed-cube support model, prove the
  literal-union wall-contact hull inequality, a volume-uniform geometric
  animal bound, and explicit sufficient conditions for the canonical pinned
  Kotecky--Preiss and hull-weight interfaces; see Note 0023.
- [x] Identify the final connected ordinary RG-II gas with Note 0023's
  quotient cubical support class, contained-tree metric, incompatibility,
  literal-union rule, and aggregated one-species convention, and exhibit a
  displayed-hierarchy-compatible ordinary KP-smallness window; see Note 0024.
  Intermediate support families and the decorated marked norm are not
  covered.
- [x] Prove a common zero-free source disk from bounded observable range,
  conditional on the exact pointwise kernel and positive finite source-free
  weighted partition function; see Note 0007. This does not supply a complex
  coarse-field domain or marked-polymer locality.
- [x] Derive the fixed source-free background jet and transcribe Eq. (190)'s
  five componentwise derivative bounds; see Note 0004. Note 0016 reduces the
  physical auxiliary-field derivative to those rows plus a local remainder,
  and Note 0017 proves the dual convolution and one-layer \(J\)-summand
  specialization. Note 0019 gives a conditional all-layer extension. Uniform
  realization of its chart/geometric premises and the \(U\) summand remain
  open.
- [ ] Classify every relevant/marginal source counterterm and the profile
  mixing map.
- [ ] Differentiate the small-field stationary/background construction
  through order two in \(z\).
- [ ] Prove gauge-orbit derivatives vanish for every polymer activity.
- [ ] Extend the estimates across the separately defined large-field
  operation with volume-independent constants; do not infer this from RG I,
  which is explicitly small-field.
- [ ] Audit the normalized coupling bookkeeping and one-loop coefficient.

## Falsification tests

Reject the target as stated if any of the following occurs:

- a constant grows with the total number of blocks;
- a global logarithm \(U_e=\exp A_e\) silently crosses the group cut locus;
- the large-field complement is omitted;
- a source-free effective action is replaced by a plain coarse Wilson action
  instead of the fine background action without proof;
- any polymer activity changes under a coarse gauge transformation;
- a source spreads without summable decay outside its block;
- a symmetry-allowed mixing or marginal term is omitted;
- the local-profile and constant-profile quantifiers are conflated;
- the logarithm is used without a uniform zero-free source disk and a fixed
  branch;
- the raw and normalized coupling derivatives are conflated;
- the universal one-loop coefficient fails after normalization is reconciled;
- reflection positivity is claimed for the effective action without a
  separate proof;
- numerical agreement replaces the analytic estimate.

## Sources audited first

- [Bałaban, RG approach I](https://doi.org/10.1007/BF01215223)
- [Bałaban, RG approach II](https://doi.org/10.1007/BF01239022)
- [Bałaban, convergent renormalization expansions](https://doi.org/10.1007/BF01217741)
- [Bałaban, large-field renormalization I](https://doi.org/10.1007/BF01257412)
- [Bałaban, large-field renormalization II](https://doi.org/10.1007/BF01238433)
- [Bałaban, averaging operations](https://doi.org/10.1007/BF01211042)
- [Bałaban, regular configurations and gauge fixing](https://doi.org/10.1007/BF01466594)
- [Bałaban, background propagators](https://doi.org/10.1007/BF01240355)
- [Bałaban, variational problem/background fields](https://doi.org/10.1007/BF01229381)

The [first source map](../../literature/audits/2026-07-22-balaban-source-map.md)
found the source-free ultraviolet scaffold but no scalar-source theorem. The
[imported-map audit](../../literature/audits/2026-07-22-balaban-imported-map.md)
now fixes the exact raw interface. The next hard target is the fluctuation
remainder between the exact conditional first jet and its minimizing-background
term, stated separately in Program 003. Until the full comparison is complete,
novelty remains false in `CLAIMS.json`.
