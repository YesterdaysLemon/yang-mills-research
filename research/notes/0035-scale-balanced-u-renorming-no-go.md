# Note 0035: scale-balanced physical-\(U\) renorming and its no-go boundary

Claim ID: YM-RG-035

Kind: weighted restriction-quotient theorem, sharp scale-incidence
obstruction, and analytic-tube no-go theorem

Evidence: E2 (finite-dimensional product-rule algebra, exact scalar path
quotient, and explicit complex one-bond/longitudinal countermodels; the
physical source corollaries retain the converted-row and tagging hypotheses)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), Proposition 9 and Eq.
  (190), printed pp. 307--309;
- T. Balaban, [*Renormalization group approach to lattice gauge field
  theories I*](https://doi.org/10.1007/BF01215223), Eqs. (1.10)--(1.16),
  printed pp. 262--263;
- Notes 0018, 0031, 0033, and 0034.

## Question isolated by Note 0034

Write

\[
s_j=L^j\eta.
\tag{1}
\]

The two Proposition-9 rows left after Note 0034's exact curl reduction have
the output-scale shapes

\[
|K|=O(s_j^{-1}),
\qquad
|\nabla K|=O(s_j^{-2}),
\tag{2}
\]

times the common input-density and decay factor

\[
s_{j'}^{-d}
\exp\!\left[
-\frac{\delta _0}{8}d_{\mathcal B}(y,y')
\right].
\tag{3}
\]

The source measure \(s_{j'}^d\) cancels (3)'s inverse density, not either
factor in (2). For the one-step physical composition, Note 0016 identifies

\[
\eta=\xi_{k+1}=:\xi,
\qquad
D\mathcal U[h]=i\xi A_h\mathcal U.
\tag{4}
\]

The tempting repair is therefore to multiply every raw output occurrence by
its scale and every gradient output occurrence by its scale squared. This
note answers two separate questions:

1. does that renorming have a good restriction-quotient cutoff; and
2. can it replace Note 0031's norm while retaining a common complex tube?

The answer to the first is conditional yes. The answer to the second is no
under the currently retained information.

## Tagged weighted raw/gradient norm

Let \(V\) be the chosen independent-bond set. A raw feature occurrence at
\(b\in V\) has a declared output scale

\[
r_b>0.
\tag{5}
\]

An oriented gradient occurrence \(e=(b_-,b_+)\) has output scale
\(t_e>0\), physical step \(h_e>0\), and real background transport \(T_e\)
with

\[
|T_eM|_{\rm RG}
\le
c_{\rm Ad}^{\rm RG}|M|_{\rm RG}.
\tag{6}
\]

Put

\[
D_ea
=
h_e^{-1}(T_ea_{b_+}-a_{b_-})
\tag{7}
\]

and define

\[
\boxed{
\lVert a\rVert_{Y_{\rm sc}}
=
\max\left\{
\sup_{b\in V}r_b|a_b|_{\rm RG},
\sup_e t_e^2|D_ea|_{\rm RG}
\right\}.
}
\tag{8}
\]

For the natural Eq. (190) assignment,

\[
r_b=s_{j_b},
\qquad
t_e=s_{j_e}.
\tag{9}
\]

After the still-unproved chart, gauge-restoration, source-component, and
tagged-stencil conversions, (8)--(9) cancel both output powers in (2).
They do not prove those conversions.

There is also a typing premise. Equation (190)'s \(j\) labels an output
cell occurrence, not intrinsically a global bond. A common norm requires one
declared tag for every translated raw and gradient occurrence across all
retained branches and collars. Taking a coefficient-dependent tag would
destroy the one common product tube and common dual space used in Note 0031.
This note treats the tags in (5)--(9) as fixed data.

## Exact weighted cutoff product rule

Let \(I\subset V\) be nonempty and

\[
N_I=\{a:a|_I=0\}.
\tag{10}
\]

For a scalar cutoff \(\chi:V\to[0,1]\) with \(\chi|_I=1\), write

\[
\chi_\pm=\chi(b_\pm),
\qquad
S=\{b:\chi(b)>0\}.
\tag{11}
\]

Equation (7) gives both exact forms

\[
\boxed{
\begin{aligned}
D_e(\chi a)
={}&
\chi_-D_ea
+h_e^{-1}(\chi_+-\chi_-)T_ea_{b_+}\\
={}&
\chi_+D_ea
+h_e^{-1}(\chi_+-\chi_-)a_{b_-}.
\end{aligned}
}
\tag{12}
\]

Define the local weighted feature maximum

\[
M_S(a)
=
\max\left\{
\sup_{b\in S}r_b|a_b|_{\rm RG},
\sup_{\substack{e=(b_-,b_+)\\b_-,b_+\in S}}
t_e^2|D_ea|_{\rm RG}
\right\}.
\tag{13}
\]

When both endpoints lie in \(S\), (12) gives the rowwise bound

\[
\begin{aligned}
t_e^2|D_e(\chi a)|_{\rm RG}
\le
\min\Bigg\{&
\left(
\chi_-
+c_{\rm Ad}^{\rm RG}
\frac{t_e^2|\chi_+-\chi_-|}
{h_er_{b_+}}
\right)M_S(a),\\
&
\left(
\chi_+
+\frac{t_e^2|\chi_+-\chi_-|}
{h_er_{b_-}}
\right)M_S(a)
\Bigg\}.
\end{aligned}
\tag{14}
\]

If exactly one endpoint lies in \(S\), choose the form in (12) whose
original-gradient coefficient is the zero-cutoff endpoint. Only the raw
inside value remains. Rows with both endpoints outside vanish.

## Physical-width theorem and the scale-incidence constant

Let \(d_h\) be the shortest-path metric in which edge \(e\) has length
\(h_e\). On a component disjoint from \(I\), set the distance to
\(+\infty\). For \(\rho>0\), define

\[
\chi_{I,\rho}(b)
=
\left(
1-\frac{d_h(b,I)}{\rho}
\right)_+.
\tag{15}
\]

Then

\[
|\chi_{I,\rho}(b_+)-\chi_{I,\rho}(b_-)|
\le
\frac{h_e}{\rho}.
\tag{16}
\]

The exact scale-incidence parameter is

\[
\boxed{
\Theta
=
\sup_{e=(b_-,b_+)}
\frac{t_e^2}
{\min\{r_{b_-},r_{b_+}\}}.
}
\tag{17}
\]

Since \(c_{\rm Ad}^{\rm RG}\ge1\), equations (12)--(17) prove

\[
\boxed{
\lVert Q_Ia\rVert_{Y_{\rm sc}/N_I}
\le
\left(
1+\frac{c_{\rm Ad}^{\rm RG}\Theta}{\rho}
\right)
M_{S_{I,\rho}}(a),
}
\tag{18}
\]

where \(S_{I,\rho}=\{\chi_{I,\rho}>0\}\). There is no support-cardinality,
topology, or regulator-volume factor in (18). Uniformity requires a common
\(\Theta\).

A sufficient local scale-incidence hypothesis is

\[
t_e
\le
\Lambda\min\{r_{b_-},r_{b_+}\},
\qquad
t_e\le S_*.
\tag{19}
\]

It implies

\[
\Theta\le\Lambda S_*.
\tag{20}
\]

For \(r_b,t_e\in\{L^j\eta\}\), the declarations

\[
|j_e-j_{b_\pm}|\le q,
\qquad
\sup_e t_e\le1
\tag{21}
\]

give

\[
\Theta\le L^q,
\qquad
C_{\rm ext}^{\rm sc}(\rho)
\le
1+\frac{c_{\rm Ad}^{\rm RG}L^q}{\rho}.
\tag{22}
\]

Neither Eq. (190) nor the existing completed-branch ledger proves the common
tag assignment or (21).

## Sharp obstruction when scales are not incident

The dependence on \(\Theta/\rho\) cannot be deleted. Work in the normalized
scalar path model of physical length

\[
D=Nh.
\tag{23}
\]

Take the active set to be the two endpoints,
\[
I=\{0,N\},
\]
Give every raw vertex the weight \(r_b=\varepsilon\), every gradient edge
the weight \(t_e^2=S^2\), and prescribe active endpoint values

\[
f(0)=\varepsilon^{-1},
\qquad
f(N)=-\varepsilon^{-1}.
\tag{24}
\]

Telescoping gives

\[
\max_i
S^2h^{-1}|f(i+1)-f(i)|
\ge
\frac{2S^2}{\varepsilon D}.
\tag{25}
\]

More explicitly, the endpoint quotient is
\[
\inf_{\substack{g(0)=\varepsilon^{-1}\\
g(N)=-\varepsilon^{-1}}}
\max\left\{
\varepsilon\max_i|g(i)|,
\frac{S^2}{h}\max_i|g(i+1)-g(i)|
\right\}.
\]
Linear interpolation attains the telescoping lower bound (25) and has
weighted raw norm one. Hence

\[
\boxed{
\lVert Q_If\rVert
=
\max\left\{
1,\frac{2S^2}{\varepsilon D}
\right\}
=
\max\left\{
1,\frac{2\Theta}{D}
\right\}.
}
\tag{26}
\]

For the collar lower bound, take \(N=2m+1\) with \(mh\ge\rho\), and choose
the original representative
\[
\widetilde f(i)=
\begin{cases}
\varepsilon^{-1},&0\le i\le m,\\
-\varepsilon^{-1},&m+1\le i\le N.
\end{cases}
\]
Both endpoints of its only jump edge have distance \(mh\ge\rho\) from
\(I\), so that edge lies completely outside the two open
physical-width collars. Their local feature maximum is exactly one. Taking
\(mh\downarrow\rho\) and \(h\downarrow0\) makes
\(D=(2m+1)h\downarrow2\rho\), while the quotient norm in (26) approaches
\(\max\{1,\Theta/\rho\}\). Thus (18) is order-sharp, and a physical-width
theorem cannot be regulator uniform if \(\Theta\) diverges.

One may instead define an intrinsic edge length

\[
\ell_e
=
h_e
\frac{\min\{r_{b_-},r_{b_+}\}}{t_e^2}.
\tag{27}
\]

An \(\ell\)-radius-\(R\) cutoff has constant
\(1+c_{\rm Ad}^{\rm RG}/R\), but its physical width can grow like
\(\Theta R\). This moves rather than removes the scale-incidence problem.

## The weighted norm does not preserve the physical complex tube

Now specialize to a homogeneous finest patch:

\[
r_b=t_e=h_e=\xi.
\tag{28}
\]

The source-balanced raw/gradient norm there is

\[
\lVert a\rVert_{Y_{{\rm sc},\xi}}
=
\max\left\{
\xi\lVert a\rVert_{\infty,{\rm RG}},
\xi^2\lVert\nabla^\xi a\rVert_{\infty,{\rm RG}}
\right\}.
\tag{29}
\]

Adding \(\xi\lVert a\rVert_{\rm op}\) and
\(\xi^2\lVert\mathcal D^\xi a\rVert_{\rm op}\) does not change the
obstruction below.

Take the identity background on a patch containing one complete plaquette.
Write
\[
\Phi_1(a)_b:=e^{i\xi a_b}
\]
for the relative-link chart at that background. In operator-norm
normalization choose

\[
H=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\tag{30}
\]

and put on one oriented bond

\[
a_t(b)=-i\frac{t}{\xi}H,
\qquad
a_t=0\quad\hbox{elsewhere}.
\tag{31}
\]

Every weighted raw, adjacent gradient, and adjacent curl occurrence in
(29) and its four-feature version is \(O(t)\), with constants independent of
\(\xi\). In the normalized scalar/max convention the norm is exactly \(t\).
But the adjacent plaquette contains the factor

\[
e^{i\xi a_t(b)}=e^{tH},
\tag{32}
\]

so

\[
\operatorname{spr}\!\left(d\Phi_1(a_t)(p)-1\right)=e^t-1.
\tag{33}
\]

Here \(\operatorname{spr}\) denotes spectral radius. Freeze
\(c_{\rm RG}>0\) with

\[
|M|_{\rm RG}\ge c_{\rm RG}\operatorname{spr}(M).
\tag{34}
\]

RG I's necessary curvature condition is

\[
|d\Phi_1(a)(p)-1|_{\rm RG}<a_0\xi^2.
\tag{35}
\]

Taking

\[
t_\xi
=
\log\left(
1+\frac{a_0\xi^2}{c_{\rm RG}}
\right)
\tag{36}
\]

violates the strict inequality in (35). Consequently every full
source-balanced weighted ball contained in the direct curvature domain has
radius

\[
\boxed{
r_{{\rm sc},\xi}
\le
C_H
\log\left(
1+\frac{a_0\xi^2}{c_{\rm RG}}
\right)
=
O(\xi^2),
}
\tag{37}
\]

where \(C_H\) is a fixed norm-convention constant and \(C_H=1\) in the
normalized scalar/max model.

The same power bound holds for every diagonal raw/gradient row-cancelling
choice, not only the exact weights in (29). Indeed, uniform cancellation of
the finest raw and gradient kernel powers requires weights
\[
w_0(\xi)\le C_0\xi,
\qquad
w_1(\xi)\le C_1\xi^2.
\]
The one-bond field (31) then has weighted raw/gradient norm at most
\(\max\{C_0,C_1\}t\), up to the same fixed stencil and norm-comparison
constants. The violating value \(t=t_\xi\) therefore gives the same
\(O(\xi^2)\) upper bound for any full ball in such a raw/gradient norm.
The conclusion also survives any fixed additional diagonal rows that
evaluate (31) as \(O(t)\). Smaller raw/gradient weights only make the ball
less restrictive and cannot evade the counterexample. An arbitrary
additional row is not covered by this one-bond argument; the unweighted
curl row is treated separately by the longitudinal field below.

This is not only a curl obstruction. In a flat abelian longitudinal sector,
take

\[
a_1(x)=\frac{t}{\xi}f(x_1)H,
\qquad
a_\nu=0\quad(\nu\ne1),
\tag{38}
\]

where \(f\) has one unit lattice step. Every plaquette curl is zero, while

\[
\lVert\nabla^\xi a\rVert=O(t\xi^{-2}),
\qquad
\lVert a\rVert_{Y_{{\rm sc},\xi}}=O(t).
\tag{39}
\]

RG I condition (ii) requires the unweighted gradient to remain below its
fixed \(a_1\) ceiling. Thus a full weighted ball satisfying condition (ii)
also has radius \(O(\xi^2)\), even if an unweighted curl row is retained.
A constant longitudinal field separately gives an \(O(\xi)\) obstruction
from the unweighted raw ceiling.

For the general weights above, the longitudinal field has weighted size
\[
\max\left\{
w_0(\xi)\frac{t}{\xi},
w_1(\xi)\frac{t}{\xi^2}
\right\}
=O(t),
\]
so the condition-(ii) conclusion is unchanged.

Therefore:

- retaining unweighted raw/gradient rows preserves Note 0031's tube but
  restores the \(s_j^{-1},s_j^{-2}\) source loss;
- weighting those rows to cancel (2) shrinks the common tube radius as
  \(O(\xi^2)\);
- retaining only an unweighted curl does not control the curl-free
  longitudinal example.

Max and positive-sum feature norms differ by only fixed constants on this
one-scale patch, so changing max to sum cannot alter the power in (37).

## Abstract Cauchy renorming no-go

The preceding examples are a concrete instance of a general invariant.
Let \(X,W\) be two norms on one finite-dimensional vector space and let

\[
M=\lVert{\rm id}:W\to X\rVert.
\tag{40}
\]

If \(F\) is known only to be holomorphic and bounded by \(B\) on the
\(X\)-ball of radius \(r_X\), the largest \(W\)-ball guaranteed to lie
inside is the ball of radius \(r_X/M\). Banach-line Cauchy gives

\[
\lVert DF(0)\rVert_{W^*}
\le
\frac{BM}{r_X}.
\tag{41}
\]

For a source synthesis \(A:S\to W\),

\[
\lVert DF(0)\circ A\rVert_{S^*}
\le
\frac{BM}{r_X}
\lVert A\rVert_{S\to W}.
\tag{42}
\]

This loss is sharp already in one dimension. Take

\[
\lVert z\rVert_X=|z|,
\qquad
\lVert z\rVert_W=w|z|,
\qquad
F(z)=\frac{B}{r_X}z,
\qquad
A(1)=w^{-1}.
\tag{43}
\]

Then \(M=w^{-1}\), \(\lVert A\rVert_{S\to W}=1\), and equality holds in
(42). With \(w=\xi^2\), the source operator is normalized but the Cauchy
loss is exactly \(\xi^{-2}\).

Thus a diagonal feature renorming cannot, from the existing bounded
\(X\)-tube alone, improve the worst-case physical source derivative. A
larger weighted tube, direct smoothing/cancellation for the assembled
synthesis, or a genuinely different physical-source target is necessary.

## Consequence for the current route

The scaled norm solves two algebraic subproblems:

1. conditional converted \(K,\nabla K\) rows have a regulator-independent
   rowwise envelope in \(Y_{\rm sc}\); and
2. under a common tag atlas and finite \(\Theta\), equation (18) gives the
   physical-width restriction-quotient extension.

It does **not** close the physical-\(U\) pullback. Equations (37)--(43) show
that replacing Note 0031's chart norm by \(Y_{\rm sc}\) returns the finest
scale loss through the analytic radius. Note 0036 subsequently tests the
joint-Ward and vertical-distance alternatives: the exact joint quotient
preserves internal \(U/J\) cancellation, but vertical decay only transfers
the scale power and a same-cell transverse gauge-invariant logical model
survives the retained abstract hypotheses. The narrowed alternatives are:

- exploit the differentiated right-inverse and projected Landau constraints
  of the actual common \(K,\nabla K\) range to prove direct smoothing;
- prove a range-restricted analytic tube or weak-quotient-dual estimate
  stronger than generic product-tube Cauchy;
- impose and justify a deliberately scale-weighted physical-source target;
  or
- prove that the completed coefficients structurally annihilate the
  offending transverse same-cell range.

## Exact boundary

- Equations (12)--(18) are exact finite-dimensional weighted cutoff
  statements after the feature tags are fixed.
- Equation (26) proves that \(\Theta/\rho\) dependence is unavoidable for
  arbitrary weighted graphs.
- Equations (31)--(37) prove that every diagonal raw/gradient
  row-cancelling weighted norm with \(w_0=O(\xi)\),
  \(w_1=O(\xi^2)\) has at most an \(O(\xi^2)\) full curvature-domain radius
  on an admitted homogeneous identity patch. Extra rows are covered by this
  spike only when they evaluate it as \(O(t)\).
- Equations (38)--(39) show that an unweighted curl row alone does not repair
  RG I condition (ii).
- Equations (40)--(43) prove that generic Banach-line Cauchy is invariant
  under the attempted diagonal renorming in the sharp one-dimensional
  model.
- The common Eq. (190) chart/gauge conversion, output tag atlas,
  scale-incidence bound, \((\mathrm H_{\rm rc})\) for the physical family,
  completed Ward premise, and actual-range control remain open. Note 0036
  gives the exact joint quotient and vertical transfer but no uniform bound
  on the actual constrained synthesis. Every later Yang--Mills gate remains
  open.
- No independent human review has been performed.

## Falsification checklist

- Let the source measure cancel the output factors in (2), although it
  cancels only (3)'s input density.
- Treat Eq. (190)'s output scale as an intrinsic unique tag of every global
  bond across all shifted branches.
- Use (18) without bounding \(\Theta\), or suppress its sharp path
  counterexample.
- Call the intrinsic metric (27) fixed-physical-width when
  \(\Theta\to\infty\).
- Put a fixed-radius \(Y_{\rm sc}\)-ball inside Note 0031's domain and omit
  the one-bond plaquette in (31)--(37).
- Add only an unweighted curl row and omit the curl-free longitudinal
  gradient in (38)--(39).
- Replace max by a positive feature sum and claim that fixed norm
  equivalence changes an inverse-mesh power.
- Use Note 0031's unweighted Cauchy bound as a weighted-dual bound without
  the inclusion factor \(M\).
- Promote the weighted cutoff or negative renorming result to an
  unconditional physical first jet, continuum construction, infrared
  theorem, or Yang--Mills mass gap.
