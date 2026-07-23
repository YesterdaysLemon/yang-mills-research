# Note 0018: the raw-\(U\) collar obstruction and a scaled repair target

Claim ID: YM-RG-018

Kind: domain obstruction and conditional analytic-collar lemma

Evidence: E2 (elementary proof; the positive replacement remains conditional)

Novelty: none claimed

Primary anchors: [RG
I](https://doi.org/10.1007/BF01215223), especially Eqs. (1.10)--(1.16)
and printed pp. 262--263, and [RG
II](https://doi.org/10.1007/BF01239022), especially Eqs. (1.34)--(1.35).

## Question left by Notes 0016--0017

RG II localizes its activities on the outer independent-variable domain

\[
\mathcal U_{k+1}^c
\bigl(Y,(1+\beta)\alpha _0,(1+\beta)\alpha _1,
\alpha _0\bigr).
\tag{1}
\]

Note 0017 obtains a regulator-uniform collar in the direct affine \(J\)
coordinate from a strict representative margin. The same argument cannot be
copied for \(U\): changing \(U\) changes the nonlinear regularity conditions
and the derived configurations in RG I condition (iv).

There is also a stronger obstruction. Even at the identity background, (1)
cannot contain a regulator-uniform ball in either of the two naive per-bond
logarithm norms used below.

Put

\[
A_0=(1+\beta)\alpha _0,
\qquad q_\xi=A_0\xi^2.
\tag{2}
\]

RG I condition (iii), Eq. (1.14), is a necessary condition for membership in
the union of complex gauge orbits defining (1). In the notation of the paper,
its \(U\)-part is

\[
|dU-1|_{\rm RG}<q_\xi
\quad\hbox{on }Y.
\tag{3}
\]

No use of conditions (i), (ii), or (iv) can repair a failure of (3).

## Norm convention and the full complex log ball

The paper works in a fixed finite-dimensional matrix representation. Let
\(|\cdot|_{\rm RG}\) denote its matrix norm, let \(\rho\) denote spectral
radius, and fix a comparison constant \(c_{\rm RG}>0\), uniform in
\(\xi\) and \(Y\) for the frozen matrix-norm convention, such that

\[
|M|_{\rm RG}\ge c_{\rm RG}\rho(M).
\tag{4}
\]

Such a constant exists by finite-dimensional norm equivalence. For the
spectral operator norm one may take \(c_{\rm RG}=1\). Keeping (4) explicit
prevents a norm convention from being mistaken for a better radius.

Set

\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad \|H\|_{\rm op}=1.
\tag{5}
\]

Choose one orientation of each unoriented bond. For
\(a:Y_1^+\to\mathfrak {sl}(2,\mathbb C)\), define

\[
U_a(b)=e^{ia(b)},
\qquad U_a(\bar b)=U_a(b)^{-1},
\qquad
\|a\|_{\rm raw}=\sup_{b\in Y_1^+}\|a(b)\|_{\rm op},
\tag{6}
\]

and let \(\mathbb B_{\rm raw}(r)=\{(U_a,0):\|a\|_{\rm raw}<r\}\).
This is the full complex log ball relevant to a holomorphic Cauchy estimate,
not only its compact real slice.

## Sharp curvature threshold in operator-norm normalization

First take \(|\cdot|_{\rm RG}=\|\cdot\|_{\rm op}\). If a plaquette \(q\)
has oriented factors \(F_j=e^{\varepsilon_jia(b_j)}\), then

\[
\|F_j\|_{\rm op}\le e^{\|a(b_j)\|_{\rm op}},
\qquad
\|F_j-1\|_{\rm op}\le e^{\|a(b_j)\|_{\rm op}}-1.
\tag{7}
\]

The telescoping identity for \(F_1F_2F_3F_4-1\) therefore gives

\[
\|dU_a(q)-1\|_{\rm op}
\le e^{\sum_{j=1}^4\|a(b_j)\|_{\rm op}}-1.
\tag{8}
\]

Define

\[
R_{\rm curv}(\xi)=\frac14\log(1+q_\xi).
\tag{9}
\]

If \(r\le R_{\rm curv}(\xi)\) and \(a\in\mathbb B_{\rm raw}(r)\), the sum
in (8) is strictly smaller than \(4r\). Hence every plaquette satisfies
\(\|dU_a-1\|_{\rm op}<q_\xi\). Thus (9) is admissible for the direct
condition-(iii) curvature inequality itself. It does not yet verify the
other orbit-domain conditions.

The threshold is sharp for that inequality. Assume that \(Y\) contains an
elementary plaquette \(p\) strictly in its interior and that its four bonds
are independent coordinates of the proposed ball. Orient
\(\partial p=b_1b_2\bar b_3\bar b_4\), put
\(t=R_{\rm curv}(\xi)\), and set

\[
a(b_1)=a(b_2)=-itH,
\qquad
a(b_3)=a(b_4)=itH,
\tag{10}
\]

with \(a=0\) elsewhere. All four oriented plaquette factors equal \(e^{tH}\),
so

\[
dU_a(p)=e^{4tH},
\qquad
\rho(dU_a(p)-1)=e^{4t}-1=q_\xi.
\tag{11}
\]

For every complex gauge transformation \(g:Y_0\to SL(2,\mathbb C)\),

\[
dU_a^g(p)=g(x_p)dU_a(p)g(x_p)^{-1}.
\tag{12}
\]

Similarity preserves the spectrum, and the operator norm dominates spectral
radius. Consequently every representative violates the strict inequality
(3). For every \(r>R_{\rm curv}(\xi)\), the field (10) lies in the open ball
because \(t<r\). This proves the claimed sharpness without assuming unitary
invariance under a complex gauge transformation.

For the paper's retained norm, use (4) and instead take

\[
t=\frac14\log\left(1+\frac{q_\xi}{c_{\rm RG}}\right).
\]

The same orbit has spectral radius \(q_\xi/c_{\rm RG}\), so (4) excludes
every representative. Therefore any full raw log ball contained in (1) must
satisfy

\[
\boxed{
r_\xi\le
\frac14\log\left(1+\frac{A_0\xi^2}{c_{\rm RG}}\right)
\le \frac{A_0}{4c_{\rm RG}}\xi^2.
}
\tag{13}
\]

The first bound is exact for the direct curvature condition in operator-norm
normalization. With only (4) available, it is an orbit-exclusion upper bound;
other norm comparisons and conditions (i), (ii), and (iv) may shrink the
actual collar further.

Notes 0015--0016 use the scaled coordinate

\[
U_A=e^{i\xi A}U.
\tag{14}
\]

Replacing \(a\) by \(\xi A\) in (13) shows that any corresponding per-bond
operator-sup radius obeys

\[
\boxed{
R_\xi\le
\frac{1}{4\xi}\log\left(
1+\frac{A_0\xi^2}{c_{\rm RG}}\right)
\le \frac{A_0}{4c_{\rm RG}}\xi.
}
\tag{15}
\]

Thus every nonnegative family of radii defined for all sufficiently small
\(\xi\), with fixed \(A_0,c_{\rm RG}\), and satisfying the asserted
full-ball inclusion has

\[
\limsup_{\xi\downarrow0}r_\xi=0,
\qquad
\limsup_{\xi\downarrow0}R_\xi=0.
\tag{16}
\]

This is a failure of the candidate norms, not a failure of analyticity of the
RG-II activities on their printed orbit domain. It also does not deny a
positive radius at any one fixed \(\xi\).

## What a viable norm must do

Let \(h_p\) be the fixed \(\xi\)-independent plaquette-supported direction
whose four entries in (10) are \((-iH,-iH,iH,iH)\). Thus the adversarial
field is \(t_\xi h_p\), where \(t_\xi=O(\xi^2)\). For a homogeneous norm
\(\|\cdot\|_{\mathsf U,\xi}\), a desired ball of one fixed radius
\(r_*>0\) in the raw chart can exclude this direction only if

\[
\|h_p\|_{\mathsf U,\xi}\gtrsim \xi^{-2}.
\tag{17}
\]

In the scaled chart (14), the necessary growth is

\[
\|h_p\|_{\mathsf U,\xi}\gtrsim \xi^{-1}.
\tag{18}
\]

A natural stronger sufficient repair target is that the chart norm uniformly
control the RG-scaled plaquette increment

\[
\xi^{-2}
\sup_p|d(e^{i\xi a}U)(p)-dU(p)|_{\rm RG}.
\tag{19}
\]

Equation (19) is not claimed to be a Banach norm, and it is stronger than the
single-direction necessities (17)--(18). By itself it is also not a
sufficiency theorem: it does not encode the local-gauge regularity in RG I
Eqs. (1.12)--(1.13).

## Conditional scaled-collar template

The paragraph after RG I Eq. (1.16) gives a useful sufficient-domain
mechanism. Choose strict smaller constants

\[
0<a_0'<\alpha_0<A_0,
\qquad 0<a_1'<A_1:=(1+\beta)\alpha_1,
\tag{20}
\]

in the paper's qualitative ``sufficiently small'' regime. Configurations
satisfying conditions (i)--(iii) with these smaller constants satisfy
condition (iv) and hence belong to the outer domain. The paper does not print
a numerical radius or a transported chart atlas.

The strongest honest collar consequence is therefore conditional. Assume
the following hypothesis \((\mathrm H_U)\) for every centre in the closure of
the physical source patch and every shifted activity chart.

1. There is one shared representative
   \(U_*=U_*'U_{*,0}\), with \(U_{*,0}\) group valued, satisfying condition
   (i) with \(a_0'\). Its direct independent coordinate satisfies
   \(\|J_*\|_{\infty,Y}<a_0'<\alpha_0\), the smaller condition-(iii) bound
   compatible with (1)'s un-enlarged third parameter.
2. The split relative chart
   \[
   \Phi_{U_*}(a)=e^{i\xi a}U_*'U_{*,0}
   \tag{21}
   \]
   holds \(U_{*,0}\) and \(J_*\) fixed. Thus condition (i) and the direct
   \(J\) bound do not change along the chart.
3. On the selected local logarithm/BCH branch, let \(q_{ii}(U')\) denote the
   least Eq. (1.13) regularity constant and set
   \(q_{iii}(U)=\xi^{-2}\sup_p|dU(p)-1|_{\rm RG}\). There are common margins
   \(\delta_1,\delta_0>0\) such that
   \[
   q_{ii}(U_*')\le a_1'-\delta_1,
   \qquad
   q_{iii}(U_*)\le a_0'-\delta_0.
   \tag{22}
   \]
4. There are a complex Banach norm \(\|\cdot\|_{\mathsf U}\), a common chart
   radius \(r_{\log}>0\), and constants \(C_{ii},C_{iii}\), independent of
   volume, location, and RG step in one frozen fixed-\(M\) hierarchy, such
   that for \(\|a\|_{\mathsf U}<r_{\log}\),
   \[
   q_{ii}(e^{i\xi a}U_*')
   \le q_{ii}(U_*')+C_{ii}\|a\|_{\mathsf U},
   \tag{23}
   \]
   \[
   \xi^{-2}\sup_p
   |d\Phi_{U_*}(a)(p)-dU_*(p)|_{\rm RG}
   \le C_{iii}\|a\|_{\mathsf U}.
   \tag{24}
   \]

Then

\[
\boxed{
r_U=\min\left\{
r_{\log},\frac{\delta_1}{C_{ii}},
\frac{\delta_0}{C_{iii}}
\right\}>0
}
\tag{25}
\]

is a full complex \(\mathsf U\)-ball contained in (1). Here a quotient with a
zero Lipschitz constant is omitted from the minimum. Conditions (i)--(iii)
remain in the strict smaller domain by \((\mathrm H_U)\), items 1--4, using
(22)--(24) for condition (ii) and the \(U\)-part of condition (iii). RG I's
p. 263 mechanism supplies condition (iv).

If \(\widehat W_Y\) is analytic and bounded by \(A_Y\) on the corresponding
outer domain, define its chart derivative by

\[
D_U^{\Phi}\widehat W_Y
:=D(\widehat W_Y\circ\Phi_{U_*})(0).
\]

Cauchy's formula on complex lines gives the conditional bound

\[
\boxed{
\|D_U^{\Phi}\widehat W_Y\|_{\mathsf U^*}
\le \frac{A_Y}{r_U}.
}
\tag{26}
\]

No hypothesis in (22)--(24) is proved here. They are the precise replacement
for the impossible raw-radius premise.

## Exact boundary

- Equations (13) and (15) are proved only for an admitted domain containing
  one full elementary plaquette and the identity centre. That already
  disproves a positive uniform radius asserted for every activity centre.
- The exact constants use the operator-sup logarithm norm and the comparison
  convention (4). Any uniformly equivalent raw per-bond norm has the same
  \(O(\xi^2)\) or \(O(\xi)\) collapse, with changed constants.
- The obstruction concerns full independent-link balls. It does not rule out
  structured minimizing-field or coarse-\(B\) directions, nor a ball in an
  RG-scaled regularity norm that penalizes isolated spikes.
- RG I Proposition 9 controls a constrained minimizing branch. Its image is
  not an open neighborhood in the full independent-link space, so it does
  not contradict (13).
- The p. 263 inclusion is used in (25) only under the explicitly named
  smaller-domain, representative, chart, and uniform Lipschitz hypotheses.
  RG I Theorem 3 allows its small-field constants to depend on fixed \(M\).
- Note 0021 supplies exact fixed-partition marked algebra, and Note 0026
  supplies its independent-variable convergent first jet. No
  \(U\)-derivative norm in a concrete RG-scaled Banach space, physical
  chain-rule pullback, synchronized marked expansion, large-field estimate,
  RG iteration, continuum construction, infrared decay, or mass gap follows.

## Falsification checks

- Apply a complex gauge transformation to (10) and verify the plaquette
  holonomy is conjugated rather than changed spectrally.
- Replace the matrix norm by one not normalized as in (4) and track
  \(c_{\rm RG}\) instead of silently setting it to one.
- Use a plaquette touching the boundary whose four bonds are not independent
  coordinates of the local ball and identify the missing geometric premise.
- Forget that the ball is open; at a proposed \(r>R_{\rm curv}(\xi)\), check
  that the adversarial field has norm \(R_{\rm curv}(\xi)<r\).
- Set \(U=e^{i\xi A}\) but reuse the raw radius bound without dividing by
  \(\xi\); (15), not (13), is the scaled-coordinate conclusion.
- Attempt to use Proposition 9's minimizing branch as a full independent
  \(U\)-ball and identify the lost transverse link directions.
- Claim that the stronger scaled plaquette control (19) proves Eq. (1.13);
  the local representative/BCH estimate (23) is still missing.
- Vary the group-valued factor \(U_{*,0}\) in (21) without controlling RG I
  condition (i) and reject the conditional collar proof.
