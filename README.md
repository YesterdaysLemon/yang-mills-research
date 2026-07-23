# Yang–Mills existence and mass gap: an open research ledger

> **Official problem status: UNSOLVED** (checked 2026-07-23)
>
> **Repository status: EXPLORATORY — NOT A SOLUTION**
>
> Full-problem evidence level: **E0**. The highest individual item is an **E2 auxiliary lemma**, not progress through the central construction.

This is a public, versioned attempt to reason carefully about the four-dimensional Yang–Mills existence and mass-gap problem. Its purpose is to make every claim, dependency, failed route, and correction inspectable. Git history records work; it does not certify mathematics.

## The target

For every compact simple gauge group \(G\), construct a nontrivial quantum Yang–Mills theory on \(\mathbb R^4\) with axiomatic strength at least matching the frameworks cited by Jaffe and Witten, and prove that its Hamiltonian has a finite positive spectral gap.

The exact scope and the ways an apparent result can miss it are frozen in [PROBLEM.md](PROBLEM.md). The canonical source is the [Clay Mathematics Institute problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).

## Current work

The main route is a Wilson lattice regulator followed by gauge-covariant renormalization, construction of local gauge-invariant observables, Osterwalder–Schrader reconstruction, and a still-missing nonperturbative infrared bridge. The first bounded target is one source-inserted RG step; supporting notes isolate both its elementary raw source identities and the final gap certificate:

- [Chosen route and dependency map](ROADMAP.md)
- [Program 002: one-block observable RG theorem](research/programs/002-one-block-observable-rg.md)
- [Program 003: first source-jet remainder](research/programs/003-first-source-jet-remainder.md)
- [Program 001: continuum gap transfer](research/programs/001-continuum-gap-transfer.md)
- [Note 0001: dense-state semigroup criterion](research/notes/0001-dense-state-gap-criterion.md)
- [Note 0002: OS gap-transfer criterion](research/notes/0002-os-gap-transfer.md)
- [Note 0003: raw-block source jets](research/notes/0003-raw-block-source-jets.md)
- [Note 0004: fixed-background source jet](research/notes/0004-fixed-background-source-jet.md)
- [Note 0005: pointwise coarea kernels](research/notes/0005-pointwise-coarea-kernels.md)
- [Note 0006: local Bałaban fiber chart](research/notes/0006-local-balaban-fiber-chart.md)
- [Note 0007: projective source kernels](research/notes/0007-projective-source-kernels.md)
- [Note 0008: complete fixed-cutoff chart branch](research/notes/0008-full-fixed-cutoff-branch.md)
- [Note 0009: parameterized fixed-cube branch kernel](research/notes/0009-parameterized-fixed-cube-kernel.md)
- [Note 0010: exact normalized RG-I coordinate law](research/notes/0010-exact-rg-coordinate-law.md)
- [Note 0011: one marked insertion at the Mayer seam](research/notes/0011-one-mark-mayer-seam.md)
- [Note 0012: rooted cube-count localization of one plaquette mark](research/notes/0012-rooted-plaquette-localization.md)
- [Note 0013: rooted d-k-weighted norm for one interior mark](research/notes/0013-rooted-dk-norm.md)
- [Note 0014: RG-admitted shifted-root cover for every plaquette](research/notes/0014-equivariant-shifted-roots.md)
- [Note 0015: fixed-patch physical composition of one rooted mark](research/notes/0015-fixed-patch-physical-composition.md)
- [Note 0016: exact auxiliary J and fixed-regulator Cauchy tubes](research/notes/0016-auxiliary-j-cauchy-tubes.md)
- [Note 0017: strict auxiliary J margin and dual metric pullback](research/notes/0017-strict-j-margin-metric-pullback.md)
- [Note 0018: raw U collar obstruction and scaled repair target](research/notes/0018-raw-u-collar-obstruction.md)
- [Note 0019: conditional forward multiscale cell-map bridge](research/notes/0019-forward-multiscale-cell-map.md)
- [Note 0020: one-mark Ursell identity on a fixed polymer gas](research/notes/0020-one-mark-ursell-identity.md)
- [Note 0021: one marked component through the RG-II Section-2 map](research/notes/0021-one-mark-section2-factorization.md)
- [Note 0022: whole-integrand Cauchy control for the Section-2 mark](research/notes/0022-whole-integrand-marked-cauchy.md)
- [Note 0023: fixed-cubical hull, animal entropy, and pinned KP](research/notes/0023-fixed-cubical-hull-animals-kp.md)
- [Note 0024: Balaban final-gas cubical instantiation and explicit KP window](research/notes/0024-balaban-final-gas-instantiation.md)
- [Note 0025: source-faithful conditioned routing of one localized mark](research/notes/0025-conditioned-mark-routing.md)
- [Note 0026: positive marked-seed resummation through the RG-II scale step](research/notes/0026-marked-seed-resummation.md)
- [Note 0027: shifted first-jet synchronization through nested Section-2 branches](research/notes/0027-shifted-first-jet-synchronization.md)
- [Note 0028: periodic endpoint bridge without tree digitization](research/notes/0028-endpoint-distance-bridge.md)
- [Note 0029: completed external-J support through the literal union](research/notes/0029-completed-external-j-support.md)
- [Note 0030: completed affine-J tube and Banach connected norm](research/notes/0030-completed-j-cauchy-tube.md)
- [Note 0031: real-center covariant-U tube and product Banach norm](research/notes/0031-real-center-covariant-u-tube.md)
- [Note 0032: support-anchored physical-J pullback without H-rho](research/notes/0032-support-anchored-physical-j-pullback.md)
- [Note 0033: quotient-localized physical-U pullback](research/notes/0033-quotient-localized-physical-u-pullback.md)
- [Bałaban theorem-level source map](literature/audits/2026-07-22-balaban-source-map.md)
- [Bałaban imported-map audit](literature/audits/2026-07-22-balaban-imported-map.md)
- [Bałaban final-gas/KP source audit](literature/audits/2026-07-22-balaban-final-gas-kp-map.md)
- [Bałaban conditioned-mark routing audit](literature/audits/2026-07-23-balaban-conditioned-mark-routing.md)
- [Bałaban marked-resummation source audit](literature/audits/2026-07-23-balaban-marked-resummation.md)
- [Bałaban shifted first-jet transport audit](literature/audits/2026-07-23-balaban-shifted-first-jet-transport.md)
- [Bałaban contained-tree to multiscale-endpoint audit](literature/audits/2026-07-23-endpoint-distance-bridge.md)
- [Bałaban completed external-J support audit](literature/audits/2026-07-23-balaban-completed-external-j-support.md)
- [Bałaban completed affine-J tube audit](literature/audits/2026-07-23-balaban-completed-j-cauchy-tube.md)
- [Bałaban real-center U-tube audit](literature/audits/2026-07-23-balaban-real-center-u-tube.md)
- [Bałaban support-anchored J-pullback audit](literature/audits/2026-07-23-balaban-support-anchored-j-pullback.md)
- [Bałaban quotient-localized U-pullback audit](literature/audits/2026-07-23-balaban-quotient-localized-u-pullback.md)

