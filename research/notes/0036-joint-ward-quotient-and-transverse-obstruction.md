# Note 0036: joint Ward-quotient synthesis and the same-cell transverse obstruction

Claim ID: YM-RG-036

Kind: exact joint physical-\(U/J\) quotient theorem, vertical scale-transfer
lemma, and sharp transverse obstruction

Evidence: E2 (finite-dimensional phase/quotient duality, direct
primary-source normalization, and explicit analytic countermodels; the
completed Ward identity and converted physical columns remain hypotheses)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), especially Eqs.
  (20)--(21), (173), (179), (182), (184), and (190), printed pp. 281,
  305--308, and Proposition 9 on printed p. 309;
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), especially Eqs.
  (2.46), (2.60), and (2.68)--(2.69), printed pp. 231 and 234--235;
- Notes 0016, 0029, and 0030--0035.

## Question left by Note 0035

Note 0035 proves that diagonal \(s_j,s_j^2\) renorming cannot replace the
strong physical-\(U\) chart norm. Two possible escapes remain:

1. combine the physical \(U\)- and induced \(J\)-summands before taking
   absolute values and use the Ward identity; or
2. use multiscale distance or a signed identity of the actual kernel to
   remove the output powers before generic Cauchy.

This note proves the exact gain available from the first idea, the exact
vertical trade available from the second, and the obstruction that remains.

## The exact joint physical column

Fix one completed coefficient \(F\) at a retained real center
\((\bar U,J_0)\). Write

\[
\ell_U:=D_U^\Phi F,
\qquad
\ell_J:=D_JF.
\tag{1}
\]

For a relative tangent \(a\), Note 0016 gives the exact induced auxiliary
variation

\[
L_{\bar U}a
:=
D\mathscr J_\xi(\bar U)[i\xi a\bar U]
=
D_{\bar U}^{\xi *}D_{\bar U}^{\xi}a
+D_A\mathfrak R(\bar U,0)[a].
\tag{2}
\]

Here \(\mathfrak R\) is Balaban's local remainder in the auxiliary-field
formula (denoted \(F\) in that source), not the completed coefficient fixed
above.

Let

