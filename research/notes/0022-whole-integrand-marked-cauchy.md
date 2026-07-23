# Note 0022: whole-integrand Cauchy control for the Section-2 mark

Claim ID: YM-RG-022

Kind: exact finite mixed-difference lemma, conditional marked-kernel bound,
and sharp obstruction

Evidence: E2 (elementary finite-dimensional complex analysis and
counterexamples; internally checked)

Novelty: none claimed

Primary anchor: T. Balaban, [*Renormalization Group Approach to Lattice
Gauge Field Theories II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), especially Eqs.
(1.9)--(1.10), the Cauchy discussion following Eq. (1.10), Eq. (2.8), and
the single-term estimate beginning at Eq. (2.14).

## Scope and source boundary

Note 0021 defines the exact distinguished-slot image

\[
W_p^{\rm post}(C)
=\sum_{A\supset Q_p}\mathcal T_{\pi;C,A}[W_{k,p}(A)]
\tag{1}
\]

on one finite regulator and one fixed compatible partition. Its first open
analytic question was whether the weakening derivatives in RG II Eq. (2.8)
create an uncontrolled product-rule multiplicity when they hit the
transformed marked integrand.

This note answers that narrow question: they do not, provided the **entire
marked integrand** is holomorphic and jointly integrably dominated on one
common weakening polydisc. One multivariable Cauchy contour then includes all
derivative placements without a factor \(2^{|S|}\), \((|D|+1)^{|S|}\), or a
factorial.

The source paper is unmarked. It applies the decomposition (1.10) to the
whole standardized function in Eq. (2.8), treats the resulting Eq. (2.14)
term as analytic in the complex weakening and Mayer parameters, and proves
an unmarked majorant. The marked formulas below are repository lemmas. They
do **not** assert that Balaban printed a marked estimate.

**Correction.** Earlier versions of this note described the actual
plaquette mark as depending on a conditioned and standardized argument
involving \(X\) and the second-stage weakening variables. The immutable-page
audit in Note 0025 shows that this schematic map was false. A localized
factor remains \(F(Z_0,B)\); the actual inserted \(W_{k,p}(A,B)\) is
independent of \(X,\sigma,\tau\), and the marked seed cutoff keeps its \(B\)
argument in Eq. (1.34). The general whole-integrand lemma below remains
valid, but its relative-moment hypothesis is unnecessary for this exact
source routing.

Each active weakening coordinate in this decomposition is differentiated
once; the multi-index is square-free, although in a general product those
derivatives may land on many different factors after a product-rule
expansion. Direct page inspection shows that the cutoffs in Eq. (2.14) are
independent of the second-stage weakening variables. A different
weakening-dependent nonholomorphic cutoff would still lie outside this
Cauchy lemma unless supplied with a holomorphic extension or a separate
valid real-derivative estimate.

## The exact mixed-difference operator

Fix one admissible collection of auxiliary data

\[
\gamma=(A,D,P,Z_0,Z,\text{conditioning and localization choices})
\tag{2}
\]

in the marked construction of Note 0021. Let \(S_\gamma\) be the finite set
of active second-stage weakening variables. Variables outside
\(S_\gamma\) are fixed at the zero/one values prescribed by the source.
Suppressing those fixed values, define

\[
\mathscr D_SF
:=\int_{[0,1]^S}\partial_SF(s)\,ds,
\qquad
\partial_S=\prod_{e\in S}\partial_{s_e}.
\tag{3}
\]

For \(S=\varnothing\), \(\mathscr D_\varnothing\) is the identity. Repeated
use of the fundamental theorem of calculus gives the exact identity

\[
\boxed{
\mathscr D_SF
=\prod_{e\in S}(E_e^1-E_e^0)F,
}
\tag{4}
\]

where \(E_e^a\) evaluates the \(e\)-th variable at \(a\). Thus the
weakening term is a mixed difference of the whole function, not a rule that
assigns each derivative to a separately estimated factor.

Let

\[
\mathbb P_R(S)=\{z\in\mathbb C^S:|z_e|<R_e\},
\qquad R_e>1.
\tag{5}
\]

If \(F\) is holomorphic on this polydisc and
\(1<r_e<R_e\), the one-variable residue formula for
\(F(1)-F(0)\), iterated over \(S\), gives

\[
\boxed{
\mathscr D_SF
=\frac1{(2\pi i)^{|S|}}
\oint_{|\zeta_e|=r_e}
F(\boldsymbol\zeta)
\prod_{e\in S}
\frac{d\zeta_e}{\zeta_e(\zeta_e-1)}.
}
\tag{6}
\]

