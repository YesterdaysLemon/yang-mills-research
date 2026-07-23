# Note 0034: transported curl closure and physical-width quotient extension

Claim ID: YM-RG-034

Kind: finite-regulator algebraic norm equivalence, quotient-extension theorem,
and sharp collar-width obstruction

Evidence: E2 (exact transported plaquette algebra and finite-dimensional
cutoff proof; the physical kernel corollaries retain explicit source-row,
scale-envelope, and real-center hypotheses)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Gauge Fixing Conditions and the Infrared Problem of Lattice
  Gauge Theories*](https://doi.org/10.1007/BF01466594), especially Eq. (1.1)
  on printed p. 76, Eq. (1.36) on printed p. 82, and Eqs. (1.47)--(1.50) on
  printed pp. 84--85;
- T. Balaban, [*Renormalization group approach to lattice gauge field
  theories I*](https://doi.org/10.1007/BF01215223), especially condition
  (ii), Eq. (1.13), on printed p. 262;
- Notes 0031 and 0033.

The inspected local PDFs have SHA-256 values

```text
Gauge-fixing paper
7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB

RG I
1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
```

## Scope and the two norms

Everything is at finite regulator. Retain Note 0031's common real-center
hypothesis \((\mathrm H_{\rm rc})\), its faithful unitary representation,
\(0<\xi\le1\), and its relative-log chart. Thus

\[
|d\bar U(p)-1|_{\rm RG}
\le
\bar a_U\xi^2
\tag{1}
\]

at every retained plaquette. Let

\[
c_{\rm op\leftarrow RG}
:=
\sup_{M\ne0}
\frac{\lVert M\rVert_{\rm op}}{|M|_{\rm RG}}
<\infty
\tag{2}
\]

for the fixed finite-dimensional matrix convention. Compactness of the real
group also gives

\[
c_{\rm Ad}^{\rm RG}
:=
\sup_{\substack{g\in G\\M\ne0}}
\frac{|\operatorname {Ad}_gM|_{\rm RG}}{|M|_{\rm RG}}
<\infty.
\tag{3}
\]

The second constant is \(1\) if the retained RG norm is
\(\operatorname {Ad}G\)-invariant.

For a complexified bond field \(a\), put

\[
\begin{aligned}
\lVert a\rVert_Y
:=
\max\{&
\lVert a\rVert_{\infty,{\rm RG}},
\lVert\nabla_{\bar U}^{\xi}a\rVert_{\infty,{\rm RG}}
\},
\end{aligned}
\tag{4}
\]

and recall Note 0031's complete norm

\[
\begin{aligned}
\lVert a\rVert_X
:=
\max\{&
\lVert a\rVert_{\infty,{\rm RG}},
\lVert\nabla_{\bar U}^{\xi}a\rVert_{\infty,{\rm RG}},\\
&
\lVert a\rVert_{\infty,{\rm op}},
\lVert\mathcal D_{\bar U}^{\xi}a\rVert_{\infty,{\rm op}}
\}.
\end{aligned}
\tag{5}
\]

Balaban's Eq. (1.1), applied componentwise to a bond field, fixes the
two-point covariant-gradient row

\[
(D_{\bar U,\mu}^{\xi}a_\nu)(x)
=
\xi^{-1}
\left[
\operatorname {Ad}_{\bar U_\mu(x)}
a_\nu(x+\xi e_\mu)
-a_\nu(x)
\right].
\tag{6}
\]

Equation (1.50) uses precisely these component derivatives. The collection
of rows (6) is the \(\nabla_{\bar U}^{\xi}\) entry in (4)--(5).

## Exact transported curl identity

Fix the positively oriented plaquette \(p_{\mu\nu}(x)\). Abbreviate its four
positive-link variables by

\[
\begin{aligned}
U_1&=\bar U_\mu(x),&
U_2&=\bar U_\nu(x+\xi e_\mu),\\
U_3&=\bar U_\mu(x+\xi e_\nu),&
U_4&=\bar U_\nu(x),
\end{aligned}
\tag{7}
\]

and put

\[
P
=
U_1U_2U_3^{-1}U_4^{-1}
=
d\bar U(p).
\tag{8}
\]

Define the two forward transports

\[
\begin{aligned}
T_\mu a_\nu(x)
&=
\operatorname {Ad}_{U_1}
a_\nu(x+\xi e_\mu),\\
T_\nu a_\mu(x)
&=
\operatorname {Ad}_{U_4}
a_\mu(x+\xi e_\nu).
\end{aligned}
\tag{9}
\]

Note 0031's reverse-link convention and prefix transport give the four
linear factors in its Eq. (8):

\[
\begin{aligned}
X_1&=a_\mu(x),\\
X_2&=T_\mu a_\nu(x),\\
X_3&=-\operatorname {Ad}_{U_1U_2U_3^{-1}}
       a_\mu(x+\xi e_\nu)
     =-\operatorname {Ad}_P T_\nu a_\mu(x),\\
X_4&=-\operatorname {Ad}_P a_\nu(x).
\end{aligned}
\tag{10}
\]

Consequently,

\[
\begin{aligned}
\sum_{\ell=1}^4X_\ell
={}&
\xi
\left[
D_{\bar U,\mu}^{\xi}a_\nu
-D_{\bar U,\nu}^{\xi}a_\mu
\right]\!(x)\\
&+
\left(I-\operatorname {Ad}_P\right)
\left[
a_\nu(x)+T_\nu a_\mu(x)
\right].
\end{aligned}
\tag{11}
\]

Since Note 0031 defines
\(\mathcal D_{\bar U}^{\xi}a=\xi^{-1}\sum_\ell X_\ell\), this proves the exact
identity

\[
\boxed{
\begin{aligned}
\mathcal D_{\bar U}^{\xi}a(p)
={}&
\left[
D_{\bar U,\mu}^{\xi}a_\nu
-D_{\bar U,\nu}^{\xi}a_\mu
\right]\!(x)\\
&+
\xi^{-1}
\left(I-\operatorname {Ad}_{d\bar U(p)}\right)
\left[
a_\nu(x)+T_\nu a_\mu(x)
\right].
\end{aligned}
}
\tag{12}
\]

This is the normalization needed by Note 0033. It is compatible with the
gauge-fixing paper's Eq. (1.47), whose linear plaquette increment is
\(i\xi^2D_{\bar U}^{\xi}a\), and with Eqs. (1.49)--(1.50), which separate
the first-order curl from quadratic commutator terms.

## The complete norm is equivalent to the printed two-feature norm

For unitary \(P\),

\[
\left\|
I-\operatorname {Ad}_P
\right\|_{{\rm op}\to{\rm op}}
\le
2\lVert P-1\rVert_{\rm op}.
\tag{13}
\]

Equations (1)--(2), unitary invariance of the operator norm, and (12) give

\[
\begin{aligned}
\lVert\mathcal D_{\bar U}^{\xi}a(p)\rVert_{\rm op}
&\le
2c_{\rm op\leftarrow RG}
\lVert\nabla_{\bar U}^{\xi}a\rVert_{\infty,{\rm RG}}\\
&\quad+
4c_{\rm op\leftarrow RG}^2
\bar a_U\xi
\lVert a\rVert_{\infty,{\rm RG}}.
\end{aligned}
\tag{14}
\]

Set

\[
C_{\rm eq}(\xi)
=
\max\left\{
1,\
2c_{\rm op\leftarrow RG}
+4c_{\rm op\leftarrow RG}^2\bar a_U\xi
\right\},
\tag{15}
\]

and

\[
C_{\rm eq}
=
\max\left\{
1,\
2c_{\rm op\leftarrow RG}
+4c_{\rm op\leftarrow RG}^2\bar a_U
\right\}.
\tag{16}
\]

The raw operator row is bounded by
\(c_{\rm op\leftarrow RG}\lVert a\rVert_{\infty,{\rm RG}}\), which is already
dominated by (15). Therefore

\[
\boxed{
\lVert a\rVert_Y
\le
\lVert a\rVert_X
\le
C_{\rm eq}(\xi)\lVert a\rVert_Y
\le
C_{\rm eq}\lVert a\rVert_Y.
}
\tag{17}
\]

Thus the raw-operator and covariant-curl entries in Note 0031's norm are
essential for the transparent curvature proof but are not independent
source-kernel rows under \((\mathrm H_{\rm rc})\). Balaban's printed raw and
covariant-gradient pair suffices after the still-required chart conversion.
No \(D^*D K\) or \(\Delta K\) row is used in (12)--(17).

## Reduced converted source-row hypothesis

Let \(\Sigma^{01}\) contain only the translated raw-RG and
covariant-gradient-RG rows in (4), with their tagged multiscale anchors.
Replace Note 0033's four-feature hypothesis by:

**Reduced converted row hypothesis
\((\mathrm H_{01}^U)\).** For every retained source-density column
\(A_\alpha\) and every \(\sigma\in\Sigma^{01}\),

\[
\boxed{
\lVert T_\sigma^{01}A_\alpha\rVert
\le
C_{\chi,U}E_{01,\sigma}(j_\sigma)
\mu_\alpha^{-1}
e^{-\lambda_U
d_{\widetilde{\mathcal B}}
(\widetilde y_\sigma,\widetilde y_\alpha)}.
}
\tag{18}
\]

This is still a genuine hypothesis. It requires the differential of the
exponential, gauge restoration, source components, common chart constants,
and the converted covariant-gradient row. Equation (17) removes the need for
separate raw-operator and curl rows.

If

\[
\overline E_{01}^{\rm glob}
:=
\sup_{\mathfrak r,p,(\bar U,J_0),\sigma\in\Sigma^{01}}
E_{01,\sigma}(j_\sigma)
<\infty,
\tag{19}
\]

then Note 0033's unweighted proof and (17) give

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\frac{
C_{\rm eq}C_{\chi,U}c_1(1/8)
\overline E_{01}^{\rm glob}B_{\rm conn}
}{r_U}.
\end{aligned}
}
\tag{20}
\]

