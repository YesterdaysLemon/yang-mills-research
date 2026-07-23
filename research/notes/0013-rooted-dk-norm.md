# Note 0013: the rooted \(d_k\)-weighted norm for one interior mark

Claim ID: YM-RG-013

Kind: finite-regulator geometry and entropy corollary

Evidence: E2 (conditional finite-regulator norm; internally checked)

Novelty: none claimed

## Specialized geometry

Retain every hypothesis and definition of Note 0012. Specialize its fixed
localization partition to the standard RG-I/II family \(\pi_k\) of
wall-adjacent \(M\)-cubes used for the Wilson localization branch. Thus the
root \(Q_p\) is one \(M\)-cube, \(p\) lies strictly in its interior, and

\[
Y=Q_p\cup A,
\qquad
m(Y)=|A|,
\tag{1}
\]

is a connected finite union of \(M\)-cubes.

RG I p. 257 writes the scale label as \(j\); this note relabels \(j=k\) and
\(X=Y\). It defines \(d_k(Y)\) as \(M^{-1}\) times the length of a shortest
tree graph contained in \(Y\) and meeting every cube of \(Y\). It also records
an equivalent shortest construction using cube edges. For \(m(Y)\ge1\),
choose a spanning tree of the wall-adjacency graph on its \(m(Y)+1\) cubes
and join the centers of adjacent cubes. Every segment has length \(M\), lies
in the union of the two cubes sharing its wall, and the tree has \(m(Y)\)
edges. For \(m(Y)=0\), a single cube edge gives an admitted graph of normalized
length \(1\). Thus, without imposing a degenerate one-vertex convention on
the source metric,

\[
\boxed{d_k(Y)\le \max\{1,m(Y)\}\le m(Y)+1.}
\tag{2}
\]

The fully decoupled root term is retained with the harmless weight
\(e^a\). This avoids identifying Balaban's convention on singleton domains:
RG II Eq. (2.30) is not compatible with using a zero singleton distance in
every source estimate.
For a different weakening partition made of larger \(R_1M_1\)-cubes, (2)
must be replaced by an explicitly proved
\(d_k(Y)\le c_{\rm geo}(m(Y)+1)\); no such generalization is used below.

## Imported pointwise estimate

Note 0012 proves on the restricted RG-II Eq. (1.34) domain that

\[
|W_{k,p}(Y;U,J,B)|
\le
C_{\rm mark}e^{16\kappa _1}g_k\lVert B\rVert_Y
(e^{\kappa _1}-1)^{-m(Y)},
\tag{3}
\]

and hence the same estimate with
\(g_k\lVert B\rVert_Y\le\varepsilon _1\). It also proves that the number of
root-connected supports with \(m\) added cubes is at most \(D_0^{2m}\). For
four-dimensional wall adjacency, \(D_0\) may be taken as

\[
D_0=2d=8.
\tag{4}
\]

No quadratic or cubic fluctuation gain is added to (3); the one-plaquette mark
can have a nonzero linear term.

## The weighted norm

RG II Eq. (1.32) permits \(0<\delta<1\). Impose the stronger range needed for
a positive retained exponent and fix

\[
0<\delta<\frac12,
\qquad
a=(1-2\delta)\kappa>0,
\tag{5}
\]

and define the exact entropy ratio

\[
q_d=
\frac{D_0^2e^a}{e^{\kappa _1}-1}.
\tag{6}
\]

Using (2), (3), and the animal count gives

\[
\begin{aligned}
&\sup_{p\in\mathcal P_{\rm int}(\pi_k)}
\sum_{Y\supset Q_p}
e^{a d_k(Y)}
\sup_{\mathrm{Eq.\ (1.34)}|_Y}|W_{k,p}(Y)|\\
&\qquad\le
e^aC_{\rm mark}e^{16\kappa _1}\varepsilon _1
\sum_{m\ge0}
\left[
\frac{D_0^2e^a}{e^{\kappa _1}-1}
\right]^m.
\end{aligned}
\tag{7}
\]

Consequently, whenever \(q_d<1\),

\[
\boxed{
\sup_{p\in\mathcal P_{\rm int}(\pi_k)}
\sum_{Y\supset Q_p}
e^{(1-2\delta)\kappa d_k(Y)}
\sup_{\mathrm{Eq.\ (1.34)}|_Y}|W_{k,p}(Y)|
\le
\frac{e^aC_{\rm mark}e^{16\kappa _1}\varepsilon _1}{1-q_d}.
}
\tag{8}
\]

This also gives the individual RG-II-style decay

\[
|W_{k,p}(Y)|
\le
\frac{e^aC_{\rm mark}e^{16\kappa _1}\varepsilon _1}{1-q_d}
e^{-(1-2\delta)\kappa d_k(Y)}.
\tag{9}
\]