Programs 002 and 003 are open theorem specifications, not results. The notes prove auxiliary finite-regulator and fixed-chart statements for a selected small-field branch; they do not identify that branch with the unrestricted raw transform. Notes 0021, 0025, and 0026 carry one interior plaquette mark through the exact fixed-partition RG-II algebra, the source-faithful conditioned formula, and the positive \(D/P/Z_0\) plus scale resummations. Under the explicit doubled-\(\varepsilon _2\) refinement and Note 0024's separate ordinary KP ceiling, this gives an absolutely convergent connected first derivative at \(t=0\). Under the added periodic compatibility \(LM\mid N\) and a nonempty common external branch domain, Note 0027 repeats the complete construction on every nested shifted branch, proves that all branch numerator/denominator pairs reconstruct the same dual-number integral up to a nonzero scalar, and averages only the completed connected coefficients. Note 0028 removes Note 0019's artificial discrete-tree-lift hypothesis and its \(\tau\) loss by a periodic covering-space endpoint argument. Note 0029 then carries external-\((U,J)\) restriction locality through the marked dual-number map and literal-union connected sum. It retains RG I's exact bond-intersection support convention and uses the admitted integer-wall closed cubulations to prove zero endpoint halos for the completed external-\(J\) coefficient. Under the completed representative compatibility hypothesis \((\mathrm H_J^{\rm conn})\), Note 0030 applies the affine \(J\) margin at the output scale and reruns the marked connected estimate in coefficientwise local \(H^\infty\) norms. Note 0031 gives a concrete full complex \(U/J\) product tube in a covariant-curl relative-log norm under the stronger common real-center hypothesis \((\mathrm H_{\rm rc})\). Its ordered-matrix estimate proves an explicit positive \(U\) radius and the product Banach rerun gives full \(U\)-chart and \(J\) dual derivative norms without bond-volume or shifted-branch factors. Note 0032 composes that completed \(J\) derivative with the audited Eq. (190) kernel in a support-anchored hybrid norm. It needs no \((\mathrm H_\rho)\), mesh comparison, endpoint allowance, or loss from the polymer exponent \(\kappa\); the source-kernel weight still requires \(0\le\gamma<\delta _0/8\). The stronger marked-plaquette-rooted norm instead follows from the less structured aggregate hypothesis \((\mathrm H_{\rm end})\).

