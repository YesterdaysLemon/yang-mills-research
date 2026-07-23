# Note 0033: quotient-localized physical-\(U\) pullback and the missing extension moment

Claim ID: YM-RG-033

Kind: conditional finite-regulator kernel-pullback and sharpness lemma

Evidence: E2 (finite-dimensional quotient duality and source convolution;
the common converted \(U\)-feature rows and local extension remain explicit
hypotheses)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), Proposition 9 and
  Eq. (190) on printed pp. 307--309;
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), Lemma 2.1 and
  Eqs. (2.59)--(2.63);
- Notes 0016, 0029, 0031, and 0032.

## Scope and completed \(U\)-derivative input

Everything below is at finite regulator. Retain Note 0031's common
real-center hypothesis \((\mathrm H_{\rm rc})\), relative chart

\[
\Phi_{\bar U}(a)=e^{i\xi a}\bar U,
\tag{1}
\]

and covariant norm

\[
\begin{aligned}
\lVert a\rVert_{\mathsf U(\bar U),\xi}
=\max\{&
\lVert a\rVert_{\infty,{\rm RG}},
\lVert\nabla_{\bar U}^{\xi}a\rVert_{\infty,{\rm RG}},\\
&
\lVert a\rVert_{\infty,{\rm op}},
\lVert\mathcal D_{\bar U}^{\xi}a\rVert_{\infty,{\rm op}}
\}.
\end{aligned}
\tag{2}
\]

Write

\[
X_{\bar U,\xi}
=
\bigl(\mathfrak g_{\mathbb C}^{E^+},
\lVert\cdot\rVert_{\mathsf U(\bar U),\xi}\bigr).
\tag{3}
\]

For one completed coefficient put

\[
\ell_{p,s,R}
=
D_U^\Phi\widehat{\mathcal C}_p^+(s,R)
\in X_{\bar U,\xi}^*.
\tag{4}
\]

Note 0031 Eq. (26) gives

\[
\boxed{
\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\lVert\ell_{p,s,R}\rVert_{X_{\bar U,\xi}^*}
\le
\frac{B_{\rm conn}}{r_U}.
}
\tag{5}
\]

The four entries in (2) all remain present below. In particular, no Ward
identity is used to quotient gauge or longitudinal directions.

## Physical coarse-background columns

Use the tagged source-label space and measure from Note 0032:

\[
\widetilde{\mathcal B}
=
\bigsqcup_j(\{j\}\times\Lambda_j),
\qquad
\mu(j',y')=(L^{j'}\eta)^d,
\qquad
\lambda_U=\frac{\delta _0}{8}.
\tag{6}
\]

Let

\[
\alpha=(\vartheta,j',y')
\tag{7}
\]

include the finite source direction and Lie-algebra component
\(\vartheta\). Its measure is
\(\mu_\alpha=\mu(j',y')\), and its tagged geometric label is
\(\widetilde y_\alpha=(j',y')\).

Retain throughout the strengthened separated-cell premise of Propagators II
Lemma 2.1 that is needed for the \(c_1\) exponential convolution.

At a retained physical center define the relative-log functional-derivative
density columns \(A_\alpha\in X_{\bar U,\xi}\) by requiring, for every source
test field \(h\),

\[
D_B\mathcal U[h]
=
i\xi\left(
\sum_\alpha\mu_\alpha A_\alpha h_\alpha
\right)\bar U.
\tag{8}
\]

Thus \(A_\alpha\) is obtained from the variational paper's
\(K=\delta\mathcal H/\delta B\) by the selected
differential-of-exponential and gauge-restoration maps. It is a density with
respect to \(\mu_\alpha\), not an unnormalized coordinate partial. Define

\[
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
=
\ell_{p,s,R}[A_\alpha].
\tag{9}
\]

This is only the independent-\(U\) summand of the physical chain rule. The
physical auxiliary-\(J\) summand is the separate object controlled in Note
0032.

Equivalently, the measure-normalized synthesis appearing in (8) is

\[
\mathcal A_Uh
=
\sum_\alpha\mu_\alpha A_\alpha h_\alpha.
\tag{10}
\]

The inverse factor \(\mu_\alpha^{-1}\) in Eq. (190) algebraically cancels the
measure in (10).

## The converted feature-row hypothesis

Let \(\Sigma^{\rm glob}\) index every translated local feature appearing in
(2). For \(\sigma\in\Sigma^{\rm glob}\), let

\[
T_\sigma:X_{\bar U,\xi}\longrightarrow Z_\sigma
\tag{11}
\]

be the corresponding raw-RG, covariant-gradient-RG, raw-operator, or
covariant-curl-operator evaluation. Then

\[
\lVert a\rVert_{\mathsf U(\bar U),\xi}
=
\sup_{\sigma\in\Sigma^{\rm glob}}
\lVert T_\sigma a\rVert_{Z_\sigma}.
\tag{12}
\]

As part of the hypothesis below, assign to every feature a tagged Eq. (190)
anchor \(\widetilde y_\sigma=(j_\sigma,y_\sigma)\). This may require an
explicitly bounded finite decomposition of a gradient or curl stencil into
local output terms, together with a common label halo and multiplicity
absorbed into the displayed constants. The source statement
\(x\in\Delta(y)\) does not by itself put an entire multi-link stencil in one
cell. The resulting anchor choice can be degenerate and need not define Note
0019's ownership map.

The variational paper prints separate \(K\), spatial-gradient,
Hölder-gradient, \(D^*D K\), and \(\Delta K\) rows. The following assembled
feature statement is the exact additional hypothesis used here.

**Common converted feature-row hypothesis
\((\mathrm H_{\rm row}^U)\).** There are common constants and nonnegative
scale weights \(E_{U,\sigma}(j_\sigma)\) such that

\[
\boxed{
\lVert T_\sigma A_\alpha\rVert_{Z_\sigma}
\le
C_{\chi,U}E_{U,\sigma}(j_\sigma)
\mu_\alpha^{-1}
e^{-\lambda_U
d_{\widetilde{\mathcal B}}
(\widetilde y_\sigma,\widetilde y_\alpha)}
}
\tag{13}
\]

for every completed regulator, center, branch, feature, and source column.
The finite source-component sum and fixed finite-dimensional norm comparisons
are absorbed into \(C_{\chi,U}\).

On one fixed relatively compact chart, the printed \(K\) and
\(\nabla K\) rows have the scale shapes

\[
(L^{j_\sigma}\eta)^{-1},
\qquad
(L^{j_\sigma}\eta)^{-2}.
\tag{14}
\]

Consequently a common pointwise chart conversion would lead to a sufficient
envelope of the form

\[
E_U(j)
=
C_{U,1}(L^j\eta)^{-1}
+C_{U,2}(L^j\eta)^{-2}.
\tag{15}
\]

Equation (15) is not promoted as source proved. In particular, the exact
transported identity that bounds the covariant-curl feature by the converted
raw and gradient rows, with the normalization in (2), must be verified.
The \(D^*D K\) and \(\Delta K\) rows used for the auxiliary-\(J\) differential
are not substitutes for that identity.

## An unweighted physical-\(U\) theorem

First assume the global completed envelope

\[
\overline E_U^{\rm glob}
:=
\sup_{\substack{
\mathfrak r,\ p,\ (\bar U,J_0)\in\mathfrak K_{p,\mathfrak r}^{\rm rc}\\
\sigma\in\Sigma_{\mathfrak r}^{\rm glob}}}
E_{U,\sigma}(j_\sigma)
<\infty.
\tag{16}
\]

For \(\lVert h\rVert_{\ell^\infty}\le1\), (10), (12), (13), and the
Propagators-II exponential convolution give

\[
\begin{aligned}
\lVert\mathcal A_Uh\rVert_{\mathsf U(\bar U),\xi}
&\le
\sup_\sigma
\sum_\alpha\mu_\alpha
\lVert T_\sigma A_\alpha\rVert
|h_\alpha|\\
&\le
C_{\chi,U}c_1(1/8)\overline E_U^{\rm glob}.
\end{aligned}
\tag{17}
\]

Finite-dimensional \(\ell^\infty\)-\(\ell^1\) phase duality now gives

\[
\begin{aligned}
\sum_\alpha\mu_\alpha
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|
&=
\sup_{\lVert h\rVert_{\ell^\infty}\le1}
\left|
\ell_{p,s,R}[\mathcal A_Uh]
\right|\\
&\le
C_{\chi,U}c_1(1/8)\overline E_U^{\rm glob}
\lVert\ell_{p,s,R}\rVert_{X_{\bar U,\xi}^*}.
\end{aligned}
\tag{18}
\]

Combining (18) with (5) proves

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\frac{
C_{\chi,U}c_1(1/8)
\overline E_U^{\rm glob}B_{\rm conn}
}{r_U}.
\end{aligned}
}
\tag{19}
\]