\[
\alpha=(\vartheta,j',y'),
\qquad
\mu_\alpha=(L^{j'}\eta)^d
\tag{3}
\]

be the measure-normalized physical source labels of Note 0033, and let
\(A_\alpha\) be the relative-\(U\) columns defined by

\[
D_B\mathcal U[h]
=
i\xi\left(
\sum_\alpha\mu_\alpha A_\alpha h_\alpha
\right)\bar U.
\tag{4}
\]

Because the physical \(J\) coordinate is \(\mathscr J_\xi(\mathcal U)\),
the full physical coefficient density is

\[
\boxed{
\mathcal L_\alpha^{\rm phys}
=
\ell_U[A_\alpha]
+\ell_J[L_{\bar U}A_\alpha].
}
\tag{5}
\]

Thus complex source-phase duality gives the cancellation-preserving identity

\[
\boxed{
\sum_\alpha\mu_\alpha w_\alpha
|\mathcal L_\alpha^{\rm phys}|
=
\sup_{\lVert c\rVert_{\ell^\infty}\le1}
\left|
\ell_U[\mathcal A_U^w c]
+\ell_J[L_{\bar U}\mathcal A_U^w c]
\right|,
}
\tag{6}
\]

where \(w_\alpha>0\) is any declared source weight and

\[
\mathcal A_U^w c
:=
\sum_\alpha\mu_\alpha w_\alpha c_\alpha A_\alpha.
\tag{7}
\]

Equation (6) is strictly stronger than applying the triangle inequality to
the \(U\)- and \(J\)-summands separately.

## Normalized product tube and its exact quotient

Let \(X_{\bar U,\xi}\) be Note 0031's strong relative-\(U\) space and let
\(Z_J\) be the independent-\(J\) sup-norm space. Normalize the product tube
by

\[
E_\xi
:=
X_{\bar U,\xi}\oplus_\infty Z_J,
\qquad
\lVert(a,z)\rVert_{E_\xi}
:=
\max\left\{
\frac{\lVert a\rVert_X}{r_U},
\frac{\lVert z\rVert_J}{\Delta_J}
\right\}.
\tag{8}
\]

Put

\[
V_\alpha
:=
(A_\alpha,L_{\bar U}A_\alpha),
\qquad
K_F^wc
:=
\sum_\alpha
\mu_\alpha w_\alpha c_\alpha V_\alpha.
\tag{9}
\]

Let \(N_F\subset E_\xi\) be the complex coordinate subspace of directions
invisible to the coefficient by Note 0029's external-coordinate locality.
Let

\[
\Gamma_\xi\phi
:=
(a_\phi,\delta_\phi J)
\tag{10}
\]

be the simultaneous infinitesimal gauge tangent, extended complex linearly
from the admitted real gauge-parameter space. The completed coefficientwise
Ward premise is

\[
DF(0)[\Gamma_\xi\phi]=0
\quad\hbox{for every admitted }\phi.
\tag{11}
\]

This premise is not proved for every completed coefficient in the current
repository. Define the complex subspace

\[
H_F
:=
N_F+\operatorname{ran}\Gamma_\xi.
\tag{12}
\]

Assume \(F\) is holomorphic and bounded by \(B_F\) on the unit
\(E_\xi\)-ball. Product-tube Banach-line Cauchy gives

\[
\lVert DF(0)\rVert_{E_\xi^*}
\le B_F.
\tag{13}
\]

Locality and (11) make \(DF(0)\) descend to \(E_\xi/H_F\). Applying (6)
therefore proves

\[
\boxed{
\sum_\alpha\mu_\alpha w_\alpha
|\mathcal L_\alpha^{\rm phys}|
\le
B_F
\left\|
Q_{H_F}K_F^w
\right\|_{\ell^\infty\to E_\xi/H_F}.
}
\tag{14}
\]

This is not merely a sufficient constant. Freeze a complex subspace
\(H\subset E_\xi\), the columns \(V_\alpha\), and the synthesis
\[
K^wc:=\sum_\alpha\mu_\alpha w_\alpha c_\alpha V_\alpha.
\]
Finite-dimensional quotient duality and source-phase duality give

\[
\boxed{
\begin{aligned}
&\sup_{\substack{
\lVert G\rVert_{H^\infty(B_{E_\xi})}\le B\\
DG(0)|_H=0}}
\sum_\alpha\mu_\alpha w_\alpha
|DG(0)[V_\alpha]|\\
&\qquad=
B
\left\|
Q_HK^w
\right\|_{\ell^\infty\to E_\xi/H}.
\end{aligned}
}
\tag{15}
\]

Indeed, after interchanging the two finite suprema, a quotient-norming
functional used as a linear holomorphic \(G\) attains the right-hand side.
Instantiating this frozen statement with \(H=H_F\) and the physical columns
at one fixed locality/Ward pattern shows that the quotient-synthesis norm is
the sharp coefficient-independent missing constant.

For a completed family whose coefficientwise tube majorants sum to
\(B_{\rm conn}\), a common bound

\[
\sup_F
\left\|
Q_{H_F}K_F^w
\right\|
\le C_{\rm joint}
\tag{16}
\]

would give the corresponding aggregate physical first-jet bound
\(C_{\rm joint}B_{\rm conn}\). Equation (16), not Ward covariance alone, is
the needed new theorem.

## Why separate absolute values lose a real Ward cancellation

The loss already appears on the unit bidisc. Put

\[
F(u,j)=\frac B2(u-j),
\qquad
\Gamma t=(t,t),
\qquad
V=M(1,1).
\tag{17}
\]

Then \(|F|\le B\), \(DF[\Gamma t]=0\), and the joint physical derivative
vanishes:

\[
DF[V]=0.
\tag{18}
\]

But separate absolute values give

\[
|D_UF[M]|+|D_JF[M]|=BM.
\tag{19}
\]

Taking \(M=\xi^{-2}\) shows that the separate Notes 0032/0033 estimates can
diverge even when the exact joint term cancels. The joint quotient in (14)
is therefore a genuine improvement.

## Arbitrary source phases forbid cross-column sign cancellation

For any quotient target \(E_\xi/H_F\), finite-dimensional duality gives

\[
\boxed{
\left\|
Q_{H_F}K_F^w
\right\|
=
\sup_{\substack{
\lambda\in H_F^\perp\\
\lVert\lambda\rVert_{E_\xi^*}\le1}}
\sum_\alpha
\mu_\alpha w_\alpha
|\lambda(V_\alpha)|.
}
\tag{20}
\]

The phases \(c_\alpha\) align the scalar values
\(\lambda(V_\alpha)\). Consequently cancellation between different source
columns cannot prove (16) for the full \(\ell^\infty\) source ball. In
particular, for every individual label

\[
\left\|Q_{H_F}K_F^w\right\|
\ge
\mu_\alpha w_\alpha
\left\|Q_{H_F}V_\alpha\right\|_{E_\xi/H_F}.
\tag{21}
\]

Any uniform theorem must improve or exclude each offending column after the
locality and gauge quotients, or change the source norm.

## What the source prints about the common kernel

The variational paper has one kernel,

\[
K_{\mu\nu}(B;x,y')
:=
\frac{\delta\mathcal H_\mu(B,x)}
{\delta B_\nu(y')}.
\tag{22}
\]

Equation (190) simultaneously bounds \(K\), its output gradient, localized
Hölder gradient, \(D^*DK\), and \(\Delta K\). These are rows of one kernel,
not five independent kernels. But Eq. (190) prints norms and absolute
values, not a signed raw/gradient cancellation.

Differentiating the exact average and Landau conditions (20)--(21) gives,
for each measure-normalized source column \(c\),

\[
D_AQ_j(U_k,\eta\mathcal H)
[\eta K_{\cdot,c}]
=
\mathbf e_c,
\qquad
R(U_k)D_{U_k}^{\eta *}K_{\cdot,c}=0.
\tag{23}
\]

The first identity is a right-inverse normalization; the second is a
projected output-divergence condition. They do not say
\(D^*K=0\), identify \(\Delta K\) with \(D^*DK\), or turn
\(\nabla_xK\) into a source derivative.

In particular, Eq. (190) prints no
\(\nabla_{y'}K\), no identity
\(\nabla_xK=-\nabla_{y'}K\), and no zero source moment. An output
summation by parts would move a derivative onto the activity functional and
create cell, active-set, and layer boundary terms for which no vanishing
trace is printed. The identities in (23) remain promising range constraints
for a future direct-synthesis theorem, but that theorem is not supplied by
the source or by the current converted-row hypothesis.

## Exact vertical scale transfer

Write

\[
s_j=L^j\eta,
\qquad
\lambda=\frac{\delta_0}{8}.
\tag{24}
\]

Propagators II Eq. (2.60) gives, for \(0<\alpha<1\) and after choosing
\(R,M\) to satisfy that paper's strengthened separation condition (2.59)
at this value of \(\alpha\),

\[
e^{-\alpha\delta_0 d_{\mathcal B}(y,y')}
\le
e^{-\alpha\delta_0 c_{\rm lay}
\max\{|j-j'|-1,0\}},
\qquad
c_{\rm lay}=RM.
\tag{25}
\]

Let \(q\ge0\), \(0\le\lambda'<\lambda\), and assume

\[
\alpha
:=
\frac{\lambda-\lambda'}{\delta_0}
\in(0,1),
\qquad
\frac14\alpha\delta_0RM
>
2d\log c_0(\alpha/2)+1,
\qquad
(\lambda-\lambda')c_{\rm lay}
\ge q\log L.
\tag{26}
\]

Here \(c_0\) is the Propagators II convolution constant; the middle
inequality is exactly its condition (2.59). Since
\(\lambda=\delta_0/8\), the present choice actually has
\(\alpha\le1/8\). If \(j\ge j'\), then
\(s_j^{-q}\le s_{j'}^{-q}\). If \(j<j'\), spend
\(\lambda-\lambda'=\alpha\delta_0\) in (25). The one-layer allowance costs
at most \(L^q\). Thus

\[
\boxed{
s_j^{-q}
e^{-\lambda d_{\mathcal B}(y,y')}
\le
L^q
s_{j'}^{-q}
e^{-\lambda' d_{\mathcal B}(y,y')}.
}
\tag{27}
\]

For the raw and gradient rows, take \(q=1,2\). This is a real scale trade,
of the same kind used in Propagators II Eq. (2.68), but it moves the output
loss to the input scale rather than deleting it.

Consequently a weighted source class

\[
\lVert h\rVert_{\mathsf S_q}
:=
\sup_{\alpha=(\vartheta,j',y')}
s_{j'}^{-q}|h_\alpha|
\tag{28}
\]

would absorb the transferred factor, as would source support restricted to
\(s_{j'}\ge s_*>0\) at cost \(s_*^{-q}\). Neither is the current unweighted
all-layer \(\ell^\infty\) source ball.

Indeed, Eq. (190) permits \(j'=j\) and \(y'=y\). For this diagonal label,

\[
d_{\mathcal B}(y,y')=0,
\qquad
s_j^{-q}e^{-\lambda d_{\mathcal B}(y,y')}
=s_j^{-q}.
\tag{29}
\]

The source set includes the finest layer \(j=0\), \(s_0=\eta\). Therefore
the exact distance-only moment

\[
\Gamma_q
:=
\sup_{(j,y)}
s_j^{-q}
\sum_{(j',y')}
e^{-\lambda d_{\mathcal B}(y,y')}
\tag{30}
\]

where the fixed finite source-component multiplicity is absorbed in the
normalization, obeys \(\Gamma_q\ge\eta^{-q}\) for the current all-layer
source space.
Vertical decay alone cannot prove a regulator-uniform unweighted theorem.

## A transverse same-cell column survives the Ward quotient

The longitudinal field in Note 0035 can be locally pure gauge, so the joint
quotient may remove it. A curvature-changing direction is different.

Work with \(SU(2)\), \(s=\xi\), and

\[
H=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\tag{31}
\]

Choose a commuting Cartan real background whose transports preserve the
\(H\)-direction and with one plaquette

\[
P_s=e^{ics^2H},
\tag{32}
\]

where \(c>0\) is fixed and small enough for the strict
\((\mathrm H_{\rm rc})\) curvature margin. On one oriented bond of that
plaquette put

\[
a_s(b)=s^{-1}H,
\qquad
a_s=0\quad\hbox{on the other three bonds}.
\tag{33}
\]

Then, up to fixed representation and transport constants,

\[
\lVert a_s\rVert_{\rm raw}\asymp s^{-1},
\qquad
\lVert\nabla^sa_s\rVert\asymp s^{-2},
\qquad
\lVert\mathcal D_{\bar U}^sa_s(p)\rVert\asymp s^{-2}.
\tag{34}
\]

Take one source label at the same layer and cell, with measure \(\mu_s\),
and set \(A_s=\mu_s^{-1}a_s\). It saturates the retained Eq. (190)
raw/gradient powers and pays no distance decay.

Now define the local analytic coefficient

\[
F_s(U,J)
:=
s^{-4}
\left(
1-\frac12\operatorname{Tr}dU(p)
\right).
\tag{35}
\]

It is independent of \(J\) and gauge invariant. On Note 0031's strong
product tube,

\[
dU(p)-1=O(s^2).
\tag{36}
\]

For \(dU(p)\in SL(2,\mathbb C)\),

\[
1-\frac12\operatorname{Tr}dU(p)
=
\frac12\det(dU(p)-1),
\tag{37}
\]

so \(F_s\) is bounded uniformly in \(s\). With Note 0031's transported-curl
normalization, its chart derivative at the background is

\[
DF_s(0)[a,z]
=
-\frac{i}{2s^2}
\operatorname{Tr}\left(
\mathcal D_{\bar U}^sa(p)P_s
\right).
\tag{38}
\]

Since \(\mathcal D_{\bar U}^sa\) is traceless and
\(P_s=1+ics^2H+O(s^4)\),

\[
DF_s(0)[a,z]
=
\frac c2
\operatorname{Tr}\left(
H\mathcal D_{\bar U}^sa(p)
\right)
+O\!\left(
s^2\lVert\mathcal D_{\bar U}^sa(p)\rVert
\right).
\tag{39}
\]

For the one-bond field (33), the commuting Cartan transports give
\(\mathcal D_{\bar U}^sa_s(p)=\pm s^{-2}H\). Hence (38) also gives the
exact scalar expression
\[
DF_s(0)[a_s,0]
=
\pm\frac{\sin(cs^2)}{s^4}
\asymp s^{-2}.
\]
Equations (34) and (39) therefore give

\[
\boxed{
\mu_s
|DF_s(0)[A_s, L_{\bar U}A_s]|
\asymp s^{-2}.
}
\tag{40}
\]

The derivative annihilates simultaneous gauge tangents because \(F_s\) is
gauge invariant, ignores every \(J\)-direction, and is supported on the
active plaquette. Hence the direction survives both terms in \(H_F\). Fix
unit source weight on this one label. Uniform boundedness of \(F_s\) on
the normalized product ball gives
\(C_*:=\sup_s\lVert DF_s(0)\rVert_{E_\xi^*}<\infty\). Using
\(DF_s/C_*\) as an annihilating quotient functional proves

\[
\left\|
Q_{H_F}K_F
\right\|
\ge
\frac{|DF_s(0)[K_F1]|}{C_*}
\gtrsim s^{-2}
\tag{41}
\]

for this logical model.

This is a countermodel to deriving (16) from the retained rowwise,
product-tube, locality, and Ward hypotheses. It is **not** a claim that an
actual Balaban completed coefficient equals \(F_s\), or that an actual
physical source column violates the differentiated range constraints (23).
Those constraints are the next source-specific structure to test.

## Consequence for the route

The joint theorem closes one conceptual gap: the full physical derivative
should be combined before absolute summation, and gauge directions should
be quotiented jointly with inactive directions. The exact missing constant
is (16).

The retained hypotheses do not bound it. Viable next inputs are:

1. prove from Eqs. (182)--(188), the right-inverse/Landau constraints (23),
   and the background propagator that every same-cell fine transverse
   column gains two powers;
2. prove a regulator-uniform complex tube only along the joint physical
   source range;
3. prove a completed derivative estimate directly in the weak quotient
   dual, stronger than generic product-tube Cauchy;
4. restrict and justify the physical source class to (28) or to a coarse
   source layer; or
5. prove that the completed coefficients annihilate the transverse
   same-cell range for a source-faithful structural reason.

### Follow-up in Note 0037

Note 0037 derives the exact Hessian factorization and uses the source
expansion \(D_B\mathcal H(0)=H_1\). Separately, its source-normalized
homogeneous one-step Cartan model retains a nonzero coarse curl, so discrete
Stokes forces every right inverse in that model to have gradient/curl order
\(s^{-2}\). This rules out inferring item 1 from right-inverse normalization
and projected-Landau orthogonality alone. Whether the full multiscale
\(H_1\) domain and Hessian selector embed or eliminate that mode remains
open, alongside a completed weak-dual theorem, range-restricted tube, or
justified source restriction.

## Exact boundary

- Equations (5)--(15) are exact finite-dimensional joint
  phase/quotient-duality statements after the physical columns and Ward
  premise are fixed.
- Equation (19) proves that separately taking absolute \(U\)- and
  \(J\)-summands can lose an exact Ward cancellation.
- Equations (20)--(21) prove that cross-column sign cancellation cannot
  control the full \(\ell^\infty\) source ball.
- Equation (23) records source-printed range identities but does not prove
  an improved norm for their actual range.
- Equation (27) is an exact vertical power transfer under (25)--(26);
  equations (29)--(30) prove that same-layer labels defeat a distance-only
  unweighted conclusion.
- Equations (31)--(41) give a uniformly bounded, gauge-invariant analytic
  countermodel that preserves the transverse \(s^{-2}\) loss under the
  current abstract hypotheses.
- The completed coefficientwise Ward premise, common converted physical
  columns, source-faithful use of (23), and every later construction and
  mass-gap gate remain open.
- No independent human review has been performed.

## Falsification checklist

- Bound the two physical chain-rule summands separately and claim that no
  Ward cancellation was lost.
- Quotient the \(U\)-direction alone while ignoring the induced
  \(J\)-gauge tangent.
- Use (14) without the coefficient's inactive subspace, or claim Ward
  annihilation for every completed coefficient without proving (11).
- Invoke cancellation among source columns despite the arbitrary phases in
  (20), or omit the one-coordinate lower bound (21).
- Rename the projected Landau condition in (23) as \(D^*K=0\), or turn
  \(\nabla_xK\) into a source derivative not printed in Eq. (190).
- Spend vertical decay without retaining the reduced exponent, the
  one-layer factor \(L^q\), or the input-scale factor \(s_{j'}^{-q}\).
- Exclude the diagonal \(j'=j,y'=y\) source label without a source-support
  theorem.
- Treat the logical coefficient (35) as an actual Balaban polymer
  coefficient or claim that it satisfies the still-unconverted range
  identities (23).
- Promote the joint quotient reduction or its obstruction to an
  unconditional physical first jet, continuum construction, infrared
  theorem, or Yang--Mills mass gap.
