# Research roadmap

Status: exploratory

Chosen scaffold: Wilson lattice → gauge-covariant RG → local observables → OS reconstruction → nonperturbative infrared bridge → spectral gap

## Why this route

The Wilson regulator is finite-dimensional, compact, and exactly gauge invariant. Osterwalder–Seiler reflection positivity and Lüscher's transfer-matrix construction provide the right positivity/spectral scaffolding at nonzero lattice spacing. Bałaban's program supplies unusually deep ultraviolet control through gauge-covariant block transformations, localized effective actions, cluster expansions, coupling renormalization, and large-field analysis.

Those are ingredients, not the desired continuum theory. The missing core is to control renormalized local gauge-invariant observables through the running-coupling crossover and prove that the flow enters a volume-uniform massive regime while retaining all reconstruction and nontriviality properties.

## Scaling sanity check

If \(T_a\) is a lattice transfer matrix and \(\lambda_0,\lambda_1\) are its two leading spectral values, define

\[
m_{\mathrm{lat}}(a)=-\log(\lambda_1/\lambda_0),
\qquad
\Delta_{\mathrm{phys}}(a)=\frac{m_{\mathrm{lat}}(a)}{a}.
\]

A finite nonzero continuum gap requires \(m_{\mathrm{lat}}(a)=a\Delta+o(a)\). A fixed positive gap in lattice units at fixed bare coupling is not the Clay result; it normally describes a correlation length of order one lattice spacing and does not establish the required nontrivial continuum limit.

## Dependency chain

1. **One-block source theorem.** Track a local plaquette-energy insertion through one gauge-covariant RG block with volume-independent polymer bounds and large fields included.
2. **Iteration and composite fields.** Iterate on fixed physical volume and construct renormalized Schwinger distributions for \(\operatorname{Tr}F^2\), then a sufficient local gauge-invariant algebra.
3. **Continuum axioms and nontriviality.** Prove OS regularity/reflection positivity, Euclidean symmetry restoration, short-distance Yang–Mills behavior, and a nonzero interacting observable.
4. **New infrared bridge.** Prove the RG trajectory reaches a volume-uniform massive basin at the dynamically generated scale. This is the central unknown wall.
5. **Spectral transfer.** Use dense local states and physical-unit exponential decay to prove a finite positive Hamiltonian gap.
6. **Infinite volume and group scope.** Retain every property on \(\mathbb R^4\) and extend from the initial \(SU(2)\) construction to every compact simple group.

Each arrow needs its own theorem; no arrow is licensed by physical expectation.

## Route comparison

| Route | Rigorous asset | Blocking mismatch |
|---|---|---|
| Wilson/Bałaban RG | Gauge invariance, UV block analysis, localized expansions | No completed local-observable continuum construction or IR massive bridge |
| Continuum gauge-fixed constructive work | UV removal with a fixed IR cutoff in a restricted setup | IR cutoff, positivity, global gauge fixing, and gap remain |
| Stochastic quantization/heat flow | Strong modern constructions in three-dimensional gauge settings | Four dimensions is critical; invariant OS-positive pure-YM measure and gap are missing |
| Transfer matrix alone | Positive Hamiltonian framework at fixed lattice spacing | Positivity is not a continuum-uniform spectral gap |
| Strong-coupling/functional inequalities | Exponential mixing and gaps in strong-coupling lattice regimes | Bare continuum trajectory begins at weak coupling; no proved RG bridge |
| Large \(N\) / loop equations | Exact structures in special limits/regimes | Does not settle fixed \(N\), arbitrary compact simple \(G\), or interchange of limits |

## Kill criteria for the chosen route

Reassess rather than patch around the issue if:

- the proposed block map cannot preserve enough gauge invariance/locality to define composite observables;
- source counterterms proliferate without a controllable finite/relevant sector;
- large-field estimates necessarily grow with total volume;
- reflection positivity cannot be retained or recovered for the limiting observable theory;
- the running trajectory cannot be connected to any rigorously controlled massive basin;
- the resulting continuum limit is Gaussian, zero, topological, or has infinite rather than finite first mass.

The roadmap is a falsifiable research program, not a forecast of success.