Each contour has length \(2\pi r_e\), while
\(|\zeta_e|=r_e\) and
\(|\zeta_e-1|\ge r_e-1\). Hence

\[
|\mathscr D_SF|
\le
\sup_{z\in\mathbb P_R(S)}|F(z)|
\prod_{e\in S}(R_e-1)^{-1},
\tag{7}
\]

where the endpoint follows by taking \(r_e\uparrow R_e\). The same statement
holds for Banach-valued \(F\), in particular for an \(L^1\)-valued
integrand, under the usual locally uniform domination.

## Direct marked-weakening lemma

For this general lemma, put every weakening-dependent determinant,
covariance density, Gaussian factor, Mayer factor, and hypothetical
weakening-dependent marked factor in the complete standardized integrand. A
cutoff factor may be included only if it is
weakening-independent or has the holomorphic extension assumed below; a
weakening-dependent nonholomorphic cutoff is outside this lemma. Write the
resulting integrand as

\[
F_\gamma^\bullet(\boldsymbol\sigma,x),
\tag{8}
\]

where \(x\) collects all remaining integration variables and \(d\nu_\gamma\)
is one fixed reference measure. Assume:

1. \(F_\gamma^\bullet\) has a jointly measurable representative which is
   holomorphic in \(\boldsymbol\sigma\) for
   \(d|\nu_\gamma|\)-almost every \(x\) on
   \(\mathbb P_R(S_\gamma)\);
2. a locally uniform integrable envelope makes
   \(\boldsymbol\sigma\mapsto
   F_\gamma^\bullet(\boldsymbol\sigma,\cdot)\) an
   \(L^1(d|\nu_\gamma|)\)-holomorphic map and permits Fubini,
   differentiation, and the contour operations; and
3. for the input coefficient \(b_{p,A}\) and one positive **joint marked**
   decoration weight \(q_\gamma^\bullet\),

   \[
   \sup_{\boldsymbol\sigma\in\mathbb P_R(S_\gamma)}
   \int|F_\gamma^\bullet(\boldsymbol\sigma,x)|
   \,d|\nu_\gamma|(x)
   \le b_{p,A}q_\gamma^\bullet.
   \tag{9}
   \]

Then (6), Fubini, and the triangle inequality prove

\[
\boxed{
\left|
\int d\nu_\gamma(x)\,
\mathscr D_{S_\gamma}F_\gamma^\bullet(\cdot,x)
\right|
\le
b_{p,A}q_\gamma^\bullet
\prod_{e\in S_\gamma}(R_e-1)^{-1}.
}
\tag{10}
\]

Equation (10) includes derivatives hitting a hypothetical
weakening-dependent marked factor, the ordinary decorations, or both. The
actual source-faithful plaquette factor is independent of those variables by
Note 0025. Expanding

\[
\partial_S(MU)
=\sum_{T\subset S}(\partial_TM)
 (\partial_{S\setminus T}U)
\tag{11}
\]

before taking absolute values would manufacture \(2^{|S|}\) separate
estimates. Expanding all Mayer decorations can manufacture still more
derivative allocations. Those are artifacts of that proof strategy, not
coefficients in (4), (6), or (10).

The loss can be strict. For
\(M(z)=\prod_{i=1}^n(1+z_i)\) and
\(U(z)=\prod_{i=1}^n(1-z_i)\),
\[
\left|\mathscr D_{\{1,\ldots,n\}}(MU)\right|=1,
\tag{11a}
\]
while integrating and taking absolute values of all \(2^n\) Leibniz
allocations separately gives
\[
\sum_{T\subset\{1,\ldots,n\}}
\int_{[0,1]^n}
\left|(\partial_TM)(\partial_{T^c}U)\right|\,ds
=2^n.
\tag{11b}
\]

Equivalently, one may define (3)--(6) directly for the
\(L^1(d|\nu_\gamma|)\)-valued map using Bochner integrals and then apply the
bounded integration functional. No pointwise representative is needed in
that formulation.

For the common source radius \(R_e=e^{\kappa _1}\), and in the same
sufficiently-large regime used in Note 0013,

\[
(e^{\kappa _1}-1)^{-|S|}
\le e^{-(\kappa _1-1)|S|}.
\tag{12}
\]

This is exactly the ordinary weakening price. If the marked integrand is
analytic only to a smaller common radius \(R_\bullet>1\), put
\(R_*=\min(e^{\kappa _1},R_\bullet)\). Relative to the source radius the
additional factor is

