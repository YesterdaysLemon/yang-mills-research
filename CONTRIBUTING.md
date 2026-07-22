# Contributing

The fastest useful contribution is a precise objection.

## Challenge a claim

Open a GitHub issue containing:

- the claim ID and proof anchor;
- the earliest step believed invalid;
- the missing hypothesis, counterexample, or incompatible source;
- severity S0–S3 under `GOVERNANCE.md`;
- whether downstream claims are affected.

Good-faith criticism remains public, including after correction. Security or private-data reports are the only normal exception.

## Propose mathematics

New claims must be added to `CLAIMS.json` and include exact scope, evidence level, dependencies, hypotheses, proof anchor, limitations, falsification tests, provenance, and review state. Do not label a restatement, numerical observation, or conditional bridge as a solution.

Use primary sources. Pin versions and map every imported theorem's hypotheses. Track regulator and volume dependence explicitly. Generated computations must be deterministic and carry their trust/error model. AI assistance must be disclosed and never entered as independent review.

## Pull-request checks

Run:

```text
python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

Mathematical review is still required after the metadata checks pass.
