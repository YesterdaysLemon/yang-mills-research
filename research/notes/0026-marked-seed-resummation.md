# Note 0026: positive marked-seed resummation through the RG-II scale step

Claim ID: YM-RG-026

Kind: finite-regulator rooted positive-resummation corollary

Evidence: E2 (source-instantiated auxiliary lemma; internally checked)

Novelty: none claimed

Primary anchor: T. Balaban, [*Renormalization Group Approach to Lattice Gauge
Field Theories. II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), Eqs. (2.26)--(2.38).
The immutable-page transcription and the distinction between printed
unmarked estimates and the rooted corollary are recorded in the
[marked-resummation
audit](../../literature/audits/2026-07-23-balaban-marked-resummation.md).

## Scope

Work at one finite regulator, one fixed RG-II partition, and one admitted
external \((U,J)\) background. Use:

- Note 0013's already proved input norm
  \[
  \mathcal B_\bullet
  =
  \sup_p\sum_{A\supset Q_p}
  e^{(1-2\delta)\kappa d_k(A)}b_{p,A},
  \qquad
  b_{p,A}
  =
  \sup_{\mathrm{Eq.\ (1.34)}|_A}|W_{k,p}(A)|;
  \tag{1}
  \]
- Note 0021's exact marked seed and unique-root component algebra; and
- Note 0025's fixed-history positive domination with no second-stage
  relative-moment loss.

The support \(A\) is required to be an admissible same-scale localization
domain \(A\in\mathcal D_k\). This is the relabelled root-connected support
produced by Note 0012, not an arbitrary subset of cubes. This membership is
what permits \(A\) to be inserted into the uncoloured families in
Eqs. (2.27)--(2.29).

The result below proves the positive auxiliary resummation that was left
open in Notes 0021--0025. It does not prove shifted-partition
synchronization, a physical \(U/J\) pullback, large-field control, RG
iteration, a continuum theory, or a mass gap.

## Source constants and the transparent refinement

Write the ordinary factor in RG II Eq. (2.26) as

\[
c_0
:=
2E_0\varepsilon _1C_1\alpha _4^{-1}
M^q e^{C_2\kappa _1},
\qquad
\varepsilon _2:=c_0\alpha _6^{-1},
\tag{2}
\]

and define

\[
w_\kappa(Y)
:=
\alpha _6e^{-\delta\kappa d_k(Y)}.
\tag{3}
\]

The condition used by the source in passing from Eq. (2.27) to Eq. (2.28)
is \(\varepsilon _2e^{5\kappa}\le1\). We also use
\(0<\delta<1/4\), which follows from the source's eventual choice, and the
harmless normalization \(\alpha _6\le1\), compatible with taking
\(\alpha _6\) sufficiently small:

\[
0<\delta<\frac14,\qquad
\alpha _6\le1,\qquad
\varepsilon _2e^{5\kappa}\le1,
\tag{4}
\]

and the fixed-union family estimate

\[
\sum_{\substack{D\subset\mathcal D_k\\\bigcup_{Y\in D}Y=U}}
\prod_{Y\in D}w_\kappa(Y)
\le1
\tag{5}
\]

for every connected localization domain \(U\).

For the \(P\)-sum put

\[
q_k=\gamma _2\frac{\varepsilon _1^2}{g_k^2},
\qquad
\rho_k=\frac{q_k}{20},
\qquad
\rho_*=
\frac1{20}\gamma _2\frac{\varepsilon _1^2}{\gamma^2}.
\tag{6}
\]

The displayed source hierarchy supplies
\(g_k\le\gamma\), \(0<\varepsilon _2\le1\),
\(\rho_*\ge4\kappa\), and \(e^{-\rho_*}\le\varepsilon _2\). To encode the
last inequality in Eq. (2.31) and the later Eq. (2.34) absorption
transparently, impose the sufficient repository inequalities

\[
\rho_*-4M^4e^{-2\rho_*}\ge0,
\qquad
24e^{-\rho_*}\le\delta\kappa .
\tag{7}
\]

