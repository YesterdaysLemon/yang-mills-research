# Note 0015: fixed-patch physical composition of one rooted mark

Claim ID: YM-RG-015

Kind: finite-regulator analytic-composition lemma

Evidence: E2 (conditional fixed-patch composition; internally checked)

Novelty: none claimed

## Why the pullback is split into two questions

Notes 0012--0014 construct marked activities in RG II's independent
\((U,J,B)\) variables. The physical RG integrand evaluates the first two
variables on background fields determined by a coarse field. That evaluation
has two logically different consequences:

1. composition on one common analytic patch, including the exact chain rule
   and preservation of the existing zeroth-order activity norm; and
2. a quantitative quasilocal estimate for derivatives with respect to the
   coarse field.

The first is finite-dimensional and is proved here. The second requires a
metric-and-norm crosswalk for the component estimates in the variational
paper's Proposition 9 Eq. (190), quantitative control of the exact auxiliary
\(J\)-map defined in RG I Eq. (1.8), full coordinate tubes for Cauchy
estimates, and new decay slack. It remains open.

This distinction prevents the word *pullback* from silently turning an
analytic composition into a summable coarse-field locality theorem.

## Fixed charts and hypotheses

Retain every hypothesis of Notes 0012--0014. In particular, work at one finite
four-dimensional \(SU(2)\) regulator and RG step, take

\[
M=L^m,\qquad m\ge2,
\]

use the RG-admitted \(L\)-spaced shift family, and retain the transported
RG-II Eq. (1.34) domains and the strict margins used in Note 0013.

Fix a coarse field \(W_0\) in one Proposition 9 gauge-fixed background patch.
Write its local relative-log coordinate as

\[
\omega=\frac1i\log(WW_0^{-1}),
\qquad
W(\omega)=e^{i\omega}W_0,
\tag{1}
\]

bond by bond in the selected local branch. Choose an open complex subdomain
\(\Omega_{\mathbb C}\) whose closure is compact in a larger Proposition 9
chart on which the background lift is holomorphic, and put
\(\Omega_{\mathbb R}=\Omega_{\mathbb C}\cap\{\omega:\omega\text{ is real}\}\).

To avoid the three incompatible uses of the letter \(B\) in the source
chain, this note uses:

- \(\omega\) for the coarse relative-log coordinate, called \(B\) in the
  variational paper;
- \(\varphi\) for RG I/II's independent fluctuation field, called \(B\) in
  Notes 0010--0014; and
- \(\mathcal W\) for a marked activity after physical evaluation, reserving
  \(\widehat W\) for the independent-variable activity and \(W\) for the
  coarse group field.

Define the physical background lift

\[
\iota(\omega)
=\bigl(\mathcal U(\omega),\mathcal J(\omega)\bigr)
=\bigl(U_{k+1}(W(\omega)),J_{k+1}(W(\omega))\bigr).
\tag{2}
\]

RG I Eqs. (1.8) and (1.15)--(1.16) identify the second component exactly:

\[
\mathcal J(\omega)
=\mathscr J_{\xi_{k+1}}(\mathcal U(\omega)),
\qquad
\mathscr J_\xi(U)
=D_U^{\xi *}\xi^{-2}\pi\operatorname{im}(dU).
\tag{2a}
\]

RG I Eq. (1.10) specifies the adjoint transformation convention for the
\((U,J)\) pair; substituting a gauge-transformed link field into the
finite-stencil formula (2a) gives covariance in that convention. The theorem
below is conditional on the following fixed-patch facts.

1. The chosen representative of the minimizing \(\mathcal U\)-branch is
   holomorphic on a neighborhood of
   \(\overline{\Omega_{\mathbb C}}\), as supplied by Proposition 9. Equation
   (2a), a finite-stencil holomorphic expression on the selected link chart,
   then makes the pair in (2) jointly holomorphic. No separate
   \(J\)-holomorphy hypothesis is needed.