There is no coordinate count, bond-volume factor, mesh factor, or branch
factor in (19). No support-extension theorem is needed at source exponent
\(\gamma=0\). Uniformity is nevertheless conditional on
\((\mathrm H_{\rm rc})\), \((\mathrm H_{\rm row}^U)\), and (16).

## Exact quotient reduction for positive source distance

Note 0029 Eq. (13) proves external-\((U,J)\) restriction locality. In the
relative chart define

\[
I_{U,p,s}^{\rm conn}(R)
=
\left\{
b:
D_{U(b)}^\Phi\widehat{\mathcal C}_p^+(s,R)
\text{ is not identically zero}
\right\}.
\tag{20}
\]

Then

\[
I_{U,p,s}^{\rm conn}(R)
\subset
\mathsf E_s^{\rm loc}(R).
\tag{21}
\]

Fix one coefficient, abbreviate its active set by \(I\), and put

\[
N_I
=
\{a\in X_{\bar U,\xi}:a|_I=0\},
\qquad
Q_I:X_{\bar U,\xi}\longrightarrow X_{\bar U,\xi}/N_I.
\tag{22}
\]

Restriction locality says \(\ell_{p,s,R}|_{N_I}=0\). Hence it descends to
\(\bar\ell_{p,s,R}\) on the quotient, and the quotient norm gives the exact
identity

\[
\boxed{
\lVert\bar\ell_{p,s,R}\rVert_{(X_{\bar U,\xi}/N_I)^*}
=
\lVert\ell_{p,s,R}\rVert_{X_{\bar U,\xi}^*}.
}
\tag{23}
\]

This quotients only directions invisible on the coefficient's active bonds.
It does not quotient gauge or longitudinal directions.

Choose any nonempty tagged feature-anchor set
\(S_{p,s,R}^U\subset\widetilde{\mathcal B}\). For
\(0\le\gamma<\lambda_U\), define

\[
w_{S,\gamma}(\alpha)
=
e^{\gamma
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^U,\widetilde y_\alpha)}
\tag{24}
\]

and the weighted quotient synthesis operator

\[
\mathsf K_{I,\gamma,S}c
=
Q_I\sum_\alpha
\mu_\alpha w_{S,\gamma}(\alpha)c_\alpha A_\alpha,
\qquad
\lVert c\rVert_{\ell^\infty}\le1.
\tag{25}
\]

Put

\[
\mathfrak M_{U,\gamma}(I,S)
=
\left\|
\mathsf K_{I,\gamma,S}
\right\|_{\ell^\infty\to X_{\bar U,\xi}/N_I}.
\tag{26}
\]

Finite-dimensional phase duality, (23), and operator duality give

\[
\boxed{
\begin{aligned}
&\sum_\alpha\mu_\alpha
e^{\gamma
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^U,\widetilde y_\alpha)}
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\mathfrak M_{U,\gamma}(I,S)
\lVert\ell_{p,s,R}\rVert_{X_{\bar U,\xi}^*}.
\end{aligned}
}
\tag{27}
\]

Moreover, \(\mathfrak M_{U,\gamma}(I,S)\) is the sharp
coefficient-independent constant in (27):

\[
\sup_{\substack{
\ell\in N_I^\perp\\
\lVert\ell\rVert_{X_{\bar U,\xi}^*}\le1}}
\sum_\alpha\mu_\alpha w_{S,\gamma}(\alpha)
|\ell[A_\alpha]|
=
\mathfrak M_{U,\gamma}(I,S).
\tag{28}
\]

