# Bałaban completed external-\(J\) support audit

Date: 2026-07-23

Purpose: separate the final-activity external-field locality printed in
RG II from the repository's marked, connected, shifted support corollary.

## Immutable primary records

T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field
Theories. I. Generation of Effective Actions in a Small Field Approximation
and a Coupling Constant Renormalization in Four Dimensions*,
Communications in Mathematical Physics 109 (1987), 249--301:

- [Project Euclid PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf)
- SHA-256:
  `1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A`

T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field
Theories. II. Cluster Expansions*, Communications in Mathematical Physics
116 (1988), 1--22:

- [Project Euclid PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf)
- SHA-256:
  `EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`

Page references below use printed journal pages.

## Printed source statements

1. RG I printed p. 251 defines the lattice sets induced by a continuous
   subset: its bonds are the nearest-neighbor intervals which intersect the
   subset. Printed p. 262 then defines both \(U\) and \(J\) at the bonds of a
   localization domain \(X\). Thus restriction to \(X\) means complete bond
   coordinates \(b\) with \(|b|\cap X\ne\varnothing\), not bonds wholly
   contained in \(X\) and not coordinates assigned by one endpoint.
2. At the start of RG II Section 2, printed p. 10, the paper says that dependence
   on the external gauge fields is suppressed in the following formulas.
3. Immediately after Eq. (2.9), printed p. 14, it says that \(H(Z)\) is
   “localized in the interior of \(Z\) with respect to the external gauge
   fields.”
4. Equation (2.10) factors a disconnected \(H(Z)\) over its connected
   components.
5. Equation (2.13), printed p. 14, groups each connected occurrence tuple by
   the literal equality \(\bigcup_iZ_i=X\).
6. The analyticity discussion on printed p. 15 explicitly names the
   external variables as \((U,J)\). It says the potentials extend
   analytically in \((U,J)\), the quadratic forms and covariances are
   analytic under the conditions imposed on the domain \(Z\), and the final
   activities and fixed-output sum are analytic on the stated
   \(X\)-dependent space.

Together these statements establish external-\((U,J)\) restriction locality
on the bond-intersection set and analyticity for the final unmarked activity
on one source cubulation. They do not state a plaquette mark, dual-number
coefficient, shifted family, connected first derivative, normalized branch
average, or zero-halo anchor.

RG II printed p. 12 separately requires the auxiliary cutoff bonds \(P\) to
be wholly contained in \(\operatorname {int}Z_0\) and not to meet its
boundary. That special \(P\)-condition does not redefine the external
\((U,J)\) restriction convention: after Eq. (2.6), the paper still describes
external-field dependence on the whole lattice before the second
localization.

## Repository marked-support corollary

The repository adds only support-preserving operations:

- Note 0012 puts the independent-\((U,J,B)\) mark on
  \(\operatorname {int}A\).
- Note 0021 includes \(A\) in the marked seed and applies the same finite
  Section-2 map coefficientwise over
  \(\mathbb C[\epsilon]/(\epsilon^2)\).
- Note 0025 verifies that conditioning leaves the mark on the conditional
  interior \(B\); exterior Gaussian standardization and the second
  weakening do not enter its argument.

Consequently

\[
H_{p,s}^{\mathbb D}(C)
=
H_s(C)-\epsilon W_{p,s}^{\rm post}(C)
\]

depends only on external bond coordinates intersecting
\(\operatorname {int}C\). Coefficient extraction gives the same restriction
property for \(W_{p,s}^{\rm post}(C)\).

Notes 0023--0024 identify the final connected hull with the literal union.
The Ursell coefficient is field independent, Note 0026 gives absolute
convergence, and Note 0027 forms and then normalizes each complete branch
coefficient. Every product contributing to \(R\) therefore depends only on
external bond coordinates intersecting \(\operatorname {int}R\). A
field-independent shift normalization cannot enlarge that support.

The repository's zero-halo conclusion is a separate grid-alignment lemma.
The nested cubulations of Notes 0014 and 0027 have integer current-lattice
walls and closed cubes. A current-lattice nearest-neighbor segment
intersecting the interior of a union of those cubes is contained in the
closed union, so both of its endpoints—and hence either fixed orientation
anchor—belong to the final support. This is not a printed source theorem.

## Exact boundary

- The printed source locality is unmarked and tied to one chosen
  cubulation. Marked coefficient extraction, shifted transport, and the
  normalized connected support theorem are repository corollaries.
- The external-\(J\) source convention retains a complete bond coordinate
  when its geometric segment intersects the interior. It does not license
  full-bond containment in the interior or a base-site-only convention.
- Zero halo uses the repository's integer-wall, closed-cube geometry. A
  non-grid-aligned cubulation would require a positive halo.
- Locality proves that derivatives outside the literal union vanish. It does
  not bound the derivative inside the union.
- A nonempty common branch domain is not a quantitative uniform complex
  collar. A full \(\ell^\infty\) \(J\)-tube with a tube-uniform connected
  norm is still needed before Banach Cauchy and the physical kernel pullback
  can be applied without a volume factor.
- No nonlinear \(U\) collar, nonzero-source polymer disk, large-field
  estimate, RG iteration, continuum construction, infrared result, or mass
  gap is imported or proved.
- This audit is not independent human review.
