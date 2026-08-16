# Common capstone rubric

Status: working rubric for prototype projects; the capstone is proposed as 40% of the course grade

## What the capstone demonstrates

The capstone is a bounded implementation replication of a published faculty method. It reproduces an agreed procedure, logic, data contract, and expected outputs using synthetic or explicitly approved pilot data. It does **not** require participant recruitment, ethics approval for new data collection, or reproduction of the paper's scientific finding.

Both pathways are assessed using the same dimensions. Platform-specific complexity is bounded so that neither track becomes the “easy option.”

## Milestones

| Milestone | Share of capstone grade | Minimum evidence |
|---|---:|---|
| Method-to-specification brief | 10% | Bounded scope, behavior/flow, data contract, exclusions, source/permission notes |
| Thin vertical slice | 15% | The smallest end-to-end path runs and creates/returns a valid example output |
| Verification review | 15% | Planned and executed checks, synthetic cases, known limitations, privacy review |
| Final reproducible artifact | 60% | Working project, clean-start instructions, complete outputs, code, checks, documentation |

Milestones are assessed as evidence of development, not as requests for AI chat transcripts.

## Common rubric

| Dimension | Weight | Meets the standard | Strong evidence beyond the standard | Not yet sufficient |
|---|---:|---|---|---|
| Bounded specification and method fidelity | 15% | Implements the agreed procedure/flow; consequential adaptations are explicit and justified | Turns ambiguous method text into precise, traceable decisions and acceptance criteria | Scope is undefined/too broad, or behavior departs from the agreed method without explanation |
| Functional artifact | 20% | Required end-to-end paths run and produce the intended behavior/output | Handles meaningful alternative paths and failures cleanly without unnecessary complexity | Central path does not run, depends on manual repair, or is only a mock-up |
| Data contract and integrity | 15% | Inputs, variables/fields, types, missingness, identifiers, and outputs are documented and handled consistently | Includes clear schema validation and safeguards against silent corruption or wrong-row transformations | Output cannot be interpreted reliably, schema assumptions are hidden, or data are silently altered incorrectly |
| Verification and debugging evidence | 20% | Uses deliberate checks for central behavior, edge cases, and plausible wrong results | Checks isolate failures well, cover consequential randomness/branching, and demonstrate recovery from a realistic defect | “It runs” is the primary evidence; checks are absent, cosmetic, or cannot detect a plausible error |
| Reproducibility and rerun safety | 10% | Another student can follow the README from a clean start and reproduce the example output | Setup is efficient, versions/dependencies are clear, and rerunning does not corrupt or duplicate outputs | Requires undocumented local state, absolute personal paths, secret manual steps, or unsafe reruns |
| Code/project clarity | 8% | Structure, names, functions, and comments support understanding; files have clear roles | Interfaces are especially coherent and complexity is well controlled | Project is unnecessarily tangled, duplicated, or difficult to trace even when it runs |
| Documentation, decisions, and limitations | 7% | README explains purpose, run steps, outputs, important choices, and known limits | Documentation makes the implementation auditable against the source method | Important choices/limits are missing or claims exceed what the artifact demonstrates |
| Privacy, permissions, and responsible AI use | 5% | Uses synthetic/approved data, respects public/private boundaries, and includes a concise AI work note when substantive | Anticipates realistic disclosure/licensing risks and documents safe alternatives | Contains unauthorized/private material, exposed secrets, misleading disclosure, or an unresolved high-risk practice |

## Pathway parity map

| Common demand | Decision-making experiment | OB survey + Python |
|---|---|---|
| Procedure fidelity | Instructions, condition assignment, trials, timing/response logic, feedback | Consent/introduction flow, blocks, branching/display logic, item and response configuration |
| Functional artifact | Runnable experiment procedure | Runnable Qualtrics protocol **and** Python export pipeline |
| Data contract | Participant/session/trial output schema and valid values | Raw export schema, column mapping, derived variables, cleaned output schema |
| Core Python substance | Application logic, randomization, validation, persistence/tests | Ingestion, schema checks, missingness, recoding/scoring, quality checks, summaries/export |
| Verification | Fixed seeds/test modes, condition counts, input/response cases, saved-row checks | Synthetic exports, known scale scores, missing/invalid cases, row/column preservation checks |
| Research output | Synthetic pilot rows and documented expected output | Synthetic survey export, cleaned/scored data, summary, useful visualization |
| Reproducibility | Clean experiment setup and run instructions | Clean pipeline run from raw synthetic export to final outputs |

A Qualtrics form without the Python pipeline is insufficient. A Python experiment that displays pages but does not implement and validate the agreed procedure/data output is also insufficient.

## Minimum completion gates

Regardless of the weighted score, a capstone is not complete until:

- one agreed central path runs end to end;
- a synthetic example output is produced and interpretable;
- clean-start rerun instructions exist;
- no known credential or identifiable/confidential-data exposure remains;
- both partners, when applicable, have access to the submitted version;
- the work is ready for the separate individual demonstration.

If a gate is missing at the deadline, the recovery process should target that gate directly rather than require an unrelated replacement project.

## Pair work and individual ownership

The artifact and milestone grades are normally shared by the pair. Both partners are responsible for the entire system rather than only the files they edited. Repository history and a concise division-of-work note help coordinate and diagnose imbalances but are not used as a simplistic line-count score.

Individual understanding is evaluated separately through the 10% course demonstration: explanation, tracing, diagnosis, and a bounded adjacent change. When individual evidence shows a serious ownership gap, the instructor may request a targeted follow-up rather than automatically accusing or penalizing AI use.

## AI work note

One note per milestone/project version is enough:

```text
Tools:
Purpose:
One consequential contribution:
How we verified it:
```

Do not submit complete transcripts unless a specific conversation is voluntarily included as evidence of an important decision and contains no private material.
