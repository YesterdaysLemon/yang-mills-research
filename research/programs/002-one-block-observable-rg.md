# Program 002: one-block local-observable RG theorem

Claim ID: `YM-RG-001`

Status: Open theorem specification

Evidence: E0

Initial group: \(SU(2)\)

Novelty: not claimed pending theorem-level prior-art comparison

## Setup

On an oriented four-dimensional periodic lattice, assign \(U_e\in SU(2)\) to
each positive link and \(U_{\bar e}=U_e^{-1}\). For a plaquette \(p\), let

\[
U_p=\prod_{e\in\partial p}U_e,
\qquad
s(U_p)=1-\tfrac12\operatorname{ReTr}U_p.
\]

Write \(x=g^{-2}\). For a real profile \(f\), introduce

\[
S_{x,z,f}(U)=4\sum_p\bigl(x+zf_p\bigr)s(U_p).
\]

Here \(z\) is a new complex source parameter. It is deliberately not called
\(J\), because \(J\) already denotes Bałaban's auxiliary derivative field in
the small-field induction. Two profile classes have different jobs:

- the normalized class supported in one coarse block, with
  \(\|f\|_{C^6_{\rm disc}}\le1\), tests locality and polymer decay;
- the finite-volume profile \(f\equiv1\) is used only for a first-derivative
  consistency test at \(z=0\), not for the local-profile norm.

Freeze the Euclidean-symmetric average in RG I Eq. (0.12), with the group
average and contour variables of Eqs. (0.5)–(0.11), and the raw group-delta
transform in Eq. (10) of the earlier averaging paper. The exact
selection and imported hypotheses are recorded in the [imported-map
audit](../../literature/audits/2026-07-22-balaban-imported-map.md). The block
factor retains RG I's odd-\(L>11\) assumption.

Write \(\mathcal T_L^{\rm raw}\) for this raw unnormalized linear transform,
whose kernel is fixed independently of \(x\) and \(z\). Any
coupling-dependent normalization, small-field threshold, or large-field
operation is a separate displayed factor. Define

\[
\mathcal R_{x,z,f}(V)
=\frac{\mathcal T_L^{\rm raw}(e^{-S_{x,z,f}})(V)}
{\mathcal T_L^{\rm raw}(e^{-S_{x,0,f}})(V)}.
\]

The ratio prevents source-free irrelevant terms from being mislabeled as
source responses. For fixed admitted \(g,L\), the normalized local profile
class, and every admissible coarse field \(V\), the target must prove a common
zero-free disk \(|z|\le z_0(g,L)\). Its radius must be independent of cutoff,
torus size, source location, \(f\) in the normalized class, and \(V\) in the
stated field domain. Use the analytic branch fixed by
\(\log\mathcal R_{x,0,f}=0\).

[Note 0003](../notes/0003-raw-block-source-jets.md) proves the pointwise
finite-regulator cumulant identities for any positive coupling-independent raw
kernel. It supplies no uniform radius, locality, mixing, or large-field bound;
those remain the content of this program.

## Target statement

For admitted regular \(V\), the variational theorem gives a unique minimizing
**gauge orbit** \([U_1(V)]\), not initially a global single-valued map. Define

\[
\mathcal E^{\mathrm{bg}}_f(V)
=4\sum_p f_p\,s\!\left(U_1(V)_p\right).
\]

This is representative independent because the plaquette trace is gauge
invariant. Any analyticity or quasilocality assertion in \(V\) must use the
specific local gauge-fixed branch and domain in Proposition 9 of the
variational paper. [Note 0004](../notes/0004-fixed-background-source-jet.md)
records exactly what that source-free background theorem supplies.

Derive a localized projection \(\Pi_{\rm rel}\) onto **all**
source-dependent relevant and marginal directions permitted by the residual
lattice symmetries and the profile class. Then prove a decomposition

\[
\log\mathcal R_{x,z,f}(V)
=M_{\rm rel}(V;z,f)
+\sum_X K_X^{\mathrm{irr}}(V;z,f),
\qquad
M_{\rm rel}=\Pi_{\rm rel}\log\mathcal R.
\]

