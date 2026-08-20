# Class 11 — Build an oTree Experiment with Codex, Part I

Today you will direct Codex to build a working decision-making experiment. The study has four lottery-choice trials and two feedback conditions. You will add it in small milestones, run it after every milestone, and inspect what changed.

## By the end of class

You should be able to:

- give Codex an authoritative experiment specification and clear project boundaries;
- ask for one bounded implementation milestone at a time;
- inspect a plan before allowing changes;
- verify a working oTree page in the browser;
- check that participant condition, trial order, and left-right presentation are stored correctly;
- compare persistent and transient sampling feedback;
- keep control of a larger project without writing every file yourself.

## Get the files for this class

1. [Download the Class 11 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-11-method-to-specification/class-11/class-11-files.zip).
2. Extract the ZIP file and locate the folder named `class-11`.
3. Move `class-11` into your local course folder, next to `class-00-setup` through `class-10`—not inside any of them.
4. Open `class-11/sampling-study` in VS Code. Open that same `sampling-study` folder as the Codex project.

Class 12 will continue from the project you build today. Keep this working folder.

## Prepare oTree

Run [`sampling-study/check_packages.py`](sampling-study/check_packages.py) in VS Code. The final lines should be:

```text
otree is ready: 6.0.15
requests is ready: 2.34.2
```

If either package is not ready, run [`sampling-study/install_packages.py`](sampling-study/install_packages.py), then run `check_packages.py` again. If installation reports an error, use the [package setup troubleshooting guide](sampling-study/package-troubleshooting.md).

## Rehearsal — strengthen one agent request

This request leaves the goal, boundaries, and evidence unclear:

> Build my experiment.

Before revealing an example, add one sentence that tells the agent:

1. where the requirements are;
2. how much it may build now;
3. what it must run or show before stopping.

<details>
<summary>Check one possible version</summary>

> Read the project Markdown files as the authoritative requirements. Implement Milestone 1 only, without adding later features. Show the diff, run the specified verification, and stop after reporting the result.

</details>

## Know the target

Open these files before sending any prompt:

| File | What it controls |
| --- | --- |
| [`EXPERIMENT_SPEC.md`](sampling-study/EXPERIMENT_SPEC.md) | What participants experience and how randomization works |
| [`DATA_CONTRACT.md`](sampling-study/DATA_CONTRACT.md) | What each saved trial row must mean |
| [`MILESTONES.md`](sampling-study/MILESTONES.md) | Which features belong in each build step |
| [`AGENT_RULES.md`](sampling-study/AGENT_RULES.md) | Project boundaries and verification rules |
| [`stimuli.csv`](sampling-study/stimuli.csv) | The four lottery pairs |

The experiment will eventually contain six milestones. Today you will complete Milestones 1–3. Class 12 will add timeout handling, automated tests, a clean export, and the final documentation audit.

## Activity 1 — ask for inspection before implementation

In Codex, select **Auto** and send:

> Read `AGENT_RULES.md`, `EXPERIMENT_SPEC.md`, `DATA_CONTRACT.md`, `MILESTONES.md`, `requirements.txt`, and `stimuli.csv`. Inspect the current folder and the installed oTree version. Do not edit anything yet. Report: (1) the files and pages you expect the finished project to contain, (2) exactly what Milestone 1 will add, (3) the commands or browser checks that will verify it, and (4) any conflict or missing decision that prevents implementation. Treat the supplied files as authoritative, do not add features, and stop for my approval.

Compare the response with `MILESTONES.md`. The plan should stop after one working trial; it should not promise conditions, automated bots, payments, recruitment, or deployment.

<details>
<summary>Check the boundaries of a sound plan</summary>

Milestone 1 should create the oTree project shell, one app, an instructions page, one sampling-and-choice trial based on `T01`, and a completion page. It should use the current no-`self` oTree style and run locally. Features assigned to later milestones should remain absent.

</details>

If the plan matches the milestone, send:

> The plan matches Milestone 1. Proceed with that milestone only.

## Activity 2 — build one complete trial

If Codex is waiting for a more explicit implementation request, send:

> Implement Milestone 1 exactly as defined in `MILESTONES.md`. Work only inside this folder. Use the first row of `stimuli.csv` as one fixed trial. The participant must reveal exactly five samples from each option before the two choice buttons become available. Save the sample counts, selected side, semantic choice, and response times. Add concise documentation for the file purpose and non-obvious timing or data decisions; do not comment obvious syntax. Run the package check and any safe oTree setup checks available without a browser. Show the diff and report the exact local command and page I should use for the manual pilot. Do not begin Milestone 2.