2. For every plaquette \(p\), admitted shift \(\sigma\), and root-connected
   polymer \(Y\), choose a named precompact complex fluctuation domain
   \(\mathfrak F_Y^\sigma\) such that the closure of
   \[
   \left\{
   (\mathcal U(\omega),\mathcal J(\omega),\varphi):
   \omega\in\overline{\Omega_{\mathbb C}},\quad
   \varphi\in\mathfrak F_Y^\sigma
   \right\}
   \]
   is contained in the transported open Eq. (1.34) domain on \(Y\). The
   finite regulator makes this a finite compact-containment requirement, not
   a volume-uniform radius theorem.
3. On \(\Omega_{\mathbb R}\), the minimizing \(\mathcal U\)-branch is
   equivariant between the transported Proposition 9 charts under the
   subgroup \(\Gamma_{N,L}\) from Note 0014. Equation (2a) and RG I Eq. (1.10)
   then give equivariance of the pair.

These hypotheses name exactly the chart and domain needed for composition.
They do not assert a global background atlas.

For later suprema, name the fixed product domain

\[
\mathfrak C_Y^\sigma
=\Omega_{\mathbb C}\times\mathfrak F_Y^\sigma.
\tag{3}
\]

Hypothesis 2 says that the full composed closure, including the fluctuation
domain, maps into the transported Eq. (1.34) domain on \(Y\).

## The physically evaluated activities

Let

\[
\widehat W_{k,p}(\sigma,Y;U,J,\varphi)
\]

be the normalized shifted activity of Note 0014. Define

\[
\mathcal W_{k,p}(\sigma,Y;\omega,\varphi)
=\widehat W_{k,p}\!\left(
\sigma,Y;
\mathcal U(\omega),\mathcal J(\omega),\varphi
\right).
\tag{4}
\]

Evaluation of Note 0014 Eq. (8) gives the exact identity

\[
\boxed{
\Delta_p\!\left(
\mathcal U(\omega),\mathcal J(\omega),\varphi
\right)
=
\sum_{\sigma\in\mathcal A_{M,L}(p)}
\sum_{Y\supset Q_{p,\sigma}}
\mathcal W_{k,p}(\sigma,Y;\omega,\varphi).
}
\tag{5}
\]

At the fixed regulator both sums are finite. Equation (5) is an evaluated
identity on the selected RG-coordinate branch, not a connected expectation.

## Analyticity, fluctuation locality, and centering