The first source jet must be displayed rather than assumed to close on one
scalar coefficient. In general it may have the form

\[
\left.\partial_zM_{\rm rel}(V;z,f)\right|_{z=0}
=c_{\mathbf1}(x,L;f)
-\mathcal E^{\mathrm{bg}}_{\mathsf Z_E(x,L)f}(V)
+\sum_{\alpha\in\mathcal A}
c_\alpha(x,L;f)\,\mathcal O^{\mathrm{bg}}_\alpha(V).
\]

Here \(\mathsf Z_E\) is allowed to mix plaquette positions and orientations,
and \(\mathcal A\) contains any additional symmetry-allowed relevant or
marginal operators. The proof must classify this list. A scalar
\(\mathsf Z_E=Z_E\mathbf1\), or an empty \(\mathcal A\), may be concluded only
after a symmetry/mixing argument or after restricting to a proved invariant
profile. Higher source jets must likewise display every projected counterterm.
Replacing the fine-background insertion by the plain coarse Wilson action of
\(V\) requires a separate theorem.

The normalization must account for the fact that this \(SU(2)\) convention
has coefficient \(4x\), whereas Bałaban's normalized-trace action gives the
working crosswalk \(x_B=4x\). That translation must be rechecked for the
finally selected map.

The required properties are:

1. the localization scheme defines \(\Pi_{\rm rel}\) polymerwise, each
   \(K_X^{\mathrm{irr}}\) vanishes at \(z=0\) and obeys
   \(\Pi_{\rm rel}K_X^{\mathrm{irr}}=0\), and every activity is
   coarse-gauge invariant, localized to a connected polymer \(X\), and
   analytic on the proved common source disk;
2. for the normalized local profile class, **both** the projected sector and
   the irrelevant sector through two source derivatives obey volume-, cutoff-,
   and source-location-independent estimates. In particular, the kernels of
   \(\mathsf Z_E\), every coefficient \(c_\alpha\), and all higher projected
   source jets must have summable or proved quasilocal decay away from
   \(\operatorname{supp}f\). The irrelevant activities obey estimates such as
   \[
   \|\partial_zK^{\mathrm{irr}}(0;f)\|_{\kappa,h}
   \le C_1(g,L)\|f\|_{C^6_{\rm disc}},
   \qquad
   \|\partial_z^2K^{\mathrm{irr}}(0;f)\|_{\kappa,h}
   \le C_2(g,L)\|f\|_{C^6_{\rm disc}}^2;
   \]
   the exact norm, constants, coupling range, and any useful smallness in
   \(g,L\) must be derived. These are source-to-remainder bounds, not by
   themselves a contraction of an RG map on incoming activities;
3. the proof identifies its exact small-field domain, and the full version
   includes the large-field complement with an explicit nonperturbative bound
   instead of importing it from a small-field theorem;
4. for the separate finite-volume test \(f\equiv1\), raw linearity gives the
   exact first-jet identity
   \[
   \left.\partial_z\log
   \mathcal T_L^{\rm raw}(e^{-S_{x,z,1}})(V)\right|_{z=0}
   =\partial_x\log
   \mathcal T_L^{\rm raw}(e^{-S_{x,0,1}})(V).
   \]
   No higher-derivative or local-polymer assertion for \(f\equiv1\) is made.
   A later normalized density \(\widehat{\mathcal T}_x
   =N_x\mathcal T_L^{\rm raw}\) has separate normalization derivatives that
   must be included in its own coupling bookkeeping; they do not alter the
   raw identity. Note 0003 proves this algebraic statement under the displayed
   raw-kernel hypotheses; matching those hypotheses to the selected Bałaban
   operation remains open;
5. the one-loop change of inverse coupling matches the universal
   asymptotically free coefficient in the chosen normalization.

For \(SU(2)\), \(b_0=11/(24\pi^2)\). For fixed \(L\) as \(g\to0\), or in a
separately proved regime with \(g^2\log L\ll1\), the consistency target is

