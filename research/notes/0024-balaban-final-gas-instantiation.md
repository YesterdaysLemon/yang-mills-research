# Note 0024: Balaban final-gas cubical instantiation and an explicit KP window

Claim ID: YM-RG-024

Kind: primary-source identification plus a conditional parameter-existence
corollary

Evidence: E2 (complete support/species mapping for the final ordinary gas,
with the repository's explicit degenerate-tree and analytic-norm conventions,
and an explicit sufficient parameter window under the displayed RG-I/RG-II
hierarchy and the stated imported-monotonicity hypothesis; no marked activity
estimate)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I*](https://doi.org/10.1007/BF01215223), especially pp. 251 and
  257 and the theorem on pp. 264--265;
- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories II. Cluster Expansions*](https://doi.org/10.1007/BF01239022),
  especially Eqs. (2.8)--(2.13), Lemma 3 Eq. (2.38), and Eqs.
  (2.39)--(2.41).

Stable primary mirrors:

- [RG I at Project Euclid](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf);
- [RG II at Project Euclid](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf).

## Result and exact boundary

The final **connected ordinary polymer gas** constructed after RG II Eq.
(2.10) is an actual four-dimensional instance of the support model in Note
0023. More precisely:

1. its species are the connected localization domains
   \(Z\in\mathcal D_{k+1}\), finite face-connected unions of closed cubes;
2. its \(d_{k+1}\) is the side-length-normalized shortest contained-tree
   metric used in Note 0023;
3. its hard-core incompatibility is exactly shared-cube or complete-wall
   contact;
4. the internal \(D,P,Z_0\) histories are summed into one ordinary activity
   \(H(Z)\) per connected final support before the gas is formed; and
5. Eq. (2.13) groups a connected occurrence tuple by its literal support
   union.

This identification begins **after** the disconnected preactivity in Eq.
(2.8) has factorized in Eq. (2.10). It does not identify the intermediate
\(Y_0,Z_0,\widetilde Z_0,Z'_0,X_0\), random-walk domains, or interior-bond
completion with Note 0023's polymers or literal-union hull. In particular,
RG II forms \(Z'_0\) as a coarse \(LM\)-cube cover of \(\widetilde Z_0\), not
of bare \(Z_0\), and the phrase
"smallest localization domain" used for an intermediate completion is not
used below as a uniqueness theorem.

Under the directly inspected primary-source formula

\[
 |H(Z)|
 \le C_3\varepsilon _1
 \exp\!\left[-(1-8\delta)\frac L2\kappa
 d_{k+1}(Z)\right]
\tag{1}
\]

from Lemma 3 Eq. (2.38), with its \(U,J\) variables suppressed in the source
notation and pointwise on the relevant analytic domain, the displayed source
freedom to take \(\kappa\) sufficiently large and then
\(\varepsilon _1\) sufficiently small contains a nonempty sub-hierarchy
satisfying Note 0023's explicit four-dimensional pinned-KP criterion. This is
a repository refinement of the source hierarchy, not the cluster criterion
printed in RG II. RG I says that \(\varepsilon _1\) obeys additional
"numerous restrictions," and I/II import earlier results without enumerating
all of them. The parameter conclusion is therefore conditional on those
unlisted restrictions being preserved when \(\varepsilon _1\) is decreased,
as every displayed \(\varepsilon _1\) restriction is.

Neither statement supplies the post-polymerization marked norm. Note 0025
subsequently proves the fixed-term marked conditioned-contour domination;
marked-seed resummation and gluing, the source disk, and shifted
synchronization remain open.

## The source cubulation and quotient convention

RG I first places the lattice in continuous Euclidean space or in a continuous
torus obtained by the usual identification of opposite boundary points. It
then uses regular cubulations of that ambient space. Thus on a periodic
lattice the cells and paths live in the quotient torus; separating two
seam-adjacent cells in a chosen fundamental-domain representative would not
be the source geometry.

For each scale \(j\), RG I p. 257 rescales the ambient space to the
\(j\)-coordinates and decomposes it into a lattice \(\pi_j\) of **closed**
side-\(M\) cubes. It defines a localization domain as a union of a finite
connected family of these cubes, where connected means that successive cubes
share a complete \((D-1)\)-dimensional wall. The class of every such domain is
\(\mathcal D_j\). Therefore, with cube labels as supports,

\[
 \mathcal D_j
 =\{\text{nonempty finite face-connected unions of closed }\pi_j
 \text{ cubes}\}.
\tag{2}
\]

Equation (2) is exactly the support class declared in Note 0023. It also
contains every face-connected literal union, rather than a selected subclass
of shapes.

## Equality of the two tree metrics

RG I defines \(d_j(X)\) by taking the length of a shortest tree graph that is
contained in \(X\) and intersects every constituent cube, then dividing by
the cube side \(M\). It stresses that the graph lies in continuous space and
then states that a shortest graph can also be formed from cube edges.

The latter shortest graph is a finite piecewise-linear contained tree, so it
is admitted in Note 0023's infimum. Conversely, every tree admitted by Note
0023 is a continuous-space contained tree of the class used in RG I.
Consequently

\[
 d_j(X)=d_{\pi_j}(X).
\tag{3}
\]

In the Note-0023 formalization, a one-vertex, zero-edge tree is admitted. This
is the standard degenerate-tree convention, but RG I does not separately
spell it out. It should not be confused with a nearest-neighbor bond-tree
metric.

There are two equivalent coordinate descriptions at the second RG-II
localization:

\[
 d_{k+1}(Z)=\frac{\ell_k(Z)}{LM}
 =\frac{\ell_{k+1}(Z)}M.
\tag{4}
\]

The first uses the preceding \(k\)-scale coordinates, in which a
\(\pi_{k+1}\) cell has side \(LM\); the second rescales to the
\(k+1\)-coordinates used in the RG-I definition. Only one of these scale
factors may be applied. This note instantiates Note 0023 in the second
convention, with \(s=M\).

## Where the one final species comes from

The second localization initially has more structure than a polymer gas.
RG II Eq. (2.8) sums over possibly disconnected outputs \(Z\), with every
connected component required to contain a component of \(Z'_0\). Equation
(2.9) then defines

\[
 H(Z)=\sum_{\text{Eq. (2.9)-admissible }Z_0}H(Z,Z_0),
\tag{5}
\]

with the earlier \(D\)- and \(P\)-sums already inside the summands. The text
after Eq. (2.13) explicitly describes the final activities as sums over
\(Z_0,D,P\). Hence those histories are not extra species labels in the final
gas.

If \(Z=Z_1\cup\cdots\cup Z_r\) is disconnected, Eq. (2.10) factorizes its
preactivity over the connected components. Equation (2.11) is then the
hard-core gas whose individual polymers are the connected supports
\(Z_i\in\mathcal D_{k+1}\), each carrying the single aggregated analytic
activity \(H(Z_i)\).

RG II p. 15 places the activities contributing to a fixed final \(X\) on an
\(X\)-dependent analytic field domain. For that fixed gas, write explicitly

\[
 \lVert H(Z)\rVert_{\mathcal U(X)}
 :=\sup_{(U,J)\in\mathcal U(X)}
 |H(Z;U,J)|,
\tag{6}
\]

where the supremum is over the relevant fixed-\(X\) analytic field domain and
\(Z\subset X\). The source prints the pointwise absolute-value estimate (1),
not this norm notation; because its constants are uniform on that domain,
taking the supremum gives the same right-hand side. "One species" means one
such analytic function per connected support. It does not mean that the
function is field-independent, and it does not split the individual histories
in (5) back into decorated polymers.

## Exact incompatibility and literal output union

RG II Eq. (2.11) defines \(\zeta(Z,Z')=0\) exactly when
\(Z\cap Z'\) contains a cube or a wall of a cube, and \(\zeta=1\) otherwise.
On the aligned closed cubulation this is precisely the symmetric reflexive
rule

\[
 Z\not\sim Z'
 \quad\Longleftrightarrow\quad
 \text{the supports share a cube label or meet across a complete face}.
\tag{7}
\]

Edge-only and vertex-only contact remain compatible. A nonzero connected
graph term in the Ursell coefficient therefore gives a face-connected literal
union; a graph containing a compatible edge has zero product and contributes
nothing.

RG II Eq. (2.13) groups the connected coefficient by

\[
 X=\bigcup_{i=1}^n Z_i.
\tag{8}
\]

The same literal-union condition is used again in the estimate following
Lemma 3. Equations (2), (7), and (8) show that \(X\in\mathcal D_{k+1}\), that
it is the unique least cube-label support containing the occurrences, and
that Note 0023's connector, animal, and hull-weight theorems apply without a
decoration multiplier to this final ordinary gas.

This argument does not use the earlier phrase "smallest localization
domain." Two separated seed sets can have more than one minimal
face-connected completion, whereas the connected tuple in (8) already has
an admitted literal union.

## Lemma 3 as the ordinary pointwise input

With all source restrictions in force, RG II Lemma 3 gives (1) pointwise and
uniformly on each relevant fixed-output analytic field domain. Thus the final
gas supplies Note 0023's ordinary activity parameters

\[
 h=C_3\varepsilon _1,
 \qquad
 \beta=(1-8\delta)\lambda,
 \qquad
 \lambda=\frac L2\kappa.
\tag{9}
\]

The factor \(\exp(5\kappa)\) visible in the later Eq. (2.39) estimate is not
part of the Lemma-3 amplitude \(h\). It occurs after an additional decay
extraction in the source's own cluster summation. Conversely, Lemma 3 does
not itself print Note 0023's KP inequality or its numerical animal constant.

The immutable Project Euclid page images were inspected directly. RG II p. 20
prints \((1-8\delta)\tfrac12L\kappa\) in Eq. (2.38); p. 21 prints
\((1-9\delta)\tfrac12L\kappa\) in Eq. (2.39) and
\((1-10\delta)\tfrac12L\kappa\) in Eq. (2.41). The following line prints
\((1-10\delta)\tfrac12L=1\) and
\(\delta=\tfrac1{10}(1-2L^{-1})\). These coefficients are therefore not
being inferred from the damaged text layer.

For reproducibility, the inspected files have SHA-256 digests

```text
RG I   1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
RG II  EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC
```

The relevant one-based PDF pages are RG I 3 and 9, and RG II 14, 20, and
21. The external PDFs are evidence inputs and are not vendored in this
repository.

## An explicit KP sub-hierarchy inside the displayed source hierarchy

At the end of RG II the source chooses

\[
 (1-10\delta)\frac L2=1,
 \qquad
 \delta=\frac1{10}\left(1-\frac2L\right),
\tag{10}
\]

where \(L>11\) is the fixed allowed odd blocking factor. Put

\[
 \Delta=\delta\lambda=\frac{L-2}{20}\kappa,
 \qquad
 a=a_{\rm out}=(1-10\delta)\lambda=\kappa.
\tag{11}
\]

The displayed source order is important. Fix \(L\), then \(\delta\), choose
\(\kappa\), and next fix \(M,\kappa _1,\alpha_i,E_0\), and the other
non-\(\varepsilon _1\) constants subject to their restrictions. This fixes
the finite \(C_3\). Only then is \(\varepsilon _1\) shrunk; the coupling
ceiling \(\gamma\) is allowed to depend on all preceding constants.

Choose \(\kappa\) large enough to satisfy every displayed source lower bound
and the additional strict inequality

\[
 \kappa>\frac{1280\log8}{L-2}.
\tag{12}
\]

Then \(\Delta>64\log8\). Choose the pinned weight

\[
 \alpha=\frac\Delta{64}.
\tag{13}
\]

The ordinary Note-0023 exponent ledger, together with the numerical budget
that a future marked estimate would have to occupy, becomes

\[
  \begin{aligned}
  \beta&=a+2\Delta,\\
  a_\bullet^{\rm budget}&=(1-9\delta)\lambda=a+\Delta,\\
  32\alpha&=\frac\Delta2,\\
  \eta&=\beta-a-32\alpha=\frac{3\Delta}{2}.
 \end{aligned}
\tag{14}
\]

In particular, \(0<32\alpha\le\Delta\) and
\(a_{\rm out}+32\alpha\le a_\bullet^{\rm budget}\). The symbol
\(a_\bullet^{\rm budget}\) is only the reserved exponent value suggested by
the \(9\delta\) line; it is **not** a marked activity bound. Moreover,

\[
 C_{\rm an}^{\rm geom}(3\Delta/2)
 \le
 \frac{S_4}{1-8^{32}e^{-3\Delta/4}}
 <\frac{S_4}{1-8^{-16}},
 \qquad
 S_4=\frac{8^{32}-1}{63}.
\tag{15}
\]

After the remaining source constants have been fixed, Lemma 3 has the finite
printed symbolic constant

\[
 C_3=2(L+2)^4O(1)\,2E_0C_1
 \alpha_4^{-1}\alpha_6^{-1}M^q e^{C_2\kappa _1}>0.
\tag{16}
\]

Here \(q\) is the finite power used in the source estimates. The unspecified
\(O(1)\) means that this is not a numerical evaluation. Define

\[
 \varepsilon_{\rm KP}
 :=
 \frac{\Delta}
 {576C_3
  \exp\{\Delta/4+\sqrt7\,\kappa\}
  C_{\rm an}^{\rm geom}(3\Delta/2)}.
\tag{17}
\]

For every

\[
 0<\varepsilon _1\le\varepsilon_{\rm KP},
\tag{18}
\]

the ordinary activity bound (1) satisfies

\[
 9(C_3\varepsilon _1)
 \exp\{16\alpha+a_{\rm out}\sqrt7\}
 C_{\rm an}^{\rm geom}(2\Delta-32\alpha)
 \le\alpha.
\tag{19}
\]

This is exactly Note 0023 Eq. (27). The displayed source proof imposes upper
smallness restrictions such as small
\(e^{32\kappa _1}\varepsilon _1\) and
\(4B_0C_1e^{16\kappa _1}\varepsilon _1\le\alpha _2/2\), explicitly takes
\(\varepsilon _1\) sufficiently small after \(\kappa\) is sufficiently large
for the connected series, and uses further shrinking to recover the
inductive amplitude. Hence a positive \(\varepsilon _1\) can lie below both
(17) and every **displayed** source upper bound. The large value and parameter
dependence of \(C_3\) make the allowed cutoff possibly extremely small, but
do not make this displayed interval empty.

Equations (12)--(19) prove existence of a displayed-hierarchy refinement for
which the repository's explicit pinned-KP criterion holds uniformly. Calling
that refinement fully source-admissible is conditional on the monotonicity of
the restrictions imported but not listed in RG I/II. Balaban did not print
this criterion, choose (13), or supply a numerical value for \(C_3\).

## What this closes

- The final connected ordinary RG-II gas is no longer merely analogous to
  Note 0023's model: its support class, quotient seams, metric,
  incompatibility, literal union, and one aggregated ordinary species per
  support instantiate that model.
- Lemma 3 supplies the exact ordinary pointwise input form, uniformly on each
  relevant fixed-output source analytic domain; the norm notation used here
  is the repository supremum of that printed pointwise bound.
- Within the displayed source hierarchy, the choices "\(\kappa\)
  sufficiently large" and "\(\varepsilon _1\) sufficiently small" contain a
  nonempty sub-hierarchy satisfying the repository's stricter explicit D=4
  pinned-KP system. Compatibility with unenumerated imported restrictions is
  an explicit monotonicity hypothesis.
- Consequently, pointwise on each relevant fixed-output domain, the ordinary
  connected expansion has the Note-0023 pinned convergence control under
  that refined hierarchy, independently of the source's separate invocation
  of its standard cluster theorem.

## What remains open

- The source gas is unmarked. No derivative of (1), marked Lemma-3 estimate,
  post-polymerization marked norm, or marked gluing bound follows. Note 0025
  separately proves a fixed-term cutoff domination for an inserted localized
  mark, not a consequence of the unmarked activity bound (1).
- The intermediate \(Y_0,Z_0,\widetilde Z_0,Z'_0,X_0\) and random-walk
  supports retain their actual mixed-scale, disconnected, and interior-bond
  rules; this note proves no canonical least completion for them.
- No common external-observable source disk, branchwise shift
  synchronization, physical \(U/J\) pullback, marginal projection,
  large-field theorem, RG iteration, continuum construction, axioms,
  infrared decay, or Yang--Mills mass gap is proved.
- RG I/II do not enumerate every restriction imported from earlier papers;
  their preservation under further downward shrinking of \(\varepsilon _1\)
  has not been independently reconstructed from that full source chain.

## Falsification checks

1. Apply the identification before Eq. (2.10) and observe that Eq. (2.8) can
   have disconnected outputs.
2. Treat the interior-bond completion \(Z_0\) as a canonical literal-union
   hull; diagonal separated seeds give competing minimal completions.
3. Divide a \(k+1\)-rescaled tree length by \(LM\) and introduce a spurious
   extra factor \(L\).
4. Retain \(D,P,Z_0\) as separate final species even though Eqs. (2.9) and
   (2.13) sum them into \(H(Z)\).
5. Import the \(\exp(5\kappa)\) factor from Eq. (2.39) into Lemma 3 and obtain
   the wrong activity amplitude.
6. Say that Lemma 3 prints (19), rather than deriving (19) by an additional
   repository choice of \(\alpha,\kappa,\varepsilon _1\).
7. Differentiate (1) to obtain a marked bound; the elementary family
   \(H_t=H_0+tN\) disproves that inference.
8. Use (18) without also satisfying every earlier source restriction, or
   choose \(\varepsilon _1\) before the constants entering \(C_3\) are fixed.
9. Treat the unenumerated imported restrictions as proved downward-closed
   merely because all restrictions displayed in RG I/II have that property.