For every fixed \((p,\sigma,Y)\), the activity in (4) is jointly holomorphic
in \((\omega,\varphi)\) on the fixed composed domain. It retains strict
dependence on the fluctuation only through \(\varphi|_{\operatorname{int}Y}\):
if
\(\varphi|_{\operatorname{int}Y}=\varphi'|_{\operatorname{int}Y}\), then

\[
\mathcal W_{k,p}(\sigma,Y;\omega,\varphi)
=
\mathcal W_{k,p}(\sigma,Y;\omega,\varphi').
\tag{6}
\]

There is no analogous claim that it depends only on \(\omega|_Y\). The
minimizing background may depend on coarse data arbitrarily far from \(Y\).

Note 0012 proves the independent-variable centering identity, and Note 0014's
normalization preserves it:

\[
\widehat W_{k,p}(\sigma,Y;U,J,0)=0
\]

for every admitted \((U,J)\). Hence

\[
\mathcal W_{k,p}(\sigma,Y;\omega,0)=0
\tag{7}
\]

identically in \(\omega\). Every pure coarse-coordinate jet therefore
vanishes at zero fluctuation:

\[
D_\omega^r
\mathcal W_{k,p}(\sigma,Y;\omega,0)=0,
\qquad r\ge0.
\tag{8}
\]

This pure-jet statement concerns the centered activities and, by (5), the
centered mark \(\Delta_p\); it does not concern the separate fixed-background
plaquette observable. Mixed \(\omega\)-\(\varphi\) derivatives and the first
\(\varphi\)-derivative at zero fluctuation need not vanish.

## Exact fixed-chart chain rule

All derivatives below are coordinate Frechet derivatives in the chosen
finite-dimensional charts. For a coarse tangent \(h\) and fluctuation tangent
\(\psi\), the first derivative is

\[
\begin{aligned}
D\mathcal W_{k,p}[h,\psi]
={}&D_U\widehat W_{k,p}
   \bigl[D\mathcal U(\omega)h\bigr]
 +D_J\widehat W_{k,p}
   \bigl[D\mathcal J(\omega)h\bigr]\\
&+D_\varphi\widehat W_{k,p}[\psi],
\end{aligned}
\tag{9}
\]

where every derivative of \(\widehat W_{k,p}\) on the right is evaluated at
\((\sigma,Y;\mathcal U(\omega),\mathcal J(\omega),\varphi)\).
Neither the \(U\)-term nor the \(J\)-term may be dropped.
Using (2a), its coarse derivative is not independent:

\[
D\mathcal J(\omega)
=D\mathscr J_{\xi_{k+1}}(\mathcal U(\omega))
 \,D\mathcal U(\omega).
\tag{9a}
\]

Note 0016 records RG I Eq. (3.11)'s exact local formula for the first factor
and the resulting conditional Cauchy bounds for the activity derivatives.

Put \(D\iota h=(D\mathcal U h,D\mathcal J h)\). The second derivative has
the compact exact form

\[
\begin{aligned}
D^2\mathcal W_{k,p}
[(h_1,\psi_1),(h_2,\psi_2)]
={}&D^2\widehat W_{k,p}
[(D\iota h_1,\psi_1),(D\iota h_2,\psi_2)]\\
&+D\widehat W_{k,p}[(D^2\iota[h_1,h_2],0)].
\end{aligned}
\tag{10}
\]

Higher derivatives are the ordinary finite-dimensional Faa di Bruno
polynomials in derivatives of \(\widehat W_{k,p}\) and \(\iota\). Equations
(9)--(10) are identities only. This note supplies no regulator-uniform bounds
for any derivative appearing in them.

## The inherited zeroth-order weighted norm

Retain Note 0014's notation

\[
a=(1-2\delta)\kappa,
\qquad
q_d=\frac{64e^a}{e^{\kappa_1}-1},
\qquad
\mathcal B_d=
\frac{e^aC_{\rm mark}e^{16\kappa_1}\varepsilon_1}{1-q_d},
\tag{11}
\]

with \(0<\delta<1/2\), the source-safe consequence
\(\kappa_1-1\ge(1-\delta)\kappa\), and the repository margin
\(\delta\kappa>\log64\).

The composed domain is a subset of the transported Eq. (1.34) domain used in
Note 0014's supremum. Therefore mere evaluation gives

\[
\begin{aligned}
&\sup_p
\sum_{\sigma\in\mathcal A_{M,L}(p)}
\sum_{Y\supset Q_{p,\sigma}}
e^{a d_{k,\sigma}(Y)}
\sup_{(\omega,\varphi)\in\mathfrak C_Y^\sigma}
|\mathcal W_{k,p}(\sigma,Y;\omega,\varphi)|\\
&\qquad\le \mathcal B_d.
\end{aligned}
\tag{12}
\]

For a finite profile, the safe linear bound remains
\(\mathcal B_d\sum_p|f_p|\). Equation (12) needs no derivative estimate from
Eq. (190); it is the restriction of an already proved supremum. It controls
activity size and polymer geometry, not response to changing the coarse field.

## Transported real-chart covariance

Let \(g\in\Gamma_{N,L}\), and use the transported real relative-log chart at
\(g_*W_0\). By hypothesis,

\[
\iota_{g_*W_0}(g_*\omega)=g_*\iota_{W_0}(\omega).
\tag{13}
\]

Let \(\omega\in\Omega_{\mathbb R}\) and \(\varphi\) be admitted and real, with
both transported representatives remaining in their named charts. Combining
(13) with Note 0014 Eq. (15) gives

\[
\mathcal W_{k,gp}
(g\sigma,gY;g_*\omega,g_*\varphi)
=
\mathcal W_{k,p}
(\sigma,Y;\omega,\varphi).
\tag{14}
\]

This is covariance between equivariantly transported real charts. It neither
glues unrelated chart choices nor extends the symmetry to unit translations
that move the next coarse lattice. The reflection step retains Note 0014's
\(SU(2)\)/\(SL(2,\mathbb C)\) restriction.

## Proof

Equation (5) is Note 0014's finite identity evaluated at (2). Joint
holomorphy of (4) is closure of finite-dimensional holomorphic maps under
composition. Independent-variable locality of \(\widehat W\) immediately
gives (6) with \(\omega\) held fixed, but says nothing about the support of
the composed background. The all-\((U,J)\) centering identity gives (7), and
differentiating the identically zero holomorphic function gives (8).

The coordinate chain rule gives (9), a second application gives (10), and the
higher-order assertion is the standard Faa di Bruno formula. Since the
physical image is contained in the domain of Note 0014's supremum, each term
in (12) is bounded by the corresponding independent-variable term; summing
proves (12). Finally, substitution of the equivariant lift (13) into Note
0014's activity transport proves (14). \(\square\)

## What Proposition 9 Eq. (190) still has to do

[Note 0004](0004-fixed-background-source-jet.md) transcribes the five rows of
Eq. (190). They control components of the first derivative of the minimizing
background with respect to a coarse relative-log coordinate, together with
several derived spatial/covariant derivatives. This is the correct input for
\(D\mathcal U(\omega)\) in (9), but it is not a bound on (4).

To turn (9) into a summable coarse-field derivative norm, a later lemma must
also provide all of the following:

1. quantitative coordinate, differential-of-exponential, gauge-restoration,
   and RG I Eq. (3.11) local-remainder factors relating Eq. (190)'s component
   kernel to both terms in (9);
2. a volume- and scale-uniform nonlinear \(U\) coordinate tube in a coherent
   RG-scaled regularity norm; Note 0017 supplies the separate direct-\(J\)
   sup-norm collar, while Note 0018 proves that the naive raw and
   \(U_A=e^{i\xi A}U\) bond-sup \(U\) radii collapse and isolates the scaled
   replacement hypotheses;
3. a cross-layer network comparison between Eq. (190)'s multiscale contour
   distance and the \(d_{k,\sigma}\) polymer metric; Note 0017 proves only the
   matched homogeneous-layer identity, disproves a uniform reverse bound,
   and leaves the forward interface bound needed here unresolved;
4. the \(U\)-summand pullback in the compatible norm; Note 0017 supplies the
   dual source convolution and homogeneous-layer auxiliary-\(J\) summand; and
5. enough exponential slack to pay that convolution and the animal
   entropy without consuming later RG-II decay requirements.

Until those steps are proved, (4) must not be called a quasilocal coarse-field
activity.

## Exact boundary

- This is a conditional theorem on one finite regulator, one common
  relatively compact background chart, the exact RG-I physical \(J\)-map,
  and a composed image compactly contained in the transported Eq. (1.34)
  domains.
- The only quantitative estimate asserted here is the inherited zeroth-order
  value norm (12). No derivative norm, uniform complex radius, or
  regulator-independent background locality constant is obtained.
- Locality is strict only in the independent fluctuation \(\varphi\). No
  support or exponential-tail statement in \(\omega\) is proved.
- Proposition 9 Eq. (190) applies directly only to the minimizing-background
  component described in the primary paper. RG I Eq. (3.11) reduces the
  auxiliary \(J\)-derivative to that component plus a local remainder, but the
  quantitative chart factors, uniform activity tubes, metric convolution,
  and connected expectation remain unproved.
- The shift label remains. Nothing here reconciles the family with one fixed
  Section-2 cluster partition.
- No intrinsic/coarea/unrestricted-raw density comparison, cutoff-conditioned
  connected sum, marginal projection, large-field estimate, RG iteration,
  continuum construction, infrared decay, or mass gap follows.

## Falsification checks

- Drop the \(D_J\widehat W[D\mathcal J h]\) term from (9) and reject the
  resulting chain rule whenever the activity depends on \(J\).
- Let the physical image approach an Eq. (1.34) boundary and identify the
  missing common-domain/Cauchy margin.
- Change \(\omega\) outside \(Y\) and reject any use of (6) as coarse-field
  strict locality.
- Differentiate (12) with respect to \(\omega\) and identify the unjustified
  exchange of a value supremum for a derivative bound.
- Replace the transported real charts in (14) by unrelated gauge slices and
  identify the missing overlap theorem.
- Insert the shift-indexed family directly into one fixed Section-2 cluster
  sum and identify the still-missing compatibility theorem.
