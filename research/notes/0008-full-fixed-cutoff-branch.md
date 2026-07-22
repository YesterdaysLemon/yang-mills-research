# Note 0008: the complete fixed-cutoff chart branch

Claim ID: YM-RG-008

Kind: primary-source corollary plus finite-dimensional coarea

Evidence: E2 (finite-regulator selected-branch statement; internally checked)

Novelty: none claimed

## Imported source facts

Retain Note 0005's density and normal-Jacobian conventions and every RG-I
hypothesis in Note 0006. In particular, fix \(d=4\), odd \(L>11\), one finite
torus and RG step, compact semisimple \(G\subset U(N)\), an admitted real coarse
background \(W\), and the fixed Eq. (2.9) threshold \(\varepsilon_1\).

Let

\[
I_k=T^{(k)}
\setminus\{b_0(c):c\in T^{(k+1)}\}
\]

be the complete independent-bond set. Use the rescaled independent coordinate

\[
a=g_kB\in\mathfrak g^{I_k},
\qquad
\mathcal Q_{\varepsilon_1}
=\{a:\|a\|_\infty<\varepsilon_1\}.
\tag{1}
\]

The following statements are checked in the primary text.

1. RG I, p. 267 after Eq. (2.10), constructs

   \[
   \widetilde Q(B')
   =L\widetilde QB'+\widetilde C(B'),
   \qquad
   L\widetilde Qh=I,
   \]

   and the analytic straightening

   \[
   B'=\Theta(X)=X-h\widetilde D(X),
   \qquad
   \widetilde Q(\Theta(X))=L\widetilde QX.
   \tag{2}
   \]

2. RG I, pp. 268 and 270, eliminates the selected \(b_0(c)\) coordinates,
   writes the linear constrained field as \(CB\), and reconstructs the
   original relative field as

   \[
   \beta_W(a)=C_Wa-h\widetilde D_W(C_Wa).
   \tag{3}
   \]

   The correction is supported on the \(b_0(c)\) bonds, so

   \[
   \beta_W(a)(b)=a(b),\qquad b\in I_k.
   \tag{4}
   \]

   Thus Eq. (2.9) is exactly the complete cube (1), not a cutoff on only a
   smaller sample of independent coordinates.

3. RG II, p. 6, Eqs. (1.19)–(1.20), proves on the whole cube that

   \[
   \|\beta_W(a)\|_\infty
   \le O(1)\|a\|_\infty
   +4C_2\bigl(O(1)\|a\|_\infty\bigr)^2
   \le C_1\|a\|_\infty
   <C_1\varepsilon_1,
   \tag{5}
   \]

   where \(C_1\) is absolute. The preceding paragraph states uniform
   analyticity and bounds on the admitted \(U,J\) domain. RG II p. 7 requires
   \(e^{32\kappa_1}\varepsilon_1\) below an absolute constant and imposes the
   remaining fixed smallness inequalities. Lemma 1, p. 9, Eq. (1.34), and the
   full integral in Section 2 use this same domain.

Choose \(\varepsilon_1\) with the strict margin required by all those printed
conditions, so the closure of (1) remains inside the common logarithm,
averaging, and analytic chart.

## Statement

Let \(F_k\) denote the selected Eq. (0.12) constraint map on that chart, and
let \(\mathcal C_{k,W}\) be the fine-field subset reconstructed from
\(\beta_W(a)\), \(a\in\mathcal Q_{\varepsilon_1}\), exactly as in RG I.
Then:

1. \(\mathcal C_{k,W}\) is the entire fixed-cutoff near-identity branch
   selected by RG I's delta elimination, and it is parameterized injectively
   by the complete cube \(\mathcal Q_{\varepsilon_1}\).
2. \(F_k\) is a submersion at every point of this branch.
3. The real coordinate determinant in RG I Eq. (2.12) is nonzero and has the
   positive orientation fixed at the background throughout this cube. No
   regulator-uniform numerical lower bound is asserted.
4. With normalized product Haar measures and invariant Riemannian metrics
   fixed, the intrinsic branch restriction

   \[
   K^{\mathrm{chart}}_k(W,A)
   =
   \int_{A\cap\mathcal C_{k,W}}
   \frac{\rho_M(U)}
        {\rho_N(W)J_{F_k}(U)}
   \,d\operatorname{vol}_{F_k^{-1}(W)}(U)
   \tag{6}
   \]

   is a finite nonzero positive Radon measure for every fixed finite
   regulator and admitted real \(W\).

This is a pointwise measure on the selected chart branch. It is not asserted
to equal the unrestricted raw group-delta fiber measure.

## Proof

The embedding \(C_W\) takes the independent coordinates into
\(\ker L\widetilde Q\). Equations (2)–(3) therefore give

\[
\widetilde Q(\beta_W(a))
=L\widetilde Q(C_Wa)=0,
\]

so the reconstructed configuration lies in \(F_k^{-1}(W)\). RG I's delta
elimination says that every configuration in the selected Eq. (2.9) branch is
obtained this way. Equation (4) proves injectivity and gives a continuous
inverse by projection to the independent coordinates.

Differentiate the exact identity in (2):

