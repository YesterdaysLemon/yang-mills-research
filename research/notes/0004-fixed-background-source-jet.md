# Note 0004: the fixed-background plaquette source jet

Claim ID: `YM-RG-003`

Kind: Lemma derived from a primary theorem

Evidence: E2 (bounded source-free-background consequence; internally checked)

Novelty: none claimed

## Imported theorem

Use Bałaban's [variational/background-field
paper](https://doi.org/10.1007/BF01229381) with all of its regularity,
smallness, geometry, and gauge-chart hypotheses.

- Theorem 1, p. 279, gives a unique minimizing gauge orbit
  \([U_1(V)]\) in the admitted one-step regular fixed-average space.
- Section G, pp. 305–309, fixes a local gauge branch for small relative coarse
  fields and proves its analytic expansion.
- Eq. (181), p. 307, gives coarse gauge covariance of the branch.
- Proposition 9 and Eqs. (182)–(190), pp. 307–309, give analyticity and an
  exponentially decaying derivative of the branch with respect to the coarse
  field.

This note does not reprove those results. It states and proves their elementary
consequence for a fixed source-free background.

## Statement

Let \(V\) lie in one of the analytic patches of Proposition 9 and let \(f\) be
a real plaquette profile of finite support. For real \(SU(2)\)-valued fields set

\[
J_f(V)=4\sum_p f_p
\left(1-\tfrac12\operatorname{Tr}U_1(V)_p\right).
\]

The value is independent of the representative of the minimizing orbit and is
invariant under coarse gauge transformations.

For the complex analytic branch, replace the real-slice plaquette action by
its holomorphic extension

\[
s_{\mathbb C}(U_p)=1-\tfrac12\operatorname{Tr}U_p.
\]

Then \(J_f\) is analytic in the local coarse coordinate
\(B=(1/i)\log V'\) used in Section G.

Proposition 9 also says that the component derivative kernel defined in its
Eq. (182) satisfies the indexed cell/scale decay inequalities (190). A finite
chain-rule specialization should transfer those bounds to \(J_f\), but the
exact indices and scale factors have not yet been transcribed into this
repository. Accordingly, no standalone quantitative quasilocal bound is part
of this E2 lemma.

Finally, the fixed-background source factor

\[
\mathcal R_{\mathrm{bg}}(z,V)=e^{-zJ_f(V)}
\]

is entire and zero free in \(z\), and

\[
\left.\partial_z\log\mathcal R_{\mathrm{bg}}(z,V)\right|_{z=0}
=-J_f(V).
\]

## Proof

Two minimizers in the orbit differ by a fine gauge transformation compatible
with the fixed coarse average. Plaquette holonomy transforms by conjugation,
so its trace, and hence \(J_f\), is representative independent. Eq. (181)
gives the same conjugation statement under a coarse transformation of \(V\),
which proves coarse gauge invariance.

Proposition 9 makes every fine link in the chosen representative an analytic
function of the local coarse coordinate \(B\). A finite product and trace of
analytic matrix-valued functions is analytic, and the finite \(f\)-weighted
sum preserves analyticity. The use of \(s_{\mathbb C}\), rather than a real-part
operation, is essential on the complexified domain.

The last identity follows directly from the definition of the exponential
source factor. \(\square\)

## Exact boundary

The raw one-block integral has instead

\[
-\left.\partial_z\log\mathcal R_{x,z,f}(V)\right|_{z=0}
=\mathbb E_{\nu_{x,V}}[\mathcal O_f],
\]

by Note 0003. In general this conditional expectation is **not** equal to
\(J_f(V)=\mathcal O_f(U_1(V))\). A chosen RG representation of their difference
must account for fluctuations and for any Jacobian or polymer terms introduced
by that representation. Controlling the difference is the next open theorem.

## Nonclaims

- No source-dependent minimizing branch is constructed.
- No scalar-source analyticity of the full block integral follows from
  source-free background analyticity.
- No uniform source radius, interacting cumulant bound, marginal
  classification, or large-field estimate is proved.
- No quantitative quasilocal derivative bound is claimed until Eq. (190)'s
  component indices, cells, scale factors, metric, and norms are transcribed.
- Nothing here removes a regulator or constructs continuum Yang–Mills theory.
