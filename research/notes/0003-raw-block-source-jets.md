# Note 0003: exact source jets of a raw positive block transform

Claim ID: `YM-RG-002`

Kind: Lemma

Evidence: E2 (finite-regulator auxiliary result; internally checked only)

Novelty: none claimed

## Statement

Let \(\mathcal U\) be a finite product of compact gauge groups, let \(s\) be a
continuous real-valued conjugation-invariant plaquette action, and let \(f\)
(and \(h\) below) be a real-valued plaquette profile. For each admissible
coarse field \(V\), let \(K_L(V,dU)\) be a nonzero finite positive measure on
\(\mathcal U\). The measure may impose a block constraint, but it must be
independent of the inverse coupling \(x\) and of every source.

For a finite lattice define

\[
S_x(U)=4x\sum_p s(U_p),
\qquad
\mathcal O_f(U)=4\sum_p f_p s(U_p),
\]

and the raw blocked density

\[
Z_{x,z,f}(V)=
\int_{\mathcal U}
e^{-S_x(U)-z\mathcal O_f(U)}K_L(V,dU).
\]

Assume \(x>0\), set \(Z_x(V)=Z_{x,0,f}(V)\) (which is independent of
\(f\)), and write

\[
\nu_{x,V}(dU)=
\frac{e^{-S_x(U)}K_L(V,dU)}{Z_x(V)}.
\]

The denominator is independent of \(f\), strictly positive, and finite. For
each fixed finite regulator, \(V\), and \(f\), the ratio

\[
\mathcal R_{x,z,f}(V)=
\frac{Z_{x,z,f}(V)}{Z_x(V)}
\]

is entire in \(z\), equals one at \(z=0\), and therefore has a uniquely fixed
analytic logarithm on some neighborhood of zero. On that neighborhood,

\[
\left.\partial_z\log\mathcal R_{x,z,f}(V)\right|_{z=0}
=-\mathbb E_{\nu_{x,V}}[\mathcal O_f],
\]

and

\[
\left.\partial_z^2\log\mathcal R_{x,z,f}(V)\right|_{z=0}
=\operatorname{Var}_{\nu_{x,V}}(\mathcal O_f)\ge0.
\]

More generally, set

\[
Z_{x,z,w;f,h}(V)=\int e^{-S_x-z\mathcal O_f-w\mathcal O_h}\,dK_L.
\]

Independent sources for profiles \(f\) and \(h\) give the mixed jet

\[
\left.\partial_z\partial_w
\log\frac{Z_{x,z,w;f,h}(V)}{Z_x(V)}\right|_{z=w=0}
=\operatorname{Cov}_{\nu_{x,V}}(\mathcal O_f,\mathcal O_h).
\]

For the finite-volume constant profile \(f\equiv1\),
\(S_x+z\mathcal O_1=S_{x+z}\). Hence the raw transform obeys

\[
\left.\partial_z\log Z_{x,z,1}(V)\right|_{z=0}
=\partial_x\log Z_{x,0,1}(V).
\]

If the kernel is gauge covariant and the action/source observable are gauge
invariant, each displayed jet is a coarse-gauge-invariant function of \(V\).

## Proof

On a finite lattice, every plaquette action \(s(U_p)\) is continuous and
bounded on the compact configuration space. Thus \(\mathcal O_f\) is bounded
and real valued on the real configuration space.
For \(z\) in a compact subset of \(\mathbb C\), the exponential integrand and
each fixed source derivative are bounded by an integrable constant. Equivalently,
the exponential power series may be integrated term by term. Therefore
\(Z_{x,z,f}(V)\), and hence \(\mathcal R_{x,z,f}(V)\), is entire.

Positivity and nonzeroness of \(K_L(V,dU)\) imply
\(0<Z_{x,0,f}(V)<\infty\). Since \(\mathcal R_{x,0,f}=1\), continuity gives a
possibly \(V\)-, volume-, and profile-dependent zero-free disk. The condition
\(\log\mathcal R(0)=0\) fixes the logarithm there.

Differentiating the logarithm once gives

\[
\partial_z\log Z_{x,z,f}
=-\frac{\int\mathcal O_f e^{-S_x-z\mathcal O_f}\,dK_L}
{\int e^{-S_x-z\mathcal O_f}\,dK_L}.
\]

At \(z=0\) this is the negative conditional expectation. Differentiating
again gives the second cumulant, namely the variance; using two source
parameters gives the covariance formula. The constant-profile identity is the
chain rule applied to the exact equality
\(Z_{x,z,1}(V)=Z_{x+z,0,1}(V)\).

For gauge covariance, change variables by the fine gauge transformation
associated with a coarse transformation of \(V\). Covariance of the kernel and
invariance of \(S_x\) and \(\mathcal O_f\) leave each integral unchanged.
\(\square\)

## What this settles in Program 002

- the raw first and second source jets are conditional cumulants;
- the constant-profile first-jet identity is exact when the raw kernel is
  coupling independent;
- pointwise finite-volume analyticity supplies a local logarithm near zero;
- gauge covariance of the raw kernel passes to the source jets.

## What it does not settle

- The zero-free radius need not be uniform in volume, cutoff, source location,
  profile, or coarse field.
- A local fine observable can have a nonlocal conditional expectation as a
  function of \(V\); no polymer decay or profile-mixing bound follows.
- The variance and higher cumulants can grow with volume.
- No minimizing-background expansion, marginal classification, small-field
  estimate, or large-field estimate is proved.
- A coupling-dependent normalization contributes its own derivatives and is
  not part of the raw identity.
- Positivity is needed for the probabilistic sign/variance statement. A signed
  or complex gauge-fixed kernel requires a different formulation.
- Nothing here constructs a continuum theory, removes a regulator, or proves
  a mass gap.

## Falsification checks

- Insert an \(x\)-dependent kernel and observe the extra derivative term in
  the constant-profile identity.
- Insert an \(x\)-dependent normalization and keep its derivative separate.
- Test a signed kernel; the second derivative remains an algebraic cumulant
  but need not be nonnegative.
- Let the volume grow and verify that neither the zero-free radius nor the
  cumulants are claimed uniform.
- Remove gauge covariance of the kernel and verify that coarse gauge
  invariance no longer follows.