The function \(s\mapsto s-4M^4e^{-2s}\) is strictly increasing. Hence
\(\rho_k\ge\rho_*\) transfers the first inequality in (7) to the
\(\rho_k\)-coefficient appearing below.

Let

\[
K_{\rm lift}:=(L+2)^4C_{\rm geom},
\qquad
\lambda:=\frac L2\kappa,
\tag{8}
\]

where \(C_{\rm geom}\ge1\) is a fixed repository envelope dominating every
absolute \(O(1)\) coefficient used in the scale-transfer chain. It is not a
numerical evaluation or an identification of the paper's potentially
different printed \(O(1)\) occurrences.

At the scale-transfer stage impose the transparent monotone refinement that
every ordinary amplitude-smallness condition used between Eqs.
(2.35)--(2.38) remains valid after

\[
\varepsilon _2\longmapsto2\varepsilon _2.
\tag{9}
\]

In particular, it is sufficient to retain the printed conditions in the
stronger form

\[
2\varepsilon _2\le1,\qquad
2K_{\rm lift}\varepsilon _2\le\frac12,
\qquad
4K_{\rm lift}\varepsilon _2e^{5\kappa}\le1,
\tag{10}
\]

together with the unchanged geometric conditions, including

\[
\frac12(\kappa _1-1)\ge2L\kappa.
\tag{11}
\]

After all non-\(\varepsilon _1\) constants are fixed, (9)--(10) are
additional upper bounds linear in \(\varepsilon _1\). They therefore preserve
a nonempty displayed-hierarchy interval by downward shrinking of
\(\varepsilon _1\); as in Note 0024, calling the complete choice
source-admissible still assumes downward monotonicity of restrictions
imported but not enumerated in the paper. The coupling ceiling \(\gamma\) is
then chosen sufficiently small to retain (7).

## The colored \(D\)-family lemma

Fix a connected output

\[
U=A\cup\bigcup_{Y\in D}Y
\tag{12}
\]

of the marked root component. Put

\[
\bar b_A
:=
e^{(1-2\delta)\kappa d_k(A)}b_{p,A},
\qquad
a:=1-4\delta,
\qquad
r:=\frac{c_0}{\alpha _6}=\varepsilon _2.
\tag{13}
\]

The exact factorization is

\[
c_0e^{-(1-3\delta)\kappa d_k(Y)}
=
w_\kappa(Y)\,
r\,e^{-a\kappa d_k(Y)}
\tag{14}
\]

and

\[
b_{p,A}
=
\alpha _6^{-1}\bar b_Aw_\kappa(A)
e^{-(1-3\delta)\kappa d_k(A)}.
\tag{15}
\]

Let \(n=|D|\). Apply RG II Eq. (2.27) to the uncoloured family
\(E=D\cup\{A\}\). If \(A\notin D\), subtracting the common endpoint \(+5\)
gives

\[
d_k(A)+\sum_{Y\in D}d_k(Y)+5n\ge d_k(U).
\tag{16}
\]

If \(A\in D\), Eq. (2.27) for \(E=D\) gives
\(\sum_{Y\in D}d_k(Y)+5n\ge d_k(U)+5\); adding the coloured
\(d_k(A)\ge0\) implies (16). By (4),

\[
r^n
\le e^{-5\kappa n}
\le e^{-5a\kappa n}.
\tag{17}
\]

Equations (14)--(17) therefore give, term by term,

\[
\begin{aligned}
&b_{p,A}
\prod_{Y\in D}
c_0e^{-(1-3\delta)\kappa d_k(Y)}
\\
&\qquad\le
\alpha _6^{-1}\bar b_A
e^{-a\kappa d_k(U)}
w_\kappa(A)\prod_{Y\in D}w_\kappa(Y).
\end{aligned}
\tag{18}
\]

