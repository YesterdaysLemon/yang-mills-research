# Balaban transported-curl and quotient-extension audit - 2026-07-23

Status: primary-source notation audit plus repository algebra review

Human review: none. This is an AI-assisted audit and is not an independent
human review.

## Immutable source anchors

The local primary-source files inspected for this checkpoint are:

```text
tmp/pdfs/gauge-fixing-conditions.pdf
SHA-256
7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB

tmp/pdfs/rg-i-full.pdf
SHA-256
1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
```

The first is T. Balaban,
[*Gauge Fixing Conditions and the Infrared Problem of Lattice Gauge
Theories*](https://doi.org/10.1007/BF01466594), CMP 99 (1985), 75--102.
The second is T. Balaban,
[*Renormalization group approach to lattice gauge field theories
I*](https://doi.org/10.1007/BF01215223), CMP 109 (1987), 249--301.

The visually inspected pages were:

- gauge-fixing printed p. 76, Eq. (1.1);
- gauge-fixing printed p. 82, Eq. (1.36);
- gauge-fixing printed pp. 84--85, Eqs. (1.47)--(1.50);
- RG I printed p. 262, Eqs. (1.11)--(1.14).

## What the source fixes

Gauge-fixing Eq. (1.1) defines the scaled covariant difference

\[
(D_{U,\mu}^{\eta}F)(x)
=
\eta^{-1}
\left[
R(U(x,x+\eta e_\mu))F(x+\eta e_\mu)-F(x)
\right],
\]

where \(R(U)X=UXU^{-1}\). It also states that the definition applies with an
arbitrary lattice scale in place of \(\eta\).

Gauge-fixing Eq. (1.36) controls both

\[
|A|,
\qquad
|\nabla_{U_0}^{\eta}A|,
\]

with the scale shapes \((L^j\eta)^{-1}\) and
\((L^j\eta)^{-2}\). RG I condition (ii), Eq. (1.13), uses the same two
features for the complex relative field:

\[
U'=\exp(i\xi A'),
\qquad
|A'|,\ |\nabla_{\bar U}^{\xi}A'|<\alpha _1.
\]

Gauge-fixing Eq. (1.47) expands the relative plaquette as

\[
(\partial_{U_0}U_1)(p)-1
=
i\eta^2(D_{U_0}^{\eta}A)(p)
-\frac12\eta^2V_2(U_0,A,\partial p)
+O(\eta^3|\partial A|^3).
\]

Equations (1.49)--(1.50) identify the quadratic commutators and explicitly
say that the algebraic identity holds for arbitrary \(A\) in the
complexified Lie algebra. Equation (1.50) writes the local terms using the
component derivatives \(D_\mu=D_{U_0,\mu}^{\eta}\).

These lines support all normalization choices in Note 0034. They do not
print Note 0034's exact four-link rearrangement or its quotient-extension
theorem.

## Exact repository curl rearrangement

Note 0031 defines the reverse link by

\[
a(\bar b)
=
-\operatorname {Ad}_{\bar U(b)^{-1}}a(b)
\]

and, after prefix transport around a plaquette, defines

\[
\mathcal D_{\bar U}^{\xi}a(p)
=
\xi^{-1}\sum_{\ell=1}^4X_{\ell,p}(a).
\]

For \(p=p_{\mu\nu}(x)\), write \(P=d\bar U(p)\), and use the forward
transports

\[
T_\mu a_\nu
=
\operatorname {Ad}_{\bar U_\mu(x)}
a_\nu(x+\xi e_\mu),
\qquad
T_\nu a_\mu
=
\operatorname {Ad}_{\bar U_\nu(x)}
a_\mu(x+\xi e_\nu).
\]

The four prefix-transported terms are

\[
a_\mu,\quad
T_\mu a_\nu,\quad
-\operatorname {Ad}_P T_\nu a_\mu,\quad
-\operatorname {Ad}_P a_\nu.
\]

Direct addition gives

\[
\mathcal D_{\bar U}^{\xi}a
=
D_\mu a_\nu-D_\nu a_\mu
+\xi^{-1}
(I-\operatorname {Ad}_P)
(a_\nu+T_\nu a_\mu).
\]

This is a repository algebraic identity. The curvature correction is
required when \(P\ne1\); omitting it would falsely identify the transported
four-link sum with the flat antisymmetric difference.

Under Note 0031's real curvature margin
\(|P-1|_{\rm RG}\le\bar a_U\xi^2\), unitary transport and fixed
finite-dimensional norm equivalence give

\[
\|\mathcal D_{\bar U}^{\xi}a\|_{\rm op}
\le
2c_{\rm op\leftarrow RG}\|\nabla_{\bar U}^{\xi}a\|_{\rm RG}
+4c_{\rm op\leftarrow RG}^2\bar a_U\xi\|a\|_{\rm RG}.
\]

Therefore the complete Note 0031 norm is uniformly equivalent to its
raw-RG and covariant-gradient-RG entries. This closes the independent
covariant-curl conversion; it does not prove the remaining conversion of
the variational \(K,\nabla K\) columns through the selected chart and gauge
restoration.

The printed \(D^*D K\) and \(\Delta K\) rows of variational Eq. (190) play no
role in this rearrangement and are not curl substitutes.

## Exact repository cutoff

For the graph whose vertices are independent bonds and whose edges are the
two-point gradient stencils from Eq. (1.1), let

\[
\chi_{I,m}(b)
=
\left(1-\frac{d_\nabla(b,I)}m\right)_+.
\]

The two-point definition gives an exact scalar product rule. Across an
inside-inside row it bounds the cutoff gradient by the original local
gradient plus
\((m\xi)^{-1}\) times a transported raw value. Across the cutoff boundary,
the equality can be written with the zero-cutoff endpoint multiplying the
original gradient, leaving only the raw inside value. Rows fully outside
vanish.

Using Note 0034's minimal collar of raw rows and inside-inside gradient
rows therefore gives

\[
\|Q_Ia\|_{X/N_I}
\le
C_{\rm eq}(\xi)
\left(
1+\frac{c_{\rm Ad}^{\rm RG}}{m\xi}
\right)
\max_{\sigma\in\Sigma_{I,m}^{01}}\|T_\sigma a\|.
\]

This is a finite-dimensional repository cutoff theorem, not a result printed
in either Balaban paper. It uses the local germ of an already
defined global representative and does not construct a linear right inverse
from arbitrary boundary data.

Taking \(m=\lceil\rho/\xi\rceil\) makes the constant uniform. On graph
components disjoint from the active set, the cutoff is defined to be zero.
A collar with a fixed number of lattice layers cannot be uniform: a
normalized scalar flat abelian longitudinal path with endpoint values
\(1,-1\) has exact quotient norm

\[
\max\left\{1,\frac2{N\xi}\right\},
\]

while its only jump can be hidden outside any fixed \(m\)-layer collar.
The example has zero plaquette curl and therefore remains a counterexample
for the complete four-entry norm. Embedding it along a fixed commuting
generator in a compact matrix group changes only fixed RG/operator norm
constants and preserves the inverse-mesh divergence.

## Consequence for Eq. (190)

Note 0034 may replace Note 0033's four-feature source-row hypothesis by
converted raw and covariant-gradient rows only. Those correspond to the
variational paper's printed \(K\) and \(\nabla K\) scale shapes

\[
(L^j\eta)^{-1},
\qquad
(L^j\eta)^{-2}.
\]

This reduction is algebraically valid, but the following remain unproved:

- the common differential-of-exponential and gauge-restoration conversion;
- the exact source-component and tagged output conventions for the
  background-covariant gradient;
- common chart constants over the completed physical family;
- regulator-uniform global or collar scale envelopes.

In particular, the candidate unweighted envelope
\(C_{U,1}(L^j\eta)^{-1}+C_{U,2}(L^j\eta)^{-2}\) may diverge when the smallest
output scale tends to zero. The source measure cancels only Eq. (190)'s
input-density factor \((L^{j'}\eta)^{-d}\); it leaves both output factors
unchanged. The chart normalization \(D\mathcal U=i\xi A\mathcal U\) contains
no spare power, and the retained conversion hypotheses are bounded rather
than scale gaining. Neither curl closure nor the cutoff cancels those
factors.

## Metric boundary

The proved collar has a common physical thickness and
\(\lceil\rho/\xi\rceil\) lattice layers. Anchoring source decay at all collar
feature labels is valid and introduces no feature-count factor. Returning to
the exact active-bond labels requires a separate comparison between
\(d_\nabla\) and the tagged Propagators-II metric. If the latter counts
unscaled lattice layers, the halo can grow like \(\xi^{-1}\). No active-label
or marked-plaquette decay theorem is inferred without that comparison.

## Audit result

The following repository implications pass the source and algebra audit:

- the normalized transported curl has the exact curvature-corrected form in
  Note 0034;
- the complete covariant norm is uniformly equivalent to Balaban's printed
  raw-plus-gradient pair under \((\mathrm H_{\rm rc})\);
- a physical-width cutoff proves the restriction-quotient extension with a
  common constant;
- the abelian longitudinal example proves that bounded lattice-layer width
  is not uniform.

The following remain open:

- \((\mathrm H_{\rm rc})\) for the actual completed minimizing family;
- converted \(K,\nabla K\) rows with common constants and tagged labels;
- a regulator-compatible scale envelope;
- the multiscale halo from the physical-width feature collar to active or
  marked-root labels;
- all nonzero-source activity, raw-law, large-field, iteration, continuum,
  reconstruction, infrared, and mass-gap gates.

No Yang--Mills existence or mass-gap solution is established by this audit.
