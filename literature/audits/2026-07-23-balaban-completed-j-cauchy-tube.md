# Audit: Balaban domains and the completed affine-\(J\) tube

Date: 2026-07-23

Claim audited: YM-RG-030

Status: primary-source domain map complete; repository corollary remains
conditional on the previously declared hypotheses

## Immutable evidence

The official Project Euclid PDFs were inspected directly. Their SHA-256
digests are:

```text
RG I   1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
RG II  EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC
```

Stable mirrors:

- [RG I](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf)
- [RG II](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-116/issue-1/Renormalization-group-approach-to-lattice-gauge-field-theories-II-Cluster/cmp/1104161193.pdf)

Relevant one-based PDF pages are RG I 14--16 and RG II 10--11, 14--15,
and 20.

## What RG I says

Printed p. 262 defines the local orbit space
\(\mathcal U_j^c(X,\alpha _0,\alpha _1,\gamma _0)\). Direct inspection gives:

1. conditions (i) and (ii) are conditions on \(U\);
2. condition (iii), Eq. (1.14), includes
   \(|J|<\gamma _0\) on \(X\);
3. condition (iv), Eqs. (1.15)--(1.16), uses the pair
   \((U_n(M^j(U)),J_n(M^j(U)))\), with \(J_n\) defined from \(U\) by
   Eq. (1.8).

Therefore an additive change of the independent \(J\) variable changes only
condition (iii).

Printed p. 263 takes smaller constants, invokes Proposition 9, and explains
that sufficiently regular minimal configurations with the source-defined
\(J\) lie in the larger domain. It says that the analytic constants are
independent of \(X\) and \(j\), but it does not print a numerical strict
margin or a transported atlas. Note 0017 correctly records those missing
uniform local representative choices as hypothesis \((\mathrm H_J)\). It
does not provide one representative whose restrictions agree with every
overlapping activity chart on every complete shifted branch.

## What RG II says

RG II Eq. (1.34) uses

\[
\mathcal U_{k+1}^c
\bigl(Y,(1+\beta)\alpha _0,(1+\beta)\alpha _1,\alpha _0\bigr).
\]

The third parameter is not multiplied by \(1+\beta\). Lemma 2 states that
each localized potential is analytic on this space.

The paragraph beginning on printed p. 15 states that:

- the potentials selected by \(D\) extend to the Eq. (1.34) spaces;
- they are also analytic on the output subspace
  \(\mathcal U_{k+1}^c(X,\alpha _0,\alpha _1)\);
- the quadratic forms and covariances in \(H(Z)\) are analytic for
  configurations satisfying conditions (i)--(iii) on \(Z\), with larger
  constants; and
- the activities in Eq. (2.13), and the whole connected sum, are analytic
  functions of \((U,J)\) on the output space.

RG I printed p. 263 states that the third parameter is omitted when it equals
\(\alpha _0\). Thus RG II's two-parameter output notation retains the direct
condition-(iii) ceiling \(|J|<\alpha _0\).

Lemma 3 Eq. (2.38) then bounds \(H(Z)\) uniformly under all preceding
restrictions. The paper suppresses the external \((U,J)\) variables in the
displayed activity bound; Note 0024's fixed-output supremum norm is a faithful
repository notation for that uniform statement.

## Repository deduction

The source does not state a completed marked \(J\)-tube theorem. The
repository deduction uses four prior results:

1. Note 0030's completed compatibility hypothesis
   \((\mathrm H_J^{\rm conn})\), strengthening Note 0017's local
   \((\mathrm H_J)\), gives
   \(\|J\|_\infty\le\bar\alpha _0<\alpha _0\) in the representative shared
   simultaneously by all activity charts on one complete branch.
2. Restrictions and shifted bond permutations are contractions/isometries in
   the raw affine \(\ell^\infty\) coordinate.
3. Note 0029 proves that a coefficient indexed by \(R\) depends only on the
   complete bonds intersecting \(\operatorname {int}R\).
4. Notes 0024--0026 use pointwise positive majorants whose inputs are already
   suprema over the full source domains.

Consequently the radius is
\(\Delta_J=\alpha _0-\bar\alpha _0\). Rerunning the positive marked and
cluster estimates in the local \(H^\infty\) norm gives the sum of
coefficientwise tube suprema with the unchanged constant \(B_{\rm conn}\).
This rerun is essential: it is not valid to infer that stronger norm merely
by interchanging a support sum and support-dependent suprema in Note 0027's
pointwise estimate.

Banach-line Cauchy then gives the dual \(\ell^\infty\) derivative norm.
Note 0029 locality identifies the restricted and global dual norms without a
bond count.

## What is not sourced or proved

- Balaban does not print the marked dual-number construction, the
  \(H^\infty\) rerun, the shifted normalization, or the completed derivative
  bound.
- The numerical and simultaneously compatible representative premise
  \((\mathrm H_J^{\rm conn})\) remains a named hypothesis. Complex gauge
  changes need not preserve the chosen raw \(\ell^\infty\) norm, so separate
  local representatives do not suffice.
- The independent affine \(J\) tube is not a physical-source disk and is not
  a nonzero plaquette-source polymer expansion.
- \((\mathrm H_\rho)\), bounded mesh matching, common kernel/chart constants,
  and the scaled nonlinear \(U\) collar remain open.
- Nothing here proves a large-field estimate, RG iteration, continuum
  construction, axioms, infrared decay, or a Yang--Mills mass gap.

This audit was performed by AI agents and is not independent human review.
