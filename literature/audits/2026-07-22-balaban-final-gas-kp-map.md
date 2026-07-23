# Balaban final-gas and KP source audit — 2026-07-22

Status: primary-page support/species identification plus a repository
parameter refinement; no novelty claim, no marked estimate, and no
Yang--Mills solution claim.

This audit records the immutable inputs behind [Note
0024](../../research/notes/0024-balaban-final-gas-instantiation.md). It is
deliberately limited to Balaban's **final connected ordinary polymer gas**
after RG II Eq. (2.10). Intermediate localization and marked activities are
outside the identification.

## Immutable primary inputs

- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I*](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf),
  **CMP 109** (1987), 249--301.
- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories II. Cluster Expansions*](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf),
  **CMP 116** (1988), 1--22.

The downloaded files used for the audit had SHA-256 digests

```text
RG I   1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
RG II  EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC
```

The PDFs are evidence inputs and are not vendored. Page references below use
printed journal pages; the corresponding one-based PDF pages are RG I 3 and
9, and RG II 14, 20, and 21.

## Exact final-gas mapping

| Repository datum | Primary-page datum | Audit conclusion |
|---|---|---|
| Ambient periodic geometry | RG I p. 251 first forms continuous Euclidean space or the torus obtained by identifying opposite boundary points, then cubulates it | Periodic seams are read in the quotient cubical complex, not a separated fundamental-domain picture |
| Support class | RG I p. 257 defines \(\mathcal D_j\) as all finite connected families of closed side-\(M\) cubes, with connectivity through complete walls | The final connected supports are exactly the face-connected closed-cell supports declared in Note 0023 |
| Tree metric | RG I p. 257 defines \(d_j\) as the shortest contained continuous-space tree meeting every cube, divided by \(M\), and says a shortest cube-edge graph exists; RG II Eq. (2.30) uses a positive volume-to-\(d_j\) comparison | Equality with Note 0023's degenerate auxiliary metric is not asserted. Every source minimizer is admissible for the auxiliary infimum, so \(d_{\rm aux}\le d_j\), and the same contained-connector construction proves the \(\sqrt{D+3}\) hull inequality directly for \(d_j\). Note 0023's monotone-metric extension then transfers its animal and KP constants |
| Final species | RG II Eqs. (2.9)--(2.10), p. 14, sum the internal \(Z_0,D,P\) histories and factor a disconnected preactivity over connected components | After factorization there is one aggregated ordinary analytic activity \(H(Z)\) per connected final support, not one species per history |
| Incompatibility | RG II Eq. (2.11), p. 14, sets \(\zeta=0\) exactly when an intersection contains a cube or a complete cube wall | This is shared-label or full-face contact; edge-only and vertex-only contact are compatible |
| Output support | RG II Eq. (2.13), p. 14, groups by the literal equality \(\bigcup_i Z_i=X\) | Every nonzero connected graph term has the literal face-connected union required by Note 0023 |

The scale normalization has two equivalent forms:

\[
 d_{k+1}(Z)=\frac{\ell_k(Z)}{LM}
 =\frac{\ell_{k+1}(Z)}M.
\]

The first length is measured before the RG rescaling and the second after it.
Using \(LM\) with the already-rescaled length would insert a false extra
factor of \(L\).

RG II Eq. (2.38) prints a pointwise absolute-value bound on \(H(Z)\). The
repository takes its supremum over the relevant fixed-output analytic domain
when applying a polymer norm. That supremum notation is a repository
formalization, not a verbatim source formula.

## Intermediate objects excluded

