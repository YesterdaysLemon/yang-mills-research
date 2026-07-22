# Note 0010: the exact normalized RG-I coordinate law

Claim ID: YM-RG-010

Kind: primary-source corollary plus finite-dimensional normalization

Evidence: E2 (finite-regulator selected-coordinate law; internally checked)

Novelty: none claimed

## Why a second branch law is named

Note 0008 defines an intrinsic coarea restriction
\(K_k^{\mathrm{chart}}(W,dU)\) on the selected near-identity branch, and Note
0009 organizes that restriction over one background patch. RG I Eqs.
(2.12)–(2.13) use a later Gaussian coordinate representation containing the
full fluctuation weight, cutoff, constraint-coordinate Jacobian, and extracted
quadratic form.

Those two representations have not been matched term by term in this
repository. Their normalized observable expectations therefore must not be
identified by notation or by projective invariance: an untracked ratio of
their densities could depend on the fluctuation coordinate. This note names
the exact printed RG-I law separately.

## Fixed-coordinate law

Retain the finite-regulator, fixed-\(\varepsilon _1\), selected-branch
hypotheses of Notes 0008–0009. Fix a real coupling \(g_k>0\), an admitted real
coarse field \(W\), and

\[
I_k=T^{(k)}\setminus\{b_0(c):c\in T^{(k+1)}\}.
\tag{1}
\]

Use RG I's independent coordinate \(B\in\mathfrak g^{I_k}\) and cutoff

\[
\chi_k(B)=
\prod_{b\in I_k}
\mathbf1\{g_k\lVert B(b)\rVert<\varepsilon _1\}.
\tag{2}
\]

The complete selected relative field is

\[
B'_W(B)=g_kC_WB-h_W\widetilde D_W(g_kC_WB),
\tag{3}
\]

and \(\mathscr U_k(W,B)\) denotes the exact fine-field reconstruction used in
RG I. Let

\[
\Gamma_k(W)=
\big(C_W^*A^{(k)}(W)C_W\big)^{-1}
\tag{4}
\]

denote the positive real Gaussian covariance extracted in Eq. (2.12). Define

\[
\Psi_k^{\mathrm{RG}}(W,B)=
P^{(k)}(g_k,U_{k+1}(W),B)
+R_{(2.12)}^{(k)}(W,B),
\]

where \(R_{(2.12)}^{(k)}\) denotes the **complete** remaining exponent inside
the printed Eq. (2.12) Gaussian integral. This notation retains every
effective-action difference and the constraint-coordinate factor

\[
\operatorname{Tr}\log\!\left(
I-h_WD\widetilde D_W(g_kC_WB)
\right).
\tag{5}
\]

Here \(\operatorname{Tr}\log=\log\det\) uses the analytic branch continued
from the identity at \(B=0\); positive real orientation on the admitted cube
selects its real value there.

No \(B\)-dependent summand or determinant is silently discarded.

Set

\[
Z_k^{\mathrm{RG}}(W)=
\int \chi_k(B)e^{\Psi_k^{\mathrm{RG}}(W,B)}
\,d\mu_{\Gamma_k(W)}(B)
\tag{6}
\]

and

\[
\nu_{k,W}^{\mathrm{RG}}(dB)=
\frac{
\chi_k(B)e^{\Psi_k^{\mathrm{RG}}(W,B)}
d\mu_{\Gamma_k(W)}(B)
}{Z_k^{\mathrm{RG}}(W)}.
\tag{7}
\]

This is the normalized probability law attached to the printed Eq. (2.13)
fluctuation integral. For every fixed admitted real \(W\),

\[
0<Z_k^{\mathrm{RG}}(W)<\infty.
\tag{8}
\]

Indeed, Note 0008 keeps the complete cutoff cube in the real analytic chart
and fixes the positive orientation of the coordinate determinant. On the real
slice the Gaussian density is strictly positive, the full exponent is real
and finite, and the cube has positive finite Lebesgue measure. Its compact
closure gives finiteness. Pushing (7) forward by
\(B\mapsto\mathscr U_k(W,B)\) gives a probability carried by the complete
selected near-identity branch.

With the paper's normalized Gaussian convention, the logarithm of (6) is
exactly the Eq. (2.13) fluctuation contribution. The broader Eq. (2.12) action
formula also contains factors depending on \(W\) and \(g_k\) but not on \(B\)
or the external observable source. Such scalars cancel from (7). Only those
factors may be omitted projectively; Eq. (5) and every other \(B\)-dependent
factor remain.

