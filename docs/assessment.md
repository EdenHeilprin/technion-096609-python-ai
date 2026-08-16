---
layout: page
title: Assessment architecture
eyebrow: Evidence of competence
lead: AI remains available. Grades come from functioning artifacts, deliberate verification, reproducibility, explanation, and transfer—not from pretending assistance does not exist.
status: Working 20/30/40/10 model · Prototype tasks will be completed before weights are frozen
permalink: /assessment/
---

## At a glance

<div class="metric-grid">
  <article><strong>20%</strong><span>Weekly mastery</span><p>Best eight of approximately ten short core tasks, with correction opportunities.</p></article>
  <article><strong>30%</strong><span>Practical checks</span><p>Two individual, computer-based tasks requiring execution, debugging, and validation.</p></article>
  <article><strong>40%</strong><span>Capstone</span><p>A staged, normally paired, reproducible behavioral-science implementation.</p></article>
  <article><strong>10%</strong><span>Demonstration</span><p>A brief individual explanation, diagnosis, and bounded modification.</p></article>
</div>

This structure provides at least 60% directly individual evidence even when the capstone is completed in pairs. It avoids making one high-pressure event determine the course grade.

## Evidence triangle

| Evidence | What it establishes |
|---|---|
| **Product** | The code/data artifact works and is understandable |
| **Process and verification** | The student tested assumptions, used runtime evidence, handled errors, and checked consequential AI suggestions |
| **Explanation and transfer** | The student owns the work and can reason beyond the exact submitted version |

No single side is enough. A polished artifact alone may hide a misconception; confident explanation alone does not create a reproducible result; extensive process notes do not compensate for never testing the central behavior.

## Weekly mastery portfolio — 20%

- Approximately ten short required core tasks; best eight count.
- Public checks establish routine behavior without replacing human judgment.
- Required core and optional stretch remain visibly separate.
- At least one correction opportunity before a published cutoff.
- Exact files, run instructions, expected output, and privacy requirements are stated in advance.

Working rubric:

| Dimension | Share |
|---|---:|
| Functional specification | 50% |
| Understandable use of the week's core concepts | 25% |
| Output/edge-case checks and clean rerun | 20% |
| Submission and privacy contract | 5% |

## Individual practical checks — 30%

Each check is completed on a computer with the same normal AI and internet access described by course policy.

### Practical Check 1 — after debugging/testing

The working prototype provides a flawed but plausible behavioral-trial summary. In 75 minutes, students must:

- translate the requirements into a small plan;
- run the code and use the traceback/output as evidence;
- repair central defects;
- add a bounded adjacent behavior;
- create checks that would catch at least one plausible wrong result;
- submit a rerunnable artifact and concise verification explanation.

The check is followed by a 5–7 minute individual demonstration. The instructor selects a small tracing, diagnosis, or adjacent-change prompt; the same tools remain available. Passing a public checker is necessary but does not replace hidden synthetic cases or transfer evidence.

[Open the Practical Check 1 prototype](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/assessments/practical-check-1)

### Practical Check 2 — after pandas

Students receive a small synthetic CSV export and must:

- inspect and validate its schema;
- make specified transformations without changing the wrong rows;
- handle a meaningful missing/invalid case;
- produce a grouped summary or visualization;
- verify the result with counts, known cases, or invariants;
- rerun from the raw synthetic input.

The tasks reward effective programming evidence, not speed of syntax recall. Practical Check 1 remains a prototype until an instructor clean-room run and novice pilot confirm its timing and difficulty.

## Capstone — 40%

The capstone reproduces a bounded procedure and data contract from a published faculty method. Students do not recruit participants or claim to reproduce the statistical finding.

| Milestone | Share of capstone grade |
|---|---:|
| Method-to-specification brief | 10% |
| Thin vertical slice | 15% |
| Verification review | 15% |
| Final reproducible artifact | 60% |

Both the decision-making and OB pathways use a [common rubric](../capstone/).

## Individual demonstration — 10%

This is a short ownership and transfer check, not an oral examination designed to catch AI use. In approximately 8–10 minutes, each student:

1. explains one consequential design choice;
2. traces one small path through the project;
3. diagnoses a prepared defect or unexpected result;
4. makes or reasons through one bounded adjacent change.

The instructor may request a targeted follow-up when evidence shows a serious gap. Tool use itself is not the accusation or grading target.

## Baseline and endline — ungraded

The course uses isomorphic diagnostic tasks near the beginning and end to observe growth in:

- code-reading and prediction;
- data representation and state tracing;
- debugging strategy;
- ability to reject plausible but wrong AI suggestions;
- confidence, anxiety, and calibration.

AI remains permitted. Students briefly report whether and how they used assistance so the course can interpret the evidence honestly. The diagnostic does not lower grades and most beginners are not expected to complete the opening form.

[Open the baseline/endline diagnostic materials](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/assignments/baseline-endline)

## AI work note

Complete transcripts are not requested. When AI substantially affects a submission, a concise note is sufficient:

```text
Tools:
Purpose:
One consequential contribution:
How I verified it:
```

Routine autocomplete and trivial queries do not require item-by-item logging.

## Failure and recovery

- A non-running artifact cannot receive full functional credit, but clear diagnosis and useful checks may still earn partial credit.
- Weekly corrections are part of mastery rather than an exceptional favor.
- A privacy/security exposure requires immediate containment and a safe recovery path.
- A student who cannot explain a pair artifact supplies additional individual evidence rather than being automatically accused of misusing AI.

Exact late-work rules, minimum individual-evidence thresholds, and grade-replacement rules remain to be tested and published in the official Moodle syllabus.
