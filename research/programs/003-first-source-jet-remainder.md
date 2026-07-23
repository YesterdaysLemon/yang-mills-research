# Program 003: the first source-jet fluctuation remainder

Claim ID: `YM-RG-004`

Status: Open theorem specification

Evidence: E0

Initial group: \(SU(2)\)

Novelty: not claimed

## Frozen setup

Use the Euclidean-symmetric RG I Eq. (0.12) average and the raw group-delta
transform selected in the [imported-map
audit](../../literature/audits/2026-07-22-balaban-imported-map.md). Retain the
odd-\(L>11\) geometry and use the fixed-\(\varepsilon_1\) small-field cutoff,
not the coupling-dependent alternative, for this first theorem.

The unrestricted raw group-delta transform remains a separate object: ordinary
disintegration only gives almost-everywhere conditional probabilities, and the
audited sources do not exclude remote logarithmic branches. This theorem is
therefore explicitly restricted to RG I's selected near-identity fixed-cutoff
branch rather than silently identifying that branch with the unrestricted
fiber.

[Note 0008](../notes/0008-full-fixed-cutoff-branch.md) uses RG II
Eqs. (1.19)–(1.20) to prove that the **complete** Eq. (2.9)
independent-bond cube stays inside one regular analytic chart. For each finite
regulator and admitted real coarse field \(V\), it defines the intrinsic
pointwise finite nonzero positive branch measure
\(K_k^{\rm chart}(V,dU)\).

[Note 0009](../notes/0009-parameterized-fixed-cube-kernel.md) proves that on
one named relatively compact Proposition 9 patch these measures form a Borel
kernel, analytic tests have real-analytic integrals and local holomorphic
continuations, and real coarse gauge transformations push the kernel forward
between equivariantly transported charts. It does not build a compatible
global atlas or identify the intrinsic density term by term with RG I
Eq. (2.12).

[Note 0010](../notes/0010-exact-rg-coordinate-law.md) separately names the
exact normalized probability law of RG I Eqs. (2.12)–(2.13), retaining its
Gaussian, cutoff, full fluctuation exponent, and every coordinate-dependent
Jacobian:

\[
\nu_{k,V}^{\rm RG}(dB)=
\frac{
\chi_k(B)e^{\Psi_k^{\rm RG}(V,B)}
d\mu_{\Gamma_k(V)}(B)
}{Z_k^{\rm RG}(V)}.
\tag{1}
\]

This program now adopts (1) as its operational law because RG II's
fluctuation/cluster construction acts on that printed coordinate integral. It
does **not** identify (1) with a normalized intrinsic-coarea law or an
unrestricted raw-fiber conditional. Only factors constant in \(B\) and the
observable source cancel projectively.

The coordinate branch, cutoff, and full source-free weight in (1) are frozen
at source zero, so they are independent of \(z\) and \(f\). They may still
depend on the source-free coupling/background construction; the
constant-profile coupling identity must continue to be stated for the
coupling-independent raw transform, not assumed for (1).

[Note 0007](../notes/0007-projective-source-kernels.md) shows that no
volume-independent lower bound on the raw branch mass is needed. Note 0010
proves positivity, patch-local analytic-test regularity, real gauge covariance,
and the explicit common zero-free source disk for (1). The remaining theorem
must prove marked-polymer locality for this exact normalized RG coordinate law.

For a real plaquette profile \(f\) supported in one coarse block and normalized
by Program 002's \(\|f\|_{C^6_{\rm disc}}\le1\), let

\[
\mathcal O_f(V,B)=4\sum_p f_p s(\mathscr U_k(V,B)_p).
\]

Note 0010 gives the exact RG-coordinate first jet as a finite-dimensional
expectation, while Note 0004 gives the fixed-background term on the unique
minimizing orbit. Define their deliberately labeled difference

\[
\mathcal J_f^{\rm RG}(V)=
\mathbb E_{\nu^{\rm RG}_{k,V}}[\mathcal O_f(V,B)]
-\mathcal O_f(U_1(V)).
\]

