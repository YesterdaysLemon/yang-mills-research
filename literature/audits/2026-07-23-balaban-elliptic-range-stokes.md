# Balaban elliptic-range and coarse-Stokes source audit

Date: 2026-07-23

Purpose: type the differentiated background kernel, identify the linear
block and gauge-average normalizations, and separate source statements from
the finite-dimensional model in YM-RG-037.

## Immutable local records

The following primary PDFs were visually inspected:

```text
Averaging operations for lattice gauge theories
03409AD81885593D65535550EAFAC08639E66123D4ACF92462847AE2EE4DD7D6

Spaces of regular gauge field configurations on a lattice and gauge fixing
conditions
7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB

The variational problem and background fields in renormalization group
method for lattice gauge theories
1F480977608AD36286D074841E3DBB02CE842113F92B818D8BD88BCCFF88DF3C
```

Stable primary records:

- [Averaging operations](https://doi.org/10.1007/BF01211042);
- [regular configurations and gauge
  fixing](https://doi.org/10.1007/BF01466594);
- [variational problem and background
  fields](https://doi.org/10.1007/BF01229381).

The rendered pages checked were:

- averaging paper printed p. 19, Eqs. (10)--(15);
- averaging paper printed p. 28, the \(Q_0,Q'_0\) linear formulas and
  Eqs. (61)--(63);
- gauge-fixing paper printed p. 80, the definition of \(R(U_0)\) and
  Eq. (1.27);
- variational paper printed p. 281, Eqs. (19)--(21);
- variational paper printed p. 297, Eqs. (125)--(129);
- variational paper printed pp. 305--309, Eqs. (174)--(190) and
  Proposition 9.

Temporary page renders are QA artifacts and are not primary records.

## Literal averaging statements

Averaging-paper Eq. (14) displays the linear coarse field average with its
\(L^{-(d+1)}\) normalization. Equation (15) defines the nonlinear group
average and the following text says that Eq. (14) is its linear term.

For the relative field used later, printed p. 28 writes

\[
(Q_0A)(c)
=
\sum_{x\in B(c_-)}
L^{-d}(R_{0,c_-}A)([x,x(c)]),
\]

and

\[
(Q'_0\lambda)(y)
=
\sum_{x\in B(y)}
L^{-d}(R_{0,y}\lambda)(x).
\]

At a flat background, or on a commuting Cartan line fixed by all adjoint
transports, these are respectively an average of parallel length-\(L\)
paths and a scalar block mean. For \(L=2,d=4\), fields constant in two
coordinates give the \(1/4\)-normalized two-dimensional formulas used in
Note 0037's source-normalized finite model.

The source describes \(Q_0A\) on printed p. 28 as an approximation in its
nonlinear discussion. Exact flat-Cartan linearization is a repository
derivation; the retained sources do not prove that the homogeneous periodic
model embeds into the full multiscale \(H_1\) domain. It is not an assertion
that the same scalar formulas hold on a generic noncommuting background.

## Literal Landau projection

Gauge-fixing printed p. 80 defines

\[
N(Q'(U_0))
=
\{\lambda:Q'(U_0)\lambda=0\}
\]

and states that \(R(U_0)\) is the orthogonal projection onto

\[
\Delta_{U_0}^{\eta}N(Q'(U_0)).
\]

Equation (1.27) is the corresponding projected Landau condition. In the
source-normalized flat-Cartan finite model, the positive lattice-scale
factor in \(\Delta^\eta\) does not change its range, giving the model
projection onto \(\Delta\ker P\). Reduction of the source's complete
multiscale \(N(Q')\) to this single nullspace is not proved.

The source does not say \(D^*A=0\), impose a cell Dirichlet or Neumann
condition, or give a vanishing cell trace.

## Literal lift and derivative statements

Variational-paper Eq. (129), together with the immediately preceding
\(G=\Delta_a^{-1}\), gives

\[
H_0
=
GQ^*(QGQ^*)^{-1}
\bigl(L^{j(\cdot)}\eta\bigr)^{-1}.
\]

Equations (174)--(177) use the distinct lift \(H_1\), and Eq. (177) says the
expansion of \(\mathcal H\) begins with \(H_1B\). Therefore

\[
D_B\mathcal H(0)=H_1
\]

is an exact derivative of the printed expansion.

Equations (179)--(180) use the alternative lift \(H_0\) and define

\[
\widetilde G=(\Delta_a-\Delta^{(2)})^{-1}.
\]

Equations (182)--(184) are the differentiated system. Equations (185)--(187)
bound the Hessian by Cauchy and make its Green-composed action small in the
existing scaled raw/gradient norm. Equation (188) is the resulting Neumann
solution. Equation (190) bounds one common kernel and its output
derivatives.

The paper says before Eq. (182) that the derivative has regularity and decay
properties identical to \(H\) or \(H_0\). It does not print a stronger
same-cell transverse estimate.

## Derived, not printed

Put

\[
A_B=\mathcal A_0(B)+H_0B,
\quad
T_B=D_BA_B,
\quad
W_B=V''(A_B).
\]

Multiplication of Eq. (183) by
\(\widetilde G^{-1}=\Delta_a-\Delta^{(2)}\) gives

\[
\bigl(\Delta_a-\Delta^{(2)}+W_B\bigr)T_B
=
\Delta_aH_0.
\]

Combining this with Eq. (182) gives

\[
D_B\mathcal H(B)
=
\bigl(I-HD'(A_B)\bigr)
\bigl(\Delta_a-\Delta^{(2)}+V''(A_B)\bigr)^{-1}
\Delta_aH_0.
\]

These are exact algebraic consequences on the paper's fixed-background small
patch, not separately printed equations.

Likewise,

\[
\Delta_aH_0
=
Q^*(QGQ^*)^{-1}
\bigl(L^{j(\cdot)}\eta\bigr)^{-1}
\]

is an exact consequence of Eq. (129), not a literal display.

## Repository-only Stokes derivation

The following facts are proved in Note 0037, not attributed to the sources:

1. the differentiated right-inverse and projected-Landau constraints define
   an affine slice with nullspace
   \(\ker C\cap\ker S\);
2. the displayed rational \(4\times4\) field satisfies the
   source-normalized \(L=2\) flat-Cartan finite-model average and projected
   Landau condition;
3. the block average is a cochain map in this specialization;
4. discrete Stokes and the nonzero coarse curl of one localized coarse bond
   force raw \(s^{-1}\) and curl/gradient \(s^{-2}\) lower bounds.

This proves a strong-norm obstruction in the source-normalized finite model.
It does not identify that model with the actual multiscale \(H_1\) source
slice, prove that a generic noncommuting background has the same scalar
matrices, show that completed coefficients detect the modeled range, or
exclude weak-dual cancellation.

## Scope boundary

- The source equations give analyticity, an elliptic selection, and the
  rowwise bounds in Eq. (190).
- The repository finite model shows that normalized right-inverse and
  projected-Landau constraints alone do not force a two-power gain in a
  strong curl/gradient norm.
- Embedding the model into the full multiscale \(H_1\) domain, or proving
  that its Hessian-selected range retains the modeled curl, remains open.
- The completed coefficientwise Ward identity, full chart/restoration
  conversion, weak-dual annihilation or cancellation, nonzero-source
  polymer activities, RG iteration, continuum construction, reconstruction,
  infrared decay, and the mass gap remain open.