Note 0033 treats the physical-\(U\) summand. Under common converted Eq. (190) rows for every feature in Note 0031's covariant norm and a common global scale envelope, it proves an unweighted source sum without a coordinate, bond-volume, mesh, or branch factor. For positive source decay it replaces the false direct-\(J\) coordinate-dual argument by exact restriction-quotient duality and identifies the sharp quotient-synthesis kernel moment. A feature-support-anchored bound follows only under the new local extension hypothesis \((\mathrm H_{\rm ext}^U)\); active-bond anchoring additionally pays an explicit collar halo. The common converted feature rows, covariant-curl identity, scale envelopes, extension theorem, and \((\mathrm H_{\rm rc})\) for the actual minimizing family remain open.

The selected-coordinate scalar source disk was already proved in Notes 0007 and 0010. Source-dependent polymer activities at nonzero source, unit-translation covariance, the remaining physical-family uniformity and rooted-locality gates, large fields, RG iteration, continuum construction, axioms, infrared decay, and the mass gap remain open. No Yang--Mills solution is claimed here.

Note 0020 settles the exact distinguished-vertex Ursell formula, including
its \(1/n!\) coefficient, repeated labels, and a conditional pinned cluster
bound, for one fixed hard-core gas. Note 0021 now carries the localized mark
through the finite RG-II Section-2 algebra, defines its decorated
post-polymerization image, proves the unique marked-component factorization,
and obtains the exact hard-core numerator. Note 0025 closes the direct
fixed-term conditioning/weakening domination: the localized mark remains on
the conditional interior \(B\), the marked seed cutoff supplies its
Eq. (1.34) bound, and the relative Gaussian-moment cost is zero. Note 0026
then proves the positive marked-seed resummation. The exact finite-subfamily
collision costs a factor \(2\), while one doubled-amplitude susceptibility
controls all later scale-stage choices. This yields
\(C_{\rm sec}=4K_{\rm lift}\alpha _6^{-1}\), the
\((1-8\delta)(L/2)\kappa\) pointwise exponent, the
\((1-9\delta)(L/2)\kappa\) rooted marked norm, and the fixed-gas connected
first-jet output at exponent \(\kappa\).

Note 0027 resolves the former shifted synchronization hypothesis at the
first-jet level, under \(LM\mid N\) and its explicit nonempty common-domain
hypothesis. It lifts input shifts modulo \(M\) to nested two-scale branches
modulo \(LM\), runs each gas separately over
\(\mathbb C[\epsilon]/(\epsilon^2)\), and proves projective equality before
forming the logarithm. Normalizing the completed branch coefficients by the
full lifted count costs no orbit factor. No cross-shift gas is introduced.

Note 0028 replaces the discrete-tree-lift premise in Note 0019 by a direct
periodic endpoint estimate. A continuous contained tree of Euclidean length
\(\ell\) gives at most \(\sqrt d\,\ell/\eta\) fine-lattice endpoint steps;
after the two within-cube allowances this yields
\[
D_{\mathcal B}(q_p,Y)
\le c_{\rm nn}\!\left[
\sqrt d\,Mb\,d_{k,\sigma}(Y)+2dMb+h+h_q
\right].
\]
For first-stage direct-\(J\) activities, the already proved interior-bond
support gives \(h=h_q=0\). The ownership/interface hypothesis
\((\mathrm H_\rho)\), bounded mesh ratio, common analytic constants, and
every nonlinear-\(U\) issue remain open.

