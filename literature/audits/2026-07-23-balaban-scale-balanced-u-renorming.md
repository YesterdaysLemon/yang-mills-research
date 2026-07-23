# Balaban scale-balanced physical-\(U\) renorming audit - 2026-07-23

Status: primary-source normalization crosswalk plus repository no-go audit

Human review: none. This is an AI-assisted audit and is not an independent
human review.

## Source inputs

This checkpoint reuses the directly inspected sources and immutable records
from the preceding audits:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), especially Proposition 9
  and Eqs. (182), (189), and (190), printed pp. 307--309;
- T. Balaban, [*Renormalization group approach to lattice gauge field
  theories I*](https://doi.org/10.1007/BF01215223), especially Eqs.
  (1.10)--(1.16), printed pp. 262--263;
- T. Balaban, [*Spaces of Regular Gauge Field Configurations on a Lattice
  and Gauge Fixing Conditions*](https://doi.org/10.1007/BF01466594),
  especially Eqs. (1.1), (1.36), and (1.47)--(1.50);
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), especially
  Lemma 2.1 and Eqs. (2.45)--(2.63).

The local primary-source hashes used by the relevant normalization audits
are:

```text
Gauge-fixing paper
7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB

RG I
1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A

Propagators II
6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F
```

No new theorem is attributed to these papers in YM-RG-035.

## Source normalization that matters

For \(s_j=L^j\eta\), the two Eq. (190) rows retained after YM-RG-034 are

\[
|K|
\lesssim
s_j^{-1}s_{j'}^{-d}
e^{-(\delta _0/8)d_{\mathcal B}(y,y')},
\]

\[
|\nabla K|
\lesssim
s_j^{-2}s_{j'}^{-d}
e^{-(\delta _0/8)d_{\mathcal B}(y,y')}.
\]

The source measure \(s_{j'}^d\) cancels only the input-density power. It
does not cancel \(s_j^{-1}\) or \(s_j^{-2}\). The one-step repository
specialization identifies \(\eta=\xi_{k+1}\) and defines its relative-chart
tangent by

\[
D\mathcal U[h]=i\xi_{k+1}A_h\mathcal U.
\]

That definition has already used the factor \(\xi_{k+1}\); it supplies no
additional scale gain after the converted \(K,\nabla K\) rows are formed.
The currently retained differential-of-exponential and gauge-restoration
maps are only assumed bounded on a fixed chart.

Therefore multiplying a raw output occurrence by \(s_j\) and a gradient
occurrence by \(s_j^2\) is the exact diagonal scaling that cancels the two
printed output powers. This is an algebraic observation, not a source
theorem about one completed physical Banach space.

## The output tag is not automatically a global-field tag

In Eq. (190), \(j\) is attached to an output cell
\(y\in\Lambda_j\) with \(x\in\Delta(y)\). It is not printed as a unique
intrinsic label of every occurrence of a global independent-bond tangent
across all restrictions, shifts, completed coefficients, and cutoff
collars.

YM-RG-035 consequently treats the raw scales \(r_b\), gradient scales
\(t_e\), and their common incidence as declared hypotheses. It does not
claim that Eq. (190) provides:

- one branch-independent tag atlas;
- bounded scale separation between every gradient row and its raw
  endpoints;
- a common tagged-metric halo; or
- a weighted completed product tube.

## Weighted cutoff is repository algebra

For

\[
D_ea=h_e^{-1}(T_ea_+-a_-),
\]

the exact two-point product rule gives

\[
D_e(\chi a)
=
\chi_-D_ea+h_e^{-1}(\chi_+-\chi_-)T_ea_+
=
\chi_+D_ea+h_e^{-1}(\chi_+-\chi_-)a_-.
\]

With raw weights \(r_b\), gradient weights \(t_e^2\), and a cutoff of
physical width \(\rho\), the relevant incidence constant is

\[
\Theta
=
\sup_e
\frac{t_e^2}{\min(r_{e,-},r_{e,+})}.
\]

YM-RG-035 proves

\[
\|Q_Ia\|_{Y_{\rm sc}/N_I}
\le
\left(
1+\frac{c_{\rm Ad}^{\rm RG}\Theta}{\rho}
\right)
M_{S_{I,\rho}}(a).
\]

This is not printed by Balaban. The scalar weighted path in YM-RG-035 shows
that its \(\Theta/\rho\) dependence is unavoidable. Thus a common
physical-width theorem requires a separately verified scale-incidence
bound.

## Why the weighted chart does not inherit RG I's tube

RG I condition (ii) controls the unweighted raw relative field and
unweighted covariant gradient by fixed small-field constants. Its
condition (iii) requires plaquette curvature of order \(\xi^2\).

On a homogeneous finest patch, the row-cancelling norm is schematically

\[
\max\{
\xi|a|,
\xi^2|\nabla^\xi a|
\}.
\]

An isolated complex Cartan bond

\[
a(b)=-i(t/\xi)H
\]

has weighted raw, gradient, and weighted curl size \(O(t)\), but its
adjacent plaquette contains \(e^{tH}\). Hence a fixed weighted ball permits
an \(O(1)\) plaquette change, whereas RG I permits only \(O(\xi^2)\).
The exact spectral-radius calculation in YM-RG-035 forces the full weighted
curvature-domain radius to be \(O(\xi^2)\).

This remains true if one retains an unweighted curl row: a flat longitudinal
field varying only in its own direction has zero plaquette curl but
unweighted gradient \(O(t\xi^{-2})\) at weighted size \(O(t)\). It exits RG
I condition (ii) unless the weighted radius is \(O(\xi^2)\).

Thus the weighted norm and the source theorem are not in conflict. The
weighted norm controls a different, larger set of fine-scale directions
than RG I's small-field domain admits.

## Cauchy boundary

Note 0031's completed derivative bound comes from a full complex ball in its
unweighted covariant norm. If a new weighted norm \(W\) embeds into that norm
\(X\) with inclusion constant \(M\), the inherited weighted ball has radius
at most \(r_X/M\), and generic Banach-line Cauchy gives

\[
\|DF(0)\|_{W^*}\le BM/r_X.
\]

At the finest scale, the exact homogeneous row-cancelling model has
\(M\asymp\xi^{-2}\).
The weighted source operator can be \(O(1)\), but the Cauchy bound then
recovers the same \(O(\xi^{-2})\) loss. YM-RG-035 gives a sharp
one-dimensional model, so this is not merely an artifact of the displayed
estimate.

## Audit conclusion

The following statements pass the source/normalization crosswalk:

- \(s_j\) and \(s_j^2\) are the exact diagonal factors that cancel the
  printed raw and gradient output powers;
- the source measure does not supply either factor;
- the weighted cutoff and its incidence constant are repository algebra;
- RG I's unweighted condition-(ii) and \(O(\xi^2)\) curvature domain do not
  contain a regulator-uniform ball in the row-cancelling weighted norm; and
- generic Cauchy returns the removed \(\xi^{-2}\) power through the shrunken
  weighted radius.

The following remain open:

- the converted \(K,\nabla K\) rows through the actual chart and gauge
  restoration;
- a common output tag atlas and scale-incidence theorem;
- direct smoothing or cancellation for the assembled physical synthesis;
- a two-norm completed derivative theorem or justified weighted physical
  source target;
- \((\mathrm H_{\rm rc})\) for the actual minimizing family; and
- all nonzero-source activity, raw-law, large-field, iteration, continuum,
  reconstruction, infrared, and mass-gap gates.

No Yang--Mills existence or mass-gap solution is established by this audit.
