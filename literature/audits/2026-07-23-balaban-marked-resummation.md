# Balaban RG-II marked-resummation source audit

Date: 2026-07-23

Purpose: pin the immutable unmarked source ledger behind repository claim
YM-RG-026 and separate Balaban's printed estimates from the repository's
one-colour corollary.

Primary source: T. Balaban, [*Renormalization Group Approach to Lattice Gauge
Field Theories. II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), pp. 17--20, Eqs.
(2.26)--(2.38).

Stable PDF:
<https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf>

Audited SHA-256:

```text
EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC
```

The relevant page images were rendered at high resolution and inspected
directly. In particular:

- printed p. 17: Eq. (2.26);
- printed p. 18: Eqs. (2.27)--(2.32);
- printed p. 19: Eqs. (2.33)--(2.36); and
- printed p. 20: Eqs. (2.37)--(2.38).

The PDF is evidence input and is not vendored in the repository.

## Eq. (2.26): fixed auxiliary-history majorant

With the repository shorthand

\[
c_0
:=
2E_0\varepsilon _1C_1\alpha _4^{-1}
M^q e^{C_2\kappa _1},
\tag{A1}
\]

the printed estimate is

\[
\begin{aligned}
|(2.14)|
\le{}&
\exp\!\left[
-(\kappa _1-1)(LM)^{-4}|Z\setminus Z'_0|
\right]
\\
&\times
\prod_{Y\in D}
\left[
c_0e^{-(1-3\delta)\kappa d_k(Y)}
\right]
\exp\!\left[
-\frac12\gamma _2\frac{\varepsilon _1^2}{g_k^2}|P|
\right]
e^{O(1)\alpha _5|Z|}.
\end{aligned}
\tag{2.26}
\]

The symbol \(c_0\) is not introduced by the paper. It is only a convenient
repository abbreviation.

## The \(D\)-family estimates

For one connected component

\[
Y_0=\bigcup_{Y\in D}Y,
\]

the source prints

\[
\sum_{Y\in D}\bigl(d_k(Y)+5\bigr)
\ge d_k(Y_0)+5.
\tag{2.27}
\]

Assuming

\[
c_0\alpha _6^{-1}e^{5\kappa}\le1,
\]

it derives

\[
\begin{aligned}
\prod_{Y\in D}\{\cdots\text{ in (2.26)}\}
\le{}&
\prod_{Y\in D}
\left[
\alpha _6e^{-\delta\kappa d_k(Y)}
\right]
\\
&\times
c_0\alpha _6^{-1}
e^{-(1-4\delta)\kappa d_k(Y_0)}.
\end{aligned}
\tag{2.28}
\]

For sufficiently large \(\kappa\) and sufficiently small \(\alpha _6\),

\[
\sum_{\substack{D:\,\bigcup_{Y\in D}Y=Y_0}}
\prod_{Y\in D}
\alpha _6e^{-\delta\kappa d_k(Y)}
\le1.
\tag{2.29}
\]

Equation (2.1) sums over finite subfamilies \(D\subset\mathcal D_k\). There
is no \(1/|D|!\) in this stage. This is material for the repository marked
corollary: a coloured support \(A\) and an ordinary member \(Y=A\) are two
occurrences even though the uncoloured family contains that geometry once.

The source also prints

\[
(3\cdot2^3)^{-1}M^{-4}|Y|
\le d_k(Y)
\le M^{-4}|Y|-1.
\tag{2.30}
\]

The upper endpoint is visibly \(-1\). No OCR reconstruction is used here.

## The \(P,Y_0,Z_0\) estimates

The smallest \(Z_0\) containing \(Y_0\) and \(P\) satisfies

\[
|P|
\ge\frac12M^{-4}|Z_0\setminus Y_0|.
\tag{A2}
\]

The paper splits the \(|P|\) exponential into five equal factors. Four are
converted with (A2), while the fifth controls the \(P\)-sum. One converted
factor and the summation factor give

\[
\begin{aligned}
&\sum_P
\exp\!\left[
-\frac1{20}\gamma _2\frac{\varepsilon _1^2}{g_k^2}
M^{-4}|Z_0\setminus Y_0|
\right]
\exp\!\left[
-\frac1{10}\gamma _2\frac{\varepsilon _1^2}{g_k^2}|P|
\right]
\\
&\quad\le
\exp\!\left\{
-M^{-4}|Z_0\setminus Y_0|
\left[
\frac1{20}\gamma _2\frac{\varepsilon _1^2}{g_k^2}
-4M^4
e^{-\frac1{10}\gamma _2\varepsilon _1^2/g_k^2}
\right]
\right\}
\le1.
\end{aligned}
\tag{2.31}
\]