\[
x_L=x-2b_0\log L+O(g^2\log L).
\]

RG I defines a recursive beta term but explicitly defers the perturbative
evaluation of its stated coupling-flow theorem. It cannot be cited as already
proving this coefficient.

## Why this is useful and bounded

The plaquette energy is gauge invariant and arises by differentiating the
action with respect to inverse coupling. Source derivatives test whether the
RG construction controls local observables rather than only the partition
function. One step is small enough for a line-by-line audit while addressing a
missing interface in this proposed constructive route.

Even a complete proof would remain an auxiliary E2 result. It would prove no
continuum limit, no iteration through strong coupling, no OS reconstruction,
and no mass gap.

## Work packets

- [x] Freeze RG I Eq. (0.12) and the raw group-delta transform;
  record the imported map, chart, propagator, and minimizer anchors.
- [ ] Transcribe every selected field domain, norm, and constant dependency
  into the one-step proof without alteration.
- [ ] Complete the theorem-by-theorem prior-art matrix: the imported map papers
  are now audited, but Large Field II remains abstract-only.
- [x] Derive the finite-regulator raw source-cumulant and constant-profile
  coupling identities; see Note 0003.
- [x] Derive the fixed source-free background jet and its analytic scope; keep
  the exact Eq. (190) decay specialization open; see Note 0004.
- [ ] Classify every relevant/marginal source counterterm and the profile
  mixing map.
- [ ] Differentiate the small-field stationary/background construction
  through order two in \(z\).
- [ ] Prove gauge-orbit derivatives vanish for every polymer activity.
- [ ] Extend the estimates across the separately defined large-field
  operation with volume-independent constants; do not infer this from RG I,
  which is explicitly small-field.
- [ ] Audit the normalized coupling bookkeeping and one-loop coefficient.

## Falsification tests

Reject the target as stated if any of the following occurs:

- a constant grows with the total number of blocks;
- a global logarithm \(U_e=\exp A_e\) silently crosses the group cut locus;
- the large-field complement is omitted;
- a source-free effective action is replaced by a plain coarse Wilson action
  instead of the fine background action without proof;
- any polymer activity changes under a coarse gauge transformation;
- a source spreads without summable decay outside its block;
- a symmetry-allowed mixing or marginal term is omitted;
- the local-profile and constant-profile quantifiers are conflated;
- the logarithm is used without a uniform zero-free source disk and a fixed
  branch;
- the raw and normalized coupling derivatives are conflated;
- the universal one-loop coefficient fails after normalization is reconciled;
- reflection positivity is claimed for the effective action without a
  separate proof;
- numerical agreement replaces the analytic estimate.

## Sources audited first

- [Bałaban, RG approach I](https://doi.org/10.1007/BF01215223)
- [Bałaban, RG approach II](https://doi.org/10.1007/BF01239022)
- [Bałaban, convergent renormalization expansions](https://doi.org/10.1007/BF01217741)
- [Bałaban, large-field renormalization I](https://doi.org/10.1007/BF01257412)
- [Bałaban, large-field renormalization II](https://doi.org/10.1007/BF01238433)
- [Bałaban, averaging operations](https://doi.org/10.1007/BF01211042)
- [Bałaban, regular configurations and gauge fixing](https://doi.org/10.1007/BF01466594)
- [Bałaban, background propagators](https://doi.org/10.1007/BF01240355)
- [Bałaban, variational problem/background fields](https://doi.org/10.1007/BF01229381)

The [first source map](../../literature/audits/2026-07-22-balaban-source-map.md)
found the source-free ultraviolet scaffold but no scalar-source theorem. The
[imported-map audit](../../literature/audits/2026-07-22-balaban-imported-map.md)
now fixes the exact raw interface. The next hard target is the fluctuation
remainder between the exact conditional first jet and its minimizing-background
term, stated separately in Program 003. Until the full comparison is complete,
novelty remains false in `CLAIMS.json`.