There is no \(1/n!\) in RG II Eq. (2.1): \(D\) is a finite subfamily. The
possible collision \(A\in D\) must consequently be counted explicitly.
For fixed \(A,U\), map \(D\) to \(E=D\cup\{A\}\). The preimage with
\(A\notin D\) contributes \(\prod_{Y\in E}w_\kappa(Y)\); the preimage with
\(A\in D\) contributes
\(w_\kappa(A)\prod_{Y\in E}w_\kappa(Y)\). Hence

\[
\begin{aligned}
&\sum_{\substack{D:\\A\cup\bigcup D=U}}
w_\kappa(A)\prod_{Y\in D}w_\kappa(Y)
\\
&\qquad=
\bigl(1+w_\kappa(A)\bigr)
\sum_{\substack{E\ni A\\\bigcup E=U}}
\prod_{Y\in E}w_\kappa(Y)
\le2.
\end{aligned}
\tag{19}
\]

The last inequality is (5), while its singleton case gives
\(w_\kappa(A)\le1\). Summing \(\bar b_A\) and using (1) proves the
coefficientwise rooted estimate

\[
\boxed{
\sum_{\substack{A\in\mathcal D_k,\ A\supset Q_p,\ D:\\
                 A\cup\bigcup D=U}}
b_{p,A}
\prod_{Y\in D}
c_0e^{-(1-3\delta)\kappa d_k(Y)}
\le
\varepsilon_\bullet
e^{-(1-4\delta)\kappa d_k(U)},
\qquad
\varepsilon_\bullet
:=
2\alpha _6^{-1}\mathcal B_\bullet.
}
\tag{20}
\]

The sharper collision constant is
\(\alpha _6^{-1}(1+\sup_Aw_\kappa(A))\). The factor \(2\) in (20) is a
safe exact consequence of retaining an ordinary occurrence with the same
geometric support as the coloured mark.

Every disconnected component not containing \(Q_p\) is unmarked and receives
the source's ordinary bound

\[
\varepsilon _2e^{-(1-4\delta)\kappa d_k(Y_i)}.
\tag{21}
\]

## The \(P,Y_0,Z_0\) resummation preserves the root coefficient

Write

\[
Y_0^\bullet
=
Y_\bullet\sqcup\coprod_{i\in I}Y_i,
\qquad
Q_p\subset A\subset Y_\bullet ,
\tag{22}
\]

and let \(Z_0\) be the smallest source domain containing
\(Y_0^\bullet\) and \(P\). Put

\[
V=M^{-4}|Z_0\setminus Y_0^\bullet|.
\tag{23}
\]

The unchanged source geometry gives \(|P|\ge V/2\). Split
\(\exp(-q_k|P|/2)\) into five factors
\(\exp(-2\rho_k|P|)\). Four convert into
\(\exp(-\rho_kV)\); one of those and the fifth factor give RG II Eq.
(2.31):

\[
\sum_Pe^{-\rho_kV}e^{-2\rho_k|P|}
\le
\exp\!\left\{
-V[\rho_k-4M^4e^{-2\rho_k}]
\right\}
\le1.
\tag{24}
\]

Thus three factors \(e^{-\rho_kV}\) remain.

For a connected component \(C\subset Z_0\), put
\(V_C=M^{-4}|C\setminus Y_0^\bullet|\). RG II Eq. (2.32), with the marked
component included without changing its geometry, is

\[
\mathbf 1_{\{Y_\bullet\subset C\}}d_k(Y_\bullet)
+\sum_{i:Y_i\subset C}d_k(Y_i)+4V_C\ge d_k(C).
\tag{25}
\]

Let \(Z_\bullet\) be the unique connected component of \(Z_0\) containing
\(Y_\bullet\). Two of the three remaining factors and the displayed
hierarchy \(\rho_k\ge\rho_*\ge4\kappa\), \(\varepsilon _2\le1\), give

\[
\varepsilon_\bullet
e^{-(1-4\delta)\kappa d_k(Y_\bullet)}
\prod_{Y_i\subset Z_\bullet}
\varepsilon _2e^{-(1-4\delta)\kappa d_k(Y_i)}
e^{-2\rho_kV_{Z_\bullet}}
\le
\varepsilon_\bullet
e^{-(1-4\delta)\kappa d_k(Z_\bullet)}.
\tag{26}
\]