Note 0029 closes the corresponding support statement for the completed
connected coefficient. RG II localizes each final \(H(C)\) in the external
fields on \(\operatorname {int}C\); the marked dual-number coefficient
inherits that locality, and every connected term contributing to \(R\) has
literal union \(R\). Thus
\[
I^{\rm conn}_{J,p,s}(R)
\subset
\{b:\ |b|\cap\operatorname {int}R\ne\varnothing\}.
\]
RG I defines restriction by this bond-intersection rule. On the admitted
integer-wall cubulations, every nearest-neighbor bond in the displayed set
has both endpoints in the closed union \(R\), so
\[
h=h_q=0.
\]
This is exact support, not by itself a derivative bound. Note 0030 closes the
next analytic gate under \((\mathrm H_J^{\rm conn})\). With
\(\Delta_J=\alpha _0-\bar\alpha _0\), restriction of every completed branch
to the support-local affine tube and a coefficientwise \(H^\infty\) rerun
give
\[
\sup_p\sup_{(U,J)\in\mathfrak K_p^{J,\mathrm{phys}}}
\sum_{s,R}e^{\kappa d_{k+1,s}(R)}
\sup_{\substack{\operatorname {supp}w\subset\mathsf E_s^{\rm loc}(R)\\
\lVert w\rVert_\infty<\Delta_J}}
\left|\widehat{\mathcal C}_p^+(s,R;U,J+w)\right|
\le B_{\rm conn}.
\]
Banach-line Cauchy and the support projection then give the corresponding
full \((\ell^\infty)^*\) derivative norm bounded by
\(B_{\rm conn}/\Delta_J\), with no bond count. This is an independent-\(J\)
tube, not a nonzero plaquette-source polymer disk. Note 0032 subsequently
uses it to prove a support-anchored physical-\(J\) chain-rule norm without
\((\mathrm H_\rho)\) or mesh matching; common kernel/chart constants remain
conditional, and pure plaquette-rooted decay needs an endpoint or
coefficient-weighted substitute.

Note 0031 supplies a concrete replacement on the retained common real-center
family. In the relative chart
\(\Phi_{\bar U}(a)=e^{i\xi a}\bar U\), use a norm controlling \(a\), RG I's
background-covariant derivative, and the covariant plaquette curl. The exact
ordered four-exponential remainder gives
\[
|d\Phi_{\bar U}(a)-1|_{\rm RG}
<
\xi^2\!\left[
\bar a_U+c_+\left(r+8r^2e^{4\xi r}\right)
\right].
\]
Thus, under the common real-center hypothesis
\((\mathrm H_{\rm rc})\),
\[
r_U=\min\left\{
1,\ a_1,\
\frac{a_0-\bar a_U}{c_+(1+8e^4)}
\right\}>0
\]
is a full complex radius. Combining it with
\(\Delta_J=\alpha _0-\bar a_J\) gives one product tube through every
complete shifted branch. The product \(H^\infty\) rerun preserves
\(B_{\rm conn}\), and Cauchy gives the full dual bounds
\(B_{\rm conn}/r_U\) and \(B_{\rm conn}/\Delta_J\). The matrix estimate is
proved; uniform existence of the common real centers is still a hypothesis.

Note 0033 supplies the functional-analytic part of the physical-\(U\)
pairing. Under its still-open common converted feature rows and global scale
envelope,
\[
\sum_{s,R}e^{\kappa d_{k+1,s}(R)}
\sum_\alpha\mu_\alpha
\left|\mathcal L_{p,s,R}^{U,\rm conn}(\alpha)\right|
\le
\frac{
C_{\chi,U}c_1(1/8)\overline E_U^{\rm glob}B_{\rm conn}
}{r_U}.
\]
For \(0<\gamma<\delta _0/8\), completed external-\(U\) locality instead
leads to the restriction quotient \(X_{\bar U,\xi}/N_I\). The weighted
quotient-synthesis norm is the sharp coefficient-independent missing
constant. A feature-support-anchored bound follows under
\((\mathrm H_{\rm ext}^U)\) with constant
\(C_{\rm ext}C_{\chi,U}c_1(\alpha_\gamma)
\overline E_U^{\rm conn}B_{\rm conn}/r_U\).
Neither the converted covariant-curl row, common scale envelopes, nor this
positive-decay extension theorem is currently proved for the physical
family.

