# Audit: Balaban kernels and the support-anchored physical-\(J\) pullback

Date: 2026-07-23

Claim audited: YM-RG-032

Status: primary-source kernel inputs already pinned; the support-set
reweighting and sharpness model are repository deductions; all uniform
kernel/chart premises remain explicit

## Immutable source record

The official Project Euclid copy of *Propagators and renormalization
transformations for lattice gauge theories II* was inspected directly and
is retained locally as `tmp/pdfs/propagators-ii.pdf` with SHA-256

```text
6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F
```

Stable primary records:

- [The variational problem and background fields in renormalization group
  method for lattice gauge
  theories](https://doi.org/10.1007/BF01229381);
- [Propagators and renormalization transformations for lattice gauge
  theories II](https://doi.org/10.1007/BF01240221).

The variational-paper derivative and its five Eq. (190) rows were directly
transcribed in Note 0004 and audited in the imported-map audit. The
Propagators-II separation and exponential-summation input was directly
transcribed in Note 0017. YM-RG-032 changes neither source formula.

## Exact imported kernel facts

For \(x\in\Delta(y)\), \(y\in\Lambda_j\), and
\(y'\in\Lambda_{j'}\), Proposition 9 Eq. (190) has the common factor

\[
(L^{j'}\eta)^{-d}
\exp\!\left[-\frac{\delta _0}{8}d_{\mathcal B}(y,y')\right].
\]

The five printed rows control the background derivative, its spatial
gradient, its weighted Holder gradient, and two covariant-Laplacian forms.
Notes 0016--0017 combine only the rows required by the exact auxiliary-field
differential. In the source-density normalization

\[
\mu(j',y')=(L^{j'}\eta)^d,
\]

the inverse density in Eq. (190) cancels \(\mu\). For

\[
0\le\gamma<\frac{\delta _0}{8},
\qquad
\alpha_\gamma=\frac18-\frac{\gamma}{\delta _0}>0,
\]

and under the strengthened separation condition used by Propagators II
Lemma 2.1, the remaining exponential sum is bounded by
\(c_1(\alpha_\gamma)\).

The output layer \(j\) controls

\[
E_J(j)
=C_{J,4}(L^j\eta)^{-3}
+C_{J,2}(L^j\eta)^{-2}
+C_{J,1}(L^j\eta)^{-1},
\]

whereas the input layer \(j'\) controls the source measure. Those two roles
must not be interchanged.

Equation (190) is printed in component/operator norms. YM-RG-032 explicitly
absorbs one fixed finite-dimensional equivalence factor into \(C_\chi\) so
that the kernel and the completed direct-\(J\) derivative use the same block
norm. Its displayed source-label sums suppress the finite spacetime-direction
and Lie-algebra component index: for each such component, the kernel is an
element of the \(J(b)\) block, the completed coordinate functional returns a
scalar, and the fixed component multiplicity is absorbed into \(C_\chi\).
Uniformity of this factor, \(C_\chi\), the local conversion constants, and
\(\overline E_J^{\rm conn}\) over the completed family is assumed, not
deduced from the source.

## What the source does not provide

Neither primary paper defines the completed coefficient
\(\widehat{\mathcal C}_p^+(s,R)\), its structural derivative support, the
active-label set \(S_{p,s,R}\), or the support-anchored norm. Those enter only
after the repository's marked RG-II and connected constructions.

The source also does not prove Note 0019's
\((\mathrm H_\rho)\), the coordinatewise periodic ownership map used there,
its interface compatibility, the output/localization mesh comparison, or a
uniform endpoint inequality from the marked plaquette to every active
external-\(J\) label. The displayed Propagators-II metric definitions and
triangle inequality do not supply those identifications.

## Repository deduction checked

Note 0029 defines the structural support

\[
I^{\rm conn}_{J,p,s}(R)
=
\{b:D_{J(b)}\widehat{\mathcal C}_p^+(s,R)
\text{ is not identically zero}\}.
\]

For each active coordinate, YM-RG-032 retains only the tagged Eq. (190)
output label \(\widetilde y_b=(j_b,y_b)\). On the disjoint tagged label
space it uses the pulled-back pseudometric
\[
d_{\widetilde{\mathcal B}}
\bigl((j,y),(j',y')\bigr)
:=d_{\mathcal B}(y,y').
\]
It forms

\[
S_{p,s,R}
=
\{\widetilde y_b:b\in I^{\rm conn}_{J,p,s}(R)\}.
\]

For every active \(b\),

\[
d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')
\le
d_{\widetilde{\mathcal B}}(\widetilde y_b,\widetilde y').
\]

This tautological inequality can replace the old root triangle before the
unchanged Eq. (190) convolution is applied. Finite-dimensional
\(\ell^\infty/\ell^1\) duality then turns the active-coordinate sum into the
already proved completed derivative norm. No ownership map, neighbor
estimate, interface route, mesh ratio, endpoint allowance, or spend from
the polymer exponent is used.

The result is therefore a genuine support-anchored hybrid norm. It measures
the rooted polymer cost in \(d_{k+1,s}\) and the source tail from the nearest
active \(J\) label in \(d_{\mathcal B}\). It is not a pure
marked-plaquette-to-source estimate.

## Endpoint boundary and sharpness

The stronger plaquette-rooted norm follows from the aggregate condition

\[
\sup_{\widetilde y\in S_{p,s,R}}
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y)
\le A d_{k+1,s}(R)+B
\]

with exponent budget \(a_*+\gamma A\le\kappa\). This condition is a
less-structured proof obligation than \((\mathrm H_\rho)\): it requests only
the final endpoint inequality.

The one-coordinate countermodel in Note 0032 verifies the logical boundary.
A unit derivative and a kernel concentrated at its own active label obey all
unrooted tube and convolution bounds, while moving that label arbitrarily far
from the tagged root \(\widetilde q_{p,s}\) makes the rooted exponential norm
diverge. This is a
countermodel to an inference from the retained inequalities, not a claim
about the actual Balaban geometry.

The endpoint condition is therefore worst-case sharp as a geometry-only
route from the unweighted completed derivative norm. It is not called
logically minimal for a particular coefficient family, because
coefficient-weighted endpoint decay can substitute for it.

## Exact nonclaims

- Empty structural support is removed before the set distance is formed.
- The coordinatewise dual identity is asserted only at finite regulator.
- Common source-kernel and chart constants remain hypotheses.
- The physical \(U\) pullback and proof of
  \((\mathrm H_{\rm rc})\) remain open.
- No nonzero-source polymer disk, unrestricted raw-law comparison,
  large-field estimate, RG iteration, continuum construction,
  Osterwalder--Schrader reconstruction, infrared decay, or Yang--Mills mass
  gap is imported or proved.
- This audit was performed by AI agents and is not independent human review.
