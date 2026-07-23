# Note 0027: shifted first-jet synchronization through nested Section-2 branches

Claim ID: YM-RG-027

Kind: finite-regulator projective first-jet reconstruction and shifted-family
corollary

Evidence: E2 (exact finite algebra plus transported estimates; internally
checked)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I. The Generation of Effective Actions in a Small Field
  Approximation and a Coupling Constant Renormalization in Four
  Dimensions*](https://doi.org/10.1007/BF01215223), especially the symmetry
  convention preceding Eq. (2.17), Eq. (2.17), and the fluctuation
  transformation after Eqs. (2.17)--(2.18);
- T. Balaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories II. Cluster
  Expansions*](https://doi.org/10.1007/BF01239022), especially Lemma 2
  Eqs. (1.41)--(1.43) and the exact finite identities
  Eqs. (2.1)--(2.13).

The source papers are unmarked and use one chosen cubulation. The nested-shift
family, dual-number insertion, projective branch comparison, and normalized
averaging below are repository corollaries.

## Result and correction to the open interface

Notes 0020--0026 left the synchronization hypothesis
\((\mathrm H_{\rm sync})\) open. The missing statement is not a zero-free
disk for the underlying scalar source ratio. Notes 0007 and 0010 already give
that disk on the real selected-coordinate law. What was missing was proof
that every completed shifted Section-2 gas is a projective rewriting of the
**same first jet**.

This note proves that finite-regulator statement. The proof has three
features which must remain separate.

1. Each shift is carried through the complete unmarked and marked Section-2
   construction on its own gas.
2. Exactness is proved before taking a logarithm: the gas and marked numerator
   on every branch reconstruct the same dual-number integral, up to one
   nonzero source-parameter-independent scalar.
3. The normalized shift average is taken only after each branch connected
   coefficient has been formed.

Covariance of bare marked activities alone would not be enough. The exact
projective reconstruction in item 2 is the synchronization theorem.

## The nested shift lift

Use the setting of Note 0014, strengthen the periodic compatibility to

\[
M=L^m,\qquad m\ge2,\qquad LM\mid N,
\tag{1}
\]

and work in the \(k\)-scale coordinates. The input localization cubes have
side \(M\), while the second localization in RG II Eq. (2.8) uses cubes of
side \(LM\). An input partition shift is specified only modulo \(M\); that
does not uniquely specify the output \(LM\)-cubulation. Retaining only an
arbitrary representative would make the output geometry representative
dependent.

Resolve this by lifting the shift:

\[
\widetilde S_{M,L}
=(L\mathbb Z/LM\mathbb Z)^4,
\qquad
\bar s=s\pmod M.
\tag{2}
\]

For \(s\in\widetilde S_{M,L}\), let \(\tau_s\) be translation by \(s\), and
transport the nested pair

\[
\pi_k^{\bar s}=\tau_s\pi_k^0,
\qquad
\pi_{k+1}^{s}=\tau_s\pi_{k+1}^0.
\tag{3}
\]

The second partition in (3) consists of side-\(LM\) cubes in \(k\)-scale
coordinates. After rescaling to \(k+1\) coordinates, it is the side-\(M\)
cubulation shifted by \(s/L\).

Define

\[
\widetilde{\mathcal A}_{M,L}(p)
=\{s\in\widetilde S_{M,L}:
  \bar s\in\mathcal A_{M,L}(p)\}.
\tag{4}
\]

Every residue \(\bar s\) has exactly \(L^4\) lifts, so Note 0014 Eq. (4)
gives

\[
\widetilde n_p
:=
|\widetilde{\mathcal A}_{M,L}(p)|
=L^4n_p>0.
\tag{5}
\]

The two cubulations in (3) are nested. Hence the input root
\(Q_{p,s}\in\pi_k^{\bar s}\) lies in a unique output cube
\(\widehat Q_{p,s}\in\pi_{k+1}^{s}\). This is the root used in the
branchwise version of Note 0026.

The \(L^4\) lifts are not new physical insertions. They are distinct
two-scale geometric branches with the same input-partition residue and
possibly different output \(LM\)-cubulations. Retaining all of them avoids a
noncovariant representative choice. Their normalization is paid once, after
the connected branch map.

## One common dual-number integral

Let

\[
\mathbb D=\mathbb C[\epsilon]/(\epsilon^2).
\tag{6}
\]

For fixed \(p\), let \(\mathfrak D_s\) denote the admitted holomorphic
external \((U,J)\) domain for the complete branch \(s\), and define

\[
\mathfrak D_p^\cap
=
\bigcap_{s\in\widetilde{\mathcal A}_{M,L}(p)}\mathfrak D_s.
\tag{6a}
\]

The projective comparison below assumes that this finite intersection is
nonempty and contains the common physical real source-free point. All
branchwise identities that are compared or summed are restricted to
\((U,J)\in\mathfrak D_p^\cap\). Branchwise norm estimates may still be
proved first on their separate transported domains.

At one finite regulator, freeze the source-free background, cutoff,
covariance, quadratic operator, and chart as in Notes 0011 and 0021. In
independent \((U,J,B)\) variables define the common first jet

\[
\mathscr I_p^{\mathbb D}(U,J)
=
\int\chi_k(B)e^{\Psi_k(U,J,B)}
\bigl(1-\epsilon\Delta_p(U,J,B)\bigr)
\,d\mu_{\Gamma_k(U,J)}(B).
\tag{7}
\]

This is exactly the reduction modulo \(\epsilon^2\) of the finite integral
with \(e^{-\epsilon\Delta_p}\). No analytic source-dependent RG induction is
being assumed.

For every \(s\in\widetilde{\mathcal A}_{M,L}(p)\), transport the complete
source-free Lemma-2 construction, not only the marked outer function.
Turning all first-stage weakening variables on gives

\[
\Psi_k(U,J,B)
=c_{k,s}(U,J)
+\sum_{Y\in\mathcal D_k^{\bar s}}
 V_k^s(Y;U,J,B),
\tag{8}
\]

where \(c_{k,s}\) is independent of \(B\) and of \(\epsilon\). Likewise the
shifted rooted construction gives

\[
\Delta_p(U,J,B)
=
\sum_{A\supset Q_{p,s}}
W_{k,p}^s(A;U,J,B).
\tag{9}
\]

Here is the exact unmarked reconstruction argument, which is separate from
the marked identity. Let \(T_s\) denote the orthogonal relabelling of the
independent fluctuation coordinates induced by \(\tau_s\), and abbreviate
\(x=(U,J)\). Apply the standard-branch Lemma-2 identity at
\((\tau_s^{-1}x,T_s^{-1}B)\):

\[
\Psi_k(\tau_s^{-1}x,T_s^{-1}B)
=c_{k,0}(\tau_s^{-1}x)
+\sum_{Y\in\mathcal D_k^0}
 V_k^0(Y;\tau_s^{-1}x,T_s^{-1}B).
\tag{8a}
\]

The undecoupled source-free exponent is covariant, so the left side is
\(\Psi_k(x,B)\). Define

\[
c_{k,s}(x):=c_{k,0}(\tau_s^{-1}x),
\qquad
V_k^s(\tau_sY;x,B)
:=
V_k^0(Y;\tau_s^{-1}x,T_s^{-1}B).
\tag{8b}
\]

Relabelling the finite sum in (8a) proves (8). In the same notation the
fixed global law obeys

\[
\chi_k(T_s^{-1}B)=\chi_k(B),
\qquad
(T_s)_*
\mu_{\Gamma_k(\tau_s^{-1}x)}
=\mu_{\Gamma_k(x)}.
\tag{8c}
\]

Thus a shifted branch does not replace the global cutoff or Gaussian law by
a new physical measure. Its later restricted covariances and
interior/exterior measures are exact Schur-complement coordinates for the
same law.

Equation (9) is proved independently by applying the standard rooted identity
to \((\tau_s^{-1}p,\tau_s^{-1}x,T_s^{-1}B)\), then using covariance of the
plaquette insertion and relabelling its finite support sum. This is the
nested-lift version of Note 0014 Eq. (6). The full-on weakening sums
reconstruct the undecoupled functions, so neither (8) nor (9) depends on the
termwise choice of random-walk expansion.

Substitution of (8)--(9) in (7) yields, for every \(s\),

\[
\mathscr I_p^{\mathbb D}
=e^{c_{k,s}}
\int\chi_k e^{\sum_YV_k^s(Y)}
\left(
1-\epsilon\sum_{A\supset Q_{p,s}}W_{k,p}^s(A)
\right)d\mu_{\Gamma_k}.
\tag{10}
\]

Thus all branches start from one integral, rather than from merely
equivariant but otherwise unrelated gases.

## Relabelling the complete Section-2 construction

For representative independence, let \(\mathsf H_{01}\) be the finite
stabilizer of the nested standard pair
\((\pi_k^0,\pi_{k+1}^0)\) in the coarse-lattice-preserving finite symmetry
group. As in Note 0014, replace every generalized-random-walk expansion used
in the two localization stages by its finite
\(\mathsf H_{01}\)-average and transport it by \(\tau_s\).

The average preserves:

- the exact summed propagator or operator;
- localization, because every summand is relabelled back to the same
  support label;
- every printed uniform estimate, by the triangle inequality; and
- the source-free analytic domain, by isometric transport.

Every operation in RG II Eqs. (2.1)--(2.13) then intertwines with this
transport. Explicitly:

1. finite potential subfamilies \(D\), their unions, and the marked seed
   \(A\cup\bigcup_{Y\in D}Y\) are carried bijectively;
2. exterior-bond subsets \(P\), \((-1)^{|P|}\), smallest \(Z_0\), enlarged
   domains, and the smallest side-\(LM\) cover \(Z'_0\) are preserved;
3. coordinate restrictions are conjugated by the induced orthogonal
   permutation of fluctuation coordinates, so determinants, conditioned
   Gaussian integrals, and standardization agree after change of variables;
4. weakening derivatives, their integration cubes, and final output
   supports \(Z\) are relabelled bijectively;
5. connected components, the cube-or-wall incompatibility relation, literal
   hulls, and the transported source tree metric are preserved.

The localized mark remains on the conditional interior \(B\), exactly as in
Note 0025, and is linear in its distinguished slot. No derivative hits the
cutoff, covariance, determinant, or weakening sector.

Run the finite construction in \(\mathbb D\). For connected output \(C\),
write

\[
H_{p,s,\epsilon}(C)
=H_s(C)-\epsilon W_{p,s}^{\rm post}(C),
\qquad
W_{p,s}^{\rm post}(C)
=-\left.\partial_tH_{p,s,t}(C)\right|_{t=0}.
\tag{11}
\]

Let \(\mathcal Z_s\) be the unmarked final hard-core polynomial and let

\[
\mathcal N_{p,s}
=
\sum_{C\supset\widehat Q_{p,s}}
W_{p,s}^{\rm post}(C)\,\mathcal Z_s[C].
\tag{12}
\]

Exactness of Eqs. (2.1)--(2.11), including all scalar Gaussian
normalizations, gives a nonzero \(\epsilon\)-independent scalar
\(S_s(U,J)\) such that

\[
\boxed{
\mathscr I_p^{\mathbb D}
=S_s(U,J)
\bigl(\mathcal Z_s-\epsilon\mathcal N_{p,s}\bigr)
\quad\text{in }\mathbb D .
}
\tag{13}
\]

At the common physical real selected-coordinate point, Note 0010's
source-free law is positive, so
\(\mathscr I_p(0)>0\) and hence \(\mathcal Z_s\ne0\). On the common complex
domain used for the connected theorem, Note 0024's ordinary KP hypothesis
instead supplies \(\mathcal Z_s\ne0\) through its absolutely convergent
cluster logarithm. More generally, the ratio below is asserted wherever
\(\mathscr I_p(0)\ne0\), equivalently wherever \(\mathcal Z_s\ne0\).
Comparing the two coefficients in (13) gives

\[
S_s\mathcal Z_s=\mathscr I_p(0),
\qquad
S_s\mathcal N_{p,s}=-\mathscr I'_p(0),
\tag{14}
\]

and therefore

\[
\boxed{
\frac{\mathcal N_{p,s}}{\mathcal Z_s}
=
-\left.\partial_t\log\mathscr I_p(t)\right|_{t=0}
\quad
\text{for every }
s\in\widetilde{\mathcal A}_{M,L}(p).
}
\tag{15}
\]

Here \((U,J)\in\mathfrak D_p^\cap\) and the common integral is nonzero, as
specified above.

The denominators \(\mathcal Z_s\) and scalars \(S_s\) need not be equal.
Equation (15) is projective equality of the branch first jets, which is the
actual synchronization requirement.

## Why covariance alone is insufficient

The projective reconstruction (13) cannot be replaced by bare covariance.
For a finite toy family let \(p,s\in\mathbb Z_2\), let the diagonal action be
\(g(p,s)=(p+g,s+g)\), and put

\[
Z_{p,s}(t)=1+k_{p-s}+t\mu.
\tag{16}
\]

This family is exactly covariant and has the same bare mark \(\mu\) on every
branch, but

\[
\left.\partial_t\log Z_{0,0}(t)\right|_0
=\frac{\mu}{1+k_0},
\qquad
\left.\partial_t\log Z_{0,1}(t)\right|_0
=\frac{\mu}{1+k_1}.
\tag{17}
\]

Taking \(k_0=0\) and \(k_1>0\) makes the two derivatives different even when
the activities are arbitrarily small. Equivariance and convergence do not
synchronize branch denominators. Equation (13) rules out exactly this
failure.

## The connected branch coefficient

For each \(s\), form the connected coefficient entirely inside its own gas:

\[
\begin{aligned}
\mathcal C_{p,s}^{+}(R)
={}&
\sum_{C_0\supset\widehat Q_{p,s}}
\sum_{n\ge0}\frac1{n!}
\sum_{\substack{C_1,\ldots,C_n\\
\operatorname{Hull}_s(C_0,\ldots,C_n)=R}}
\Phi_s^T(C_0^\bullet,C_1,\ldots,C_n)\\
&\qquad\qquad\times
W_{p,s}^{\rm post}(C_0)
\prod_{i=1}^nH_s(C_i).
\end{aligned}
\tag{18}
\]

The \(+\) records the convention for
\(-\partial_t\log\mathscr I_p|_0\). Repeated unmarked labels remain present,
and \(1/n!\) counts only the \(n\) unmarked occurrences.

Under Note 0024's separate ordinary KP ceiling and Note 0026's marked
hypotheses, (18) is absolutely convergent. Notes 0020--0021 and (15) then
give

\[
\sum_R\mathcal C_{p,s}^{+}(R)
=
\frac{\mathcal N_{p,s}}{\mathcal Z_s}
=
-\left.\partial_t\log\mathscr I_p(t)\right|_0 .
\tag{19}
\]

Only now define the normalized shifted coefficient

\[
\widehat{\mathcal C}_{p}^{+}(s,R)
=
\frac1{\widetilde n_p}\mathcal C_{p,s}^{+}(R).
\tag{20}
\]

Equations (5), (19), and (20) prove the synchronized representation

\[
\boxed{
-\left.\partial_t\log\mathscr I_p(t)\right|_0
=
\sum_{s\in\widetilde{\mathcal A}_{M,L}(p)}
\sum_R\widehat{\mathcal C}_{p}^{+}(s,R).
}
\tag{21}
\]

No gas contains two shift labels, no cross-shift incompatibility is
introduced, and no unmarked activity is averaged before taking a logarithm.

## Uniform norm and no lift entropy

Use the unnormalized \(W_{k,p}^s\) separately on every branch. The
transported branchwise application of Note 0013 Eq. (8), used in the
derivation preceding Note 0014 Eq. (10), gives the same input ceiling

\[
\sup_{\substack{p\\
s\in\widetilde{\mathcal A}_{M,L}(p)}}
\sum_{A\supset Q_{p,s}}
e^{(1-2\delta)\kappa d_{k,s}(A)}
\lVert W_{k,p}^s(A)\rVert
\le\mathcal B_d.
\tag{22}
\]

All constants and smallness conditions in Notes 0024--0026 are unchanged by
the finite relabelling. In particular, under the explicit doubled-amplitude
refinement and the independent condition
\(0<\varepsilon _1\le\varepsilon_{\rm KP}\), Note 0026 Eq. (41) holds on
every branch:

\[
\sup_{\substack{p\\
s\in\widetilde{\mathcal A}_{M,L}(p)}}
\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
|\mathcal C_{p,s}^{+}(R)|
\le
B_{\rm conn},
\tag{23}
\]

where

\[
B_{\rm conn}
=
e^{16\alpha}
C_{\rm sec}C_{\rm an}^{\rm geom}(\Delta)\mathcal B_d,
\qquad
C_{\rm sec}=4K_{\rm lift}\alpha _6^{-1}.
\tag{24}
\]

Normalize only at (20). Since there are exactly \(\widetilde n_p\) branches,

\[
\boxed{
\sup_p
\sum_{s\in\widetilde{\mathcal A}_{M,L}(p)}
\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
|\widehat{\mathcal C}_{p}^{+}(s,R)|
\le B_{\rm conn}.
}
\tag{25}
\]

Thus neither the original shift orbit nor the \(L^4\) distinct nested
branches cost an entropy factor. For a finite profile \(f\), linearity and
the triangle inequality give the right-hand side
\(B_{\rm conn}\sum_p|f_p|\).

Dividing the bare mark by \(\widetilde n_p\) and then dividing the completed
coefficient again would be a false double normalization.

## Coarse-lattice-preserving covariance

The group \(\Gamma_{N,L}\) from Note 0014 acts on the lift set modulo \(LM\):

\[
g(x)=P_gx+t_g,
\qquad
gs=P_gs+t_g\pmod{LM}.
\tag{26}
\]

Because \(LM\mid N\), this is well defined and

\[
g\widetilde{\mathcal A}_{M,L}(p)
=\widetilde{\mathcal A}_{M,L}(gp),
\qquad
\widetilde n_{gp}=\widetilde n_p.
\tag{27}
\]

The nested-stabilizer construction and the relabelling in the Section-2
proof give

\[
\mathcal C_{gp,gs}^{+}
(gR;g_*U,g_*J)
=
\mathcal C_{p,s}^{+}(R;U,J),
\qquad
d_{k+1,gs}(gR)=d_{k+1,s}(R).
\tag{28}
\]

The same statement holds for \(\widehat{\mathcal C}^{+}\). As in Note 0014,
the reflection step uses
\(\operatorname{Tr}(X^{-1})=\operatorname{Tr}(X)\) in \(SL(2,\mathbb C)\)
and is therefore asserted only for \(SU(2)\).

Equation (28) covers the subgroup preserving the next coarse lattice. It
does not cover fine unit translations that move that lattice.

## The source disk that already exists

For one real \(SU(2)\) plaquette,

\[
\Delta_p=\mathcal O_p-\mathcal O_p^{\rm bg},
\qquad
\operatorname{osc}(\Delta_p)
=\operatorname{osc}(\mathcal O_p)\le8.
\tag{29}
\]

Note 0007 therefore gives for the normalized selected-coordinate law

\[
\mathbb E e^{-t\Delta_p}\ne0
\qquad
\text{when}
\qquad
|t|<\frac{\log2}{4}.
\tag{30}
\]

The radius is independent of the regulator, scale, plaquette, and shift. For
a real finite profile \(f\), the corresponding radius is

\[
|t|<
\frac{\log2}{4\sum_p|f_p|},
\tag{31}
\]

with the usual \(f=0\) convention. Restoring the background contribution
multiplies the ratio by a nonzero exponential.

Equations (30)--(31) concern the exact scalar integral. They do **not**
construct holomorphic source-dependent polymer activities
\(H_{p,s,t}(C)\) for \(t\ne0\), nor do they prove KP smallness uniformly on
that disk. The full nonzero-\(t\) polymer-gas disk remains open and is not
needed for the first-jet theorem.

## Exact boundary

- Equations (13)--(15) prove the projective first-jet reconstruction for
  every nested shifted branch. Equations (21) and (25) close
  \((\mathrm H_{\rm sync})\) at \(t=0\), with no cross-shift gas and no orbit
  or lift entropy.
- The result assumes the full source hierarchy used by Notes 0012--0014 and
  0021--0026, \(LM\mid N\), the doubled-amplitude refinement, and the
  separate ordinary KP ceiling. The projective comparison also assumes the
  nonempty common branch domain \(\mathfrak D_p^\cap\) in (6a), including a
  common physical real source-free point. Compatibility with imported but
  unenumerated restrictions retains Note 0026's downward-monotonicity caveat.
- The source proves the unmarked one-cubulation formulas. The nested
  stabilizer average, shifted marked construction, projective equality, and
  differentiated connected bound are repository corollaries.
- The scalar source disk was already available from Notes 0007 and 0010.
  No nonzero-\(t\) polymer expansion or differentiated cluster theorem on
  that disk is proved here.
- The coefficient theorem is in independent \((U,J)\) variables. Notes
  0015--0019 give pointwise fixed-chart composition and conditional pieces
  of the derivative pullback, but the uniform scaled nonlinear \(U\)
  pullback and the premises of the all-layer \(J\) bridge remain open.
- No intrinsic/unrestricted raw-law comparison, unit-translation theorem,
  marginal projection, large-field estimate, RG iteration, continuum or
  infinite-volume construction, Osterwalder--Schrader axioms, infrared
  decay, or Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Select one representative of \(s\bmod M\) without specifying the output
  \(LM\)-cubulation and observe that the inherited root and output metric can
  depend on that choice.
- Remove the \(L^4\) lift multiplicity from (5), or divide both the bare mark
  and (20), and lose the normalized identity.
- Use only bare covariance and reproduce the counterexample (16)--(17).
- Change the cutoff, covariance, background, or chart with the source
  parameter and recover additional first-jet terms absent from (11).
- Choose branch domains with empty common intersection and observe that the
  fixed-\((U,J)\) projective comparison is not even defined.
- Mix two shift labels in one hard-core gas or average \(H_s\) before taking
  a logarithm and create denominators not present in (13).
- Forget the scalar \(S_s\), demand equality of branch denominators, and
  impose a stronger condition than projective synchronization requires.
- Add the minimizing-background contribution once per shift rather than once
  after the fluctuation average.
- Use (30) to claim source-dependent polymer activities or KP convergence at
  \(t\ne0\); physical zero-freeness alone does not imply either statement.
- Promote the independent-variable finite-regulator coefficient bound to a
  physical continuum observable or mass gap without the remaining gates.
