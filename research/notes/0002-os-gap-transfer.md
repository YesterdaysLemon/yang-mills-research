# Note 0002: an Osterwalder–Schrader gap-transfer criterion

Claim ID: `YM-SPEC-002`

Kind: Lemma and regulator-to-limit corollary

Evidence: E2 (conditional auxiliary result; internally checked only)

Novelty: none claimed

## Purpose

This note fixes the quantifiers needed to turn reflected Euclidean decay into a
Hamiltonian gap. It proves a conditional transfer statement. It does **not**
construct a Yang–Mills measure, prove convergence of a regulator, establish
reflection positivity, or supply the decay estimate.

## Continuum proposition

Assume an Osterwalder–Schrader reconstruction has produced a Hilbert space
\(\mathcal H\), a unit vacuum \(\Omega\), and a nonnegative self-adjoint
Hamiltonian \(H\) with

\[
H\Omega=0,
\qquad
\ker H=\operatorname{span}\{\Omega\}.
\]

For a positive-time algebra element \(F\), set

\[
F^\circ=F-S(F)\mathbf 1,
\qquad
\psi_F=[F^\circ],
\]

so that \(\psi_F\perp\Omega\), and suppose the reconstruction gives, for
\(t\ge0\),

\[
Q_F(t):=S\!\left(\Theta F^\circ\,\tau_tF^\circ\right)
=\langle\psi_F,e^{-tH}\psi_F\rangle.
\]

Let \(\mathfrak F\) be a family for which the nonzero vectors \(\psi_F\) are
total in \(\Omega^\perp\). For each such vector define

\[
\rho_F=-\lim_{t\to\infty}\frac1t\log Q_F(t).
\]

Then the limit exists and

\[
\rho_F=\inf\operatorname{supp}\mu_F,
\qquad
\mu_F(B)=\langle\psi_F,E_H(B)\psi_F\rangle.
\]

If \(\Omega^\perp\ne\{0\}\), the bottom of the nonvacuum spectrum obeys

\[
m:=\inf\sigma(H|_{\Omega^\perp})
=\inf_{F\in\mathfrak F:\,\psi_F\ne0}\rho_F.
\]

Consequently, if some \(\Delta>0\) has the property that for every
\(F\in\mathfrak F\) there are finite \(C_F,t_F\) with

\[
0\le Q_F(t)\le C_F e^{-\Delta t}
\qquad(t\ge t_F),
\]

then \(\sigma(H)\cap(0,\Delta)=\varnothing\). If the theory is nontrivial so
that \(\Omega^\perp\ne\{0\}\), its mass \(m\) is finite and \(m\ge\Delta>0\).

### Proof

For nonzero \(\psi_F\), the spectral theorem writes \(Q_F\) as the strictly
positive Laplace transform of the nonzero finite positive measure \(\mu_F\),
so the logarithm is defined. Its support is nonempty and bounded below. If
\(\alpha_F=\inf\operatorname{supp}\mu_F\), then

\[
Q_F(t)\le \|\psi_F\|^2e^{-\alpha_Ft}.
\]

For every \(\varepsilon>0\), the definition of support gives positive
\(\mu_F\)-mass in
\([\alpha_F,\alpha_F+\varepsilon)\), and hence

\[
Q_F(t)\ge
\mu_F([\alpha_F,\alpha_F+\varepsilon))
e^{-(\alpha_F+\varepsilon)t}.
\]

Taking logarithmic large-time limits and then
\(\varepsilon\downarrow0\) proves \(\rho_F=\alpha_F\).

Because every \(\mu_F\) is supported in
\(\sigma(H|_{\Omega^\perp})\), one has \(\rho_F\ge m\). Conversely, for
every \(\varepsilon>0\), the restricted spectral projection
\(E_{H|_{\Omega^\perp}}([m,m+\varepsilon))\) is nonzero. Totality supplies an
\(F\) whose projection into that interval is nonzero, so
\(\rho_F<m+\varepsilon\). This proves the infimum formula. The exponential
bound gives \(\rho_F\ge\Delta\) whenever \(\psi_F\ne0\), and the infimum formula gives
\(m\ge\Delta\). Equivalently, semigroup Cauchy–Schwarz propagates the diagonal
bounds to the linear span of the \(\psi_F\), after which
[Note 0001](0001-dense-state-gap-criterion.md) applies. \(\square\)

## Regulator-to-limit corollary

