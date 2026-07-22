# Program 002: one-block local-observable RG theorem

Claim ID: `YM-RG-001`

Status: Open theorem specification

Evidence: E0

Initial group: \(SU(2)\)

Novelty: not claimed pending theorem-level prior-art comparison

## Setup

On an oriented four-dimensional periodic lattice, assign \(U_e\in SU(2)\) to each positive link and \(U_{\bar e}=U_e^{-1}\). For a plaquette \(p\), let

\[
U_p=\prod_{e\in\partial p}U_e,
\qquad
s(U_p)=1-\tfrac12\operatorname{ReTr}U_p.
\]

For a real source profile \(f\) supported in one coarse block, introduce

\[
S_{g,J,f}(U)=4\sum_p\bigl(g^{-2}+Jf_p\bigr)s(U_p).
\]

Fix a precise gauge-covariant Bałaban block transformation \(\mathcal T_L\) with scale factor \(L\). The first research target is an exact source-dependent decomposition after **one** block step.

## Target statement

Prove, with every convention and norm fixed, a decomposition of the form

\[
\mathcal T_L(e^{-S_{g,J,f}})(V)
=\exp\!\left[
-S_{g_L}(V)
-JZ_E(g,L)\mathcal E_{Lf}(V)
+\sum_X K_X(V;J,f)
\right]
\]

such that:

1. each \(K_X\) is coarse-gauge invariant, localized to a connected polymer \(X\), and analytic for \(|J|\le J_0\);
2. after projecting out the identity and action-density directions, a source-derivative polymer norm through order two contracts with constants independent of lattice spacing, torus size, and source location;
3. the large-field complement is included and receives an explicit nonperturbative bound rather than being discarded;
4. for constant \(f\), differentiating in the source agrees with differentiating the renormalized inverse coupling;
5. the one-loop change of inverse coupling matches the universal asymptotically free coefficient in the chosen normalization.

A representative desired estimate is

\[
\|K\|_{\kappa,h}^{(2)}
\le q(g,L)\|f\|_{C^6_{\rm disc}},
\qquad
q(g,L)\le C(g^2+L^{-2})+Ce^{-c/g^2}<1,
\]

but this formula is a design target. The exact norm, projections, admissible fields, constants, and range of \(g,L\) must be derived from the selected block transformation, not reverse-engineered to make the inequality true.

## Why this is useful and bounded

The plaquette energy is gauge invariant and arises by differentiating the action with respect to inverse coupling. Source derivatives therefore test whether the RG construction controls actual local observables rather than only the partition function. One step is small enough for a line-by-line audit while directly addressing a missing input in the official problem.

Even a complete proof would remain an auxiliary E2 result. It would prove no continuum limit, no iteration through strong coupling, no OS reconstruction, and no mass gap.

## Work packets

- [ ] Pin one Bałaban block map and translate its field domains and norms without alteration.
- [ ] Build a theorem-by-theorem prior-art matrix for source-free and source-inserted steps.
- [ ] Derive the constant-source coupling identity before estimating remainders.
- [ ] Differentiate the small-field stationary/background construction through order two in \(J\).
- [ ] Prove gauge-orbit derivatives vanish for every polymer activity.
- [ ] Extend the estimates across the large-field decomposition with volume-independent constants.
- [ ] Audit marginal projections and the one-loop coefficient.

## Falsification tests

Reject the target as stated if any of the following occurs:

- a constant grows with the total number of blocks;
- a global logarithm \(U_e=\exp A_e\) silently crosses the group cut locus;
- the large-field complement is omitted;
- any polymer activity changes under a coarse gauge transformation;
- a source spreads without summable decay outside its block;
- an unprojected marginal term remains and prevents iteration;
- the constant-source derivative identity fails;
- the universal one-loop coefficient fails after normalization is reconciled;
- reflection positivity is claimed for the effective action without a separate proof;
- numerical agreement replaces the analytic estimate.

## Sources to audit first

- [Bałaban, RG approach I](https://doi.org/10.1007/BF01215223)
- [Bałaban, RG approach II](https://doi.org/10.1007/BF01239022)
- [Bałaban, convergent renormalization expansions](https://doi.org/10.1007/BF01217741)
- [Bałaban, large-field renormalization I](https://doi.org/10.1007/BF01257412)

The immediate next action is primary-source extraction: reproduce the exact block-map definitions and determine which parts of this target are already implicit or explicit. Until that comparison is complete, novelty remains false in `CLAIMS.json`.
