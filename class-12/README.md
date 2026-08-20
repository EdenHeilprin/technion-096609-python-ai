# Class 12 — Build an oTree Experiment with Codex, Part II

Continue the `sampling-study` project you built in Class 11. Today you will make it reliable enough to pilot and export: add timeout behavior, enforce data relationships, run automated oTree bots in both conditions, validate a trial-level export, and ask Codex for a final documentation and release audit.

## By the end of class

You should be able to:

- compare an existing project with its remaining milestones before editing;
- specify how incomplete and timed-out trials must be stored;
- direct Codex to add automated participant bots and run them in both conditions;
- generate and inspect a synthetic trial-level export;
- validate relationships between exported fields rather than checking columns by appearance;
- request useful documentation without changing working behavior;
- complete a final browser pilot and identify remaining limitations.

## Continue your Class 11 project

Open your existing `class-11/sampling-study` folder in VS Code and as the Codex project. Run `check_packages.py` once, then start `otree devserver` and confirm that one forced persistent session and one forced transient session still open correctly.

If your Class 11 project does not run after a reasonable debugging attempt, use the [tested Class 11 recovery checkpoint](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-12-experiment-slice/class-12/class-11-recovery-checkpoint.zip). Extract it, preserve your original folder under a different name, and continue in the checkpoint's `sampling-study` folder.

## Rehearsal — name the evidence

For each claim, decide whether the strongest immediate evidence is **browser behavior**, a **saved trial row**, or an **automated bot**:

1. A transient outcome disappears after 800 milliseconds.
2. The same condition is stored on all four rows for one participant.
3. A timeout never becomes a valid Option A or Option B choice.

<details>
<summary>Check the strongest evidence</summary>

1. Browser behavior: directly observe the outcome appearing and disappearing.
2. Saved trial rows: inspect the four stored condition values for one participant.
3. Automated bot: submit an explicit timeout and assert that side and choice are blank. Inspecting the resulting row provides a second check.

</details>

## Activity 1 — audit the current project before changing it

Stop the local server. In Codex, send:

> Read `AGENT_RULES.md`, `EXPERIMENT_SPEC.md`, `DATA_CONTRACT.md`, and `MILESTONES.md`, then inspect the complete current project without editing. Compare the current implementation with Milestones 4–6 only. Return a table with: required behavior, current evidence, missing or uncertain work, files likely to change, and the exact verification needed. Distinguish browser checks, bot checks, and export checks. Do not add requirements or begin implementation.

Check that the audit recognizes the current Class 11 experiment as the baseline. It should preserve the working four trials and two feedback conditions rather than propose a rewrite.

## Activity 2 — add timeout behavior and server-side integrity

Send:

> Implement Milestone 4 only. Add a 90-second decision-page timeout and `sampling_decisions_timeout_pilot` as a separate local session config that uses 2 seconds without creating a third experimental condition. For an ordinary completed trial, enforce on the server that both sample counts are exactly five and that the semantic choice matches the selected side. On timeout, set `timed_out` to true and clear selected side, semantic choice, `decision_rt_ms`, and `trial_rt_ms`; partial sample counts may remain. On ordinary completion, set `timed_out` to false. Make the final page report completed trials out of four. Preserve all Class 11 behavior. Add concise documentation for non-obvious integrity and timeout decisions, show the diff, run safe checks, and report exact manual pilot steps. Do not add bots or custom export yet.

Review the diff, then run `otree devserver`.

Pilot one ordinary forced-condition session and the 2-second timeout session.

<details>
<summary>Check Milestone 4</summary>

**Ordinary trial:** five samples from both options are required; the selected side and semantic choice agree; `timed_out` is false; both timing fields are present.

**Timeout trial:** the next page appears after about two seconds; `timed_out` is true; side, choice, and timing fields are blank; partial counts may remain.

The 2-second config is a local testing convenience. The normal experiment still uses 90 seconds.

</details>

Stop the server before continuing.

## Activity 3 — add automated pilots and the curated export

Send:

> Implement Milestone 5 only. Add oTree bots that cover: (1) ordinary valid left choices in all four rounds and (2) one explicit timeout while the other rounds complete normally. Run both cases under the forced persistent config and the forced transient config. Add a `custom_export` with exactly the 21 columns and field order in `DATA_CONTRACT.md`. Add an independent `validate_export.py` that accepts an exported CSV path, reloads it, and checks the contract's allowed values, four unique trials per participant, one condition per participant, left-right mapping, choice mapping, completed-row rules, timeout missingness, and valid sample outcomes. Generate synthetic exports, run the validator, show the diff, and report the exact commands and results. Do not change participant-facing behavior.

Review the bot submissions and the export validator rather than relying only on the completion summary. Run the exact test and validation commands reported by Codex yourself.

<details>
<summary>Evidence required for Milestone 5</summary>

- Both bot cases pass in both feedback conditions.
- The exported file has exactly the 21 columns in `DATA_CONTRACT.md`.
- Every synthetic participant has four trial rows and one condition.
- Ordinary rows contain counts, a valid side and matching semantic choice, and timing values.
- The timeout row has an explicit true timeout value and blank side, choice, and timing values.
- `validate_export.py` finishes successfully on the new export.

</details>

## Activity 4 — request documentation without changing behavior

Send:

> Implement Milestone 6 as a documentation and release-audit task. First explain the current project architecture and data flow from `stimuli.csv` through participant interaction to the curated export. Then improve documentation only where it reduces a reader's work: module and function docstrings, concise comments for randomization, stable sample sequences, timing, timeout clearing, choice mapping, bots, and export validation, plus a project README with setup, run, test, pilot, and export instructions. Do not narrate obvious syntax and do not refactor or rename working code. Show the documentation-only diff. Then run the complete package check, both forced-condition bot suites, export generation, and independent export validation. Report every command, result, and remaining limitation.

Inspect the diff before accepting it. Executable behavior should not change. Useful documentation should explain why a decision exists, what data move between parts, or how a claim is verified.

<details>
<summary>Reject documentation like this</summary>

```python
# Import random
import random

# Set the condition
player.condition = participant.condition
```

These comments merely repeat the syntax. A useful comment would explain why the participant-level assignment is copied into every trial row or why sample sequences are generated before rendering the page.

</details>

## Activity 5 — final pilot and data inspection

Run the project's documented verification sequence yourself. Then start `otree devserver` and complete one four-trial forced-condition pilot.

Before calling the project ready, inspect:

1. instructions, both feedback behaviors, sample limits, choice, timeout, and completion page;
2. one participant's four stored trial rows;
3. the curated export's columns and values;
4. the independent validator result;
5. the agent's list of remaining limitations.

The experiment is ready for a local synthetic pilot when all five checks agree. This class does not make it ready for real recruitment or public deployment.

## Before you leave

You should now have a functioning local oTree experiment that:

- assigns one of two feedback conditions per participant;
- presents four randomized, CSV-defined lottery trials;
- stores side mapping, sample sequences, counts, choice, timing, and timeout state;
- behaves correctly in both feedback conditions;
- passes ordinary and timeout bots;
- produces a validated 21-column trial-level export;
- contains documentation that helps a reader understand decisions and data flow.

## Class 12 reference

| Term | Simple meaning |
| --- | --- |
| Server-side validation | A rule checked by Python before submitted values are accepted |
| Timeout | The page ends without an ordinary choice after its allowed time |
| oTree bot | An automated participant that submits controlled values to pages |
| Forced session config | A local pilot configuration that selects one known condition |
| Custom export | A deliberately selected and ordered dataset produced from oTree records |
| Data-integrity check | A test of relationships between stored values, not only their individual types |
| Synthetic export | Data generated by test participants rather than real participants |
| Regression | An earlier working behavior that becomes broken after a later change |
| Release audit | A final comparison of requirements, implementation, tests, outputs, and limitations |

## Additional guidance

The official oTree documentation explains [participant treatments](https://otree.readthedocs.io/en/latest/treatments.html), [bots](https://otree.readthedocs.io/en/latest/bots.html), and [custom data exports](https://otree.readthedocs.io/en/latest/admin.html#custom-data-exports) in more detail.
