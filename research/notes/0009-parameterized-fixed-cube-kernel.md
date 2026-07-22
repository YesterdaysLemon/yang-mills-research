# Note 0009: a parameterized fixed-cube branch kernel

Claim ID: YM-RG-009

Kind: primary-source corollary plus finite-dimensional parameter analysis

Evidence: E2 (finite-regulator, patch-local selected-branch statement;
internally checked)

Novelty: none claimed

## Frozen patch

Retain Note 0005's density and normal-Jacobian conventions, and retain every
map-specific hypothesis of Notes 0006 and 0008. Do **not** import Note 0005's
global properness or surjectivity hypotheses. Fix one finite regulator and RG
step, normalized product Haar measures, bi-invariant product group metrics and
their Ad-invariant Lie-algebra inner products, the selected bonds \(b_0(c)\),
and the fixed Eq. (2.9) cutoff

\[
\mathcal Q_{\varepsilon _1}
=\{a\in\mathfrak g^{I_k}:\|a\|_\infty<\varepsilon _1\}.
\tag{1}
\]

The norm in (1) is RG I's exact conjugation-invariant cutoff norm (equivalently
its fixed normalized matrix norm in the chosen representation); it is not
redefined by this note. Lebesgue measure \(da\), Gram adjoints, and determinants
below use the fixed Ad-invariant inner product and a fixed oriented orthonormal
basis of the independent-coordinate space.

Fix an admitted real coarse background \(W_0\). Let

\[
P\Subset P_{\mathrm{var}}
\tag{2}
\]

be a connected real-analytic coordinate ball around \(W_0\) contained in
one gauge-fixed Section G/Proposition 9 background branch of Bałaban's
variational paper. Shrink \(P\), if necessary, so that:

1. the selected bonds \(b_0(c)\) do not change on \(P\);
2. their defining coefficient matrices remain invertible on \(\overline P\);
3. \(\overline P\times\overline{\mathcal Q}_{\varepsilon _1}\) remains, with
   strict margin, in every logarithm, averaging, gauge, and RG-I/II analytic
   domain used below.

This is one named relatively compact chart. It is not an atlas over all
admitted backgrounds.

## Joint branch parameterization

Write the RG-I reconstruction from Note 0008 as

\[
\beta_W(a)
=C_Wa-h_W\widetilde D_W(C_Wa),
\qquad
\Phi(W,a)=\exp(i\beta_W(a))V^{(k)}(W).
\tag{3}
\]

Here \(a\) consists of all independent-bond coordinates. Then \(\Phi\) is
jointly real analytic on a neighborhood of
\(\overline P\times\overline{\mathcal Q}_{\varepsilon _1}\), and, for each
\(W\in P\), \(a\mapsto\Phi(W,a)\) is Note 0008's embedding of the complete
selected fixed-cutoff branch \(\mathcal C_{k,W}\).

The parameter dependence is not an inference from separate, pointwise
analyticity. It follows from the construction. Proposition 9 supplies the
analytic gauge-fixed background branch, and RG I's analytic averaging maps
therefore make \(V^{(k)}(W)\) analytic. The relative constraint
\(\widetilde Q_W(X)\) of RG I Eqs. (2.2)--(2.4) is jointly analytic in
\((W,X)\). If

\[
A_W=D_X\widetilde Q_W(0),
\tag{4}
\]

then the selected coefficient inverse \(h_W\), characterized by its support
on the \(b_0(c)\) bonds and \(A_Wh_W=I\), is analytic on \(P\). With \(\iota\)
the insertion of independent coordinates,

\[
C_W=\iota-h_WA_W\iota
\tag{5}
\]

is the analytic embedding into \(\ker A_W\). To justify the parameter in the
nonlinear correction, write

\[
R_W(X)=\widetilde Q_W(X)-A_WX,
\qquad
G(W,X,D)=D-R_W(X-h_WD).
\tag{6}
\]

