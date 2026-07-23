# Balaban RG-II conditioned-mark routing audit

Date: 2026-07-23

Scope: RG II Eqs. (2.3), (2.5), (2.6), (2.8), and (2.14), with one
repository-supplied localized plaquette mark inserted before Section 2.

Primary source: T. Balaban, *Renormalization Group Approach to Lattice Gauge
Field Theories. II. Cluster Expansions*,
[Project Euclid PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf).

Audited file SHA-256:

```text
EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC
```

## Why this audit was necessary

Earlier repository text used the schematic post-conditioning argument

\[
W_{k,p}\bigl(A,\mathfrak B_{Z_0}(\sigma;B,X)\bigr)
\]

and therefore treated the unbounded standardized Gaussian \(X\) as an
obstruction to inheriting the local Eq. (1.34) marked domain. Direct
inspection of the immutable pages shows that this is not the variable map in
Balaban's conditioned representation. The localized factor remains a
function of the conditional interior field \(B\). This audit records the
correction before any marked estimate is made.

## Immutable page map

| Formula | Printed page | One-based PDF page |
|---|---:|---:|
| (2.3), (2.5) | 12 | 12 |
| (2.6) | 12--13 | 12--13 |
| (2.8) | 14 | 14 |
| (2.14), (2.15) | 15 | 15 |

All formula glyphs used below were checked against 8x page renders. The
source does not label the paths or radii of the \(\sigma\)- and
\(\tau\)-contours inside Eq. (2.14); no radius is inferred from that display
alone.

## The cutoff split

Immediately before Eq. (2.3), Balaban defines

\[
Y_0^{c*}
=
\{b\in T^{(k)}:b\subset Y_0^c\}
\setminus
\{b_0(c):c\in T^{(k+1)}\}.
\]

The displayed decomposition is

\[
\chi_k
=
\chi_{k,Y_0}\chi_{k,Y_0^c}
=
\sum_{P\subset Y_0^{c*}}
(-1)^{|P|}
\chi_{k,Y_0}\chi^c_{k,P},
\]

\[
\chi^c_{k,P}
=
\prod_{b\in P}
\chi\!\left(
\left\{|B(b)|\ge\frac{\varepsilon _1}{g_k}\right\}
\right).
\tag{2.3}
\]

The global cutoff is the product of the small-field indicators on the
independent bonds. Hence its factor \(\chi_{k,Y_0}\) controls every such bond
in \(Y_0\). The paper then takes the smallest \(Z_0\in\mathcal D_k\)
containing \(Y_0\) and \(P\), with every bond of \(P\) in the interior of
\(Z_0\).

For the marked repository construction the seed is rerun as

\[
Y_0^\bullet=A\cup\bigcup_{Y\in D}Y.
\tag{A1}
\]

Write
\[
I_k(A):=\{b\in I_k:b\subset\operatorname{int}A\}.
\]
If the independent-coordinate dependency set satisfies
\[
\operatorname{Dep}_B W_{k,p}(A)\subset I_k(A),
\]
then every field coordinate used by the mark is controlled by
\(\chi_{k,Y_0^\bullet}\). This formulation explicitly excludes the
distinguished \(b_0(c)\) coordinates omitted from \(I_k\).

## Conditioning does not shift the localized factor

Equation (2.5) splits the original Gaussian into an exterior field \(B'\)
and a conditional interior field \(B\). Its final line has the form

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
\\
&\qquad\cdot
\int d\mu_{C^{(k)}(Z_0)}(B)\,
\exp\!\left[
-\left\langle
Z_0^cB',C^*\Delta_kCZ_0B
\right\rangle
\right]
F(Z_0,B).
\tag{2.5}
\end{aligned}
\]

The source then makes only the exterior change of variables

\[
B'=(C^{(k)})^{1/2}X.
\]

Equation (2.6) consequently contains

\[
\begin{aligned}
&\int d\mu_0(X)\,
\exp\!\left[-\frac12\langle\cdots X,\cdots X\rangle\right]
\\
&\qquad\cdot
\int d\mu_{C^{(k)}(Z_0)}(B)\,
\exp\!\left[
-\left\langle
B,C^*\Delta_kCZ_0^c(C^{(k)})^{1/2}X
\right\rangle
\right]
F(Z_0,B).
\tag{2.6}
\end{aligned}
\]

Thus:

- \(X\) is the standardized exterior variable;
- \(B\) is the conditional interior integration variable;
- \(X\) couples linearly to \(B\) in the density; and
- \(F(Z_0,B)\) is unchanged and receives no \(B'\) or \(X\) argument.

This is an unshifted-density representation of conditioning. Rewriting the
same Gaussian with a shifted centered interior variable is possible in
finite dimensions, but Balaban does not make that rewrite, and importing its
shift into a locally defined mark would change the proof obligation.

## Second-stage weakening map

Equation (2.8) inserts its new variables only into

\[
C^{(k)}(Z_0,s(Z)),\qquad
(C^{(k)})^{1/2}(s(Z)),\qquad
\Delta_k(s(Z)).
\tag{A2}
\]

The localized factor inherited from \(F(Z_0,B)\) has no second-stage
\(s\)-argument. For fixed \(D,P,Z_0,Z\), Eq. (2.14) is

\[
\begin{aligned}
&
\prod_{\Delta\subset Z\setminus\widetilde Z'_0}
\int_0^1 ds(\Delta)\,
\frac1{2\pi i}\int
\frac{d\sigma(\Delta)}
     {(\sigma(\Delta)-s(\Delta))^2}
\\
&\quad\cdot
\prod_{Y\in D}
\int_0^1 dt(Y)\,
\frac1{2\pi i}\int
\frac{d\tau(Y)}
     {(\tau(Y)-t(Y))^2}
\\
&\quad\cdot
\left.\int d\mu_0(X)\right|_Z
\exp\!\left[
-\frac12
\left\langle
\Gamma_k(Z_0,\sigma(Z))X,
C^{(k)}(Z_0,\sigma(Z))
\Gamma_k(Z_0,\sigma(Z))X
\right\rangle
\right]
\\
&\quad\cdot
\int d\mu_{C^{(k)}(Z_0,\sigma(Z))}(B)
\exp\!\left[
-\left\langle
B,\Gamma_k(Z_0,\sigma(Z))X
\right\rangle
\right]
\\
&\quad\cdot
(-1)^{|P|}
\chi_{k,Y_0}(B)\chi^c_{k,P}(B)
\exp\!\left[
\sum_{Y\in D}\tau(Y)V_k(Y,B)
\right],
\tag{2.14}
\end{aligned}
\]

where

\[
\Gamma_k(Z_0,\sigma(Z))
=
C^*\Delta_k(\sigma(Z))C
Z_0^c
(C^{(k)})^{1/2}(\sigma(Z)).
\tag{A3}
\]

The dependency map is therefore:

| Object | Interior \(B\) | Exterior \(X\) | \(\sigma\) | \(\tau\) |
|---|---:|---:|---:|---:|
| \(C^{(k)}(Z_0,\sigma)\), \(\Delta_k(\sigma)\), \(\Gamma_k(\sigma)\) | no | no | yes | no |
| complex Gaussian/density factor containing those operators | yes | yes | yes | no |
| \(\chi_{k,Y_0}(B)\), \(\chi^c_{k,P}(B)\) | yes | no | no | no |
| \(V_k(Y,B)\) | yes | no | no | multiplied by \(\tau(Y)\) |
| inserted \(W_{k,p}(A,B)\) | yes | no | no | no |

No separate determinant appears in Eq. (2.14); it is part of the normalized
complex Gaussian measure. Equation (2.15) exposes the comparison factor

\[
\left|
\frac{
\det(C^{(k)}(Z_0,\sigma)^{-1})
}{
\det(\operatorname{Re}[C^{(k)}(Z_0,\sigma)^{-1}])
}
\right|^{1/2}
\]

and a positive Gaussian whose covariance is

\[
\bigl(
\operatorname{Re}[C^{(k)}(Z_0,\sigma)^{-1}]
\bigr)^{-1}.
\]

It is the inverse of the real part of the complex precision, not the inverse
of the real part of the covariance.

## Marked corollary and correction

The construction is unmarked and prints no distinguished
\(W_{k,p}(A,B)\); RG II still retains its external \(J\) variable. In the
repository construction, the mark is inserted into \(F(Z_0,B)\) after its
first-stage localization. Equations (2.5)--(2.14) then route it unchanged:

\[
W_{k,p}(A,B),
\]

with no \(X\), \(\sigma\), or \(\tau\) argument. Define
\(\|B\|_A=\max_{b\in I_k(A)}\|B(b)\|\), with the empty maximum equal to zero.
On the support of \(\chi_{k,Y_0^\bullet}\),

\[
g_k\|B\|_A<\varepsilon _1.
\tag{A4}
\]

Consequently the original Eq. (1.34) marked supremum applies pointwise. For
the full real \(B\)-integral, the repository uses the measurable extension
equal to \(W_{k,p}\) on the strict local Eq. (1.34) domain and zero off it.
The fixed-cutoff containment audited from RG II Eqs. (1.20) and (1.34)
ensures that this extension agrees with the localized mark wherever the
marked seed cutoff is nonzero. The unbounded-\(X\) continuation and relative
Gaussian-moment problem stated in earlier versions of Notes 0021--0022 was
an artifact of the wrong variable map.

For one fixed auxiliary history and the same named ordinary contour set
\(\mathcal C_\gamma\), use
\[
K_\gamma(\sigma)
=
\left(\operatorname{Re}
[C^{(k)}(Z_0,\sigma)^{-1}]\right)^{-1},
\qquad
d\lambda_\gamma^\sigma
=d\mu_I(X)d\mu_{K_\gamma(\sigma)}(B),
\]
and leave the determinant quotient, cutoffs, absolute density, and all other
ordinary factors in \(\mathcal I_\gamma^{(0)}\). The repository consequence
is

\[
q_\gamma^\bullet=q_\gamma^{(0)},\qquad
C_\bullet=1,\qquad
\eta_{\rm mom}=0.
\tag{A5}
\]

This correction does not prove a final marked polymer norm. It closes only
the fixed \(A,D,P,Z_0,Z\) conditioned-contour domination. The next source
interface is the positive resummation of the enlarged seed (A1), including
the marked tree-gluing and \(k\)-to-\(k+1\) scale conversion.
