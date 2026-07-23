# Note 0025: source-faithful conditioned routing of one localized mark

Claim ID: YM-RG-025

Kind: primary-source correction and fixed-term marked domination lemma

Evidence: E2 (finite-dimensional source-routing corollary; internally
checked)

Novelty: none claimed

Primary anchor: T. Balaban, [*Renormalization Group Approach to Lattice Gauge
Field Theories. II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), Eqs. (2.3), (2.5), (2.6),
(2.8), and (2.14). The immutable-page transcription and hash are recorded in
the [conditioned-routing
audit](../../literature/audits/2026-07-23-balaban-conditioned-mark-routing.md).

## Scope and correction

Work at one finite regulator, one fixed RG-II partition, one admitted
external \((U,J)\) background, and one localized interior plaquette mark
from Note 0012. For a fixed first-stage support \(A\), Mayer subfamily \(D\),
exterior-bond subset \(P\), conditioning domain \(Z_0\), and second-stage
output \(Z\), use the marked seed

\[
Y_0^\bullet
=
A\cup\bigcup_{Y\in D}Y.
\tag{1}
\]

Earlier versions of Notes 0021--0022 described the conditioned mark
schematically as

\[
W_{k,p}\bigl(A,\mathfrak B_{Z_0}(\sigma;B,X)\bigr).
\tag{2}
\]