Note 0011 settles its exact background split and one-mark Mayer algebra. Note
0012 proves the exact rooted decomposition and a conditional cube-count norm,
uniform over plaquettes interior to one fixed partition, in the independent
RG-II variables. Note 0013 upgrades it to the conditional
\((1-2\delta)\kappa d_k\)-weighted norm on the standard \(M\)-cube branch under
an explicit entropy margin. Note 0014 supplies an RG-admitted shifted-family
cover for every plaquette and coarse-lattice-preserving transport. The
conditional fixed-chart composition, exact \(U\)-and-\(J\) chain rules, and
zeroth-order norm are supplied by Note 0015. Note 0016 identifies the exact
physical auxiliary field, reduces its differential to the Eq. (190)-controlled
background derivative plus a local remainder, and gives conditional
independent-variable derivative norms on fixed-regulator complex tubes. Note
0017 supplies a strict direct-\(J\) representative collar, the dual
Eq. (190) source convolution, and a conditional homogeneous-layer pullback
for the auxiliary-\(J\) chain-rule summand. Note 0018 proves that naive raw
and \(\xi\)-scaled bond-sup \(U\) collars collapse and isolates the necessary
RG-scaled replacement hypotheses. Note 0019 proves a conditional all-layer
\(J\)-summand extension under explicit interface, tree-lift, support, mesh,
and common-chart premises. Note 0020 proves the exact one-mark Ursell formula
and a conditional pinned cluster bound for one fixed hard-core gas, and shows
that bare shifted marks cannot be mixed without branch synchronization or a
proved common-gas embedding. Note 0021 constructs the exact decorated
post-conditioning activity, unique marked-component factorization, and finite
hard-core numerator on one compatible fixed partition. Note 0022 proves that
under common \(L^1\)-holomorphy and a joint majorant, the complete marked
weakening integrand can be estimated by one contour without extra
derivative-allocation entropy, and with the ordinary radius price if that
radius is shared. It isolates a positive seed-dependent kernel. Note 0023
proves a literal-union hull,
volume-uniform animal entropy, and an explicit sufficient pinned
Kotecky--Preiss/hull-weight package for a separately declared standard
closed-cube gas. Note 0024 identifies the final connected ordinary RG-II gas
with that model and supplies a displayed-hierarchy-compatible ordinary
KP-smallness window. Note 0025 corrects the source variable map and proves
the fixed-term marked bound with zero relative-moment cost. Marked-seed
kernel decay, tree/scale gluing, the decorated marked norm, differentiated
absolute convergence, and shifted synchronization remain open. The scaled
\(U\) pullback, uniform
realization of Note 0019's premises, and full physical coarse-field
derivative/quasilocal norm,
the summed fixed-partition marked norm, unit-translation covariance, and
a physical convergent connected marked estimate are the first parts not
settled by those auxiliary lemmas or the imported source-free theorem.

## Target theorem

On one named relatively compact admitted regular coarse-field patch, derive a polymer
representation

\[
\mathcal J_f^{\rm RG}(V)=M_f(V)+\sum_X K_{X,f}(V),
\qquad
M_f=\Pi_{\rm rel}\mathcal J_f^{\rm RG},
\]

with all of the following properties.

1. **Complete projection.** Classify every first-jet relevant/marginal
   operator and every allowed position/orientation mixing of \(f\); do not
   assume a scalar energy renormalization factor.
2. **Gauge invariance.** The projected term and each localized activity are
   invariant under coarse gauge transformations.
3. **Quasilocality.** The profile-mixing kernels, projected coefficients, and
   polymer activities have summable exponential decay away from
   \(\operatorname{supp}f\), in explicitly copied Bałaban norms.
4. **Uniformity.** Constants are independent of torus size, cutoff scale, and
   source location for fixed admitted \(g,L\) and normalized \(f\). These are
   normalized cumulant/polymer constants, not a lower bound on the raw product
   cutoff mass.
5. **Analytic domain.** The coarse-field analyticity domain is exactly the
   gauge-fixed regular patch supplied by the imported theorems; no global
   logarithm or gauge slice is used.
6. **Source-free compatibility.** The proof derives the representation by
   differentiating a source-inserted construction or by a justified insertion
   into the cluster expansion. It may not infer source bounds merely by
   differentiating a source-free final estimate.

This target covers one source derivative in the fixed small-field branch only.
It deliberately excludes the second source derivative, coupling-dependent
cutoffs, the large-field complement, RG iteration, continuum limits, and
infrared conclusions.

## Available inputs

- exact finite-regulator conditional-cumulant identity (Note 0003);
- unique minimizing orbit plus analytic gauge-fixed branch (Note 0004), with
  the variational paper's five Eq. (190) component bounds transcribed but not
  yet crosswalked uniformly to the physical activity derivative norm;