Indeed, the inequality is (27). Conversely, choose a source phase vector
approaching the operator norm in (26), then choose a norming functional on
the finite-dimensional quotient and lift it through (23).

If \(I=\varnothing\), then the derivative and chain density vanish. The term
is removed before set distance or the quotient operator is formed.

Let

\[
\overline{\mathfrak M}_{U,\gamma}^{\rm conn}
:=
\sup_{\substack{
\mathfrak r,\ p,
(\bar U,J_0)\in\mathfrak K_{p,\mathfrak r}^{\rm rc},\ s,R\\
I_{U,p,s}^{\rm conn}(R)\ne\varnothing}}
\mathfrak M_{U,\gamma}
\bigl(I_{U,p,s}^{\rm conn}(R),S_{p,s,R}^U\bigr)
<\infty.
\tag{29}
\]

If this supremum has no nonempty active-support terms, set
\(\overline{\mathfrak M}_{U,\gamma}^{\rm conn}=0\).

Equations (5) and (27) then give the exact conditional hybrid theorem

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s
\sum_{\substack{R\supset\widehat Q_{p,s}\\
I_{U,p,s}^{\rm conn}(R)\ne\varnothing}}
e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
e^{\gamma
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^U,\widetilde y_\alpha)}
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\overline{\mathfrak M}_{U,\gamma}^{\rm conn}
\frac{B_{\rm conn}}{r_U}.
\end{aligned}
}
\tag{30}
\]

The full polymer exponent \(\kappa\) is retained. Equation (30) uses no
ownership map, root-to-cell mesh comparison, support-cardinality factor,
bond-volume factor, or shifted-branch factor. Its new content is the exact
identification of the remaining positive-\(\gamma\) constant.

## A checkable support-local sufficient condition

Quotient duality alone does not bound (29). A sufficient route is the
following feature-extension theorem.

For every nonempty \(I\), choose a finite stencil collar
\(\Sigma_I\subset\Sigma^{\rm glob}\) containing the raw feature evaluations
on \(I\). Assume

\[
\boxed{
\lVert Q_Ia\rVert_{X_{\bar U,\xi}/N_I}
\le
C_{\rm ext}
\max_{\sigma\in\Sigma_I}
\lVert T_\sigma a\rVert_{Z_\sigma}.
}
\tag{31}
\]

Call (31) \((\mathrm H_{\rm ext}^U)\). The constant must be common in the
regulator, center, branch, support, and shift. A statement that restriction
is a contraction does not prove (31): zero extension can create
\(O(\xi^{-1})\) covariant-gradient and curl jumps.

Choose

\[
\boxed{
S_{p,s,R}^U
=
\left\{
\widetilde y_\sigma:
\sigma\in\Sigma_{I_{U,p,s}^{\rm conn}(R)}
\right\}.
}
\tag{32}
\]

Thus the positive source weight is anchored at the complete feature collar,
not merely at the active raw bonds. Assume the completed local envelope

\[
\overline E_U^{\rm conn}
:=
\sup_{\substack{
\mathfrak r,\ p,
(\bar U,J_0)\in\mathfrak K_{p,\mathfrak r}^{\rm rc},\ s,R\\
\sigma\in\Sigma_{I_{U,p,s}^{\rm conn}(R)}}}
E_{U,\sigma}(j_\sigma)
<\infty.
\tag{33}
\]

Under the retained separated-cell premise, for

\[
0\le\gamma<\lambda_U,
\qquad
\alpha_\gamma
=
\frac18-\frac{\gamma}{\delta _0}>0,
\tag{34}
\]

For every \(\sigma\in\Sigma_I\),

\[
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^U,\widetilde y_\alpha)
\le
d_{\widetilde{\mathcal B}}
(\widetilde y_\sigma,\widetilde y_\alpha).
\tag{35}
\]

Apply (13), the source-measure cancellation, and the exponential convolution
feature by feature. Then use the maximum in (31), not a sum over features:

\[
\boxed{
\mathfrak M_{U,\gamma}(I,S)
\le
C_{\rm ext}C_{\chi,U}
c_1(\alpha_\gamma)
\overline E_U^{\rm conn}.
}
\tag{36}
\]

Combining (30) and (36) gives

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s
\sum_{\substack{R\supset\widehat Q_{p,s}\\
I_{U,p,s}^{\rm conn}(R)\ne\varnothing}}
e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
e^{\gamma
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^U,\widetilde y_\alpha)}
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\frac{
C_{\rm ext}C_{\chi,U}
c_1(\alpha_\gamma)
\overline E_U^{\rm conn}B_{\rm conn}
}{r_U},
\end{aligned}
}
\tag{37}
\]

where empty-support terms are omitted. There is no feature-cardinality
factor because (31) uses a maximum before the source convolution.

If instead one wants to anchor at tagged active-bond labels
\(S_{p,s,R}^{U,\rm act}\), a common collar bound

\[
\sup_{\sigma\in\Sigma_I}
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^{U,\rm act},\widetilde y_\sigma)
\le H_U
\tag{38}
\]

gives (36)--(37) with the extra factor \(e^{\gamma H_U}\).
Neither (31) nor a common \(H_U\) is currently source proved.

## A plaquette-rooted corollary

Choose a tagged marked-plaquette root \(\widetilde q_{p,s}\). If the chosen
feature anchors satisfy

\[
\sup_{\widetilde y\in S_{p,s,R}^U}
d_{\widetilde{\mathcal B}}
(\widetilde q_{p,s},\widetilde y)
\le
A_Ud_{k+1,s}(R)+B_U
\tag{39}
\]

and

\[
a_*+\gamma A_U\le\kappa,
\tag{40}
\]

then (30), or its explicit sufficient version (37), yields the corresponding
plaquette-rooted source weight with residual polymer exponent \(a_*\) and
the extra factor \(e^{\gamma B_U}\). As in Note 0032, this endpoint statement
is not part of the support-anchored theorem.

## Why the direct-\(J\) proof cannot be copied

Under the standing mesh range \(0<\xi\le1\), consider two scalar bond
coordinates with

\[
\lVert(a_0,a_1)\rVert_{X_\xi}
=
\max\left\{
|a_0|,\ |a_1|,\ \xi^{-1}|a_1-a_0|
\right\}.
\tag{41}
\]

The longitudinal functional

\[
\ell_\xi(a)
=
\xi^{-1}(a_1-a_0)
\tag{42}
\]

has

\[
\lVert\ell_\xi\rVert_{X_\xi^*}=1,
\qquad
\sum_{b=0}^1\lVert\ell_{\xi,b}\rVert_*
=
\frac2\xi.
\tag{43}
\]

Thus the direct-\(J\) identity between the coordinatewise \(\ell^1\) sum and
the Banach dual norm fails by a mesh factor. If two source columns are
\(A_0=(1,0)\) and \(A_1=(0,1)\), then

\[
\sum_{\alpha=0}^1|\ell_\xi[A_\alpha]|
=
\frac2\xi.
\tag{44}
\]

The quotient synthesis norm in (26) detects exactly this cost. The raw
kernel rows alone do not control the covariant-gradient feature in (41).

There is a separate reason not to use the global weighted kernel norm for
positive \(\gamma\). On the line \(\{0,\ldots,n\}\), take both source and
output spaces to have the sup norm, let the kernel be the identity, and let
the coefficient be evaluation at output \(0\). With support anchor
\(S=\{0\}\), the weighted global synthesis norm is \(e^{\gamma n}\), while
the quotient norm seen by the coefficient is exactly \(1\). The kernel
columns satisfy arbitrarily strong off-diagonal decay. Hence the global
weighted norm can lose exponentially in the regulator diameter even when
the physical local composition is uniformly bounded.

## Ward identities do not remove the longitudinal sector

For a simultaneous infinitesimal gauge direction, covariance gives a joint
identity of the form

\[
D_U^\Phi\widehat{\mathcal C}[a_\phi]
+
D_J\widehat{\mathcal C}[\delta_\phi J]
=0.
\tag{45}
\]