That is not Balaban's variable routing. Equations (2.5)--(2.6) leave every
localized factor as \(F(Z_0,B)\), where \(B\) is the conditional interior
field. They standardize only the exterior variable
\(B'=(C^{(k)})^{1/2}X\). Equation (2.8) then inserts its second-stage
weakening variables only into the covariance and global operator sector.
The correction is material because the false map (2) manufactured an
unbounded-\(X\) marked-domain problem which the actual source representation
does not have.

The source is unmarked. Every statement below about \(W_{k,p}\) is a
repository corollary obtained by inserting Note 0012's already localized
factor into Balaban's finite formula. No marked theorem is attributed to the
paper.

## Exact source routing

Let \(F(Z_0,B)\) be any localized factor supported in \(Z_0\). The last line
of RG II Eq. (2.5) has the nested form

\[
\begin{aligned}
&\int d\mu_{C^{(k)}}(B')\,
\exp\!\left[
-\frac12
\left\langle
Z_0^cB',
C^*\Delta_kC\,C^{(k)}(Z_0)\,
C^*\Delta_kCZ_0^cB'
\right\rangle
\right]
\left[
\int d\mu_{C^{(k)}(Z_0)}(B)\,
\exp\!\left[
-\left\langle
Z_0^cB',C^*\Delta_kCZ_0B
\right\rangle
\right]
F(Z_0,B)
\right].
\end{aligned}
\tag{3}
\]

After \(B'=(C^{(k)})^{1/2}X\), Eq. (2.6) changes the density in (3), not the
argument of \(F\):

\[
\int d\mu_{C^{(k)}(Z_0)}(B)\,
\exp\!\left[
-\left\langle
B,C^*\Delta_kCZ_0^c(C^{(k)})^{1/2}X
\right\rangle
\right]
F(Z_0,B).
\tag{4}
\]

Equation (2.8) weakens exactly

\[
C^{(k)}(Z_0,s(Z)),\qquad
(C^{(k)})^{1/2}(s(Z)),\qquad
\Delta_k(s(Z)).
\tag{5}
\]

The complete Eq. (2.14) integrand therefore has the dependency pattern

\[
\begin{aligned}
\mathcal I_\gamma^{(0)}
(\sigma,\tau;B,X)
={}&
\mathcal G_\gamma(\sigma;B,X)
(-1)^{|P|}
\chi_{k,Y_0}(B)\chi^c_{k,P}(B)
\\
&\times
\exp\!\left[
\sum_{Y\in D}\tau(Y)V_k(Y,B)
\right],
\end{aligned}
\tag{6}
\]

where all \(\sigma\)-dependence is in the complex Gaussian/operator factor
\(\mathcal G_\gamma\). In particular,

\[
\partial_{\sigma(\Delta)}
\chi_{k,Y_0}(B)
=
\partial_{\sigma(\Delta)}
\chi^c_{k,P}(B)
=
\partial_{\sigma(\Delta)}
V_k(Y,B)
=0
\tag{7}
\]

in the source representation. These derivatives express parameter
independence; no derivative of a characteristic function with respect to
\(B\) is being taken.

## The seed cutoff controls the mark

For the independent fluctuation bonds \(I_k\), the global cutoff is

\[
\chi_k(B)
=
\prod_{b\in I_k}
\mathbf 1\{g_k\|B(b)\|<\varepsilon _1\}.
\tag{8}
\]

Equation (2.3) factors this product as
\(\chi_{k,Y_0}\chi_{k,Y_0^c}\) before applying exterior
inclusion--exclusion. Rerun that identity with (1). For a function of the
independent coordinates, let \(\operatorname{Dep}_B\) denote the set of
independent bonds on whose \(B\)-coordinates it depends, and put

\[
I_k(A):=\{b\in I_k:b\subset\operatorname{int}A\},
\qquad
\|B\|_A:=\max_{b\in I_k(A)}\|B(b)\|,
\]

with the maximum over the empty set equal to zero. The precise
independent-coordinate form of Note 0012's fixed-partition locality is

\[
\operatorname{Dep}_B W_{k,p}(A)
\subset I_k(A).
\tag{9}
\]

Since \(A\subset Y_0^\bullet\subset Z_0\), (8)--(9) imply

\[
\boxed{
\chi_{k,Y_0^\bullet}(B)\ne0
\quad\Longrightarrow\quad
g_k\|B\|_A<\varepsilon _1.
}
\tag{10}
\]

Define the fixed-input norm

\[
b_{p,A}
:=
\sup_{\mathrm{Eq.\ (1.34)}|_A}
|W_{k,p}(A;U,J,B)|.
\tag{11}
\]

The external background is restricted to the common domain already used by
Notes 0012 and 0013. For the full real \(B\)-integral, fix the measurable
extension

\[
\widetilde W_{k,p}(A;U,J,B)
:=
\begin{cases}
W_{k,p}(A;U,J,B),
&B|_{I_k(A)}\text{ lies in the strict local Eq.\ (1.34) domain},\\
0,&\text{otherwise}.
\end{cases}
\]

The fixed-cutoff cube is contained in that local domain by the source
containment estimate audited with RG II Eqs. (1.20) and (1.34), so this
extension agrees with \(W_{k,p}\) wherever
\(\chi_{k,Y_0^\bullet}\ne0\). Assigning the threshold boundary the value zero
is harmless because it has Gaussian measure zero. No complex \(B\)-contour
is introduced in Section 2: \(B\) remains the real integration coordinate
while the covariance density and external background may be complex.
Equations (10)--(11) now give globally

\[
|\widetilde W_{k,p}(A;U,J,B)|\le b_{p,A}.
\tag{12}
\]

## Fixed-term conditioned-contour domination

Insert the distinguished factor after the first-stage localization:

\[
\mathcal I_\gamma^\bullet
(\sigma,\tau;B,X)
=
\widetilde W_{k,p}(A;U,J,B)\,
\mathcal I_\gamma^{(0)}
(\sigma,\tau;B,X),
\tag{13}
\]

with \(Y_0=Y_0^\bullet\) in every seed-derived object. The mark in (13) is
independent of \(X,\sigma,\tau\). It is not a factor multiplying a
precomputed activity with the old unmarked seed: \(P,Z_0,\widetilde Z'_0\),
the active weakening family, and the allowed output \(Z\) must all be
recomputed from (1).

After the RG II Eq. (2.15) absolute-density comparison, fix the positive
Gaussian base measure

\[
d\lambda_\gamma^\sigma(B,X)
:=
d\mu_I(X)\,
d\mu_{K_\gamma(\sigma)}(B),
\qquad
K_\gamma(\sigma)
:=
\left(
\operatorname{Re}
[C^{(k)}(Z_0,\sigma)^{-1}]
\right)^{-1}.
\]

In this convention the determinant quotient, cutoffs, absolute exponential
density, and every remaining ordinary factor all belong to
\(\mathcal I_\gamma^{(0)}\), not to \(d\lambda_\gamma^\sigma\).
Let \(\mathcal C_\gamma\) denote exactly the ordinary product contour for
\((\sigma,\tau)\) already assigned to the history \(\gamma\); no new path or
radius is introduced. Equations (12)--(13) prove, with

\[
q_\gamma^{(0)}
:=
\sup_{(\sigma,\tau)\in\mathcal C_\gamma}
\int
|\mathcal I_\gamma^{(0)}(\sigma,\tau;B,X)|
\,d\lambda_\gamma^\sigma(B,X),
\]

\[
\begin{aligned}
\sup_{(\sigma,\tau)\in\mathcal C_\gamma}
\int
|\mathcal I_\gamma^\bullet
(\sigma,\tau;B,X)|
\,d\lambda_\gamma^\sigma(B,X)
&\le
b_{p,A}
\sup_{(\sigma,\tau)\in\mathcal C_\gamma}
\int
|\mathcal I_\gamma^{(0)}
(\sigma,\tau;B,X)|
\,d\lambda_\gamma^\sigma(B,X)
\\
&\le
b_{p,A}q_\gamma^{(0)}
\end{aligned}
\tag{14}
\]

uniformly on the same admitted \(\sigma,\tau\) contours as the ordinary
term. Thus the marked joint weight in Note 0022 may be taken to be

\[
\boxed{
q_\gamma^\bullet=q_\gamma^{(0)},\qquad
C_\bullet=1,\qquad
\eta_{\rm mom}=0.
}
\tag{15}
\]

There is:

- no transformed marked argument;
- no relative Gaussian moment for the mark;
- no smaller second-stage marked radius;
- no derivative allocation in which a second-stage derivative hits the
  mark; and
- no extra determinant or covariance factor caused by the mark.

All Gaussian completion, complex-precision comparison, \(P\)-cutoff gain,
and potential estimates in RG II Eqs. (2.15)--(2.26) therefore apply to the
fixed marked term with the single multiplicative factor \(b_{p,A}\), after
the seed has been enlarged as in (1). This is a bound on one fixed
\(\gamma=(A,D,P,Z_0,Z,\ldots)\), not yet on its resummation.

## Finite-dimensional conditioning check

The variable routing in (3)--(4) can be checked in the smallest correlated
Gaussian. Let

\[
Q=
\begin{pmatrix}
a&c\\c&d
\end{pmatrix},
\qquad
a>0,\quad ad-c^2>0,
\tag{16}
\]

with the first coordinate inside and the second outside. The restricted
inside covariance is \(a^{-1}\), while the outside marginal variance is
\(a/(ad-c^2)\). Relative to these two normalized Gaussian measures, the
cross-density factor is

\[
\exp\!\left[-cxb-\frac{c^2x^2}{2a}\right].
\]

The inside Gaussian moment-generating factor is
\[
\mathbb E_{b\sim N(0,a^{-1})}e^{-cxb}
=
\exp\!\left[\frac{c^2x^2}{2a}\right],
\]
so it cancels the displayed exterior correction exactly. For the localized
mark \(F(b)=b^2\),
\[
\mathbb E_b\!\left[b^2e^{-cxb}\right]
=
\left(\frac1a+\frac{c^2x^2}{a^2}\right)
\exp\!\left[\frac{c^2x^2}{2a}\right].
\]
After the cancellation and the outside expectation, this gives

\[
\frac1a+
\frac{c^2}{a^2}\frac{a}{ad-c^2}
=
\frac d{ad-c^2}
=
(Q^{-1})_{11},
\tag{17}
\]

which is the original Gaussian moment. The exterior variable changes the
density through \(e^{-cxb}\); it never changes the written argument
\(F(b)\). The exact-arithmetic regression test accompanying this note checks
the two cancelling quadratic coefficients, (17), the first and zeroth
moments, and the pointwise domination (14).

## The wrong-map obstruction, retained only as a falsifier

Suppose one were instead to evaluate a locally defined mark on

\[
P_Ab+P_AT_\sigma X.
\tag{18}
\]

For a bounded marked domain and a nondegenerate Gaussian \(X\), containment
for every \(X\) is possible only if

\[
P_AT_\sigma=0
\quad\text{and}\quad
P_Ab\ \text{lies in the marked domain}.
\tag{19}
\]

If \(P_AT_\sigma\ne0\), an open Gaussian-positive tail leaves every bounded
domain. This explains why the earlier schematic (2) appeared obstructed.
The actual source representation satisfies the first condition in (19)
because \(X\) is exterior and the inserted mark sees the unshifted interior
\(B\).

The raw plaquette outer function is entire and has at most linear-exponential
growth in a link-algebra perturbation, so a uniformly bounded linear
Gaussian image could be integrable. That observation is unnecessary here
and would not repair the old proof by itself: the composite reconstruction
used to define \(W_{k,p}\) was proved only on its local analytic domain, and
entireness without a growth order does not imply Gaussian integrability.

## What remained at this checkpoint and the successor

Equation (15) closes the direct conditioned-contour gate in Notes 0021--0022
and sets the moment part of their loss ledger to zero. It does not sum over
the marked seeds. At this checkpoint, the next estimate began with a pinned
version of the
source's Eqs. (2.27)--(2.29): the input decay of \(b_{p,A}\) must be combined
with the ordinary \(D\)-weights to control

\[
A\cup\bigcup_{Y\in D}Y,
\tag{20}
\]

then propagated through the \(P,Z_0,\widetilde Z'_0,Z\) resummations and the
\(k\)-to-\(k+1\) tree-metric conversion. In the notation of Note 0022,

\[
r_{\rm mom}=0,
\tag{21}
\]

but a root/gluing or other geometric overhead may remain. The following were
therefore open at this checkpoint:

- positive marked-seed \(A\)-to-\(Z\) kernel decay after every resummation;
- the exact marked tree-gluing and scale-conversion inequalities;
- aggregation and multiplicity control for the final decorated marked
  species;
- the rooted final marked norm and differentiated absolute convergence on a
  regulator-uniform source disk;
- branchwise shifted synchronization and the physical \(U/J\) pullbacks;
- large fields, RG iteration, the continuum theory, axioms, infrared decay,
  and the Yang--Mills mass gap.

Subsequent [Note 0026](0026-marked-seed-resummation.md) closes the first
three bullets and the fixed-partition part of the fourth: it proves the
positive \(D/P/Z_0\) and scale resummations, controls the decorated
multiplicity by a doubled-amplitude susceptibility, and obtains the rooted
marked norm plus the absolutely convergent connected derivative at \(t=0\)
on one fixed gas. It does **not** construct the regulator-uniform common
source disk named in the fourth bullet. The last two bullets remain open.

## Exact boundary

- The immutable source pages prove the variable-routing statements only for
  Balaban's unmarked \(F(Z_0,B)\). The passage to \(W_{k,p}(A,B)\) uses the
  repository's already proved localization and the rerun marked seed (1).
- Equations (10), (14), and (15) are fixed-term consequences. They neither
  differentiate an unmarked inequality nor infer a marked final activity
  from RG II Lemma 3.
- Note 0026 is the separate successor that performs the positive marked
  resummation; that later result does not enlarge this claim's fixed-history
  scope.
- The complex covariance causes no problem in pulling out (12): Eq. (2.15)
  first takes the absolute density and compares it with a positive Gaussian,
  while (12) is pointwise on the cutoff support.
- The sharp cutoff is independent of the second-stage weakening parameters.
  Its nonsmoothness in \(B\) is irrelevant because no \(B\)-derivative or
  complex \(B\)-contour is taken.
- No assertion here constructs a continuum Yang--Mills theory or proves a
  mass gap.

## Falsification checklist

- Shift \(F(Z_0,B)\) by the exterior standardized variable in Eq. (2.6) and
  compare with the printed page.
- Omit \(A\) from \(Y_0^\bullet\); then \(\chi_{k,Y_0^\bullet}\) need not
  control the mark's fluctuation coordinates.
- Allow \(W_{k,p}(A)\) to depend on a bond outside \(A\); implication (10)
  fails unless the seed and cutoff are enlarged again.
- Insert a mark before completing the first-stage localization and silently
  let the second-stage weakening act on its global propagators.
- Pull \(b_{p,A}\) through a term with the old unmarked \(Y_0\), \(P\), or
  \(Z_0\); that is not the marked construction.
- Replace
  \((\operatorname{Re}[C^{-1}])^{-1}\) by
  \((\operatorname{Re}C)^{-1}\) in the positive Gaussian comparison.
- Promote (14) to a summed marked Lemma-3 bound without proving the
  marked-seed resummation and scale conversion.