- pointwise positive fiber kernels for proper smooth submersions (Note 0005),
  conditional on proving the selected map and cutoff satisfy its hypotheses;
- RG I's local analytic constraint straightening and a positive precompact
  background-centered fiber ball (Note 0006), without full-cutoff uniformity;
- projective invariance, centered-score differentiation, and a uniform
  bounded-observable source disk once a named pointwise kernel gives a positive
  finite source-free weighted partition function (Note 0007);
- RG II's complete-cube containment and the resulting pointwise positive
  measure on the entire selected fixed-cutoff chart branch (Note 0008),
  without an unrestricted-fiber comparison;
- the patch-local Borel kernel, analytic-test regularity, local holomorphic
  continuation, and transported-chart covariance of that intrinsic branch
  measure (Note 0009), without a global compatible atlas or a termwise match
  to RG I Eq. (2.12);
- the separately named exact normalized RG-I Eq. (2.13) coordinate law, its
  fixed-domain analyticity, centered-score derivative, source disk, and real
  gauge covariance (Note 0010), without identifying it with the intrinsic or
  unrestricted raw laws;
- the exact finite-regulator background-centered mark, first-jet split, range
  bound, and one-mark Mayer identity at the RG-II Section 2 seam (Note 0011),
  without by itself supplying localization;
- the exact independent-variable rooted decomposition and conditional
  fixed-partition-interior cube-count norm for one plaquette mark (Note 0012),
  without by itself supplying shifted roots, minimizing-background pullback,
  or a connected marked expectation;
- the rooted \((1-2\delta)\kappa d_k\)-weighted norm on the standard
  wall-adjacent \(M\)-cube branch (Note 0013), under the source-safe hierarchy
  consequence and explicit added entropy margin
  \(\delta\kappa>\log64\), without a claim that this numerical threshold or the
  exact text-layer-dropped prefactor is printed as transcribed in RG II;
- the normalized RG-admitted shifted-family cover for every plaquette and
  transport under the subgroup preserving the next coarse lattice (Note
  0014), without unit-translation covariance, one-fixed-partition cluster
  compatibility, or minimizing-background quasilocality;
- the conditional fixed-chart physical composition, exact all-plaquette
  identity, fluctuation locality, centering, \(U\)-and-\(J\) chain rules,
  transported real-chart covariance, and inherited zeroth-order \(d_k\) norm
  (Note 0015), without a physical coarse-field derivative norm or connected
  bound;
- the exact finite-stencil physical auxiliary field, its holomorphy,
  covariance, and full first-differential reduction, qualitative nonuniform
  fixed-chart decay, and conditional rooted independent-variable derivative
  norms on explicit fixed-regulator tubes (Note 0016), without uniform tube
  radii/chart constants, a \(d_{\mathcal B}\)-to-\(d_{k,\sigma}\) comparison,
  the physical chain-rule convolution, or a connected bound;
- the strict representative-\(J\) collar, dual source-measure kernel sum, and
  conditional homogeneous-layer pullback for the auxiliary-\(J\) chain-rule
  summand (Note 0017), together with the raw-\(U\) collar obstruction and
  conditional scaled-collar template (Note 0018), and the conditional
  all-layer \(J\)-summand bridge (Note 0019), without a concrete RG-scaled
  \(U\) norm or a proof of Note 0019's interface, tree-lift, support, mesh,
  and uniform-chart premises;
- the exact fixed-gas distinguished-vertex Ursell identity, repeated-label
  convention, shifted-branch separation rule, and conditional pinned
  Kotecky--Preiss implication (Note 0020);
- the exact fixed-partition decorated post-conditioning mark, unique
  marked-component factorization, and finite hard-core numerator (Note 0021),
  together with the exact whole-integrand marked Cauchy reduction under
  explicit common-domain and joint-majorant hypotheses and the corrected
  conditional exponent fork (Note 0022);
- the literal-union hull, volume-uniform geometric animal bound, and explicit
  sufficient pinned Kotecky--Preiss/hull-weight conditions for the separately
  declared standard closed-cube gas (Note 0023), together with the final
  ordinary source-class/metric/species identification and explicit
  sufficient displayed-hierarchy ordinary KP window (Note 0024), and the
  source-faithful fixed-term marked contour domination with zero moment cost
  (Note 0025), but without the positive marked-seed kernel decay, tree/scale
  gluing, decorated marked activity norm, differentiated absolute
  convergence, or synchronized shifted RG construction needed for the
  physical application;
