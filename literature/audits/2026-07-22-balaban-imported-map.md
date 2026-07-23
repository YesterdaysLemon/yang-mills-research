# Bałaban imported-map audit — 2026-07-22

Status: full-text theorem/interface audit; no novelty or Yang–Mills solution
claim.

This audit selects one concrete averaging operation for the next bounded
experiment and records the exact limitations of the gauge chart, background
propagators, and variational minimizer imported by RG I. Page numbers are
printed journal pages.

## Selected averaging operation

The selected operation is RG I Eq. (0.12), not Eq. (0.4).

RG I introduces Eq. (0.12) to match a Euclidean-invariant axial gauge. It says
that Eqs. (0.4) and (0.12) are equally suitable and that many other maps with
the same essential properties could be used. Selection here is therefore a
new convention for this repository, not a claim that the literature has one
canonical “Bałaban map.”

### Exact construction to import

In [RG I](https://doi.org/10.1007/BF01215223), pp. 252–254:

1. Eqs. (0.5)–(0.10) axiomatize a finite group average \(M\): it is analytic
   on sufficiently close inputs, permutation invariant, covariant under the
   relevant left/right group action, and maps real \(G\)-valued inputs back to
   \(G\).
   The selected Federbush mean is the nearby solution of
   \[
   \sum_j\frac1i\log\!\left(U_jM(\{U_\ell\})^{-1}\right)=0
   \tag{RG I 0.10}
   \]
   on that local domain.
2. Eq. (0.11) defines the symmetric contour variable. The paper writes it as
   \(U(y,x)\); to distinguish it from a link field, this repository writes:
   \[
   C_U(y,x)=M\bigl(\{U(\Gamma):\Gamma\in\mathcal G(y,x)\}\bigr).
   \]
3. For a coarse bond \(c=(c_-,c_+)\), put
   \(x'=x+(c_+-c_-)\). With the repository's scale label
   \(\overline U_L\), Eq. (0.12) is
   \[
   \overline U_L(c)=
   \exp\!\left[
     i\sum_{x\in B(c_-)}L^{-d}\frac1i
     \log\!\left(
       C_U(c_-,x)\,U([x,x'])\,C_U(x',c_+)\,U(-c)
     \right)
   \right]U(c).
   \tag{RG I 0.12}
   \]

This displayed formula, together with the contour set, orientations, local
logarithm branch, and group-average axioms in Eqs. (0.5)–(0.11), is the frozen
repository interface. Those domain conditions must be copied without
enlargement when code or estimates are introduced.

The earlier paper [Averaging operations for lattice gauge
theories](https://doi.org/10.1007/BF01211042), **CMP 98** (1985), 17–51,
provides the underlying interface:

- Eq. (10), p. 19, gives the raw transformation
  \[
  (T\rho)(V)=\int dU\,\delta\!\left(V\overline U(U)^{-1}\right)\rho(U),
  \]
  with the product Haar measure and group delta understood over coarse bonds.
- Eq. (11), p. 19, is gauge covariance of the average. Eqs. (12)–(13) show
  that the raw transform preserves gauge invariance.
- Immediately after Eq. (42), p. 24, the paper records finite-range locality:
  the \(k\)-step averaged bond depends only on fine bonds in the two associated
  \(k\)-blocks.
- Proposition 3, p. 36, gives analyticity and the bounds (122)–(124) only on
  its stated small regular field domain; it is not global group analyticity.

For Program 002, Eq. (10) is the coupling-independent **raw** group-delta
transform. Note 0003 applies only after its delta constraint is realized as a
pointwise nonzero finite positive fiber measure on the admitted coarse-field
domain; a merely formal delta or pushforward-a.e. conditional measure is not
enough for the target analytic estimates. Coupling-dependent normalizations,
gauge-fixing Jacobians, and later small-/large-field operations are not part of
that raw identity.

## Geometry and small-field restrictions

RG I pp. 251–252 takes \(L\) to be an odd integer greater than 11 and fixes its
torus/block geometry before defining Eqs. (0.4) and (0.12). Program 002 must
retain those assumptions unless it reproves the geometric estimates.

RG I then separates several objects that must not be conflated:

- Eq. (0.13), p. 254, is a general gauge-invariant kernel
  \((T\rho)(V)=\int dU\,t(V,U)\rho(U)\).
- Eq. (0.16), p. 255, adds fixed regular/small-field restrictions including
  \(|C_U(y,x)-1|<\varepsilon_0\).
- Eq. (2.9), pp. 266–267, uses
  \[
  \chi_k=
  \prod_{b\in T^{(k)}\setminus\{b_0(c):c\in T^{(k+1)}\}}
  \mathbf1\{|B'(b)|<\varepsilon_1\}
  \]
  on the independent fluctuation bonds. The text also offers the
  coupling-dependent alternative threshold
  \(g_k\gamma_k^{-1}\varepsilon_1\), with
  \(\gamma_k=C\log((L^k\varepsilon)^{-1})\).

The fixed-threshold variant can be coupling independent. The alternative is
not. Differentiating an operation whose indicator or normalization depends on
\(x=g^{-2}\) creates extra terms and may encounter a nonsmooth boundary. The
constant-profile identity in Note 0003 therefore applies first to the raw
transform, not automatically to every restricted effective-action formula.

### Constraint straightening and the local fiber

RG I pp. 265–268 contains more than a formal delta constraint:

- Eqs. (2.2)–(2.4) put the admitted critical background
  \(V^{(k)}(W)\) on the fiber over \(W\) and express the relative constraint as
  \(M(V'V^{(k)})M(V^{(k)})^{-1}=e^{i\widetilde Q(B')}\).
- On p. 267, after Eq. (2.10), the nonlinear map is written
  \(\widetilde Q(B')=L\widetilde QB'+\widetilde C(B')\), with
  \(\widetilde C=O((B')^2)\). One corridor bond \(b_0(c)\) is selected for each
  coarse bond, and a right inverse \(h\), supported on those bonds, satisfies
  \(L\widetilde Qh=I\).
- The analytic change
  \(B'=B-h\widetilde D(B)\), with \(\widetilde D=O(B^2)\), exactly straightens
  the constraint to \(L\widetilde QB\).
- On p. 268 the delta eliminates the variables on \(b_0(c)\) and writes
  \(B'=CB\), where \(B\) contains the remaining independent-bond variables and
  \(C\) is the embedding determined there by \(V^{(k)}\). Eq. (2.12) retains
  the coordinate Jacobian
  \(\exp\operatorname{Tr}\log(I-h\,(\delta\widetilde D/\delta B)(g_kCB))\).
  It equals one at the background. Nonvanishing and constant positive real
  orientation on a sufficiently small chart are continuity corollaries, not a
  printed uniform RG-I estimate.

Thus the selected constraint is a local analytic submersion at each background
in the paper's admitted domain, and a sufficiently small precompact real fiber
ball has positive finite coarea mass. This does not control the entire sharp
cutoff support, furnish a uniform lower bound, or produce a global pointwise
disintegration. The exact corollary and its failure boundary are in [Note
0006](../../research/notes/0006-local-balaban-fiber-chart.md).

### The complete fixed-cutoff cube stays in the selected chart

The local conclusion above is not the end of the printed small-field analysis.
RG I p. 270, Eq. (3.2), and RG II p. 6, Eq. (1.19), write the full relative
field on the selected branch as

\[
B'=g_kCB-h\widetilde D(g_kCB).
\]

Here \(B\) runs over every independent bond
\(I_k=T^{(k)}\setminus\{b_0(c)\}\). Because the correction is supported on the
selected \(b_0(c)\) bonds, \(B'(b)=g_kB(b)\) for each \(b\in I_k\); the fixed
Eq. (2.9) cutoff is therefore exactly \(g_k|B(b)|<\varepsilon_1\) on the whole
independent-bond cube.

RG II, [*Renormalization group approach to lattice gauge field theories II:
Cluster expansions*](https://doi.org/10.1007/BF01239022), p. 6,
Eq. (1.20), proves throughout this cube that

\[
|B'|
\le O(1)g_k|B|
+4C_2\bigl(O(1)g_k|B|\bigr)^2
\le C_1g_k|B|
<C_1\varepsilon_1,
\]

with \(C_1\) absolute. The preceding paragraph states uniform analyticity and
bounds on the admitted \(U,J\) domain; p. 7 then chooses
\(e^{32\kappa_1}\varepsilon_1\) below an absolute constant and imposes the
remaining fixed smallness inequalities. Lemma 1, p. 9, Eq. (1.34), uses the
same complete domain, and Section 2, pp. 12ff., integrates over all
independent bonds. Thus the Eq. (1.20) support-containment and analytic-domain
bounds keep every point of the complete fixed-cutoff cube on this near-identity
branch in one logarithm/gauge/analytic chart, uniformly in volume, scale, and
admitted background for fixed RG parameters. This uniformity is only the
printed containment/domain estimate; it is not a determinant or coarea-mass
bound.

This is **not** a global theorem about the unrestricted raw group-delta fiber.
The logarithmic near-identity branch has already been selected, and the papers
do not exclude remote group roots after that restriction is forgotten. Nor do
they print a volume-independent scalar determinant or total raw-mass lower
bound. The chart statement can support a named pointwise branch kernel; its
normalization, Borel/covariance properties, and distinction from the
unrestricted transform must remain explicit.

### Constraint reduction is not a gauge quotient

RG I's independent-bond integral still has the full regular-fiber dimension.
The paper does not impose a gauge delta or divide by a residual gauge volume:

- Eqs. (0.14)–(0.16), pp. 254–255, insert an exact orbit-normalized
  exponential gauge weight. The normalized gauge Haar integral is one; the
  text explicitly avoids gauge delta functions.
- Eq. (2.10), pp. 266–267, has exponential-coordinate Haar density
  \(\sigma(B')\), the averaging constraint
  \(\delta(\widetilde Q(B'))\), and the fixed cutoff. The delta elimination
  removes exactly one \(\mathfrak g\)-variable \(B'(b_0(c))\) per coarse bond,
  leaving
  \[
  (\#\text{ fine bonds}-\#\text{ coarse bonds})\dim G,
  \]
  the full regular-fiber dimension. Gauge directions remain integrated.
- The Eq. (2.12) determinant is the nonlinear constraint-coordinate
  Jacobian, not a Faddeev–Popov determinant. Equation (2.16) states invariance
  of the resulting integrand and measure under the displayed coarse gauge
  transformations.
- The normalized Gaussian \(d\mu_{C^{(k)}(W)}(B)\) in Eqs. (2.12)–(2.13) is a
  reference measure after logarithmic coordinates, constraint elimination,
  scaling, quadratic extraction, and normalization. It is not by itself the
  raw Haar/group-delta fiber law.

Consequently, the intrinsic coarea restriction in Note 0008 is a legitimate
pointwise raw representative on the selected branch, but matching it term by
term to the later Gaussian-weighted formula requires all Haar densities,
normalizations, scaling factors, and coordinate Jacobians. No such matching is
silently assumed.

### Patchwise background dependence and covariance

The pointwise branch can be organized over one background patch without
promoting it to a global disintegration.

- The variational paper's Section G, Eq. (181), p. 307, and Proposition 9
  provide one local analytic gauge-fixed background branch and its exact
  covariance under \(\widetilde u\), the lift constant on the prescribed
  blocks and agreeing with the coarse transformation at their representatives.
- Composing that branch with RG I Eqs. (2.2)–(2.4), the selected coefficient
  inverse after Eq. (2.10), and the unique analytic straightening makes
  \(h_W\), \(C_W\), \(\widetilde D_W\), and the reconstructed fine branch jointly
  real analytic after shrinking to a relatively compact patch. RG II
  Eq. (1.20) keeps the complete closed fixed cube in the common domain.
- The correction is supported only on the selected (b_0(c)) bonds, so the
  independent coordinates and their sharp cutoff are identical for every
  background in the patch. Parameter differentiation therefore has no moving
  cutoff boundary.
- RG I Eq. (2.16), p. 269, states that every expression in Eq. (2.12), together
  with its measure, is invariant under the displayed real coarse gauge
  transformations; the cutoff is invariant because the induced adjoint maps
  are local orthogonal transformations.

[Note 0009](../../research/notes/0009-parameterized-fixed-cube-kernel.md)
records the finite-dimensional consequence for the intrinsic coarea
restriction: a positive finite Borel kernel on one relatively compact patch,
real-analytic analytic-test integrals, local holomorphic test-integral
continuations, and exact real-gauge pushforward covariance between
equivariantly transported charts. It does not supply arbitrary-Borel-set
continuity, a positive complex measure, global compatibility between unrelated
patches, or a termwise normalization match to the Eq. (2.12) Gaussian law.

[Note 0010](../../research/notes/0010-exact-rg-coordinate-law.md) therefore
names the exact normalized Eq. (2.13) Gaussian/cutoff coordinate law as a
separate probability. It retains the complete Eq. (2.12) exponent and every
coordinate-dependent determinant, proves its patch-local analytic-test and
real covariance consequences, and labels its first jet
\(\mathcal J_f^{\rm RG}\). This operational law is not called the intrinsic
coarea conditional or unrestricted raw-fiber conditional absent a complete
density ledger.

[Note 0011](../../research/notes/0011-one-mark-mayer-seam.md) inserts one real
plaquette source into that exact coordinate law. It proves the fixed-background
split, bounded centered mark, and finite Mayer identity at the seam immediately
after RG II Lemma 2. It does not itself localize the mark.

[Note 0012](../../research/notes/0012-rooted-plaquette-localization.md) uses RG
II Eqs. (1.9)--(1.10), (1.17), (1.21), and (1.34), together with RG I's
pp. 265--266 exponential relative-field reconstruction, to prove an exact
root-connected mixed-difference decomposition for one centered plaquette mark.
Cauchy decay on \(|s(\Delta)|\le e^{\kappa _1}\) and a bounded-degree animal
count give a cube-count norm uniform over plaquettes interior to the fixed
partition under an explicit polydisc-versus-entropy condition. The mark is
only linear-small in \(B\): RG
II Eqs. (1.37)--(1.40) concern a specially subtracted source-free Wilson
remainder, so their cubic gain is not transferred. The result is local only in
independent \((U,J,B)\) variables and leaves shifted roots, the \(d_k\)-norm
upgrade, full-partition Euclidean covariance, minimizing-background pullback,
and connected marked expansion open. [Note
0013](../../research/notes/0013-rooted-dk-norm.md) subsequently uses RG I's
p. 257 shortest-tree definition \(d_k(Y)\le m(Y)\), RG II Eq. (1.32), and the
source-safe hierarchy consequence and explicit repository margin
\(\delta\kappa>\log64\) to close the standard fixed-partition
\(d_k\)-weighted norm. The numerical threshold is not attributed to the paper;
the exact leading prefactor dropped by the available Eq. (1.32) text layers,
shifted roots, the pullback, and the connected expansion remained open at that
stage. [Note
0014](../../research/notes/0014-equivariant-shifted-roots.md) subsequently
covers every plaquette with the RG-admitted \(L\)-spaced shift orbit for
\(M=L^m\), \(m\ge2\), retaining the same weighted norm after normalization.
RG I's symmetry restriction preceding Eq. (2.17), its field pullback, and the
post-Eq. (2.18) fluctuation transformation support transport only under the
subgroup preserving the next coarse lattice. Exact intermediate weakening is
obtained by a repository finite-stabilizer average, not quoted from the paper.
Unit translations, one-fixed-partition cluster compatibility, the pullback,
and the connected expansion remained open at that stage. [Note
0015](../../research/notes/0015-fixed-patch-physical-composition.md)
subsequently composes the shifted family on one common holomorphic physical
\((U,J)\) chart. It preserves the exact identity,
fluctuation locality and centering, transported real-chart covariance, and the
zeroth-order \(d_k\) norm, and records the complete \(U\)-and-\(J\) chain rule.
[Note 0016](../../research/notes/0016-auxiliary-j-cauchy-tubes.md) corrects the
former separate \(J\)-lift hypothesis: RG I Eqs. (1.8), (1.10), and
(1.15)--(1.16) define the physical auxiliary field as the finite-stencil
holomorphic equivariant map
\(\mathscr J_\xi(U)=D_U^{\xi *}\xi^{-2}\pi\operatorname{im}(dU)\). RG I
Eqs. (3.10)--(3.11) reduce its first differential to the covariant Laplacian
term plus the derivative of a local remainder. Note 0016 also obtains
conditional independent-variable activity derivative norms from full complex
Cauchy tubes at fixed regulator. [Note
0017](../../research/notes/0017-strict-j-margin-metric-pullback.md) uses RG
I's separate strict smaller physical representative domain to obtain a
direct-\(J\) collar under a frozen hierarchy, then proves the source-density
kernel sum and a homogeneous-layer physical pullback for the auxiliary-\(J\)
chain-rule summand. Note 0018 proves that full naive raw and \(\xi\)-scaled
bond-sup \(U\) collars collapse and records the conditional RG-scaled
replacement. Note 0019 proves a forward all-layer auxiliary-\(J\) pullback
only under explicit seam-aware ownership, source-admissible interface,
exact tree-lift, support-halo, mesh, and common-chart premises; those
premises are not imported source theorems. [Note
0020](../../research/notes/0020-one-mark-ursell-identity.md) separately proves
the exact one-mark Ursell algebra and a conditional pinned bound for one fixed
hard-core gas. It keeps the \(1/n!\) distinguished-slot factor, repeated
labels, the wall-contact compatibility convention, and each shifted branch
separate. [Note
0021](../../research/notes/0021-one-mark-section2-factorization.md)
subsequently constructs the exact decorated post-conditioning mark and unique
marked-component factorization on one compatible fixed partition. Neither
note imports a marked Lemma 3. The scaled nonlinear \(U\) pullback, uniform
realization of Note 0019's geometry, actual fixed-partition marked estimate,
hull crosswalk, shifted synchronization, convergence, and physical connected
estimate remain open.

## Regular configurations and gauge chart

T. Bałaban, [Spaces of regular gauge field configurations on a lattice and
gauge fixing conditions](https://doi.org/10.1007/BF01466594), **CMP 99**
(1985), 75–102:

- Eqs. (1.3)–(1.10), pp. 77–78, define nested domains, buffer geometry, the
  gauge-invariant plaquette-curvature bound, and covariant regularity bounds.
  These are small/regular-field assumptions, not bare-coupling estimates.
- Eqs. (1.13)–(1.14), p. 78, fix block averages and identify the subgroup of
  transformations equal to the identity on the coarse set.
- Eq. (1.27), pp. 80–81, defines the generalized Landau chart only for a small
  relative field. The surrounding discussion explicitly warns that a naive
  once-per-orbit global statement may fail. Eqs. (1.28)–(1.29) show that the
  averaged constraints do not themselves define a group orbit.
- Theorem 2, p. 83, under Eqs. (1.33)–(1.39) and sufficiently small
  \(\alpha_0+\alpha_1\), constructs a unique constrained transformation into
  the stated Landau chart with first/second regularity bounds. Constants have
  the dependencies listed there. This is local uniqueness in the admitted
  regular region, not a global solution of the Gribov problem.
- Theorem 8, p. 101, permits the inhomogeneous gauge condition in Eq. (1.146)
  for a sufficiently small right-hand side in the stated weighted norm.
- Proposition 6 and Eqs. (1.136)–(1.138), pp. 97–100, bridge the
  gauge-invariant regularity conditions to local gauges with the field and
  derivative bounds required by the propagator paper. This still remains a
  local small-field statement.

Program 002 may use this chart only with every domain and smallness hypothesis
carried forward.

## Background propagators

T. Bałaban, [Propagators for lattice gauge theories in a background
field](https://doi.org/10.1007/BF01240355), **CMP 99** (1985), 389–434:

- Eqs. (3.35)–(3.38), pp. 396–397, require a local gauge in which the
  background and its derivatives obey scale-dependent bounds, with
  \(M\alpha_0\) small, and define a complex background-field neighborhood.
- Theorems 3.1–3.3, pp. 397–399, give multiscale regularity and exponential
  decay for the listed propagators/inverses. Their constants are independent
  of the admissible domain sequence, with the parameter dependencies stated
  in the paper.
- Theorem 3.4, p. 400, gives analytic dependence in the complex
  **background-gauge-field** neighborhood. It is not analyticity in an
  external scalar plaquette source.
- Theorem 3.12, pp. 423–424, extends the stated regularity, random-walk, and
  positivity properties to additional propagators under both background
  conditions, with the exception explicitly noted there.
- Theorem 3.14, pp. 426–427, controls changes caused by modifying domains away
  from the observation region.
- Theorem 3.15 and Eq. (3.187), p. 432, give exponential decay of the
  unit-lattice fluctuation covariance with constants depending on \(d,L\).
  This is an ultraviolet/locality estimate, not a physical Yang–Mills mass
  gap.

Section E, pp. 427–428, does introduce an arbitrary Lie-algebra-valued **bond**
source \(g\) in the finite-dimensional Gaussian defining \(C^{(k)}\); Eqs.
(3.155), (3.157), and (3.158) give its generating functional/covariance. This
legitimizes source derivatives for that one Gaussian integral. It is not the
scalar composite plaquette source coupled to the full interacting Wilson
measure, and it supplies no interacting source-marked cluster theorem.

### Multiscale metric and exponential convolution

T. Bałaban, [*Propagators and renormalization transformations for lattice
gauge theories II*](https://projecteuclid.org/download/pdf_1/euclid.cmp/1103941783),
**CMP 96** (1984), 223–250, supplies the metric behind the variational
paper's decay notation. Eqs. (2.45)--(2.48), pp. 230--231, use
\(s_j=L^j\eta\) and a shortest multiscale contour measured in local scale
units to define \(d_{\mathcal B}\). Equation (2.53) identifies the associated
cell as \(\Delta(y)=B^j(y)\), and Eq. (2.54) gives the triangle inequality.
Lemma 2.1, Eqs. (2.59)--(2.63), pp. 233--234, gives the required exponential
summation/convolution bound under the paper's stronger separation condition.

This is not the rooted polymer distance \(d_{k,\sigma}\) used in Notes
0013--0017. Note 0017 proves the source-measure cancellation and dual
exponential sum, and on one matched homogeneous layer compares the
multiscale diameter to the contained-tree metric with an \(M\) factor. It
also shows that a reverse comparison does not extend uniformly: travel in a
layer \(r-r_0\) levels coarser has fixed-scale/multiscale ratio
\(L^{r-r_0}/M\). The reciprocal ratio helps, rather than obstructs, the
forward inequality used in the pullback. That forward cross-layer theorem
still does not follow from the audited definitions because interface charges
and generic shifted-cell alignment have not been controlled.

## Variational minimizer and analytic branch

T. Bałaban, [The variational problem and background fields in renormalization
group method for lattice gauge
theories](https://doi.org/10.1007/BF01229381), **CMP 102** (1985), 277–309:

- Theorem 1, p. 279, proves existence of a minimal orbit for regular
  coarse data and uniqueness of the critical orbit inside the stated regular
  space, with local regularity bounds (9)–(10). It does not initially define a
  global single-valued field \(V\mapsto U_k(V)\).
- Section G, pp. 305–309, explicitly calls \(U_k(V)\) multivalued before a
  gauge condition is fixed. It constructs a local analytic branch for small
  relative coarse fields.
- Eq. (181), p. 307, gives the gauge-covariance rule for that branch.
- Proposition 9, p. 309, summarizes the analytic extension, its determining
  equations, regularity bounds, and analytic dependence on an external regular
  **gauge background**. Again, this is not scalar-source analyticity.
- Eq. (182) defines the first functional derivative of the Landau-gauge
  relative minimizer \(\mathcal H(B)\) with respect to the coarse relative-log
  field.
  For \(x\in\Delta(y)\), \(y\in\Lambda_j\),
  \(y'\in\Lambda_{j'}\), Eq. (190) bounds the derivative itself, its spatial
  gradient, its \(\zeta\)-weighted \(\beta\)-Hoelder gradient, and its
  \(D_{U_k}^{\eta *}D_{U_k}^{\eta}\) and
  \(\Delta_{U_k}^{\eta}\) images. The five scale factors are respectively
  \((L^j\eta)^{-1}\), \((L^j\eta)^{-2}\),
  \((\|\zeta\|_\beta^\xi+|\zeta|)(L^j\eta)^{-2-\beta}\),
  \((L^j\eta)^{-3}\), and \((L^j\eta)^{-3}\), all multiplied by
  \((L^{j'}\eta)^{-d}\exp[-\delta_0d(y,y')/8]\); the third row assumes
  \(\operatorname{supp}\zeta\subset\widetilde\Delta(y)\). [Note
  0004](../../research/notes/0004-fixed-background-source-jet.md) records the
  indexed display. Combined with RG I's exact local auxiliary-field formula,
  Eq. (190) gives qualitative exponential decay of the physical \(J\)
  derivative on one fixed compact chart, as recorded in Note 0016. Note 0017
  composes this kernel with the direct-\(J\) activity derivative using
  \(\ell^\infty\)-\(\ell^1\) duality, avoiding a polymer-volume factor, and
  proves a conditional one-layer \(d_k\)-summed result. It is still not the
  full \(U\)-and-\(J\) physical derivative or a connected-expectation bound.

Because \(\mathcal O_f(U)=4\sum_p f_ps(U_p)\) is gauge invariant, its value on
the source-free minimizing orbit is well defined without selecting a
representative. Analyticity/locality as a function of \(V\), however, must use
one of the proved local gauge-fixed branches and its exact domain.

The derivative of a source factor evaluated on a **fixed source-free**
background is simply \(\mathcal O_f(U_1(V))\). If the saddle itself is
re-minimized after adding the source, differentiability of the gauge-fixed
branch and invertibility of its constrained Hessian must be invoked; the
source-free existence theorem alone does not license that step.

## Resulting exact first hard interface

Note 0003 gives, for the raw conditional measure,

\[
-\left.\partial_z\log\mathcal R_{x,z,f}(V)\right|_{z=0}
=\mathbb E_{\nu_{x,V}}[\mathcal O_f].
\]

The variational paper identifies the source-free background term
\(\mathcal O_f(U_1(V))\). The first genuinely unproved quantity is therefore

\[
\mathcal J_f(V)=
\mathbb E_{\nu_{x,V}}[\mathcal O_f]
-\mathcal O_f(U_1(V)).
\]

The next theorem must give \(\mathcal J_f\) a localized, gauge-invariant
polymer representation on the exact regular domain, classify all projected
profile/operator mixing, and prove cutoff-/volume-/location-uniform bounds.
None of the four imported papers states that theorem.

## Nonclaims and remaining checks

- The group-delta kernel still needs a precise positive disintegration on each
  admitted coarse fiber before it is used as a measure-theoretic dependency.
- The exact norms/constants of every imported theorem have not yet been
  transcribed into machine-checkable definitions.
- The fixed-threshold small-field branch does not cover the large-field
  complement.
- Source-free background analyticity does not imply a regulator-uniform
  zero-free scalar-source disk.
- Exponential decay of background propagators is not a continuum correlation
  decay theorem or a Hamiltonian mass gap.
