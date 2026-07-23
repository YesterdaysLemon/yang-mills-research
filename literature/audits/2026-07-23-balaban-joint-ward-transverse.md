# Balaban joint-\(U/J\), kernel-range, and vertical-decay audit - 2026-07-23

Status: primary-source equation audit plus repository theorem boundary

Human review: none. This is an AI-assisted audit and is not an independent
human review.

## Source inputs and immutable local records

The equations used in YM-RG-036 were checked in:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), Eqs. (20)--(21),
  (181)--(190), and Proposition 9, printed pp. 281 and 307--309;
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), Eqs. (2.46),
  (2.59)--(2.60), and (2.68)--(2.69), printed pp. 231 and 234--235.

The local files used for this audit have SHA-256 hashes:

```text
Variational problem and background fields
1F480977608AD36286D074841E3DBB02CE842113F92B818D8BD88BCCFF88DF3C

Propagators II
6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F
```

The variational scan was acquired from the
[University of Michigan archive](https://deepblue.lib.umich.edu/items/e9af57c2-30bd-4dfc-85cd-3f01956f02fa).
Rendered pages containing printed p. 281, pp. 307--309, and Propagators II
printed pp. 234--235 were visually inspected. Text extraction was used only
as a locator, not as the final equation authority.

## One common variational kernel

The variational paper defines one kernel

\[
K_{\mu\nu}(B;x,y')
=
\frac{\delta\mathcal H_\mu(B,x)}{\delta B_\nu(y')}.
\]

The five lines of Eq. (190) are estimates for this common kernel:

1. \(K\);
2. its output covariant gradient;
3. a localized Hölder difference of that gradient;
4. \(D^*DK\); and
5. \(\Delta K\).

They are not five independently selectable kernels. The displayed estimates
are norm or absolute-value bounds. They do not print a signed cancellation
between the raw and gradient rows.

Equation (190) also does not print:

- a source derivative \(\nabla_{y'}K\);
- an identity \(\nabla_xK=-\nabla_{y'}K\);
- a zero source moment; or
- a vanishing trace across output cells, active sets, or layer interfaces.

Consequently an output summation by parts cannot be converted into an input
derivative or discarded boundary term from Eq. (190) alone.

## Differentiated range constraints

Equations (20)--(21) impose the exact averaging and projected Landau
conditions on the minimizing background. Differentiating them with respect
to a measure-normalized source coordinate gives, in the repository's
notation,

\[
D_AQ_j(U_k,\eta\mathcal H)
[\eta K_{\cdot,c}]
=
\mathbf e_c,
\qquad
R(U_k)D_{U_k}^{\eta *}K_{\cdot,c}=0.
\]

The first equation is a right-inverse normalization for each kernel column.
The second is a projected output-divergence condition. Neither equation
states \(D^*K=0\), identifies \(\Delta K\) with \(D^*DK\), or supplies the
completed coefficient's Ward identity.

These two equations are genuine source-specific range information. They are
the next constraints that a positive direct-synthesis theorem must exploit.
YM-RG-036 does not claim that its abstract transverse countermodel satisfies
them, nor that an actual Balaban column violates them.

## Vertical scale separation

Write \(s_j=L^j\eta\). Propagators II Eq. (2.60) gives, for
\(0<\alpha<1\) and with \(R,M\) chosen to satisfy the strengthened
separation condition (2.59) at that \(\alpha\),

\[
e^{-\alpha\delta_0d_{\mathcal B}(y,y')}
\le
e^{-\alpha\delta_0RM\max\{|j-j'|-1,0\}}.
\]

For \(0\le\lambda'<\lambda\), set
\(\alpha=(\lambda-\lambda')/\delta_0\). If

\[
\alpha\in(0,1),
\qquad
\frac14\alpha\delta_0RM
>
2d\log c_0(\alpha/2)+1,
\qquad
(\lambda-\lambda')RM\ge q\log L,
\]

where the middle inequality is Eq. (2.59), then the exact one-layer
allowance gives

\[
s_j^{-q}e^{-\lambda d_{\mathcal B}(y,y')}
\le
L^q s_{j'}^{-q}e^{-\lambda'd_{\mathcal B}(y,y')}.
\]

This is the same kind of scale-power/decay trade visible in Eq. (2.68).
It moves an output loss to the input scale; it does not remove the power.
Equation (2.69) supplies the source measure, which cancels the printed input
density but not this transferred \(s_{j'}^{-q}\).

The current source class contains \(j'=j\) and \(y'=y\). At that diagonal
label the distance is zero, so the finest layer contributes
\(\eta^{-q}\). Vertical decay alone therefore cannot give a
regulator-uniform theorem on the current unweighted all-layer
\(\ell^\infty\) source ball. A source norm weighted by \(s_{j'}^{-q}\), a
coarse-layer support restriction, or additional signed/range structure
would be a different theorem.

## What is repository algebra

The following statements in YM-RG-036 are not attributed to Balaban:

- combining the physical \(U\) derivative and induced \(J\) derivative into
  one joint column before taking absolute values;
- quotienting the product \(U/J\) tube by both inactive directions and
  simultaneous gauge tangents;
- the exact finite-dimensional phase/quotient-duality formula and its sharp
  coefficient-independent constant;
- the unit-bidisc example showing that separate absolute values can destroy
  an exact Ward cancellation; and
- the commuting-Cartan, gauge-invariant Wilson-plaquette countermodel showing
  that the current abstract rowwise, locality, product-tube, and Ward
  hypotheses do not exclude a same-cell transverse \(s^{-2}\) loss.

The completed coefficientwise Ward identity and the converted common physical
columns remain hypotheses. The countermodel is logical: it is not identified
with a completed Balaban coefficient or with the actual range of \(K\).

## Audit conclusion

The following source statements pass the visual equation crosswalk:

- Eq. (190) consists of five bounds on one common kernel;
- Eqs. (20)--(21) differentiate to a right-inverse normalization and a
  projected Landau-divergence constraint;
- no source-variable derivative, zero source moment, or signed row
  cancellation is printed at those anchors;
- Eq. (2.60), with (2.59) retained at the spent exponent, transfers output
  scale powers to input scale powers with a one-layer \(L^q\) cost; and
- Eqs. (2.68)--(2.69) exhibit the same scale-power trade and source-measure
  normalization, not deletion of the diagonal same-cell loss.

Still open are the completed Ward premise, the actual chart and
gauge-restoration conversion of the common \(K,\nabla K\) columns, a
source-faithful theorem on the differentiated range constraints, the
physical-family hypothesis \((\mathrm H_{\rm rc})\), nonzero-source
activities, raw matching, large fields, RG iteration, continuum and
infinite-volume construction, reconstruction, infrared decay, and the mass
gap.

No Yang--Mills existence or mass-gap solution is established by this audit.
