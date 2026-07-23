# Note 0031: a real-center covariant-\(U\) tube and product Banach norm

Claim ID: YM-RG-031

Kind: conditional finite-regulator analytic-collar and connected-norm lemma

Evidence: E2 (elementary matrix proof plus a primary-source domain
crosswalk; internally checked)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I*](https://doi.org/10.1007/BF01215223), especially Eqs.
  (1.10)--(1.16) and the smaller-domain discussion on printed pp. 262--263;
- T. Balaban, [*Spaces of Regular Gauge Field Configurations on a Lattice
  and Gauge Fixing Conditions*](https://doi.org/10.1007/BF01466594),
  especially Eqs. (1.21), (1.47)--(1.50), (1.139)--(1.145), and
  Proposition 7 on printed pp. 79, 84--85, and 100.

## Scope and the new sufficient hypothesis

Retain the complete finite-regulator construction and hypotheses of Notes
0024--0030. In particular, retain the fixed \(M\), every admitted nested
shifted branch, the ordinary and marked convergence hypotheses, and the
completed connected constant \(B_{\rm conn}\).

RG II's outer domain has parameters

\[
\mathcal U_{k+1}^c
\bigl(Y,(1+\beta)\alpha _0,(1+\beta)\alpha _1,\alpha _0\bigr).
\tag{1}
\]

Choose fixed smaller constants

\[
0<a_0<\alpha _0,
\qquad
0<a_1<\alpha _1,
\tag{2}
\]

in the qualitative smallness range of RG I printed p. 263. Thus a
configuration whose \(U\)-parts of RG I conditions (i)--(iii) satisfy the
smaller \(a_0,a_1\) bounds has the corresponding source-derived condition
(iv). If its independent \(J\) separately satisfies the unchanged direct
ceiling \(\alpha _0\), the pair belongs both to (1) and to the fixed-output
domain. The smaller-domain argument for condition (iv) depends on \(U\);
it does not replace the third parameter in (1) by \(a_0\). The source does
not print numerical choices for \(a_0,a_1\).

The result below uses the following explicit sufficient replacement for
Note 0030's separate completed-\(J\) representative hypothesis and Note
0018's abstract \(U\)-collar hypothesis.

**Common real-center hypothesis \((\mathrm H_{\rm rc})\).** Every retained
physical center has one global representative

\[
(\bar U,J_0)
\tag{3}
\]

with these properties.

1. \(\bar U\) is \(G\)-valued in the fixed faithful unitary representation.
   Its restriction to every input, intermediate, output, and shifted chart
   is the representative used there. Shift transport is the corresponding
   bond permutation of the same global pair.
2. On every required local domain, \(\bar U\) satisfies RG I condition (i)
   with the smaller constant \(a_0\). For one common
   \(0\le\bar a_U<a_0\), it also has the stronger direct curvature margin
   \[
   |d\bar U(p)-1|_{\rm RG}
   \le \bar a_U\xi ^2
   \tag{4}
   \]
   at every plaquette used by a retained branch.
3. For one common \(0\le\bar a_J<\alpha _0\),
   \[
   \lVert J_0\rVert_{\infty,{\rm RG}}\le\bar a_J.
   \tag{5}
   \]
4. The smaller-domain implication on RG I printed p. 263 applies uniformly
   to all these restrictions at the fixed \(M\). In particular, once the
   \(U\)-parts of conditions (i)--(iii) satisfy the smaller
   \(a_0,a_1\) bounds, the fields derived from that \(U\) in condition (iv)
   obey the required outer and output bounds. The independent \(J\) is
   tested separately against the third parameter \(\alpha _0\).

This is a stronger physical-center premise than the source currently proves
uniformly in the repository. It is nevertheless concrete: it asks for one
real global minimizing representative with strict curvature and independent
\(J\) margins. It does not ask for compatible choices among unrelated
complex gauge representatives.

## The covariant relative-log norm

Fix one center \(\bar U\) and \(0<\xi\le1\). Work on one orientation of the
independent bonds. For a complexified Lie-algebra bond field \(a\), define

\[
\Phi_{\bar U}(a)(b)=e^{i\xi a(b)}\bar U(b)
\tag{6}
\]

on the chosen orientation and define the reverse link by inversion. This is
equivalent to the linear reverse-orientation convention

\[
a(\bar b)=-\operatorname {Ad}_{\bar U(b)^{-1}}a(b).
\tag{7}
\]

For a plaquette \(p\), push the four \(\bar U\)-links in
\(d\Phi_{\bar U}(a)(p)\) to the right. This gives the exact factorization

\[
d\Phi_{\bar U}(a)(p)
=F_p(a)\,d\bar U(p),
\qquad
F_p(a)=\prod_{\ell=1}^4e^{i\xi X_{\ell,p}(a)},
\tag{8}
\]

where every \(X_{\ell,p}(a)\) is a unitary transport of one oriented value
of \(a\). Define the covariant plaquette curl by

\[
\mathcal D_{\bar U}^{\xi}a(p)
=\xi^{-1}\sum_{\ell=1}^4X_{\ell,p}(a).
\tag{9}
\]

This is the linear term in Balaban's Eqs. (1.47)--(1.50). The definition in
(9) fixes all orientation signs without identifying it with a differently
normalized source symbol.

Let \(\lVert\cdot\rVert_{\rm op}\) be the operator norm. Freeze one
finite-dimensional comparison constant \(c_+\) such that

\[
|M|_{\rm RG}\le c_+\lVert M\rVert_{\rm op}
\tag{10}
\]

for every matrix in the fixed representation. Define

\[
\begin{aligned}
\lVert a\rVert_{\mathsf U(\bar U),\xi}
=\max\{&
\lVert a\rVert_{\infty,{\rm RG}},
\lVert\nabla_{\bar U}^{\xi}a\rVert_{\infty,{\rm RG}},\\
&\lVert a\rVert_{\infty,{\rm op}},
\lVert\mathcal D_{\bar U}^{\xi}a\rVert_{\infty,{\rm op}}
\}.
\end{aligned}
\tag{11}
\]

The first two entries are the quantities in RG I condition (ii); the scale
is part of the superscripted covariant derivative
\(\nabla_{\bar U}^{\xi}\), not a separate prefactor. The last two entries
are retained even if a selected source convention already controls them by
the first two. They make the curvature estimate independent of that
convention. For a completed shifted family, (11) means the supremum over all
translated local stencils used by its branches. Restriction to a local
stencil is therefore a contraction and taking a supremum over shifts
introduces no branch-count factor.

Because (11) contains \(\lVert a\rVert_\infty\), it is a complex Banach norm
on the finite-dimensional independent-bond space. It penalizes an isolated
bond spike through the covariant derivative/curl entries. It is not either
raw bond-sup norm ruled out by Note 0018.

## A complex plaquette remainder lemma

Let \(\lVert a\rVert_{\mathsf U(\bar U),\xi}<r\). Put

\[
q_p=\xi\sum_{\ell=1}^4
\lVert X_{\ell,p}(a)\rVert_{\rm op}<4\xi r.
\tag{12}
\]

For arbitrary matrices \(Y_1,\ldots,Y_4\), set
\(F(t)=\prod_{\ell=1}^4e^{tY_\ell}\). Twice differentiating the ordered
product and using submultiplicativity gives

\[
\lVert F''(t)\rVert_{\rm op}
\le
\left(\sum_{\ell=1}^4\lVert Y_\ell\rVert_{\rm op}\right)^2
\exp\!\left(
t\sum_{\ell=1}^4\lVert Y_\ell\rVert_{\rm op}
\right).
\tag{13}
\]

Taylor's formula with integral remainder, applied with
\(Y_\ell=i\xi X_{\ell,p}(a)\), yields

\[
\left\lVert
F_p(a)-1-i\xi\sum_{\ell=1}^4X_{\ell,p}(a)
\right\rVert_{\rm op}
\le\frac12q_p^2e^{q_p}
<8\xi^2r^2e^{4\xi r}.
\tag{14}
\]

Equation (9) bounds the linear term by \(\xi^2r\). Since
\(d\bar U(p)\) is unitary, (4), (8), (10), and (14) give

\[
\boxed{
|d\Phi_{\bar U}(a)(p)-1|_{\rm RG}
<
\xi^2\left[
\bar a_U+c_+\left(r+8r^2e^{4\xi r}\right)
\right].
}
\tag{15}
\]

No Hermiticity was used. Thus (15) holds on the full complexified
independent-link ball, not merely on the compact real slice. Proposition 7
is consistent with the same linear-plus-quadratic curvature cost, but it is
not used to extend a real gauge-fixing theorem to complex fields.

Put

\[
\delta_U=a_0-\bar a_U>0,
\qquad
C_U=c_+(1+8e^4),
\tag{16}
\]

and define

\[
\boxed{
r_U
=\min\left\{
1,\ a_1,\ \frac{\delta_U}{C_U}
\right\}>0.
}
\tag{17}
\]

If \(\lVert a\rVert_{\mathsf U(\bar U),\xi}<r_U\), then RG I condition
(ii) holds with \(a_1\), while (15) and \(0<\xi\le1\) give

\[
|d\Phi_{\bar U}(a)-1|_{\rm RG}<a_0\xi^2.
\tag{18}
\]

Condition (i) is unchanged because the split in (6) keeps the group-valued
factor \(\bar U\) fixed. Hypothesis \((\mathrm H_{\rm rc})\), item 4, then
supplies condition (iv).

This proves the concrete complex \(U\)-collar that Note 0018 left
conditional. Its positive radius comes from the covariant-curl norm, not
from finite-regulator compactness.

## One common product tube

Define the independent-\(J\) radius

\[
\Delta_J=\alpha _0-\bar a_J>0.
\tag{19}
\]

For each retained physical center, let

\[
\mathbb T_{U,J}(\bar U,J_0)
=
\left\{
\bigl(\Phi_{\bar U}(a),J_0+w\bigr):
\lVert a\rVert_{\mathsf U(\bar U),\xi}<r_U,\
\lVert w\rVert_{\infty,{\rm RG}}<\Delta_J
\right\}.
\tag{20}
\]

Every point of (20) satisfies RG I conditions (i), (ii), and the
\(U\)-part of (iii) with the smaller constants by (17)--(18).
Condition (iv) depends on \(U\), not on the independent \(J\), and follows
from \((\mathrm H_{\rm rc})\). Finally,

\[
\lVert J_0+w\rVert_{\infty,{\rm RG}}
<
\bar a_J+\Delta_J
=\alpha _0,
\tag{21}
\]

so the direct \(J\)-part of condition (iii) holds on every outer and output
domain. Consequently,

\[
\boxed{
\mathbb T_{U,J}(\bar U,J_0)
\text{ is contained in every external domain of the complete branch.}
}
\tag{22}
\]

The map \((a,w)\mapsto(\Phi_{\bar U}(a),J_0+w)\) is holomorphic on the
entire parameter space because it is a finite product of matrix
exponentials and affine maps. Source analyticity on the containing domains
therefore gives holomorphy of every pulled-back coefficient on the full
parameter ball.

The same global representative is restricted everywhere, and shifted
transport only permutes the stencils used in the suprema. Thus
\((\mathrm H_{\rm rc})\) implies Note 0030's
\((\mathrm H_J^{\rm conn})\) for this retained family. It is a sufficient
replacement, not a derivation of a global representative for every
background orbit admitted by the source.

## Product-\(H^\infty\) rerun

For fixed regulator and center, use the commutative Banach algebra

\[
\mathscr A_{\bar U,J_0}
=H^\infty\!\left(
\mathbb B_{\mathsf U}(r_U)
\times\mathbb B_{\ell^\infty}(\Delta_J)
\right)
\tag{23}
\]

with its supremum norm, after pulling every coefficient back by
\((a,w)\mapsto(\Phi_{\bar U}(a),J_0+w)\). This definition does not require
\(\Phi_{\bar U}\) to be globally injective. The input potential and
final-activity estimates used in Note 0030 are already uniform over their
full source domains. Equation (22) therefore lets every finite sum, product,
restriction, weakening integral, positive resummation, and pinned Ursell
estimate in Notes 0024--0030 be repeated in (23). The positive majorants and
the shifted post-connected normalization are unchanged.

Hence the completed coefficients obey the stronger product-tube norm

\[
\boxed{
\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\sup_{\substack{
\lVert a\rVert_{\mathsf U(\bar U),\xi}<r_U\\
\lVert w\rVert_{\infty,{\rm RG}}<\Delta_J
}}
\left|
\widehat{\mathcal C}_p^+
\bigl(s,R;\Phi_{\bar U}(a),J_0+w\bigr)
\right|
\le B_{\rm conn}.
}
\tag{24}
\]

As in Note 0030, (24) is obtained coefficientwise before the \(R\)-sum. It
is not inferred by exchanging a pointwise sum with separately optimized
suprema.

## Two full dual derivative norms

Define the chart derivative at the real center by

\[
D_U^\Phi\widehat{\mathcal C}_p^+[h]
=
\left.\frac{d}{dz}\right|_{z=0}
\widehat{\mathcal C}_p^+
\bigl(s,R;\Phi_{\bar U}(zh),J_0\bigr).
\tag{25}
\]

For every global \(h\) with
\(\lVert h\rVert_{\mathsf U(\bar U),\xi}\le1\), the whole complex line
\(|z|<r_U\) lies in (20). Cauchy's formula therefore controls the full
global dual norm directly; no support projection or zero extension is
needed. The same argument applies to arbitrary global \(J\)-directions of
\(\ell^\infty\)-norm at most one. Summing the coefficientwise bounds in
(24) gives

\[
\boxed{
\sup_p\sup_{\mathfrak K_p^{\rm rc}}
\sum_{s,R}e^{\kappa d_{k+1,s}(R)}
\left\|
D_U^\Phi\widehat{\mathcal C}_p^+(s,R)
\right\|_{\mathsf U^*}
\le\frac{B_{\rm conn}}{r_U},
}
\tag{26}
\]

and

\[
\boxed{
\sup_p\sup_{\mathfrak K_p^{\rm rc}}
\sum_{s,R}e^{\kappa d_{k+1,s}(R)}
\left\|
D_J\widehat{\mathcal C}_p^+(s,R)
\right\|_{(\ell^\infty)^*}
\le\frac{B_{\rm conn}}{\Delta_J}.
}
\tag{27}
\]

Neither estimate has a bond-volume or shifted-branch factor.

## Exact boundary

- The matrix estimate (15), the radius (17), and the Banach-algebra
  implication are proved here. The regulator-uniform existence of the
  common real representatives and strict margins in
  \((\mathrm H_{\rm rc})\) is not proved by the source audit.
- For the \(J\)-coordinate alone, \((\mathrm H_{\rm rc})\) is stronger than
  necessary. A restriction-natural, support-preserving cocycle atlas with
  transition norms at most \(K\) would give radius
  \(\Delta_J/K\) and derivative bound
  \(K B_{\rm conn}/\Delta_J\). The source audit does not prove such a
  uniform atlas; arbitrary complex transitions can have unbounded adjoint
  norm. The real-center hypothesis is retained here because it supplies one
  product \(U/J\) chart.
- RG I printed p. 263 gives a qualitative smaller-domain mechanism and
  identifies sufficiently regular minimal configurations, but it does not
  print common numerical \(a_0,a_1,\bar a_U,\bar a_J\) for every regulator
  and shifted branch used here.
- Proposition 7 is stated for Lie-algebra-valued real perturbations. This
  note uses only its surrounding plaquette algebra as provenance and proves
  the needed complex estimate independently.
- The derivative in (26) is a relative-log chart derivative. Note 0033
  supplies an unweighted physical coarse-field \(U\)-summand under common
  converted Proposition 9 Eq. (190) rows and a global scale envelope, then
  identifies the exact restriction-quotient moment for positive source
  decay. Note 0034 proves the curvature-corrected curl identity, reduces the
  required source rows to the raw-RG and covariant-gradient-RG pair, and
  proves the quotient extension on a collar of fixed physical thickness.
  Note 0035 then proves that multiplying those two rows by their matching
  output scales does not repair the physical pullback: the common analytic
  radius shrinks as \(O(\xi^2)\), and generic Cauchy restores the
  \(\xi^{-2}\) loss. The reduced converted rows, a direct
  smoothing/cancellation or two-norm replacement, the active-label metric
  halo, and \((\mathrm H_{\rm rc})\) for the physical family remain unproved.
- Equations (26)--(27) do not discharge Note 0019's
  \((\mathrm H_\rho)\), bounded mesh matching, or common kernel/chart
  constants. They also do not construct a nonzero scalar-source polymer
  disk.
- No intrinsic/unrestricted raw-law comparison, unit-translation theorem,
  large-field estimate, RG iteration, continuum or infinite-volume
  construction, Osterwalder--Schrader reconstruction, infrared decay, or
  Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Drop the covariant curl from (11) and place independent \(O(1)\) values on
  the four bonds of one plaquette; recover Note 0018's collapsing raw radius.
- Replace the unitary real center by an arbitrary complex representative and
  use unitary invariance in (12); the proof then loses its uniform transport
  bound.
- Replace \(\sum X_{\ell,p}=\xi\mathcal D_{\bar U}^{\xi}a\) by a raw sum
  without the factor \(\xi\), creating a false \(O(\xi)\) curvature term.
- Omit the quadratic exponential remainder in (14), especially for
  noncommuting link matrices.
- Use Proposition 7 itself for complex \(a\), despite its printed real
  Lie-algebra hypothesis.
- Let the base curvature approach \(a_0\xi^2\) so that
  \(\delta_U\downarrow0\), and observe \(r_U\downarrow0\).
- Perturb the independent \(J\) but recompute it inside condition (iv);
  RG I condition (iv) instead uses the field derived from \(U\).
- Use unrelated representatives in different branches and claim that
  \((\mathrm H_{\rm rc})\) holds.
- Infer (24) from a pointwise connected sum without the
  coefficientwise \(H^\infty\) rerun.
- Promote the chart derivative (26) to an unconditional physical
  coarse-field pullback without Note 0034's reduced converted rows and a
  regulator-uniform treatment of their output scales, or anchor its
  physical-width feature collar at smaller active labels without a
  tagged-metric crosswalk.
- Replace that missing scale argument by a diagonal \(s_j,s_j^2\) chart
  renorming without confronting Note 0035's \(O(\xi^2)\) analytic-radius
  obstruction.