Let \(r\in\mathbb N\) index finite regulators with lattice spacing
\(a_r\downarrow0\) and physical temporal extent tending to infinity. Assume
there is a limiting Schwinger functional \(S\) satisfying a corrected OS
reconstruction package—OS II's \(E0'\) and \(E1\)–\(E4\) in its stated
setting, or another theorem with the same needed consequences—with
reconstructed Hamiltonian satisfying
\(\ker H=\operatorname{span}\{\Omega\}\).
For every \(F\in\mathfrak F\), let \(R_rF\) be a specified renormalized
lattice representative and define its regulator-specific centering by

\[
(R_rF)^\circ=R_rF-S_r(R_rF)\mathbf1.
\]

Set

\[
Q_{r,F}(k)=S_r\!\left(
\Theta(R_rF)^\circ\,\tau_k(R_rF)^\circ
\right).
\]

Assume all of the following.

1. **Physical-time convergence.** Whenever admissible no-wrap integers
   \(k_r\) satisfy \(a_rk_r\to t\ge0\),
   \[
   Q_{r,F}(k_r)\longrightarrow Q_F(t).
   \]
   The diverging temporal extent must make such approximants available for
   each fixed \(t\). “No-wrap” means that the observable supports and their
   reflected/translated copies do not cross a periodic temporal seam.
2. **Uniform physical decay with arbitrarily small loss.** There is a single
   \(\Delta>0\) such that, for every \(F\in\mathfrak F\) and every
   \(0<\varepsilon<\Delta\), there are finite
   \(C_{F,\varepsilon}\), \(t_{F,\varepsilon}\), and
   \(r_{F,\varepsilon}\) for which
   \[
   0\le Q_{r,F}(k)
   \le C_{F,\varepsilon}
      e^{-(\Delta-\varepsilon)a_rk}
   \]
   whenever \(r\ge r_{F,\varepsilon}\),
   \(a_rk\ge t_{F,\varepsilon}\), and \(k\) is no-wrap admissible. The
   prefactor is independent of \(r\), \(a_r\), the volume, and \(k\).
3. **Totality.** The nonzero limiting classes \([F^\circ]\), not merely the
   regulator representatives, are total in \(\Omega^\perp\).
4. **Nontriviality.** At least one limiting centered class is nonzero.

Then the reconstructed Hamiltonian has a finite positive mass gap
\(m\ge\Delta\).

### Proof

Fix \(F\), \(\varepsilon\), and a physical time
\(t>t_{F,\varepsilon}\).
Choose admissible \(k_r\) with \(a_rk_r\to t\). Passing the uniform estimate
to the limit yields

\[
0\le Q_F(t)
\le C_{F,\varepsilon}e^{-(\Delta-\varepsilon)t}.
\]

The continuum proposition excludes spectrum in
\((0,\Delta-\varepsilon)\). Since this holds for every
\(\varepsilon\in(0,\Delta)\), it excludes all of \((0,\Delta)\). Totality
prevents a hidden low-energy sector, and nontriviality makes the nonvacuum
spectrum nonempty, so its positive infimum is finite. \(\square\)

## Why the epsilon form is used

A regulator prefactor may not simply be discarded. The displayed uniform
epsilon-loss estimate permits subexponential corrections only after they have
been converted into a regulator-independent \(C_{F,\varepsilon}\). A bound
whose prefactor diverges with cutoff or volume does not meet the hypothesis
unless a separate argument proves this uniform conversion.

## Exact missing Yang–Mills inputs

- a nontrivial continuum/infinite-volume limit of gauge-invariant Schwinger
  functions with the required ultraviolet behavior;
- corrected OS regularity, Euclidean covariance, reflection positivity, and
  reconstruction for that limit;
- renormalized local gauge-invariant representatives and control of operator
  mixing;
- totality of the exact observable family carrying the decay bound;
- a positive regulator- and volume-uniform physical decay rate.

Nothing in this note supplies any of those inputs.

## Source anchors

- Osterwalder and Schrader, [Axioms for Euclidean Green's functions
  II](https://doi.org/10.1007/BF01608978), especially the correction discussion
  and reconstructed Hilbert-space/semigroup relations on pp. 282, 287, and
  290–291.
- Lüscher, [Construction of a self-adjoint, strictly positive transfer matrix
  for Euclidean lattice gauge
  theories](https://doi.org/10.1007/BF01614090), for fixed-lattice transfer
  matrix context only.
- Osterwalder and Seiler, [Gauge field theories on a
  lattice](https://doi.org/10.1016/0003-4916(78)90039-8), for lattice
  reflection-positivity context only.