Review the changed files before running the project yourself. In VS Code, open a terminal in `sampling-study` and run:

```text
otree devserver
```

Open the local address shown in the terminal and complete the experiment once.

<details>
<summary>Check the Milestone 1 pilot</summary>

- The instructions page appears before the trial.
- The trial presents two lottery options.
- Each sample button stops after five samples.
- Choice buttons remain unavailable until both sample counts reach five.
- Choosing left or right reaches a completion page without an error.
- The oTree data page contains the selected side, semantic choice, both counts, and timing values.

</details>

Stop the local server with **Ctrl+C** before continuing.

## Activity 3 — expand to four randomized trials

Send:

> Read the current code, then implement Milestone 2 only. Load and validate all four rows from `stimuli.csv`. Give each participant all four trial IDs exactly once in a randomized order that remains stable across their rounds. Randomize whether Option A appears on the left or right on every trial and store both side mappings. Pre-generate and store the sample sequences so refreshing a page does not silently create different outcomes. Copy the participant-level trial assignment into each trial row needed by `DATA_CONTRACT.md`. Keep the Milestone 1 behavior working. Show the diff, run safe checks, and tell me exactly what to inspect in a four-trial manual pilot. Do not add feedback conditions, timeouts, bots, or custom exports yet.

Run `otree devserver` again and complete all four trials.

<details>
<summary>Check the Milestone 2 pilot</summary>

- Four decision trials appear before the completion page.
- Each trial uses a different `trial_id` from `T01` through `T04`.
- At least one trial can place Option A on a different side from another trial; identical sides by chance are not an error.
- Refreshing a trial does not change its stored trial identity, side mapping, or sample sequences.
- The saved rows record trial identity, lottery values, left-right mapping, samples, choice, and timing.

</details>

Stop the server before continuing.

## Activity 4 — add the two experimental conditions

Send:

> Read the current code, then implement Milestone 3 only. Add one participant-level condition with exactly two values: `persistent` and `transient`. Use `sampling_decisions` as the ordinary random-condition session config; assign one value when the participant starts and keep it for all four rounds. Add `sampling_decisions_persistent` and `sampling_decisions_transient` as forced configs. Under `persistent`, keep the complete sample history visible. Under `transient`, display only the newest outcome for 800 milliseconds, temporarily disable sampling while it is visible, then hide it and re-enable valid sampling buttons. Store the condition in every trial row. Preserve all Milestone 1–2 behavior, show the diff, run safe checks, and give me the exact manual checks for both forced configs. Do not add timeouts, bots, custom exports, payment, or deployment.

Start `otree devserver`. From the demo list, pilot both forced-condition session configs.

<details>
<summary>Check the two conditions</summary>

**Persistent:** each new outcome is added to the visible history for that option.

**Transient:** the newest outcome appears briefly, sampling is unavailable during that interval, and the outcome is then hidden.

For both conditions:

- the same condition remains attached to all four trial rows for one participant;
- five samples per option are still required;
- trial order, side mapping, choice, and timing remain stored.

</details>

## Before you leave

Your `sampling-study` folder should now contain a locally working oTree experiment with:

- four CSV-defined lottery trials;
- randomized trial order and left-right mapping;
- one stable participant condition;
- persistent and transient sampling feedback;
- five samples from each option before choice;
- trial-level choice, mapping, sequence, and timing data.

Keep the folder unchanged until Class 12. Do not delete the local database yet; it provides a useful record of today's pilot.

## Class 11 reference

| Term | Simple meaning |
| --- | --- |
| oTree project | The folder containing project settings and one or more experiment apps |
| App | One connected part of an oTree study, with its data fields, pages, and templates |
| Session config | A named way to start the study, including options used for a specific pilot |
| Participant field | Information stored once and reused across a participant's rounds |
| Round | One repeated instance of the app; here, one lottery-choice trial |
| Template | The HTML file that defines a participant-facing page |
| Semantic choice | The identity of the chosen option, `A` or `B`, independent of screen side |
| Milestone | One bounded, testable addition to the project |
| Manual pilot | Completing the study in a browser and inspecting what was stored |

## Additional guidance

The [official oTree installation guide](https://otree.readthedocs.io/en/latest/install.html) and [pages documentation](https://otree.readthedocs.io/en/latest/pages.html) provide more detail if you need to understand an oTree command or page structure used by the agent.
