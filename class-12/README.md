# Class 12 — Build and Verify a Decision Experiment Slice

Class 11 ended with a specification for a small decision experiment. Today you will turn that specification into a working terminal prototype, run synthetic pilots, inspect the saved data, and verify that the result follows its contract.

## By the end of class

You should be able to:

- connect a build brief, data contract, program, tests, and saved CSV;
- explain why experiment logic is easier to test when it is separated from keyboard input and screen output;
- use a random seed to reproduce a condition assignment and trial order;
- preserve both a raw key press and its condition-dependent meaning;
- run a synthetic pilot from beginning to end;
- validate a saved output file independently of the program that created it;
- use Codex to implement one bounded change across several connected files;
- review the resulting diff and rerun the relevant evidence yourself.

## Get the files for this class

1. [Download the Class 12 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-12-experiment-slice/class-12/class-12-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-12`. On Windows, it may appear inside an additional folder named `class-12-files`.
3. Move `class-12` into your local course folder, next to `class-00-setup` through `class-11`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-12`.

If your course folder already contains `class-12`, you do not need to download it again.

## Rehearsal — recover the path from method to evidence

The five steps below are out of order. Put them in a sensible sequence before revealing one possible answer.

- build one thin end-to-end slice;
- define the data contract;
- inspect the method;
- validate the saved output;
- separate method facts, implementation decisions, and unresolved questions.

<details>
<summary>Check one possible sequence</summary>

```text
Inspect the method
    ↓
Separate facts, decisions, and unresolved questions
    ↓
Define the data contract
    ↓
Build one thin end-to-end slice
    ↓
Validate the saved output
```

A real project may revisit earlier steps, but it should not silently invent requirements or postpone all verification until the end.

</details>

## Four ideas to recognize

### 1. Separate the interaction from the experiment logic

[`run_experiment.py`](run_experiment.py) displays options, waits for keyboard input, and writes a CSV. [`experiment_core.py`](experiment_core.py) contains smaller functions that assign a condition, order trials, map a key to a choice, and build one output row.

The smaller core functions do not wait for a person. [`test_experiment_core.py`](test_experiment_core.py) can therefore call them with known inputs and check their outputs immediately.

| Part | Main responsibility |
| --- | --- |
| `run_experiment.py` | Coordinate one interactive session |
| `experiment_core.py` | Apply the experiment's rules |
| `test_experiment_core.py` | Check the rules with controlled examples |
| `validate_output.py` | Reload a saved pilot and check its data contract |

### 2. A seed makes a random path reproducible

The program needs random condition assignment and trial order. During development, we also need to reproduce a run that revealed a problem.

```python
rng = random.Random(seed)
condition = rng.choice(CONDITIONS)
rng.shuffle(ordered_trials)
```

Using the same seed with the same code produces the same pseudorandom sequence. Changing the seed gives the generator a different starting point. A fixed seed does not remove the randomization mechanism; it makes one generated path repeatable for testing.

### 3. Record the key and what the key meant

Key `1` selects the first displayed option. Under `sure_first`, that means `sure`; under `risky_first`, it means `risky`.

Saving only `selected_key` would make later analysis depend on reconstructing the display order. The output therefore stores all three:

- `option_1`: what appeared first;
- `selected_key`: what the participant pressed;
- `choice`: the semantic decision, `sure` or `risky`.

### 4. Validate the artifact, not only the running program

A program can finish without an error and still save incomplete or contradictory data. The validator reopens the CSV as a new input and checks its columns, rows, allowed values, missingness, and relationships.

That separation matters: the code that produces evidence should not be the only code trusted to judge that evidence.

## Read the build brief and contract

Open [`BUILD_BRIEF.md`](BUILD_BRIEF.md) and [`DATA_CONTRACT.md`](DATA_CONTRACT.md) before running the project.

Identify:

1. the method facts inherited from Class 11;
2. the newly resolved invalid-key behavior;
3. the known timing limitation of this terminal prototype;
4. what one saved row represents;
5. which fields are empty on a timeout.

<details>
<summary>Check the central distinctions</summary>

- Four trials, one condition per participant, condition-dependent option order, keys `1` and `2`, a 12-second limit, and one row per trial are method facts.
- Ignoring an invalid key while the original timer continues is a local implementation decision made for this prototype.
- Terminal `input()` cannot automatically stop at exactly 12 seconds. A blank Enter simulates no response; a response entered after 12 seconds is also stored as a timeout once input returns.
- One row represents one synthetic participant completing, or timing out on, one decision trial.
- `selected_key`, `choice`, and `response_time_ms` are empty on a timeout.

</details>

## Activity 1 — test and trace the experiment core

Open [`test_experiment_core.py`](test_experiment_core.py). For each test, name the requirement it checks before running the file.

Run it. A correct starting project prints:

```text
All experiment-core tests passed
```

Choose one test and trace its values into the matching function in [`experiment_core.py`](experiment_core.py). Explain why that test would be awkward if the same function also called `input()`.

<details>
<summary>Check one strong explanation</summary>

`test_key_mapping()` supplies known keys and option orders directly to `choice_from_key()`. It checks all four mappings immediately. If the function also waited for keyboard input, every test case would require a person to press a key and the test would no longer be automatic or reliably repeatable.

</details>

## Activity 2 — inspect reproducible randomization

Open [`inspect_seeds.py`](inspect_seeds.py). Predict:

1. whether the two runs using seed `12` will match;
2. whether seed `27` must match seed `12`;
3. whether every run should still contain all four trial identities exactly once.

Run the file and compare the three session plans.

<details>
<summary>Check the output</summary>

```text
Seed 12: condition=risky_first, order=['T01', 'T02', 'T04', 'T03']
Seed 12: condition=risky_first, order=['T01', 'T02', 'T04', 'T03']
Seed 27: condition=risky_first, order=['T04', 'T01', 'T02', 'T03']
```

The repeated seed produces the same condition and order. The different seed produces a different order in this example. All three plans still contain each trial exactly once.

</details>

Change only the final seed from `27` to `12` and rerun the file. Restore `27` before continuing.

## Activity 3 — run and validate two synthetic pilots

Open [`run_experiment.py`](run_experiment.py). Keep the initial participant code `P900` and seed `12`.

Run the program. On three trials, press `1` or `2`. On one trial, press Enter without typing a key to simulate no response. The program creates `output/P900.csv`.

Open the CSV and connect each column to [`DATA_CONTRACT.md`](DATA_CONTRACT.md). Then open [`validate_output.py`](validate_output.py), keep `PARTICIPANT_CODE = "P900"`, and run it. A valid pilot prints:

```text
File: P900.csv
Rows: 4
Condition: risky_first
All output checks passed
```

Now create a second pilot:

1. In `run_experiment.py`, change `PARTICIPANT_CODE` to `"P901"` and `RANDOM_SEED` to `27`.
2. Run all four trials, using only keys `1` and `2` this time.
3. In `validate_output.py`, change `PARTICIPANT_CODE` to `"P901"` and run it.
4. Run [`compare_pilots.py`](compare_pilots.py).

<details>
<summary>What should remain true across both pilots?</summary>

- Each CSV has exactly four trial rows.
- Each participant has one condition and each trial identity once.
- `option_1` follows the assigned condition.
- Every completed key maps to the recorded semantic choice.
- The simulated timeout in `P900` has no key, choice, or response time.
- `P901` has four completed rows.
- The trial orders may differ because the seeds differ.

</details>

## Activity 4 — propagate one research-relevant field with Codex

The program uses a seed but does not yet save it. Open [`FEATURE_REQUEST.md`](FEATURE_REQUEST.md), then open the `class-12` folder as a Codex project.

Begin in **Read only** and send:

> Read `FEATURE_REQUEST.md`, `DATA_CONTRACT.md`, `experiment_core.py`, `run_experiment.py`, `test_experiment_core.py`, and `validate_output.py`. Do not edit yet. Explain the smallest coherent change, file by file, and name the evidence that should pass afterward. Do not propose additional features.

Compare the plan with the feature request. It should update the contract, row construction, session coordinator, tests, and output validator—not merely add a column at the final `to_csv()` call.

Switch to **Auto** and send:

> Implement exactly `FEATURE_REQUEST.md`. Update only the six files named in my previous message. Preserve all other experiment behavior. Run `test_experiment_core.py` when finished and summarize the diff and test result.

Review the diff before accepting the result. Check that:

- `random_seed` appears immediately after `participant_code` in the contract and column order;
- every row receives the actual `RANDOM_SEED` used for that session;
- the tests check the new field;
- the validator requires an integer seed that is constant within the participant;
- no unrelated behavior changed.

Run `test_experiment_core.py` yourself. Then create a fresh pilot with participant `P902` and seed `44`, point `validate_output.py` to `P902`, and verify the new CSV.

<details>
<summary>Evidence of a complete implementation</summary>

- The core tests print `All experiment-core tests passed`.
- `output/P902.csv` contains `random_seed` as its second column.
- Every row in that file stores `44`.
- The output validator prints `All output checks passed`.
- Earlier CSV files created before the contract change do not gain the new column automatically; the new pilot is the current evidence.

</details>

## Class 12 reference

| Term | Simple meaning |
| --- | --- |
| Terminal prototype | A working text-based version used to test logic before building the eventual interface |
| Core logic | Rules that can run without waiting for screen or keyboard interaction |
| Session coordinator | Code that connects loading, display, input, logic, and saving in the required order |
| Pseudorandom | Generated by a repeatable algorithm while still behaving like random variation for this purpose |
| Random seed | The starting value used to reproduce one pseudorandom sequence |
| Reproducible run | A run whose condition and order can be generated again under the same code and seed |
| Synthetic pilot | A trial run using invented participant details rather than research data |
| Output validator | A separate program that reloads a saved artifact and checks its contract |
| Regression test | A check that protects behavior that already worked before a change |
| Field propagation | Carrying one value consistently from its source through code, saved data, tests, and validation |
| Known limitation | A documented behavior that the current prototype does not yet implement fully |

## Companion tutorial

Watch Indently's 2:44 **[Why Is `random.seed()` So Important In Python?](https://www.youtube.com/watch?v=-7I9ffz-kHk)**.

It demonstrates the central idea used in this class: a fixed seed makes a pseudorandom sequence repeatable. The video uses the module-level `random.seed()` function; our project uses `random.Random(seed)` to give this experiment its own generator without changing randomness elsewhere in a larger program.