The norm is uniform in finite volume, RG scale, and the location of plaquettes
strictly interior to the fixed \(\pi_k\) partition. Linearity gives the safe
profile corollary proportional to \(\sum_p|f_p|\) for profiles supported on
those plaquettes only.

## Closure under a source-safe parameter consequence

RG II Eq. (1.32) prints the range \(0<\delta<1\) and a hierarchy involving
\(\kappa _1-1\). The searchable text layers available in this audit drop a
leading glyph before that parenthesis, so this note does not claim an exact
transcription of the printed prefactor. Both candidate readings found during
the audit imply the weaker consequence

\[
\kappa _1-1\ge(1-\delta)\kappa.
\tag{10}
\]

Equation (10) is the only hierarchy consequence used below. Independently
rendering and transcribing the dropped prefactor remains a source-audit item.

For \(\kappa _1\ge\log(e/(e-1))\), in particular in the printed
sufficiently-large regime,

\[
(e^{\kappa _1}-1)^{-1}\le e^{-(\kappa _1-1)}.
\tag{11}
\]

Combining (5), (6), (10), and (11),

\[
q_d
\le D_0^2
e^{(1-2\delta)\kappa-(\kappa _1-1)}
\le D_0^2e^{-\delta\kappa}.
\tag{12}
\]

Thus a transparent sufficient entropy margin is

\[
\boxed{\delta\kappa>2\log D_0.}
\tag{13}
\]

In four dimensions, (4) makes (13)

\[
\boxed{\delta\kappa>\log64.}
\tag{14}
\]

Under (10) and (14), (8) holds with the explicit denominator bounded below by
\(1-64e^{-\delta\kappa}>0\).

RG II says that \(\delta\kappa\) is taken sufficiently large when it spends the
\(X\)-entropy after Eq. (1.32), but it does not print the numerical threshold
\(\log64\). Equations (13)--(14) are this repository's explicit one-mark animal
bookkeeping, not a verbatim Bałaban constant.

## What this closes and what it does not

Equation (8) closes Note 0012's fixed-partition-interior \(d_k\)-norm upgrade
at the same retained exponent \((1-2\delta)\kappa\) used in RG II Lemma 1.
This is stronger than merely rewriting a pointwise bound: the animal entropy
has been paid explicitly through \(q_d\).

It does not by itself make the marked activity compatible with the later
Lemma 3 exponent, which spends further decay in the cluster construction. The
later Note 0021 carries the rooted seed through the exact finite Section-2
algebra and isolates the required marked domination, gluing, and animal
entropy hypotheses; it does not prove them for the actual activities.

## Exact boundary

- The theorem is conditional on Note 0012, the selected \(\pi_k\) geometry,
  the source-safe consequence (10), common to the candidate readings of RG II
  Eq. (1.32), and the explicit added entropy margin (13).
- It covers plaquettes strictly interior to one fixed partition. Note 0014
  subsequently supplies an RG-admitted shifted-family cover for
  boundary-crossing plaquettes and transport under the subgroup preserving the
  next coarse lattice. Note 0021 subsequently proves one-fixed-partition
  algebraic compatibility for an interior root, and Note 0026 proves the
  marked norm and first-jet sum on that fixed partition. Unit-translation
  covariance and shifted synchronization remain open.
- The activities are local only in independent \((U,J,B)\). No locality or
  quasilocality after the physical specialization
  \((U,J)=(U_{k+1}(W),J_{k+1}(W))\) is inferred.
- Note 0021 subsequently proves the exact cutoff-conditioned marked
  numerator/denominator algebra, and Note 0026 proves the fixed-partition
  marked decay and convergence theorem. No marginal projection,
  profile-mixing theorem, or large-field bound follows.
- The result concerns the exact selected RG-coordinate branch, not the
  intrinsic coarea or unrestricted raw law.
- No RG iteration, continuum construction, Osterwalder--Schrader
  reconstruction, infrared decay estimate, or mass gap follows.

## Falsification checks

- Replace wall adjacency by a different weakening geometry and check that the
  proof fails unless a new \(c_{\rm geo}\) is inserted.
- Omit the root term \(m=0\) or its extra factor \(e^a\) and lose the
  source-convention-safe singleton estimate.
- Use \(d_k(Y)\le m(Y)+1\) in the wrong direction and observe that the weighted
  estimate no longer follows.
- Set \(\delta\kappa=\log64\) and observe that (12) no longer proves strict
  convergence.
- Claim (14) is printed in RG II and compare it with the paper's qualitative
  "sufficiently large" statement.
- Substitute the minimizing background or enter the Section 2 cluster sum and
  identify the missing theorems rather than treating (8) as their proof.
