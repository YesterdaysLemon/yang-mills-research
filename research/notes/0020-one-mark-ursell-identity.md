# Note 0020: one-mark Ursell identity on a fixed polymer gas

Claim ID: YM-RG-020

Kind: exact finite-gas identity plus conditional rooted cluster bound

Evidence: E2 (elementary fixed-gas algebra and a version-pinned
Kotecky--Preiss implication under explicit convergence, synchronization, and
hull-weight premises)

Novelty: none claimed

Primary anchor: T. Balaban, [*Renormalization Group Approach to Lattice
Gauge Field Theories II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), especially Eqs.
(2.1)--(2.13), Lemma 3 Eq. (2.38), and Eq. (2.41).

Pinned-cluster anchor: R. Fernandez and A. Procacci,
[*Cluster expansion for abstract polymer models. New bounds from an old
approach*](https://arxiv.org/abs/math-ph/0605041v2), version 2, Eqs. (2.7),
(2.14), and (2.15); published as
[CMP 274 (2007), 123--140](https://doi.org/10.1007/s00220-007-0279-2).

## Scope and source boundary

This note closes one algebraic part of Program 003's Step 10. It proves the
exact connected formula produced by differentiating one **fixed** hard-core
polymer gas, explains its factorial, and gives a conditional weighted rooted
bound. It does not prove that the plaquette mark of Notes 0011--0014 survives
RG II's cutoff expansion, Gaussian conditioning, covariance weakening,
component factorization, and final polymerization with the required norm.
Note 0021 subsequently proves the exact finite fixed-partition passage and
component identity while leaving that norm conditional. Note 0023 gives one
explicit standard-closed-cube realization of the hull, animal, and pinned-KP
premises below. Subsequent Note 0024 identifies the final connected ordinary
RG-II gas with that model and gives a displayed-hierarchy-compatible ordinary
smallness window. Subsequent Note 0026 supplies the required marked norm and
instantiates this note's connected first-jet bound on one fixed gas under an
explicit doubled-amplitude refinement together with Note 0024's separate
ordinary KP ceiling.

The source is unmarked. Its exact relevant conventions are as follows.

1. RG II Eq. (2.1) first sums over unordered finite subfamilies of localized
   potentials, so there is no factorial at that Mayer-subset stage.
2. Eqs. (2.2)--(2.10) enlarge, condition, and factor the resulting supports.
   In particular, Eq. (2.10) factors \(H(Z)\) over connected components.
3. Eq. (2.11) is the ordered hard-core gas

   \[
   1+\sum_{n\ge1}\frac1{n!}
   \sum_{Z_1,\ldots,Z_n}
   \prod_{i<j}\zeta(Z_i,Z_j)\prod_i H(Z_i).
   \tag{1}
   \]

   The printed convention has \(\zeta(Z,Z')=0\) when
   \(Z\cap Z'\) contains a cube **or a complete cube wall**, and
   \(\zeta=1\) otherwise. Thus sharing a wall is already incompatible.
4. Eq. (2.12) exponentiates (1) with one exterior factor \(1/n!\) and
   connected coefficient

   \[
   p^T(Z_1,\ldots,Z_n)
   =\sum_{G\in\mathcal C_n}
   \prod_{\{i,j\}\in E(G)}
   [\zeta(Z_i,Z_j)-1],
   \qquad p^T(Z)=1.
   \tag{2}
   \]

   There is no second factorial inside \(p^T\).
5. Eq. (2.13) groups connected tuples by their union
   \(X=\bigcup_i Z_i\).

These formulas license the fixed-compatibility algebra below. They do not
license a marked activity estimate merely by differentiation.

## One fixed hard-core gas

Fix one finite regulator, one localization partition \(\pi\), and a finite
species set \(\mathfrak P_\pi\). Let \(\not\sim_\pi\) be a symmetric,
reflexive incompatibility relation and put

\[
f_\pi(X,X')=-\mathbf 1_{\{X\not\sim_\pi X'\}}
=\zeta_\pi(X,X')-1.
\tag{3}
\]

Reflexivity is important: repeated labels vanish in the hard-core partition
function, even though they must remain in its logarithmic expansion.

Let \(K_t(X)\) be differentiable at zero, with

\[
K_t(X)=K(X)+tM_p(X)+o(t).
\tag{4}
\]

The subscript \(p\) distinguishes the one plaquette mark. At this abstract
stage it asserts no relation between \(M_p\) and the pre-Section-2 activities
\(W_{k,p}\) of Notes 0012--0014.

Use the source's ordered convention:

\[
Z_\pi(t)=
\sum_{n\ge0}\frac1{n!}
\sum_{X_1,\ldots,X_n\in\mathfrak P_\pi}
\prod_{i=1}^nK_t(X_i)
\prod_{1\le i<j\le n}[1+f_\pi(X_i,X_j)].
\tag{5}
\]

Because incompatibility is reflexive, (5) is exactly the unordered
compatible-set polynomial

\[
Z_\pi(t)=
\sum_{\Gamma\subset\mathfrak P_\pi\ {\rm compatible}}
\prod_{X\in\Gamma}K_t(X).
\tag{6}
\]

If \(Z_\pi(0)\ne0\), ordinary finite-dimensional differentiation gives

\[
\left.\partial_t\log Z_\pi(t)\right|_{t=0}
=\frac{Z_\pi^\bullet}{Z_\pi(0)},
\tag{7}
\]

where

\[
Z_\pi^\bullet
=\sum_{A\in\mathfrak P_\pi}M_p(A)
\sum_{\substack{\Gamma\subset\mathfrak P_\pi\ {\rm compatible}\\
                  X\sim_\pi A\ \text{for every }X\in\Gamma}}
\prod_{X\in\Gamma}K(X).
\tag{8}
\]

There is no factorial in (8), because it uses unordered compatible sets.
Equations (7)--(8) are exact at every finite regulator and require no
small-activity assumption beyond the displayed nonzero denominator.

## Distinguished-vertex Ursell formula

For an ordered tuple \(\gamma_0,\ldots,\gamma_n\), define

\[
\Phi_\pi^T(\gamma_0,\ldots,\gamma_n)
=\begin{cases}
1,&n=0,\\[2mm]
\displaystyle
\sum_{G\in\mathcal C_{n+1}}
\prod_{\{i,j\}\in E(G)}f_\pi(\gamma_i,\gamma_j),&n\ge1.
\end{cases}
\tag{9}
\]

The superscript on \(A^\bullet\) below records the differentiated slot; its
compatibility with an ordinary polymer is still the fixed relation (3).
Differentiating the connected logarithm of (5) gives

\[
\boxed{
\left.\partial_t\log Z_\pi(t)\right|_{t=0}
=\sum_A M_p(A)
\sum_{n\ge0}\frac1{n!}
\sum_{X_1,\ldots,X_n}
\Phi_\pi^T(A^\bullet,X_1,\ldots,X_n)
\prod_{i=1}^nK(X_i).
}
\tag{10}
\]

Equation (10) holds coefficientwise as a formal power series at the origin.
It holds at the stated activities when the connected series and its marked
derivative converge absolutely. Finite volume and \(Z_\pi(0)\ne0\) alone do
not imply that the Taylor series about zero reaches arbitrary complex
activities.

The coefficient in (10) is \(1/n!\), not \(1/(n+1)!\). In the unmarked log
series, differentiation of an \((n+1)\)-tuple chooses any of its \(n+1\)
slots, so

\[
\frac{n+1}{(n+1)!}=\frac1{n!}.
\tag{11}
\]

Equivalently, direct differentiation of RG II Eq. (2.13) gives

\[
\dot E(X)=
\sum_{r\ge1}\frac1{(r-1)!}
\sum_{\substack{Z_1,\ldots,Z_r\\\cup_iZ_i=X}}
p^T(Z_1,\ldots,Z_r)\,
\dot H(Z_1)\prod_{i=2}^rH(Z_i).
\tag{12}
\]

One must not retain both \(1/(r-1)!\) and a further sum over the distinguished
slot. Equation (12) is a repository corollary of the printed unmarked
formula, not a marked theorem stated in RG II.

No extra factor \(1/Z_\pi(0)\) appears on the right of (10): the connected
coefficients already perform the numerator--denominator cancellation in
(7). Conversely, using only \(Z_\pi^\bullet\) omits that cancellation.

Repeated ordinary labels are essential in (10). They vanish from (5), since
\(1+f_\pi(X,X)=0\), but their Ursell coefficients generate the powers needed
for the reciprocal in (7). Replacing the ordered tuples in (10) by subsets
of distinct polymers is false.

## Root connectivity and a conditional hull

If
\(\Phi_\pi^T(A^\bullet,X_1,\ldots,X_n)\ne0\), the incompatibility graph of
the tuple is connected to the distinguished vertex. This is an abstract graph
statement. It does not say that every \(X_i\) directly touches \(A\), and it
does not by itself prove a bound in RG I's contained-tree metric.

Assume a declared fixed-partition hull map

\[
R=\operatorname {Hull}_\pi(A,X_1,\ldots,X_n)
\tag{13}
\]

with the following properties.

1. Every nonzero connected tuple has a hull in the admitted output-polymer
   class.
2. If \(M_p(A)\ne0\), then \(A\supset Q_p\), and (13) implies
   \(R\supset A\), hence \(R\supset Q_p\).
3. The source incompatibility convention, including wall contact, is the
   convention used to prove closure and any later metric inequality.

Then define

\[
\begin{aligned}
\mathcal C_{p,\pi}^\bullet(R)
={}&\sum_A\sum_{n\ge0}\frac1{n!}
\sum_{\substack{X_1,\ldots,X_n\\
\operatorname {Hull}_\pi(A,X_1,\ldots,X_n)=R}}
\Phi_\pi^T(A^\bullet,X_1,\ldots,X_n)\\
&\hspace{35mm}\times M_p(A)\prod_{i=1}^nK(X_i).
\end{aligned}
\tag{14}
\]

Under absolute convergence, (10) may be regrouped as

\[
\left.\partial_t\log Z_\pi(t)\right|_{t=0}
=\sum_{R\supset Q_p}\mathcal C_{p,\pi}^\bullet(R).
\tag{15}
\]

Repeated labels do not enlarge (13), but their separate terms in (14) remain
mandatory.

## Pinned Kotecky--Preiss implication

Let \(A_\pi,c_\pi\ge0\) be finite weights on ordinary polymers. A
distinguished tag inherits its underlying polymer's weight:
\(A_\pi(Y^\bullet):=A_\pi(Y)\). Assume the fixed-gas condition

\[
\sum_{X\not\sim_\pi Y}
|K(X)|e^{A_\pi(X)+c_\pi(X)}
\le A_\pi(Y)
\tag{16}
\]

for every ordinary \(Y\) and every admitted marked root \(Y^\bullet\). The
version-pinned Kotecky--Preiss estimate, applied to
\(\rho(X)=|K(X)|e^{c_\pi(X)}\), is

\[
\sum_{n\ge0}\frac1{n!}\sum_{X_1,\ldots,X_n}
|\Phi_\pi^T(Y^\bullet,X_1,\ldots,X_n)|
\prod_i|K(X_i)|e^{c_\pi(X_i)}
\le e^{A_\pi(Y)}.
\tag{17}
\]

Here is the exact source crosswalk. Fernandez--Procacci version 2 Eq. (2.7)
defines

\[
\Pi_Y(\rho)=
1+\sum_{n\ge1}\frac1{n!}
\sum_{X_1,\ldots,X_n}
|\Phi_\pi^T(Y,X_1,\ldots,X_n)|
\prod_i\rho(X_i),
\tag{17a}
\]

which is precisely the left side of (17). Their Eq. (2.15) is (16) after
\(\rho(X)=|K(X)|e^{c_\pi(X)}\) and \(a=A_\pi\); the source explicitly includes
the reflexively incompatible root in that sum. Their Eqs. (2.14)--(2.15)
then give \(\Pi_Y(\rho)\le e^{A_\pi(Y)}\). Thus (16)--(17) use a
version-pinned theorem with a term-by-term notation map, not an appeal to an
unspecified standard estimate.

In particular, with \(c_\pi=0\),

\[
\left|\left.\partial_t\log Z_\pi(t)\right|_{t=0}\right|
\le\sum_A|M_p(A)|e^{A_\pi(A)}.
\tag{18}
\]

For a localized output bound, assume in addition that every term grouped into
\(R\) obeys the geometric crosswalk

\[
e^{a_{\rm out}d_\pi(R)}
\le e^{a_{\rm out}d_\pi(A)}
\prod_{i=1}^ne^{c_\pi(X_i)},
\tag{19}
\]

that the pinned weight satisfies

\[
A_\pi(A)\le A_0+\epsilon d_\pi(A),
\tag{20}
\]

and that the post-polymerization marked activity has the norm

\[
\sup_p\sum_{A\supset Q_p}
e^{a_\bullet d_\pi(A)}|M_p(A)|\le\mathcal B_\bullet.
\tag{21}
\]

Equations (14), (17), and (19)--(21) prove

\[
\boxed{
\sup_p\sum_{R\supset Q_p}
e^{a_{\rm out}d_\pi(R)}
|\mathcal C_{p,\pi}^\bullet(R)|
\le e^{A_0}\mathcal B_\bullet,
\qquad
a_{\rm out}+\epsilon\le a_\bullet.
}
\tag{22}
\]

This is a conditional abstract implication. In the intended application,
Note 0013 has \(a_\bullet=(1-2\delta)\kappa\) before the Section-2
operations. No positive numerical value of \(a_{\rm out}\) follows until
(16), the survival of (21), and the hull inequality (19) are proved for the
actual post-conditioning activities.

Subsequent Note 0023 verifies one concrete sufficient package for
(13), (16), and (19)--(20) in a declared standard cubulation: literal-union
hulls, the piecewise-linear contained-tree metric, one ordinary species per
unlabelled support, a pointwise ordinary activity bound, and explicit strict
animal-entropy and smallness inequalities. Note 0024 then identifies the
final connected ordinary RG-II species, quotient seams, and incompatibility,
and maps the source metric through Note 0023's one-sided monotone-metric
extension plus a direct source-metric connector. It does not assert metric
equality. Note 0024 also gives an explicit sufficient \(\varepsilon _1\)
window within the displayed hierarchy. Applying the rooted conclusion here
still requires the independent post-polymerization marked norm and control
of every marked decoration and shift.

## Shift labels must remain outside the gas

For an admissible shift \(\sigma\), the partition \(\pi^\sigma\), species
set, incompatibility graph, unmarked activities, hull, and metric may all
depend on \(\sigma\). Write the resulting branch coefficient as

\[
\mathcal C_{p,\sigma}^\bullet(R)
=\mathcal C^\bullet
(K^\sigma,M_{p}^\sigma,\not\sim_\sigma,
  \operatorname {Hull}_\sigma;R).
\tag{23}
\]

The only presently safe shifted route is the following explicit
synchronization hypothesis \((\mathrm H_{\rm sync})\).

1. For every \(\sigma\in\mathcal A_{M,L}(p)\), carry the complete unmarked
   and source-inserted construction through RG II Eqs. (2.1)--(2.13) on the
   **same** partition \(\pi^\sigma\).
2. On that branch, the differentiated post-conditioning activity is exactly
   \(M_p^\sigma\), with the sign and normalization inherited from the same
   physical source ratio.
3. Each complete branch represents the same finite-regulator physical
   logarithmic derivative, and all rearrangements and bounds are uniform in
   \(\sigma\).

Under \((\mathrm H_{\rm sync})\), form (23) first and only then define

\[
\widehat{\mathcal C}_p^\bullet(\sigma,R)
=\frac1{n_p}\mathcal C_{p,\sigma}^\bullet(R),
\qquad
n_p=|\mathcal A_{M,L}(p)|.
\tag{24}
\]

The physical coefficient is the sum of (24). If (22) is uniform branchwise,
then

\[
\sup_p\sum_{\sigma,R}
e^{a_{\rm out}d_{k,\sigma}(R)}
|\widehat{\mathcal C}_p^\bullet(\sigma,R)|
\le e^{A_0}\mathcal B_\bullet.
\tag{25}
\]

Thus the normalized orbit pays no additional factor, but the output remains
\((\sigma,R)\)-labelled. Subsequent Note 0027 realizes this first-jet route
using nested two-scale lift labels \(s\), with normalization by their actual
lifted count.

Note 0014 proves that every individual shifted bare decomposition sums to the
same undecoupled mark. It does **not** prove \((\mathrm H_{\rm sync})\) for
the later cutoff-conditioned gas. In particular, one may not put all
\((\sigma,Y)\) labels into one gas, invent cross-shift compatibility, average
\(K^\sigma\) before taking a logarithm, or erase the shift label after the
cluster sum. Such operations have no source justification and can change
denominators or create mixed-shift configurations not present in any source
branch. Subsequent Note 0027 proves \((\mathrm H_{\rm sync})\) at first-jet
level by reconstructing the same dual-number integral on every separate
nested shifted gas. It does not build the alternative common gas in the next
paragraph.

There is one alternative: embed every shifted mark into a single proved
common gas with exactly the same \(K\), incompatibility, and hull. The
connected map is linear in the distinguished activity on that common gas, so
the normalized bare average may then be moved through it. No such embedding
is proved here.

## Physical sign and the background term

Notes 0010--0011 insert the fluctuation remainder through
\(e^{-t\Delta_p}\). For a completed source-inserted Section-2 construction,
define the **post-polymerization** positive-sign mark by

\[
W_p^{\rm post}(X)
:=-\left.\partial_tK_t^{\rm phys}(X)\right|_{t=0},
\qquad
M_p(X)=\left.\partial_tK_t^{\rm phys}(X)\right|_{t=0}
=-W_p^{\rm post}(X).
\tag{26}
\]

Thus (10) uses \(M_p=-W_p^{\rm post}\) in the
\(+\partial_t\log Z\) convention, or the rooted series with the positive
\(W_p^{\rm post}\) is written for
\(-\partial_t\log Z|_{t=0}\). The two conventions must not be combined.
Note 0021 subsequently proves, on one fixed compatible partition, that
\(W_p^{\rm post}\) is the exact decorated linear image of the pre-Section-2
family. Notes 0026 and 0027 subsequently prove the required norm and repeat
the complete construction uniformly over the nested shifted family,
discharging \((\mathrm H_{\rm sync})\) only at first-jet level.
Note 0011's explicit minimizing-background contribution remains outside this
fluctuation gas and must be restored in the full first jet.

## The source decay ledger is unmarked

The audited source spends decay through the unmarked Section-2 construction.
The high-confidence transcription is

\[
|H(Z)|
\le C_3\varepsilon_1
\exp\!\left[-(1-8\delta)\frac L2\kappa
d_{k+1}(Z)\right]
\tag{27}
\]

in Lemma 3 Eq. (2.38), followed by

\[
|E^{(k+1)}(X)|
\le O(1)C_3\varepsilon_1
\exp\!\left[-(1-10\delta)\frac L2\kappa
d_{k+1}(X)\right]
\tag{28}
\]

in Eq. (2.41). The source then chooses

\[
(1-10\delta)\frac L2=1,
\qquad
\delta=\frac1{10}\left(1-\frac2L\right),
\tag{29}
\]

and a smallness condition on \(C_3\varepsilon_1\) to recover the inductive
\(e^{-\kappa d_{k+1}}\) form.

The immutable Project Euclid page images were subsequently inspected in Note
0024. They directly confirm \(8\delta\), \(9\delta\), \(10\delta\), and the
\(L/2\) factors in Eqs. (2.38)--(2.41). More importantly, (27)--(28) bound
unmarked \(H\) and \(E^{(k+1)}\). They do not bound \(\dot H\), preserve Note
0013's mark norm, prove (16), or supply (19). Assigning the exponent in (28)
to the marked output without those steps would be an unsupported source
differentiation.

## Coefficient falsification checks

The coefficients in checks 1--3 below are also evaluated directly in
[the rooted-Ursell unit
tests](../../tests/test_rooted_ursell_coefficients.py).

1. **One self-incompatible species.** Let
   \(K_t(A)=k+t\mu\). Then

   \[
   Z(t)=1+k+t\mu,
   \qquad
   \left.\partial_t\log Z(t)\right|_0
   =\frac\mu{1+k}
   =\mu-\mu k+\mu k^2-\cdots.
   \tag{30}
   \]

   Here \(\Phi^T(A^\bullet,A)=-1\) and
   \(\Phi^T(A^\bullet,A,A)=2\). The latter term contributes
   \(2\mu k^2/2!=\mu k^2\). Excluding repeats or using \(1/(n+1)!\) fails.
2. **Compatible spectator.** If \(B\) is compatible with the marked species,
   then \(Z(t)=(1+k+t\mu)(1+b)\), while the logarithmic derivative is still
   \(\mu/(1+k)\). Every connected coefficient containing \(B\) vanishes.
   Keeping the numerator without its denominator leaves the spurious factor
   \(1+b\).
3. **Three-vertex star.** Let the mark \(R^\bullet\) be incompatible with
   compatible ordinary species \(A,B\). Then

   \[
   Z(t)=(1+a)(1+b)+t\mu,
   \qquad
   \left.\partial_t\log Z(t)\right|_0
   =\frac\mu{(1+a)(1+b)}.
   \tag{31}
   \]

   Since \(\Phi^T(R^\bullet,A,B)=1\), the two ordered tuples divided by
   \(2!\) give the required \(+\mu ab\) coefficient.
4. **Premature activity averaging.** Two identical one-species branch gases
   each give \(\mu/(1+k)\). If one incorrectly divides both the unmarked and
   marked activities by two and puts the two labels into one cross-compatible
   gas, then

   \[
   Z_{\rm mix}(t)=
   \left(1+\frac k2+t\frac\mu2\right)^2,
   \qquad
   \left.\partial_t\log Z_{\rm mix}(t)\right|_0
   =\frac\mu{1+k/2},
   \tag{32}
   \]

   not the branchwise average \(\mu/(1+k)\). This is deliberately **not**
   Eq. (24)'s normalization, which acts after the branch coefficient is
   formed; it falsifies averaging \(K^\sigma\) and \(M_p^\sigma\) inside a
   nonlinear logarithm. Leaving each \(K^\sigma=k\), scaling only the marked
   slots, and declaring the two branches cross-compatible happens to
   factorize in this toy case, but that accidental equality supplies neither
   a source cross-shift compatibility rule nor a common hull. Declaring the
   labels incompatible gives a different answer and merely inserts another
   unproved rule.

## Exact boundary

- Equations (7)--(12) prove the exact finite-gas ratio and formal or
  absolutely convergent rooted Ursell identity for one fixed species set,
  compatibility relation, and unmarked activity family.
- Equations (14)--(15) require a fixed-partition hull closed under every
  connected incompatibility tuple. Abstract graph connectivity alone is not
  the needed geometric theorem. Subsequent Note 0023 supplies such a theorem
  for its declared standard closed-cube, literal-union support model.
- Equation (22) is conditional on the canonical pinned KP condition, the
  post-polymerization marked norm, and the weighted hull crosswalk. None is
  inferred from unmarked Lemma 3. Note 0023 supplies explicit sufficient
  cubical and numerical conditions for the first and third premises, and Note
  0026 subsequently supplies the marked norm for the source-faithful
  fixed-partition plaquette mark.
- Equations (24)--(25) are conditional on a complete branchwise synchronized
  source construction. Bare-mark averaging from Note 0014 is not enough;
  subsequent Note 0027 supplies the needed dual-number construction on
  nested two-scale branches.
- Note 0021 subsequently proves the exact fixed-partition passage of the mark
  through RG II Eqs. (2.2)--(2.10), including sharp cutoffs, Gaussian
  conditioning, weakening, and component factorization, and identifies the
  final mark as a decorated linear image of the earlier rooted family. Note
  0025 proves its fixed-term marked domination, and Note 0026 proves its
  positive resummation and final norm on one fixed partition. Note 0027
  subsequently transports that complete construction and synchronizes the
  shifted first jets without mixing their gases.
- Note 0024 identifies the final connected ordinary RG-II support class and
  supplies a one-sided auxiliary-to-source metric comparison and direct
  source-metric \(\sqrt7\) connector; it does not identify the two metrics.
  It also supplies one explicit ordinary KP-smallness window. Note 0026
  supplies the marked Lemma-3 analogue on one gas, and Note 0027 supplies the
  uniform shifted first-jet expansion. The selected-coordinate scalar disk
  was already proved in Notes 0007 and 0010, while source-dependent polymer
  activities and KP convergence at nonzero source remain open. Consequently
  the physical pulled-back connected marked expansion remains open.
- The physical \(U\)-chain pullback, realization of Note 0019's geometric
  premises, marginal projection, large fields, RG iteration, continuum
  construction, Osterwalder--Schrader axioms, infrared decay, and the
  Yang--Mills mass gap remain open.

## Falsification checklist

- Use \(1/(n+1)!\) in (10) and compare with (30).
- Remove repeated labels from the logarithm and lose the \(+\mu k^2\) term.
- Keep a separate \(1/Z_\pi(0)\) after writing (10) and double-count the
  denominator cancellation.
- Infer direct contact with the root from connectedness and test a chain of
  mutually incompatible decorations.
- Replace wall incompatibility by disjoint interiors and change the source
  graph.
- Apply (27) to \(\dot H\) without a differentiated-localization estimate.
- Drop the \(L/2\) in (27)--(29) and obtain the wrong induction ledger.
- Average shifted activities or logarithms before proving a common gas or
  \((\mathrm H_{\rm sync})\).
- Combine the positive-mark and \(+\partial_t\log\) sign conventions in
  (26).
- Present (22) as a physical Yang--Mills result rather than a conditional
  fixed-gas implication.