\[
D\widetilde Q_{\Theta(X)}\,D\Theta_X=L\widetilde Q.
\tag{7}
\]

The right side is onto because \(L\widetilde Qh=I\). Hence
\(D\widetilde Q_{\Theta(X)}\), and therefore the equivalent group constraint
differential, is onto throughout the domain. This proves the submersion
statement.

The determinant sign also follows from the same exact structure. Let \(P_I\)
project to the independent bonds. Since \(h\widetilde D\) is supported on the
selected bonds,

\[
P_I D\Theta_Xv=P_Iv.
\]

If \(D\Theta_Xv=0\), then \(v\) is supported on the selected bonds. That
selected subspace is \(\operatorname{im}h\): it has one
\(\mathfrak g\)-coordinate per coarse constraint and \(L\widetilde Qh=I\).
Write \(v=hy\). Equation (7) gives

\[
0=D\widetilde Q_{\Theta(X)}D\Theta_Xv
=L\widetilde Qv=y,
\]

so \(v=0\). Thus \(D\Theta_X\) is invertible everywhere on the real cube. Its
determinant is continuous, equals one at the origin, and cannot change sign on
the connected cube. It is therefore positive throughout. This validates the
real sign of the Eq. (2.12) coordinate factor but supplies no
dimension-independent scalar lower bound.

The branch parameterization has the full regular-fiber dimension: one
\(\mathfrak g\) coordinate remains for every fine bond except one selected
bond per coarse constraint. Its differential is injective because projection
to the independent components is the identity by (4). Thus
\(\mathcal C_{k,W}\) is a relatively open chart in the regular fiber.

By (5) and the strict smallness margin, the analytic reconstruction and the
algebra above extend to the closed cube, whose image is a compact subset of the
regular chart. The positive normal Jacobian
\(J_{F_k}\), the Haar densities, and the induced fiber density are continuous
there. They have finite upper bounds and positive lower bounds for this fixed
finite regulator and \(W\). The open cube has positive fiber volume, so (6)
is finite and strictly positive. Standard finite-dimensional local coarea
gives exactly (6). No global properness or global surjectivity statement is
used. \(\square\)

## Source consequence

For a real source-free action \(S_{k,x,W}\) whose branch integral is finite,
set

\[
Z^{\mathrm{chart}}_{k,x,W}(z;f)
=\int_{\mathcal C_{k,W}}
e^{-S_{k,x,W}(U)-z\mathcal O_f(U)}
K^{\mathrm{chart}}_k(W,dU).
\tag{8}
\]

At every fixed real admitted \(W\), positivity gives
\(0<Z^{\mathrm{chart}}_{k,x,W}(0;f)<\infty\). The selected branch and fixed
cutoff are frozen at \(z=0\), so they are independent of the source parameter
and profile. Note 0007 applies pointwise: the normalized ratio is entire and,
for the SU(2) one-block profile,

\[
\frac{Z^{\mathrm{chart}}_{k,x,W}(z;f)}
     {Z^{\mathrm{chart}}_{k,x,W}(0;f)}
\ne0
\quad\text{when}\quad
|z|<\frac{\log 2}{4\sum_p|f_p|},
\tag{9}
\]

with the \(f=0\) convention stated there. Its first log jet is the exact
selected-branch conditional expectation of \(-\mathcal O_f\).

## Exact boundary

The conclusion is deliberately narrower than a global disintegration theorem.

- The unrestricted compact-group fiber may have remote logarithmic branches,
  group roots, gauge copies, or large fields not represented by
  \(\mathcal C_{k,W}\). No equality or complement estimate is proved.
- Equation (6) uses an intrinsic positive real coarea density. The proof also
  fixes the sign of RG I Eq. (2.12)'s determinant on the real cube, but gives
  neither a regulator-uniform scalar lower bound nor a nonvanishing theorem on
  the whole complexified cube.
- Pointwise finiteness and positivity do not give a volume-, scale-, or
  background-uniform total-mass lower bound. Note 0007 explains why such a raw
  bound is generally false and unnecessary for normalized source ratios.
- Joint Borel or holomorphic dependence on \(W\), coarse-gauge covariance of
  the selected branch, and exact matching to every gauge-fixing normalization
  remain separate obligations.
- If the selected background or chart depends on \(x\), coupling
  differentiation acquires kernel terms. Only source independence is used in
  (8)–(9).
- No source-marked polymer estimate, large-field construction, RG iteration,
  continuum limit, infrared bridge, or mass gap follows.

## Falsification checks

- Check Eq. (4) on every independent bond; failure destroys injectivity.
- Find an independent \(a\) in the fixed cube for which (5) leaves the common
  chart; this would refute whole-support containment.
- Differentiate (2) and verify that \(L\widetilde Qh=I\) makes the nonlinear
  constraint differential onto.
- Search for an off-branch solution of the group constraint; its existence
  does not refute this claim but refutes any promotion to the unrestricted raw
  transform.
- Let the number of independent bonds grow and verify that the total branch
  mass may decay even though every finite-regulator mass is positive.
- Vary the chart with \(x\) and recover the missing kernel term in a raw
  coupling derivative.
