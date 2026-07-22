# Note 0006: the local Bałaban fiber chart

Claim ID: YM-RG-006

Kind: Lemma derived from a primary construction

Evidence: E2 (one finite-regulator local-chart corollary; internally checked)

Novelty: none claimed

## Imported construction

Use RG I, [*Generation of effective actions in a small field approximation
and a coupling constant renormalization in four
dimensions*](https://doi.org/10.1007/BF01215223), with every geometry,
regularity, smallness, and gauge-chart hypothesis imposed on pp. 265–268.
Fix \(d=4\), odd \(L>11\), the paper's finite torus, compact semisimple
\(G\subset U(N)\), and a coarse field \(W\) in the admitted domain for which
\(U_{k+1}(W)\in\mathcal U_{k+1}(\varepsilon_0)\) exists.

The source facts used below are:

- Eqs. (2.2)–(2.3), p. 265, give the associated critical configuration
  \(V^{(k)}(W)\) with block average \(W\).
- Eq. (2.4), p. 266, writes the relative constraint, for
  \(V'=e^{iB'}\), as

  \[
  M(V'V^{(k)})M(V^{(k)})^{-1}
  =e^{i\widetilde Q(B')}.
  \tag{RG I 2.4}
  \]

- On p. 267, after Eq. (2.10),

  \[
  \widetilde Q(B')=L\widetilde Q B'+\widetilde C(B'),
  \qquad
  \widetilde C(B')=O((B')^2).
  \tag{7}
  \]

  One corridor bond \(b_0(c)\) is selected for each coarse bond \(c\), and a
  right inverse \(h\), supported on those bonds, is chosen so that

  \[
  L\widetilde Qh=I.
  \tag{8}
  \]

- The same page constructs a unique analytic \(\widetilde D(B)=O(B^2)\) and
  the change of variables

  \[
  B'=\Theta(B)=B-h\widetilde D(B),
  \qquad
  \widetilde Q(\Theta(B))=L\widetilde QB.
  \tag{9}
  \]

- On p. 268, the group delta is reduced to the linear constraint and eliminates
  the variables on \(b_0(c)\). The paper then writes \(B'=CB\), where \(B\)
  collects the remaining independent-bond variables and \(C\) is the embedding
  determined there by \(V^{(k)}\). Eq. (2.12) retains the coordinate Jacobian
  as

  \[
  \exp\operatorname{Tr}\log\!\left(
  I-h\frac{\delta\widetilde D}{\delta B}(g_kCB)
  \right),
  \tag{RG I 2.12 Jacobian}
  \]

Eq. (2.9), p. 266, imposes the fixed-\(\varepsilon_1\) cutoff only on the
independent bonds \(b\ne b_0(c)\), and it equals one at \(B'=0\).

## Statement

At \(V^{(k)}(W)\), the Eq. (0.12) one-step averaging constraint is a local
real-analytic submersion. In the relative logarithmic chart it is analytically
conjugate to the surjective linear map \(L\widetilde Q\).

There is a sufficiently small real neighborhood of \(B'=0\) in which:

1. the coordinate change \(\Theta\) is a real-analytic diffeomorphism;
2. its real coordinate determinant is nonzero and has the positive orientation
   fixed at the origin;
3. the fixed-\(\varepsilon_1\) constrained fiber contains a nonempty relatively
   open ball about the background point; and
4. after normalized Haar/group-delta conventions are fixed, any sufficiently
   small precompact such fiber ball has finite strictly positive coarea mass.

The neighborhood and all upper/lower bounds in this statement may depend on
the finite torus, scale, coupling-coordinate convention, coarse field, chart,
and cutoff parameters. No uniformity is claimed.

## Proof

Eqs. (2.2)–(2.4) put \(B'=0\) on the fiber over the admitted \(W\). Equations
(7)–(9) give the exact analytic normal form. Since
\(\widetilde D(B)=O(B^2)\),

\[
D\Theta(0)=I.
\]

The analytic inverse-function theorem therefore makes \(\Theta\) a local
real-analytic diffeomorphism. Equation (9), together with the right inverse
\(L\widetilde Qh=I\), shows that the differential of the nonlinear constraint
is onto at the background. Surjectivity persists on a sufficiently small
neighborhood, so the constraint is a local analytic submersion there.

The real coordinate determinant of \(D\Theta\) is one at the origin and is
continuous. After shrinking the real neighborhood, it is nonzero and retains
positive orientation. Eq. (2.12) prints the determinant with its rescaled
argument \(g_kCB\); the constant-orientation conclusion is the local continuity
corollary used here, not a printed uniform RG-I estimate. No absolute
determinant is inserted after analytic continuation.

The fixed cutoff in Eq. (2.9) concerns only the independent coordinates and is
strictly satisfied at the origin. Shrink once more so the independent
coordinates stay inside the cutoff and the analytically solved dependent
coordinates remain inside the logarithm/gauge chart. The constrained slice
then contains a nonempty relatively open fiber ball.

On a smaller precompact ball, the Haar-coordinate density and positive normal
Jacobian are continuous and strictly positive; the separate real coordinate
determinant also stays nonzero with fixed orientation. The fiber ball has
positive finite Riemannian volume. Therefore the local fiber integral of the
Haar density divided by the positive normal Jacobian is finite and strictly
positive: its integrand is continuous and bounded above and below by positive
constants on the compact closure. This is the compactly supported local
instance of the coarea density in Note 0005; it does not invoke that note's
global proper-surjective hypotheses. \(\square\)

## Exact boundary

This result constructs only a local positive contribution around the
source-free background. It does **not** prove that the entire Eq. (2.9)
restricted transform has a pointwise fiber kernel with uniform positive mass.
RG II Eqs. (1.19)–(1.20) later prove that the complete independent-bond cutoff
cube on the already selected near-identity branch stays inside one analytic
chart; see the imported-map audit. That later support-containment result is not
used in this local proof and does not identify the branch with the unrestricted
raw group fiber. Note 0008 combines it with intrinsic coarea to define the
pointwise measure on the complete selected branch.

Program 003 still has to:

- transcribe the branch's joint Borel/background dependence and exact
  Haar/group-delta normalization on each named patch;
- keep remote logarithmic branches explicitly outside the theorem unless a
  complement estimate is proved;
- establish the required coarse-gauge covariance or use only a justified
  gauge-invariant patch formula; and
- formulate uniform normalized/log-extensive estimates rather than assume a
  volume-independent lower bound on total raw mass.

The construction is not a global submersion or surjectivity theorem. It gives
no result for arbitrary or merely plaquette-small coarse fields, no global
logarithm or gauge slice, and no large-field statement. By itself it supplies
no source zero-free disk, marked-polymer estimate, continuum theory, infrared
bridge, or mass gap.

## Falsification checks

- Verify \(L\widetilde Qh=I\) with the selected \(b_0(c)\); failure destroys
  the submersion conclusion.
- Check \(D\widetilde D(0)=0\) and the unit coordinate determinant at the
  background.
- Enlarge the ball toward a chart boundary and search for a zero or orientation
  change of the real coordinate determinant, or degeneration of the positive
  normal Jacobian.
- Check that the solved \(b_0(c)\) variables remain inside every stated
  small-field condition, not only the independent-bond cutoff.
- Distinguish a positive local fiber ball from a positive uniform lower bound
  for the whole restricted transform.
- Do not infer pointwise covariance from an arbitrary almost-everywhere
  conditional version.
