# Note 0007: projective source kernels and a bounded-source disk

Claim ID: YM-RG-007

Kind: elementary finite-measure lemma

Evidence: E2 (internally checked only)

Novelty: none claimed

## Statement

Let \(K_r(V,du)\) be a finite nonzero positive measure for every real
regulator/coarse-field pair \((r,V)\). Let \(S_{r,x,V}\) be real and measurable,
and suppose

\[
0<Z_{r,x,V}(0)
=\int e^{-S_{r,x,V}(u)}K_r(V,du)<\infty .
\tag{1}
\]

Define

\[
\nu_{r,x,V}(du)
=Z_{r,x,V}(0)^{-1}e^{-S_{r,x,V}(u)}K_r(V,du).
\tag{2}
\]

Let \(\mathcal O_{r,f}\) be real and bounded on the support of this probability
measure. Write

\[
a_{r,f,V}=\operatorname*{ess\,inf}_{\nu_{r,x,V}}\mathcal O_{r,f},
\qquad
b_{r,f,V}=\operatorname*{ess\,sup}_{\nu_{r,x,V}}\mathcal O_{r,f},
\qquad
D_{r,f,V}=b_{r,f,V}-a_{r,f,V}.
\tag{3}
\]

Then the normalized source ratio

\[
R_{r,x,V}(z)
=\frac{\int e^{-S_{r,x,V}(u)-z\mathcal O_{r,f}(u)}K_r(V,du)}
{\int e^{-S_{r,x,V}(u)}K_r(V,du)}
=\mathbb E_{\nu_{r,x,V}}e^{-z\mathcal O_{r,f}}
\tag{4}
\]

is entire. If \(D_{r,f,V}>0\), it is zero-free on

\[
|z|<\frac{2\log 2}{D_{r,f,V}}.
\tag{5}
\]

If \(D_{r,f,V}=0\), it is a nonzero exponential and hence zero-free on all of
\(\mathbb C\). On the disk (5), choose the branch with \(\log R(0)=0\). Its
first two source jets are

\[
\partial_z\log R(0)=-\mathbb E_\nu\mathcal O_{r,f},
\qquad
\partial_z^2\log R(0)=\operatorname{Var}_\nu(\mathcal O_{r,f})
\le \frac{D_{r,f,V}^2}{4}.
\tag{6}
\]

If a distinguished background value
\(\mathcal O_{r,f}(U_1(V))\in[a_{r,f,V},b_{r,f,V}]\), then

\[
\left|
\mathbb E_\nu\mathcal O_{r,f}
-\mathcal O_{r,f}(U_1(V))
\right|
\le D_{r,f,V}.
\tag{7}
\]

If \(D_{r,f,V}\le D_*>0\) throughout a family, the common disk
\(|z|<2\log 2/D_*\), the variance bound, and the background-difference bound
are uniform throughout that family. In particular, no regulator-uniform lower
bound on the raw mass \(K_r(V,M)\) is needed.
Any fixed \(0<z_0<2\log 2/D_*\), for example
\(z_0=\log 2/D_*\), gives the corresponding closed zero-free disk
\(|z|\le z_0\).

## Proof of the disk

Set \(c=(a+b)/2\) and \(Y=\mathcal O-c\), suppressing the indices. Then
\(|Y|\le D/2\) almost surely and

\[
e^{zc}R(z)=\mathbb E_\nu e^{-zY}.
\]

For every \(z\in\mathbb C\),

\[
\begin{aligned}
\left|\mathbb E_\nu e^{-zY}-1\right|
&\le \mathbb E_\nu\left|e^{-zY}-1\right|\\
&\le \mathbb E_\nu\left(e^{|z||Y|}-1\right)\\
&\le e^{|z|D/2}-1.
\end{aligned}
\tag{8}
\]

The last expression is strictly less than one when (5) holds, so the
expectation cannot vanish there. Boundedness supplies a locally uniform
majorant for the exponential series and proves entireness. Differentiating at
zero gives (6); the variance bound is the elementary range inequality
\(\operatorname{Var}X\le(\sup X-\inf X)^2/4\). Equation (7) follows because
both numbers lie in the same interval. \(\square\)

## Projective invariance

Let

\[
K'_r(V,du)=A_r(x,V)K_r(V,du),
\qquad 0<A_r(x,V)<\infty,
\tag{9}
\]

where \(A_r\) is independent of \(z\) and \(f\). Equations (2), (4), and every
normalized source cumulant are unchanged. By contrast,

\[
K'_r(V,M)=A_r(x,V)K_r(V,M)
\tag{10}
\]

and its coarse-field derivatives can be changed arbitrarily by the choice of
\(A_r\). Thus an absolute raw-mass lower bound is not invariant under the
natural projective equivalence relevant to normalized source observables.

