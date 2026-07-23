# Note 0037: elliptic range factorization and the coarse-curl Stokes obstruction

Claim ID: YM-RG-037

Kind: exact differentiated-background factorization, finite-dimensional
constraint-slice theorem, and source-normalized flat-Cartan finite-model
Stokes obstruction

Evidence: E2 (direct primary-source normalization, exact finite-dimensional
algebra, and an explicit rational constrained representative)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Averaging operations for lattice gauge
  theories*](https://doi.org/10.1007/BF01211042), especially Eqs. (14)--(15)
  on printed p. 19 and the linear \(Q_0,Q'_0\) formulas on printed p. 28;
- T. Balaban, [*Spaces of regular gauge field configurations on a lattice
  and gauge fixing conditions*](https://doi.org/10.1007/BF01466594),
  especially the definition of \(R(U_0)\) and Eq. (1.27) on printed p. 80;
- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), especially Eqs. (20)--(21),
  (129), and (174)--(190), printed pp. 281, 297, and 305--309;
- Notes 0031 and 0033--0036.

## Question left by Note 0036

Note 0036 isolates the sharp joint physical-\(U/J\) quotient-synthesis
constant. Its logical transverse example does not yet obey the actual
differentiated averaging and projected-Landau equations. This leaves a
specific possible escape:

> Do the actual range equations or the differentiated Hessian equation force
> every localized same-cell source column to gain two powers of its output
> scale?

This note gives a negative answer for strong raw/gradient/curl control in a
source-normalized homogeneous one-step Cartan model of those constraints. It
does **not** identify that model with the paper's full multiscale \(H_1\)
source patch, prove that a completed coefficient detects the modeled range,
or close the physical first jet.

## Measure-normalized physical columns

Let \(c\) denote a physical coarse-source coordinate and let \(\mu_c\) be its
source measure. Retain Note 0033's density convention

\[
D_B\mathcal H[h]
=
\sum_c\mu_c A_c h_c.
\tag{1}
\]

The actual coordinate column is therefore

\[
\boxed{\kappa_c:=\mu_cA_c.}
\tag{2}
\]

At a fixed source center \(\bar B\), define

\[
\begin{aligned}
C_{\bar B}a
&:=
\bigoplus_j
D_2Q_j\!\left(U_k,\eta\mathcal H(\bar B)\right)[\eta a],\\
S_{\bar B}a
&:=
R(U_k)D_{U_k}^{\eta *}a.
\end{aligned}
\tag{3}
\]

The background \(U_k\) is fixed while \(B\) is differentiated. Differentiating
variational-paper Eqs. (20)--(21) gives

\[
\boxed{
C_{\bar B}\kappa_c=e_c,
\qquad
S_{\bar B}\kappa_c=0.
}
\tag{4}
\]

Thus the right-inverse equation applies to \(\kappa_c=\mu_cA_c\), not to the
density \(A_c\) without its measure.

## The constraints define an affine slice

Let \(X,Y,Z\) be finite-dimensional complex Hilbert spaces, and let

\[
C:X\to Y,
\qquad
S:X\to Z.
\tag{5}
\]

Assume \(C|_{\ker S}\) is onto. Put

\[
\mathcal Z:=\ker C\cap\ker S.
\tag{6}
\]

Choose any right inverse \(H:Y\to\ker S\) of \(C|_{\ker S}\). Then the complete
solution set of

\[
C\kappa=e,
\qquad
S\kappa=0
\tag{7}
\]

is

\[
\boxed{\kappa=He+\mathcal Z.}
\tag{8}
\]

With the inherited Hilbert structures, the minimum-norm base point is

\[
\kappa^\dagger
=
C_G^*(C_GC_G^*)^{-1}e,
\qquad
C_G:=C|_{\ker S}.
\tag{9}
\]

For a scalar detector \(\ell\in X^*\), the constraints determine its value
precisely when

\[
\ell|_{\mathcal Z}=0.
\tag{10}
\]

Finite-dimensional annihilator duality gives the exact test

\[
\boxed{
\ell|_{\mathcal Z}=0
\quad\Longleftrightarrow\quad
\ell\in\operatorname{ran}C^*+\operatorname{ran}S^*.
}
\tag{11}
\]

Consequently, the two differentiated constraints alone cannot control a
transverse detector that is nonzero on \(\mathcal Z\). The actual Balaban
kernel is one point of (8), selected by additional elliptic equations.

## Exact source-derived elliptic factorization

The source uses three different constrained lifts:

- \(H\) is the original quadratic lift and the operator in the nonlinear
  averaging-restoration term \(HD(A')\);
- \(H_1\) is the improved constrained lift in Eqs. (174)--(177);
- \(H_0\) is the alternative better-regularity lift in Eqs. (179)--(190).

Do not identify these operators with one another or with the later
Landau-to-axial gauge transformation.

Set

\[
A_B:=\mathcal A_0(B)+H_0B,
\qquad
T_B:=D_BA_B=\frac{\delta\mathcal A_0}{\delta B}+H_0,
\qquad
W_B:=V''(A_B).
\tag{12}
\]

Immediately before Eq. (180), the paper defines

\[
\widetilde G=(\Delta_a-\Delta^{(2)})^{-1}.
\tag{13}
\]

Equation (183) is

\[
\frac{\delta\mathcal A_0}{\delta B}
+\widetilde G\,W_BT_B
=
\widetilde G\Delta^{(2)}H_0.
\tag{14}
\]

Multiplying by \(\widetilde G^{-1}\) and substituting
\(\delta_B\mathcal A_0=T_B-H_0\) gives the exact derived identity

\[
\boxed{
\bigl(\Delta_a-\Delta^{(2)}+W_B\bigr)T_B
=
\Delta_aH_0.
}
\tag{15}
\]

Differentiating Eq. (179), as printed in Eq. (182), then gives

\[
\boxed{
K_B:=D_B\mathcal H(B)
=
\bigl(I-HD'(A_B)\bigr)T_B.
}
\tag{16}
\]

On the small fixed-background Proposition-9 patch, Eq. (187) supplies the
smallness used in Eq. (188), so

\[
\boxed{
K_B
=
\bigl(I-HD'(A_B)\bigr)
\bigl(\Delta_a-\Delta^{(2)}+V''(A_B)\bigr)^{-1}
\Delta_aH_0.
}
\tag{17}
\]

Equation (129), together with the preceding definition
\(G=\Delta_a^{-1}\), states on a source \(B\)

\[
H_0B
=
GQ^*(QGQ^*)^{-1}
\bigl(L^{j(\cdot)}\eta\bigr)^{-1}B,
\qquad
G=\Delta_a^{-1}.
\tag{18}
\]

Thus the operator identity

\[
\Delta_aH_0
=
Q^*(QGQ^*)^{-1}
\bigl(L^{j(\cdot)}\eta\bigr)^{-1}
\tag{19}
\]

is an exact algebraic consequence, not a separately printed equation.
The order-\(-2\) inverse in (17) is fed by the order-\(+2\) source
\(\Delta_aH_0\). Equations (186)--(188) make the nonlinear term small in the
existing scaled raw/gradient norm; they print no additional positive power of
the output scale.

The alternative Eqs. (174)--(175) similarly give

\[
K_B
=
\bigl(I-HD'(A_B)\bigr)
\bigl(I+\mathfrak G V''(A_B)\bigr)^{-1}H_1.
\tag{20}
\]

Most importantly, Eq. (177) prints

\[
\mathcal H(B)=H_1B+O(B^2),
\tag{21}
\]

and hence

\[
\boxed{K_0=H_1.}
\tag{22}
\]

Any uniform range theorem valid on a patch containing \(B=0\) must therefore
hold for the linear constrained lift \(H_1\) itself.

## Source-normalized flat-Cartan finite model

The following is not an arbitrary block map: it retains the normalizations
and flat/commuting-Cartan linear forms of the primary-source \(Q_0,Q'_0\),
and \(R\) operators. The retained papers do not, however, prove that this
homogeneous finite periodic model is an embedded patch of their full
multiscale \(H_1\) construction. That identification remains a separate
open step.

Take \(d=4\) and a periodic fine torus

\[
\Lambda_f
=
(\mathbb Z/4\mathbb Z)^2
\times
(\mathbb Z/2\mathbb Z)^2.
\tag{23}
\]

The \(L=2\) coarse torus is

\[
\Lambda_c
=
(\mathbb Z/2\mathbb Z)^2
\times
(\mathbb Z/1\mathbb Z)^2.
\tag{24}
\]

Restrict \(SU(2)\) bond fields to the Cartan line generated by

\[
H=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\tag{25}
\]

For a flat background, or for a commuting Cartan background acting on this
same Cartan line, every adjoint transport in the linear averages is the
identity.

Write dimensionless scalar bond fields as

\[
a=\eta\kappa.
\tag{26}
\]

For fields constant in the last two coordinates, combine the flat-Cartan
linearization of the nonlinear average with the \(Q_0\) formula on printed
p. 28. The resulting source-normalized finite-model bond map is

\[
\begin{aligned}
(Ca)_1(X,Y)
&=
\frac14
\sum_{r\in\{0,1\}^2}
\sum_{t=0}^1
a_1(2(X,Y)+r+te_1),\\
(Ca)_2(X,Y)
&=
\frac14
\sum_{r\in\{0,1\}^2}
\sum_{t=0}^1
a_2(2(X,Y)+r+te_2).
\end{aligned}
\tag{27}
\]

The factor \(1/4\) is the \(2^{-4}\) source average after summing the four
identical positions in the suppressed coordinates. Exact identification
with the differential of Eq. (20) on the full multiscale domain would
require the additional embedding just isolated above.

Let \(P_4\) be the full four-dimensional scalar block mean. On fields
constant in the last two coordinates, its restriction \(P\) is the
\(2\times2\) block mean

\[
\begin{aligned}
(P_4\phi)(X,Y,0,0)
&=
\frac1{16}
\sum_{\rho\in\{0,1\}^4}
\phi\bigl(2(X,Y,0,0)+\rho\bigr),\\
(P\phi)(X,Y)
&=
\frac14
\sum_{r\in\{0,1\}^2}
\phi\bigl(2(X,Y)+r\bigr).
\end{aligned}
\tag{28}
\]

Gauge-fixing printed p. 80 defines \(R(U_0)\) as the orthogonal projection
onto

\[
\Delta_{U_0}^{\eta}N(Q'(U_0)).
\tag{29}
\]

At the present background, the irrelevant positive scale in
\(\Delta^\eta\) does not change its range. The corresponding finite-model
projector is therefore the full orthogonal projection onto

\[
\Delta\ker P_4.
\tag{30}
\]

For dimensionless fields define

\[
\begin{aligned}
(d\phi)_\mu(x)
&=\phi(x+e_\mu)-\phi(x),\\
d^*a(x)
&=\sum_{\mu=1}^2
\bigl(a_\mu(x-e_\mu)-a_\mu(x)\bigr),\\
(da)(x)
&=
a_1(x)+a_2(x+e_1)-a_1(x+e_2)-a_2(x),\\
\Delta&=d^*d.
\end{aligned}
\tag{31}
\]

The last two directions make no contribution for the embedded fields.

## An exact Landau representative

Let \(e_c\) be \(1\) on the coarse positive \(1\)-bond at
\((X,Y)=(0,0)\) and \(0\) on every other coarse bond. Give \(a_1\) the
following values, with rows indexed by \(y\) and columns by \(x\):

\[
a_1=
\begin{pmatrix}
\frac14&\frac34&\frac14&-\frac14\\
\frac14&\frac34&\frac14&-\frac14\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad
a_2=0.
\tag{32}
\]

Set \(a_3=a_4=0\), extend the displayed arrays constantly in the last two
coordinates, and multiply by \(H\). Direct substitution in (27) gives

\[
Ca=e_c.
\tag{33}
\]

Let \(g=d^*a\). A direct calculation gives

\[
g=
\begin{pmatrix}
-\frac12&-\frac12&\frac12&\frac12\\
-\frac12&-\frac12&\frac12&\frac12\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\tag{34}
\]

The array \(\Delta g\) is constant on each displayed \(2\times2\) block.
Because the extension is constant in the last two coordinates, it is
therefore constant on each full \(2^4\) block. Hence

\[
\Delta g\in\operatorname{ran}P_4^*=(\ker P_4)^\perp.
\tag{35}
\]

For every \(\phi\in\ker P_4\), self-adjointness of \(\Delta\) gives

\[
\langle g,\Delta\phi\rangle
=
\langle\Delta g,\phi\rangle
=0.
\tag{36}
\]

Therefore

\[
g\perp\Delta\ker P_4,
\qquad
\boxed{Rd^*a=0.}
\tag{37}
\]

The projected Landau condition is nontrivial here:
\(\ker P_4\) has positive dimension. Equations (33) and (37) prove that the
localized right-inverse slice is nonempty.

## Discrete Stokes forces a transverse \(s^{-2}\) loss

The bond average (27) is a cochain map. Direct cancellation of interior
bonds gives

\[
d_cC=C_2d,
\tag{38}
\]

where, on the displayed \(1\)-\(2\) plane,

\[
(C_2f)(X,Y)
=
\frac14
\sum_{r\in\{0,1\}^2}
\sum_{u,v=0}^1
f(2X+r+ue_1+ve_2).
\tag{39}
\]

Every row of \(C_2\) has \(\ell^1\)-mass \(4\). Since

\[
(d_ce_c)(0,0)=1,
\tag{40}
\]

every field satisfying \(Ca=e_c\), with or without a Landau condition, obeys

\[
1
=
|(C_2da)(0,0)|
\le
4\lVert da\rVert_\infty.
\tag{41}
\]

Thus

\[
\boxed{\lVert da\rVert_\infty\ge\frac14.}
\tag{42}
\]

The selected row of \(C\) has \(\ell^1\)-mass \(2\), so

\[
\boxed{\lVert a\rVert_\infty\ge\frac12.}
\tag{43}
\]

If

\[
\lVert\delta a\rVert_\infty
:=
\max_{x,\mu,\nu}
|a_\mu(x+e_\nu)-a_\mu(x)|,
\tag{44}
\]

then \(\lVert da\rVert_\infty\le2\lVert\delta a\rVert_\infty\). Therefore

\[
\boxed{\lVert\delta a\rVert_\infty\ge\frac18.}
\tag{45}
\]

Let

\[
s=2\eta,
\qquad
\kappa=\eta^{-1}a.
\tag{46}
\]

With the source's scaled derivative conventions,

\[
\lVert\kappa\rVert_\infty
=\eta^{-1}\lVert a\rVert_\infty,
\quad
\lVert\nabla^\eta\kappa\rVert_\infty
=\eta^{-2}\lVert\delta a\rVert_\infty,
\quad
\lVert d^\eta\kappa\rVert_\infty
=\eta^{-2}\lVert da\rVert_\infty.
\tag{47}
\]

Equations (42)--(45) give the exact lower bounds

\[
\boxed{
\lVert\kappa\rVert_\infty\ge s^{-1},
\qquad
\lVert\nabla^\eta\kappa\rVert_\infty\ge\frac12s^{-2},
\qquad
\lVert d^\eta\kappa\rVert_\infty\ge s^{-2}.
}
\tag{48}
\]

The representative (32) supplies matching upper bounds up to fixed numerical
constants:

\[
\lVert\kappa\rVert_\infty\le\frac32s^{-1},
\qquad
\lVert\nabla^\eta\kappa\rVert_\infty,
\ \lVert d^\eta\kappa\rVert_\infty
\le3s^{-2}.
\tag{49}
\]

The \(s^{-2}\) power is therefore unavoidable and order-sharp in this
source-normalized finite model. Projected Landau changes the longitudinal
representative but cannot change the block curl fixed by (38)--(40).

## Consequence and missing embedding

At \(B=0\), Eq. (22) identifies the paper's actual kernel with \(H_1\).
Equations (38)--(48) show that any realization of its localized Cartan column
inside the homogeneous model above would retain the same lower bounds,
independently of the Hessian selector. What is not proved here is that the
paper's full multiscale domain, complete \(Q'\) nullspace, and boundary
conditions admit this homogeneous periodic reduction.

The finite model therefore rules out deriving the following conclusion from
the normalized right-inverse and projected-Landau constraints alone:

> derive a regulator-uniform two-power strong-norm gain for every localized
> same-cell column solely from right-inverse normalization and projected
> Landau orthogonality.

It does not rule out a gain produced by the full multiscale Hessian selector
or by boundary/domain structure absent from the finite model.

The obstruction is transverse. If \(a\mapsto a+d\phi\) is an admitted
linearized gauge change with \(P_4\phi=0\), then

\[
C(a+d\phi)=Ca,
\qquad
d(a+d\phi)=da.
\tag{50}
\]

Thus quotienting gauge directions cannot erase the coarse-curl aggregate.
This does not show that every completed coefficient detects it. A completed
weak-dual theorem could still annihilate this range for a structural reason.

## What remains viable

The exact factorization and finite-model Stokes obstruction narrow the
remaining options:

1. prove or disprove the homogeneous Cartan model's embedding into the full
   multiscale \(H_1\) domain, with the complete \(Q'\) constraint;
2. prove that the completed physical coefficient derivative annihilates the
   resulting coarse-curl range after the simultaneous \(U/J\) Ward quotient;
3. prove a completed derivative estimate directly in a weak quotient dual
   that does not dominate the strong curl/gradient norm;
4. justify a physical source class whose coarse one-form is curl-free,
   smoothed, weighted, or separated from the tested output cell;
5. construct a range-restricted analytic tube whose radius scales together
   with the unavoidable transverse column; or
6. reorganize the observable/source coordinates before coefficientwise
   absolute summation.

The first option is a statement about actual completed activities, not about
the background propagator alone.

## Exact boundary

- Equations (4), (8), and (11) are exact finite-dimensional range statements
  after the physical source convention is fixed.
- Equations (15)--(17) are exact consequences of variational-paper
  Eqs. (182)--(183), on its fixed-background small patch.
- Equation (19) is an exact consequence of Eq. (129) and
  \(G=\Delta_a^{-1}\), not a separately printed identity.
- Equation (22) is the exact derivative at the origin of the source-printed
  expansion (177).
- Equations (27)--(30) form a source-normalized \(L=2\), homogeneous
  flat/commuting-Cartan finite model of the linear \(Q_0,Q'_0\), and Landau
  projector.
- Equations (32)--(49) give an exact rational constrained representative and
  a Stokes lower bound for a localized coarse bond.
- Embedding that model into the source's full multiscale \(H_1\) domain and
  complete \(Q'\) nullspace is not proved.
- No completed coefficientwise Ward identity, annihilation of the transverse
  range, converted physical column through every chart/restoration step,
  nonzero-source polymer disk, continuum construction, infrared theorem, or
  mass gap is proved.
- No independent human review has been performed.

## Falsification checklist

- Apply (4) to \(A_c\) rather than \(\kappa_c=\mu_cA_c\).
- Confuse \(H,H_0,H_1\), or confuse the \(HD(A')\) averaging restoration with
  the later Landau-to-axial gauge transformation.
- Call (19) a literal printed display rather than an exact consequence of
  Eq. (129).
- Read the inverse in (17) as a two-power gain while discarding its
  \(\Delta_aH_0\) source.
- Replace the projected condition \(RD^*K=0\) by \(D^*K=0\). The explicit
  representative only proves the former.
- Drop the factor \(\eta\) in \(a=\eta\kappa\), or replace the source's
  \(L^{-d}\) path average by an unnormalized path sum.
- Miss the block-average multiplicity in (27) or the row mass \(4\) in (39).
- Use the Stokes lower bound for a curl-free coarse source; its premise is
  the localized coarse bond with \(d_ce_c\ne0\).
- Call the finite periodic model an actual \(H_1\) source slice without
  proving the full multiscale \(Q'\), domain, and boundary embedding.
- Promote the one-block Cartan strong-norm obstruction to a theorem that all
  completed coefficients detect it.
- Promote any statement in this note to a continuum construction, infrared
  mass-gap estimate, or solution of the Yang--Mills problem.
