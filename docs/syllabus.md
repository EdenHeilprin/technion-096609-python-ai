---
layout: page
title: Working syllabus
eyebrow: Course contract
lead: A practical introduction to Python for graduate behavioral-science students, with modern AI assistance treated as normal infrastructure rather than a prohibited shortcut.
status: Public development draft · Updated 17 August 2026 · Moodle will contain the final official version
permalink: /syllabus/
---

## Course identity

| Field | Working description |
|---|---|
| Formal catalog name | **Quantitative Models in Behavioral Sciences** / **מודלים כמותיים במדעי ההתנהגות** |
| Course number | 096609 |
| Actual instructional focus | Introductory Python, behavioral research workflows, and AI-assisted coding |
| Audience | Graduate behavioral-science students with zero or almost zero programming background |
| Prerequisites | No prior programming course required |
| Teaching language | Hebrew |
| Written materials and code | English |
| Planned format | 14 meetings of approximately two hours; the exact timetable is published in Moodle |
| Instructor | Eden Heilprin |

## Course promise

> **Assistance is normal. Understanding and verification remain yours.**

Students will learn enough foundational Python to write, read, trace, and debug small programs independently. They will also learn to direct modern AI chats and coding agents, inspect their changes, test their claims, and recover when generated code is plausible but wrong.

The course does not treat handwritten syntax recall as equivalent to programming competence. Every consequential coding assessment is completed on a computer.

## Learning outcomes

By the end of the course, a successful student can:

1. represent behavioral information using appropriate Python values, types, lists, and dictionaries;
2. read and explain beginner-level control flow, including conditions, loops, and changing program state;
3. decompose repeated behavior into functions with clear parameters and return values;
4. run programs in VS Code and make systematic debugging progress using tracebacks, intermediate output, assertions, and small tests;
5. read and write simple files and CSV data without silently corrupting the result;
6. use a focused set of pandas operations to inspect, validate, transform, summarize, and visualize behavioral data;
7. organize a small project so another person can reproduce its central output from a clean start;
8. translate a bounded research method into procedure logic, data contracts, acceptance criteria, and known limitations;
9. detect and repair at least one plausible-but-wrong AI-generated implementation;
10. use AI tools for explanation, planning, implementation, debugging, review, and documentation while remaining accountable for the final artifact;
11. explain and make a bounded adjacent change to submitted work;
12. recognize privacy, permission, bias, and reproducibility risks in research software.

## Supported working environment

The single supported classroom path is:

- VS Code;
- a current course-supported Python version;
- the VS Code Python and Jupyter extensions;
- Git and GitHub;
- pandas and a small documented package set;
- one free or institutionally funded AI baseline.

PyCharm and Spyder are legitimate alternatives, but the course cannot maintain three parallel troubleshooting paths without a teaching assistant. Required participation will not depend on purchasing an individual AI subscription. Tool-access details remain provisional while institutional options are being clarified.

## Learning rhythm

Most meetings follow the same loop:

> **Predict or trace → run → explain → modify → test → reflect**

Each week contains:

- two to four observable outcomes;
- at most one short required preparation resource;
- runnable in-class code;
- a required core task with exact checks;
- an optional stretch task;
- one deliberate AI-learning target;
- exact submission files and rerun instructions;
- a tested reference solution and correction route after submission.

## Working course map

| Meeting | Main focus | Primary evidence |
|---:|---|---|
| 1 | VS Code, GitHub orientation, first Python | Successful run, prediction, explanation, first self-check |
| 2 | Types, variables, strings, conversion, input/output | Small core program |
| 3 | Lists and dictionaries | Behavioral-data representation task |
| 4 | Conditions, validation, edge cases | Conditional task with explicit cases |
| 5 | Loops, counters, accumulators | Repeated-trial task and trace |
| 6 | Functions, parameters, return values, scope | Refactoring checkpoint |
| 7 | Tracebacks, assertions, debugging, tests | Individual executable practical check |
| 8 | Codex/agentic coding workshop, subject to access | Reviewed agent-assisted multi-file change |
| 9 | Paths, files, CSV, rerun safety, pandas introduction | File/data lab |
| 10 | Pandas transformations, summaries, basic visualization | Reproducible notebook or script |
| 11 | Experiment/survey architecture and capstone specification | Method-to-specification milestone |
| 12 | Integration studio | Capstone thin vertical slice; no major new topic |
| 13 | Clinic and rehearsal | Debugging, questions, recovery, demonstration preparation |
| 14 | Demonstrations, studio, catch-up, or contingency | Individual demonstration or remaining integration |