If \(A_r\) depends on \(x\), it still cancels from (4), but it contributes
\(\partial_x\log A_r\) to a raw coupling derivative. The constant-profile
coupling identity in Note 0003 therefore requires the raw kernel convention to
be fixed independently of \(x\), even though the source-only statement here
requires only \(z\)-independence.

## Correct coarse-field derivative

Suppose on a real coarse patch a fiber integral has been pulled back to a
fixed domain \(D\):

\[
\mathbb E_{\nu_V}O_V
=\frac{\int_D O(V,b)q(V,b)\,db}
{\int_D q(V,b)\,db},
\qquad q(V,b)>0.
\tag{11}
\]

Under ordinary dominated \(C^1\) hypotheses, a directional derivative
\(\partial_\xi\) satisfies

\[
\partial_\xi\mathbb E_{\nu_V}O_V
=\mathbb E_{\nu_V}[\partial_\xi O_V]
+\operatorname{Cov}_{\nu_V}
\!\left(O_V,\partial_\xi\log q(V,\cdot)\right).
\tag{12}
\]

This centered-score formula is also projectively invariant: multiplying
\(q(V,b)\) by \(A(V)>0\) adds the \(b\)-constant
\(\partial_\xi\log A(V)\) to the score, and covariance kills it. A bound on
\(\partial_V\log K_r(V,M)\) is therefore neither necessary nor sufficient for
locality of normalized observables. A moving sharp domain would add boundary
terms; it must be straightened to a fixed domain or handled separately.

## Product-cutoff counterexample

Let

\[
M_n=N\times(S^1)^n,\qquad F_n(v,\theta)=v,
\]

with normalized product Haar measure, and let \(A\subset S^1\) have Haar
measure \(q\in(0,1)\). The fixed product restriction

\[
C_n=N\times A^n
\]

has pointwise raw fiber mass

\[
K_n^{C_n}(v,M_n)=q^n\longrightarrow0.
\tag{13}
\]

Every fiber intersection has positive measure, \(F_n\) is a proper
submersion, and its normal Jacobian is one. Thus even perfect per-coordinate
geometry does not imply a regulator- or volume-independent raw lower bound
when the fiber dimension grows. Normalizing the restricted fiber measure
removes the factor \(q^n\); an observable depending on only one coordinate can
have an \(n\)-independent law and source disk.

This is the relevant warning for a product small-field cutoff. If an
unnormalized vacuum sector needs the raw mass, the natural target is an
extensive/quasilocal expansion for its logarithm, not a volume-independent
positive lower bound.

## SU(2) plaquette specialization

For

\[
s(U_p)=1-\tfrac12\operatorname{ReTr}U_p
\]

on \(SU(2)\), \(0\le s(U_p)\le2\). Hence for

\[
\mathcal O_f(U)=4\sum_p f_p s(U_p)
\]

the range diameter obeys

\[
D_f\le8\sum_p|f_p|.
\tag{14}
\]

The same group bound also gives the absolute estimate

\[
\|\mathcal O_f\|_\infty\le8\sum_p|f_p|,
\qquad
\left|\mathbb E_\nu\mathcal O_f\right|
\le8\sum_p|f_p|.
\tag{15}
\]

For any Program 003 application satisfying (1) with a named pointwise kernel,
(5) therefore supplies the common disk

\[
|z|<\frac{\log 2}{4\sum_p|f_p|}
\tag{16}
\]

when \(f\ne0\) and the denominator is nonzero; for \(f=0\), the ratio is one.
For profiles supported in one fixed-\(L\)
coarse block with a norm controlling \(\|f\|_\infty\), the number of fine
plaquettes is a constant depending on \(L\), not on the torus size, cutoff
step, source location, coarse field, or conditional law. Equation (16) then
gives a uniform source-only zero-free disk.

This does **not** construct the full Eq. (2.9) kernel. It gives no complex
coarse-field neighborhood, source-marked polymer representation, mixing
classification, quasilocality, large-field estimate, RG iteration, continuum
limit, or mass gap. Those remain the content of Programs 002–003 and later
bridges.

## Falsification checks

- Multiply a raw kernel by \(A(V)\) and verify that its mass changes while
  every normalized source ratio remains fixed.
- Use the product restriction (13) and verify exponential raw-mass decay
  despite pointwise positivity and unit normal Jacobian.
- On an equally weighted two-point fiber with values \(0,D\), locate zeros at
  \(z=(2k+1)\pi i/D\); the proved disk lies strictly inside the first zero.
- Let the observable range grow with the regulator and observe that no common
  disk follows.
- Let the pulled-back domain move with \(V\) and check that (12) acquires a
  boundary term.
- Keep total mass constant while oscillating the normalized density in \(V\);
  this refutes any attempt to infer normalized locality from raw mass alone.