Note 0032 does complete the auxiliary-\(J\) kernel composition in a hybrid
norm. If \(S_{p,s,R}\) is the tagged multiscale-label set of the completed
coefficient's active external-\(J\) coordinates, use the pulled-back
pseudometric
\(d_{\widetilde{\mathcal B}}((j,y),(j',y'))
=d_{\mathcal B}(y,y')\). Then, under the still-open common kernel/chart
constants,
\[
\sum_{s,R}e^{\kappa d_{k+1,s}(R)}
\sum_{j',y'}\mu(j',y')
e^{\gamma d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')}
\left|\mathcal L_{p,s,R}^{J,\rm conn}(j',y')\right|
\le
\frac{C_\chi c_1(\alpha_\gamma)\overline E_J^{\rm conn}B_{\rm conn}}
{\Delta_{\rm tube}}.
\]
No \((\mathrm H_\rho)\), mesh comparison, endpoint allowance, or loss from
the polymer exponent \(\kappa\) appears; the source-kernel weight still uses
\(0\le\gamma<\delta _0/8\). This is decay from the active \(J\) support,
not from the marked plaquette alone. The latter follows from the sufficient
aggregate endpoint hypothesis for a tagged root \(\widetilde q_{p,s}\),
\(\sup_{\widetilde y\in S}
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y)
\le A d_{k+1,s}(R)+B\), with
\(a_*+\gamma A\le\kappa\). A one-coordinate countermodel proves that some
endpoint information or coefficient-weighted substitute is indispensable
for that stronger rooted inference.

Under its stated common \(L^1\)-holomorphy and joint-majorant hypotheses,
Note 0022 proves that Eq. (2.8)'s whole-integrand weakening contour carries
the mark with no extra Leibniz or decoration-allocation multiplicity, and
with the ordinary Cauchy-radius factor if the marked term shares the source
radius. It also corrects the conditional exponent bookkeeping to a parallel
fork. Note 0025 corrects the earlier schematic transformed argument:
Eqs. (2.5)--(2.14) never give the localized plaquette mark the standardized
exterior \(X\) or second-stage weakening variables. Note 0026 closes the
resulting positive \(A\)-to-output resummation through the
\(k\)-to-\(k+1\) scale conversion under the explicit requirement that every
ordinary scale-stage smallness condition also hold at
\(2\varepsilon _2\).

Note 0023 closes the previously abstract hull/animal/KP implication inside a
declared standard closed-cube model. The literal union pays an unavoidable
contact charge \(\sqrt7\) per ordinary occurrence in four dimensions, while
an explicit rooted-animal estimate is uniform for
\(\eta>64\log8\). Note 0024 then checks the immutable primary pages and
identifies Balaban's final connected ordinary RG-II gas with that cubical
support model through a one-sided source-metric comparison and a direct
\(\sqrt7\) connector; it does not identify the source metric with the
auxiliary degenerate-tree convention. It also exhibits a nonempty
displayed-hierarchy-compatible
\((\kappa,\varepsilon _1)\) sub-hierarchy satisfying the repository's
explicit ordinary pinned-KP inequality. Note 0026 imports that ordinary
ceiling separately from its doubled-\(\varepsilon _2\) scale refinement.
This is not yet the Yang--Mills estimate: Note 0027 synchronizes only the
independent-variable first derivative at \(t=0\). The exact selected-coordinate
scalar ratio is already zero-free for one plaquette on
\(|t|<\log 2/4\), but no source-dependent polymer activities or uniform KP
theorem on that disk is proved. Physical pullbacks and every continuum and
infrared gate remain open.

## Evidence discipline

- [CLAIMS.json](CLAIMS.json) is the authoritative claim registry.
- [STATUS.json](STATUS.json) records full-problem gates separately from partial lemmas.
- [GOVERNANCE.md](GOVERNANCE.md) defines evidence levels E0–E8, promotion rules, corrections, and announcement language.
- [audit/checklist.md](audit/checklist.md) tracks the obligations of the official problem.
- [audit/objections.json](audit/objections.json) preserves unresolved attacks and defects.
- [research/LOG.md](research/LOG.md) is the chronological research ledger.

Run the repository checks with:

```text
python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

The checks enforce metadata and claim-governance invariants. They do **not** verify deep mathematical truth.

## Non-claims

This repository does not currently construct a four-dimensional continuum Yang–Mills QFT, remove its regulators, verify the full axioms, prove nontriviality, or establish a mass gap. Numerical evidence, fixed-lattice strong-coupling results, lower-dimensional models, and perturbation theory alone would not settle the stated problem.

## Participate critically

Proof-breaking is more valuable than cheerleading. Open an issue with the exact claim ID, the first invalid step, and a counterexample or missing hypothesis when possible. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Official status and prize process

Clay currently lists the problem as unsolved. A prize candidate must be published in a qualifying outlet, survive at least two years of rigorous community examination, achieve general acceptance, and then pass Clay's process. Clay does not accept direct submissions. See the [official rules](https://www.claymath.org/millennium-problems/rules/).

## License

Code and original repository text are released under the [MIT License](LICENSE). External sources retain their own rights.