The printed coefficient is \(\gamma _2\); the \(\rho\) notation used in Note
0026 is repository shorthand.

For a connected \(Z_0\) containing
\(Y_0=\bigcup_iY_i\), the geometric inequality is

\[
\sum_i d_k(Y_i)
+4M^{-4}|Z_0\setminus Y_0|
\ge d_k(Z_0).
\tag{2.32}
\]

The subsequent displayed assumptions include

\[
\frac1{20}\gamma _2\frac{\varepsilon _1^2}{g_k^2}
\ge
\frac1{20}\gamma _2\frac{\varepsilon _1^2}{\gamma^2}
\ge4\kappa,
\tag{A3}
\]

\[
\varepsilon _2
:=
c_0\alpha _6^{-1}
\le1,
\qquad
e^{-\gamma _2\varepsilon _1^2/(20\gamma^2)}
\le\varepsilon _2.
\tag{A4}
\]

For the repository marked corollary it is convenient to impose the
additional sufficient inequalities

\[
\rho_*-4M^4e^{-2\rho_*}\ge0,
\qquad
24e^{-\rho_*}\le\delta\kappa,
\qquad
\rho_*=\frac{\gamma _2\varepsilon _1^2}{20\gamma^2}.
\tag{A4a}
\]

These are not printed as a separate source display. The first transparently
encodes the last \(\le1\) in Eq. (2.31); since
\(s\mapsto s-4M^4e^{-2s}\) is increasing and \(\rho_k\ge\rho_*\), it controls
the actual \(\rho_k\) coefficient. The second combines the lower side of
Eq. (2.30), \(M^{-4}|Y|\le24d_k(Y)\), with the final Eq. (2.34) absorption.

The remaining subset sum is

\[
\begin{aligned}
&\sum_{Z_0\setminus Y_0}
\exp\!\left[
-\frac1{20}\gamma _2\frac{\varepsilon _1^2}{g_k^2}
M^{-4}|Z_0\setminus Y_0|
\right]
\\
&\qquad\le
\exp\!\left[
e^{-\gamma _2\varepsilon _1^2/(20\gamma^2)}
M^{-4}|Z_0|
\right].
\end{aligned}
\tag{2.34}
\]

After absorbing this exponential, the partially resummed source bound is

\[
\begin{aligned}
\left|\sum_{D,P}(2.14)\right|
\le{}&
\exp\!\left[
-(\kappa _1-1)(LM)^{-4}|Z\setminus Z'_0|
\right]
\\
&\times
\prod_i
\left[
\varepsilon _2
e^{-(1-5\delta)\kappa d_k(Z_i)}
\right]
e^{O(1)\alpha _5|Z|}.
\end{aligned}
\tag{2.35}
\]

The prose immediately after Eq. (2.31) is grammatically incomplete in the
scan. This audit imports the displayed inequalities and the later explicit
assumptions, not a guessed completion of that sentence.

## Scale conversion and final ordinary bound

