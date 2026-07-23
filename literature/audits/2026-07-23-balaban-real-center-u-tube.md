# Audit: Balaban regular domains and the real-center \(U\) tube

Date: 2026-07-23

Claim audited: YM-RG-031

Status: primary-source domain map complete; the complex plaquette estimate
is an independent repository proof; the common real-center family remains
an explicit hypothesis

## Immutable evidence

The official Project Euclid PDFs were inspected directly. Their SHA-256
digests are:

```text
RG I                  1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A
Gauge-fixing paper    7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB
```

Stable mirrors:

- [RG I](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.pdf)
- [Spaces of regular gauge field configurations](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-99/issue-1/Spaces-of-regular-gauge-field-configurations-on-a-lattice-and/cmp/1103942611.pdf)

Relevant one-based PDF pages are RG I 14--15 and gauge-fixing paper
3--5, 10--12, 22--23, and 26--27.

## RG I printed pp. 262--263

Direct inspection of the definition of
\(\mathcal U_j^c(X,\alpha _0,\alpha _1,\gamma _0)\) gives:

1. condition (i) writes \(U=U'\bar U\), keeps \(\bar U\) \(G\)-valued, and
   imposes curvature and local regularity bounds on \(\bar U\);
2. condition (ii) writes \(U'=\exp(i\xi A')\), with \(A'\) in the
   complexified algebra, and bounds \(A'\) and
   \(\nabla_{\bar U}^{\xi}A'\). The scale is carried in the superscripted
   derivative, not in a separate multiplier;
3. condition (iii) bounds the curvature of the total \(U\) and the direct
   independent \(J\); and
4. condition (iv) constructs its tested \(J_n\) from \(U\), not from the
   independent \(J\).

Printed p. 263 then chooses smaller constants in conditions (i)--(iii),
invokes the variational estimates, and concludes that condition (iv) holds
when the smaller curvature constant is sufficiently small. It explicitly
identifies sufficiently regular minimal configurations as examples.

This supports the logic of Note 0031: hold a smaller regular real
\(\bar U\) fixed, put the complex perturbation in \(U'\), control the total
curvature, and vary the independent \(J\) only under its unchanged direct
ceiling \(\alpha _0\). The smaller \(a_0,a_1\) mechanism is used for the
\(U\)-dependent condition (iv); it is not substituted for RG II Eq.
(1.34)'s third parameter. The page does not print a numerical strict margin
uniform over all regulators, physical centers, restrictions, and shifted
branches.

## Gauge-fixing paper

The paper's Eq. (1.21) factors the plaquette of \(U'U_0\) into transported
relative links and the plaquette of \(U_0\). Eqs. (1.47)--(1.50) identify
the covariant linear plaquette term and the quadratic commutator terms.
Printed p. 85 says explicitly that the Eq. (1.49) identity holds for
arbitrary \(A\) in the complexified Lie algebra.

Section E separately admits complexified configurations in its analytic
contraction argument on printed pp. 96--97. That statement belongs to the
linearizing gauge transformation and is not silently transferred to every
later theorem.

Section G assumes \(U_0\in\mathcal U_k(\{\Omega_j\},\alpha _0)\) and a
Lie-algebra-valued \(A\) satisfying the three scaled bounds in Eq. (1.140).
Eq. (1.141) gives the curvature cost
\(\alpha _0+2\alpha _2+8d\alpha _2^2\). Proposition 7 then constructs a
unique axial-gauge representative in the enlarged regular real space.
The proposition is not printed as a theorem for arbitrary complexified
\(A\).

Note 0031 therefore does not invoke Proposition 7 to obtain a complex
collar. It proves the needed estimate directly from the exact ordered
plaquette product:

\[
\left\|
\prod_{\ell=1}^4e^{i\xi X_\ell}
-1-i\xi\sum_{\ell=1}^4X_\ell
\right\|_{\rm op}
\le
\frac12q^2e^q,
\qquad
q=\xi\sum_{\ell=1}^4\|X_\ell\|_{\rm op}.
\]

This elementary inequality is valid for noncommuting complex matrices.
The covariant curl identity turns the linear term into \(O(\xi^2)\), while
the remainder is \(O(\xi^2\|A\|^2)\).

## Repository deduction

Under the declared common real-center hypothesis
\((\mathrm H_{\rm rc})\), the relative-log norm controls:

- the two quantities required by RG I condition (ii);
- the operator norm of the relative link field; and
- its covariant plaquette curl.

The explicit radius

\[
r_U
=
\min\left\{
1,\ a_1,\
\frac{a_0-\bar a_U}{c_+(1+8e^4)}
\right\}
\]

keeps the full complex \(U\) ball inside the smaller direct curvature
domain. The independent radius
\(\Delta_J=\alpha _0-\bar a_J\) keeps the direct \(J\) bound strict.
Because condition (iv) depends on \(U\), the Cartesian product of those
balls lies in every external domain used by a complete branch.

The one global real representative and its shifted bond permutations also
supply the simultaneous representative compatibility that Note 0030
previously named \((\mathrm H_J^{\rm conn})\). Rerunning the already proved
positive marked and connected estimates in the common product
\(H^\infty\) algebra leaves \(B_{\rm conn}\) unchanged. Banach-line Cauchy
then gives full global dual derivative norms \(B_{\rm conn}/r_U\) and
\(B_{\rm conn}/\Delta_J\).

## What is not sourced or proved

- The source does not prove one regulator-uniform global real
  representative with the strict constants required by
  \((\mathrm H_{\rm rc})\) for every retained physical center and nested
  shifted branch.
- A uniformly bounded, restriction-compatible transition atlas would be
  enough for the \(J\)-coordinate alone, with radius reduced by its operator
  bound. The source does not prove the required cocycle and restriction
  compatibility. Arbitrary complex gauge transitions are insufficient:
  \(\operatorname {Ad}_{\operatorname {diag}(t,t^{-1})}E_{12}=t^2E_{12}\).
- The source does not print the explicit radius above, the product-tube
  theorem, the marked \(H^\infty\) rerun, or the completed dual derivative
  bounds.
- Proposition 7 is not used as a complex theorem.
- A relative-log activity derivative is not yet the physical
  coarse-background derivative. The Eq. (190) kernel must still be paired
  quantitatively with the new norm, and the multiscale metric, mesh, and
  chart constants remain open.
- Nothing here proves a nonzero-source polymer gas, unrestricted raw-law
  identity, large-field estimate, RG iteration, continuum construction,
  axioms, infrared decay, or a Yang--Mills mass gap.

This audit was performed by AI agents and is not independent human review.
