# Program 003: the first source-jet fluctuation remainder

Claim ID: `YM-RG-004`

Status: Open theorem specification

Evidence: E0

Initial group: \(SU(2)\)

Novelty: not claimed

## Frozen setup

Use the Euclidean-symmetric RG I Eq. (0.12) average and the raw group-delta
transform selected in the [imported-map
audit](../../literature/audits/2026-07-22-balaban-imported-map.md). Retain the
odd-\(L>11\) geometry and use the fixed-\(\varepsilon_1\) small-field cutoff,
not the coupling-dependent alternative, for this first theorem.

On the admitted coarse-field domain, first construct a pointwise positive
finite disintegration \(K_L(V,dU)\) of the raw group-delta constraint. A
regular conditional probability defined only for almost every \(V\) is not
enough for the target analytic estimates. [Note
0006](../notes/0006-local-balaban-fiber-chart.md) supplies a positive
pointwise contribution on a sufficiently small background-centered fiber ball,
but not the whole restricted transform or any uniform lower bound.

For a specified local Borel chart domain
\(\mathcal C_V\subset F^{-1}(V)\), let \(B'_V\) denote the exact gauge-fixed
fluctuation coordinate only on \(\mathcal C_V\). Its zero-extended local
restriction is

\[
\chi_k(B')=
\prod_{b\in T^{(k)}\setminus\{b_0(c):c\in T^{(k+1)}\}}
\mathbf1\{|B'(b)|<\varepsilon_1\},
\]

and define, without evaluating \(B'_V\) off its domain,

\[
\widetilde\chi_{k,V}(U)=
\begin{cases}
\chi_k(B'_V(U)),&U\in\mathcal C_V,\\
0,&U\notin\mathcal C_V,
\end{cases}
\qquad
K_L^{\rm sf,loc}(V,dU)
=\widetilde\chi_{k,V}(U)K_L(V,dU).
\]

where the product and chart are exactly those of Eq. (2.9), not an enlarged
global coordinate system. The construction must prove that
\(\mathcal C_V\) and the pullback are Borel, source and coupling independent,
compatible with the required coarse gauge covariance, and of finite nonzero
mass on every admitted fiber.

The target must then either prove that the entire chosen fixed-cutoff support
lies in one such domain, assemble compatible local domains without double
counting, or explicitly shrink the theorem to a named local restriction. Only
after that step yields a pointwise kernel \(K_L^{\rm sf}\) may
\(\nu^{\rm sf}_{x,V}\) denote its normalized conditional measure. Conditional
on those facts, Note 0003 applies to the restricted kernel; it does not identify
it with the unrestricted full transform.

For a real plaquette profile \(f\) supported in one coarse block and normalized
by Program 002's \(\|f\|_{C^6_{\rm disc}}\le1\), let

\[
\mathcal O_f(U)=4\sum_p f_p s(U_p).
\]

Note 0003 gives the exact restricted-kernel first jet as a conditional
expectation once the displayed construction is complete, while Note 0004
gives the fixed-background term on the unique minimizing orbit. Define their
difference

\[
\mathcal J_f(V)=
\mathbb E_{\nu^{\rm sf}_{x,V}}[\mathcal O_f(U)]
-\mathcal O_f(U_1(V)).
\]

This is the first quantity not settled by algebra or the imported source-free
background theorem.

## Target theorem

On the exact admitted regular coarse-field domain, derive a polymer
representation

\[
\mathcal J_f(V)=M_f(V)+\sum_X K_{X,f}(V),
\qquad
M_f=\Pi_{\rm rel}\mathcal J_f,
\]

with all of the following properties.

1. **Complete projection.** Classify every first-jet relevant/marginal
   operator and every allowed position/orientation mixing of \(f\); do not
   assume a scalar energy renormalization factor.
2. **Gauge invariance.** The projected term and each localized activity are
   invariant under coarse gauge transformations.
3. **Quasilocality.** The profile-mixing kernels, projected coefficients, and
   polymer activities have summable exponential decay away from
   \(\operatorname{supp}f\), in explicitly copied Bałaban norms.
4. **Uniformity.** Constants are independent of torus size, cutoff scale, and
   source location for fixed admitted \(g,L\) and normalized \(f\).
5. **Analytic domain.** The coarse-field analyticity domain is exactly the
   gauge-fixed regular patch supplied by the imported theorems; no global
   logarithm or gauge slice is used.
6. **Source-free compatibility.** The proof derives the representation by
   differentiating a source-inserted construction or by a justified insertion
   into the cluster expansion. It may not infer source bounds merely by
   differentiating a source-free final estimate.

This target covers one source derivative in the fixed small-field branch only.
It deliberately excludes the second source derivative, coupling-dependent
cutoffs, the large-field complement, RG iteration, continuum limits, and
infrared conclusions.

## Available inputs

- exact finite-regulator conditional-cumulant identity (Note 0003);
- unique minimizing orbit plus analytic gauge-fixed branch (Note 0004), with
  the variational paper's Eq. (190) component decay still to be transcribed;
- pointwise positive fiber kernels for proper smooth submersions (Note 0005),
  conditional on proving the selected map and cutoff satisfy its hypotheses;
- RG I's local analytic constraint straightening and a positive precompact
  background-centered fiber ball (Note 0006), without full-cutoff uniformity;
- background-propagator decay and change-of-domain estimates;
- RG I/II source-free local analytic polymer expansions.

None of those inputs supplies the displayed source-inserted polymer theorem.

## First derivation route

1. Insert \(z\mathcal O_f\) before the RG I fluctuation-coordinate changes.
2. Construct the pointwise positive coarse-fiber disintegration and state its
   reference measure, support, and regularity in \(V\).
3. Keep every Jacobian, characteristic function, and normalization visibly
   separate and verify which are \(z\)- or \(x\)-dependent.
4. Differentiate at \(z=0\) before taking logarithms of polymer products.
5. Isolate the background contribution \(\mathcal O_f(U_1(V))\).
6. Apply the RG II connected-cluster organization to the remaining marked
   activity and prove its distance-to-source bounds.
7. Perform the full symmetry/Ward-identity projection on the marked first
   jet.

## Falsification tests

- The group-delta fiber cannot be given the positive disintegration assumed by
  Note 0003.
- A fixed cutoff still creates a boundary/source derivative term omitted by
  the derivation.
- The marked activity has an unsummable tail or a constant grows with volume.
- A profile-orientation mixing term survives outside the proposed projection.
- Gauge fixing creates a noncovariant marked activity.
- A proof uses Proposition 9 outside its local analytic patch.
- A source-free bound is differentiated without a common analytic source
  domain.

Failure of this bounded theorem would force Program 002 to change map, source
class, projection, or route. Success would still be only an auxiliary E2
small-field result and would not establish a continuum theory or mass gap.