The product in (26) ranges only over ordinary \(Y_i\) contained in
\(Z_\bullet\). Componentwise, one of the two displayed
\(e^{-\rho_kV_C}\) factors pays the \(4V_C\) connector in (25). On an empty
ordinary component, \(C\setminus Y_0^\bullet=C\) contains at least one
\(M\)-cube and hence \(V_C\ge1\); the other factor supplies
\(e^{-\rho_kV_C}\le e^{-\rho_*}\le\varepsilon _2\); on a nonempty ordinary
component its \(Y_i\)-product already supplies \(\varepsilon _2\), so the
extra factor may be discarded. The rooted component has no empty case and
requires no ordinary coefficient.

There is no empty-root case because \(Q_p\subset A\subset Y_\bullet\). An
ordinary component containing at least one \(Y_i\) keeps one
\(\varepsilon _2\); an empty ordinary component instead contributes at most
\(e^{-\rho_*}\le\varepsilon _2\). Thus every unmarked component is bounded
with the source comparison factor \(\varepsilon _2\).

The last factor \(e^{-\rho_kV}\) controls the remaining allowed
subset/occupancy choices \(Z_0\setminus Y_0^\bullet\) as in Eq. (2.34):

\[
\sum_{Z_0\setminus Y_0^\bullet}
e^{-\rho_kM^{-4}|Z_0\setminus Y_0^\bullet|}
\le
\exp\!\left(e^{-\rho_*}M^{-4}|Z_0|\right).
\tag{27}
\]

Forgetting the requirement \(Q_p\subset Y_0^\bullet\) only enlarges this
positive sum. The lower side of RG II Eq. (2.30),
\(M^{-4}|Z_j|\le24d_k(Z_j)\), and (7) give, componentwise,

\[
\exp\!\left(e^{-\rho_*}M^{-4}|Z_j|\right)
\le e^{\delta\kappa d_k(Z_j)}.
\tag{28}
\]

Consequently the marked analogue of Eq. (2.35) is

\[
\boxed{
\varepsilon_\bullet
e^{-(1-5\delta)\kappa d_k(Z_\bullet)}
\prod_{j\ne\bullet}
\left[
\varepsilon _2
e^{-(1-5\delta)\kappa d_k(Z_j)}
\right],
}
\tag{29}
\]

times the unchanged exterior-volume and
\(e^{O(1)\alpha _5|Z|}\) factors. The fixed root identifies
\(Y_\bullet\) before the \(P\)-sum and \(Z_\bullet\) afterward; no
component-choice multiplicity occurs in (29).

## Scale transfer as one positive susceptibility

The operations after Eq. (2.35) are colour blind:

1. each connected \(Z_i\) is mapped to the smallest \(Z_i'\in\mathcal
   D_{k+1}\) containing it;