The RG-I correction is the unique solution of \(G=0\), and
\(\Theta_W(X)=X-h_W\widetilde D_W(X)\). At a real solution,

\[
D_DG
=I+(D R_W)_{\Theta_W(X)}h_W
=(D\widetilde Q_W)_{\Theta_W(X)}h_W.
\tag{7}
\]

This derivative is invertible throughout the closed cube. Indeed, Note 0008
proves

\[
(D\widetilde Q_W)_{\Theta_W(X)}D\Theta_W(X)=A_W
\tag{8}
\]

and that \(D\Theta_W(X)\) is invertible. Projection to the independent bonds
is unchanged by \(D\Theta_W\), so it preserves the selected-coordinate space
\(\operatorname{im}h_W\). Thus
\(D\Theta_W(X)h_W=h_WK_{W,X}\) for an invertible square matrix \(K_{W,X}\).
Multiplying (8) by \(h_W\) gives

\[
\big((D\widetilde Q_W)_{\Theta_W(X)}h_W\big)K_{W,X}=I,
\]

which proves invertibility in (7). The parameterized analytic implicit
function theorem now applies at every point of the compact real set. A finite
cover and RG-I uniqueness glue the local solutions. RG II Eq. (1.20) is used
only to keep the whole closed cube in the common analytic domain. This proves
the joint continuation asserted in (3).

The support property of the correction remains exact:

\[
\beta_W(a)(b)=a(b),\qquad b\in I_k.
\tag{9}
\]

Consequently the sharp cutoff pulls back to the same cube (1) for every
\(W\in P\). There is no background-dependent integration boundary.

## Analytic coarea density

Let \(F_k\) be the selected constraint map. In the density conventions of
Note 0005, define on the fixed cube

\[
q(W,a)=
\frac{\rho_M(\Phi(W,a))}
     {\rho_N(W)J_{F_k}(\Phi(W,a))}
\sqrt{\det G(W,a)},
\qquad
G=(D_a\Phi)^*D_a\Phi .
\tag{10}
\]

All adjoints and square roots in (10) are real. Note 0008 proves that \(F_k\)
is a submersion and \(D_a\Phi\) is injective on the whole cube. Thus the
squared normal and tangent Gram determinants are positive real-analytic
functions on the compact closure. Their positive real square roots are real
analytic. The Haar-coordinate densities are positive analytic functions (and
are constant if the Haar measures are represented by the corresponding
normalized invariant Riemannian volumes). Hence

\[
0<m_P\le q(W,a)\le M_P<\infty
\tag{11}
\]

on \(\overline P\times\overline{\mathcal Q}_{\varepsilon _1}\). The constants
may depend on this patch, regulator, scale, and volume.

For every Borel set \(A\) of fine configurations, set

\[
K_k^{\mathrm{chart}}(W,A)
=\int_{\mathcal Q_{\varepsilon _1}}
  \mathbf1_A(\Phi(W,a))q(W,a)\,da.
\tag{12}
\]

With the product Lebesgue convention fixed above, (12) is exactly the pullback
of Note 0008's intrinsic coarea
restriction. It has the following consequences on \(P\).

1. \(K_k^{\mathrm{chart}}\) is a finite positive Borel kernel: for fixed
   Borel \(A\), \(W\mapsto K_k^{\mathrm{chart}}(W,A)\) is Borel.
2. Its total mass is nonzero, with a positive lower bound on this fixed compact
   patch. This is not a regulator-uniform lower bound.
3. If \(\varphi\) is bounded Borel, its test integral is Borel. If \(\varphi\)
   is \(C^r\) on a neighborhood of the compact branch image
   \(\Phi(\overline P\times\overline{\mathcal Q}_{\varepsilon _1})\), with
   the required derivatives continuous there, the test integral is \(C^r\).
   If \(\varphi\) has a common holomorphic extension near the complexified
   compact image, then its real restriction gives

   \[
   W\longmapsto
   \int\varphi(U)K_k^{\mathrm{chart}}(W,dU)
   \tag{13}
   \]

   is real analytic.

