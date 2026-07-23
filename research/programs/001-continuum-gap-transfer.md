# Program 001: continuum gap transfer

Status: Active, exploratory

Full-problem evidence: E0

Primary claim dependencies: `YM-SPEC-001`, `YM-SPEC-002`

## Question

What is the weakest regulator-uniform statement about gauge-invariant
Euclidean correlations that passes to an Osterwalder–Schrader limit and forces
a finite positive gap in the reconstructed Hamiltonian?

## Proposed bridge

Let \(r\) follow one identified cutoff/infinite-volume trajectory, with lattice
spacing \(a_r\downarrow0\) and diverging physical temporal extent. For a
limiting positive-time observable \(A\), specify a renormalized lattice
representative \(R_rA\), centered with the regulator expectation. At an
admissible no-wrap lattice time \(k\), set

\[
Q_{r,A}(k)=S_r\!\left(\Theta(R_rA)^\circ\,
\tau_k(R_rA)^\circ\right).
\]

The exact sufficient estimate isolated in Note 0002 has quantifier order

\[
\exists\Delta>0\ \forall A\ \forall\varepsilon\in(0,\Delta)\
\exists C_{A,\varepsilon},t_{A,\varepsilon},r_{A,\varepsilon}\
\forall r\ge r_{A,\varepsilon}\ \forall k,
\]

followed by

\[
0\le Q_{r,A}(k)
\le C_{A,\varepsilon}
e^{-(\Delta-\varepsilon)a_rk}
\quad\text{when }a_rk\ge t_{A,\varepsilon}
\]

and \(k\) is no-wrap admissible. The prefactor may depend on the observable
and \(\varepsilon\), but not on regulator, lattice spacing, volume, or time.
One must separately prove:

1. convergence \(Q_{r,A}(k_r)\to Q_A(t)\) for every admissible sequence with
   \(a_rk_r\to t\), not merely distributional convergence under unrelated
   smearings;
2. a corrected OS reconstruction package, not reflection positivity alone;
3. totality after the OS null-space quotient of the exact limiting observable
   family for which the estimate holds;
4. nontriviality, Euclidean symmetry restoration, any physical-time
   anisotropy normalization, and the required Yang–Mills short-distance
   behavior.

Under those hypotheses, the inequality passes first at each fixed physical
time. Note 0002 then takes the large-time spectral limit and excludes
\((0,\Delta)\). Nontriviality makes the vacuum-orthogonal sector nonzero and
hence the mass finite. None of items 1–4, and especially no Yang–Mills estimate
with a regulator-uniform exponent and prefactor, is established here.

## Why start here

This bridge makes a common category error visible: an exponential bound in
lattice units at fixed bare coupling is not automatically a nonzero gap in
physical units on an asymptotically free continuum trajectory. The dependence
of every constant on \(a_r\), volume, bare coupling, observable
renormalization, support, and gauge group must be tracked.

## First falsification checklist

- Does the proposed lattice rate shrink to zero after conversion to physical
  units?
- Is the estimate proved only in a strong-coupling region disconnected from
  the continuum trajectory?
- Does the prefactor depend on the regulator or diverge in a way that prevents
  passage to the chosen limiting observable?
- Is the observable centered separately at every regulator, including
  identity mixing?
- Is pointwise convergence of the translated reflected form actually proved?
- Are finite-torus wraparound and physical-time anisotropy excluded?
- Is reflection positivity lost through gauge fixing or renormalization?
- Are only Wilson loops controlled, without a proved totality statement for
  their reconstructed classes?
- Is clustering assumed to prove the gap and then cited as a consequence of
  the gap?
- Does the argument control only a finite torus or a subsequence whose limit
  is unidentified?

## Milestones

- [x] Prove and expose the abstract semigroup criterion.
- [x] State a precise sequential correlation-level transfer theorem and
  quantifier order.
- [ ] Embed that theorem in a full convergence topology and corrected OS
  construction.
- [ ] Audit its novelty against constructive-QFT and lattice literature.
- [ ] Map every hypothesis to known theorems or an explicit open lemma.
- [ ] Attempt the first genuinely Yang–Mills-specific uniform estimate.

Passing the first two items is organizational progress, not evidence that the
central problem is close.
