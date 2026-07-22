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

The unrestricted raw group-delta transform remains a separate object: ordinary
disintegration only gives almost-everywhere conditional probabilities, and the
audited sources do not exclude remote logarithmic branches. This theorem is
therefore explicitly restricted to RG I's selected near-identity fixed-cutoff
branch rather than silently identifying that branch with the unrestricted
fiber.

[Note 0008](../notes/0008-full-fixed-cutoff-branch.md) uses RG II
Eqs. (1.19)–(1.20) to prove that the **complete** Eq. (2.9)
independent-bond cube stays inside one regular analytic chart. For each finite
regulator and admitted real coarse field \(V\), it defines the intrinsic
pointwise finite nonzero positive branch measure
\(K_k^{\rm chart}(V,dU)\). Assume the real source-free branch weight is
integrable and strictly positive on a set of positive branch measure, so that

\[
0<Z_{k,x,V}^{\rm chart}(0)
=\int e^{-S_{k,x,V}(U)}K_k^{\rm chart}(V,dU)<\infty.
\]

Then set

\[
\nu_{k,x,V}^{\rm chart}(dU)
=\frac{e^{-S_{k,x,V}(U)}K_k^{\rm chart}(V,dU)}
       {Z_{k,x,V}^{\rm chart}(0)}.
\tag{1}
\]

The chart branch and cutoff are frozen at source zero, so they are independent
of \(z\) and \(f\). They may still depend on the source-free coupling/background
construction; the constant-profile coupling identity must continue to be
stated for the coupling-independent raw transform, not assumed for (1).

[Note 0007](../notes/0007-projective-source-kernels.md) shows that no
volume-independent lower bound on the raw branch mass is needed. The displayed
positive finite weighted partition function gives the normalized law, and
bounded plaquette range gives an explicit common zero-free source disk. The
remaining theorem must prove joint coarse-field analyticity or a precise real
substitute, coarse-gauge
covariance for gauge-invariant tests, and marked-polymer locality of this
normalized branch law.

For a real plaquette profile \(f\) supported in one coarse block and normalized
by Program 002's \(\|f\|_{C^6_{\rm disc}}\le1\), let

\[
\mathcal O_f(U)=4\sum_p f_p s(U_p).
\]

Notes 0007–0008 give the exact selected-branch first jet as a pointwise
conditional expectation, while Note 0004 gives the fixed-background term on
the unique minimizing orbit. Define their difference

\[
\mathcal J_f(V)=
\mathbb E_{\nu^{\rm chart}_{k,x,V}}[\mathcal O_f(U)]
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
   source location for fixed admitted \(g,L\) and normalized \(f\). These are
   normalized cumulant/polymer constants, not a lower bound on the raw product
   cutoff mass.
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
- projective invariance, centered-score differentiation, and a uniform
  bounded-observable source disk once a named pointwise kernel gives a positive
  finite source-free weighted partition function (Note 0007);
- RG II's complete-cube containment and the resulting pointwise positive
  measure on the entire selected fixed-cutoff chart branch (Note 0008),
  without an unrestricted-fiber comparison or covariance theorem;
- background-propagator decay and change-of-domain estimates;
- RG I/II source-free local analytic polymer expansions.

None of those inputs supplies the displayed source-inserted polymer theorem.

## First derivation route

1. Insert \(z\mathcal O_f\) before the RG I fluctuation-coordinate changes.
2. Use the pointwise positive selected-branch measure from Note 0008; state its
   exact support and prove the missing joint regularity/covariance in \(V\).
3. Keep every Jacobian, characteristic function, and normalization visibly
   separate and verify which are \(z\)- or \(x\)-dependent.
4. Differentiate at \(z=0\) before taking logarithms of polymer products.
5. Isolate the background contribution \(\mathcal O_f(U_1(V))\).
6. Apply the RG II connected-cluster organization to the remaining marked
   activity and prove its distance-to-source bounds.
7. Perform the full symmetry/Ward-identity projection on the marked first
   jet.

## Falsification tests

- The selected branch fails the joint Borel/covariance properties needed for
  gauge-invariant marked activities.
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