- background-propagator decay and change-of-domain estimates;
- RG I/II source-free local analytic polymer expansions.

None of those inputs supplies the displayed source-inserted polymer theorem.

## First derivation route

1. [x] Insert \(z\mathcal O_f\) through the source-independent RG-I coordinate
   changes and work with Note 0010's full fixed-cube law.
2. [x] Keep every \(B\)-dependent factor, differentiate at \(z=0\), isolate
   \(\mathcal O_f(U_1(V))\), and derive the exact one-mark Mayer identity; see
   Note 0011.
3. [x] Prove a rooted decomposition of the background-centered mark on RG II
   Eq. (1.34) with a conditional cube-count norm uniform over plaquettes
   interior to one fixed partition; see Note 0012.
4. [x] Upgrade the standard \(M\)-cube branch to the conditional rooted
   \(d_k\)-weighted norm on the standard branch
   with strict entropy slack; see Note 0013.
5. [x] Cover every plaquette by the RG-admitted shifted family and record
   transport under the subgroup preserving the next coarse lattice; see Note
   0014. Full unit-translation covariance and cluster-partition compatibility
   remain open.
6. [x] Compose the shifted family with one common holomorphic physical
   \((U,J)\) pair, prove centering and the exact chain
   rules, and preserve the zeroth-order norm; see Note 0015.
7. [x] Transcribe RG I's exact physical auxiliary field and differential, and
   use full complex Cauchy tubes to prove conditional rooted \(D_U\)- and
   \(D_J\)-operator norms at fixed regulator; see Note 0016.
8. [x] Prove the strict direct-\(J\) collar, dual Eq. (190) source
   convolution, and the auxiliary-\(J\) pullback on a matched homogeneous
   layer; see Note 0017. The note also disproves a uniform reverse
   cross-layer bound. Note 0019 proves the forward all-layer implication
   conditionally under its named geometry and uniformity premises.
9. [ ] Discharge Note 0019's interface, tree-lift, support, mesh, and
   common-chart premises for the exact shifted family; construct the nonlinear
   \(U\) collar and pullback in an RG-scaled regularity norm. Note 0018 proves
   that the naive raw alternatives cannot satisfy this step.
10. [ ] Carry exactly one rooted mark through RG II Eqs. (2.2)–(2.13), using
   Lemma 3 for the unmarked decorations, and prove the connected sum converges.
   Note 0020 settles the fixed-gas distinguished-slot algebra, including
   \(1/n!\), repeated labels, and the conditional pinned bound. Note 0021
    settles the finite fixed-partition cutoff, conditioning, weakening,
    post-polymerization image, component factorization, and hard-core numerator
    algebra. Under its explicit common \(L^1\)-holomorphy and joint-majorant
    hypotheses, Note 0022 removes an artificial product-rule multiplicity and
    reduces direct weakening to one positive kernel. Note 0023 closes the
    literal-union hull, animal entropy,
    and sufficient pinned-KP crosswalk in its declared standard closed-cube
    model. Note 0024 identifies the final connected ordinary source gas with
    that model and gives an explicit sufficient ordinary smallness window.
    Note 0025 proves the source-faithful fixed-term marked contour bound with
    zero moment loss. The marked-seed kernel decay, tree/scale gluing and
    final norm, differentiated convergence, and shift synchronization remain
    open.
11. [ ] Perform the full symmetry/Ward-identity projection on the marked first
   jet and classify all position/orientation mixing.

## Falsification tests

- A proof silently replaces \(\nu^{\rm RG}\) by the unmatched intrinsic coarea
  or unrestricted raw-fiber law.
- A later argument silently crosses unrelated background charts without an
  overlap theorem.
- A fixed cutoff still creates a boundary/source derivative term omitted by
  the derivation.
- The marked activity has an unsummable tail or a constant grows with volume.
- A profile-orientation mixing term survives outside the proposed projection.
- Gauge fixing creates a noncovariant marked activity.
- A proof uses Proposition 9 outside its local analytic patch.
- A source-free bound is differentiated without a common analytic source
  domain.

Failure of this bounded theorem would force Program 002 to change map, source
class, projection, or route. Success would still be only an auxiliary E2
small-field result and would not establish a continuum theory or mass gap.