\[
\left(
\frac{e^{\kappa _1}-1}{R_*-1}
\right)^{|S|}
=e^{\chi|S|},
\qquad
\chi=\log\frac{e^{\kappa _1}-1}{R_*-1}.
\tag{13}
\]

It cannot be renamed a fixed \(\delta\)-loss unless an explicit bound relates
\(|S|\) to the relevant tree metric and the resulting exponent fits the
ledger.

For example, if a later auxiliary sum contributes at most
\(C_{\rm weak}^{|S|}\) choices and one proves
\(|S|\le c_{\rm weak}d\) in the same metric, the combined smaller-radius and
choice loss is at most

\[
\exp\!\left\{
c_{\rm weak}\bigl(\log C_{\rm weak}+\chi\bigr)d
\right\}.
\tag{13a}
\]

One \(\delta\)-unit pays (13a) only under the explicit inequality
\[
c_{\rm weak}\bigl(\log C_{\rm weak}+\chi\bigr)
\le\delta\kappa.
\tag{13b}
\]

Neither the cardinality-to-metric inequality nor this numerical margin is
proved for the actual marked construction here.

## Reduction to one positive kernel

After applying (10), retain every seed-dependent admissibility rule and put
all absolute auxiliary weights into

\[
K_\pi^\bullet(C,A)
:=\sum_{\gamma:(C,A)}
|c_\gamma|q_\gamma^\bullet
\prod_{e\in S_\gamma}(R_e-1)^{-1}.
\tag{14}
\]

The symbol \(c_\gamma\) includes the cutoff inclusion--exclusion signs only
after absolute values have been taken. The family being summed depends on
\(A\), because \(A\) belongs to the seed. Equations (1) and (10) give the
conditional operator bound

\[
\boxed{
|W_p^{\rm post}(C)|
\le\sum_{A\supset Q_p}b_{p,A}K_\pi^\bullet(C,A).
}
\tag{15}
\]

No extra marked-slot multiplicity occurs in (15). The remaining task is an
actual bound on \(K_\pi^\bullet(C,A)\), including the conditioned Gaussian integral,
the seed geometry, and all resummations. The input rooted \(A\)-sum should be
performed only after (15); counting possible sub-supports of \(A\) again
would be artificial.

## What joint domination must mean

A useful sufficient form of (9) factors the pointwise integrand only for the
purpose of a **joint** estimate:

\[
|M_A(\boldsymbol\sigma,x)|\le b_{p,A}m_A(x),
\qquad
|U_\gamma(\boldsymbol\sigma,x)|\le u_\gamma(x),
\tag{16}
\]

uniformly on the common polydisc, together with

\[
\int m_Au_\gamma\,d|\nu_\gamma|
\le C_\bullet e^{\eta d_k(A)}
\int u_\gamma\,d|\nu_\gamma|.
\tag{17}
\]

Here \(C_\bullet\) and \(\eta\) must be uniform in \(A,\gamma,p\), the
regulator, the admitted background, and the fixed-partition root before they
may be pulled outside the later sums.

For example, for one fixed \(q>1\), the relative moment estimate

\[
\int m_A^q u_\gamma\,d|\nu_\gamma|
\le C_\bullet^q e^{q\eta d_k(A)}
\int u_\gamma\,d|\nu_\gamma|
\tag{18}
\]

implies (17) by Holder's inequality. Separate bounds on
\(\int m_A\) and \(\int u_\gamma\) do not imply a bound on their product.

Define the ordinary, unmarked weight and its corresponding kernel separately:

\[
q_\gamma^{(0)}
:=\int u_\gamma\,d|\nu_\gamma|,
\qquad
K_\pi^{(0)}(C,A)
:=\sum_{\gamma:(C,A)}
|c_\gamma|q_\gamma^{(0)}
\prod_{e\in S_\gamma}(R_e-1)^{-1}.
\tag{18a}
\]

Equations (16)--(17) then imply

\[
\boxed{
|W_p^{\rm post}(C)|
\le C_\bullet
\sum_{A\supset Q_p}
b_{p,A}e^{\eta d_k(A)}K_\pi^{(0)}(C,A).
}
\tag{18b}
\]

For a genuinely \(\sigma\)-dependent mark, (16)--(18) remain a useful
sufficient interface. They are not needed for the actual plaquette routing.
Note 0025 transcribes Eqs. (2.3), (2.5), (2.6), (2.8), and (2.14) and proves

