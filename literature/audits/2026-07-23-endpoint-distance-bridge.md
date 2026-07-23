# Contained-tree to multiscale-endpoint audit

Date: 2026-07-23

Purpose: separate the metric facts imported by YM-RG-028 from the
repository's periodic endpoint and support-anchor corollaries.

## Imported source facts

1. RG I p. 257 defines \(d_k(Y)\) by the side-length-normalized length of a
   shortest tree graph contained in \(Y\) and meeting its localization cubes.
   Note 0013 already records the source-convention-safe singleton and
   cube-edge consequences used by this repository.
2. Propagators II Eqs. (2.45)--(2.54) define the physical multiscale cell
   labels and admissible-contour metric, identify the associated blocks, and
   give the triangle inequality.
3. Neither paper prints Note 0019's coordinatewise periodic ownership map,
   its nearest-neighbor constant \(c_{\rm nn}=d(L+2)+1\), a discrete
   fine-bond realization of the contained tree, or YM-RG-028's endpoint
   theorem.

Primary records:

- [RG I](https://doi.org/10.1007/BF01215223)
- [Propagators II](https://doi.org/10.1007/BF01240221)

## Repository quotient-geometry corollary

For a path between two fine torus sites, lift the complete path to the
periodic cover. Its endpoint displacement is in \(\eta\mathbb Z^d\), and

\[
\operatorname {dist}_\eta(z,z')
\le
\eta^{-1}\lVert\widetilde z'-\widetilde z\rVert_1
\le
\sqrt d\,\eta^{-1}\ell_2(\gamma).
\]

For a shifted polymer with side-\(Mb\eta\) cubes, use an
\(\varepsilon\)-minimizing continuous contained tree only to bound the
displacement between two tree-contact points. The two anchor halos and two
within-cube pieces are already rectilinear. This gives

\[
\operatorname {dist}_\eta(z_p,z_x)
\le
\sqrt d\,Mb\,d_{k,\sigma}(Y)+2dMb+h+h_q.
\]

Only after this endpoint estimate is proved is Note 0019's
fine-neighbor \(\rho\) theorem applied to a separate fine-lattice geodesic.
No value of \(\rho\) is assigned to a continuous tree point.

The geometric localization cubes are closed supports. They are distinct from
the half-open owned cells used solely to make \(\rho\) single valued. The
covering lift handles periodic seams, and the
\(\varepsilon\)-minimizing formulation does not assume attainment.

## Repository support corollary

Note 0012's repository conclusion after Eq. (8) says that the first-stage
marked activity is local in the independent \((U,J,B)\) variables in the
interior of \(Y\), in the RG-II decoupled-variable sense. If the full
oriented independent \(J\)-bond lies in \(\operatorname {int}Y\), anchoring
it at a deterministic base site gives \(h=0\). The strictly interior
plaquette base site gives \(h_q=0\).

This does not audit the external-\(J\) dependency set of completed Section-2
connected coefficients.

## Exact boundary

- The source contained-tree and multiscale-metric definitions are imported.
  The quotient lift, \(\sqrt d\) conversion, endpoint constants, support
  anchors, and removal of \((\mathrm H_T)\) are repository corollaries.
- Every interface and admissibility clause of Note 0019's
  \((\mathrm H_\rho)\) remains assumed.
- Bounded mesh ratio and common representative, chart, kernel, Cauchy, and
  activity constants remain necessary for the conditional all-layer
  auxiliary-\(J\) norm.
- No completed-gas support theorem, nonlinear \(U\) pullback, large-field
  estimate, RG iteration, continuum construction, infrared conclusion, or
  mass gap is imported or proved by this audit.
- This audit is not independent human review.