The strengthened separated-cell premise of Propagators II remains in force.

## The gradient graph and exact cutoff product rule

Let \(G_\nabla\) be the undirected graph whose vertices are the chosen
independent bonds. Join \(b\) and \(b'\) when one row of (6), after applying
the reverse-orientation convention if necessary, compares their values.
Write \(d_\nabla\) for graph distance, with
\(d_\nabla(b,I)=+\infty\) on a connected component disjoint from \(I\).

For a nonempty active set \(I\) and an integer \(m\ge1\), define

\[
V_m(I)
=
\{b:d_\nabla(b,I)<m\},
\qquad
\chi_{I,m}(b)
=
\left(
1-\frac{d_\nabla(b,I)}m
\right)_+.
\tag{21}
\]

Use the same scalar cutoff on reverse orientations. Then
\(\chi_{I,m}=1\) on \(I\), vanishes outside \(V_m(I)\), and changes by at
most \(1/m\) across an edge of \(G_\nabla\). On a component disjoint from
\(I\), the convention in (21) is \(\chi_{I,m}=0\).

For one oriented gradient row comparing \(b\) and \(b'\), Balaban's Eq.
(1.1) gives either of the exact product-rule forms

\[
\begin{aligned}
\nabla_{\bar U}^{\xi}(\chi a)(b,b')
={}&
\chi(b)\nabla_{\bar U}^{\xi}a(b,b')\\
&+
\xi^{-1}
\bigl(\chi(b')-\chi(b)\bigr)
\operatorname {Ad}_{g_{b'b}}a(b')\\
={}&
\chi(b')\nabla_{\bar U}^{\xi}a(b,b')\\
&+
\xi^{-1}
\bigl(\chi(b')-\chi(b)\bigr)
a(b),
\end{aligned}
\tag{22}
\]

Here \(g_{b'b}\in G\) is the real background transport in that row. The two
displayed forms let either endpoint carry the original-gradient
coefficient; the reverse-oriented row obeys the corresponding identity
after interchanging the endpoints and inverting the transport.

Define the minimal two-feature collar

\[
\begin{aligned}
\Sigma_{I,m}^{01}
=&
\{\hbox{raw-RG row at }b:b\in V_m(I)\}\\
&\cup
\{\hbox{gradient-RG row on }\{b,b'\}:
b,b'\in V_m(I)\}.
\end{aligned}
\tag{23}
\]

If a gradient row crosses from \(V_m(I)\) to its complement, use (22) with
the zero-cutoff endpoint as the coefficient. Only the raw value at the
inside endpoint remains. Rows with both endpoints outside vanish. Hence,
for \(b=\chi_{I,m}a\),

\[
\lVert b\rVert_Y
\le
\left(
1+\frac{c_{\rm Ad}^{\rm RG}}{m\xi}
\right)
\max_{\sigma\in\Sigma_{I,m}^{01}}
\lVert T_\sigma^{01}a\rVert.
\tag{24}
\]

Because \(b|_I=a|_I\), it is an admissible representative of \(Q_Ia\).
Combining (17) and (24) proves

\[
\boxed{
\lVert Q_Ia\rVert_{X/N_I}
\le
C_{\rm eq}(\xi)
\left(
1+\frac{c_{\rm Ad}^{\rm RG}}{m\xi}
\right)
\max_{\sigma\in\Sigma_{I,m}^{01}}
\lVert T_\sigma^{01}a\rVert.
}
\tag{25}
\]

This is a proved instance of Note 0033's
\((\mathrm H_{\rm ext}^U)\). It is a quotient estimate using the local germ
of the given representative. It does not assert a linear right inverse from
arbitrary restriction data.

## Uniform physical-width collar

Fix a physical collar thickness \(\rho>0\) in the units in which one
gradient edge has length \(\xi\), and put

\[
m_\rho(\xi)
=
\left\lceil\frac{\rho}{\xi}\right\rceil.
\tag{26}
\]

Then \(m_\rho(\xi)\xi\ge\rho\), so (25) gives the common bound

\[
\boxed{
\lVert Q_Ia\rVert_{X/N_I}
\le
C_{\rm ext}(\rho)
\max_{\sigma\in\Sigma_{I,m_\rho(\xi)}^{01}}
\lVert T_\sigma^{01}a\rVert,
\qquad
C_{\rm ext}(\rho)
=
C_{\rm eq}
\left(
1+\frac{c_{\rm Ad}^{\rm RG}}{\rho}
\right).
}
\tag{27}
\]

The constant is independent of regulator, center, branch, support,
disconnectedness, and local topology, once \((\mathrm H_{\rm rc})\) and the
fixed norm conventions hold. The number of lattice layers grows like
\(\xi^{-1}\). If the collar fills a small finite regulator, the estimate
remains true but its source-distance anchor may become global and therefore
weaker.

## Fixed lattice-layer collars cannot be uniform

The \((m\xi)^{-1}\) term is order-sharp. First work in the normalized scalar
\(U(1)\) model, with both retained scalar matrix norms equal to absolute
value, and take a flat longitudinal field in dimension \(d\ge2\):

\[
a_1(x)=f(x_1),
\qquad
a_\nu(x)=0\quad(\nu\ne1),
\tag{28}
\]

with no transverse dependence. Every plaquette curl vanishes, while the
nonzero gradient rows include

\[
\xi^{-1}\bigl(f(i+1)-f(i)\bigr).
\tag{29}
\]

On the path \(\{0,\ldots,N\}\), take active endpoint values
\(f(0)=1\), \(f(N)=-1\). Every extension satisfies, by telescoping,

\[
\max_i
\xi^{-1}|f(i+1)-f(i)|
\ge
\frac2{N\xi}.
\tag{30}
\]

Linear interpolation attains this lower bound and has raw norm \(1\).
Therefore the exact quotient norm is

\[
\boxed{
\lVert Q_If\rVert
=
\max\left\{
1,\frac2{N\xi}
\right\}.
}
\tag{31}
\]

The same obstruction embeds in an abelian direction of any fixed compact
matrix group. If \(H\ne0\) is the chosen commuting generator, the exact
formula before scalar normalization is
\[
\max\left\{
\max\{|H|_{\rm RG},\lVert H\rVert_{\rm op}\},
\frac{2|H|_{\rm RG}}{N\xi}
\right\}.
\]
Its fixed norm constants do not affect the inverse-mesh divergence or the
collar-width conclusion.

Now take \(N=2m+1\) and choose an original global representative with

\[
f(i)=
\begin{cases}
1,&i\le m,\\
-1,&i\ge m+1.
\end{cases}
\tag{32}
\]

Both endpoints of its single jump have distance \(m\) from
\(I=\{0,N\}\), so neither belongs to \(V_m(I)\). Every feature in (23) has
size at most \(1\), but

\[
\lVert Q_If\rVert
=
\max\left\{
1,\frac2{(2m+1)\xi}
\right\}.
\tag{33}
\]

Thus no extension inequality using a uniformly bounded number of gradient
layers can have a regulator-uniform constant for arbitrary active sets.
The physical-width choice \(m\asymp\rho/\xi\) is necessary up to constants.
This obstruction retains the full curl norm: the chosen longitudinal
abelian sector has curl exactly zero.

## Positive-distance physical-\(U\) corollary

For each nonempty completed active set
\(I=I_{U,p,s}^{\rm conn}(R)\), choose the physical-width collar (23), (26)
and the tagged anchor set

\[
S_{p,s,R}^{U,\rho}
=
\left\{
\widetilde y_\sigma:
\sigma\in
\Sigma_{I_{U,p,s}^{\rm conn}(R),m_\rho(\xi)}^{01}
\right\}.
\tag{34}
\]

Assume the completed reduced-row envelope

\[
\overline E_{01}^{\rm conn,\rho}
:=
\sup_{\substack{
\mathfrak r,p,(\bar U,J_0),s,R\\
\sigma\in
\Sigma_{I_{U,p,s}^{\rm conn}(R),m_\rho(\xi)}^{01}}}
E_{01,\sigma}(j_\sigma)
<\infty.
\tag{35}
\]

For

\[
0\le\gamma<\frac{\delta_0}{8},
\qquad
\alpha_\gamma
=
\frac18-\frac{\gamma}{\delta_0}>0,
\tag{36}
\]

the reduced source rows (18), featurewise Propagators-II convolution, and
(27) bound Note 0033's sharp quotient moment by

\[
\boxed{
\mathfrak M_{U,\gamma}
\left(
I,S_{p,s,R}^{U,\rho}
\right)
\le
C_{\rm ext}(\rho)
C_{\chi,U}
c_1(\alpha_\gamma)
\overline E_{01}^{\rm conn,\rho}.
}
\tag{37}
\]

Inserting (37) into Note 0033 Eq. (30) gives

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(\bar U,J_0)\in\mathfrak K_p^{\rm rc}}
\sum_s
\sum_{\substack{R\supset\widehat Q_{p,s}\\
I_{U,p,s}^{\rm conn}(R)\ne\varnothing}}
e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
e^{\gamma
d_{\widetilde{\mathcal B}}
(S_{p,s,R}^{U,\rho},\widetilde y_\alpha)}
\left|
\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)
\right|\\
&\qquad\le
\frac{
C_{\rm ext}(\rho)
C_{\chi,U}
c_1(\alpha_\gamma)
\overline E_{01}^{\rm conn,\rho}
B_{\rm conn}
}{r_U}.
\end{aligned}
}
\tag{38}
\]

There is no feature-cardinality, support-cardinality, bond-volume, mesh, or
branch factor. The full polymer exponent \(\kappa\) is retained. The collar
has a common physical width, not a common number of lattice layers.

Returning from \(S_{p,s,R}^{U,\rho}\) to the exact active-bond labels still
requires a metric comparison for a collar of \(m_\rho(\xi)\) gradient steps.
If the tagged metric counts unscaled lattice layers, the corresponding halo
can grow like \(\xi^{-1}\). No uniform active-label or marked-plaquette
corollary is claimed without that crosswalk.

## Scale-envelope boundary

Equations (17) and (27) remove the independent curl-row and extension
premises, but they do not remove the output-scale factors in Eq. (190).
The raw and gradient shapes remain

\[
(L^j\eta)^{-1},
\qquad
(L^j\eta)^{-2}.
\tag{39}
\]

The source measure
\(\mu_\alpha=(L^{j'}\eta)^d\) cancels Eq. (190)'s input-density factor
\((L^{j'}\eta)^{-d}\); it does not cancel either output-scale factor in
(39). Nor does setting \(\eta=\xi\) supply an unused power: the chart tangent
is already normalized by
\(D\mathcal U=i\xi A\,\mathcal U\), and the present chart and
gauge-restoration hypotheses are bounded rather than scale gaining.

Thus a candidate envelope
\(C_{U,1}(L^j\eta)^{-1}+C_{U,2}(L^j\eta)^{-2}\) can still diverge when the
smallest retained output scale tends to zero. A regulator-uniform physical
theorem needs either the matching scaled source/output norm, a cancellation
not used here, or a separate proof that the completed family never takes the
unweighted supremum over those fine rows. This note does not hide that issue
inside \(C_{\rm eq}\) or \(C_{\rm ext}(\rho)\).

## Exact boundary

- Equation (12) is an exact finite-dimensional transported identity with the
  \(\xi^{-1}\) normalization used by Note 0031.
- Equation (17) proves that, under the real curvature margin, the complete
  four-entry norm is uniformly equivalent to Balaban's raw-plus-gradient
  pair. The printed \(D^*D K\) and \(\Delta K\) rows are not used.
- Equation (27) proves a common quotient-extension constant for collars of
  fixed physical width. Equation (33) disproves a common bounded-layer
  constant for arbitrary active sets.
- Equations (20) and (38) remain conditional on
  \((\mathrm H_{\rm rc})\), the reduced converted source rows, the relevant
  common scale envelopes, and the strengthened separated-cell premise.
- Feature-collar anchoring is proved. Active-bond anchoring still needs a
  multiscale metric halo for \(m_\rho(\xi)\) layers; marked-plaquette
  anchoring still needs the downstream endpoint budget.
- No common converted raw/gradient rows, regulator-uniform scale envelope,
  physical-family real centers, nonzero-source polymer activities, raw-law
  comparison, unit translations, large-field estimate, RG iteration,
  continuum or infinite-volume construction, Osterwalder--Schrader
  reconstruction, infrared decay, or Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Omit the curvature correction in (12) when \(d\bar U(p)\ne1\).
- Lose the factor \(\xi^{-1}\) in Note 0031's curl definition.
- Use complex rather than real/unitary background transports in (13).
- Bound the curl by raw \(K\) alone and omit the converted gradient row.
- Substitute the printed \(D^*D K\) or \(\Delta K\) row for (12).
- Use zero extension or a fixed lattice-layer cutoff and suppress the
  \(1/(m\xi)\) term.
- Exclude gradient rows with both endpoints in \(V_m(I)\), or omit the raw
  inside endpoint needed for a boundary-crossing row.
- Claim that a collar of \(\lceil\rho/\xi\rceil\) lattice layers has a
  common unscaled tagged-metric halo without proving the metric crosswalk.
- Hide the possible divergence of the raw/gradient scale envelope inside a
  chart, norm-equivalence, or extension constant.
- Promote (20) or (38) to an unconditional physical first jet, continuum
  construction, infrared theorem, or Yang--Mills mass gap.