\[
\mathcal I_\gamma^\bullet(\boldsymbol\sigma,\boldsymbol\tau;B,X)
=
\widetilde W_{k,p}(A,B)
\mathcal I_\gamma^{(0)}(\boldsymbol\sigma,\boldsymbol\tau;B,X).
\tag{19}
\]

With

\[
b_{p,A}
=
\sup_{\mathrm{Eq.\ (1.34)}|_A}|W_{k,p}(A)|,
\]

where \(\widetilde W_{k,p}\) is Note 0025's measurable extension equal to
\(W_{k,p}\) on the strict local Eq. (1.34) domain and zero off it. The marked
seed \(Y_0^\bullet=A\cup\bigcup_{Y\in D}Y\) and its interior cutoff ensure
that this extension agrees with the original mark on the nonzero integrand
support, while globally

\[
|\widetilde W_{k,p}(A,B)|\le b_{p,A}.
\tag{19a}
\]

Consequently (16)--(17) hold with

\[
m_A=1,\qquad
C_\bullet=1,\qquad
\eta=0,\qquad
q_\gamma^\bullet=q_\gamma^{(0)}.
\tag{19b}
\]

The second-stage source radius is unchanged, no derivative hits the mark,
and no relative Gaussian moment is required. At this checkpoint the
unresolved interface was the positive resummation of the enlarged marked
seed and its tree/scale gluing, not a common transformed marked domain.
Subsequent Note 0026 closes that interface for the source-faithful plaquette
mark on one fixed partition.

## Correct exponent ledger: a fork

The source-free Section-2 ledger is

\[
1-2\delta\longrightarrow1-4\delta
\longrightarrow1-5\delta\longrightarrow1-6\delta
\longrightarrow1-7\delta\longrightarrow1-8\delta.
\tag{20}
\]

The first arrow is the ordinary \(D/Y_0\) resummation. The final four arrows
pay the later enlargement, scale-conversion, family, and output sums. For a
general weakening-dependent mark, any relative-moment cost must be joined to
this ledger as a parallel branch, not blindly appended to every ordinary
loss. For the actual source-faithful mark, Note 0025 proves
\(r_{\rm mom}=0\); the notation below retains the general case only to expose
the budget.

Write the relative-moment cost as
\(\eta=r_{\rm mom}\delta\kappa\), and let
\(r_{\rm root}\delta\kappa\) denote the rooted-support overhead and
\(r_{\rm other}\delta\kappa\) collect every remaining
metric-proportional marked loss incurred before the marked seed is glued to
the ordinary \(D/Y_0\) branch. Define the **total** pre-gluing marked cost

\[
r_{\rm tot}:=r_{\rm mom}+r_{\rm root}+r_{\rm other}.
\tag{21}
\]

Assume that marked gluing itself costs no further metric-proportional
exponent beyond a uniform multiplicative constant. The two branches entering
that gluing retain

\[
\begin{aligned}
\text{mark branch:}&\quad 1-2\delta
   \longrightarrow1-(2+r_{\rm tot})\delta,\\
\text{ordinary }D/Y_0\text{ branch:}&\quad 1-2\delta
   \longrightarrow1-4\delta.
\end{aligned}
\tag{22}
\]

Their union retains

\[
1-\max\{4,2+r_{\rm tot}\}\delta.
\tag{23}
\]

If the four later resummations remain valid with this retained input margin,
the conditional output exponent is

\[
\boxed{
a_{\rm out}(r_{\rm tot})
=\left[
1-\bigl(\max\{4,2+r_{\rm tot}\}+4\bigr)\delta
\right]\frac L2\kappa.
}
\tag{24}
\]

Thus any **total** \(r_{\rm tot}\le2\) still ends at
\((1-8\delta)(L/2)\kappa\). For the actual source-faithful plaquette mark,
Note 0025 sets \(r_{\rm mom}=0\), so the remaining condition is
\(r_{\rm root}+r_{\rm other}\le2\). For \(r_{\rm tot}>2\), the formal endpoint
worsens to
\((1-(6+r_{\rm tot})\delta)(L/2)\kappa\); using that endpoint additionally
requires \((6+r_{\rm tot})\delta<1\) and a fresh verification that every
later resummation closes with the smaller margin. The printed source-free
closure proves only its baseline ledger. A radius penalty of the form (13)
is a different quantity and is not automatically included in
\(r_{\rm tot}\).

## Sharp counterexamples

The hypotheses above cannot be weakened in the most tempting ways.

