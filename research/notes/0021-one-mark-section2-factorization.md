# Note 0021: one marked component through the RG-II Section-2 map

Claim ID: YM-RG-021

Kind: exact finite-regulator marked-component identity plus conditional norm
interface

Evidence: E2 (finite-regulator algebra; conditional estimate under named
marked hypotheses; internally checked)

Novelty: none claimed

Primary anchor: T. Balaban, [*Renormalization Group Approach to Lattice
Gauge Field Theories II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), especially Eqs.
(2.1)--(2.11) and Lemma 3.

## Scope and source boundary

This note closes the finite algebraic gap left in Note 0020 between a rooted
plaquette activity before RG II Section 2 and the differentiated activity of
the resulting fixed hard-core gas. Work at one finite regulator, on one fixed
RG-II localization partition \(\pi\), with a plaquette \(p\) strictly inside
its root cell \(Q_p\). Freeze the background and the global cutoff, Gaussian
measure, quadratic operator, coordinate chart, and localization rules at
their source-free values. The domains and restricted operators derived after
choosing a seed are rerun with that marked seed; they are not copied from an
unmarked term.

The source paper is unmarked. It proves the unmarked Section-2 construction
and its component factorization. The distinguished-source formulas below are
repository corollaries obtained by differentiating the finite algebra itself.
They are not a marked theorem printed by Balaban, and no source-free
inequality is differentiated.

Use the localized unmarked potentials \(V(Y,B)\) at the entrance to RG II
Eq. (2.1), suppressing the fixed background arguments. Assume the exact
fixed-partition rooted identity from Note 0012,

\[
\Delta_p(B)=\sum_{A\supset Q_p}W_{k,p}(A,B),
\tag{1}
\]

where the sum is finite at the regulator, every admitted \(A\) is connected
to \(Q_p\) in the same localization geometry, and each \(W_{k,p}(A)\) is
local on \(A\). Equation (1), not merely the plaquette label on
\(\Delta_p\), supplies the support needed below.

## One exact source family

After removing the source- and \(B\)-independent scalar from Note 0011, define

\[
\mathscr I_{p,\pi}(t)=
\int \chi_\pi(B)
\exp\!\left\{
\sum_YV(Y,B)-t\sum_{A\supset Q_p}W_{k,p}(A,B)
\right\}
\,d\mu_\pi(B).
\tag{2}
\]

By (1), this is exactly the fixed-partition fluctuation integral with the
physical factor \(e^{-t\Delta_p}\). At a finite regulator the cutoff integral
is finite-dimensional, the sums are finite, and differentiation at zero is
legitimate. This statement supplies no regulator-uniform complex source disk.

For a finite subset \(D\) of the unmarked potential labels, put

\[
G_D(B,\mathbf s)=
\prod_{Y\in D}V(Y,B)e^{s_YV(Y,B)},
\qquad \mathbf s\in[0,1]^D,
\tag{3}
\]

with \(G_\varnothing=1\). The elementary Mayer identity used at RG II
Eq. (2.1) gives

\[
e^{\sum_YV(Y,B)}
=\sum_{D}\int_{[0,1]^D}G_D(B,\mathbf s)\,d\mathbf s.
\tag{4}
\]

Therefore

\[
-\mathscr I'_{p,\pi}(0)
=\sum_{A\supset Q_p}\sum_D
\int_{[0,1]^D}\!d\mathbf s
\int \chi_\pi(B)W_{k,p}(A,B)G_D(B,\mathbf s)\,d\mu_\pi(B).
\tag{5}
\]

There is no factorial in (4)--(5): \(D\) is an unordered subset at this
stage. Every summand in (5) has the marked seed

\[
Y_0^\bullet=A\cup\bigcup_{Y\in D}Y.
\tag{6}
\]

The \(D=\varnothing\) term retains the bare mark \(A\). Omitting \(A\) from
(6), or omitting the empty \(D\), destroys the exact identity.

## The finite Section-2 operator