The mapping does not apply to \(Y_0,Z_0,\widetilde Z_0,Z'_0,X_0\), the
random-walk domains, or the pre-factorization output in Eq. (2.8). Those
objects can be disconnected and mix scales. In particular, the interior-bond
rule can enlarge \(Z_0\), while RG II p. 13 forms \(Z'_0\) as a coarse
\(LM\)-cube cover of \(\widetilde Z_0\). The phrase "smallest localization
domain" in that intermediate construction is not used as a theorem that
arbitrary disconnected seeds possess a unique least face-connected
completion.

## Direct exponent-glyph audit

The Project Euclid page images, rather than only their damaged text layers,
show:

- RG II Eq. (2.38), p. 20:
  \((1-8\delta)\tfrac12L\kappa\);
- RG II Eq. (2.39), p. 21:
  \((1-9\delta)\tfrac12L\kappa\);
- RG II Eq. (2.41), p. 21:
  \((1-10\delta)\tfrac12L\kappa\);
- the next line:
  \((1-10\delta)L/2=1\) and
  \(\delta=\tfrac1{10}(1-2L^{-1})\).

Lemma 3 also prints

\[
 |H(Z)|\le C_3\varepsilon _1
 e^{-(1-8\delta)(L/2)\kappa d_{k+1}(Z)},
\]

with the symbolic finite constant

\[
 C_3=2(L+2)^4O(1)\,2E_0C_1
 \alpha_4^{-1}\alpha_6^{-1}M^q e^{C_2\kappa _1}.
\]

The source's \(O(1)\) is unspecified, so this is not a numerical evaluation.
The displayed formula does not contain \(\varepsilon _1\).

## Repository KP refinement

Put \(\lambda=(L/2)\kappa\). With the source's final choice of \(\delta\),
define

\[
 \Delta=\delta\lambda=\frac{L-2}{20}\kappa,
 \qquad a=(1-10\delta)\lambda=\kappa.
\]

After satisfying every displayed source lower bound on \(\kappa\), impose the
additional strict inequality

\[
 \kappa>\frac{1280\log8}{L-2},
\]

and choose \(\alpha=\Delta/64\). Then

\[
 \beta=a+2\Delta,
 \qquad a_\bullet^{\rm budget}=a+\Delta,
 \qquad 32\alpha=\Delta/2,
 \qquad \eta=3\Delta/2>64\log8.
\]

The \(a_\bullet^{\rm budget}\) value is only the numerical room left for a
future marked theorem, not an activity estimate. Thus every ordinary
exponent inequality in Note 0023 is strict. Its ordinary
four-dimensional pinned-KP inequality follows whenever

\[
 0<\varepsilon _1\le
 \frac{\Delta}
 {576C_3e^{\Delta/4+\sqrt7\kappa}
 C_{\rm an}^{\rm geom}(3\Delta/2)}.
\]

RG II p. 21 explicitly invokes \(\kappa\) sufficiently large and
\(\varepsilon _1\) sufficiently small. Its displayed earlier conditions on
\(e^{32\kappa _1}\varepsilon _1\) and
\(4B_0C_1e^{16\kappa _1}\varepsilon _1\) are upper bounds, so the new ceiling
can be intersected with them after the other constants in \(C_3\) are fixed.
RG I nevertheless says that \(\varepsilon _1\) has "numerous restrictions,"
and the two papers import results without enumerating all their hypotheses.
Full source compatibility is therefore conditional on those unlisted
restrictions also being preserved by downward shrinking. Balaban does not
print this KP inequality or choose this \(\alpha\); the window is a repository
sufficient refinement of the displayed hierarchy.

## What the audit does not establish

- It supplies no marked derivative of Lemma 3, marked conditioned-contour
  envelope, positive marked-kernel decay, marked gluing estimate, or
  decorated marked norm.
- It proves no common disk for an external observable source and no
  differentiated branchwise cluster expansion.
- It supplies no scaled physical \(U/J\) pullback, marginal projection,
  large-field theorem, RG iteration, continuum construction,
  Osterwalder--Schrader reconstruction, infrared decay, or mass gap.
- No independent human review has been recorded.
- The restrictions imported but not printed in RG I/II have not yet been
  reconstructed from the complete earlier-paper chain to verify their
  downward monotonicity in \(\varepsilon _1\).
