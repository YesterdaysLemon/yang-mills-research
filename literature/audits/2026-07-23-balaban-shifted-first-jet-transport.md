# Bałaban shifted first-jet transport audit

Date: 2026-07-23

Purpose: distinguish the exact source-free identities used by YM-RG-027 from
the repository's shifted, marked, and projective corollaries.

## Immutable artifacts

- RG I Project Euclid PDF:
  `1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A`
- RG II Project Euclid PDF:
  `EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC`

Stable mirrors:

- [RG I](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf)
- [RG II](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf)

## Exact source chain

1. RG I's symmetry convention preceding Eq. (2.17), Eq. (2.17), and the
   discussion after Eqs. (2.17)--(2.18) give covariance of the undecoupled
   construction and the induced orthogonal transformation of fluctuation
   coordinates for symmetries preserving the next coarse lattice.
2. RG II Lemma 2 Eq. (1.41) is an exact decomposition of the source-free
   fluctuation action into localized \(V_k(Y)\). Eqs. (1.42)--(1.43) state
   its source-free structure and estimates.
3. RG II Eq. (2.1) is the finite Mayer-subfamily identity. Eqs. (2.2)--(2.4)
   use exact support grouping and cutoff inclusion--exclusion.
4. Eqs. (2.5)--(2.7) are exact Gaussian conditioning and exterior
   standardization identities. Their restricted covariances and determinants
   are coordinates for the original global Gaussian integral, not new
   physical laws.
5. RG II explicitly says before Eq. (2.8) that the second localization uses
   \(\pi_{k+1}\) cubes of side \(LM\) in the \(k\)-scale coordinates.
   Eqs. (2.8)--(2.10) give the exact weakening reconstruction and connected
   component factorization.
6. Eqs. (2.11)--(2.13) give the final hard-core gas, its connected
   logarithm, and grouping by literal support union.

The source formulas use one chosen cubulation and contain no scalar plaquette
source, dual number, distinguished mark, shifted family, or branch-average
theorem.

## Repository transport corollary

For a translation \(s\) preserving the next coarse lattice, apply the
standard Lemma-2 identity to the transported fields and fluctuation
coordinates, then relabel back. Covariance of the undecoupled exponent gives

\[
\Psi_k(x,B)
=c_{k,s}(x)+\sum_YV_k^s(Y;x,B).
\]

The fixed global cutoff and Gaussian law satisfy

\[
\chi_k(T_s^{-1}B)=\chi_k(B),
\qquad
(T_s)_*\mu_{\Gamma_k(\tau_s^{-1}x)}
=\mu_{\Gamma_k(x)}.
\]

Thus every shifted Section-2 calculation is an exact recombination of the
same global integral. This conclusion would fail if a branch used a genuinely
partition-modified cutoff or Gaussian law.

For a fixed plaquette, the repository comparison is restricted to the
explicitly assumed nonempty common intersection of all admitted transported
external branch domains. The source does not supply a global
compatible-atlas theorem for that intersection.

Because Section 2 uses both \(M\)- and \(LM\)-cubulations, an input shift
modulo \(M\) does not specify the output cubulation. YM-RG-027 therefore uses
all

\[
s\in(L\mathbb Z/LM\mathbb Z)^4
\]

and transports the nested pair together. Under \(LM\mid N\), every admitted
input residue has \(L^4\) such two-scale lifts.

Insert

\[
1-\epsilon\Delta_p,
\qquad
\epsilon^2=0,
\]

and use the separately proved shifted rooted identity for \(\Delta_p\).
The finite source-independent identities above then give on every branch

\[
\mathscr I_p^{\mathbb D}
=S_s(\mathcal Z_s-\epsilon\mathcal N_{p,s}),
\qquad
S_s\ne0.
\]

Equality of the ratio
\(\mathcal N_{p,s}/\mathcal Z_s\), rather than equality of branch
denominators or activities, is the projective synchronization statement.

## Exact boundary

- Bałaban proves the unmarked source-free identities on a chosen
  cubulation.
- The stabilizer averaging, nested shift lift, marked dual-number insertion,
  projective comparison, and connected branch normalization are repository
  corollaries.
- The existing zero-free scalar disk comes from the bounded-observable
  argument in Notes 0007 and 0010, not from RG II's polymer expansion.
- No source-dependent activities \(H_{s,t}\), uniform KP theorem at
  \(t\ne0\), physical \(U/J\) pullback, large-field estimate, RG iteration,
  continuum construction, infrared decay, or mass gap is imported or proved
  by this audit.
- The audit is not independent human review.
