---
layout: page
title: Capstone
eyebrow: Final destination
lead: Reproduce a bounded implementation of a real behavioral method—without pretending to recruit participants or rerun the science.
status: Common architecture and rubric established · Papers and platform details remain open
permalink: /capstone/
---

## What “replication” means here

Students select an approved published faculty method and reproduce an agreed, bounded implementation of:

- the procedure or survey flow;
- consequential condition, stimulus, or scoring logic;
- the input/output data contract;
- central checks and expected synthetic outputs;
- setup and rerun instructions;
- known adaptations and limitations.

Students do **not** recruit participants, require new-data ethics approval, reproduce the statistical finding, or claim a complete scientific replication.

## Two comparable pathways

<div class="track-grid">
  <article><span>Track A</span><h3>Decision-making experiment</h3><p>Implement a functioning procedure—potentially in oTree—with condition/stimulus logic, randomization, validation, neutral feedback, synthetic pilot output, and a documented schema.</p></article>
  <article><span>Track B</span><h3>OB survey + Python</h3><p>Build the Qualtrics protocol and a reproducible Python pipeline for schema validation, cleaning, recoding/scoring, response-quality checks, summaries, visualization, and export.</p></article>
</div>

A Qualtrics form without its Python pipeline is insufficient. A Python experiment that displays pages but does not implement and validate the agreed procedure/data output is also insufficient.

## Shared milestones

| Milestone | Share of capstone grade | Required evidence |
|---|---:|---|
| Method-to-specification brief | 10% | Bounded scope, flow/behavior, data contract, exclusions, permission/source notes |
| Thin vertical slice | 15% | Smallest end-to-end path runs and creates/returns a valid example output |
| Verification review | 15% | Planned/executed checks, synthetic cases, known limitations, privacy review |
| Final reproducible artifact | 60% | Working project, clean-start instructions, complete outputs, code, checks, documentation |

## Common rubric

| Dimension | Weight |
|---|---:|
| Bounded specification and method fidelity | 15% |
| Functional artifact | 20% |
| Data contract and integrity | 15% |
| Verification and debugging evidence | 20% |
| Reproducibility and rerun safety | 10% |
| Code/project clarity | 8% |
| Documentation, decisions, and limitations | 7% |
| Privacy, permissions, and responsible AI use | 5% |

[Read the detailed common rubric](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/capstone/rubric.md)

## Pathway parity

| Common demand | Decision-making experiment | OB survey + Python |
|---|---|---|
| Procedure fidelity | Instructions, assignment, trials, timing/response logic, feedback | Introduction/consent flow, blocks, branching/display logic, response configuration |
| Functional artifact | Runnable experiment procedure | Runnable Qualtrics protocol **and** Python export pipeline |
| Data contract | Participant/session/trial schema and valid values | Raw schema, column mapping, derived variables, clean-output schema |
| Python substance | Application logic, randomization, validation, persistence/tests | Ingestion, schema checks, missingness, recoding/scoring, quality checks, summaries/export |
| Verification | Fixed seeds/test modes, condition counts, response cases, saved-row checks | Synthetic exports, known scores, missing/invalid cases, row/column preservation |
| Research output | Synthetic pilot rows with documented expected output | Synthetic export, cleaned/scored data, summary, useful visualization |

## Pair work and ownership

For a cohort of approximately 10–14, the working default is pairs. This yields five to seven projects and makes meaningful project review feasible for one instructor. Both partners remain responsible for the whole system—not only files they edited.

The capstone artifact/milestone grade is shared. Personal ownership is evaluated through the separate 10% individual demonstration: explanation, tracing, diagnosis, and a bounded adjacent change.

## Completion gates

The capstone is not complete until:

- one agreed central path runs end to end;
- a synthetic example output exists and is interpretable;
- clean-start rerun instructions exist;
- no known credential or identifiable/confidential-data exposure remains;
- both partners can access the submitted version;
- the work is ready for individual demonstration.

## What must be prototyped before papers are selected

The instructor should first build one generic thin vertical slice for each pathway. These prototypes establish the maximum feasible complexity, expected setup time, testing approach, output schema, and comparable Python substance. Candidate papers should then be selected against those tested constraints—not the other way around.
