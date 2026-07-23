# Note 0028: a periodic endpoint bridge without tree digitization

Claim ID: YM-RG-028

Kind: finite-regulator quotient-geometry lemma and conditional
auxiliary-\(J\) pullback refinement

Evidence: E2 (elementary geometric proof; internally checked)

Novelty: none claimed

Primary anchors:

- T. Bałaban, [*Renormalization Group Approach to Lattice Gauge Field
  Theories I*](https://doi.org/10.1007/BF01215223), p. 257's
  side-length-normalized contained-tree metric;
- T. Bałaban, [*Propagators and Renormalization Transformations for Lattice
  Gauge Theories II*](https://doi.org/10.1007/BF01240221), especially
  Eqs. (2.45)--(2.54), for the multiscale contour metric and its triangle
  inequality.

The papers do not state the endpoint comparison below. It is a repository
quotient-geometry corollary using Note 0019's explicitly assumed ownership
map and nearest-neighbor estimate.

## Correction to the open geometry ledger

Note 0019 introduced a discrete-tree-lift hypothesis
\((\mathrm H_T)\): a shortest continuous contained tree was required to have
an equally short finest-lattice bond-tree realization, together with a
uniform proximity error \(\tau\). That is stronger than the physical
pullback needs.

The multiscale estimate uses only the distance between a root anchor and an
output-coordinate anchor. A continuous route bounds that quotient endpoint
distance even when the route itself lies off the fine lattice. One may then
take any finest-lattice geodesic between the endpoints and apply Note 0019's
bondwise \(\rho\) estimate to that geodesic. No digitization of the contained
tree is required.

## Fine-torus endpoint lemma

Let

\[
\mathbb T_\eta=(\eta\mathbb Z/P\mathbb Z)^d
\tag{1}
\]

with its periodic nearest-neighbor distance
\(\operatorname {dist}_\eta\), where \(P/\eta\in\mathbb N\). Let
\(z,z'\in\mathbb T_\eta\), and let
\(\gamma\) be any rectifiable continuous torus path joining them. If
\(\ell_2(\gamma)\) is its Euclidean length, then

\[
\boxed{
\operatorname {dist}_\eta(z,z')
\le
\frac{\sqrt d}{\eta}\ell_2(\gamma).
}
\tag{2}
\]

To prove (2), lift \(\gamma\) to \(\mathbb R^d\) beginning at one chosen lift
\(\widetilde z\). Its endpoint is a deck translate
\(\widetilde z'\) of \(z'\), and

\[
\operatorname {dist}_\eta(z,z')
\le
\eta^{-1}\lVert\widetilde z'-\widetilde z\rVert_1
\le
\frac{\sqrt d}{\eta}
\lVert\widetilde z'-\widetilde z\rVert_2
\le
\frac{\sqrt d}{\eta}\ell_2(\gamma).
\tag{3}
\]

The selected lift automatically handles winding and the periodic seam. The
path need not lie on fine bonds. If the source length is instead certified
as rectilinear \(\ell^1\) length, the factor \(\sqrt d\) in (2)--(3) can be
replaced by \(1\). This note retains the safe Euclidean comparison.

## Applying the lemma to a shifted polymer

Retain Note 0019's notation. The finest Propagators-II spacing is \(\eta\),
the current shifted localization mesh is \(s_*=b\eta\), and every
localization cube has side

\[
S=Mb\eta.
\tag{4}
\]

Assume \(P/S\in\mathbb N\), so these side-\(S\) cubes form a valid shifted
periodic cubulation. The condition \(P/\eta\in\mathbb N\) in (1) alone would
not imply this coarser divisibility.

Let \(Y\) be a connected union of those cubes and let
\(Q_{p,\sigma}\subset Y\) be its root cube. By the definition of
\(d_{k,\sigma}\), for every \(\varepsilon>0\) there is a connected
rectifiable tree \(T_\varepsilon\subset Y\), meeting every cube of \(Y\),
with

\[
\ell_2(T_\varepsilon)
\le
Mb\eta\bigl(d_{k,\sigma}(Y)+\varepsilon\bigr).
\tag{5}
\]

Writing (5) with an arbitrary \(\varepsilon\) also covers a convention in
which the shortest tree is specified only as an infimum.
The localization cubes here are their geometric closed realizations, as in
the contained-tree support. They must not be replaced by the half-open owned
cells used only to make \(\rho\) single valued.

Assume only Note 0019's support-halo hypothesis
\((\mathrm H_I)\). Thus an output coordinate \(x\in I(Y)\) and the root have
fine-site anchors \(z_x,z_p\) with

\[
\operatorname {dist}_\eta(z_x,Y)\le h,
\qquad
\operatorname {dist}_\eta(z_p,Q_{p,\sigma})\le h_q.
\tag{6}
\]

The fine torus is finite, so the halo minima are attained. Choose fine sites
\(u_p\in Q_{p,\sigma}\) and \(u_x\in Y\) with distances at most
\(h_q\) and \(h\), respectively, and view their fine-bond geodesics as
polygonal torus paths. Let \(Q_x\subset Y\) be a cube containing \(u_x\).
Choose points \(v_p\in T_\varepsilon\cap Q_{p,\sigma}\) and
\(v_x\in T_\varepsilon\cap Q_x\). The \(\ell^1\)-diameter of one side-\(S\)
cube is \(dS\). The route between the corresponding points in the abstract
finite tree has Euclidean length at most the total tree length; its torus
projection may self-identify without changing that bound. Concatenating the
two halo paths, two within-cube routes, and this projected tree route gives a
continuous torus path from \(z_p\) to \(z_x\).

Lift the entire concatenated path beginning at \(z_p\). The two halo pieces
contribute at most \((h_q+h)\eta\) to the lifted \(\ell^1\) displacement,
the two within-cube pieces contribute at most \(2dS\), and the displacement
between the lifted tree-contact points is at most
\(\sqrt d\,\ell_2(T_\varepsilon)\). The total lifted endpoint difference
lies in \(\eta\mathbb Z^d\), so its coordinate steps project to a fine-bond
torus path. Divide by \(\eta\) and let \(\varepsilon\downarrow0\):

\[
\boxed{
\operatorname {dist}_\eta(z_p,z_x)
\le
\sqrt d\,Mb\,d_{k,\sigma}(Y)
+2dMb+h+h_q.
}
\tag{7}
\]

No rounding constant is needed. The lifted endpoint displacement is already
a vector in \(\eta\mathbb Z^d\), and the inequality holds for every
\(\varepsilon>0\). Explicitly, if the right-hand side of (7) without
\(\varepsilon\) is \(R\), the construction gives
\(\operatorname {dist}_\eta(z_p,z_x)\le
R+\sqrt d\,Mb\varepsilon\) for every \(\varepsilon>0\), hence the claimed
limit. Integer-valuedness explains only the absence of a lattice-rounding
term; it is not needed to justify the limit.

The additive endpoint allowance cannot be deleted wholesale under only (6).
A tree may meet a cube at the point opposite the selected fine-site anchor.
For two adjacent one-dimensional closed cubes, Note 0013's source-safe bound
is \(d_k(Y)\le1\), while the two outer anchors are distance \(2S\) apart.
Under a degenerate infimum convention the shared endpoint even gives a
zero-length connected set meeting both closed cubes. Thus \(2dMb\) is a safe
rather than asserted-sharp allowance. A stronger source convention or anchor
rule could improve it, but is not assumed here.

## The forward multiscale comparison

Retain Note 0019's interface hypothesis \((\mathrm H_\rho)\). Its Eq. (13)
states that the ownership map is \(c_{\rm nn}\)-Lipschitz on fine endpoints,
where

\[
c_{\rm nn}=d(L+2)+1.
\tag{8}
\]

For the output-cell label \(y_x=\rho(z_x)\) and root label
\(q_p=\rho(z_p)\), combine (7) with that endpoint estimate:

\[
d_{\mathcal B}(q_p,y_x)
\le
c_{\rm nn}
\left[
\sqrt d\,Mb\,d_{k,\sigma}(Y)
+2dMb+h+h_q
\right].
\tag{9}
\]

If \(I(Y)=\varnothing\), set
\(D_{\mathcal B}(q_p,Y)=E_J(Y)=0\); then the direct-\(J\) derivative density
vanishes and every bound below is trivial. Otherwise, taking the supremum
over \(x\in I(Y)\) proves

\[
\boxed{
D_{\mathcal B}(q_p,Y)
\le
C_{\rm end}^{(1)}d_{k,\sigma}(Y)+C_{\rm end}^{(0)},
}
\tag{10}
\]

with

\[
\boxed{
C_{\rm end}^{(1)}
=c_{\rm nn}\sqrt d\,Mb,
\qquad
C_{\rm end}^{(0)}
=c_{\rm nn}(2dMb+h+h_q).
}
\tag{11}
\]

Equations (10)--(11) replace Note 0019 Eqs. (19)--(20) without
\((\mathrm H_T)\) and without \(\tau\). The fine geodesic used to invoke the
\(\rho\) estimate need not remain in \(Y\); Note 0019 Eq. (13) is a
full-torus endpoint inequality.

## Direct-\(J\) support specialization

For the first-stage shifted activities of Notes 0012--0014, define

\[
I_J(Y)
=
\{b\in E_k^+:\ D_{J(b)}W_{k,p}^{\sigma}(Y)
   \text{ is not identically zero}\}.
\tag{12}
\]

Here \(E_k^+\) is one globally chosen orientation of every unoriented
\(k\)-scale bond; \(D_{J(b)}\) includes its
\(\mathfrak {su}(2)_{\mathbb C}\) components.
Note 0012's repository locality conclusion immediately after its Eq. (8),
in the RG-II decoupled-variable sense, gives

\[
I_J(Y)
\subset
\{b\in E_k^+:\ |b|\subset\operatorname {int}Y\}.
\tag{13}
\]

Here \(|b|\subset\operatorname {int}Y\) means that the full oriented geometric
bond is contained in the interior, not merely that one endpoint is assigned
to \(Y\). Fix one global orientation of every independent bond and anchor
\(b\) at its initial site \(z_b\). Equation (13) gives \(z_b\in Y\).
The half-open rule changes only \(\rho(z_b)\)'s cell ownership and does not
change this geometric membership. Anchor the plaquette source at its base
site, which lies in the strict interior of \(Q_{p,\sigma}\). With

\[
y_b=\rho(z_b),
\qquad
q_p=\rho(z_p),
\tag{14}
\]

the support-halo hypothesis holds for this direct-\(J\) derivative with

\[
\boxed{h=h_q=0.}
\tag{15}
\]

This specialization is only for the already localized first-stage
independent-variable activity. It does not establish the corresponding
external-\(J\) support theorem for every completed Section-2 connected
coefficient. Subsequent Note 0029 audits the printed final-activity locality
and the marked literal-union map and proves that later support theorem
separately.
RG I condition (iv) creates no additional direct-\(J\) halo here: it uses
the derived \(J_n(U)\), while the affine independent-\(J\) variation changes
only condition (iii), as isolated in Note 0017.

## Refined conditional all-layer \(J\) bound

Retain all hypotheses of Note 0019's conditional all-layer
auxiliary-\(J\) theorem except \((\mathrm H_T)\): in particular
\((\mathrm H_J)\), \((\mathrm H_\rho)\), the source-kernel separation,
\(b\le b_*\), the appropriate support halos, and common
\(C_\chi,c_1(\alpha_\gamma),\overline E_J,\Delta_J^{-1}\), and
\(\mathcal B_d\). Put

\[
C_*
=c_{\rm nn}\sqrt d\,Mb_*,
\qquad
C_{0,*}
=c_{\rm nn}(2dMb_*+h+h_q),
\tag{16}
\]

and choose \(a_*\ge0\) with

\[
\boxed{
a_*+\gamma c_{\rm nn}\sqrt d\,Mb_*\le a.
}
\tag{17}
\]

Then Note 0019's proof of Eq. (26), with (10) in place of its Eq. (19),
gives

\[
\boxed{
\begin{aligned}
&\sup_p\sum_{\sigma,Y}e^{a_*d_{k,\sigma}(Y)}
\sup_{\mathfrak C_Y^\sigma}\left[
\sum_{j',y'}\mu(j',y')e^{\gamma d_{\mathcal B}(q_p,y')}
|\mathcal L_{p,\sigma,Y}^J(j',y')|\right]\\
&\quad\le
\frac{C_\chi c_1(\alpha_\gamma)\overline E_J
e^{\gamma C_{0,*}}\mathcal B_d}{\Delta_J}.
\end{aligned}
}
\tag{18}
\]

For the direct-\(J\) specialization (12)--(15), use
\(C_{0,*}=2dc_{\rm nn}Mb_*\).

Equation (18) is still conditional. It removes only the artificial
tree-digitization and support-halo premises for the first-stage direct-\(J\)
family. It does not prove \((\mathrm H_\rho)\), the mesh bound, common chart
constants, or the corresponding derivative theorem for the completed
YM-RG-027 coefficients. Subsequent Note 0029 supplies zero support halos for
those completed coefficients on the admitted integer-wall cubulations, but
still no common Cauchy tube or derivative norm.

## Exact boundary

- The quotient endpoint lemma (2) and polymer comparison (7) are elementary
  finite geometry. No source theorem about a discrete tree lift is used.
- The factor \(\sqrt d\) is the safe conversion from Euclidean tree length
  to coordinate displacement. Replacing it by \(1\) requires a separately
  certified \(\ell^1\) or rectilinear source convention.
- The result removes \((\mathrm H_T)\) and \(\tau\), but it retains every
  interface and admissibility clause in \((\mathrm H_\rho)\). Those clauses
  are not inferred from the displayed Propagators-II definitions.
- The direct-\(J\) support conclusion uses only the first-stage
  independent-variable locality of Notes 0012--0014. Completed Section-2
  coefficients require a separate external-coordinate support audit;
  subsequent Note 0029 supplies it through the literal-union connected map.
- The slope remains proportional to \(b\). If the mesh ratio is unbounded,
  no regulator-uniform forward comparison follows.
- The common strict-\(J\) representative, source-kernel, conversion, Cauchy,
  and activity constants in (18) remain hypotheses.
- No concrete RG-scaled nonlinear \(U\) collar, physical \(U\)-summand,
  physical connected YM-RG-027 coefficient bound, nonzero-source polymer
  disk, raw-law comparison, large-field estimate, RG iteration, continuum
  construction, infrared decay, or Yang--Mills mass gap follows.
- No independent human review has been performed.

## Falsification checklist

- Apply \(\rho\) directly to a continuous boundary-riding tree point and
  identify the category error; \(\rho\) is used only on fine endpoints of a
  separate fine geodesic.
- Work at a periodic seam without lifting the continuous endpoint route and
  lose control of its deck translation.
- Use Euclidean tree length with coefficient \(1\) and take a diagonal route
  whose \(\ell^1/\ell^2\) ratio is \(\sqrt d\). Concretely in \(d=2\), take
  closed unit squares
  \(D_i=[i,i+1]^2\) and connectors
  \(C_i=[i,i+1]\times[i+1,i+2]\). Their face-connected union contains a
  diagonal route of Euclidean length \(\sqrt2\,n\) meeting every cube, while
  the endpoint \(\ell^1\) displacement is \(2n\); for large \(n\), no fixed
  endpoint allowance repairs coefficient \(1\).
- Assume a shortest tree is attained; instead use the
  \(\varepsilon\)-minimizing formulation (5).
- Replace the closed localization cubes by half-open \(\rho\)-ownership cells
  and create a false nonattainment at a shared wall.
- Delete every additive endpoint allowance and use two adjacent cubes with
  opposite outer anchors; Note 0013 gives \(d_k(Y)\le1\), while their
  separation is \(2Mb\).
- Let \(I(Y)\) contain an arbitrarily distant coordinate and recover the
  original support obstruction; (13) is essential to the \(h=0\)
  specialization.
- Let \(b\to\infty\) while a localization edge remains in the finest
  Propagators-II layer and observe that the slope in (11) diverges.
- Claim that removing \((\mathrm H_T)\) proves \((\mathrm H_\rho)\), the
  common chart constants, a completed-coefficient Cauchy tube, or the
  nonlinear \(U\) pullback.