The proof is direct parameter integration on the fixed finite-dimensional
cube. Every required \(C^r\) derivative extends continuously to the compact
closure and therefore has a constant integrable majorant. The analytic clause
uses the common holomorphic extension and its Cauchy bounds. This proves weak or
test-integral regularity; it does not make \(W\mapsto K(W,A)\) continuous or
analytic for an arbitrary Borel set \(A\).

There is also a local complex consequence. The globally defined positive
real-analytic function \(q\) in (10) has a unique local holomorphic germ along
the real coordinate ball and compact cube. These germs agree on overlaps and,
after shrinking to a sufficiently thin complex neighborhood, give a
nonvanishing holomorphic extension \(q_{\mathbb C}\). Equivalently, one may
complexify the real Gram determinants using transpose rather than Hermitian
adjoint and choose the branches agreeing with the positive real roots. For a
test \(\varphi\) with a holomorphic extension and a common compact-domain
majorant, (13) has a local holomorphic continuation obtained by integrating
the complexified density over the same real cube. This does not define a
positive measure at complex \(W\), a canonical complex coarea law, or a
regulator-uniform complex radius.

## Coarse-gauge covariance

Let \(u\) be a real coarse gauge transformation and let \(v=\widetilde u\) be
the precise fine lift supplied by variational Eq. (181): it is constant on the
prescribed blocks and agrees with \(u\) at their coarse representatives. On
coarse bonds, fine configurations, relative fields, independent
coordinates, and constraint coordinates write respectively

\[
W^u(c)=u(c_-)W(c)u(c_+)^{-1},
\quad
(\Gamma_vU)(b)=v(b_-)U(b)v(b_+)^{-1},
\tag{14}
\]

\[
(R_b(v)X)(b)=\operatorname{Ad}_{v(b_-)}X(b),
\quad R_I(v)=R_b(v)|_{I_k},
\quad
(R_c(u)Y)(c)=\operatorname{Ad}_{u(c_-)}Y(c).
\tag{15}
\]

Assume \(W\) and \(W^u\) are admitted and choose the target chart by
equivariantly transporting the source chart. Variational Eq. (181), covariance
of the RG-I constraint, and uniqueness of the selected constructions give

\[
V^{(k)}(W^u)=\Gamma_vV^{(k)}(W),
\qquad
\widetilde Q_{W^u}(R_b(v)X)=R_c(u)\widetilde Q_W(X),
\tag{16}
\]

\[
h_{W^u}R_c(u)=R_b(v)h_W,
\quad
C_{W^u}R_I(v)=R_b(v)C_W,
\quad
\widetilde D_{W^u}(R_b(v)X)
=R_c(u)\widetilde D_W(X).
\tag{17}
\]

The last three identities are consequences of uniqueness, not separately
printed formulas. Substitution into (3) yields the exact intertwiner

\[
\beta_{W^u}(R_I(v)a)=R_b(v)\beta_W(a),
\qquad
\Phi(W^u,R_I(v)a)=\Gamma_v\Phi(W,a).
\tag{18}
\]

Each adjoint action in (15) is orthogonal for the fixed Ad-invariant real inner product,
so \(R_I(v)\) preserves both Lebesgue measure and the cutoff cube. Product
Haar measures and the chosen metrics are invariant, and equivariance of
\(F_k\) preserves its normal Jacobian. Changing variables in (12) therefore
gives the pointwise Radon-measure identity

\[
(\Gamma_v)_*K_k^{\mathrm{chart}}(W,\cdot)
=K_k^{\mathrm{chart}}(W^u,\cdot).
\tag{19}
\]

In particular, the integral of every gauge-invariant test is unchanged.
RG I Eq. (2.16) independently states the corresponding invariance for all
expressions and the Gaussian measure in its Eq. (2.12) representation.
Equation (19), however, concerns the intrinsic real coarea restriction and
does not identify its normalization term by term with that later Gaussian
representation.

