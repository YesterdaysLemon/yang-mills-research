# Note 0029: completed external-\(J\) support through the literal union

Claim ID: YM-RG-029

Kind: finite-regulator external-field locality and support-anchor corollary

Evidence: E2 (exact support algebra; internally checked)

Novelty: none claimed

Primary anchors:

- T. Bałaban,
  [*Renormalization Group Approach to Lattice Gauge Field Theories. I*](https://doi.org/10.1007/BF01215223),
  printed pp. 251 and 262 for the bond-intersection restriction convention;
- T. Bałaban,
  [*Renormalization Group Approach to Lattice Gauge Field Theories. II.
  Cluster Expansions*](https://doi.org/10.1007/BF01239022), especially the
  locality statement immediately after Eq. (2.9), the factorization in
  Eq. (2.10), the literal-union connected grouping in Eq. (2.13), and the
  \((U,J)\)-analyticity discussion on the following page.

The immutable page and source/repository boundary are recorded in the
[completed-support audit](../../literature/audits/2026-07-23-balaban-completed-external-j-support.md).

## The remaining support question

Note 0028 proved zero support halos for the first-stage direct-\(J\)
activities of Notes 0012--0014, but deliberately left the completed
Section-2 coefficient open. The object needed by the physical pullback is
not a first-stage activity. It is the branchwise connected coefficient

\[
\widehat{\mathcal C}_p^+(s,R;U,J)
\tag{1}
\]

from Note 0027, after conditioning, the second localization,
post-polymerization marked resummation, the connected logarithm, and shift
normalization.

The missing issue is whether those operations can introduce dependence on an
external independent-\(J\) coordinate outside \(R\). They do not. This note
proves that support statement. It does not prove the quantitative common
complex tube needed to bound the derivative.

## Local external-field algebras and the source bond convention

Fix one finite regulator and one nested shifted branch \(s\). Let
\(E_s^+\) be one global orientation of the independent external bonds. For a
connected final support \(C\), put

\[
\mathsf E_s^{\rm loc}(C)
=
\{b\in E_s^+:\ |b|\cap\operatorname {int}C\ne\varnothing\}.
\tag{2}
\]

This is the source convention, not an endpoint-ownership convention. RG I
printed p. 251 says that a continuous subset determines the nearest-neighbor
bond intervals which intersect it; printed p. 262 then defines both \(U\)
and \(J\) on the bonds of a localization domain. Consequently, restriction
to \(\operatorname {int}C\) retains the coordinates in (2). It does **not**
by itself imply \(|b|\subset\operatorname {int}C\).

Let \(\mathfrak D_s\) be the branch analytic external \((U,J)\) domain used
in Note 0027. Define
\(\mathscr A_s(C)\) to be the algebra of holomorphic functions \(F\) on
\(\mathfrak D_s\) with the restriction property

\[
\begin{aligned}
&(U,J),(U',J')\in\mathfrak D_s,\\
&(U,J)|_{\mathsf E_s^{\rm loc}(C)}
=(U',J')|_{\mathsf E_s^{\rm loc}(C)}
\quad\Longrightarrow\quad
F(U,J)=F(U',J').
\end{aligned}
\tag{3}
\]

For the \(J\)-only conclusion below, \(U=U'\) may be held fixed in (3).

These algebras have the elementary support rules

\[
\mathscr A_s(C)\mathscr A_s(C')
\subset
\mathscr A_s(C\cup C'),
\qquad
\mathscr A_s(C)+\mathscr A_s(C')
\subset
\mathscr A_s(C\cup C').
\tag{4}
\]

The same inclusion holds for any convergent sum whose summands all belong to
\(\mathscr A_s(R)\). Indeed, two external fields agreeing on
\(\mathsf E_s^{\rm loc}(R)\) give equal summands term by term and hence
equal sums. Here
\(\mathsf E_s^{\rm loc}(C)\cup\mathsf E_s^{\rm loc}(C')
\subset\mathsf E_s^{\rm loc}(C\cup C')\), which is all (4) needs. Local
uniform convergence, available under the ordinary and marked cluster
hypotheses retained below, also preserves holomorphy.

## Ordinary and marked final activities

At the beginning of RG II Section 2, Bałaban suppresses the external gauge
fields from the notation. Immediately after Eq. (2.9), the paper states that
\(H(Z)\) is “localized in the interior of \(Z\) with respect to the external
gauge fields.” The following-page analyticity discussion names those fields
as \((U,J)\). Therefore, on every transported branch,

\[
H_s(C)\in\mathscr A_s(C).
\tag{5}
\]

Equation (5) is a source theorem for the unmarked activity on one chosen
cubulation, transported as in Note 0027.

The marked statement is a repository coefficientwise corollary. Note 0012
gives

\[
W_{k,p}^s(A)\in\mathscr A_s(A)
\tag{6}
\]

in the independent \((U,J,B)\) coordinates. Notes 0021 and 0025 then insert
that factor into the exact finite Section-2 construction:

- the marked support \(A\) is included in the seed;
- conditioning leaves the mark a function of the conditional interior
  field \(B\);
- standardization acts only on the exterior Gaussian coordinate;
- the second weakening localizes the covariance/operator sector and does not
  insert exterior coordinates into the mark; and
- the output assignment contains the complete marked seed.

Run that construction over
\(\mathbb D=\mathbb C[\epsilon]/(\epsilon^2)\). For one connected output
\(C\), its dual-number activity is

\[
H_{p,s}^{\mathbb D}(C)
=
H_s(C)-\epsilon W_{p,s}^{\rm post}(C).
\tag{7}
\]

The same external-field restriction proof used for (5) applies
coefficientwise: the additional coefficient (6) is already local on a seed
contained in \(C\), while every later operation is source-parameter
independent. Hence

\[
H_{p,s}^{\mathbb D}(C)
\in
\mathscr A_s(C)\otimes\mathbb D,
\qquad
\boxed{
W_{p,s}^{\rm post}(C)\in\mathscr A_s(C).
}
\tag{8}
\]

Equation (8) is not a marked theorem printed by Bałaban. It uses the exact
dual-number map of Note 0021 and the corrected interior-field routing of
Note 0025.

## The connected literal-union theorem

Notes 0023--0024 identify the hull of a nonzero final connected occurrence
tuple with its literal cube-label union. Thus Note 0027 Eq. (18) may be read
as

\[
\begin{aligned}
\mathcal C_{p,s}^{+}(R)
={}&
\sum_{C_0\supset\widehat Q_{p,s}}
\sum_{n\ge0}\frac1{n!}
\sum_{\substack{C_1,\ldots,C_n\\
C_0\cup\cdots\cup C_n=R}}
\Phi_s^T(C_0^\bullet,C_1,\ldots,C_n)\\
&\qquad\qquad\times
W_{p,s}^{\rm post}(C_0)
\prod_{i=1}^nH_s(C_i),
\end{aligned}
\tag{9}
\]

where terms with zero Ursell coefficient may harmlessly remain in the sum.
The coefficient \(\Phi_s^T\) depends only on the fixed incompatibility
graph, not on \(U\) or \(J\). By (4), (5), and (8), every nonzero summand in
(9) lies in

\[
\mathscr A_s(C_0\cup\cdots\cup C_n)
=
\mathscr A_s(R).
\tag{10}
\]

Repeated labels do not change the union and do not change (10). Under
Notes 0024 and 0026, the connected marked sum converges absolutely and
locally uniformly on the retained branch domain. Therefore

\[
\mathcal C_{p,s}^{+}(R)\in\mathscr A_s(R).
\tag{11}
\]

Note 0027 normalizes only after the branch connected map:

\[
\widehat{\mathcal C}_p^+(s,R)
=
\widetilde n_p^{-1}\mathcal C_{p,s}^+(R).
\tag{12}
\]

The scalar \(\widetilde n_p^{-1}\) is external-field independent, so

\[
\boxed{
\widehat{\mathcal C}_p^+(s,R)\in\mathscr A_s(R).
}
\tag{13}
\]

Equivalently, if two admitted external fields have identical restrictions
to \(\mathsf E_s^{\rm loc}(R)\), then their completed normalized
coefficients in (13) are equal. The projective reconstruction scalar
\(S_s(U,J)\) from Note 0027 causes no exception: it cancels before (9) is
formed and is not an extra factor in the connected coefficient.

## Completed external-\(J\) support and the aligned-cubulation anchor

Define the completed derivative-support set on the common branch domain by

\[
I^{\rm conn}_{J,p,s}(R)
=
\left\{
b\in E_s^+:
D_{J(b)}
\widehat{\mathcal C}_p^+(s,R)
\text{ is not identically zero}
\right\}.
\tag{14}
\]

Holomorphy and (13) give the exact support theorem

\[
\boxed{
I^{\rm conn}_{J,p,s}(R)
\subset
\mathsf E_s^{\rm loc}(R).
}
\tag{15}
\]

Equation (15) is the exact source-licensed support statement. The zero-halo
anchor needs one additional elementary fact about the repository
cubulations.

The input and output cubulations in Notes 0014 and 0027 have walls at
integer current-lattice coordinates: their side lengths are \(M\) and
\(LM\), and every admitted shift is an integer lattice translation. Regard
their cubes and their unions as closed geometric sets, as in Note 0028.
For such a grid-aligned cubical union \(R\), a current-lattice
nearest-neighbor segment which meets \(\operatorname {int}R\) is contained
in \(R\). Indeed, choose an interior point of the segment. No cubulation wall
normal to the bond lies strictly between two consecutive lattice sites.
On the open bond cell, membership in the cubical complex is constant; since
one point is interior, the open segment lies in \(R\), and closedness adds
both endpoints. At the periodic seam, apply the same argument to a lift of
the bond and cubulation in the torus cover. Thus

\[
b\in\mathsf E_s^{\rm loc}(R)
\quad\Longrightarrow\quad
|b|\subset R.
\tag{16a}
\]

Choose the initial site of each globally oriented bond as its deterministic
anchor. Equations (15) and (16a) put that anchor in \(R\). The plaquette base
site is strictly inside the input root \(Q_{p,s}\), while Note 0027 gives

\[
Q_{p,s}\subset\widehat Q_{p,s}\subset R.
\tag{16}
\]

It is therefore an admitted root anchor in \(R\). The completed coefficient,
not only the first-stage activity, satisfies Note 0028's support-anchor
condition with

\[
\boxed{h=h_q=0.}
\tag{17}
\]

The conclusion also records external-\(U\) restriction locality through
(13), but it supplies no additive or RG-scaled nonlinear \(U\) tube.

## Output-scale endpoint consequence

Instantiate Note 0028 at the output scale. Let \(b_{k+1,s}\) be the ratio
between the shifted \((k+1)\)-localization mesh and the finest
Propagators-II mesh, assume the two periodic divisibility conditions from
Note 0028, and retain \((\mathrm H_\rho)\). With

\[
c_{\rm nn}=d(L+2)+1,
\tag{18}
\]

Equations (15)--(17) give

\[
\boxed{
D_{\mathcal B}(q_{p,s},R)
\le
c_{\rm nn}\sqrt d\,M b_{k+1,s}\,d_{k+1,s}(R)
+2d\,c_{\rm nn}M b_{k+1,s}.
}
\tag{19}
\]

No shift-orbit or \(L^4\)-lift factor occurs. Equation (19) is a support and
geometry statement. It does not estimate
\(D_J\widehat{\mathcal C}_p^+(s,R)\).

## The quantitative tube still missing

The base-point norm in Note 0027 Eq. (25) and a nonempty common branch
domain do not imply a common Cauchy radius. To obtain a regulator-uniform
completed \(J\)-derivative norm, one still needs constants
\(\Delta_J^{\rm conn}>0\) and \(B_{\rm conn}^{\rm tube}<\infty\), common in
the regulator, \(p,s,R\), and admitted background. Let
\(\mathfrak K_p^{\rm phys}\subset\mathfrak D_p^\cap\) be the retained
physical base set. One must prove that, for every
\((U,J)\in\mathfrak K_p^{\rm phys}\), the
\(\ell^\infty\)-ball

\[
\left\{
J+w:
\operatorname {supp}w\subset\mathsf E_s^{\rm loc}(R),
\ \lVert w\rVert_{\ell^\infty}<\Delta_J^{\rm conn}
\right\}
\tag{20}
\]

stays in the completed coefficient domain and

\[
\boxed{
\sup_p
\sup_{(U,J)\in\mathfrak K_p^{\rm phys}}
\sum_{\substack{s\in\widetilde{\mathcal A}_{M,L}(p)\\
R\supset\widehat Q_{p,s}}}
e^{\kappa d_{k+1,s}(R)}
\sup_{\substack{\operatorname {supp}w\subset
\mathsf E_s^{\rm loc}(R)\\
\lVert w\rVert_{\ell^\infty}<\Delta_J^{\rm conn}}}
\left|
\widehat{\mathcal C}_p^+(s,R;U,J+w)
\right|
\le
B_{\rm conn}^{\rm tube}.
}
\tag{21}
\]

The sums in (21) use the same root restriction and branch family as Note
0027. If (20)--(21) are proved, Banach-space Cauchy gives, without a bond
count,

\[
\sup_p
\sup_{(U,J)\in\mathfrak K_p^{\rm phys}}
\sum_{s,R}
e^{\kappa d_{k+1,s}(R)}
\left\|
D_J\widehat{\mathcal C}_p^+(s,R)
\right\|_{(\ell^\infty)^*}
\le
\frac{B_{\rm conn}^{\rm tube}}{\Delta_J^{\rm conn}}.
\tag{22}
\]

Under Note 0019's remaining common kernel/chart constants,
\((\mathrm H_\rho)\), and \(b_{k+1,s}\le b_*\), put

\[
C_*^{\rm conn}
=c_{\rm nn}\sqrt d\,Mb_*,
\qquad
C_{0,*}^{\rm conn}
=2d\,c_{\rm nn}Mb_*,
\tag{23}
\]

and choose

\[
a_*+\gamma C_*^{\rm conn}\le\kappa.
\tag{24}
\]

Then the Note-0019/0028 argument would turn (22) into the conditional
completed physical-\(J\) pullback

\[
\begin{aligned}
&\sup_p
\sup_{(U,J)\in\mathfrak K_p^{\rm phys}}
\sum_{s,R}e^{a_*d_{k+1,s}(R)}
\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(q_{p,s},y')}
\left|\mathcal L_{p,s,R}^{J,\rm conn}(j',y')\right|\\
&\quad\le
\frac{
C_\chi c_1(\alpha_\gamma)\overline E_J
e^{\gamma C_{0,*}^{\rm conn}}
B_{\rm conn}^{\rm tube}
}{
\Delta_J^{\rm conn}
}.
\end{aligned}
\tag{25}
\]

Equation (25) is a target implication, not an unconditional result of this
note. In particular, neither Note 0016's fixed-regulator compactness radii
nor Note 0027's nonempty common intersection supplies the uniform tube
bound (21).

**Subsequent closure.** [Note
0030](0030-completed-j-cauchy-tube.md) introduces the completed
representative compatibility hypothesis \((\mathrm H_J^{\rm conn})\),
strengthening Note 0017's local \((\mathrm H_J)\), and applies its margin at
the output scale. It reruns the marked and connected estimates in
coefficientwise local \(H^\infty\) norms. Under that hypothesis and Notes
0024--0027's retained
gas premises, it proves (20)--(21) with
\[
\Delta_J^{\rm conn}=\alpha _0-\bar\alpha _0,
\qquad
B_{\rm conn}^{\rm tube}=B_{\rm conn}.
\]
It also proves (22) and hence the conditional implication (25). The other
premises of (25), including \((\mathrm H_\rho)\), bounded mesh matching, and
common source-kernel/chart constants, remain open.

## Exact boundary

- Bałaban proves the unmarked locality (5) and the unmarked
  \((U,J)\)-analyticity on one chosen cubulation. The marked dual-number
  coefficient, shifted transport, literal-union connected support, and the
  aligned-cubulation anchor (13)--(17) are repository corollaries.
- The source support set consists of complete bond segments intersecting the
  geometric interior. It is neither full-bond containment in the interior
  nor endpoint ownership. Zero halo follows separately from the
  integer-wall cubical-complex lemma (16a).
- Absolute connected convergence is used only after each complete shifted
  gas is formed. No cross-shift gas or average-before-logarithm is
  introduced.
- The result closes the completed external-\(J\) support-anchor premise. It
  does not close \((\mathrm H_\rho)\), bounded mesh matching, common
  source-kernel/chart constants, or by itself the tube hypothesis
  (20)--(21). Subsequent Note 0030 closes that tube hypothesis under
  \((\mathrm H_J^{\rm conn})\).
- External-\(U\) restriction locality does not overcome the raw-\(U\) collar
  obstruction in Note 0018 and does not construct an RG-scaled nonlinear
  \(U\) pullback.
- No nonzero-source polymer-activity disk, intrinsic/raw comparison,
  large-field estimate, RG iteration, continuum or infinite-volume
  construction, Osterwalder--Schrader theorem, infrared decay, or
  Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Retain only first-stage locality and silently apply it after conditioning,
  weakening, and connectedization without the coefficientwise
  dual-number argument (7)--(8).
- Treat the intermediate \(Z_0\) completion as the final support. The final
  support theorem begins only after Eq. (2.10) and uses the literal union in
  Eq. (2.13).
- Replace the literal union by a rectangular, convex, or filled hull and
  change the dependency set.
- Delete repeated labels from (9); they do not enlarge support, but they are
  required for the logarithmic coefficient.
- Let an Ursell or normalization coefficient depend on \(J\) and create an
  extra derivative term. Both are fixed combinatorial scalars.
- Replace the source convention
  \(|b|\cap\operatorname {int}R\ne\varnothing\) by the stronger unsupported
  claim \(|b|\subset\operatorname {int}R\).
- Drop integer-wall alignment in (16a). A non-grid-aligned cubulation would
  require a positive endpoint halo.
- Infer (21) from a base-point bound or from the mere nonemptiness of
  \(\mathfrak D_p^\cap\).
- Use a coordinatewise Cauchy estimate and sum over bonds, manufacturing a
  volume factor; the required hypothesis is a full
  \(\ell^\infty\)-ball and its dual operator norm.
- Claim that (19) proves \((\mathrm H_\rho)\), a bounded mesh ratio, common
  chart constants, the nonlinear \(U\) pullback, or any continuum or
  mass-gap conclusion.
