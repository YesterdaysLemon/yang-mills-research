# Note 0012: rooted cube-count localization of one plaquette mark

Claim ID: YM-RG-012

Kind: finite-regulator marked-decoupling corollary

Evidence: E2 (finite-regulator auxiliary lemma; internally checked)

Novelty: none claimed

## Exact scope

Work at one finite regulator and one RG step in the independent
\((U,J,B)\) variables used by RG II. Retain the complete small-field and
analytic hypotheses of RG II Eqs. (1.11)--(1.21), and use exactly the local
complex domain in Eq. (1.34). In particular,

\[
B'=g_kCB-h\widetilde D(g_kCB),
\tag{1}
\]

and RG II Eq. (1.21) gives, for all weakening variables satisfying
\(|s(\Delta)|\le R=e^{\kappa _1}\),

\[
\lVert H_k(s,B')\rVert
\le 4B_0C_1e^{16\kappa _1}g_k\lVert B\rVert
<4B_0C_1e^{16\kappa _1}\varepsilon _1
\tag{2}
\]

in each of the admissible propagator norms. The printed smallness condition
on \(e^{32\kappa _1}\varepsilon _1\) is retained.

Fix one RG-II localization partition and one plaquette \(p\) lying strictly
inside a root localization cube \(Q_p\). Full covariance under symmetries that
move this partition is not assumed. Let \(\Sigma_p\) be the finite set of
localization cubes outside \(Q_p\) at the fixed regulator.

Write \(\mathcal P_{\rm int}(\mathcal Q)\) for the plaquettes that lie strictly
inside some cube of this fixed partition. Every supremum and profile corollary
below is restricted to this set. Plaquettes crossing cube boundaries require a
finite family of shifted partitions or the partition of unity used around RG
II Eq. (1.37); that extension is not made here.

## The decoupled mark

RG I pp. 265--266 gives the exact relative-field crosswalk after its printed
gauge transformations. For an oriented fine bond \(b\), set

\[
X_b(U,A)=e^{i\eta_{\rm lat}A_b}U_b,
\qquad
X_{\bar b}(U,A)=X_b(U,A)^{-1}
=U_b^{-1}e^{-i\eta_{\rm lat}A_b}.
\]

The gauge-transformed reconstructed field is \(X(U,H_k(B'))\). The omitted
outer gauge factors cancel from a plaquette trace. Define the local holomorphic
outer function

\[
\Phi_p(U,A)=4\left(1-\frac12\operatorname{Tr}X_p(U,A)\right),
\tag{3}
\]

and set

\[
F_p(s;U,J,B)=
\Phi_p(U,H_k(s,B'(B)))-\Phi_p(U,H_k(s,B'(0))).
\tag{4}
\]

Equation (1), RG II Eq. (1.17), and the fixed-point normalization at the
origin give \(B'(0)=0\) and \(H_k(s,0)=0\). Thus (4) is
\(\Phi_p(U,H_k(s,B'(B)))-\Phi_p(U,0)\), and
\(F_p(\mathbf 1)=\Delta_p(U,J,B)\), the single-plaquette version of Note
0011's background-centered mark at the entrance to RG II Lemma 2. Therefore

\[
F_p(s;U,J,0)=0
\tag{5}
\]

for every admitted \(s\). This centering removes only the constant term. A
linear term in \(B\) generally remains; the quadratic/cubic cancellation used
for the source-free Wilson remainder in RG II Eqs. (1.39)--(1.40) is not used
here.

RG II Eq. (1.1) inserts an additional local multiplier
\((t\zeta_\Pi+t_\Pi\zeta_D)\) for one of its source-free terms. That multiplier
is not silently identified with this mark. Here the localized analytic outer
function is \(\Phi_p\), and the only nonlocal input being weakened is the
direct RG-I reconstruction \(H_k\). This is precisely the general
\(E(X,U,J,A)\) pattern described immediately before RG II Eq. (1.1); applying
Eqs. (1.9)--(1.10) to this new outer function is the repository corollary.

## Exact mixed-difference decomposition

For \(a\in\{0,1\}\), let \(E_\Delta^a\) replace \(s(\Delta)\) by \(a\).
For \(A\subset\Sigma_p\), put

\[
W_{k,p}(A)=
\left[
\prod_{\Delta\in A}(E_\Delta^1-E_\Delta^0)
\prod_{\Delta\in\Sigma_p\setminus A}E_\Delta^0
\right]F_p.
\tag{6}
\]

Expanding \(E_\Delta^1=E_\Delta^0+(E_\Delta^1-E_\Delta^0)\) over the finite
set \(\Sigma_p\) gives the exact identity

\[
\Delta_p(U,J,B)=\sum_{A\subset\Sigma_p}W_{k,p}(A;U,J,B).
\tag{7}
\]

The decoupled propagators are block diagonal between distinct active
components. The same component argument used after RG II Eqs. (1.9)--(1.10)
therefore shows that (6) vanishes if \(A\) contains a component disconnected
from \(Q_p\). Write \(Y(A)=Q_p\cup A\) for the remaining root-connected
support and relabel (7) as

\[
\boxed{
\Delta_p(U,J,B)=
\sum_{Y\supset Q_p}W_{k,p}(Y;U,J,B).
}
\tag{8}
\]

Every term in (8) depends only on \((U,J,B)\) in the interior of \(Y\), in
the precise RG-II decoupled-variable sense. It is holomorphic on the
restriction of Eq. (1.34) to \(Y\), is invariant under the simultaneous
background gauge action, and vanishes at \(B=0\). These statements follow
term by term because the weakening, mixed-difference, and Cauchy operations
commute with the covariant decoupled reconstruction.

## A linear holomorphic mark bound

For \(m=|A|\), define \(s_A(\zeta)\) to equal \(\zeta_\Delta\) on \(A\)
and zero on \(\Sigma_p\setminus A\). Repeated one-variable Cauchy formulas on
\(|\zeta_\Delta|=R\) give

\[
W_{k,p}(A)=
\frac{1}{(2\pi i)^m}
\oint
F_p(s_A(\zeta);U,J,B)
\prod_{\Delta\in A}
\frac{d\zeta_\Delta}
{\zeta_\Delta(\zeta_\Delta-1)}.
\tag{9}
\]

For \(A=\varnothing\), (9) means the fully decoupled value
\(F_p(0;U,J,B)\). Hence

\[
|W_{k,p}(A)|
\le M_{p,Y}(B)(R-1)^{-m},
\qquad
M_{p,Y}(B)=
\sup_{|\zeta_\Delta|\le R,\ \Delta\in A}
|F_p(s_A(\zeta);U,J,B)|.
\tag{10}
\]

The needed bound on \(M_{p,Y}\) is elementary but is recorded explicitly.
On the strict Eq. (1.34) domain, the four background link factors in (3) and their
oriented inverses occurring in one plaquette have a uniform matrix-norm bound
\(K\). Fix a norm-comparison constant \(c_{\rm emb}\) such that the defining
\(2\times2\) operator norm of a Lie-algebra element is at most
\(c_{\rm emb}\) times the RG-II field norm. For a matrix perturbation,

\[
\lVert e^X-I\rVert\le e^{\lVert X\rVert}\lVert X\rVert.
\tag{11}
\]

Put

\[
h=\lVert H_k(s,B')\rVert_{\infty,p},
\qquad
h_*=4B_0C_1e^{16\kappa _1}\varepsilon _1.
\]

Telescope the product of the four perturbed link factors in (3), interpolate
from zero to \(H_k(s,B')\), and use
\(|\operatorname{Tr}A|\le2\lVert A\rVert\). This gives the explicit estimate

\[
|F_p(s;U,J,B)|
\le
16\eta_{\rm lat}c_{\rm emb}K^4
e^{4\eta_{\rm lat}c_{\rm emb}h_*}h.
\tag{12}
\]

The fixed smallness conditions keep the interpolation segment in the same
domain and include \(h_*\le\alpha _2/2\). Since the rescaled lattice spacing
satisfies \(0<\eta_{\rm lat}\le1\), applying (2) to (12) gives the
scale-independent constant

\[
C_{\rm mark}=
64c_{\rm emb}K^4B_0C_1e^{2c_{\rm emb}\alpha _2},
\tag{13}
\]

depending only on the fixed RG technical parameters, norm convention, and
strict Eq. (1.34) domain, but not on the volume, scale, root, or source
location, such that

\[
M_{p,Y}(B)
\le C_{\rm mark}e^{16\kappa _1}g_k\lVert B\rVert_Y
\le C_{\rm mark}e^{16\kappa _1}\varepsilon _1.
\tag{14}
\]

Combining (10) and (14),

\[
|W_{k,p}(Y;U,J,B)|
\le
C_{\rm mark}e^{16\kappa _1}g_k\lVert B\rVert_Y
(e^{\kappa _1}-1)^{-m(Y)},
\tag{15}
\]

where \(m(Y)\) is the number of localization cubes in \(Y\setminus Q_p\).
No second- or third-order smallness is asserted.

## An interior-location-uniform cube-count norm

Let \(D_0\) be the maximum degree of the localization-cube adjacency graph;
it depends only on the fixed dimension and localization convention. The
number \(N_m(Q_p)\) of root-connected supports with \(m\) added cubes obeys

\[
N_m(Q_p)\le D_0^{2m}.
\tag{16}
\]

Indeed, fix an ordering of incident edges, choose the resulting canonical
spanning tree of each support, and encode it by its depth-first walk from the
root. The walk has length at most \(2m\), determines the visited support, and
has at most \(D_0^{2m}\) possible edge sequences.

Choose \(\lambda>0\) subject to the explicit margin

\[
q=\frac{D_0^2e^\lambda}{e^{\kappa _1}-1}<1.
\tag{17}
\]

This is an additional transparent parameter condition, not an unstated
consequence of RG II's \(d_k\)-norm estimates. Equations (15)--(17) give

\[
\boxed{
\sup_{p\in\mathcal P_{\rm int}(\mathcal Q)}
\sum_{Y\supset Q_p}
e^{\lambda m(Y)}
\sup_{\mathrm{Eq.\ (1.34)}}|W_{k,p}(Y)|
\le
\frac{C_{\rm mark}e^{16\kappa _1}\varepsilon _1}{1-q}.
}
\tag{18}
\]

The constant is independent of the finite volume, RG scale, and admissible
interior plaquette location. For a finite real or complex profile supported in
\(\mathcal P_{\rm int}(\mathcal Q)\), linearity and the triangle inequality
give the corresponding safe profile estimate proportional to
\(\sum_p|f_p|\). No statement is made for a profile meeting boundary-crossing
plaquettes, and no conversion to Program 002's still-untranscribed discrete
\(C^6\) norm is made.

## Interface with the exact RG-coordinate law

At the fixed background of Notes 0010--0011, substitute the selected
independent RG-II variables into (8) before performing the Section 2
integrals. This supplies a rooted decomposition of the unique mark appearing
in Note 0011 Eq. (10). It does not yet supply the expectation of that mark:
the marked seed

\[
Y_0^\bullet=Y(A)\cup\bigcup_{X\in D}X
\tag{19}
\]

must still be carried through the cutoff expansion, Gaussian conditioning,
covariance weakening, component factorization, and connected graph sum in RG
II Eqs. (2.2)--(2.13).

Locality in independent \((U,J,B)\) variables also does not become locality in
the coarse field \(W\) after the nonlocal substitution
\(U=U_{k+1}(W)\). A separate quasilocal pullback theorem using the variational
paper's componentwise Eq. (190) bounds is required.

## Exact boundary

- The proof is a repository marked corollary of RG II's source-free
  decoupling construction; RG II does not print this scalar-source theorem.
- Equation (18) is a localization-cube-count norm under (17), not the printed
  \(d_k\)-weighted norm. Relating \(m(Y)\) to \(d_k(Y)\), spending polymer
  entropy with strict slack, and matching the later Lemma 3 norm remain open.
- Gauge invariance is termwise. No Euclidean covariance theorem is proved
  here. Even the partition-preserving transport identity must be recorded
  explicitly, and shifted partitions or symmetrization are needed for the
  full lattice group.
- The supremum and profile corollary cover only
  \(\mathcal P_{\rm int}(\mathcal Q)\); a shifted-root construction is required
  before arbitrary plaquette support is covered.
- The result is local in independent \((U,J,B)\), not in \(W\), and concerns
  the exact selected-coordinate branch only. It is not an intrinsic-coarea or
  unrestricted raw-fiber theorem.
- No cutoff-conditioned connected marked sum, marginal projection, profile
  mixing theorem, large-field estimate, RG iteration, continuum construction,
  infrared decay, or mass gap follows.

## Falsification checks

- Give the mark a nonzero linear perturbation and verify that (12)--(15), but
  not a quadratic or cubic bound, survive.
- Delete the \(A=\varnothing\) term and observe that the fully decoupled root
  contribution is lost.
- Let a mixed-difference set have a component disconnected from \(Q_p\) and
  check its cancellation using the block-diagonal weakened reconstruction.
- Replace (17) by equality and observe that the geometric series in (18) no
  longer proves summability.
- Place \(p\) across a cube boundary and reject use of (18) without a shifted
  partition or partition-of-unity extension.
- Weight (15) by the same exponent one hopes to retain and expose the missing
  entropy slack.
- Substitute \(U_{k+1}(W)\) and try to infer strict locality in \(W\); the
  nonlocal minimizing branch invalidates that inference.
