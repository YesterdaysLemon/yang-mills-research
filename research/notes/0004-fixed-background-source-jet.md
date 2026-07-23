# Note 0004: the fixed-background plaquette source jet

Claim ID: `YM-RG-003`

Kind: Lemma derived from a primary theorem

Evidence: E2 (bounded source-free-background consequence; internally checked)

Novelty: none claimed

## Imported theorem

Use Bałaban's [variational/background-field
paper](https://doi.org/10.1007/BF01229381) with all of its regularity,
smallness, geometry, and gauge-chart hypotheses.

- Theorem 1, p. 279, gives a unique minimizing gauge orbit
  \([U_1(V)]\) in the admitted one-step regular fixed-average space.
- Section G, pp. 305–309, fixes a local gauge branch for small relative coarse
  fields and proves its analytic expansion.
- Eq. (181), p. 307, gives coarse gauge covariance of the branch.
- Proposition 9 and Eqs. (182)–(190), pp. 307–309, give analyticity and an
  exponentially decaying derivative of the branch with respect to the coarse
  field.

This note does not reprove those results. It states and proves their elementary
consequence for a fixed source-free background.

## Statement

Let \(V\) lie in one of the analytic patches of Proposition 9 and let \(f\) be
a real plaquette profile of finite support. For real \(SU(2)\)-valued fields set

\[
J_f(V)=4\sum_p f_p
\left(1-\tfrac12\operatorname{Tr}U_1(V)_p\right).
\]

The value is independent of the representative of the minimizing orbit and is
invariant under coarse gauge transformations.

For the complex analytic branch, replace the real-slice plaquette action by
its holomorphic extension

\[
s_{\mathbb C}(U_p)=1-\tfrac12\operatorname{Tr}U_p.
\]

Then \(J_f\) is analytic in the local coarse coordinate
\(B=(1/i)\log V'\) used in Section G.

Proposition 9 writes the Landau-gauge relative minimizer as
\(\exp(i\eta\mathcal H(B))\), where \(B=(1/i)\log V'\), and defines its first
functional derivative in Eq. (182). For

\[
x\in\Delta(y),\qquad y\in\Lambda_j,
\qquad y'\in\Lambda_{j'},
\]

and bond directions \(\mu,\nu\), put

\[
K_{\mu\nu}(B;x,y')
=\frac{\delta\mathcal H_\mu(B,x)}{\delta B_\nu(y')}.
\]

The five component inequalities printed together in Eq. (190) are

\[
\begin{bmatrix}
|K_{\mu\nu}(B;x,y')|\\
|\nabla_xK_{\mu\nu}(B;x,y')|\\
\|\zeta\nabla K(B;\cdot,y')\|_\beta\\
|D_{U_k}^{\eta *}D_{U_k}^{\eta}K_{\mu\nu}(B;x,y')|\\
|\Delta_{U_k}^{\eta}K_{\mu\nu}(B;x,y')|
\end{bmatrix}
\le O(1)
\begin{bmatrix}
(L^j\eta)^{-1}\\
(L^j\eta)^{-2}\\
(\|\zeta\|_\beta^\xi+|\zeta|)(L^j\eta)^{-2-\beta}\\
(L^j\eta)^{-3}\\
(L^j\eta)^{-3}
\end{bmatrix}
(L^{j'}\eta)^{-d}
\exp\!\left[-\frac18\delta_0 d(y,y')\right].
\tag{190-import}
\]

The third line has \(\operatorname{supp}\zeta\subset\widetilde\Delta(y)\).
The symbols \(\|\zeta\|_\beta^\xi\), \(|\zeta|\), the cells, and the
multiscale distance are retained in the paper's notation. Notice especially
the distinct roles of \(j\) and \(j'\), and the exponent \(\delta_0/8\);
Eq. (189) immediately above has \(\delta_0/4\).

This is a componentwise first-background-derivative theorem for the
minimizer. It is not a derivative bound for a polymer activity. A finite
chain rule can use it as the minimizing-background input, but a quantitative
activity estimate additionally needs the chart/differential-of-exponential
factors, quantitative control of the exact auxiliary-\(J\) differential, a
metric/norm crosswalk, uniform activity Cauchy margins, convolution control,
and new entropy slack. Note 0016 supplies the exact finite-stencil
auxiliary-field reduction and conditional fixed-regulator Cauchy bounds, but
not those uniform crosswalks. Note 0017 subsequently supplies the strict
direct-\(J\) representative collar, dual source-density convolution, and a
conditional homogeneous-layer \(J\)-summand pullback; it also exhibits the
failure of a uniform reverse cross-layer comparison while leaving the
forward interface bound unresolved. Accordingly, no full standalone
quantitative quasilocal activity bound is part of this E2 lemma.

Finally, the fixed-background source factor

\[
\mathcal R_{\mathrm{bg}}(z,V)=e^{-zJ_f(V)}
\]

is entire and zero free in \(z\), and

\[
\left.\partial_z\log\mathcal R_{\mathrm{bg}}(z,V)\right|_{z=0}
=-J_f(V).
\]

## Proof

Two minimizers in the orbit differ by a fine gauge transformation compatible
with the fixed coarse average. Plaquette holonomy transforms by conjugation,
so its trace, and hence \(J_f\), is representative independent. Eq. (181)
gives the same conjugation statement under a coarse transformation of \(V\),
which proves coarse gauge invariance.

Proposition 9 makes every fine link in the chosen representative an analytic
function of the local coarse coordinate \(B\). A finite product and trace of
analytic matrix-valued functions is analytic, and the finite \(f\)-weighted
sum preserves analyticity. The use of \(s_{\mathbb C}\), rather than a real-part
operation, is essential on the complexified domain.

The last identity follows directly from the definition of the exponential
source factor. \(\square\)

## Exact boundary

The raw one-block integral has instead

\[
-\left.\partial_z\log\mathcal R_{x,z,f}(V)\right|_{z=0}
=\mathbb E_{\nu_{x,V}}[\mathcal O_f],
\]

by Note 0003. In general this conditional expectation is **not** equal to
\(J_f(V)=\mathcal O_f(U_1(V))\). A chosen RG representation of their difference
must account for fluctuations and for any Jacobian or polymer terms introduced
by that representation. Controlling the difference is the next open theorem.

## Nonclaims

- No source-dependent minimizing branch is constructed.
- No scalar-source analyticity of the full block integral follows from
  source-free background analyticity.
- No uniform source radius, interacting cumulant bound, marginal
  classification, or large-field estimate is proved.
- Equation (190)'s component indices and scale factors are transcribed above,
  but no quantitative quasilocal activity bound is claimed without the
  remaining uniform chart, local-remainder, \(d_{\mathcal B}\)-to-
  \(d_{k,\sigma}\), Cauchy-radius, convolution, and entropy crosswalk.
- Nothing here removes a regulator or constructs continuum Yang–Mills theory.
