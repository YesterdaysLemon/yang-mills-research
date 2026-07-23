# Note 0011: one marked insertion at the Mayer seam

Claim ID: YM-RG-011

Kind: finite-dimensional source corollary plus exact Mayer algebra

Evidence: E2 (finite-regulator identity; internally checked)

Novelty: none claimed

## Fixed operational law

Use exactly the normalized RG-I coordinate law of Note 0010. Fix one finite
regulator, admitted real background \(W\), real finite-support plaquette
profile \(f\), and

\[
\mathcal O_f^{\mathrm{field}}(U)=
4\sum_p f_p\left(
1-\frac12\operatorname{Tr}U_p
\right),
\qquad
\mathcal O_f(W,B)=
\mathcal O_f^{\mathrm{field}}(\mathscr U_k(W,B)).
\tag{1}
\]

Let

\[
\mathcal O_f^{\mathrm{bg}}(W)=\mathcal O_f(W,0),
\qquad
\Delta_f(W,B)=
\mathcal O_f(W,B)-\mathcal O_f^{\mathrm{bg}}(W).
\tag{2}
\]

At \(B=0\), RG I identifies the reconstruction with its selected source-free
minimizing background \(U_{k+1}(W)\), up to the selected gauge representative.
Program 003's one-step notation \(U_1(W)\) denotes that same minimizing orbit.
Because \(\mathcal O_f\) is gauge invariant,
\(\mathcal O_f^{\mathrm{bg}}(W)=\mathcal O_f^{\mathrm{field}}(U_1(W))\)
independently of the representative. No source-dependent saddle or background
is introduced.

## Exact background split

Write Note 0010's full Eq. (2.12) exponent as
\(\Psi_k^{\mathrm{RG}}(W,B)\). The exact normalized source ratio factors as

\[
\begin{aligned}
R_{k,W}^{\mathrm{RG}}(z;f)
&=e^{-z\mathcal O_f^{\mathrm{bg}}(W)}\\
&\quad\times
\frac{
\int \chi_k(B)
e^{\Psi_k^{\mathrm{RG}}(W,B)-z\Delta_f(W,B)}
\,d\mu_{\Gamma_k(W)}(B)
}{
\int \chi_k(B)e^{\Psi_k^{\mathrm{RG}}(W,B)}
\,d\mu_{\Gamma_k(W)}(B)
}.
\end{aligned}
\tag{3}
\]

This is only the identity
\(\mathcal O_f=\mathcal O_f^{\mathrm{bg}}+\Delta_f\), applied after the
source-independent RG-I coordinate changes. Since the real observable is
bounded on the finite cutoff cube, differentiation under the integral is
valid and gives

\[
-\partial_z\log R_{k,W}^{\mathrm{RG}}(0;f)
=\mathcal O_f^{\mathrm{bg}}(W)
+\mathbb E_{\nu_{k,W}^{\mathrm{RG}}}\Delta_f(W,B).
\tag{4}
\]

Thus Program 003's operational remainder is exactly

\[
\mathcal J_f^{\mathrm{RG}}(W)
=\mathbb E_{\nu_{k,W}^{\mathrm{RG}}}\Delta_f(W,B).
\tag{5}
\]

The mark has the following finite-regulator properties.

1. \(\Delta_f\) is linear in \(f\).
2. It is holomorphic on the same local complex background/fluctuation patch as
   the reconstructed field.
3. On the real slice it is invariant under the simultaneous transported-chart
   gauge transformation of \(W\) and \(B\).
4. It vanishes at \(B=0\).
5. For real \(SU(2)\) fields,

   \[
   |\Delta_f(W,B)|\le 8\sum_p|f_p|.
   \tag{6}
   \]

The last bound uses \(0\le1-\tfrac12\operatorname{Tr}U_p\le2\) and is a
range bound only. It gives no decay with distance from \(\operatorname{supp}f\).

## Exact one-mark Mayer identity

In Note 0010's notation, the source-free exponent is

\[
\Psi_k^{\mathrm{RG}}(W,B)
=P^{(k)}(g_k,U_{k+1}(W),B)
+R_{(2.12)}^{(k)}(W,B).
\tag{7}
\]

RG II Lemma 2, Eqs. (1.41)–(1.43), decomposes this exponent at the entrance to
Section 2 into a finite-regulator family of localized activities, up to a
source- and \(B\)-independent scalar convention:

\[
\Psi_k^{\mathrm{RG}}(W,B)
=c_k(W)+\sum_{Y\in\mathcal D_k}V_k(Y;W,B).
\tag{8}
\]

The factor \(e^{c_k(W)}\) cancels from the normalized source ratio, so the
Mayer algebra may use the displayed activity sum without identifying scalar
normalization conventions. Here \(\mathcal D_k\) is finite at the fixed
regulator. For each activity,

\[
e^{V_Y}=1+\int_0^1V_Ye^{tV_Y}\,dt.
\tag{9}
\]

Multiplying (9) over \(Y\in\mathcal D_k\) and inserting exactly one copy of
\(\Delta_f\) gives the algebraic identity