## Local background analyticity

Let \(w\) be a coordinate on one relatively compact Proposition 9 patch from
Note 0009, and put

\[
a=g_kB,
\qquad
\mathcal Q_{\varepsilon _1}
=\{a:\lVert a\rVert_\infty<\varepsilon _1\}.
\tag{9}
\]

When (7) is written relative to the product Lebesgue measure \(da\), its
normalized ratios are unchanged if the Gaussian's scalar normalization is
dropped. The resulting fixed-domain density is

\[
q_k^{\mathrm{RG}}(w,a)=
\exp\!\left[
-\frac12\langle a,H_k(w)a\rangle
+\widehat\Psi_k^{\mathrm{RG}}(w,a)
\right],
\tag{10}
\]

where

\[
H_k(w)=g_k^{-2}\Gamma_k(W(w))^{-1},
\qquad
\widehat\Psi_k^{\mathrm{RG}}(w,a)
=\Psi_k^{\mathrm{RG}}(W(w),a/g_k).
\tag{11}
\]

RG I Eq. (3.1) specifically extends
\(P^{(k)}(g_k,U_{k+1},B)\) to
\(P^{(k)}(g_k,U,J,B)\). RG I Section 3 constructs the other terms in
\(R_{(2.12)}^{(k)}\), and RG II states that the required functions, operators,
quadratic forms, and covariances are analytic in its \((U,J)\) domain.
Proposition 9 provides the local analytic background lift, while RG II
Eq. (1.20) keeps the whole closed cube inside that common domain. Thus (10) is
jointly real analytic on a neighborhood of the compact real patch and cube and
has a local holomorphic extension.

For every real \(w_0\), shrink to a complex neighborhood \(\Omega_{w_0}\) on
which the source-free denominator stays nonzero. If \(F(w,a)\) is holomorphic
near \(\Omega_{w_0}\times\overline{\mathcal Q}_{\varepsilon _1}\), with a
common compact-domain majorant, then

\[
w\longmapsto
\frac{
\int_{\mathcal Q_{\varepsilon _1}}
F(w,a)q_k^{\mathrm{RG}}(w,a)\,da
}{
\int_{\mathcal Q_{\varepsilon _1}}
q_k^{\mathrm{RG}}(w,a)\,da
}
\tag{12}
\]

is holomorphic. On the real slice, (12) makes
\(w\mapsto\nu_{k,W(w)}^{\mathrm{RG}}\) a patchwise Borel probability kernel
in the independent-coordinate space.

For a differentiable real test \(O(w,a)\), differentiation on the fixed cube
gives the exact centered-score formula

\[
D_\xi\mathbb E_{\nu_w^{\mathrm{RG}}}O
=\mathbb E_{\nu_w^{\mathrm{RG}}}[D_\xi O]
+\operatorname{Cov}_{\nu_w^{\mathrm{RG}}}\!\left(
O,
D_\xi\!\left[
\widehat\Psi_k^{\mathrm{RG}}
-\frac12\langle a,H_k(w)a\rangle
\right]
\right).
\tag{13}
\]

There is no cutoff-boundary term: (9) is the same domain for every \(w\).

## Scalar plaquette source

For \(SU(2)\), let \(f\) be real and finitely supported (automatically a
finite sum on the fixed torus). Define the field observable and its coordinate
pullback by

\[
\mathcal O_f^{\mathrm{field}}(U)=
4\sum_p f_p\left(
1-\frac12\operatorname{Tr}U_p
\right),
\qquad
\mathcal O_f(w,a)=
\mathcal O_f^{\mathrm{field}}
\big(\mathscr U_k(W(w),a/g_k)\big),
\tag{14}
\]

using the holomorphic trace expression on the complexified patch. Define

\[
R_{k,w}^{\mathrm{RG}}(z;f)=
\frac{
\int_{\mathcal Q_{\varepsilon _1}}
e^{-z\mathcal O_f(w,a)}q_k^{\mathrm{RG}}(w,a)\,da
}{
\int_{\mathcal Q_{\varepsilon _1}}
q_k^{\mathrm{RG}}(w,a)\,da
}.
\tag{15}
\]