It does not give
\(D_U^\Phi\widehat{\mathcal C}[a_\phi]=0\). The present bounds take absolute
values of the \(U\)- and \(J\)-chain-rule summands separately. Therefore the
longitudinal sector cannot be discarded. Exploiting (45) would require a new
joint \(U/J\) theorem before absolute summation.

## Exact boundary

- Equation (19) is a conditional unweighted physical-\(U\) source sum.
  As originally stated it uses the full common converted feature rows.
  Note 0034 proves that, under \((\mathrm H_{\rm rc})\), the raw-RG and
  covariant-gradient-RG rows suffice with the explicit factor
  \(C_{\rm eq}\). The reduced rows and global output-scale envelope remain
  hypotheses, as does the strengthened separated-cell premise for the
  \(c_1\) convolution; no support-extension theorem is needed at
  \(\gamma=0\).
- Equation (30) identifies the sharp coefficient-independent quotient
  synthesis moment for a positive source-distance weight. Finiteness with
  common constants is not proved merely by quotient duality.
- Equation (37) is conditional on both
  \((\mathrm H_{\rm row}^U)\) and
  \((\mathrm H_{\rm ext}^U)\) in its original formulation. Note 0034 proves
  the extension inequality for a collar of fixed physical thickness and
  replaces the four-feature rows by its reduced raw/gradient hypothesis.
- Note 0034's exact transported identity proves that the raw-operator and
  covariant-curl entries are controlled by the raw-RG and
  covariant-gradient-RG pair under \((\mathrm H_{\rm rc})\). No
  \(D^*D K\) or \(\Delta K\) row is substituted for the curl conversion.
- The feature-anchor choice (32) can be a collar enlargement of the exact
  active raw-bond labels. Moving back to those labels costs (38).
- The hybrid theorem retains the full polymer exponent \(\kappa\). Positive
  source decay still requires \(0\le\gamma<\delta _0/8\).
- \((\mathrm H_{\rm rc})\), common converted raw/gradient constants, common
  output-scale control, and the tagged-metric halo from Note 0034's
  \(\lceil\rho/\xi\rceil\)-layer feature collar to smaller active labels
  remain open for the actual completed minimizing family. Note 0035 proves
  that the obvious diagonal \(s_j,s_j^2\) renorming does not provide that
  control: its full analytic radius is only \(O(\xi^2)\). A fixed number of
  lattice layers cannot replace the physical-width collar uniformly.
- No nonzero-source polymer-activity disk, unrestricted raw-law comparison,
  unit-translation theorem, large-field estimate, RG iteration, continuum or
  infinite-volume construction, Osterwalder--Schrader reconstruction,
  infrared decay, or Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Replace the quotient norm in (23) by a zero-extension norm and ignore the
  boundary gradient/curl jump.
- Copy Note 0032's coordinatewise direct-\(J\) dual identity into the
  coupled norm (2); (41)--(44) disprove that step.
- Use only the raw \(K\) row of Eq. (190) and omit the covariant-gradient or
  the Note 0034 curl reduction.
- Put an entire gradient or curl stencil in one Eq. (190) cell without a
  bounded local decomposition and label-halo proof.
- Claim that the printed \(D^*D K\) or \(\Delta K\) rows establish the
  transported curl identity instead of Note 0034's exact
  curvature-corrected normalization.
- Bound the positive-\(\gamma\) composition by the global weighted synthesis
  norm and hide a regulator-diameter factor.
- Define \(S_{p,s,R}^U\) from active raw bonds while using a larger feature
  collar without paying (38).
- Quotient gauge directions by Ward covariance after separately taking
  absolute values of the \(U\) and \(J\) summands.
- Drop the source measure, its inverse Eq. (190) density, the strengthened
  separated-cell premise, or the condition \(\gamma<\delta _0/8\).
- Invoke a row-balanced chart norm as a uniform repair without paying Note
  0035's \(O(\xi^2)\) analytic radius and resulting Cauchy loss.
- Promote (19), (30), or (37) to an unconditional physical first jet, an
  unrestricted RG construction, a continuum theory, or a mass gap.