\[
\begin{aligned}
\Delta_f(B)e^{\sum_YV_Y(B)}
={}&\sum_{D\subset\mathcal D_k}
\int_{[0,1]^D}
\Delta_f(B)
\left(\prod_{Y\in D}V_Y(B)\right)\\
&\qquad\qquad\times
\exp\!\left(\sum_{Y\in D}t_YV_Y(B)\right)
\,d\mathbf t .
\end{aligned}
\tag{10}
\]

Equation (10) is the exact first-mark analogue of the elementary Mayer
expansion used at RG II Eq. (2.1). It constructs the first source jet without
requiring a full \(z\)-dependent RG induction: the mark occurs linearly and
exactly once, while every other factor is an unmarked source-free activity.

The identity may be integrated against the unchanged cutoff and Gaussian
measure in (3). It does not license termwise infinite-volume limits; all sums
here are finite before a convergence theorem is invoked.

## Localization interface and the next proved auxiliary lemma

Indexing

\[
\Delta_f=\sum_p f_p\Delta_p
\tag{11}
\]

does not make \(\Delta_p(W,B)\) local in the fluctuation coordinate. The
reconstructed field contains the minimizing background and propagator
dependence. The independent-variable localization interface is a rooted
decomposition

\[
\Delta_p(U,J,B)=
\sum_{Y\supset Q_p}W_{k,p}(Y;U,J,B)
\tag{12}
\]

where \(Q_p\) is a fixed RG-II localization cell having \(p\) strictly in its
interior. Require the decomposition on the exact RG-II analytic domain, with:

- dependence only on fields in the interior of \(Y\);
- \(W_{k,p}(Y;U,J,0)=0\);
- simultaneous gauge invariance and correct Euclidean covariance of the root
  plaquette;
- a location-uniform rooted summability norm such as

  \[
  \sup_p\sum_{Y\supset Q_p}
  e^{\kappa_\bullet d_k(Y)}
  \sup_{\mathrm{RG\ II\ Eq.\ (1.34)}}|W_{k,p}(Y;U,J,B)|<\infty,
  \tag{13}
  \]

  with strict decay slack relative to the unmarked RG-II norm.

Note 0012 subsequently proves (12) on the independent RG-II \((U,J,B)\)
domain for plaquettes interior to one fixed localization partition, with a
conditional interior-location-uniform cube-count norm. Note 0013 upgrades that
norm to the target (13) for the standard wall-adjacent \(M\)-cube branch under
an explicit entropy margin. Note 0014 subsequently gives an RG-admitted
shifted-root cover for every plaquette and transport under the subgroup
preserving the next coarse lattice. It does not prove unit-translation
covariance or locality after the minimizing-background pullback. Note 0021
subsequently proves the exact marked Section-2 algebra on one compatible fixed
partition, and Note 0026 subsequently proves its marked norm and connected
first derivative at \(t=0\). Note 0027 subsequently synchronizes the complete
nested shifted first jets without mixing their gases.

Given (12), a marked activity \(W_{k,p}(A)\) and an unmarked Mayer
family \(D\) have the rooted seed

\[
Y_0^\bullet=A\cup\bigcup_{Y\in D}Y.
\tag{14}
\]

That seed, rather than the unmarked union alone, must be carried through RG II
Eqs. (2.2)–(2.10). The connected logarithm would then contain exactly one
marked activity decorated by the already controlled unmarked activities. None
of those rooted estimates is proved by (10). Note 0021 subsequently proves
the finite distinguished-slot and component algebra, and Note 0026 separately
proves those positive estimates under its doubled-amplitude refinement.

## Exact boundary

- Equations (3)–(10) concern the exact normalized RG-I selected-coordinate law
  \(\nu^{\mathrm{RG}}\), not the intrinsic coarea or unrestricted raw law.
- The source insertion and one-mark identity are repository corollaries; the
  audited RG I/II papers are source free and do not print this marked theorem.
- The \(\ell^1\) profile bound in (6) is not Program 002's still-untranscribed
  discrete \(C^6\) source norm.
- This note alone proves no localization of \(\Delta_p\). Note 0012 separately
  supplies the independent-variable fixed-partition decomposition, and Note
  0013 its standard-branch \(d_k\) norm, and Note 0014 an all-plaquette
  RG-admitted shifted cover. Note 0026 closes fixed-partition cluster
  differentiation at \(t=0\), and Note 0027 synchronizes the shifted first
  jets. Nonzero-source polymer activities, the physical pullback, marginal
  projection, position/orientation mixing, and the large-field estimate
  remain open.
- No RG iteration, continuum construction, Osterwalder–Schrader
  reconstruction, infrared decay estimate, or mass gap follows.

## Falsification checks

- Replace \(\mathcal O_f^{\mathrm{bg}}\) by a source-dependent background and
  recover the omitted background derivative terms.
- Let \(f\) be complex and observe that the real range statement no longer
  applies.
- Drop the \(D=\varnothing\) term from (10) and lose the bare marked insertion.
- Treat \(\Delta_p\) as local merely because it carries a plaquette index; the
  nonlocal reconstruction refutes that shortcut.
- Use an intrinsic-coarea expectation in (4) without a density-matching
  theorem and obtain a different, presently uncontrolled jet.
