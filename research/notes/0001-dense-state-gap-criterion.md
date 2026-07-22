# Note 0001: a dense-state semigroup criterion for a spectral gap

Claim ID: `YM-SPEC-001`

Kind: Lemma

Evidence: E2 (bounded auxiliary result; internally checked only)

Novelty: none claimed

## Statement

Let \(H\ge 0\) be self-adjoint on a Hilbert space \(\mathcal H\), and suppose

\[
\ker H=\operatorname{span}\{\Omega\}, \qquad \|\Omega\|=1.
\]

Fix \(\Delta>0\). The following are equivalent.

1. \(\sigma(H)\cap(0,\Delta)=\varnothing\).
2. There is a dense linear subspace \(D\subset\Omega^\perp\) such that, for every \(\psi\in D\), some finite \(C_\psi\) satisfies
   \[
   \langle\psi,e^{-tH}\psi\rangle\le C_\psi e^{-\Delta t}
   \quad\text{for every }t\ge0.
   \]

The constant may depend on \(\psi\), but \(\Delta\) may not.

## Proof

Assume (1). For \(\psi\perp\Omega\), its spectral measure

\[
\mu_\psi(B)=\langle\psi,E_H(B)\psi\rangle
\]

has no atom at zero and is supported in \([\Delta,\infty)\). The spectral theorem gives

\[
\langle\psi,e^{-tH}\psi\rangle
=\int_{[\Delta,\infty)}e^{-t\lambda}\,d\mu_\psi(\lambda)
\le e^{-\Delta t}\|\psi\|^2.
\]

Thus (2) holds with \(D=\Omega^\perp\) and \(C_\psi=\|\psi\|^2\).

Conversely, assume (2). Fix \(\psi\in D\). If
\(\mu_\psi((0,\Delta))>0\), then because

\[
(0,\Delta)=\bigcup_{n\text{ sufficiently large}}[1/n,\Delta-1/n],
\]

there are \(0<a<b<\Delta\) with \(\mu_\psi([a,b])>0\). Positivity of the spectral integral then yields

\[
\langle\psi,e^{-tH}\psi\rangle
\ge e^{-bt}\mu_\psi([a,b]).
\]

Combining this with the assumed upper bound gives

\[
\mu_\psi([a,b])e^{(\Delta-b)t}\le C_\psi
\]

for all \(t\ge0\), impossible as \(t\to\infty\). Hence
\(E_H((0,\Delta))\psi=0\) for every \(\psi\in D\). The spectral projection is bounded, so it vanishes on the closure \(\Omega^\perp\). It also vanishes on \(\Omega\), since the interval excludes zero. Therefore
\(E_H((0,\Delta))=0\), proving (1). \(\square\)

## Boundary and failure checks

- Continuous spectrum accumulating at zero is excluded by the same interval argument; no eigenvector assumption is used.
- Density is essential. Without it, the tested states could miss a low-energy invariant subspace.
- Vacuum orthogonality is essential because the vacuum contribution is constant in \(t\).
- A common decay exponent is essential. State-dependent exponents with infimum zero do not give a uniform gap.
- The argument permits spectrum at exactly \(\Delta\), as the definition of a gap does.

## Relation to Yang–Mills

After an Osterwalder–Schrader reconstruction, centered local gauge-invariant observables should generate a dense set of states orthogonal to the vacuum. A common exponential bound for their Euclidean time correlations would therefore imply a Hamiltonian gap by this lemma.

That sentence is a reduction, not the missing proof. The hard tasks are to construct the nontrivial four-dimensional continuum theory, justify reconstruction and density, and prove a positive decay rate that survives ultraviolet and infinite-volume limits in physical units.
