# Note 0030: a completed affine-\(J\) tube and Banach cluster norm

Claim ID: YM-RG-030

Kind: conditional finite-regulator analytic and connected-norm lemma

Evidence: E2 (primary-source domain audit plus a finite-dimensional
Banach-algebra rerun under the explicitly strengthened
strict-representative and marked-gas hypotheses; internally checked)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I*](https://doi.org/10.1007/BF01215223), especially Eqs.
  (1.10)--(1.18) on printed pp. 262--263;
- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories II. Cluster Expansions*](https://doi.org/10.1007/BF01239022),
  especially Eq. (1.34), Lemma 2, the analyticity discussion on printed
  p. 15, and Lemma 3 Eq. (2.38).

## Scope

Retain the complete finite-regulator construction and hypotheses of Notes
0017 and 0021--0029. In particular:

1. the fixed-\(M\) strict representative hypothesis
   \((\mathrm H_J)\) holds with
   \[
   0<\bar\alpha _0<\alpha _0;
   \tag{1}
   \]
2. all source hierarchy, doubled-\(\varepsilon _2\), ordinary KP, marked
   resummation, periodic divisibility, and common-branch premises of Notes
   0024--0027 hold;
3. every branch uses the raw affine independent-\(J\) coordinate; and
4. \(\mathfrak K_p^{J,\mathrm{phys}}\) is the retained family of physical
   centres satisfying the completed representative compatibility hypothesis
   below.

**Completed strict-\(J\) representative compatibility
\((\mathrm H_J^{\rm conn})\).** For each retained physical centre and each
complete shifted branch, there is one representative whose restrictions are
the representatives used in every overlapping input, intermediate, final,
and output activity chart on that branch. In these compatible
representatives the raw affine \(J\) coordinate has
\(\lVert J\rVert_\infty\le\bar\alpha _0\), and shifted transport is an
\(\ell^\infty\)-isometric bond permutation.

This is a strengthening of the local quantifiers in Note 0017's
\((\mathrm H_J)\), not a new source theorem. RG I does not print a
simultaneously compatible transported representative atlas. Without
\((\mathrm H_J^{\rm conn})\), unrelated complex gauge representatives can
act nonisometrically on the raw \(J\) coordinate, and separate local margins
do not define one common affine branch tube.

This note proves that, under \((\mathrm H_J^{\rm conn})\), the strict margin
survives all later RG-II operations and gives the strong
completed-coefficient norm required by Note 0029.

The perturbation below changes the **independent** complex variable \(J\)
while \(U\), the fluctuation variables, the cutoffs, and all weakening
parameters are fixed. The perturbed pair need not itself lie on the physical
submanifold \(J=\mathscr J_\xi(U)\); that transverse complex line is the
Cauchy device used to differentiate at a physical centre.

## The source domains have one affine \(J\) ceiling

RG I defines

\[
\mathcal U_j^c(X,\alpha _0,\alpha _1,\gamma _0)
\tag{2}
\]

as a union of complex gauge orbits represented by pairs satisfying four
conditions. On printed p. 262:

- conditions (i) and (ii) involve only \(U\);
- condition (iii), Eq. (1.14), contains the direct bound
  \[
  \lVert J\rVert_{\infty,X}<\gamma _0;
  \tag{3}
  \]
- condition (iv), Eqs. (1.15)--(1.16), tests
  \((U_n(M^j(U)),J_n(M^j(U)))\), where \(J_n\) is computed from \(U\) by
  Eq. (1.8), not from the independent variable \(J\).

Printed p. 263 then exhibits smaller constants and explains that sufficiently
regular physical configurations lie strictly inside the base domain. This is
the source mechanism isolated, without a numerical overclaim, as
\((\mathrm H_J)\) in Note 0017.

RG II uses the same separation. Its Eq. (1.34) outer potential domain is

\[
\mathcal U_{k+1}^c
\bigl(Y,(1+\beta)\alpha _0,(1+\beta)\alpha _1,\alpha _0\bigr).
\tag{4}
\]

Lemma 2 makes every localized potential analytic on (4). The printed p. 15
discussion then says:

1. the potentials are also analytic on the restricted output space
   \(\mathcal U_{k+1}^c(X,\alpha _0,\alpha _1)\);
2. the quadratic forms and covariances are analytic for pairs satisfying
   RG-I conditions (i)--(iii) on their local \(Z\), with constants much
   larger than \(\alpha _0,\alpha _1\); and
3. the final activities \(H(Z)\) and the connected sum are analytic on the
   output space.

RG I printed p. 263 explicitly says that the third parameter is omitted from
the notation when \(\gamma _0=\alpha _0\). Thus the two-parameter output
space in this paragraph retains the same direct bound
\(\lVert J\rVert_\infty<\alpha _0\); it does not discard condition (iii).

Thus no later external-field domain printed in this chain imposes a smaller
direct independent-\(J\) ceiling than (3) with
\(\gamma _0=\alpha _0\).

## Restriction-stable completed tubes

Put

\[
\boxed{\Delta_J^{\rm conn}:=\Delta_J
=\alpha _0-\bar\alpha _0>0.}
\tag{5}
\]

For a complete shifted branch \(s\), final connected support \(R\), and
physical centre
\((U,J)\in\mathfrak K_p^{J,\mathrm{phys}}\) satisfying
\((\mathrm H_J^{\rm conn})\), define

\[
\mathbb T_{p,s,R}(U,J)
=
\left\{
(U,J+w):
\operatorname {supp}w\subset\mathsf E_s^{\rm loc}(R),\
\lVert w\rVert_{\ell^\infty}<\Delta_J
\right\},
\tag{6}
\]

where \(\mathsf E_s^{\rm loc}(R)\) is Note 0029's complete-bond
intersection support.

Every restriction map in the construction is a contraction:

\[
\lVert w|_C\rVert_{\infty,C}
\le\lVert w\rVert_{\infty,R}
<\Delta_J
\tag{7}
\]

for \(C\subset R\). Hence, on every local domain,

\[
\lVert J+w\rVert_\infty
<
\bar\alpha _0+\Delta_J
=\alpha _0.
\tag{8}
\]

Conditions (i), (ii), and (iv) are unchanged, so the same representative
proves membership in (4) and in every restricted output domain. The
quadratic-form and covariance domains are no smaller. Shift transport is a
permutation of bond coordinates and is therefore isometric in
\(\ell^\infty\).

For a connected occurrence tuple with literal union \(R\), each final
support \(C_i\) is a subset of \(R\), and every internal
\(D,P,Z_0\) history contributing to \(H_s(C_i)\) or
\(W_{p,s}^{\rm post}(C_i)\) is localized inside \(C_i\). Note 0029 proves
that the completed coefficient has no external-coordinate dependence outside
\(\mathsf E_s^{\rm loc}(R)\). Consequently,

\[
\boxed{
\mathbb T_{p,s,R}(U,J)
\text{ lies in the complete branch coefficient domain.}
}
\tag{9}
\]

This conclusion is stronger than nonemptiness of the branch intersection and
does not come from finite-regulator compactness. It uses the quantitative
strict margin and simultaneous representatives in
\((\mathrm H_J^{\rm conn})\), the raw affine \(J\) coordinate, and
restriction contraction.

## The connected estimate must be rerun in \(H^\infty\)

Note 0027 Eq. (25), read only as a pointwise estimate, does **not** justify
interchanging the support sum with separate suprema over (6). We therefore
rerun the already proved positive majorants in a Banach algebra.

For each fixed \((p,s,R,U,J)\), let

\[
\mathscr A_{p,s,R}
=H^\infty\bigl(\mathbb T_{p,s,R}(U,J)\bigr),
\qquad
\lVert F\rVert_{p,s,R}
=
\sup_{\substack{\operatorname {supp}w\subset
\mathsf E_s^{\rm loc}(R)\\
\lVert w\rVert_\infty<\Delta_J}}
|F(U,J+w)|.
\tag{10}
\]

This is a commutative Banach algebra under pointwise products. Its norm
obeys

\[
\lVert F+G\rVert\le\lVert F\rVert+\lVert G\rVert,
\qquad
\lVert FG\rVert\le\lVert F\rVert\lVert G\rVert.
\tag{11}
\]

The two analytic inputs are already uniform on their full source domains:

1. Note 0013 defines
   \[
   b_{p,A}
   =
   \sup_{\mathrm{Eq.\ (1.34)}|_A}|W_{k,p}(A)|,
   \tag{12}
   \]
   so (9) gives
   \(\lVert W_{k,p}^s(A)\rVert_{p,s,R}\le b_{p,A}\) whenever
   \(A\subset R\).
2. RG II Lemma 3 is uniform on the fixed-output analytic domain. Note 0024
   makes its supremum norm explicit:
   \[
   \lVert H_s(C)\rVert_{p,s,R}
   \le
   C_3\varepsilon _1
   \exp\!\left[
   -(1-8\delta)\frac L2\kappa d_{k+1,s}(C)
   \right].
   \tag{13}
   \]

Every step of Notes 0025--0026 after those inputs uses only finite sums,
products, absolute positive kernels, restriction, integration bounded by the
same positive envelope, and the triangle inequality. Equations (11)--(13)
therefore reproduce the coloured \(D\)-family bound, the \(P,Y_0,Z_0\)
resummation, the doubled-amplitude scale susceptibility, the final marked
norm, and the pinned cluster estimate with absolute values replaced by the
norm (10). No derivative is taken during this rerun.

More explicitly, if a connected occurrence tuple has literal union
\(C_0\cup\cdots\cup C_n=R\), restriction of a point of
\(\mathbb T_{p,s,R}\) to \(C_i\) is a point of
\(\mathbb T_{p,s,C_i}\). Therefore

\[
\sup_{\mathbb T_{p,s,R}}
\left|
W_{p,s}^{\rm post}(C_0)\prod_{i=1}^nH_s(C_i)
\right|
\le
\left\|W_{p,s}^{\rm post}(C_0)\right\|_{p,s,C_0}
\prod_{i=1}^n\left\|H_s(C_i)\right\|_{p,s,C_i}.
\tag{13a}
\]

Apply (13a) before the \(R\)-sum. Literal-union grouping partitions the same
positive Ursell majorant used in Notes 0020 and 0023, so no supremum is moved
through a support sum.

In particular, Note 0026 Eq. (41) becomes, branchwise,

\[
\sup_p\sup_s
\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\lVert\mathcal C_{p,s}^{+}(R)\rVert_{p,s,R}
\le B_{\rm conn},
\tag{14}
\]

where

\[
B_{\rm conn}
=e^{16\alpha}
C_{\rm sec}C_{\rm an}^{\rm geom}(\Delta)\mathcal B_d,
\qquad
C_{\rm sec}=4K_{\rm lift}\alpha _6^{-1}.
\tag{15}
\]

The proof of (14) is coefficientwise in \(R\), so its use of a different
local algebra for each \(R\) is harmless: every coefficient receives exactly
the same positive majorant as in Note 0026 before the final \(R\)-sum.

Finally perform Note 0027's post-connected normalization. There are
\(\widetilde n_p\) branches and each coefficient is divided by
\(\widetilde n_p\), so the branch count cancels exactly. We obtain the strong
tube norm

\[
\boxed{
\sup_p
\sup_{(U,J)\in\mathfrak K_p^{J,\mathrm{phys}}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\sup_{\substack{\operatorname {supp}w\subset
\mathsf E_s^{\rm loc}(R)\\
\lVert w\rVert_\infty<\Delta_J}}
\left|
\widehat{\mathcal C}_p^+(s,R;U,J+w)
\right|
\le B_{\rm conn}.
}
\tag{16}
\]

Thus Note 0029's requested constants can be chosen as

\[
\boxed{
\Delta_J^{\rm conn}=\alpha _0-\bar\alpha _0,
\qquad
B_{\rm conn}^{\rm tube}=B_{\rm conn}.
}
\tag{17}
\]

Equation (16) is not inferred from a supremum of a pointwise support sum. It
is the sum of the coefficientwise tube norms produced by the Banach-algebra
rerun.

## Banach-line Cauchy and the full dual norm

Fix one coefficient and let \(v\) be supported in
\(\mathsf E_s^{\rm loc}(R)\) with
\(\lVert v\rVert_\infty\le1\). For every \(0<r<\Delta_J\), the map

\[
z\longmapsto
\widehat{\mathcal C}_p^+(s,R;U,J+zv)
\tag{18}
\]

is holomorphic on \(|z|<\Delta_J\). The one-variable Cauchy formula gives

\[
\left|
D_J\widehat{\mathcal C}_p^+(s,R)[v]
\right|
\le
\frac1r
\sup_{\lVert w\rVert_\infty<\Delta_J}
\left|
\widehat{\mathcal C}_p^+(s,R;U,J+w)
\right|.
\tag{19}
\]

Let \(r\uparrow\Delta_J\). Note 0029's exact locality says the derivative
vanishes on coordinates outside \(\mathsf E_s^{\rm loc}(R)\). Restricting an
arbitrary global unit vector to that set does not increase its
\(\ell^\infty\) norm, so the support-restricted and full global dual norms
coincide. Summing (19) and using (16) yields

\[
\boxed{
\sup_p
\sup_{(U,J)\in\mathfrak K_p^{J,\mathrm{phys}}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\left\|
D_J\widehat{\mathcal C}_p^+(s,R)
\right\|_{(\ell^\infty)^*}
\le
\frac{B_{\rm conn}}{\Delta_J}.
}
\tag{20}
\]

There is no sum over bonds in this argument and hence no support-volume
factor.

## Conditional completed physical-\(J\) summand

Retain Note 0029's remaining hypotheses: Note 0019's
\((\mathrm H_\rho)\), common source-kernel and chart constants, an output
mesh bound \(b_{k+1,s}\le b_*\), and

\[
C_*^{\rm conn}=c_{\rm nn}\sqrt d\,Mb_*,
\qquad
C_{0,*}^{\rm conn}=2d\,c_{\rm nn}Mb_*,
\qquad
a_*+\gamma C_*^{\rm conn}\le\kappa.
\tag{21}
\]

Combining (20) with Notes 0019, 0028, and 0029 now proves the conditional
completed physical-\(J\) chain-rule summand

\[
\boxed{
\begin{aligned}
&\sup_p
\sup_{(U,J)\in\mathfrak K_p^{J,\mathrm{phys}}}
\sum_{s,R}e^{a_*d_{k+1,s}(R)}
\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(q_{p,s},y')}
\left|\mathcal L_{p,s,R}^{J,\rm conn}(j',y')\right|\\
&\quad\le
\frac{
C_\chi c_1(\alpha_\gamma)\overline E_J
e^{\gamma C_{0,*}^{\rm conn}}
B_{\rm conn}
}{
\alpha _0-\bar\alpha _0
}.
\end{aligned}
}
\tag{22}
\]

Equation (22) closes the completed-coefficient Cauchy premise, not the other
premises printed in its first sentence.

## Exact boundary

- The source proves the unmarked analytic domains and uniform unmarked
  activity bound. The completed marked \(H^\infty\)-norm rerun, shifted
  normalization, and derivative statement are repository corollaries.
- The result is conditional on \((\mathrm H_J^{\rm conn})\), which
  strengthens Note 0017's local \((\mathrm H_J)\) quantifiers by requiring
  simultaneous compatible representatives. RG I motivates the strict margin
  by its smaller-domain construction, but does not print a numerical
  \(\bar\alpha _0\) or a common transported representative atlas.
- The full ball in (6) is in the independent affine \(J\) coordinate. It is
  not a nonzero plaquette-source disk and does not keep
  \(J=\mathscr J_\xi(U)\) away from the centre.
- Equation (16) is a coefficientwise tube-norm theorem. A pointwise reading
  of Note 0027 Eq. (25) alone would not imply it.
- Equation (22) remains conditional on \((\mathrm H_\rho)\), bounded mesh
  matching, and common kernel/chart constants. Those premises are not
  consequences of the affine tube.
- External-\(U\) locality still supplies no RG-scaled nonlinear \(U\) collar.
  Note 0018's raw-\(U\) obstruction remains in force.
- No intrinsic/unrestricted raw-law comparison, nonzero-source polymer gas,
  large-field estimate, RG iteration, continuum or infinite-volume
  construction, Osterwalder--Schrader reconstruction, infrared decay, or
  Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Let the independent perturbation \(w\) enter RG-I condition (iv), even
  though its \(J_n(M^j(U))\) is derived from \(U\), and manufacture a false
  smaller radius.
- Use only the visible \((1+\beta)\) enlargement in (4) as a \(J\) margin;
  the third parameter is not enlarged.
- Choose physical and activity-chart representatives inconsistently and
  bypass \((\mathrm H_J^{\rm conn})\); complex gauge changes need not be
  isometric in the raw \(\ell^\infty\) coordinate.
- Infer (16) by moving a support-dependent supremum through Note 0027's
  pointwise sum instead of rerunning the positive estimates in (10).
- Bound derivatives coordinate by coordinate and sum over bonds, producing
  an artificial volume factor.
- Forget Note 0029 locality and identify the support-restricted dual norm
  with the global dual norm without proving vanishing outside \(R\).
- Treat the transverse independent-\(J\) ball as a disk of physical pairs or
  as a nonzero plaquette-source polymer expansion.
- Drop \((\mathrm H_\rho)\), the mesh bound, or common kernel/chart constants
  from (22).
- Promote this conditional small-field first-jet summand to a nonlinear
  \(U\) theorem, unrestricted RG transformation, continuum construction, or
  mass-gap claim.