For a fixed seed, RG II Eqs. (2.2)--(2.9) perform finite
source-independent operations: support bookkeeping, inclusion--exclusion over
the auxiliary bond set, enlargement to \(Z_0\), Gaussian conditioning and
local change of variables, covariance weakening, local integration, and
resummation into \(H(Z,Z_0)\) and then \(H(Z)\). Each operation is linear in
one distinguished integrand when all unmarked decorations are held fixed.

More precisely, Eq. (2.3)'s exterior-bond subset \(P\) retains its unmarked
sign \((-1)^{|P|}\), while the smallest \(Z_0\) is now required to contain
\(Y_0^\bullet\) and \(P\). This changes the inside/outside split, allowed
\(P\)'s, conditioned restriction, smallest next-partition cover \(Z_0'\),
weakening-index family, and allowed outputs \(Z\) combinatorially as \(A\)
changes. Equations (2.5)--(2.7) nevertheless use the same source-independent
global quadratic operator, determinant convention, standard-Gaussian rule,
and resolvent construction; no \(t\)-derivative of those objects appears.
The immutable-page correction in Note 0025 shows that Eqs. (2.5)--(2.6)
leave a localized factor as \(F(Z_0,B)\): standardization acts only on the
exterior \(B'=(C^{(k)})^{1/2}X\). Equation (2.8) weakens the global
covariance/operator sector, while the inserted \(W_{k,p}(A,B)\) remains a
function of the conditional interior \(B\), independent of the second-stage
weakening variables and \(X\). Its weakening derivatives therefore do not
hit the mark. The distinguished slot remains linear, but it is still not a
factor multiplying a previously constructed \(H(Z)\): changing \(A\)
changes the seed-derived cutoff split, \(P,Z_0,\widetilde Z'_0\), active
weakening family, and allowed outputs.

Denote their composite distinguished-slot map by

\[
\mathcal T_{\pi;Z,Z_0,A}
\bigl[W_{k,p}(A)\bigr].
\tag{7}
\]

The notation includes the sums and integrals over \(D\), \(\mathbf s\), the
auxiliary bonds, conditioning data, and weakening variables compatible with
the marked seed (6). It is linear in the displayed \(W_{k,p}(A)\), but it
depends nonlinearly on the frozen unmarked family \(V\). Define

\[
H_p^\bullet(Z,Z_0)
=\sum_{A\supset Q_p}
\mathcal T_{\pi;Z,Z_0,A}[W_{k,p}(A)],
\tag{8}
\]

and use the same \(Z_0\)-resummation convention as the source,

\[
H_p^\bullet(Z)=
\sum_{Z_0:\,Z_0'\rightsquigarrow Z}H_p^\bullet(Z,Z_0).
\tag{9}
\]

Here \(Z_0'\rightsquigarrow Z\) denotes the precise assignment in RG II
Eqs. (2.8)--(2.9), after passing to the smallest next-partition cube union
\(Z_0'\). The arrow is only an abbreviation for the source's allowed
weakening outputs, not a new geometric relation.

Equivalently, run the same finite construction on (2) and call its output
\(H_{p,t}(Z,Z_0)\) and \(H_{p,t}(Z)\). Only its first jet is needed: all
formulas may be read in the dual-number ring
\(\mathbb C[t]/(t^2)\), so this notation does not assert a full
source-dependent RG induction. Since all maps following the source insertion
are \(t\)-independent and the sums are finite,

\[
H_p^\bullet(Z,Z_0)
=-\left.\partial_tH_{p,t}(Z,Z_0)\right|_{t=0},
\qquad
H_p^\bullet(Z)
=-\left.\partial_tH_{p,t}(Z)\right|_{t=0}.
\tag{10}
\]

Thus the post-Section-2 mark is the exact **linear image** of the entire
pre-Section-2 family. It is not generally equal to any single
\(W_{k,p}(A)\): the unmarked Mayer factors, cutoff decomposition,
conditioning, weakening, and local integrations decorate it.

## The unique marked component

Let

\[
Z=Z_1\sqcup\cdots\sqcup Z_m
\tag{11}
\]

be the decomposition into the connected components used at RG II Eq. (2.10).
Every nonzero marked contribution contains its seed (6), hence contains the
connected set \(A\supset Q_p\). Consequently exactly one component, denoted
\(Z_*\), contains \(Q_p\). All source-independent choices supported in the
other components resum exactly as in the unmarked construction.

For a connected output polymer \(C\), define the positive physical-sign
post-polymerization mark

\[
W_p^{\rm post}(C)
:=H_p^\bullet(C)
=-\left.\partial_tH_{p,t}(C)\right|_{t=0}.
\tag{12}
\]

Before using rootedness, ordinary product differentiation gives

\[
H_p^\bullet(Z)=
\sum_{i=1}^m H_p^\bullet(Z_i)
\prod_{j\ne i}H(Z_j).
\tag{13}
\]

Rootedness makes every summand but the unique \(i=*\) vanish. Hence

\[
H_p^\bullet(Z)=
\begin{cases}
W_p^{\rm post}(Z_*)\displaystyle\prod_{i\ne *}H(Z_i),
& Q_p\subset Z,\\[6pt]
0,&Q_p\not\subset Z.
\end{cases}
\tag{14}
\]

This is the one-mark analogue of RG II Eq. (2.10). It can also be obtained by
differentiating that finite product: only the unique root-containing factor
has nonzero derivative. There is no sum over possible marked components and
no extra combinatorial coefficient.

Combining (8), (9), and (12) gives the promised exact map

\[
\boxed{
W_p^{\rm post}(C)
=\sum_{A\supset Q_p}
\mathcal T_{\pi;C,A}[W_{k,p}(A)]
}
\tag{15}
\]

for connected \(C\), where \(\mathcal T_{\pi;C,A}\) includes the source's
\(Z_0\)-resummation. Equation (15) is an algebraic identification, not a
bound on the operator \(\mathcal T\).

## Exact hard-core numerator

Let \(\zeta(C,C')\) be RG II Eq. (2.11)'s compatibility indicator, including
its full-wall incompatibility convention. The unmarked gas is

\[
\mathcal Z_\pi=
1+\sum_{n\ge1}\frac1{n!}
\sum_{C_1,\ldots,C_n}
\prod_{i<j}\zeta(C_i,C_j)\prod_iH(C_i).
\tag{16}
\]

At finite regulator this is a finite hard-core polynomial written in ordered
notation. Define the gas compatible with one fixed connected mark by

\[
\mathcal Z_\pi[C]=
\sum_{n\ge0}\frac1{n!}
\sum_{C_1,\ldots,C_n}
\left(\prod_i\zeta(C,C_i)\right)
\left(\prod_{i<j}\zeta(C_i,C_j)\right)
\prod_iH(C_i).
\tag{17}
\]

Equations (5), (10), and (14) give

\[
\boxed{
-\mathscr I'_{p,\pi}(0)
=\sum_{C\supset Q_p}W_p^{\rm post}(C)\,\mathcal Z_\pi[C].
}
\tag{18}
\]

If the source-independent scalar removed in defining (2) is restored, it
multiplies both \(\mathscr I(0)\) and the right side of (18), so it cancels
from the normalized ratio. Whenever \(\mathscr I_{p,\pi}(0)\ne0\),

\[
-\left.\partial_t\log\mathscr I_{p,\pi}(t)\right|_{t=0}
=\frac{
\sum_{C\supset Q_p}W_p^{\rm post}(C)\mathcal Z_\pi[C]
}{\mathcal Z_\pi}.
\tag{19}
\]

Equation (19) is the exact finite numerator/denominator identity. Applying
Note 0020's distinguished-vertex Ursell formula to (19) uses
\(M_p=-W_p^{\rm post}\) in the \(+\partial_t\log\) convention, or uses
\(+W_p^{\rm post}\) directly in the \(-\partial_t\log\) convention. The
formal connected series additionally requires a formal-power-series
interpretation, and evaluation at the physical activities requires absolute
convergence. Neither follows from (19).

Equation (19) is only the fluctuation contribution. The full plaquette first
jet of Note 0011 is its explicit minimizing-background term
\(\mathcal O_p^{\rm bg}\) plus (19); the background term is not a polymer-gas
mark.

## Fixed-term domination and the remaining decay interface

The exact map (15) does not by itself bound the sum over marked seeds. In
particular, the unmarked estimate on \(H\) in RG II Lemma 3 contains no
information about \(-\partial_tH_{p,t}|_{t=0}\). Let

\[
\mathcal B_\bullet=
\sup_p\sum_{A\supset Q_p}
e^{(1-2\delta)\kappa d_k(A)}
\lVert W_{k,p}(A)\rVert_{\mathrm{Eq.\ (1.34)}|_A}.
\tag{20}
\]

Note 0025 proves the direct fixed-term estimate on the exact source routing,
using its fixed positive Gaussian base
\(d\lambda_\gamma^\sigma=d\mu_I(X)d\mu_{K_\gamma(\sigma)}(B)\), with
\(K_\gamma(\sigma)=(\operatorname{Re}
[C^{(k)}(Z_0,\sigma)^{-1}])^{-1}\), and putting every determinant, cutoff,
absolute-density, and ordinary factor in the integrand. On the same ordinary
contour set \(\mathcal C_\gamma\),

\[
\sup_{(\sigma,\tau)\in\mathcal C_\gamma}
\int
|\mathcal I_\gamma^\bullet(A;\sigma,\tau;B,X)|
\,d\lambda_\gamma^\sigma(B,X)
\le
\lVert W_{k,p}(A)\rVert_{\mathrm{Eq.\ (1.34)}|_A}
q_\gamma^{(0)}.
\tag{20a}
\]

Here \(q_\gamma^{(0)}\) is the same positive conditioned-contour majorant as
for the ordinary term with the **enlarged marked seed** (6). The interior
cutoff controls every \(B\)-coordinate of the mark, and the mark has no
second-stage weakening or \(X\) argument. Thus (20a) uses the source radius,
has no relative Gaussian moment, and costs \(r_{\rm mom}=0\).

The remaining implication assumes the following for this fixed partition.

1. **Marked seed resummation and gluing.** The positive terms (20a), summed
   over \(A,D,P,Z_0\) and the later localization choices, obey a rooted
   \(A\)-to-output kernel estimate. The seed (6), every enlargement, and its
   output obey the marked versions of the source's tree-gluing inequalities,
   including the scale conversion

   \[
   2d_k(Z_i^\bullet)
   \ge Ld_{k+1}((Z_i^\bullet)').
   \tag{21}
   \]

2. **Uniform ordinary smallness.** Every source-free resummation and entropy
   hypothesis used in Lemma 3 holds with constants independent of \(p\), the
   regulator, and the admitted background.

These remaining hypotheses are not consequences of the printed source-free
bound. The loss ledger is a fork, not an additive chain. Write the total
unproved geometric pre-gluing overhead as

\[
r\delta\kappa
=(r_{\rm root}+r_{\rm other})\delta\kappa,
\qquad r_{\rm mom}=0.
\tag{20b}
\]

The marked input and ordinary \(D/Y_0\) resummation run in parallel.
Assuming gluing has no further uncharged metric-proportional loss, it retains
the weaker branch; the four later source losses then give

\[
\begin{aligned}
&\left(1-2\delta\longrightarrow1-(2+r)\delta\right)
\quad\parallel\quad
\left(1-2\delta\longrightarrow1-4\delta\right),\\
&\hspace{9mm}\xrightarrow{\text{gluing and four later losses}}
1-\bigl(\max\{4,2+r\}+4\bigr)\delta
=1-8\delta,
\qquad r\le2.
\end{aligned}
\tag{22}
\]

Thus the conditional marked Lemma-3 implication is

\[
|W_p^{\rm post}(C)|
\le C_{\rm sec}\mathcal B_\bullet
\exp\!\left[-(1-8\delta)\frac L2\kappa
d_{k+1}(C)\right].
\tag{23}
\]

Here \(C_{\rm sec}\) is uniform only if hypotheses 1--2 are uniform. Equation
(23) is not established for the Yang--Mills activities until those hypotheses
are proved term by term.

Subsequent [Note 0026](0026-marked-seed-resummation.md) performs that
term-by-term proof for the source-faithful plaquette mark on one fixed
partition. Its coloured \(D\)-family lemma, \(P/Y_0/Z_0\) resummation, and
positive scale susceptibility discharge hypotheses 1--2 under the explicit
extra requirement that every scale-stage ordinary smallness condition holds
also at \(2\varepsilon _2\). In that scope, (23) holds with
\[
C_{\rm sec}=4K_{\rm lift}\alpha _6^{-1}.
\]
The fork ledger (20b)--(22) is retained as the earlier conditional
bookkeeping route; Note 0026 supplies the sharper direct proof.

## Pointwise decay is not the rooted norm

Even conditional (23) does not give a rooted \(\ell^1\) norm at the same
exponent. Define the explicit output-animal constant

\[
C_{\rm an}(\eta)=
\sup_Q\sum_{C\supset Q}e^{-\eta d_{k+1}(C)}.
\tag{24}
\]

Assume \(C_{\rm an}(\eta)<\infty\) uniformly. For

\[
a_{\rm post}=(1-8\delta)\frac L2\kappa-\eta,
\tag{25}
\]

(23) yields

\[
\sup_p\sum_{C\supset \widehat Q_p}
e^{a_{\rm post}d_{k+1}(C)}|W_p^{\rm post}(C)|
\le C_{\rm sec}C_{\rm an}(\eta)\mathcal B_\bullet,
\tag{26}
\]

where \(\widehat Q_p\) is the named next-scale output root assigned to
\(Q_p\). Choosing one explicit \(\delta\)-unit of entropy slack,

\[
\eta=\delta\frac L2\kappa,
\qquad
a_{\rm post}=(1-9\delta)\frac L2\kappa,
\tag{27}
\]

requires \(\delta<1/9\) for a positive exponent and a sufficiently large
animal-entropy margin. Subsequent Note 0023 proves, for its declared standard
\(D\)-dimensional closed-cube support model,

\[
C_{\rm an}^{\rm geom}(\eta)
\le
\frac{S_D}{1-(2D)^{2^{D+1}}e^{-\eta/2}},
\qquad
\eta>2^{D+2}\log(2D),
\quad
S_D=\sum_{j=0}^{2^D-1}(2D)^{2j}.
\tag{28}
\]

In \(D=4\), using the one-\(\delta\) choice in (27) therefore requires the
additional strict numerical condition
\(\delta(L/2)\kappa>64\log8\). Note 0023 also supplies a literal-union hull
and a conditional pinned Kotecky--Preiss criterion in that same model.
Subsequent Note 0024 identifies the final connected ordinary RG-II gas with
the model and gives a sufficient displayed-hierarchy ordinary-activity
window. Subsequent Note 0026 identifies the already aggregated decorated
marked output, proves (26) with
\(C_{\rm an}=C_{\rm an}^{\rm geom}\), and closes the fixed-partition
connected first-jet sum. The budget still leaves one further
\(\delta\)-unit before the source's unmarked connected-output exponent
\((1-10\delta)(L/2)\kappa\).

## Fixed partition, shifts, and the physical pullback

Everything above is performed on one partition \(\pi\) on which both the
unmarked construction and the rooted identity (1) are valid. For a shifted
partition \(\pi^\sigma\), one must repeat (2)--(19) on that same branch. The
resulting \(W_{p,\sigma}^{\rm post}\), compatibility relation, and denominator
remain \(\sigma\)-labelled until Note 0020's synchronization hypothesis is
proved. Averaging the bare \(W_{k,p}^\sigma\) before this nonlinear step is not
licensed.

Subsequent Note 0027 proves that synchronization hypothesis at first-jet
level. It lifts the shifts to nested input/output cubulations, proves the
shifted unmarked Lemma-2 reconstruction, applies this finite algebra to the
same dual-number integral on every separate gas, and only then averages the
completed connected coefficients. It does not average the bare activities or
construct one mixed-shift gas.

Likewise, (15) is local in the independent \((U,J,B)\) coordinates used by
RG II. Substitution of the physical minimizing background requires the
separate \(U\)- and \(J\)-pullback theorems isolated in Notes 0015--0019.
Nothing in the finite Section-2 algebra supplies those estimates.

## Executable coefficient checks

[The marked-component tests](../../tests/test_marked_component_factorization.py)
use exact rational first jets to check the unique-root specialization of
(13)--(14) and the hard-core numerator (18) in small finite products and
gases. They also insert a \(t\)-dependent auxiliary multiplier and recover the
extra derivative term excluded by the frozen-source hypotheses. They do not
test the Mayer seed, the decorated map (15), the logarithmic division in (19),
the ordered-sum factorial/repeated-label convention already tested in Note
0020, or any RG-II conditioning, weakening, geometry, or estimate.
[The marked-resummation
tests](../../tests/test_marked_seed_resummation.py) separately check the
finite-family collision, connector, susceptibility, constant, and exponent
algebra used by Note 0026.

## Exact boundary

- Equations (2)--(19) prove, at one finite regulator and on one fixed
  compatible partition, the exact passage of a unique rooted source
  derivative through RG II Eqs. (2.1)--(2.10), the definition (12) of
  \(W_p^{\rm post}\), the unique marked-component factorization, and the
  finite hard-core numerator identity.
- Equation (15) identifies \(W_p^{\rm post}\) as a decorated linear image of
  the complete pre-Section-2 family. It does not identify it termwise with a
  bare \(W_{k,p}(A)\).
- Equations (23) and (26) were derived here as conditional implications under
  marked-seed resummation, gluing, uniform-smallness, and output-animal
  hypotheses. Note 0025 proves the direct fixed-term conditioned-contour
  domination (20a), and Note 0026 subsequently discharges those positive
  resummation and animal hypotheses on one fixed partition under its explicit
  doubled-amplitude refinement.
- Subsequent Note 0023 proves the output-animal estimate (28), a
  literal-union hull crosswalk, and a sufficient pinned-KP implication for
  its declared standard-cubical one-species model. Note 0024 identifies the
  final ordinary source class, quotient seams, metric, and aggregated
  ordinary species and supplies an explicit displayed-hierarchy smallness
  window. Note 0026 supplies the actual aggregated decorated marked norm and
  controls its distinguished-component multiplicity by one positive
  susceptibility.
- No unmarked inequality has been differentiated. A common complex-source
  Lemma-3 theorem plus Cauchy would be an alternative route, but no such
  theorem is imported here.
- Note 0026 proves absolute convergence of the connected first derivative at
  \(t=0\) for the fixed gas under Note 0024's separate ordinary KP ceiling,
  and Note 0027 subsequently synchronizes all nested shifted first jets. The
  selected-coordinate scalar zero-free disk was already proved in Notes 0007
  and 0010. Source-dependent polymer activities and KP convergence at
  nonzero source remain open.
- The physical nonlinear \(U\) pullback, discharge of Note 0019's geometric
  premises, marginal projection, large fields, RG iteration, continuum
  construction, Osterwalder--Schrader axioms, infrared decay, and the
  Yang--Mills mass gap remain open.

## Falsification checklist

- Replace the source-independent cutoff or covariance by a \(t\)-dependent
  one and recover the additional derivative terms omitted by (10).
- Delete \(A\) from (6) and observe that the output need not contain \(Q_p\).
- Delete the \(D=\varnothing\) term and lose the undecorated marked activity.
- Differentiate a bound known only at \(t=0\): the toy family
  \(H_t=H_0+tN\) has arbitrary derivative \(N\) with the same \(H_0\).
- Put the mark in two components of (11) and contradict the fact that every
  marked seed contains the one connected root \(A\supset Q_p\).
- Shift the mark by the standardized exterior \(X\), or give it a
  second-stage \(\sigma\)-argument, and compare with the source-faithful
  routing in Eqs. (2.5)--(2.14).
- Replace (15) by \(W_p^{\rm post}=W_{k,p}\) and expose the missing
  seed-dependent cutoff split, decorations, conditioning, weakening, and
  integration.
- Use the full exponent in (23) inside the rooted sum and observe that all
  decay is canceled before output-animal entropy is paid.
- Mix shifted activities before forming their branch denominators and recover
  Note 0020's finite counterexample.
