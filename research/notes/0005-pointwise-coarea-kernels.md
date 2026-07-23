# Note 0005: pointwise coarea kernels for finite block maps

Claim ID: YM-RG-005

Kind: Lemma derived from standard geometric-measure results

Evidence: E2 (finite-dimensional auxiliary result; internally checked only)

Novelty: none claimed

## Imported results

This note uses two standard finite-dimensional results.

1. The smooth coarea formula, in the normal-Jacobian convention used below.
   A directly accessible statement and proof are Eqs. (A-1)–(A-2), pp. 59–61,
   of Ralph Howard's [*The Kinematic Formula in Riemannian Homogeneous
   Spaces*](https://doi.org/10.1090/memo/0509). Federer's general version is
   in Sections 3.2.20–3.2.22 of [*Geometric Measure
   Theory*](https://doi.org/10.1007/978-3-642-62010-2).
2. Ehresmann's theorem that a proper surjective smooth submersion is a smooth
   locally trivial fiber bundle. An accessible proof is Lemma 9.2 of
   Kolář–Michor–Slovák, [*Natural Operations in Differential
   Geometry*](https://www.maths.tcd.ie/EMIS/monographs/KSM/kmsbookh.pdf).

No assertion that Bałaban's Eq. (0.12) map satisfies the hypotheses is imported
or proved here.

## Statement

Let \(M^m\) and \(N^n\), \(m\ge n\), be second-countable smooth Riemannian
manifolds without boundary. Let

\[
d\mu_M=\rho_M\,d\operatorname{vol}_M,
\qquad
d\mu_N=\rho_N\,d\operatorname{vol}_N,
\]

where \(\rho_M,\rho_N\) are smooth and strictly positive. Suppose
\(F:M\to N\) is a smooth, proper, surjective submersion. Define the normal
Jacobian

\[
J_F(u)=\det\!\left(dF_u dF_u^*\right)^{1/2}>0.
\]

For \(v\in N\) and Borel \(A\subseteq M\), set

\[
K_F(v,A)=
\int_{A\cap F^{-1}(v)}
\frac{\rho_M(u)}{\rho_N(v)J_F(u)}
\,d\operatorname{vol}_{F^{-1}(v)}(u).
\tag{1}
\]

Then:

1. \(K_F(v,\cdot)\) is a finite nonzero positive Radon measure supported on
   \(F^{-1}(v)\) for every \(v\), not merely for almost every \(v\).
2. \(K_F\) is a Borel measure kernel and, for every nonnegative Borel
   \(\varphi\),

   \[
   \int_M\varphi\,d\mu_M
   =\int_N\left[\int_M\varphi(u)K_F(v,du)\right]d\mu_N(v).
   \tag{2}
   \]

3. For every \(a\in C^\infty(M)\), the function
   \(v\mapsto K_F(v,a)\) is smooth. Thus
   \(m_F(v)=K_F(v,M)\) is smooth and strictly positive, and

   \[
   \widehat K_F(v,du)=m_F(v)^{-1}K_F(v,du)
   \]

   is an everywhere-defined conditional probability kernel. If \(N\) is
   compact, \(m_F\) has positive finite uniform lower and upper bounds.

If a compact Lie group \(H\) acts isometrically on \(M,N\), preserves both
weighted measures, and \(F(hu)=hF(u)\), then

\[
K_F(hv,hA)=K_F(v,A).
\tag{3}
\]

No freeness of the \(H\)-actions is required.

## Proof

Because every value is regular, the preimage theorem makes \(F^{-1}(v)\) a
smooth embedded \((m-n)\)-manifold. Surjectivity makes it nonempty and
properness makes it compact. The density in (1) is continuous and strictly
positive on that compact fiber. A nonempty compact Riemannian manifold has
finite positive volume; in dimension zero the induced volume is counting
measure. This proves pointwise finiteness and nonzeroness.

The smooth coarea formula is

\[
\int_M h(u)J_F(u)\,d\operatorname{vol}_M(u)
=\int_N\left[\int_{F^{-1}(v)}h(u)
\,d\operatorname{vol}_{F^{-1}(v)}(u)\right]
d\operatorname{vol}_N(v).
\tag{4}
\]

Apply (4) to
\(h=\varphi\rho_M/J_F\), and use
\(d\operatorname{vol}_N=\rho_N^{-1}d\mu_N\). This gives (2) with exactly the
density in (1).

For regularity, Ehresmann's theorem gives, near each \(v_0\), a compact smooth
fiber \(Q\), an open \(U\ni v_0\), and a fiber-preserving diffeomorphism

\[
\Psi:U\times Q\longrightarrow F^{-1}(U).
\]

Pulling (1) through \(\Psi\) writes \(K_F(v,a)\) as the integral over fixed
compact \(Q\) of a smooth density. Differentiation under that integral proves
smoothness to every order. The same local representation, first for
rectangles and then by a monotone-class argument, gives the Borel-kernel
property. If \(N\) is compact, the extreme-value theorem applied to the smooth
positive function \(m_F\) gives the uniform bounds.

For (3), equivariance gives

\[
dF_{hu}\,dh_u=dh_{F(u)}\,dF_u.
\]

The two action differentials are isometries, so \(J_F(hu)=J_F(u)\). The action
maps \(F^{-1}(v)\) isometrically onto \(F^{-1}(hv)\) and preserves the weight;
a change of variables in (1) proves covariance. \(\square\)

## Exact group-delta meaning

Take \(M,N\) to be finite products of compact Lie groups with normalized Haar
measures and invariant metrics. If the group delta is normalized relative to
\(d\mu_N\), then for every smooth \(\varphi\), \(K_F(v,\varphi)\) is the
distinguished pointwise representative of

\[
\int_M\varphi(u)\,\delta_N(F(u)v^{-1})\,d\mu_M(u).
\]

Indeed, for every smooth test function \(\psi\), Eq. (2) gives

\[
\int_N\psi(v)K_F(v,\varphi)\,d\mu_N(v)
=\int_M\varphi(u)\psi(F(u))\,d\mu_M(u).
\]

Ordinary measure disintegration alone would instead give conditional
probabilities only \(F_*\mu_M\)-almost everywhere. It also hides the raw
pushforward density

\[
m_F(v)=K_F(v,M),
\qquad
K_F(v,\varphi)=m_F(v)
\mathbb E_{\widehat K_F(v)}[\varphi].
\]

The factor \(m_F\) cancels in a normalized source ratio when it is positive,
but it may not be silently set to one.

## Fixed sharp restriction

For a Borel set \(C\subseteq M\), define

\[
K_F^C(v,A)=K_F(v,A\cap C).
\tag{5}
\]

This is a finite positive kernel and disintegrates the measure
\(\mathbf1_Cd\mu_M\). Its mass is nonzero at \(v\) exactly when

\[
\int_{C\cap F^{-1}(v)}
\frac{\rho_M(u)}{\rho_N(v)J_F(u)}
\,d\operatorname{vol}_{F^{-1}(v)}(u)>0.
\tag{6}
\]

Mere nonempty intersection is insufficient: one point has zero measure in a
positive-dimensional fiber. A sufficient condition is that
\(C\cap F^{-1}(v)\) contain a nonempty relatively open subset for every \(v\).
If \(C\) is \(H\)-invariant, (3) survives. If \(C\) is independent of coupling
and source, their derivatives create no cutoff derivative.

A sharp fixed indicator can still destroy smooth coarse dependence because its
boundary may move in a local fiber chart. For the fixed-domain route used in
Program 003, smoothness follows if the restriction has product form
\(\Psi(U\times C_0)\), up to fiber-null sets, with a common dominated
differentiation bound. Coarea alone gives no complex analyticity. A sufficient
holomorphic route additionally requires a holomorphic extension of the
pulled-back integrand and density to a common complex neighborhood and an
integrable majorant on each compact complex subdomain. A genuinely analytic
moving domain could instead be straightened first; a fixed domain is not
logically necessary in every formulation.

By contrast, if the restricted mass is finite and nonzero and a source
observable \(\mathcal O\) is bounded, then pointwise source analyticity is
immediate:

\[
Z_v(z)=\int e^{-z\mathcal O(u)}K_F^C(v,du)
\]

is entire, because
\(|e^{-z\mathcal O(u)}|\le e^{|z|\|\mathcal O\|_\infty}\).

## Boundary of applicability

For a block map defined only on an open regular chart \(W\subset M\), the same
argument applies to a restriction only after proving:

- \(dF\) is surjective on a neighborhood of the cutoff support;
- the weighted support is proper over the admitted coarse patch;
- Eq. (6) is positive for every admitted coarse field;
- the closure of the cutoff support remains inside the logarithm and
  gauge-chart domains and away from rank boundaries and Jacobian zeros;
- any claimed covariance is implemented by the chart or is restricted to
  gauge-invariant integrals on a fixed slice.

Compactness of the full product group does not supply these local facts. A
proper surjective map without the submersion condition is also insufficient.
For example, the degree-one map
\(F(e^{it})=e^{i(t+\sin t)}\) from \(S^1\) to \(S^1\) is smooth, proper, and
surjective, but its derivative vanishes at \(t=\pi\).

## Consequence for Program 003

This lemma reduces the formal-delta issue to explicit geometry. Note 0006
separately verifies a local Eq. (0.12) submersion and positive precompact fiber
ball at each admitted background. Program 003 must still extend that chart to a
complete named restricted kernel, prove positive fiber volume for every field
in its exact scope, and keep the positive normal Jacobian away from zero on the
whole chosen support. If an analytic coordinate determinant is retained as in
RG I, its nonvanishing and real orientation are a separate obligation. This
note itself proves no map-specific fact, large-field statement, continuum
construction, or mass gap.

## Falsification checks

- Use \(F(e^{it})=e^{i(t+\sin t)}\) and observe failure of the submersion
  hypothesis at \(t=\pi\).
- Normalize the conditional probability prematurely and recover the missing
  factor \(m_F(v)=K_F(v,M)\), the raw transform of the constant function one.
- Intersect a positive-dimensional fiber at one point and verify that the
  restricted mass is still zero.
- Use a sharp cutoff with a moving fiber boundary and check that coarse
  smoothness can fail.
- Break equivariance or measure invariance and verify that kernel covariance no
  longer follows.
- Approach a logarithm/chart boundary and verify that compactness of the full
  group does not prevent the local Jacobian from degenerating.