For every connected component \(Z_i\) and its smallest next-scale
localization domain \(Z'_i\), the paper prints

\[
2d_k(Z_i)\ge Ld_{k+1}(Z'_i).
\tag{2.36}
\]

After extracting \(e^{-\delta\kappa d_k(Z_i)}\), the fixed-\(Z'_i\)
one-component sum makes the replacements

\[
\varepsilon _2
\longmapsto
(L+2)^4O(1)\varepsilon _2
\tag{A5}
\]

and

\[
(1-5\delta)\kappa d_k(Z_i)
\longmapsto
(1-6\delta)\frac L2\kappa d_{k+1}(Z'_i).
\tag{A6}
\]

For \(n\ge1\) components with the same \(Z'_i\), the geometric series is
bounded by

\[
2(L+2)^4O(1)\varepsilon _2
\]

when

\[
(L+2)^4O(1)\varepsilon _2\le\frac12.
\tag{A7}
\]

The following family resummation additionally assumes

\[
2(L+2)^4O(1)\varepsilon _2e^{5\kappa}\le1.
\tag{A8}
\]

It gives

\[
\begin{aligned}
\left|\sum_{D,P,Z_0}(2.14)\right|
\le{}&
\exp\!\left[
-(\kappa _1-1)(LM)^{-4}|Z\setminus Z'_0|
\right]
\\
&\times
\prod_i
\left[
2(L+2)^4O(1)\varepsilon _2
e^{-(1-7\delta)\frac L2\kappa d_{k+1}(Z'_i)}
\right]
e^{O(1)\alpha _5|Z|}.
\end{aligned}
\tag{2.37}
\]

The last hole resummation assumes, in particular,

\[
\frac12(\kappa _1-1)\ge2L\kappa,
\tag{A9}
\]

and bounds \((LM)^4\alpha _0,(LM)^4\alpha _1,
(LM)^4\alpha _4,(LM)^4\gamma _2\) independently of \(M\). The source writes

\[
\alpha _5
=
O(1)e^{-\delta _0M/3}
+O(\alpha _0+\alpha _1)
+O(1)\alpha _4+\gamma _2.
\tag{A10}
\]

With

\[
C_3
=
2(L+2)^4O(1)\,
2E_0C_1\alpha _4^{-1}\alpha _6^{-1}
M^qe^{C_2\kappa _1},
\tag{A11}
\]

Lemma 3 is

\[
|H(Z)|
\le
C_3\varepsilon _1
e^{-(1-8\delta)\frac L2\kappa d_{k+1}(Z)}.
\tag{2.38}
\]

Every \(O(1)\) in these formulas is unspecified and may denote a different
absolute constant. A repository constant that uses them must be a uniform
envelope, not an asserted numerical equality.

## Repository one-colour corollary

Balaban prints no distinguished plaquette mark in Eqs. (2.26)--(2.38).
Note 0026 adds one colour only after Notes 0021 and 0025 have established:

1. the marked seed is rerun before every seed-dependent construction;
2. one and only one connected component carries the mark;
3. after fixed-history domination, the colour does not alter any support,
   smallest-domain, family-union, or hole rule.

The marked \(D\)-family estimate uses Eqs. (2.27)--(2.29) directly. Because
Eq. (2.1) has subfamilies rather than factorial-weighted lists, the map
\(D\mapsto D\cup\{A\}\) has two possible preimages when the ordinary family
may contain \(A\). This yields the safe factor \(2\), not a cancelled
factorial.

After the marked analogue of Eq. (2.35), erase the colour. The later
positive majorant is a finite power series

\[
\mathscr S_x(Z)
=
\sum_{N\ge1}a_N(Z)x^N,
\qquad a_N(Z)\ge0,
\qquad x=\varepsilon _2.
\tag{A12}
\]

Replacing one component coefficient by \(y=\varepsilon_\bullet\) is bounded
by

\[
y\,\partial_x\mathscr S_x(Z).
\tag{A13}
\]

Since \(N\le2^{N-1}\),

\[
y\,\partial_x\mathscr S_x(Z)
\le
\frac y{2x}\mathscr S_{2x}(Z).
\tag{A14}
\]

For this comparison the repository fixes
\(C_{\rm geom}\ge1\) as one envelope dominating every relevant source
\(O(1)\) coefficient in the scale-transfer chain, and writes
\(K_{\rm lift}=(L+2)^4C_{\rm geom}\). Neither name nor a numerical value is
printed by Balaban. The ordinary output coefficient is bounded by
\(2K_{\rm lift}x\); the repository invokes the termwise-positive scale
inequalities at the abstract amplitude \(2x\).

Note 0026 therefore reruns those termwise-positive inequalities at doubled
abstract amplitude while imposing every ordinary smallness restriction at
\(2\varepsilon _2\). This is an explicit additional monotone refinement. It
does not modify the geometric or exponent ledger, and it is not attributed
to Balaban.

The later fixed-gas connected consequence uses two separate repository
premises that are not implied by doubling \(\varepsilon _2\):

1. Note 0024's explicit ordinary-gas ceiling
   \(0<\varepsilon _1\le\varepsilon_{\rm KP}\); and
2. its one-sided metric crosswalk
   \(d_{\rm aux}\le d_{k+1}\), together with a direct
   \(\sqrt7\) connector inequality for the source metric.

The first supplies the pinned ordinary gas. The second lets Note 0023's
auxiliary animal constant dominate the source-metric animal sum without
identifying Balaban's singleton convention with the auxiliary degenerate
tree convention.

## Exact boundary

- The source ledger above is unmarked.
- The collision factor, positive derivative comparison, doubled-amplitude
  refinement, marked output norm, and connected first-jet consequence are
  repository corollaries.
- The connected consequence additionally assumes the independent ordinary
  KP ceiling and uses a one-sided source-metric extension; neither follows
  from the doubled-amplitude scale comparison.
- The external PDFs are not evidence of independent review of those
  corollaries.
- No numerical value is assigned to any \(O(1)\).
- Subsequent Note 0027 separately proves shifted first-jet synchronization as
  a repository transport corollary. No nonzero-source polymer-activity disk,
  physical pullback, large-field result, RG iteration, continuum
  construction, axioms, infrared decay, or mass gap is obtained from this
  audit.
