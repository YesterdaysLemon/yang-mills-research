# Note 0032: a support-anchored physical-\(J\) pullback without \((\mathrm H_\rho)\)

Claim ID: YM-RG-032

Kind: conditional finite-regulator kernel-pullback and sharpness lemma

Evidence: E2 (finite-dimensional duality plus the already audited
Propagators-II kernel convolution; internally checked)

Novelty: none claimed

Primary anchors:

- T. Balaban, [*The variational problem and background fields in
  renormalization group method for lattice gauge
  theories*](https://doi.org/10.1007/BF01229381), Proposition 9 and
  Eq. (190) on printed pp. 307--309;
- T. Balaban, [*Propagators and renormalization transformations for lattice
  gauge theories II*](https://doi.org/10.1007/BF01240221), Lemma 2.1 and
  Eqs. (2.59)--(2.63);
- Notes 0017, 0029, 0030, and 0031.

## Scope and completed derivative input

Everything in this note is at finite regulator. The coordinate spaces are
finite dimensional, so the dual of a direct-sum \(\ell^\infty\) norm is the
coordinatewise \(\ell^1\) sum. No assertion about the dual of an
infinite-dimensional \(\ell^\infty\) space is used.

Retain the completed marked construction of Notes 0024--0029 and one of the
two completed \(J\)-tube inputs:

1. under Note 0030's \((\mathrm H_J^{\rm conn})\), put
   \[
   \Delta_{\rm tube}=\alpha _0-\bar\alpha _0;
   \tag{1a}
   \]
2. on Note 0031's common real-center family, put
   \[
   \Delta_{\rm tube}=\alpha _0-\bar a_J.
   \tag{1b}
   \]

Write \(\mathfrak K_p^{\rm tube}\) for the corresponding retained physical
center family. Both inputs give

\[
\boxed{
\sup_p\sup_{(U,J)\in\mathfrak K_p^{\rm tube}}
\sum_s\sum_{R\supset\widehat Q_{p,s}}
e^{\kappa d_{k+1,s}(R)}
\left\|
D_J\widehat{\mathcal C}_p^+(s,R)
\right\|_{(\ell^\infty)^*}
\le
\frac{B_{\rm conn}}{\Delta_{\rm tube}}.
}
\tag{2}
\]

The new result below uses (2), not the \(U\)-derivative part of Note 0031.
Thus the common real-center hypothesis is one sufficient instantiation, not
a new premise hidden inside the kernel argument.

## The retained source-kernel input

Use Note 0017's normalization

\[
s_j=L^j\eta,
\qquad
\mu(j,y)=s_j^d,
\qquad
\lambda_J=\frac{\delta _0}{8}.
\tag{3}
\]

Let the tagged output/source label space be

\[
\widetilde{\mathcal B}
=
\bigsqcup_j\bigl(\{j\}\times\Lambda_j\bigr).
\]

Pull back the source metric to a possibly degenerate tagged metric by

\[
d_{\widetilde{\mathcal B}}
\bigl((j,y),(j',y')\bigr)
:=
d_{\mathcal B}(y,y').
\tag{3a}
\]

The source notation suppresses these layer tags. The pullback can assign
zero distance to two distinct tags of the same physical label; only
nonnegativity and the inherited triangle inequality are used below.

For each external \(J\)-bond \(b\), let \(x_b\) be the deterministic oriented
base site used in Note 0029. Use the tagged Propagators-II output label

\[
\widetilde y_b=(j_b,y_b),
\qquad
y_b\in\Lambda_{j_b},
\qquad
x_b\in\Delta(y_b),
\tag{4}
\]

of the type already appearing in Eq. (190). Likewise write
\(\widetilde y'=(j',y')\) for a source label. If the source construction
permits more than one valid output label, fix one for each coordinate. This
coordinatewise choice is not Note 0019's half-open ownership map: no
nearest-neighbor compatibility, interface route, periodic selector, or root
comparison is required.

Let

\[
K_b(j',y')
=
\frac{\delta\mathcal J(b)}
{\delta B(j',y')}.
\tag{5}
\]

Here and below the notation suppresses the finite spacetime-direction and
Lie-algebra component index \(\vartheta\) of the source coordinate. More
precisely,

\[
K_b(j',y';\vartheta)
=
\frac{\delta\mathcal J(b)}
{\delta B_\vartheta(j',y')}
\]

is an element of the \(J(b)\) component block, and
\(\|\cdot\|_{\mathsf J}\) is the norm on that block. Every displayed
\(\sum_{j',y'}\) also includes the finite sum over \(\vartheta\); its fixed
multiplicity is absorbed into \(C_\chi\). Thus
\(\ell_{p,s,R,b}[K_b(j',y';\vartheta)]\) is a scalar and the absolute value
in the chain-rule density is unambiguous.

Assume that Note 0017's fixed-chart Eq. (190) conversion constants can be
chosen commonly over the completed family. Let
\(\|\cdot\|_{\mathsf J}\) be the finite-dimensional component norm used in
the direct-\(J\) tube. A fixed norm-equivalence factor comparing the printed
operator norm with \(\|\cdot\|_{\mathsf J}\) is absorbed into \(C_\chi\).
Then

\[
\left\|K_b(j',y')\right\|_{\mathsf J}
\le
C_\chi E_J(j_b)\mu(j',y')^{-1}
e^{-\lambda_J d_{\widetilde{\mathcal B}}
(\widetilde y_b,\widetilde y')},
\tag{6}
\]

where

\[
E_J(j)
=
C_{J,4}s_j^{-3}
+C_{J,2}s_j^{-2}
+C_{J,1}s_j^{-1}.
\tag{7}
\]

Fix

\[
0\le\gamma<\lambda_J,
\qquad
\alpha_\gamma
=
\frac18-\frac\gamma{\delta _0}>0,
\tag{8}
\]

and retain the strengthened separation condition required by Propagators II
Lemma 2.1 at \(\alpha_\gamma\). The source-measure cancellation and
exponential sum proved in Note 0017 then give

\[
\boxed{
\sum_{j',y'}\mu(j',y')
e^{\gamma d_{\widetilde{\mathcal B}}
(\widetilde y_b,\widetilde y')}
\left\|K_b(j',y')\right\|_{\mathsf J}
\le
C_\chi c_1(\alpha_\gamma)E_J(j_b).
}
\tag{9}
\]

Let \(\mathscr F_{\rm comp}\) be the retained family of finite regulators
and completed branch data. For
\(\mathfrak r\in\mathscr F_{\rm comp}\), write
\(\mathfrak K_{p,\mathfrak r}^{\rm tube}\) for the selected center family.
Finally assume the completed output-coordinate envelope

\[
\overline E_J^{\rm conn}
:=
\sup_{\substack{
\mathfrak r\in\mathscr F_{\rm comp},\ p,\ 
(U,J)\in\mathfrak K_{p,\mathfrak r}^{\rm tube},\ s,R\\
b\in I^{\rm conn}_{J,p,s}(R)}}
E_J(j_b)
<\infty.
\tag{10}
\]

This is the existing \(\overline E_J\) when that constant is chosen over the
completed family. Its uniformity, like that of \(C_\chi\) and the local
conversion constants, remains a hypothesis. The present argument removes
\((\mathrm H_\rho)\) and mesh matching; it does not manufacture common
Eq. (190) constants.

## The active-label set and its distance

Use Note 0029's structural derivative-support set

\[
I^{\rm conn}_{J,p,s}(R)
=
\left\{
b:
D_{J(b)}\widehat{\mathcal C}_p^+(s,R)
\text{ is not identically zero}
\right\}.
\tag{11}
\]

For a nonempty support define

\[
\boxed{
S_{p,s,R}
=
\left\{
\widetilde y_b:
b\in I^{\rm conn}_{J,p,s}(R)
\right\},
}
\tag{12}
\]

and

\[
d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')
=
\min_{\widetilde y\in S_{p,s,R}}
d_{\widetilde{\mathcal B}}(\widetilde y,\widetilde y').
\tag{13}
\]

If \(I^{\rm conn}_{J,p,s}(R)=\varnothing\), then the finite-dimensional
\(J\)-derivative and its physical chain-rule density are identically zero.
Such a coefficient contributes zero and is omitted before (13) is formed.
This convention avoids the undefined product
\(e^{\gamma d(\varnothing,\widetilde y')}0\).

The weight

\[
\kappa d_{k+1,s}(R)
+
\gamma d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')
\tag{14}
\]

is a two-stage network cost. The rooted polymer metric reaches the complete
connected support, while the Propagators-II metric runs from the nearest
active external-\(J\) coordinate to the physical source label. It is not a
pure marked-plaquette-to-source distance.

## Support-anchored physical-\(J\) theorem

At a retained physical center, write the finite-dimensional derivative as

\[
D_J\widehat{\mathcal C}_p^+(s,R)[v]
=
\sum_{b\in I^{\rm conn}_{J,p,s}(R)}
\ell_{p,s,R,b}[v(b)].
\tag{15}
\]

Define the completed physical-\(J\) chain-rule density

\[
\mathcal L_{p,s,R}^{J,\rm conn}(j',y')
=
\sum_{b\in I^{\rm conn}_{J,p,s}(R)}
\ell_{p,s,R,b}
\left[K_b(j',y')\right].
\tag{16}
\]

Then

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(U,J)\in\mathfrak K_p^{\rm tube}}
\sum_s
\sum_{\substack{R\supset\widehat Q_{p,s}\\
S_{p,s,R}\ne\varnothing}}
e^{\kappa d_{k+1,s}(R)}
\sum_{j',y'}\mu(j',y')
e^{\gamma d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')}
\left|
\mathcal L_{p,s,R}^{J,\rm conn}(j',y')
\right|\\
&\qquad\le
\frac{
C_\chi c_1(\alpha_\gamma)
\overline E_J^{\rm conn}
B_{\rm conn}
}{
\Delta_{\rm tube}
}.
\end{aligned}
}
\tag{17}
\]

In particular, the full polymer exponent \(\kappa\) is retained. There is no
endpoint additive factor, mesh ratio, support-cardinality factor, bond-volume
factor, or shifted-branch factor.

For every active \(b\),

\[
d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')
\le
d_{\widetilde{\mathcal B}}(\widetilde y_b,\widetilde y').
\tag{18}
\]

The scalar triangle inequality and operator duality therefore give

\[
\begin{aligned}
&e^{\gamma d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')}
\left|
\mathcal L_{p,s,R}^{J,\rm conn}(j',y')
\right|\\
&\quad\le
\sum_b
\|\ell_{p,s,R,b}\|_*
e^{\gamma d_{\widetilde{\mathcal B}}(\widetilde y_b,\widetilde y')}
\|K_b(j',y')\|_{\mathsf J}.
\end{aligned}
\tag{19}
\]

Multiply by \(\mu(j',y')\), sum in \((j',y')\), and apply (9) to each
coordinate:

\[
\begin{aligned}
&\sum_{j',y'}\mu(j',y')
e^{\gamma d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y')}
\left|
\mathcal L_{p,s,R}^{J,\rm conn}(j',y')
\right|\\
&\quad\le
C_\chi c_1(\alpha_\gamma)
\sum_bE_J(j_b)\|\ell_{p,s,R,b}\|_*\\
&\quad\le
C_\chi c_1(\alpha_\gamma)\overline E_J^{\rm conn}
\sum_b\|\ell_{p,s,R,b}\|_*.
\end{aligned}
\tag{20}
\]

At finite regulator, direct-sum duality is exact:

\[
\sum_b\|\ell_{p,s,R,b}\|_*
=
\left\|
D_J\widehat{\mathcal C}_p^+(s,R)
\right\|_{(\ell^\infty)^*}.
\tag{21}
\]

Multiplying (20) by \(e^{\kappa d_{k+1,s}(R)}\), summing, and applying (2)
proves (17).

For comparison only, choose any tagged root
\(\widetilde q_{p,s}\in\widetilde{\mathcal B}\). Relative to Note 0017
Eq. (21), the proof replaces the root triangle

\[
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y')
\le
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y_b)
+d_{\widetilde{\mathcal B}}(\widetilde y_b,\widetilde y')
\tag{22}
\]

by the tautological set-distance inequality (18). The Eq. (190) convolution
is otherwise unchanged. Notes 0019 and 0028 are not used in (17).

## A sufficient endpoint hypothesis for the plaquette-rooted norm

The stronger old target can be recovered from a much less structured
geometry premise than \((\mathrm H_\rho)\). Choose a tagged
Propagators-II root label \(\widetilde q_{p,s}\in\widetilde{\mathcal B}\)
for the marked plaquette root.

**Uniform support-endpoint hypothesis \((\mathrm H_{\rm end})\).** There are
constants \(A,B\ge0\), common over the retained family, such that

\[
\boxed{
\sup_{\widetilde y\in S_{p,s,R}}
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y)
\le
A\,d_{k+1,s}(R)+B.
}
\tag{23}
\]

This asks only for the final aggregate endpoint inequality. It does not ask
for an ownership map, a nearest-neighbor image theorem, an interface route,
or a mesh construction.

For \(a_*\ge0\) satisfying

\[
\boxed{
a_*+\gamma A\le\kappa,
}
\tag{24}
\]

the triangle inequality and (23) imply

\[
d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y')
\le
A\,d_{k+1,s}(R)+B
+d_{\widetilde{\mathcal B}}(S_{p,s,R},\widetilde y').
\tag{25}
\]

Consequently, (17) gives

\[
\boxed{
\begin{aligned}
&\sup_p\sup_{(U,J)\in\mathfrak K_p^{\rm tube}}
\sum_s
\sum_{\substack{R\supset\widehat Q_{p,s}\\
S_{p,s,R}\ne\varnothing}}
e^{a_*d_{k+1,s}(R)}
\sum_{j',y'}\mu(j',y')
e^{\gamma d_{\widetilde{\mathcal B}}
(\widetilde q_{p,s},\widetilde y')}
\left|
\mathcal L_{p,s,R}^{J,\rm conn}(j',y')
\right|\\
&\qquad\le
\frac{
C_\chi c_1(\alpha_\gamma)
\overline E_J^{\rm conn}
e^{\gamma B}B_{\rm conn}
}{
\Delta_{\rm tube}
}.
\end{aligned}
}
\tag{26}
\]

If positive residual polymer decay is required, take
\(a_*>0\), hence \(\gamma A<\kappa\). Keeping the original exponent
\(a_*=\kappa\) is generally impossible unless \(\gamma A=0\).

Note 0028 together with \((\mathrm H_\rho)\) and
\(b_{k+1,s}\le b_*\) supplies the special values below when the labels in
(4) and the tagged root are chosen to be the corresponding
\(\rho\)-anchors:

\[
A=c_{\rm nn}\sqrt d\,Mb_*,
\qquad
B=2d\,c_{\rm nn}Mb_*,
\qquad
c_{\rm nn}=d(L+2)+1.
\tag{27}
\]

Thus the old geometry package is one sufficient construction of
\((\mathrm H_{\rm end})\), not a premise of the support-anchored theorem.

## Worst-case sharpness of the endpoint requirement

For \(\gamma>0\), the completed derivative norm and the source-kernel
convolution alone cannot imply a regulator-uniform
\(q_{p,s}\)-rooted estimate. Consider the following abstract sequence of
finite models:

\[
d_{k+1,s_n}(R_n)=1,
\qquad
I^{\rm conn}_{J,p,s_n}(R_n)=\{b_n\},
\qquad
\|\ell_{b_n}\|_*=1,
\tag{28}
\]

with source labels satisfying

\[
d_{\widetilde{\mathcal B}}
(\widetilde q_{p,s_n},\widetilde y_{b_n})=n.
\tag{29}
\]

Take \(\mu=1\), let \(K_{b_n}\) equal \(1\) at the single source label
\(\widetilde y'=\widetilde y_{b_n}\) and vanish elsewhere, and take the
analytic coefficient
\(F_n(J)=J(b_n)\) on the unit affine tube. Every unrooted exponential kernel
sum, tube norm, and unweighted derivative norm is then bounded by \(1\).
The polymer-weighted quantities have the common factor \(e^\kappa\), so they
remain uniformly bounded in \(n\). After cancelling that common factor, the
support-anchored source weight is \(1\), whereas the plaquette-rooted weight
is

\[
e^{\gamma d_{\widetilde{\mathcal B}}
(\widetilde q_{p,s_n},\widetilde y_{b_n})}
=e^{\gamma n}\longrightarrow\infty.
\tag{30}
\]

This is a countermodel to an inference from the retained inequalities. It
does not assert that Balaban's actual multiscale geometry realizes this
sequence. It shows that some endpoint information, or an analytic substitute
carrying equivalent weighted information, is indispensable for the stronger
rooted target.

The wording matters. Hypothesis \((\mathrm H_{\rm end})\) is a sufficient,
worst-case-sharp **geometry-only** condition for deriving (26) from the
unweighted dual norm. It is not logically necessary for a particular
coefficient family: coefficient amplitudes can themselves decay with the
endpoint distance, and a coefficient-weighted endpoint moment can be weaker.

## Exact boundary

- Equation (17) proves decay away from the full active external-\(J\)
  support, not pure decay away from the marked plaquette.
- The proof eliminates \((\mathrm H_\rho)\), endpoint mesh matching, and any
  loss from the polymer exponent \(\kappa\) for this hybrid norm. It still
  spends source-kernel decay through \(\gamma<\lambda_J\), and it retains the
  completed tube premise,
  the common Eq. (190) constants, the strengthened Propagators-II separation
  condition, and \(\overline E_J^{\rm conn}<\infty\).
- Different valid coordinatewise kernel labels can give different valid
  hybrid norms. Enlarging \(S_{p,s,R}\) weakens the weight and preserves the
  estimate.
- Repeated active coordinates with the same label cause no factor: the
  coordinate sum is already the exact finite-dimensional dual norm.
- Note 0029's structural support is used. The proof does not rely on
  background-specific cancellations.
- The countermodel establishes logical sharpness relative to the retained
  inequalities, not a failure of the actual Balaban geometry.
- The result supplies only the physical auxiliary-\(J\) chain-rule summand.
  It does not supply the physical \(U\) pullback, prove
  \((\mathrm H_{\rm rc})\), construct nonzero-source polymer activities,
  compare with the unrestricted raw law, control large fields, iterate the
  RG, construct a continuum theory, prove the Osterwalder--Schrader axioms,
  establish infrared decay, or prove a Yang--Mills mass gap.
- No independent human review has been performed.

## Falsification checklist

- Use \(d_{\widetilde{\mathcal B}}(\widetilde q_{p,s},\widetilde y')\)
  in (17) without an endpoint hypothesis
  or coefficient-weighted substitute.
- Define \(d_{\widetilde{\mathcal B}}(\varnothing,\widetilde y')=+\infty\)
  and silently multiply its
  exponential by a zero chain density.
- Drop the source measure \(\mu(j',y')\), its inverse in Eq. (190), or the
  condition \(\gamma<\delta _0/8\).
- Replace the exact finite-dimensional direct-sum duality (21) by a claim
  about the full dual of infinite-dimensional \(\ell^\infty\).
- Sum pointwise coordinate bounds instead of the coordinate functionals and
  introduce a support-volume factor.
- Treat a coordinatewise Eq. (190) label choice as though it proved Note
  0019's global ownership/interface hypothesis.
- Call \((\mathrm H_{\rm end})\) logically minimal for every coefficient
  family rather than worst-case sharp for geometry-only control.
- Claim that (17) proves marked-plaquette-rooted locality, the physical
  \(U\)-summand, an unrestricted RG theorem, a continuum theory, or a mass
  gap.
