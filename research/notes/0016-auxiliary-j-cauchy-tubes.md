# Note 0016: the physical auxiliary field and honest Cauchy tubes

Claim ID: YM-RG-016

Kind: finite-regulator analytic-reduction lemma

Evidence: E2 (conditional chartwise derivative bounds; internally checked)

Novelty: none claimed

Primary anchors: [RG I](https://doi.org/10.1007/BF01215223), [RG
II](https://doi.org/10.1007/BF01239022), the
[variational/background-field paper](https://doi.org/10.1007/BF01229381), and
[*Propagators and renormalization transformations for lattice gauge theories
II*](https://doi.org/10.1007/BF01240221).

## What the primary papers already define

Retain every hypothesis and notation of Notes 0012--0015. In particular,
work at one finite four-dimensional \(SU(2)\) regulator and RG step, on one
selected Proposition 9 background chart, and use the normalized shifted
activities

\[
\widehat W_{k,p}(\sigma,Y;U,J,\varphi).
\]

RG I does not leave the physical auxiliary field \(J\) unspecified. On
printed p. 261, Eq. (1.8) defines

\[
\mathscr J_\xi(U)
:=D_U^{\xi *}\,\xi^{-2}\pi\operatorname{im}(dU),
\qquad \xi=L^{-j}.
\tag{1}
\]

Here \(\pi\) is the projection from complex matrices to
\(\mathfrak g_{\mathbb C}\), and the paper uses the holomorphic convention
\(\operatorname{im}X=(X-X^{-1})/(2i)\). RG I Eqs. (1.15)--(1.16), printed
p. 262, define \(J_n\) by (1) evaluated on the minimizing \(U_n\), with
\(L^{-n}\) replacing \(\xi\). Consequently, in RG I's rescaled convention,

\[
\boxed{
J_{k+1}(W)=
\mathscr J_{\xi_{k+1}}\!\left(U_{k+1}(W)\right),
\qquad \xi_{k+1}=L^{-(k+1)}.
}
\tag{2}
\]

RG I Eq. (3.1), pp. 269--270, and RG II Eq. (1.35), printed p. 9,
then specialize the independent variables to this exact pair. Thus the
separate \(J\)-holomorphy hypothesis retained in the first version of Note
0015 was unnecessary. The common-domain hypothesis was not unnecessary:
the pair in (2) must still remain inside every transported RG-II Eq. (1.34)
domain on which an activity is evaluated.

## Holomorphy, covariance, and the exact differential reduction

The map \(\mathscr J_\xi\) is a finite-stencil holomorphic expression in the
link variables on every selected complex link chart. RG I Eq. (1.10)
specifies the adjoint transformation convention for the \((U,J)\) pair;
direct substitution in (1) gives covariance in that convention. Therefore,
wherever the selected
minimizing branch

\[
\mathcal U(\omega)=U_{k+1}(W(\omega))
\]

is holomorphic and equivariant, the physical auxiliary field is not an
independent lift but the holomorphic and equivariant composition

\[
\mathcal J(\omega)
=\mathscr J_{\xi_{k+1}}(\mathcal U(\omega)).
\tag{3}
\]

RG I Eqs. (3.10)--(3.11), printed p. 272, make the local differential
structure explicit. For the paper's relative coordinate
\(U_A=e^{i\xi A}U\),

\[
\mathscr J_\xi(U_A)
=\mathscr J_\xi(U)
+D_U^{\xi *}D_U^\xi A
+F(U,A),
\tag{4}
\]

where \(F\) is local in \(U,dU,A,\nabla^\xi A\). Differentiating at \(A=0\)
gives the exact first variation

\[
D\mathscr J_\xi(U)[i\xi AU]
=D_U^{\xi *}D_U^\xi A+D_AF(U,0)[A].
\tag{5}
\]

The local \(D_AF(U,0)\) term is part of the formula and may not be dropped.
Combining (3) with Note 0015's chain rule gives

\[
\boxed{
\begin{aligned}
D\mathcal W_{k,p}[h,\psi]
={}&D_U\widehat W_{k,p}[D\mathcal U(\omega)h]\\
&+D_J\widehat W_{k,p}
 \!\left[D\mathscr J_\xi(\mathcal U(\omega))
               D\mathcal U(\omega)h\right]
+D_\varphi\widehat W_{k,p}[\psi].
\end{aligned}
}
\tag{6}
\]

All activity derivatives in (6) are evaluated at
\((\sigma,Y;\mathcal U(\omega),\mathcal J(\omega),\varphi)\).

For this one-step specialization identify the variational paper's finest
lattice spacing with the RG-I relative-field scale,
\(\eta=\xi_{k+1}\). Given a coarse tangent \(h\), define \(A_h\) in the
selected relative chart by

\[
D\mathcal U(\omega)[h]
=i\xi_{k+1}A_h\mathcal U(\omega).
\tag{6a}
\]

Let \(K=\delta\mathcal H/\delta B\) be the component kernel in the
variational paper's Eq. (190), with \(x\in\Delta(y)\). Applied to \(h\),
\(K\) first produces the variation of the relative minimizer \(\mathcal H\);
the chosen differential-of-exponential and gauge-restoration maps then
produce \(A_h\) in (6a). On one fixed relatively compact chart, those maps,
the coefficients in (5), and their finite-stencil translates are bounded.
The \(K\), \(\nabla K\), and
\(D_U^{\eta *}D_U^\eta K\) rows of Eq. (190), with its multiscale layer
indices \(j,j'\) retained, therefore imply the qualitative chartwise
consequence

\[
\left|
\frac{\delta\mathcal J_\mu(\omega,x)}
     {\delta\omega_\nu(y')}
\right|
\le C_{\Omega,N,k,j,j',c}
\exp[-c\,d_{\mathcal B}(y,y')],
\qquad 0<c<\frac{\delta_0}{8}.
\tag{7}
\]

The constant in (7) deliberately retains its chart, regulator, and scale
dependence. This is a finite-stencil reduction of the \(J\)-derivative to the
printed minimizer estimates, not the sharp scale-explicit norm needed for RG
iteration. In particular, the expected leading fourth-row scale cannot be
asserted alone until the \(D_AF(U,0)\), differential-of-exponential, and
gauge-restoration factors are bounded in the same norms.

## The outer domain is not itself a numerical Cauchy radius

RG II Eq. (1.34) gives the activity domain

\[
\mathscr D^{\rm out}_{Y,\sigma}
=\mathcal U^{c,\sigma}_{k+1}
\!\left(Y,(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0\right)
\times
\{\varphi:g_k|\varphi|<\varepsilon_1\text{ on }Y\}.
\tag{8}
\]

The first two parameters have a visible \(1+\beta\) enlargement, but the
third does not. RG I Eq. (1.14) uses the third parameter for the direct
\(|J|\) bound. Moreover, \(\mathcal U^c_{k+1}\) is a nonlinear union of
complex gauge orbits, not a canonical additive ball. Therefore (8) alone
does not supply numerical radii for \(D_U\) or \(D_J\).

For each shifted polymer fix a split representative product chart

\[
\chi_{Y,\sigma}(U,J)
=\bigl(\chi^U_{Y,\sigma}(U),\chi^J_{Y,\sigma}(J)\bigr)
=(u,j),
\]

and complex Banach norms
\(\|\cdot\|_{\mathsf U,Y,\sigma}\) and
\(\|\cdot\|_{\mathsf J,Y,\sigma}\). Let the full composed compact set be

\[
K^{\rm full}_{Y,\sigma}
=\overline{\left\{
\left(\chi_{Y,\sigma}\!\left(
\mathcal U(\omega)|_{\operatorname{int}Y},
\mathcal J(\omega)|_{\operatorname{int}Y}
\right),\varphi\right):
\omega\in\overline{\Omega_{\mathbb C}},\quad
\varphi\in\mathfrak F_Y^\sigma
\right\}}.
\tag{9}
\]

Assume that there are full complex norm-ball radii \(r_U,r_J>0\) such that,
for every \((u,j,\varphi)\in K^{\rm full}_{Y,\sigma}\),

\[
\{(u+v,j,\varphi):\|v\|_{\mathsf U,Y,\sigma}<r_U\}
\subset(\chi_{Y,\sigma}\times\operatorname{id})
(\mathscr D^{\rm out}_{Y,\sigma}),
\tag{10}
\]

\[
\{(u,j+w,\varphi):\|w\|_{\mathsf J,Y,\sigma}<r_J\}
\subset(\chi_{Y,\sigma}\times\operatorname{id})
(\mathscr D^{\rm out}_{Y,\sigma}).
\tag{11}
\]

The fluctuation is held fixed along each tube in (10)--(11), but the radii are
uniform over its full compact closure. These are norm balls, not merely
separate coordinate-axis circles. At one fixed regulator, the full compact
containment in Note 0015, openness in the chosen representative charts, and
the finiteness of the \((p,\sigma,Y)\) family give some common radii
\(r_{U,N,k},r_{J,N,k}>0\). No lower bound uniform in \(N\) or \(k\) follows.

**Subsequent refinement.** The last sentence concerns radii obtained from
compactness alone. [Note 0017](0017-strict-j-margin-metric-pullback.md)
separately uses RG I's strict smaller physical representative domain. Under
its named hypothesis \((\mathrm H_J)\), the linear direct-\(J\) coordinate has
the explicit radius
\(\Delta_J=\alpha_0-\bar\alpha_0\), independent of \(N,k,p,\sigma,Y\).
This does not produce a \(U\)-radius and does not follow from the visible
\(1+\beta\) enlargement by itself.

## Cauchy bounds without a polymer-volume loss

Put

\[
R=e^{\kappa_1},
\qquad
A_{p,\sigma,Y}(\varphi)
=\frac{C_{\rm mark}e^{16\kappa_1}g_k\|\varphi\|_Y}{n_p}
(R-1)^{-m_\sigma(Y)}.
\tag{12}
\]

Notes 0012 and 0014 prove

\[
|\widehat W_{k,p}(\sigma,Y;U,J,\varphi)|
\le A_{p,\sigma,Y}(\varphi)
\tag{13}
\]

throughout (8). Fix a unit vector in the \(U\)-chart norm and apply the
one-variable Cauchy formula on its complex line inside (10). Taking the
supremum over unit vectors gives the operator norm, with no sum over the
number of links in \(Y\):

\[
\boxed{
\|D_U\widehat W_{k,p}(\sigma,Y)\|_{\rm op}
\le \frac{A_{p,\sigma,Y}(\varphi)}{r_U}.
}
\tag{14}
\]

The same proof using (11) gives

\[
\boxed{
\|D_J\widehat W_{k,p}(\sigma,Y)\|_{\rm op}
\le \frac{A_{p,\sigma,Y}(\varphi)}{r_J}.
}
\tag{15}
\]

Both derivatives retain the linear fluctuation factor and hence vanish at
\(\varphi=0\). Coordinatewise Cauchy estimates followed by a sum of partial
derivatives would instead risk a factor proportional to the number of field
components in \(Y\).

Retain

\[
a=(1-2\delta)\kappa,
\qquad
q_d=\frac{64e^a}{e^{\kappa_1}-1},
\qquad
\mathcal B_d=
\frac{C_{\rm mark}e^{16\kappa_1}\varepsilon_1}{1-q_d}.
\tag{16}
\]

The same animal count used in Notes 0013--0014, together with the exact
\(1/n_p\) cancellation of the shift sum, yields

\[
\boxed{
\sup_p\sum_{\sigma,Y}
e^{a d_{k,\sigma}(Y)}
\sup_{\mathfrak C_Y^\sigma}
\|D_U\widehat W_{k,p}(\sigma,Y)\|_{\rm op}
\le\frac{\mathcal B_d}{r_U},
}
\tag{17}
\]

\[
\boxed{
\sup_p\sum_{\sigma,Y}
e^{a d_{k,\sigma}(Y)}
\sup_{\mathfrak C_Y^\sigma}
\|D_J\widehat W_{k,p}(\sigma,Y)\|_{\rm op}
\le\frac{\mathcal B_d}{r_J}.
}
\tag{18}
\]

Here the sums have the same admitted ranges as Note 0015 Eq. (12). For the
derived fixed-regulator radii, (17)--(18) are finite-regulator estimates. They
become volume- and scale-uniform only if one separately proves

\[
\inf_{N,k}r_{U,N,k}>0,
\qquad
\inf_{N,k}r_{J,N,k}>0.
\tag{19}
\]

More generally, if a polymer-dependent radius satisfies

\[
r_{U,\sigma,Y}^{-1}
\le c_Ue^{\theta_Um_\sigma(Y)},
\tag{20}
\]

then the same sum closes only when \(q_de^{\theta_U}<1\), and its constant is

\[
\frac{c_UC_{\rm mark}e^{16\kappa_1}\varepsilon_1}
{1-q_de^{\theta_U}}.
\tag{21}
\]

The analogous statement holds for \(J\). Thus a shrinking analytic radius
spends the same entropy budget needed later by the marked expansion.

## Why this still does not prove a physical derivative norm

Equations (17)--(18) control derivatives with respect to the independent
activity variables. To insert (7) into (6), one must compare two different
geometries.

The distance \(d_{\mathcal B}\) in Proposition 9 Eq. (190) is the multiscale
contour distance defined in Bałaban's *Propagators and renormalization
transformations for lattice gauge theories II*, Eqs. (2.45)--(2.48). Its
triangle inequality and exponential summation lemma are Eqs. (2.54) and
(2.59)--(2.63). It is not Note 0014's contained-tree polymer metric
\(d_{k,\sigma}\).

A later theorem must identify the variational cells and scales with the
shifted localization cubes, prove a regulator-uniform geometric comparison
including layer interfaces, and retain enough exponent after the resulting
kernel convolution and animal count. It must also quantify the coefficients
suppressed in the chart-dependent constant in (7). Until that is done,
neither (7) nor (17)--(18) is a summable physical coarse-field derivative
norm.

Note 0017 proves the exact source-measure cancellation, a dual
\(d_{\mathcal B}\)-weighted kernel sum with no polymer-volume loss, and a
conditional one-layer pullback for the \(D_J\)-chain-rule summand. Note 0018
then proves that full raw and \(U_A=e^{i\xi A}U\) per-bond sup-norm
\(U\)-radii necessarily collapse as the regulator is removed. A collar in a
concrete RG-scaled regularity norm, uniform chart coefficients, and all layer
interfaces remain open, so the full physical derivative norm is still not
proved.

## Exact boundary

- The exact physical \(J\) formula, its holomorphy, and its covariance are no
  longer open. The sharp, regulator-uniform norm for its coarse derivative is
  open.
- The \(1+\beta\) enlargement in RG II Eq. (1.34) is not called a \(J\)-radius;
  its third parameter is not enlarged.
- The fixed-regulator common radii obtained by compactness may shrink with
  volume, scale, chart choice, or changes in the admitted polymer family; the
  underlying polymer-specific margins need not be uniform. Under Note 0017's
  strict representative hypothesis the direct-\(J\) radius is the exception.
  Note 0018 shows more than absence of a conclusion for \(U\): in the naive
  raw and \(\xi\)-scaled per-bond sup norms the radius must vanish. Only its
  explicitly conditional RG-scaled replacement remains viable.
- Cross-regulator use would also require a coherent RG-normalized family of
  chart norms; positive numerical radii in unrelated norms would not suffice.
- No coarse-field strict locality, uniform quasilocal derivative, fixed
  Section-2 partition, connected marked expectation, large-field estimate,
  RG iteration, continuum construction, infrared decay, or mass gap follows.

## Falsification checks

- Replace (2) by an arbitrary holomorphic \(J\)-lift and identify the ignored
  RG-I definition.
- Drop \(D_AF(U,0)\) from (5) and reject the resulting \(J\)-variation.
- Let the physical \(J\)-values approach the boundary \(|J|=\alpha_0\) and
  observe that (8) gives no common positive \(J\)-radius.
- Use an unscaled raw-log \(U\)-coordinate in place of
  \(U_A=e^{i\xi A}U\) and expose the hidden factor of \(\xi\) in the radius;
  then check Note 0018 and observe that both naive radii still collapse.
- Replace the norm balls (10)--(11) by coordinate-axis discs and identify the
  possible field-dimension factor.
- Set \(q_de^{\theta_U}=1\) in (20)--(21) and observe that the proof loses
  geometric-series summability.
- Identify \(d_{\mathcal B}\) with \(d_{k,\sigma}\) without a cell map and
  reject the purported physical derivative bound.
