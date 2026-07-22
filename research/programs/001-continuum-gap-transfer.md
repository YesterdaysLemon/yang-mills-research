# Program 001: continuum gap transfer

Status: Active, exploratory

Full-problem evidence: E0

Primary claim dependency: `YM-SPEC-001`

## Question

What is the weakest regulator-uniform statement about gauge-invariant Euclidean correlations that passes to an Osterwalder–Schrader limit and forces a finite positive gap in the reconstructed Hamiltonian?

## Proposed bridge

For lattice spacing \(a\), volume scale \(L\), and a centered gauge-invariant local observable \(A\), seek a physical-unit estimate of the form

\[
0\le S^{c}_{a,L}(A^*,\tau_tA)
\le C_A e^{-\Delta t},
\]

where \(\Delta>0\) is independent of \(a\) and \(L\) along a continuum/infinite-volume trajectory. To use it, one must separately prove:

1. convergence of the relevant Schwinger functions as \(a\to0\) and \(L\to\infty\);
2. reflection positivity and the remaining reconstruction hypotheses;
3. density of the centered local states in the vacuum-orthogonal Hilbert space;
4. nontriviality and the required Yang–Mills short-distance behavior;
5. finiteness of the first positive spectral scale, not only a lower exclusion interval.

Under those hypotheses, the inequality passes to each fixed limiting correlation and Note 0001 supplies the spectral conclusion. None of items 1–5, and especially no uniform positive \(\Delta\), is established here.

## Why start here

This bridge makes a common category error visible: an exponential bound in lattice units at fixed bare coupling is not automatically a nonzero gap in physical units on an asymptotically free continuum trajectory. The dependence of every constant on \(a\), \(L\), bare coupling, observable renormalization, support, and gauge group must be tracked.

## First falsification checklist

- Does the proposed lattice rate shrink to zero after conversion to physical units?
- Is the estimate proved only in a strong-coupling region disconnected from the continuum trajectory?
- Does the prefactor diverge in a way that prevents passage to the chosen limiting observable?
- Is reflection positivity lost through gauge fixing or renormalization?
- Are only Wilson loops controlled, without a proved density statement for the reconstructed state space?
- Is clustering assumed to prove the gap and then cited as a consequence of the gap?
- Does the argument control only a finite torus or a subsequence whose limit is unidentified?

## Milestones

- [x] Prove and expose the abstract semigroup criterion.
- [ ] State a precise regulator-to-limit theorem with topologies and quantifier order.
- [ ] Audit its novelty against constructive-QFT and lattice literature.
- [ ] Map every hypothesis to known theorems or an explicit open lemma.
- [ ] Attempt the first genuinely Yang–Mills-specific uniform estimate.

Passing the first item is organizational progress, not evidence that the central problem is close.