1. **Real-cube control is insufficient.** For
   \(F_n(z)=\prod_{i=1}^n(2z_i-1)\),
   \(\sup_{[0,1]^n}|F_n|=1\), but
   \(\mathscr D_{\{1,\ldots,n\}}F_n=2^n\). Complex room is what pays the
   mixed difference.
2. **The unmarked weakening does not control the mark.** If \(U=1\) and
   \(M(z)=\prod_i z_i\), then \(\mathscr D_SU=0\) while
   \(\mathscr D_S(MU)=1\).
3. **Separate integrated bounds do not multiply.** On a probability space
   with an event \(E\) of mass \(\varepsilon\), put
   \(m=u=\varepsilon^{-1}\mathbf1_E\). Then
   \(\int m=\int u=1\), but \(\int mu=\varepsilon^{-1}\).
4. **A smaller analytic domain has no free extension.** For \(R>r>0\),
   \(f_n(z)=(z/r)^n\) has supremum one on \(|z|\le r\), while
   \(|f_n(R)|=(R/r)^n\). An input-domain norm alone cannot bound a transformed
   argument outside that domain.

These examples remain warnings for other, genuinely weakening-dependent
insertions. The wrong-map outer-disk example does not apply to the actual
plaquette mark after Note 0025's source-routing correction.

## Executable checks

[The whole-integrand Cauchy tests](../../tests/test_whole_integrand_cauchy.py)
check the exact mixed-difference identity, the derivative-allocation trap,
the real-cube counterexample, and failure of separate integrated majorants.
The [conditioned-routing
tests](../../tests/test_conditioned_mark_routing.py) separately check the
unshifted two-coordinate Gaussian identity and the pointwise marked
domination. [The marked-resummation
tests](../../tests/test_marked_seed_resummation.py) separately check the
finite-family collision, connector, scale susceptibility, and exponent
ledger; none of these executable checks certifies regulator-uniform
mathematical truth.

## Exact boundary

- Equations (4), (6), and (10) prove the finite whole-integrand
  mixed-difference/Cauchy lemma. They remove an artificial Leibniz
  multiplicity from the list of possible obstructions.
- Equations (14)--(15) reduce direct marked weakening to one positive
  seed-dependent kernel. They do not bound that kernel for the actual
  activities.
- Equations (17)--(18) state a sufficient interface for a general
  weakening-dependent mark, not a theorem imported from RG II. For the
  actual source-faithful plaquette routing, Note 0025 proves the stronger
  specialization (19)--(19b) directly from the seed cutoff.
- Equation (24) corrects the conditional ledger to a parallel fork. It
  confirms the Note-0021 endpoint if the total pre-gluing marked cost is at
  most two \(\delta\)-units and all gluing/resummation hypotheses hold.
- The fixed-term marked conditioned-contour envelope is now proved in Note
  0025 with zero relative-moment cost. Note 0026 subsequently proves the
  positive \(A\)-to-output resummation, marked norm, and connected derivative
  at \(t=0\) on one fixed gas, and Note 0027 subsequently synchronizes the
  complete nested shifted first jets. No nonzero-source polymer-activity disk
  or physical \(U/J\) pullback is proved here.
- Subsequent Note 0023 proves an output-animal bound, literal-union hull
  crosswalk, and sufficient pinned Kotecky--Preiss criterion for a declared
  standard closed-cube, one-species support model. Note 0024 identifies the
  final connected ordinary RG-II gas with that model and supplies an explicit
  sufficient displayed-hierarchy ordinary smallness window. Note 0026
  supplies the aggregated decorated marked species and norm under its
  doubled-amplitude refinement.
- No large-field estimate, RG iteration, continuum construction, axiomatic
  reconstruction, infrared decay estimate, or Yang--Mills mass gap follows.

## Falsification checklist

- Estimate the factors in (11) separately and compare the resulting
  \(2^{|S|}\) with the single-contour bound (10).
- For a hypothetical weakening-dependent mark, produce an argument outside
  the common polydisc and invalidate (9), even if the unmarked integrand
  remains analytic.
- Replace the joint bound (17) by separate \(L^1\) bounds and use
  counterexample 3.
- Spend a smaller marked radius without paying (13).
- Append a one-\(\delta\) marked loss after the entire unmarked chain instead
  of using the fork (21)--(24), and obtain the wrong endpoint.
- Use (15) as an actual Yang--Mills activity estimate before bounding
  \(K_\pi^\bullet(C,A)\), or use (18b) before bounding
  \(K_\pi^{(0)}(C,A)\).
