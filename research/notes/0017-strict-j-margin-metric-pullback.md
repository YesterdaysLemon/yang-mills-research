# Note 0017: a strict auxiliary-\(J\) margin and the dual metric pullback

Claim ID: YM-RG-017

Kind: conditional finite-regulator analytic and kernel-norm lemma

Evidence: E2 (internally checked; source-hierarchy and chart compatibility
hypotheses retained)

Novelty: none claimed

Primary anchors: [RG
I](https://doi.org/10.1007/BF01215223), [RG
II](https://doi.org/10.1007/BF01239022), the
[variational/background-field paper](https://doi.org/10.1007/BF01229381), and
[*Propagators and renormalization transformations for lattice gauge theories
II*](https://doi.org/10.1007/BF01240221).

## The strict representative hypothesis isolated from RG I

Retain every hypothesis and notation of Notes 0013--0016. Fix the block
parameter \(M\) and the RG-I parameter hierarchy once and for all. RG I
defines

\[
\mathcal U_j^c(X,\alpha _0,\alpha _1,\gamma _0)
\]

as a union of complex gauge orbits having representatives that satisfy its
conditions (i)--(iv), printed pp. 262--263. Conditions (i) and (ii) involve
only \(U\). Condition (iii), Eq. (1.14), contains the direct bound

\[
\lVert J\rVert_{\infty,X}<\gamma _0.
\tag{1}
\]

The paper then usually takes \(\gamma_0=\alpha_0\).
Condition (iv) tests the derived pairs
\((U_n(M^j(U)),J_n(M^j(U)))\); its \(J_n\) is computed from \(U\) by RG I
Eq. (1.8), not from the independent variable \(J\).

On printed p. 263 RG I chooses smaller constants
\(\alpha _0'<\alpha _0\) and \(\alpha _1'<\alpha _1\), uses Proposition 9 to
obtain condition (iv) when the smaller constants are sufficiently small, and
then specializes to the source-defined \(J\) with
\(\lVert J\rVert_\infty<\alpha _0'\). It states that sufficiently regular
minimal configurations satisfy these conditions. The statement is
qualitative: it prints neither a numerical value of \(\alpha _0'\) nor a
transported representative atlas.

RG I declares \(\alpha_0,\alpha_1\) independent of \(X\) and \(j\), and its
Theorem 3 chooses the small-field constants once for fixed \(M\). Thus the
p. 263 mechanism is uniform in location and RG step inside that frozen
small-field hierarchy. What still has to be named for this repository's
shifted family is the representative compatibility below.

Accordingly, make the exact part needed below explicit.

**Strict-\(J\) representative hypothesis \((\mathrm H_J)\).** There is one
constant

\[
0<\bar\alpha _0<\alpha _0
\tag{2}
\]

chosen with the fixed RG-I hierarchy such that, for every admitted
\((N,k,p,\sigma,Y)\) and every
\(\omega\in\overline{\Omega_{\mathbb C}}\), the physical pair has a
representative satisfying RG I conditions (i)--(iii) on \(Y\) and condition
(iv) on RG I's prescribed \(Y^{-2}\), with base parameters
\((\alpha _0,\alpha _1,\alpha _0)\), and

\[
\lVert J_{k+1}(U_{k+1})\rVert_{\infty,Y}
\le \bar\alpha _0.
\tag{3}
\]

The representative for each centre is required to be the one used by the
split activity chart. In this note the chart's \(J\) coordinate is assumed to
be the raw affine direct-\(J\) coordinate:

\[
\chi^J_{Y,\sigma}(J+w)=\chi^J_{Y,\sigma}(J)+w,
\qquad
\lVert w\rVert_{\mathsf J,Y,\sigma}=\lVert w\rVert_{\infty,Y}.
\]

Transported shifts act isometrically in this norm. RG I's p. 263 discussion motivates
\((\mathrm H_J)\), but this note does not replace its qualitative
"sufficiently small" choices by an unaudited numerical constant.

## Exact additive \(J\)-collar

Define

\[
\Delta_J:=\alpha _0-\bar\alpha _0>0.
\tag{4}
\]

For any representative in \((\mathrm H_J)\) and any algebra-valued bond field
\(w\) with

\[
\lVert w\rVert_{\infty,Y}<\Delta_J,
\tag{5}
\]

the pair \((U,J+w)\) belongs to the RG-II Eq. (1.34) outer domain

\[
\mathcal U_{k+1}^c
\bigl(Y,(1+\beta)\alpha _0,(1+\beta)\alpha _1,\alpha _0\bigr).
\tag{6}
\]

Indeed, conditions (i), (ii), and (iv) are unchanged when the independent
\(J\) variable changes. For condition (iii),

\[
\lVert J+w\rVert_{\infty,Y}
<\bar\alpha _0+\Delta_J=\alpha _0.
\tag{7}
\]

The same representative therefore proves membership in the union of orbits;
no additive chart on that union is inferred. This is a full complex
\(\ell^\infty\)-norm ball in the linear \(J\) coordinate. It is not a
coordinate-axis polydisc and it does not use compactness of a regulator-sized
family.

Let \(A_{p,\sigma,Y}(\varphi)\) and \(\mathcal B_d\) be Note 0016 Eqs.
(12) and (16). Cauchy's formula on complex lines in (5) gives

\[
\boxed{
\lVert D_J\widehat W_{k,p}(\sigma,Y)\rVert_{(\ell^\infty)^*}
\le
\frac{A_{p,\sigma,Y}(\varphi)}{\Delta_J}.
}
\tag{8}
\]

Consequently, under \((\mathrm H_J)\), Note 0016 Eq. (18) sharpens to

\[
\boxed{
\sup_p\sum_{\sigma,Y}e^{a d_{k,\sigma}(Y)}
\sup_{\mathfrak C_Y^\sigma}
\lVert D_J\widehat W_{k,p}(\sigma,Y)\rVert_{(\ell^\infty)^*}
\le \frac{\mathcal B_d}{\Delta_J}.
}
\tag{9}
\]

The constant in (9) is independent of volume, RG step, plaquette, shift, and
polymer once the fixed-\(M\) hypothesis \((\mathrm H_J)\) holds. There is no
corresponding direct-sup-norm conclusion for \(U\): varying \(U\) changes
every nonlinear regularity and derived-pair condition. Note 0018 sharpens
this boundary by proving that the naive raw and \(\xi\)-scaled bond-sup
\(U\)-radii collapse and by isolating a conditional RG-scaled replacement.

## The Eq. (190) kernel as a weighted source density

Write

\[
s_j=L^j\eta,
\qquad
\mu(j,y)=s_j^d,
\qquad
\lambda=\frac{\delta _0}{8}.
\tag{10}
\]

The source normalization used in the variational paper is

\[
(D_B\mathcal H\,h)(x)
=\sum_{j',y'}\mu(j',y')K(x;j',y')h(j',y').
\tag{11}
\]

For \(x\in\Delta(y)\), \(y\in\Lambda_j\), Eq. (190) has the common
kernel-density factor

\[
\mu(j',y')^{-1}
e^{-\lambda d_{\mathcal B}(y,y')}.
\tag{12}
\]

Its five output scale factors are transcribed in Note 0004. In the exact
auxiliary-field differential of Note 0016, the
\(D_U^{\eta *}D_U^\eta K\) row supplies the leading term, while the local
remainder and the selected differential-of-exponential/gauge-restoration
maps can also use the \(K\) and \(\nabla K\) rows. Do not count the printed
\(\Delta_U^\eta K\) row a second time when it is merely the alternative
Laplacian rewrite of the leading row.

On a selected chart, let \(C_{J,1},C_{J,2},C_{J,4}\ge0\) bound those local conversion
maps in the same component norms and put

\[
E_J(j)=C_{J,4}s_j^{-3}+C_{J,2}s_j^{-2}+C_{J,1}s_j^{-1}.
\tag{13}
\]

Equation (190) then gives a constant \(C_\chi\), finite on the fixed chart,
such that the physical auxiliary-\(J\) derivative density obeys

\[
\left\lVert
\frac{\delta\mathcal J(x)}{\delta B(j',y')}
\right\rVert_{\rm op}
\le
C_\chi E_J(j)\mu(j',y')^{-1}
e^{-\lambda d_{\mathcal B}(y,y')}.
\tag{14}
\]

Equation (14) is scale explicit, but it is regulator uniform only if
\(C_\chi,C_{J,1},C_{J,2},C_{J,4}\) are proved uniform for the selected chart
family. This note does not assume that conclusion silently.

## Dual exponential summation without a polymer-volume factor

Fix

\[
0\le\gamma<\lambda,
\qquad
\alpha_\gamma=\frac18-\frac\gamma{\delta _0}>0.
\tag{15}
\]

Whenever the paper's strengthened separation condition for Eq. (2.59) holds
at \(\alpha_\gamma\), Propagators II Lemma 2.1, Eqs. (2.59)--(2.63), gives a
constant \(c_1(\alpha_\gamma)\) for the exponential sum. Multiplying (14) by
\(\mu(j',y')e^{\gamma d_{\mathcal B}(y,y')}\) and summing yields

\[
\boxed{
\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(y,y')}
\left\lVert
\frac{\delta\mathcal J(x)}{\delta B(j',y')}
\right\rVert_{\rm op}
\le
C_\chi E_J(j)c_1(\alpha_\gamma).
}
\tag{16}
\]

The factor \(\mu(j',y')^{-1}\) in Eq. (190) cancels the source measure in
(16) exactly. The unused decay is
\((\lambda-\gamma)d_{\mathcal B}\), which is precisely the exponent to which
Lemma 2.1 is applied.

Represent the finite-dimensional derivative in (8) as

\[
D_J\widehat W_Y[b]=\sum_{x\in I(Y)}\ell_{Y,x}[b(x)].
\tag{17}
\]

For the direct-sum \(\ell^\infty\) norm,

\[
\sum_{x\in I(Y)}\lVert\ell_{Y,x}\rVert_*
=\lVert D_J\widehat W_Y\rVert_{(\ell^\infty)^*}.
\tag{18}
\]

Absorb the fixed spacetime and \(SU(2)\) component count into \(C_\chi\), and
define the auxiliary-\(J\) chain-rule density

\[
\mathcal L_Y^J(j',y')
=\sum_{x\in I(Y)}
\ell_{Y,x}\!\left[
\frac{\delta\mathcal J(x)}{\delta B(j',y')}
\right].
\tag{19}
\]

For a root cell \(q\), set

\[
D_{\mathcal B}(q,Y)
=\sup_{x\in I(Y)}d_{\mathcal B}(q,y_x),
\qquad x\in\Delta(y_x),
\tag{20}
\]

and \(E_J(Y)=\sup_{x\in I(Y)}E_J(j_x)\). The triangle inequality, (16),
Fubini's theorem for finite sums, and (18) prove

\[
\boxed{
\begin{aligned}
&\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(q,y')}
|\mathcal L_Y^J(j',y')|\\
&\quad\le
C_\chi c_1(\alpha_\gamma)E_J(Y)
e^{\gamma D_{\mathcal B}(q,Y)}
\lVert D_J\widehat W_Y\rVert_{(\ell^\infty)^*}.
\end{aligned}
}
\tag{21}
\]

The key point is (18): the sum over \(x\in I(Y)\) is already the dual
operator norm controlled by Cauchy. Replacing it by a pointwise derivative
bound and then summing over \(x\) would introduce a polymer-volume factor and
would change a geometric animal sum from \((1-q_d)^{-1}\) to a bound of
order \((1-q_d)^{-2}\).

## Conditional one-layer comparison with the rooted polymer metric

The following is the maximal comparison justified without solving the
multiscale interface problem. Assume:

1. every output cell in \(I(Y)\), the root cell \(q_p\), and a shortest
   contained tree for \(Y\) lie in one Propagators-II layer \(r\);
2. \(s_r=L^r\eta\) is the lattice spacing used for the shifted partition;
3. each shifted localization cube is identified with an \(M s_r\)-cube of
   that layer; and
4. the tree and the endpoint paths are admissible contours for
   \(d_{\mathcal B}\).

Within one layer, Propagators II Eq. (2.46) is lattice \(\ell^1\)-length
divided by \(s_r\). The contained tree in Note 0013 has length
\(M s_r d_{k,\sigma}(Y)\). Thus, if \(\tau_{\mathcal B}(Y)\) denotes the
infimum of total Eq. (2.46) length over the same admitted contained-tree
class,

\[
\tau_{\mathcal B}(Y)=M d_{k,\sigma}(Y).
\tag{22a}
\]

Joining the root and output cells to that tree
inside their \(M s_r\)-cubes costs at most \(d(M+1)\) at each endpoint in
the dimensionless \(d_{\mathcal B}\) metric. Hence

\[
\boxed{
D_{\mathcal B}(q_p,Y)
\le M d_{k,\sigma}(Y)+C_{\rm end},
\qquad C_{\rm end}=2d(M+1).
}
\tag{22}
\]

This is a diameter-from-tree bound; the reverse comparison is false for
arbitrary bushy polymers and is neither needed nor claimed.

Let \(a=(1-2\delta)\kappa\) as in Note 0016, and choose \(a_*\ge0\) so that

\[
a_*+\gamma M\le a.
\tag{23}
\]

For the following corollary, fix one layer \(r\) and restrict the activity sum
to the admitted \((\sigma,Y)\) satisfying assumptions 1--4 in that same
layer; write this restriction as \(\sum^{(r)}_{\sigma,Y}\). Assume in addition
that \(C_\chi,C_{J,1},C_{J,2},C_{J,4}\) can be chosen common over this
one-layer family, so that \(E_J(Y)=E_J(r)\). Combining (9), (21), and (22)
gives the conditional one-layer auxiliary-\(J\) pullback norm

\[
\boxed{
\begin{aligned}
&\sup_p\sum^{(r)}_{\sigma,Y}e^{a_*d_{k,\sigma}(Y)}
\sup_{\mathfrak C_Y^\sigma}\left[
\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(q_p,y')}
|\mathcal L_{p,\sigma,Y}^J(j',y')|\right]\\
&\quad\le
\frac{C_\chi c_1(\alpha_\gamma)E_J(r)
e^{\gamma C_{\rm end}}\mathcal B_d}{\Delta_J}.
\end{aligned}
}
\tag{24}
\]

No \(|Y|\), regulator volume, or shifted-orbit factor occurs in (24). Its
decay expenditure is explicit: \(\gamma M\) is taken from the rooted
\(d_k\) exponent, and \(\gamma<\delta_0/8\) is taken from Eq. (190).

## What the coarse-layer ratio does and does not prove

There is a concrete obstruction, not just a missing estimate. Suppose the
localization mesh is matched to layer \(r_0\), while a contour segment of a
fixed physical length travels in a coarser layer \(r\). The fixed-scale
\(d_k\) normalization uses \(M s_{r_0}\), whereas the local
\(d_{\mathcal B}\) normalization uses \(s_r=L^{r-r_0}s_{r_0}\). The ratio of
the segment's fixed-scale contribution to its multiscale contribution is

\[
\frac{L^{r-r_0}}{M}.
\tag{25}
\]

It is unbounded when the permitted layer depth grows. Therefore no
regulator-uniform reverse bound \(d_{k,\sigma}\le C d_{\mathcal B}\), and no
two-sided metric equivalence, follows from the definitions. This is not an
obstruction to the direction actually used in (22): on such a coarse-layer
segment the opposite ratio is
\(d_{\mathcal B}/d_{k,\sigma}=M/L^{r-r_0}\le M\), so coarse travel by itself
helps a bound of the form \(d_{\mathcal B}\le C d_{k,\sigma}\).

The needed forward comparison nevertheless remains unproved in this note
across general layered contours. A source recheck corrects one earlier
description: Propagators II Eq. (2.57) is a lower bound on actual travel
between distinct layer surfaces used in the Eq. (2.58) summation, not an
additive \(RM\) toll in the definition of \(d_{\mathcal B}\). Thus an ordinary
fine path already pays its interface travel.

Likewise, nonalignment between Note 0014's shifted \(M\)-grid and a deeper
Propagators-II grid is not by itself a one-sided obstruction. A bondwise proof
could map each fine site to its multiscale cell and bound the
\(d_{\mathcal B}\) distance of the cells assigned to two fine nearest
neighbors. What is missing here is that explicit tie-broken cell map, its
uniform nearest-neighbor constant, and a support/root statement placing every
output coordinate within a bounded fine-lattice halo of \(Y\).

Equation (25) falsifies only the reverse half of a uniform equivalence. The
missing cell-map and support premises leave the forward
\(d_{\mathcal B}\)-to-\(d_{k,\sigma}\) estimate needed by (22) unresolved in
this note; they do not refute it. A later proof may establish the bondwise
cell-map theorem, restrict the admitted support geometry, or replace the
fixed-scale polymer norm by a compatible multiscale network norm.

## Exact boundary

- Equation (9) is a uniform representative-\(J\) result only under the named
  hierarchy/representative hypothesis \((\mathrm H_J)\). RG I prints the
  qualitative smaller-domain mechanism, not a numerical cross-chart atlas.
- Equation (24) controls only the
  \(D_J\widehat W[D\mathcal J\,h]\) summand of Note 0016's physical chain
  rule. The \(D_U\widehat W[D\mathcal U\,h]\) summand still lacks a uniform
  nonlinear \(U\)-chart collar in a concrete RG-scaled regularity norm;
  Note 0018 rules out the naive bond-sup alternatives.
- The source-metric convolution is proved before identifying
  \(d_{\mathcal B}\) with \(d_{k,\sigma}\). Equation (22) is deliberately
  conditional on a matched homogeneous layer. The primary sources audited so
  far do not supply the shifted-cell map or the needed one-sided contour bound
  across every layer interface. Equation (25) rules out only the reverse bound.
- Uniformity of \(C_\chi\) and the local coefficients in (13) remains open.
  A finite fixed-chart constant is not an RG-iteration theorem.
- No one-fixed-partition compatibility, connected marked expectation,
  large-field estimate, RG iteration, continuum construction, infrared
  decay, or Yang--Mills mass gap follows.

## Falsification checks

- Vary \(J\) and verify directly that RG I condition (iv) uses the
  source-defined \(J_n(M^j(U))\), not the independent \(J\) coordinate.
- Let \(\bar\alpha _0\uparrow\alpha _0\) and observe
  \(\Delta_J\downarrow0\).
- Choose a physical representative not shared with the activity chart and
  identify the missing premise in \((\mathrm H_J)\).
- Drop the measure \(\mu(j',y')\) in (11) or the inverse measure in Eq. (190)
  and reject the cancellation in (16).
- Replace the dual \(\ell^1\) identity (18) by coordinatewise suprema and
  expose the artificial polymer-volume factor.
- Move the chart supremum in (24) inside the source sum and identify the
  invalid interchange of supremum and summation.
- Set \(\gamma=\delta_0/8\) and observe that the reserved exponential sum has
  no positive exponent.
- Apply (22) across an unverified layer interface and reject the comparison.
- Attempt to use (25) to reject the forward bound
  \(d_{\mathcal B}\le C d_{k,\sigma}\), reject that inference, and identify
  the reversed inequality that (25) actually obstructs.
- Add both Eq. (190) Laplacian rows as independent leading terms and identify
  the double counting.