## Weighted and source-inserted consequence

Let \(S(W,U)\) be a specifically named jointly real-analytic real branch
weight on a joint neighborhood of the compact graph
\(\{(W,\Phi(W,a)):W\in\overline P,
a\in\overline{\mathcal Q}_{\varepsilon _1}\}\). Require the explicit
covariance

\[
S(W^u,\Gamma_vU)=S(W,U).
\]

Define

\[
Z(W)=\int e^{-S(W,U)}K_k^{\mathrm{chart}}(W,dU),
\qquad
\nu_W(dU)=Z(W)^{-1}e^{-S(W,U)}K_k^{\mathrm{chart}}(W,dU).
\tag{20}
\]

Then \(Z\) is positive and real analytic on the real patch, has a positive
minimum on every compact subpatch, and normalized analytic test expectations
are real analytic. They have local holomorphic continuations wherever the
complexified denominator remains nonzero. Equations (19) and the displayed
covariance give \((\Gamma_v)_*\nu_W=\nu_{W^u}\).

For a bounded analytic plaquette insertion \(\mathcal O_f\), the joint
source integral

\[
Z(W,z;f)=
\int e^{-S(W,U)-z\mathcal O_f(U)}
K_k^{\mathrm{chart}}(W,dU)
\tag{21}
\]

is locally holomorphic in the complexified background and entire in \(z\).
On the positive **real** background slice, Note 0007 supplies its explicit
zero-free source disk and exact first two log-source jets. A strictly smaller
closed source disk remains zero-free after shrinking to a sufficiently thin
complex background tube by compactness and continuity; the original explicit
radius is not asserted throughout that tube. Merely assuming pointwise
integrability of an unnamed \(S_{k,x,W}\) would not imply any joint background
regularity; (20) requires
the displayed joint hypothesis or an exact RG-I/II weight whose analyticity
has been transcribed.

## Exact boundary

- This is one relatively compact Proposition 9 patch. Compatibility of
  independently selected patches and a global admitted-background atlas are
  not proved.
- Gauge covariance is for real coarse transformations with the prescribed
  block-constant lift and an equivariantly transported chart. Complex gauge
  transformations need not preserve the real cube or positive measure.
- The selected branch need not be saturated under arbitrary fine gauge
  transformations that are the identity on the coarse lattice.
- Borel-kernel and analytic-test regularity do not imply total-variation
  continuity or regularity of arbitrary Borel-set evaluations.
- A moving cutoff, a changing set of selected bonds, or an additional
  background-dependent characteristic function would invalidate the
  fixed-domain differentiation argument.
- No equality or comparison with the unrestricted raw group-delta fiber is
  proved. The intrinsic coarea normalization is still not matched term by
  term to every Haar, Gaussian, scaling, and determinant convention in RG I
  Eq. (2.12).
- No source-marked polymer estimate, uniform patch radius, RG iteration,
  continuum construction, infrared estimate, or mass gap follows.

## Falsification checks

- Replace the fixed cube by
  \(\int_{-1}^1\mathbf1_{\{|a-W|<1/2\}}da\) and recover the lost smoothness at
  a moving boundary.
- Take \(K_W=\delta_W\): analytic tests vary analytically, while
  \(K_W(A)=\mathbf1_A(W)\) can be discontinuous.
- Specify a non-Borel parameter choice in a separately analytic family and
  verify that pointwise analyticity alone gives no Borel kernel.
- Complexify (10) with a Hermitian norm and observe the forbidden dependence on
  complex conjugates; the holomorphic continuation uses the analytic
  bilinear complexification.
- Approach the boundary of the Proposition 9 domain and reject any claim that
  the patch-specific lower bound or complex radius remains uniform.
- Choose unrelated charts at \(W\) and \(W^u\); without equivariant transport,
  (18) is not supplied by the cited sources.