2. components with the same \(Z_i'\) are grouped;
3. families of distinct \(Z_i'\) are united into \(Z'_0\); and
4. the \(Z\setminus Z'_0\) holes are summed.

Changing one component from ordinary to marked changes none of those
support rules. Forgetting the colour maps every marked history into an
ordinary scale-stage history with one eligible component distinguished.
The fixed root may only remove possible choices, so it is safe to overcount
all distinguished components.

This erasure statement is an explicit premise of the comparison, not a
consequence of root uniqueness alone. It holds here because Note 0025's
fixed-history domination changes only the coefficient attached to the
already enlarged seed, while the marked \(P,Y_0,Z_0\) construction above
uses the same support and hole rules as the ordinary construction. The two
possible earlier \(A\in D\) preimages have already been summed into
\(\varepsilon_\bullet\) in (20); erasure at the scale stage does not count
that collision again.

After absolute values, factor one \(\varepsilon _2\) from each of the \(N\)
raw connected \(Z_i\)-components before same-\(Z_i'\) grouping. At finite
regulator, write the complete termwise-absolute ordinary positive
scale-stage majorant as the finite series

\[
\mathscr S_x(Z)
=
\sum_{N\ge1}a_N(Z)x^N,
\qquad
x=\varepsilon _2,
\qquad
a_N(Z)\ge0,
\tag{30}
\]

where the coefficients \(a_N(Z)\) are independent of \(x\).

Replacing exactly one ordinary component by the marked coefficient
\(y=\varepsilon_\bullet\) gives

\[
\mathscr S^\bullet_{x,y}(Z)
\le
y\,\partial_x\mathscr S_x(Z)
=
\frac yx\sum_{N\ge1}N\,a_N(Z)x^N.
\tag{31}
\]

Since \(N\le2^{N-1}\) for \(N\ge1\),

\[
\mathscr S^\bullet_{x,y}(Z)
\le
\frac y{2x}\mathscr S_{2x}(Z).
\tag{32}
\]

Equation (2.36),

\[
2d_k(Z_i)\ge Ld_{k+1}(Z_i'),
\tag{33}
\]

is unchanged by the colour. Under (9), the termwise-positive scale-transfer
inequalities from Eqs. (2.35)--(2.38) may therefore be rerun at the abstract
amplitude \(2x\). The source's ordinary output coefficient is bounded by
\(2K_{\rm lift}x\), so at doubled amplitude it is bounded by
\(4K_{\rm lift}x\), while the exponent is unchanged:

\[
\mathscr S_{2x}(Z)
\le
4K_{\rm lift}x
e^{-(1-8\delta)\lambda d_{k+1}(Z)}.
\tag{34}
\]

Combining (20), (29), and (31)--(34) proves the actual fixed-partition
marked Lemma-3 analogue

\[
\boxed{
|W_p^{\rm post}(Z)|
\le
C_{\rm sec}\mathcal B_\bullet
e^{-(1-8\delta)\lambda d_{k+1}(Z)},
\qquad
C_{\rm sec}
=
4K_{\rm lift}\alpha _6^{-1}.
}
\tag{35}
\]

No smallness of \(\mathcal B_\bullet\) is used in the linear marked
resummation. The doubled-\(\varepsilon _2\) condition controls only the
ordinary susceptibility surrounding the unique mark.

## The final marked norm and fixed-partition connected sum

Use the source choice

\[
\delta=\frac1{10}\left(1-\frac2L\right),
\qquad
\Delta:=\delta\lambda,
\tag{36}
\]

and Note 0024's strict refinement

\[
\Delta>64\log8.
\tag{37}
\]

Retain also Note 0024's independent ordinary-gas smallness premise

\[
0<\varepsilon _1\le\varepsilon_{\rm KP},
\tag{37a}
\]

where \(\varepsilon_{\rm KP}\) is defined in its Eq. (17), equivalently so
that its Eq. (19) holds. Conditions (9)--(10) control the doubled scale
susceptibility and do not imply (37a). The joint refinement is obtained by
placing \(\varepsilon _1\) below the minimum of these finitely many positive
displayed ceilings, subject to the same imported-restriction monotonicity
caveat.

Note 0024 proves that Balaban's source \(d_{k+1}\) obeys Note 0023's
monotone-metric extension: its auxiliary degenerate metric is no larger, and
the source metric itself has the same \(\sqrt7\) connector. Hence

\[
\sup_Q\sum_{Z\supset Q}e^{-\Delta d_{k+1}(Z)}
\le C_{\rm an}^{\rm geom}(\Delta).
\tag{37b}
\]

This standard-cube animal bound at \(\eta=\Delta\) turns (35) into

\[
\boxed{
\sup_p
\sum_{Z\supset\widehat Q_p}
e^{(1-9\delta)\lambda d_{k+1}(Z)}
|W_p^{\rm post}(Z)|
\le
C_{\rm sec}C_{\rm an}^{\rm geom}(\Delta)
\mathcal B_\bullet.
}
\tag{38}
\]

Here \(\widehat Q_p\) is the next-scale root inherited from \(Q_p\).
Equation (38) is the previously missing post-polymerization marked norm on
one fixed partition. It sums the already aggregated decorated activity
\(W_p^{\rm post}(Z)\); auxiliary histories are not treated as additional
final species.

Finally take Note 0024's

\[
\alpha=\frac\Delta{64},
\qquad
a_{\rm out}=(1-10\delta)\lambda=\kappa.
\tag{39}
\]

By the explicit premise (37a), the final ordinary gas satisfies Note 0024's
instantiation of Note 0023's pinned Kotecky--Preiss condition and
source-metric hull crosswalk, while

\[
a_{\rm out}+32\alpha
\le(1-9\delta)\lambda.
\tag{40}
\]

Notes 0020 and 0023 therefore give the absolutely convergent
fixed-partition connected first-jet sum

\[
\boxed{
\sup_p\sum_{R\supset\widehat Q_p}
e^{\kappa d_{k+1}(R)}
|\mathcal C_{p,\pi}^\bullet(R)|
\le
e^{16\alpha}
C_{\rm sec}C_{\rm an}^{\rm geom}(\Delta)
\mathcal B_\bullet.
}
\tag{41}
\]

This is convergence of the first derivative at \(t=0\) on one fixed gas. It
does not construct a nonvanishing common external-source disk, and it does
not authorize averaging different shifted gases before their separate
connected maps are formed.

## Executable regressions

The accompanying tests check:

- the exact two-preimage \(D\mapsto D\cup\{A\}\) collision identity;
- the factor \(2\) coloured-family bound under the uncoloured Eq. (2.29)
  majorant;
- the connector exponent in (16)--(18);
- the positive-series inequality
  \(y\partial_x\mathscr S_x\le(y/2x)\mathscr S_{2x}\);
- the constant chain
  \(2\alpha _6^{-1}\mapsto4K_{\rm lift}\alpha _6^{-1}\); and
- the \(8\delta,9\delta,10\delta\) output ledger.

These are algebraic and combinatorial regressions. They do not certify the
Yang--Mills theorem.

## Exact boundary

- Balaban proves only the unmarked Eqs. (2.26)--(2.38). Repository
  distinguished-colour corollaries include (18)--(20), the marked adaptation
  (25), the root-restricted sums (26)--(29), (31)--(35), (38), and (41).
- The factor \(2\) in (20) is not a factorial convention. It records the two
  possible ordinary-subfamily preimages when an ordinary support equals the
  marked support.
- The scale susceptibility deliberately overcounts all \(N\) possible
  marked components. The actual fixed root is a subset of those choices.
- Condition (9) is an explicit extra monotone smallness refinement, not a
  formula printed by Balaban.
- Condition (37a) is a separate ordinary-gas KP premise; it is not a
  consequence of the doubled-amplitude conditions.
- The final animal and hull steps use the proved one-sided source-metric
  extension, not equality with Note 0023's degenerate auxiliary metric.
- The \(O(1)\) inside \(K_{\rm lift}\) is not evaluated numerically.
- No independent human review has been performed.
- Shift synchronization, the physical \(U/J\) pullbacks, intrinsic/raw
  comparison, large fields, RG iteration, continuum construction,
  Osterwalder--Schrader axioms, infrared decay, and the Yang--Mills mass gap
  remain open.

## Falsification checklist

- Insert a \(1/|D|!\) in Eq. (2.1) and reject the resulting collision
  bookkeeping.
- Deduplicate the coloured \(A\) against an equal ordinary support and lose
  the second preimage in (19).
- Apply Eq. (2.27) without the endpoint \(+5\) charges and lose the connector
  payment in (17).
- Use the ordinary proof at \(x\), rather than \(2x\), after bounding
  \(N\le2^{N-1}\).
- Let the colour change the \(Z_i\mapsto Z_i'\), family-union, or hole rules;
  then (31) is no longer justified.
- Treat the \(A,D,P,Z_0,Z'_0\) histories as separate final polymer species
  after they have already been aggregated into \(W_p^{\rm post}(Z)\).
- Promote (41) to a synchronized physical result or a continuum mass gap.
