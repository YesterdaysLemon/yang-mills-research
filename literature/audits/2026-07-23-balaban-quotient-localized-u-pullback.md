# Balaban quotient-localized \(U\)-pullback audit — 2026-07-23

Status: primary-source boundary audit plus repository derivation review

Human review: none. This is an AI-assisted audit and is not an independent human review.

## Sources and immutable anchor

The source inputs are:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), especially Section G,
  Proposition 9, and Eqs. (181)--(190), printed pp. 305--309;
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), especially
  Eqs. (2.45)--(2.54) and Lemma 2.1, Eqs. (2.59)--(2.63);
- T. Balaban, [*Renormalization group approach to lattice gauge field
  theories I*](https://doi.org/10.1007/BF01215223), especially the physical
  auxiliary-field and relative-coordinate formulas on printed pp. 261--263
  and 269--272.

The Propagators-II PDF used for the metric/convolution audit is retained
locally as `tmp/pdfs/propagators-ii.pdf`. Its SHA-256 is

`6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F`.

This is the CMP 96 Propagators-II paper. It is not the distinct CMP 116
RG-II cluster-expansion paper.

## What Proposition 9 actually supplies

In the variational paper's notation, let

\[
K_{\mu\nu}(B;x,y')
=
\frac{\delta\mathcal H_\mu(B,x)}{\delta B_\nu(y')},
\qquad
x\in\Delta(y),\quad
y\in\Lambda_j,\quad
y'\in\Lambda_{j'}.
\]

Equation (190) prints five component rows:

\[
K,\qquad
\nabla K,\qquad
\zeta\nabla K,\qquad
D_{U_k}^{\eta *}D_{U_k}^{\eta}K,\qquad
\Delta_{U_k}^{\eta}K.
\]

Their output-scale factors are, respectively,

\[
(L^j\eta)^{-1},\quad
(L^j\eta)^{-2},\quad
\bigl(\|\zeta\|_\beta^\xi+|\zeta|\bigr)
(L^j\eta)^{-2-\beta},\quad
(L^j\eta)^{-3},\quad
(L^j\eta)^{-3}.
\]

The Hölder row also requires
\(\operatorname{supp}\zeta\subset\widetilde\Delta(y)\).
Every row also carries

\[
(L^{j'}\eta)^{-d}
\exp\!\left[-\frac{\delta _0}{8}d_{\mathcal B}(y,y')\right].
\]

The roles of \(j\) and \(j'\) are distinct. The decay exponent in Eq. (190)
is \(\delta _0/8\), not the \(\delta _0/4\) appearing immediately above in
Eq. (189).

The source theorem is a componentwise derivative theorem for the selected
minimizing background branch. It is not itself a Banach-operator theorem for
a completed connected polymer coefficient.

## Source-measure normalization

Propagators II uses the cell scale

\[
s_{j'}=L^{j'}\eta.
\]

The natural source measure is

\[
\mu(j',y')=s_{j'}^d.
\]

It cancels Eq. (190)'s inverse source-density factor
\(s_{j'}^{-d}\). Lemma 2.1 then supplies the exponential convolution used in
Notes 0017 and 0032, under its strengthened separation premise. For

\[
0\le\gamma<\frac{\delta _0}{8},
\qquad
\alpha_\gamma
=
\frac18-\frac{\gamma}{\delta _0},
\]

the remaining sum is controlled by \(c_1(\alpha_\gamma)\).

Nothing in that convolution compares \(d_{\mathcal B}\) with the completed
rooted polymer metric. Note 0033 avoids such a comparison for its unweighted
and feature-support-anchored statements.

## The relative-log tangent and the four required features

Note 0016 records the fixed-chart identity

\[
D\mathcal U[h]
=
i\xi A_h\mathcal U.
\]

The variational \(K\)-column first produces the variation of
\(\mathcal H\); the selected differential-of-exponential and
gauge-restoration maps then produce \(A_h\). On one fixed relatively compact
chart those finite-dimensional maps are bounded.

Note 0031's \(U\)-tube, however, uses the complete norm

\[
\max\left\{
\|a\|_{\infty,\mathrm{RG}},
\|\nabla_{\bar U}^{\xi}a\|_{\infty,\mathrm{RG}},
\|a\|_{\infty,\mathrm{op}},
\|\mathcal D_{\bar U}^{\xi}a\|_{\infty,\mathrm{op}}
\right\}.
\]

Consequently a physical-\(U\) pullback needs converted kernel rows for all
four features:

1. raw RG-norm evaluation;
2. background-covariant gradient in the RG norm;
3. raw operator-norm evaluation;
4. the covariant plaquette curl with Note 0031's normalization.

The first and third differ only by a fixed finite-dimensional norm
comparison. The second is expected to use the printed \(K\) and
\(\nabla K\) rows plus derivatives of the local chart coefficients. The
fourth needs an exact transported local identity relating
\(\mathcal D_{\bar U}^{\xi}A_h\) to the converted \(K/\nabla K\) data.
Equation (190) labels one output site \(x\in\Delta(y)\); it does not state
that one cell contains an entire multi-link gradient or curl stencil. A
converted feature row must therefore include a bounded local decomposition,
tagged term labels, and any common label halo or multiplicity.

That four-feature conversion with common regulator-, center-, branch-, and
scale-independent constants is **not source proved** by the lines audited
here. In particular:

- \(D_{U_k}^{\eta *}D_{U_k}^{\eta}K\) is the leading row used in the
  physical auxiliary-\(J\) differential;
- \(\Delta_{U_k}^{\eta}K\) is an alternate Laplacian row;
- neither may be silently renamed as Note 0031's covariant plaquette curl.

This is the reason Note 0033 names
\((\mathrm H_{\rm row}^U)\) instead of claiming that Eq. (190) already
states the required assembled Banach estimate.

## The unweighted repository corollary

Assume the converted four-feature row estimate and a common global
output-scale envelope. For a bounded source test direction \(h\), form

\[
\mathcal A_Uh
=
\sum_\alpha\mu_\alpha A_\alpha h_\alpha.
\]

The source-measure cancellation and Propagators-II convolution bound each
feature uniformly. Taking the supremum over feature locations is precisely
the \(U\) norm; it is not a sum over bonds. Therefore

\[
\|\mathcal A_U\|_{\ell^\infty\to\mathsf U}
\le
C_{\chi,U}c_1(1/8)\overline E_U^{\rm glob}.
\]

Finite-dimensional source phase duality and Note 0031's completed
\(\mathsf U^*\) derivative norm then give Note 0033 Eq. (19). This is a
repository functional-analytic corollary, not a theorem printed by Balaban.

At source exponent \(\gamma=0\), it needs no support projection, zero
extension, ownership map, or bond count. Its common converted rows and
global scale envelope remain conditional.

## Why positive support decay is a different theorem

Note 0029 proves that each completed coefficient depends only on external
\((U,J)\) bonds meeting the interior of its literal-union support. Thus its
\(U\)-derivative annihilates directions that vanish on the active \(U\)
bonds.

Let \(X\) be Note 0031's global \(U\)-norm space, let \(I\) be that active
bond set, and put

\[
N_I=\{a:a|_I=0\}.
\]

The supported derivative descends to \(X/N_I\), with exactly the same dual
norm. This is the correct restriction quotient. It does not identify the
quotient norm with a zero-extension norm.

For a positive source-distance weight, Note 0033 defines the quotient
synthesis operator

\[
\mathsf K_{I,\gamma,S}c
=
Q_I\sum_\alpha
\mu_\alpha
e^{\gamma d_{\widetilde{\mathcal B}}(S,\widetilde y_\alpha)}
c_\alpha A_\alpha.
\]

Finite-dimensional duality proves that its operator norm is the sharp
coefficient-independent constant multiplying the completed
\(\mathsf U^*\) derivative norm. This exact reduction is a repository
result.

No audited source theorem supplies a common bound on this restriction
quotient synthesis norm.

## The genuine extension premise

A checkable sufficient route is a local feature collar \(\Sigma_I\) and

\[
\|Q_Ia\|_{X/N_I}
\le
C_{\rm ext}
\max_{\sigma\in\Sigma_I}\|T_\sigma a\|.
\]

This is Note 0033's \((\mathrm H_{\rm ext}^U)\). It is a local right-inverse
or quotient-extension theorem for the complete covariant norm.

The distinction matters. In the toy norm

\[
\|(a_0,a_1)\|
=
\max\{|a_0|,|a_1|,\xi^{-1}|a_1-a_0|\},
\]

the restriction value \(a_0=u\) has the constant extension \((u,u)\) of
cost \(|u|\), while its zero extension \((u,0)\) costs
\(\max\{|u|,\xi^{-1}|u|\}\). Thus zero extension can invent an inverse-mesh
loss not present in the quotient.

Conversely, for the standing range \(0<\xi\le1\), the functional

\[
\ell_\xi(a)=\xi^{-1}(a_1-a_0)
\]

has covariant dual norm \(1\), while the sum of its two raw coordinate
functional norms is \(2/\xi\). This disproves a direct copy of Note 0032's
\(\ell^\infty\)-\(\ell^1\) coordinate argument.

The feature collar must include every row used by the norm. If the positive
source weight is anchored at the collar labels themselves, the
Propagators-II convolution adds no feature-cardinality factor. If it is
anchored at the smaller active-bond label set, a common collar halo and its
factor \(e^{\gamma H_U}\) must be retained.

Neither the common extension constant nor the halo is proved by
\((\mathrm H_{\rm rc})\).

## Ward-identity boundary

Gauge covariance gives a joint infinitesimal identity schematically of the
form

\[
D_U\widehat{\mathcal C}[a_\phi]
+
D_J\widehat{\mathcal C}[\delta_\phi J]
=0.
\]

It does not say that the \(U\) term vanishes separately. Notes 0032 and 0033
take absolute values of the two physical chain-rule summands separately.
Therefore no longitudinal or gauge direction may be discarded from the
\(U\) norm in the present argument.

A future proof could try to use Ward cancellation before absolute
summation, but that would be a new joint \(U/J\) theorem.

## Audit result

The following repository implications are sound, conditional on their named
premises:

- common converted feature rows plus a global envelope imply the unweighted
  physical-\(U\) sum without a volume or mesh factor;
- completed external-\(U\) locality gives exact restriction-quotient
  duality;
- the quotient synthesis norm is the sharp universal positive-\(\gamma\)
  kernel moment;
- a common local feature-extension theorem plus the converted Eq. (190) rows
  bounds that moment without a support-cardinality factor.

The following remain open:

- the common four-feature conversion from Eq. (190);
- the exact covariant-curl identity and normalization;
- a regulator-uniform global or completed scale envelope;
- the positive-\(\gamma\) local extension constant and any active-label
  collar halo;
- \((\mathrm H_{\rm rc})\) for the actual completed minimizing family.

No nonzero-source polymer-activity disk, unrestricted raw-law comparison,
large-field estimate, RG iteration, continuum construction,
Osterwalder--Schrader reconstruction, infrared decay, or Yang--Mills mass
gap is established by this audit.