This ratio is jointly holomorphic in \(w\in\Omega_{w_0}\) and entire in
\(z\). It is a positive-probability expectation only for real \(w\). On that
real slice, Note 0007 gives

\[
R_{k,w}^{\mathrm{RG}}(z;f)\ne0
\quad\text{for}\quad
|z|<\frac{\log 2}{4\sum_p|f_p|},
\tag{16}
\]

with the stated \(f=0\) convention, and

\[
\partial_z\log R_{k,w}^{\mathrm{RG}}(0;f)
=-\mathbb E_{\nu_{k,W(w)}^{\mathrm{RG}}}\mathcal O_f,
\qquad
\partial_z^2\log R_{k,w}^{\mathrm{RG}}(0;f)
=\operatorname{Var}_{\nu_{k,W(w)}^{\mathrm{RG}}}(\mathcal O_f).
\tag{17}
\]

A smaller closed source disk persists on a sufficiently thin complex
background tube by compactness and continuity. The explicit real-slice radius
in (16) is not asserted throughout the original complex neighborhood.
Inserting the factor \(e^{-z\mathcal O_f}\) after the source-independent RG-I
coordinate changes is this repository's finite-dimensional corollary; RG I/II
do not print a scalar-source or marked-polymer theorem.

## Real coarse-gauge covariance

Let \(u\) be a real coarse gauge transformation and use the precise lift and
coordinate actions of Note 0009. RG I Eq. (2.16) states that the entire Eq.
(2.12) integrand and its Gaussian measure are invariant; it also states that
\(\chi_k\) is invariant because the coordinate action is local and
orthogonal. Therefore, whenever \(W\) and \(W^u\) are admitted in
equivariantly transported charts,

\[
(R_I(v))_*\nu_{k,W}^{\mathrm{RG}}
=\nu_{k,W^u}^{\mathrm{RG}}.
\tag{18}
\]

The reconstructed field intertwines by Note 0009 Eq. (18), so every
gauge-invariant reconstructed observable has equal expectation at \(W\) and
\(W^u\). This is a real, transported-chart statement, not a global gauge-slice
or complex-gauge theorem.

## Operational first-jet target

The exact first jet obtained by inserting the scalar source into the RG-I
Eq. (2.13) coordinate law is now named as the operational target for a new
marked extension of the RG-II fluctuation/cluster construction:

\[
\mathcal J_f^{\mathrm{RG}}(W)=
\mathbb E_{\nu_{k,W}^{\mathrm{RG}}}
\big[\mathcal O_f^{\mathrm{field}}(\mathscr U_k(W,B))\big]
-\mathcal O_f^{\mathrm{field}}(U_1(W)).
\tag{19}
\]

Program 003 may target a marked-polymer expansion for (19). It may not call
(19) the exact intrinsic-coarea conditional jet or the unrestricted raw-fiber
conditional jet until a separate density-matching theorem is proved.

## Exact boundary

- The law is the exact normalized RG-I Eq. (2.13) selected-coordinate law, not
  the intrinsic Note 0008 coarea law or the unrestricted raw transform.
- No \(B\)-dependent factor in Eq. (2.12) may be dropped. Projective invariance
  removes only source-independent factors constant in \(B\).
- The background analyticity and covariance are patch local; there is no
  globally holomorphic probability kernel or regulator-uniform
  complex-background radius.
- The fixed cutoff is the coupling-independent option as a set in
  \(a=g_kB\). No coupling derivative or coupling-independent raw-transform
  identity is inferred for (7).
- No remote branch, large-field complement, source-marked polymer estimate,
  RG iteration, continuum construction, infrared statement, or mass gap
  follows.

## Falsification checks

- Omit the determinant term (5) or any other coordinate-dependent term and
  verify that the resulting probability need not equal the Eq. (2.13) law.
- Multiply the density by a nonconstant positive function of \(B\) and observe
  that projective invariance does not protect normalized expectations.
- Differentiate after replacing (9) by a moving cutoff and recover a boundary
  contribution missing from (13).
- Use the complexified density as if it were positive and locate the lost
  probabilistic interpretation.
- Identify \(\nu^{\mathrm{RG}}\) with \(K^{\mathrm{chart}}\) without the full
  Haar, scaling, delta-Jacobian, gauge-weight, and Gaussian ledger; this is the
  forbidden normalization shortcut.
