# Note 0019: a conditional forward multiscale cell-map bridge

Claim ID: YM-RG-019

Kind: conditional multiscale geometry and weighted pullback lemma

Evidence: E2 (elementary proof under explicit cell, interface, mesh,
discrete-tree-lift, and support premises)

Novelty: none claimed

Primary anchors: [*Propagators and Renormalization Transformations for
Lattice Gauge Theories
II*](https://doi.org/10.1007/BF01240221), especially Eqs.
(2.45)--(2.54), and [RG I](https://doi.org/10.1007/BF01215223) for the
contained-tree definition used in Note 0013.

## Correction and target

Note 0017 proves on one matched homogeneous layer that

\[
D_{\mathcal B}(q,Y)
\le M d_{k,\sigma}(Y)+C_{\rm end}.
\tag{1}
\]

It also proves that a regulator-uniform reverse inequality
\(d_{k,\sigma}\lesssim d_{\mathcal B}\) fails across arbitrarily separated
layers. That reverse failure does not obstruct the forward direction in (1).

A source recheck corrects an earlier description of Propagators II
Eq. (2.57). It lower-bounds actual travel between distinct layer surfaces for
the Eq. (2.58) exponential summation. It is not an additive \(RM\) interface
toll in the definition of \(d_{\mathcal B}\). The forward problem can instead
be reduced to a nearest-neighbor estimate for an explicit multiscale cell
map.

The paper supplies the multiscale metric and its triangle inequality. It does
not print all the cell-ownership, interface-collar, mesh-matching,
discrete-tree-lift, and support premises below. This note therefore states
them rather than silently treating them as source theorems.

Subsequent Note 0028 proves that the endpoint consequence does not require
the discrete-tree-lift premise: a covering-space argument applied to an
\(\varepsilon\)-minimizing continuous tree removes
\((\mathrm H_T)\) and \(\tau\), at the safe price of a \(\sqrt d\) factor in
the slope. The original conditional route is retained below for audit.

## Tagged cells and the ownership map

Fix dimension \(d\), odd block ratio \(L\ge3\), finest Propagators-II
spacing \(\eta\), and

\[
s_j=L^j\eta,
\qquad
\mathbb T^{(j)}=s_j\mathbb Z^d/P\mathbb Z^d.
\tag{2}
\]

Keep the paper's physical Eq. (2.45) set and introduce a tagged cover

\[
\widetilde{\mathcal B}=\bigsqcup_{j=0}^K\Lambda_j,
\qquad
\pi:\widetilde{\mathcal B}\longrightarrow
\mathcal B=\bigcup_{j=0}^K\Lambda_j,
\qquad \pi(j,y)=y.
\tag{3}
\]

The paper's \(d_{\mathcal B}\) is defined on the physical union. Pull it back
to the tagged cover by

\[
d_{\widetilde{\mathcal B}}(\widetilde y,\widetilde y')
:=d_{\mathcal B}(\pi\widetilde y,\pi\widetilde y').
\tag{3a}
\]

This is a pseudometric if two tags have the same physical representative and
inherits Eq. (2.54)'s triangle inequality. For economy, every later
\(d_{\mathcal B}\) between tagged labels means the pullback (3a). Every
source or target cell label below is likewise understood with its selected
layer tag.

For sites of the finest periodic lattice, write

\[
z\sim_\eta z'
\quad\Longleftrightarrow\quad
z'-z=\pm\eta e_\mu\pmod P
\tag{4}
\]

for one coordinate direction. Let \(\operatorname {dist}_\eta\) be the
minimum number of such bonds.

Use the following deterministic ownership convention. Fix a periodic
fundamental domain and, in every coordinate, include the lower face and
exclude the upper face of each cell. At the periodic seam this rule is
applied after the unique compatible lift to the chosen domain.

1. Off interfaces, \(r(z)\) is the unique open-layer index containing \(z\).
2. A site on \(\Sigma_{j+1}\) belongs to the inner layer \(j+1\), matching
   the convention used in Propagators II.
3. Coincident interfaces use one fixed layer precedence rule. Corners and
   the periodic seam use the coordinatewise half-open cell rule above, not
   an arbitrary ordering of all boundary candidates.

For \(j=r(z)\), use the block identified in the paper's Eq. (2.53) and write

\[
\mathcal C_j(z)
=\{y\in\Lambda_j:z\in\Delta_j(y)\},
\qquad
\Delta_j(y)=B^j(y).
\tag{5}
\]

Let \(\operatorname {sel}_j(z)\) be the unique candidate selected by the
coordinatewise periodic half-open convention and put

\[
\rho(z)=\bigl(r(z),\operatorname {sel}_{r(z)}(z)\bigr)
\in\widetilde{\mathcal B}.
\tag{6}
\]

Equivalently, the owned half-open cells

\[
\widehat\Delta(j,y)=\{z:r(z)=j,\ \rho(z)=(j,y)\},
\qquad y\in\Lambda_j,
\tag{7}
\]

form a disjoint partition of the fine torus. The same coordinatewise
selector is used for every occurrence of \(\rho\), including source and
target anchors below. Equation (2.53) identifies \(\Delta(y)=B^j(y)\); it
does not itself define this ownership map. A tagged label used as a contour
endpoint always means its physical projection under \(\pi\).

## The interface hypotheses

The numerical bound below assumes the following cubical hypothesis
\((\mathrm H_\rho)\).

1. **Aligned hierarchy.** The block ratio is an odd integer \(L\ge3\). The
   grids have a common origin,
   \(\mathbb T^{(j+1)}\subset\mathbb T^{(j)}\), every active grid fits the
   periodic torus, and every interface is a union of compatible coordinate
   faces. Thus \(P/s_j\in\mathbb N\) for every active \(j\). Merely requiring
   one divisibility relation at the finest scale is not substituted for
   these conditions.
2. **Half-open cell geometry.** A layer-\(j\) selected cell has
   \(\ell^1\)-diameter at most \(d s_j\). Under the coordinatewise selector,
   if \(z\sim_\eta z'\) and \(r(z)=r(z')=j\), the two owned cells are equal
   or joined by an admissible layer-\(j\) face bond of length \(s_j\). An
   arbitrary corner tie-break that can select diagonally separated cells is
   excluded.
3. **No skipped interface.** Fine neighbors satisfy
   \[
   |r(z)-r(z')|\le1.
   \tag{8}
   \]
   This is checked in the original scale indexing. Empty or coincident labels
   are not compressed in a way that hides a jump with scale ratio larger than
   \(L\). A larger active-scale jump is not admitted in this note; a variant
   would have to replace \(L\) in (9)--(12) by the actual interface ratio.
4. **Source-admissible outer collar.** If \(z\sim_\eta z'\) crosses
   \(\Sigma_{j+1}\), with \(z\) in the outer layer \(j\), and
   \(y=\rho(z),y'=\rho(z')\), there are an outer-collar point \(a\), a
   common-grid point
   \(w\in\Sigma_{j+1}\cap\mathbb T^{(j+1)}\), with
   \(a\in\mathbb T^{(j)}\), and
   \(v=w+s_{j+1}n_{\rm in}\in\mathbb T^{(j+1)}\) on the inner side such that
   admissible paths obey
   \[
   \begin{aligned}
   \operatorname {len}_j(y\leadsto a)&\le d s_j,\\
   \operatorname {len}_j(a\leadsto w)&\le d s_{j+1},\\
   \operatorname {len}_{j+1}(w\leadsto v)&=s_{j+1},\\
   \operatorname {len}_{j+1}(v\leadsto y')&\le d s_{j+1}.
   \end{aligned}
   \tag{9}
   \]
   The second path has open interior in the outer collar and meets the
   inner-owned surface only at its endpoint \(w\). At \(w\), the mesh is
   switched without geometric cost; the first layer-\(j+1\) coarse bond
   \(w\to v\) has open interior in the inner layer and costs one unit. No
   fine tangential path is run on the inner-owned surface.
5. **Admissibility premise.** The four pieces in (9), including the mesh
   switch at \(w\) and the crossing coarse bond, are admissible in the sense
   of Propagators II Eq. (2.46). This is assumed source compatibility, not a
   consequence claimed from Eq. (2.47).
6. **Periodic version.** The same statements hold at the torus seam after a
   local lift to the periodic cover.

These premises are stronger than the paper's displayed definitions. In
particular, Eq. (2.47) decomposes an already admissible contour; it is not by
itself a proof of (8)--(9), or of the source admissibility in condition 5,
for every arbitrary fine-neighbor pair.

## Nearest-neighbor Lipschitz bound

Propagators II Eq. (2.46) charges a length-\(s_j\) layer-\(j\) bond one unit.
If two fine neighbors have the same layer, condition 2 gives

\[
d_{\mathcal B}(\rho(z),\rho(z'))\le1.
\tag{10}
\]

At a \(j\leftrightarrow j+1\) interface, (9) gives an admissible contour with
four costs

\[
d,
\qquad dL,
\qquad 1,
\qquad d.
\tag{11}
\]

Therefore, under \((\mathrm H_\rho)\),

\[
\boxed{
\sup_{z\sim_\eta z'}
d_{\mathcal B}(\rho(z),\rho(z'))
\le c_{\rm nn},
\qquad
c_{\rm nn}=d(L+2)+1.
}
\tag{12}
\]

For a fine path \(z_0,\ldots,z_n\), the triangle inequality in Propagators II
Eq. (2.54) now proves

\[
\boxed{
d_{\mathcal B}(\rho(z_0),\rho(z_n))
\le c_{\rm nn}n.
}
\tag{13}
\]

Thus \(\rho\) is a \(c_{\rm nn}\)-Lipschitz map from the finest graph to the
multiscale metric. The value in (12) is repository cubical bookkeeping, not a
constant printed by Ba\l aban.

## Mesh matching and shifted-polymer support

Let the unit spacing of Note 0014's current shifted localization lattice be

\[
s_*=b\eta,
\qquad b\in\mathbb N.
\tag{14}
\]

Each shifted cube then has side \(M b\eta\). RG I p. 257 defines
\(d_{k,\sigma}\) using the length of a shortest *continuous* tree contained
in the polymer and meeting every localization cube. That definition does not
make the shortest tree a finest-lattice bond tree of exactly the same length.

The forward comparison therefore needs a separate discrete-lift hypothesis
\((\mathrm H_T)\). There is one common \(\tau\ge0\), measured in finest
bonds, such that every admitted \((\sigma,Y)\) has a connected fine-bond tree
\(\widetilde T_Y\) satisfying

\[
|\widetilde T_Y|_\eta
\le M b\,d_{k,\sigma}(Y),
\tag{15}
\]

and, for every shifted cube \(Q\subset Y\) and fine site \(u\) represented
in \(Q\),

\[
\operatorname {dist}_\eta(u,\widetilde T_Y)
\le dMb+\tau.
\tag{15a}
\]

The constant \(\tau\) absorbs translation, coset, periodic-seam, and
open/closed-boundary conventions. Both parts of \((\mathrm H_T)\) are
premises. Equation (15) assumes no length increase; \(\tau\) occurs only in
the proximity bound (15a). In particular, (15) is not inferred merely by
drawing the continuous minimizer on top of the fine graph. The lifted tree
is not required to remain contained in \(Y\); the proof below uses only (15)
and (15a). Requiring both exact length and containment can already fail for a
short row of closed shifted cubes.

The activity output set also needs a support premise
\((\mathrm H_I)\). Here \(\operatorname {dist}_\eta(z,Y)\) means distance
to the fine sites represented in the geometric union \(Y\). For every
admitted \((p,\sigma,Y)\):

1. each \(x\in I(Y)\) has a deterministic site anchor \(z_x\) with
   \[
   \rho(z_x)=y_x,
   \qquad
   \operatorname {dist}_\eta(z_x,Y)\le h;
   \tag{16}
   \]
2. the source root cell \(q_p\) has an anchor \(z_p\) with
   \[
   \rho(z_p)=q_p,
   \qquad
   \operatorname {dist}_\eta(z_p,Q_{p,\sigma})\le h_q.
   \tag{17}
   \]

Site, bond, and plaquette coordinates use fixed anchor rules. The mark's own
base site may be used in (17), making \(h_q=0\) and \(q_p\) independent of
\(\sigma\). The constants \(h,h_q\) are measured in finest bonds and must be
common over the family.

Subsequent Note 0028 discharges this halo premise with \(h=h_q=0\) for the
first-stage direct-\(J\) derivatives of Notes 0012--0014, using their
repository interior-locality conclusion and deterministic bond/source
base-site anchors. Subsequent Note 0029 extends the zero-halo conclusion to
the completed Section-2 connected coefficients by using final-activity
bond-intersection locality, the literal-union connected map, and the
integer-wall closed-cubulation lemma. A common completed-coefficient Cauchy
tube remains separate.

Choose fine sites in \(Q_{p,\sigma}\) and in a cube of \(Y\) realizing the
two halo distances. Hypothesis \((\mathrm H_T)\) joins each such site to
\(\widetilde T_Y\). Joining the root anchor to the tree, traveling on the
tree, and joining to a target anchor costs at most

\[
h_q+dMb+\tau+Mb\,d_{k,\sigma}(Y)+dMb+\tau+h.
\tag{18}
\]

Equations (13) and (18) prove the forward comparison

\[
\boxed{
D_{\mathcal B}(q_p,Y)
\le C d_{k,\sigma}(Y)+C_0,
}
\tag{19}
\]

with

\[
\boxed{
C=c_{\rm nn}Mb,
\qquad
C_0=c_{\rm nn}(2dMb+2\tau+h+h_q).
}
\tag{20}
\]

For \(b=1\),

\[
C=M[d(L+2)+1].
\tag{21}
\]

In \(d=4\), \(c_{\rm nn}=4L+9\). The proof never aligns the shifted
\(M\)-grid with a deeper grid: it uses only a fine path and the fixed map
\(\rho\). Thus the constants have no shifted-orbit factor. Independence of
\(\sigma\) holds only when the common \((\mathrm H_T)\) constant \(\tau\)
and the support halos are themselves shift uniform.

## Essential scale warning

The mesh ratio \(b\) in (14) cannot be dropped. If a localization edge has
physical length \(Mb\eta\) and lies in the finest Propagators-II layer, its
\(d_{\mathcal B}\) cost is \(Mb\). Consequently (19) cannot have a constant
uniform in an unbounded \(b\).

Thus the forward bridge is regulator uniform only when Note 0014's current
fine mesh is the Propagators-II finest mesh, \(b=1\), or when their ratio is
uniformly bounded. Uniformity also requires common bounds on \(\tau,h,h_q\).
This is the actual scale-matching and discretization condition. Arbitrary
shift \(\sigma\) is not an additional factor once those bounds hold.

## Conditional all-layer auxiliary-\(J\) pullback

Retain every hypothesis of Note 0017 through its Eq. (21), including
\((\mathrm H_J)\), \(0\le\gamma<\delta_0/8\), the separated-cell hypothesis
for the source kernel, and the direct-\(J\) activity bound with exponent
\(a=(1-2\delta)\kappa\). Assume \((\mathrm H_\rho)\), \((\mathrm H_T)\),
\((\mathrm H_I)\), one common mesh bound \(b\le b_*\), and common constants
\(\tau,h,h_q\). Let \(\mathscr R\) denote the full admitted family of
regulators and background charts. Assume one common
\(C_\chi,c_1(\alpha_\gamma),\Delta_J^{-1}\), and \(\mathcal B_d\) over
\(\mathscr R\), as well as common local chart conversions with

\[
\overline E_J
=\sup_{\mathscr R,\,p,\sigma,Y}E_J(Y)<\infty.
\tag{22}
\]

Put

\[
C_*=c_{\rm nn}Mb_*,
\qquad
C_{0,*}=c_{\rm nn}(2dMb_*+2\tau+h+h_q),
\tag{23}
\]

and choose \(a_*\ge0\) such that

\[
a_*+\gamma C_*\le a.
\tag{24}
\]

Equations (19), (23), and (24) give

\[
e^{a_*d_{k,\sigma}(Y)}e^{\gamma D_{\mathcal B}(q_p,Y)}
\le
e^{\gamma C_{0,*}}
e^{a d_{k,\sigma}(Y)}.
\tag{25}
\]

Combining Note 0017 Eq. (21) with (25), summing, and then using Note 0017
Eq. (9) proves

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
\tag{26}
\]

Unlike Note 0017 Eq. (24), the sum in (26) is not restricted to one
homogeneous layer. It remains conditional on the new geometric, support,
mesh, and common-chart hypotheses. The exponent price is
\(\gamma c_{\rm nn}Mb_*\), not merely \(\gamma M\).

Subsequent Note 0028 updates the endpoint comparison, constants, and exponent
budget in (19)--(21) and (23)--(24) to the source-convention-safe values
\[
C_*^{\rm end}=c_{\rm nn}\sqrt d\,Mb_*,
\qquad
C_{0,*}^{\rm end}=c_{\rm nn}(2dMb_*+h+h_q),
\]
and removes \((\mathrm H_T)\) and \(\tau\). All
\((\mathrm H_\rho)\), mesh, representative, kernel, and common-chart
hypotheses remain.

## Exact boundary

- Propagators II prints the multiscale label set, admissible-contour metric,
  cell blocks, and triangle inequality. It does not print the tagged cover,
  its pulled-back pseudometric, the coordinatewise seam-aware map \(\rho\),
  the no-skipped-interface property, the source-admissible outer-collar
  construction, or the constant \(d(L+2)+1\). In particular, Eq. (2.53)
  does not define \(\rho\).
- RG I's contained tree is continuous. The discrete tree lift
  \((\mathrm H_T)\), including both (15) and the common error \(\tau\) in
  (15a), is not a source theorem established here. Subsequent Note 0028
  shows that it is unnecessary for the endpoint comparison.
- The identification or uniformly bounded ratio between Note 0014's current
  mesh and the Propagators-II finest mesh is an explicit premise. If
  \(b\to\infty\), the forward constant diverges.
- The halo hypothesis cannot be omitted. If \(Y=Q_{p,\sigma}\), then
  \(d_{k,\sigma}(Y)=0\); allowing \(I(Y)\) to contain an arbitrarily distant
  coordinate makes \(D_{\mathcal B}(q,Y)\) unbounded.
- Equation (19) is one sided. It neither contradicts nor repairs Note 0017's
  failure of the reverse comparison.
- For this note's original proof, regulator-uniform constants require fixed
  \(d,L,M\) and uniformly bounded \(b,\tau,h,h_q\). Note 0028 removes
  \(\tau\), but not the bounded-\(b\), interface, or remaining support
  requirements.
- Equation (26) is regulator uniform only under the explicitly common
  \(C_\chi,c_1(\alpha_\gamma),\overline E_J,\Delta_J^{-1}\), and
  \(\mathcal B_d\). Their finiteness at one regulator is not enough.
- Equation (26) controls only the auxiliary-\(J\) chain-rule summand. It still
  assumes common local conversion coefficients and does not supply Note
  0018's concrete RG-scaled \(U\) collar or the physical \(U\) pullback.
- Note 0021 supplies exact one-fixed-partition marked algebra, and Note 0026
  supplies its independent-variable marked norm and connected first jet.
  Note 0027 subsequently synchronizes the nested shifted first jets. No
  physical pulled-back expansion, nonzero-source polymer-activity disk,
  large-field estimate, RG iteration, continuum construction, infrared decay,
  or mass gap follows.

## Falsification checks

- Draw the layer-\(j\) tangential path directly on the inner-owned
  \(\Sigma_{j+1}\) and reject it; the incoming route in (9) stays outside
  except at \(w\), changes mesh there, and uses the first coarse bond to enter
  the inner layer.
- Permit a fine bond to jump over an uncompressed layer and identify the
  failure of (12).
- Replace the coordinatewise half-open selector by an arbitrary corner
  ordering and produce equal-layer fine neighbors assigned to diagonal
  cells.
- Omit the periodic seam rule and produce two possible values of \(\rho\) for
  the same periodic site.
- Treat the continuous shortest tree as an identical finest-bond tree. A
  shifted row of closed cubes can put the continuous minimizer on a
  boundary/coset not realized by the chosen fine graph. This note's original
  proof required \((\mathrm H_T)\); subsequent Note 0028 avoids the
  digitization entirely by bounding only the quotient endpoints.
- Let \(b=L^r\to\infty\) while a shifted-tree edge lies in layer zero and
  reject a regulator-uniform \(C\).
- Set \(Y=Q_{p,\sigma}\) and move one output anchor arbitrarily far away to
  falsify (19) without \((\mathrm H_I)\).
- Demand alignment between the shifted \(M\)-grid and every deeper grid and
  identify the unnecessary premise: the proof is bondwise.
- Use Note 0017 Eq. (25) to reject the forward bound and identify the reversed
  inequality actually obstructed there.
- Retain the old exponent budget \(a_*+\gamma M\le a\) instead of (24) and
  expose the missing cell-map and mesh factors.
- Move the chart supremum inside the source sum in (26) and reject the
  resulting interchange.