See the [expanded course map](../weeks/). Meetings 12–14 intentionally leave room for integration and recovery; they are not hidden extra chapters.

## Working assessment model

| Component | Weight | Evidence |
|---|---:|---|
| Weekly mastery portfolio | 20% | Best eight of approximately ten short core tasks, with correction opportunities |
| Individual practical checks | 30% | Two computer-based tasks that require execution, debugging, validation, and transfer |
| Behavioral-science capstone | 40% | Staged, normally paired, reproducible implementation using synthetic or approved pilot data |
| Individual demonstration | 10% | Brief explanation, tracing, diagnosis, and bounded modification |

These weights are the current prototyping baseline, not yet an official grading commitment. The design supplies at least 60% directly individual evidence even when the capstone is completed in pairs.

Read the [assessment architecture](../assessment/) for the rationale and current details.

## AI use and accountability

AI tools are permitted throughout the course, including graded work. There is no percentage limit on AI-generated code, no routine transcript requirement, and no planned use of AI-output detectors for grading.

Students remain responsible for:

- running the artifact and checking its actual behavior;
- explaining consequential behavior, assumptions, and limitations;
- constructing checks that distinguish plausible output from correct output;
- making or reasoning through an adjacent change;
- protecting confidential data and credentials;
- briefly describing substantive AI assistance and verification when requested.

Recommended professional workflow:

> **Specify → attempt → ask → inspect → predict → test → revise → explain → disclose**

See the [course policies](../policies/).

## Capstone

Students implement a bounded version of a published faculty method. “Replication” means reproducing the agreed procedure, logic, data contract, and expected outputs—not recruiting participants or claiming to reproduce the scientific finding.

Two Python-substantive pathways are being developed:

- **Decision-making experiment:** a functioning experimental procedure, potentially using oTree, with validated condition/stimulus logic and documented synthetic output.
- **OB survey + Python:** a Qualtrics protocol plus a reproducible Python pipeline for ingestion, schema validation, cleaning, scoring, quality checks, summaries, visualization, and export.

Both use the same common rubric. A Qualtrics form without the Python pipeline is insufficient; a page-based experiment without validated method and output logic is also insufficient.

See the [capstone page](../capstone/).

## Collaboration and revision

Discussion, peer explanation, and privacy-safe debugging help are encouraged. Unless work is explicitly paired, the submitted artifact and explanation remain individually accountable. Sharing a current private solution or another student's repository for copying is not acceptable.

Weekly mastery work normally permits correction before a published cutoff. Revision should respond to evidence: identify the failure, change the relevant part, rerun, and explain what now supports the result. Precise resubmission and late-work rules will be published in Moodle before the course begins.

## Privacy and research data

Course exercises and public repositories use synthetic or explicitly approved public data. Never place grades, student identity mappings, participant identifiers, credentials, confidential study material, hidden tests, or unreleased solutions in the public repository or an unapproved AI service.

When uncertain, use a structurally equivalent synthetic example and contact the instructor privately.

## Platforms and authoritative information

- **Moodle:** official announcements, dates, submissions, grades, private communication, and final policy versions.
- **Course website:** accessible view of the course journey, syllabus, policies, assessment, and roadmap.
- **GitHub repository:** versioned code, assignments, synthetic data, documentation, and public corrections.

If an official date differs, Moodle is authoritative. Please report the mismatch.

## Accessibility and support

Students should contact the instructor privately about accessibility needs, technical barriers, or circumstances that affect participation. Instructor-created video material should include captions or a text alternative; code is distributed as text rather than screenshots; links and instructions should remain usable without color alone.

A temporary zero-install route will protect the first learning meeting when local setup fails, while the longer-term supported environment remains local VS Code.

## Items still awaiting confirmation

- exact meeting duration and timetable;
- final weights, thresholds, resubmission, and late-work rules;
- course-wide AI/Codex/Copilot access;
- Qualtrics availability and oTree deployment route;
- final capstone papers and pair policy;
- official Moodle course-shell link;
- institutionally required syllabus language or outcomes, if any.

These are tracked on the [public development roadmap](../roadmap/). Until the official syllabus is posted in Moodle, this page is a transparent working design rather than a binding course regulation.
