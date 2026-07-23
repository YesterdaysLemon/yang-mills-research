# Note 0023: fixed-cubical hull, animal entropy, and pinned KP

Claim ID: YM-RG-023

Kind: elementary cubical geometry plus a conditional fixed-gas estimate

Evidence: E2 (complete finite-dimensional proofs under an explicit standard
cubical support model; the final ordinary RG-II gas is identified with this
model and given an explicit displayed-hierarchy-compatible smallness window
only in subsequent Note 0024; no marked activity estimate)

Novelty: none claimed

Primary convention anchor: T. Balaban, [*Renormalization Group Approach to
Lattice Gauge Field Theories II. Cluster
Expansions*](https://doi.org/10.1007/BF01239022), especially Eqs.
(2.11)--(2.13).

Pinned-cluster anchor: R. Fernandez and A. Procacci,
[*Cluster expansion for abstract polymer models. New bounds from an old
approach*](https://arxiv.org/abs/math-ph/0605041v2), version 2, Eqs. (2.7),
(2.14), and (2.15).

## Scope and source boundary

Note 0020 isolated three geometric and analytic premises for its rooted
cluster estimate: an admitted hull, the weighted hull crosswalk, and the
pinned Kotecky--Preiss condition. Note 0021 separately needed a
volume-uniform output-animal constant. This note proves one explicit
sufficient package for all four statements in a **standard cubical support
model**.

The source supplies the motivating incompatibility convention: two RG-II
polymers are incompatible when their supports share a cube or a complete
cube wall. It does not state the theorem below with this note's connector,
animal, or numerical constants; those are repository results. This note by
itself does not identify the source class with the declared model.
Subsequent [Note
0024](0024-balaban-final-gas-instantiation.md) performs that primary-source
crosswalk for the **final connected ordinary gas after RG II Eq. (2.10)**,
using the monotone-metric extension proved below, and supplies one explicit
ordinary KP sub-hierarchy. It does not identify the intermediate support
families or any marked activity.

## The fixed cubical model

Let \(D\ge1\) and let \(\mathcal Q\) be a regular cubulation by closed
axis-aligned \(D\)-cubes of side \(s>0\), either in a box or in a flat
periodic torus. Across a periodic seam, cells, paths, and lengths are read in
the quotient cubical complex, not as separated representatives in a chosen
fundamental domain.

A cubical polymer \(Y\) is a nonempty finite face-connected set of cube
labels. Its realization \(|Y|\) is the union of the corresponding closed
cells, and

\[
 N(Y)=|Y|_{\rm cubes}
\tag{1}
\]

denotes its number of cubes. Define the normalized piecewise-linear contained-tree
metric

\[
 d_{\mathcal Q}(Y)
 =\frac1s\inf_T\mathcal H^1(T),
\tag{2}
\]

where \(T\subset |Y|\) ranges over finite piecewise-linear embedded tree
graphs meeting every constituent closed cube; a degenerate one-vertex tree
is allowed. A point on a common face meets both incident cubes. Thus (2) is
not a lattice-bond tree metric, and adjacent closed cubes can have zero
distance. The piecewise-linear restriction also makes the finite-graph
pruning step below literal rather than invoking a compact-continuum theorem.

Assume throughout the geometric and KP statements that:

1. every input and output uses this same cubulation and metric;
2. the output class contains every finite face-connected literal union;
3. incompatibility is symmetric and reflexive and can occur only when two
   supports share a full cube or contain cubes sharing a complete elementary
   face; and
4. the occurrence graph of every tuple being grouped is connected.

Assumption 3 matches the geometric content needed from RG II Eq. (2.11). It
is deliberately stated as an implication: any additional nonlocal
incompatibility would require a new connector theorem.

## The literal-union hull theorem

For a distinguished occurrence \(A\) and \(n\) ordinary occurrences, put

\[
 R=\operatorname{Hull}_{\mathcal Q}(A,X_1,\ldots,X_n)
 :=A\cup X_1\cup\cdots\cup X_n
\tag{3}
\]

as a union of cube labels. Occurrences, including repeated labels, are
counted with multiplicity in \(n\).

The connected occurrence graph and Assumption 3 make \(R\) face-connected,
so it is admitted. It is also the unique least cubical support containing
every occurrence. If \(A\supset Q_p\), then \(R\supset Q_p\).

Most importantly,

\[
\boxed{
 d_{\mathcal Q}(R)
 \le d_{\mathcal Q}(A)
 +\sum_{i=1}^n d_{\mathcal Q}(X_i)
 +b_D n,
 \qquad b_D=\sqrt{D+3}.}
\tag{4}
\]

To prove (4), select a spanning tree of the occurrence graph and an
epsilon-minimizing contained tree in each occurrence. For each of the \(n\)
spanning-tree edges:

- if the supports share a cube, join the two input trees inside that cube at
  cost at most \(s\sqrt D\);
- if they meet across a complete face, use a seam-compatible local lift. The
  two incident cubes form
  \([0,2s]\times[0,s]^{D-1}\), whose diameter is
  \(s\sqrt{D+3}\).

The input trees and connectors form a connected finite graph inside \(R\)
meeting every cube. Subdivide at the witnesses and intersections and take a
graph-theoretic spanning tree. Its length is no larger than the graph's
total length. Divide by \(s\) and let epsilon tend to zero.

For \(D=4\), the shared-cube and face-contact costs furnished by this proof
are respectively \(2\) and \(\sqrt7\). The latter is safe, not asserted
optimal.

The additive contact charge cannot be discarded. In one dimension take
three consecutive closed unit cells \(Q_0,Q_1,Q_2\), with

\[
 A=Q_0\cup Q_1,
 \qquad X=Q_2.
\tag{5}
\]

A face point meets both cells of \(A\), so \(d(A)=d(X)=0\), whereas
\(d(A\cup X)=1\). Hence the putative inequality
\(d(R)\le d(A)+d(X)\) is false. Repeated occurrences need not enlarge the
literal union, but (4) safely overcounts their metric and contact terms just
as the ordered Ursell series retains them.

## Cube count from the contained-tree metric

Let

\[
 B_D=2^D.
\tag{6}
\]

Every cubical polymer obeys the volume-uniform estimate

\[
\boxed{
 N(Y)\le B_D\bigl(\lfloor2d_{\mathcal Q}(Y)\rfloor+1\bigr)
 \le B_D+2B_Dd_{\mathcal Q}(Y).}
\tag{7}
\]

Indeed, let a contained tree have length \(\ell\). A depth-first tour of a
finite tree has length at most \(2\ell\). Split its parameter interval into
\(\lfloor2\ell/s\rfloor+1\) subintervals of length strictly less than
\(s\). The midpoint images give open Euclidean balls of radius \(s/2\)
covering the tree. In each coordinate, an open interval of length \(s\)
meets at most two closed grid intervals; hence each ball meets at most
\(2^D\) closed cubes. The same local statement holds in the quotient at a
periodic seam. Let \(\ell\downarrow s d_{\mathcal Q}(Y)\). This also handles
a non-attained infimum in (2).

At distance zero, (7) permits up to \(2^D\) closed cubes meeting at one grid
vertex. That boundary multiplicity is why no smaller zero-distance constant
is used.

## Rooted animal count and an explicit entropy constant

Fix a root cube \(Q\). If \(m=N(Y)-1\), the number of face-connected
unlabelled supports of \(m+1\) cubes containing \(Q\) satisfies

\[
 \#\mathcal A_m(Q)\le q_D^{2m},
 \qquad q_D=2D.
\tag{8}
\]

Fix a global order of the \(2D\) coordinate directions. Choose
deterministically a spanning tree of each support and use that order to fix
its depth-first child traversal starting at \(Q\). Its \(m\) edges are
traversed twice, with at most \(2D\) direction labels at each step. The
resulting direction word determines its visited support, so the canonical
assignment is injective.
The same upper bound holds on a periodic cubulation; identifications can only
reduce the number of distinct direction-labelled neighbors.

Define the purely geometric animal constant

\[
 C_{\rm an}^{\rm geom}(\eta)
 =\sup_Q\sum_{Y\in\mathcal A(Q)}e^{-\eta d_{\mathcal Q}(Y)},
\tag{9}
\]

where every unlabelled support appears once. From (7),

\[
 d_{\mathcal Q}(Y)
 \ge\frac12\left(\left\lceil\frac{m+1}{B_D}\right\rceil-1\right).
\tag{10}
\]

Put

\[
 S_D=\sum_{j=0}^{B_D-1}q_D^{2j}
 =\frac{q_D^{2B_D}-1}{q_D^2-1}.
\tag{11}
\]

Grouping \(m=rB_D+j\) in (8)--(10) gives

\[
\boxed{
 C_{\rm an}^{\rm geom}(\eta)
 \le
 \frac{S_D}{1-q_D^{2B_D}e^{-\eta/2}}}
\tag{12}
\]

whenever

\[
\boxed{
 \eta>4B_D\log q_D
 =2^{D+2}\log(2D).}
\tag{13}
\]

This is a crude sufficient threshold, not a necessary one. In four
dimensions,

\[
 B_4=16,
 \quad q_4=8,
 \quad \eta>64\log8\approx133.084,
 \quad
 C_{\rm an}^{\rm geom}(\eta)
 \le\frac{(8^{32}-1)/63}{1-8^{32}e^{-\eta/2}}.
\tag{14}
\]

A finite torus has finitely many supports even below (13), but that fact
alone supplies no volume-uniform constant.

## Monotone-metric extension

The zero-length convention in (2) is useful for a conservative animal
majorant, but it need not be identified with a source's tree-size convention.
Let \(\widetilde d\) be another nonnegative function on the same cubical
supports such that

\[
d_{\mathcal Q}(Y)\le\widetilde d(Y)
\tag{15a}
\]

and, for every connected occurrence tuple,

\[
\widetilde d(R)
\le\widetilde d(A)+\sum_{i=1}^n\widetilde d(X_i)+b_Dn.
\tag{15b}
\]

Then (7) implies the safe affine bound

\[
N(Y)\le B_D+2B_D\widetilde d(Y),
\tag{15c}
\]

and the rooted animal sum in the larger metric is bounded by the already
computed auxiliary constant:

\[
\sup_Q\sum_{Y\ni Q}e^{-\eta\widetilde d(Y)}
\le C_{\rm an}^{\rm geom}(\eta).
\tag{15d}
\]

Consequently every pinned-KP and rooted-output argument below remains valid,
with exactly the same constants, after replacing every activity, hull, and
output occurrence of \(d_{\mathcal Q}\) by \(\widetilde d\). Equations
(15c)--(15d) replace the only cube-count and animal-sum uses, while (15b)
replaces the hull connector. No equality of the two metrics is required.

## A concrete pinned KP criterion

Now assume one ordinary polymer species per cubical support. Let its activity
obey

\[
 |H(X)|\le h e^{-\beta d_{\mathcal Q}(X)}
\tag{15}
\]

uniformly. For \(\alpha>0\), \(a\ge0\), define the pinned and hull weights

\[
 A(X)=\alpha N(X),
 \qquad
 c(X)=a\bigl(d_{\mathcal Q}(X)+b_D\bigr).
\tag{16}
\]

The affine form of (7), rather than a coarser single-constant bound, gives

\[
 |H(X)|e^{A(X)+c(X)}
 \le h e^{\alpha B_D+a b_D}e^{-\eta d_{\mathcal Q}(X)},
 \qquad
 \eta=\beta-a-2\alpha B_D.
\tag{17}
\]

If (13) holds for this \(\eta\) and

\[
\boxed{
 (2D+1)h e^{\alpha B_D+a b_D}
 C_{\rm an}^{\rm geom}(\eta)
 \le\alpha,}
\tag{18}
\]

then the canonical pinned condition of Note 0020 holds:

\[
 \sum_{X\not\sim Y}|H(X)|e^{A(X)+c(X)}\le A(Y).
\tag{19}
\]

To see this, the closed face-neighborhood of \(Y\) has at most
\((2D+1)N(Y)\) cubes. Every polymer incompatible with \(Y\) contains a cube
in that neighborhood. Sum (17) first over a possible contact cube, use (9),
and then apply (18). Reflexivity includes \(X=Y\), as required by the pinned
theorem. The same proof applies to a distinguished root whose
incompatibilities are those of its underlying support.

If the gas has decorated species over one support, (9) must instead count
the actual species labels, and incompatibility must still be determined by
the support contact rule used above. A uniform multiplicity bound \(M\)
multiplies the left side of (18) by \(M\). A bound
\(Me^{\theta d(X)}\) replaces \(C_{\rm an}^{\rm geom}(\eta)\) by
\(M C_{\rm an}^{\rm geom}(\eta-\theta)\), and requires the strengthened
strict margin
\(\eta-\theta>4B_D\log q_D\). Unbounded unaccounted decoration
multiplicity or decoration-dependent nonlocal incompatibility invalidates
(18).

## Crosswalk to the rooted output estimate

Equation (4) implies Note 0020 Eq. (19) whenever
\(0\le a_{\rm out}\le a\):

\[
 e^{a_{\rm out}d_{\mathcal Q}(R)}
 \le e^{a_{\rm out}d_{\mathcal Q}(A)}
 \prod_{i=1}^n e^{c(X_i)}.
\tag{20}
\]

Equation (7) also gives Note 0020's pinned-root parameters with the explicit
valid affine choice

\[
 A_0=\alpha B_D,
 \qquad \epsilon=2\alpha B_D.
\tag{21}
\]

Therefore, if the post-polymerization mark independently has the norm

\[
 \sup_p\sum_{A\supset Q_p}
 e^{a_\bullet d_{\mathcal Q}(A)}|M_p(A)|
 \le\mathcal B_\bullet,
\tag{22}
\]

and

\[
 a_{\rm out}\le a,
 \qquad
 a_{\rm out}+2\alpha B_D\le a_\bullet,
\tag{23}
\]

then Note 0020 proves

\[
\boxed{
 \sup_p\sum_{R\supset Q_p}
 e^{a_{\rm out}d_{\mathcal Q}(R)}
 |\mathcal C_{p,\pi}^\bullet(R)|
 \le e^{\alpha B_D}\mathcal B_\bullet.}
\tag{24}
\]

Thus the abstract hull, animal, and pinned-KP interfaces close together under
one explicit inequality system. Equation (24) still consumes the separate
marked norm (22); no unmarked activity estimate creates it.

## Four-dimensional conditional budget

To compare with Notes 0020--0022, put

\[
 \lambda=\frac L2\kappa,
 \quad
 \beta=(1-8\delta)\lambda,
 \quad
 a_\bullet=(1-9\delta)\lambda,
 \quad
 a=a_{\rm out}=(1-10\delta)\lambda.
\tag{25}
\]

Assume here \(\lambda>0\) and \(0<\delta<1/10\), so all three displayed
decay exponents are positive.

Let \(\Delta=\delta\lambda\). Then

\[
 \eta=\beta-a-32\alpha=2\Delta-32\alpha.
\tag{26}
\]

For any gas identified with this declared model, one transparent sufficient
system is

\[
\begin{gathered}
 \Delta>64\log8,
 \qquad 0<32\alpha\le\Delta,\\
 9h\exp\{16\alpha+a_{\rm out}\sqrt7\}
 C_{\rm an}^{\rm geom}(2\Delta-32\alpha)
 \le\alpha.
\end{gathered}
\tag{27}
\]

Within this model, the first inequality makes the one-delta marked-animal
spend from Note 0021 volume-uniform. Together with the second, it also implies
\(2\Delta-32\alpha\ge\Delta>64\log8\), so the ordinary KP animal constant is
finite. The second inequality is exactly (23). A convenient choice is
\(\alpha=\Delta/64\). This note does not by itself solve the remaining
smallness inequality or attribute that choice to the source; Note 0024
subsequently proves that the final ordinary RG-II gas has a nonempty
displayed-hierarchy-compatible \(\varepsilon _1\) window satisfying it.

If the pointwise marked bound isolated conditionally in Note 0021 holds with
constant \(C_{\rm sec}\mathcal B_{\rm in}\), then (12) at
\(\eta=\Delta\) and (24) yield

\[
 \sup_p\sum_{R\supset Q_p}
 e^{(1-10\delta)\lambda d_{\mathcal Q}(R)}
 |\mathcal C_{p,\pi}^\bullet(R)|
 \le
 e^{16\alpha}C_{\rm sec}
 C_{\rm an}^{\rm geom}(\Delta)\mathcal B_{\rm in}.
\tag{28}
\]

Note 0024 subsequently discharges the class, source-metric extension, seam,
one-ordinary-species, and ordinary-amplitude/KP-window gates for the final
gas. [Note 0026](0026-marked-seed-resummation.md) then proves the marked
Lemma-3 analogue, treats the already aggregated marked output as the single
decorated species used here, and instantiates (28) with
\[
C_{\rm sec}=4K_{\rm lift}\alpha _6^{-1},
\qquad
\mathcal B_{\rm in}=\mathcal B_\bullet.
\]
This discharge is restricted to one fixed partition and its explicit
doubled-\(\varepsilon _2\) hierarchy. The large factor
\(e^{a_{\rm out}\sqrt7}\) also shows why a qualitative statement that
activities are small is not enough; the numerical hierarchy must beat the
hull-contact fugacity and the crude animal constant.

## Executable checks

[The cubical hull and animal tests](../../tests/test_cubical_hull_animals.py)
check the shared-cube and full-wall squared diameters, periodic quotient
distance, the nonzero contact-charge counterexample, exact small rooted
animal counts, the half-unit shells in (10), and the geometric-series algebra
and strict threshold in (12)--(13). They do not themselves certify the
source-class identification, any activity estimate, or the KP theorem
imported in Note 0020. The independent source mapping and ordinary parameter
window are recorded in Note 0024.

## Exact boundary

- Equations (3)--(4) prove the literal-union hull and weighted crosswalk for
  the declared closed-cube model, including full-wall incompatibility and
  periodic quotient seams.
- Equations (7)--(14) prove a volume-uniform geometric animal bound with the
  explicit sufficient four-dimensional threshold \(64\log8\).
- Equations (15a)--(15d) extend the same constants to any larger source tree
  size satisfying the same connector inequality; equality with the
  auxiliary degenerate metric is unnecessary.
- Equations (15)--(24) prove that an explicit pointwise ordinary activity
  bound and numerical smallness condition imply Note 0020's pinned KP and
  rooted output bound.
- This claim alone makes no source identification. Subsequent Note 0024
  proves that RG II's final connected ordinary gas instantiates the declared
  class, quotient-seam convention, monotone source-metric extension,
  literal-union rule, and one-species accounting, and gives a
  displayed-hierarchy-compatible ordinary \(\varepsilon _1\) window for
  (27). It explicitly excludes intermediate and marked supports.
- Note 0025 proves the fixed-term marked conditioned-contour domination.
  Note 0026 subsequently proves the positive resummation, final marked norm,
  decorated-mark multiplicity bound, and connected first derivative at
  \(t=0\) on one fixed gas, with this note's pinned step supplied by Note
  0024's separate ordinary KP ceiling. A common source disk and
  shifted-branch synchronization remain open.
- The physical \(U/J\) pullbacks, marginal projection, large fields, RG
  iteration, continuum and infinite-volume construction, axioms,
  nontriviality, infrared decay, and the Yang--Mills mass gap remain open.

## Falsification checklist

- Treat wall contact only through open interiors and lose the contained
  connector.
- Measure a periodic seam in a fundamental-domain representative and obtain
  a spurious volume-sized connector.
- Replace the literal union by a convex, rectangular, filled, fattened, or
  reblocked hull without paying for its added cubes.
- Remove the \(b_Dn\) contact charge and test (5).
- Use a lattice-bond or differently normalized tree metric with the Euclidean
  constant \(\sqrt{D+3}\).
- Identify a larger source tree size with the auxiliary degenerate metric
  instead of proving both (15a) and (15b).
- Count decorated histories as one geometric species in (9).
- Replace the strict threshold (13) by \(\eta>0\).
- Omit the factor \(e^{\alpha B_D+a b_D}\) or the closed-neighborhood factor
  \(2D+1\) from (18).
- Use the unmarked bound (15) as the marked norm (22).
- Claim the actual RG-II connected expansion before verifying every model
  identification and numerical premise listed above.
