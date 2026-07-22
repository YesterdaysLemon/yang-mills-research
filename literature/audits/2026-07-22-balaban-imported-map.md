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
