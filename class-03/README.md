# Class 3 — Lists and Dictionaries

Today you will group related values in lists and dictionaries, retrieve individual values, update a record, and represent a small piece of behavioral-research data.

AI tools are permitted. For the rehearsal, try arranging the lines yourself before consulting the Class 2 materials or another tool.

## By the end of class

You should be able to:

- create a list and explain why its first item has index `0`;
- retrieve an item by its list index;
- use `len()` and `.append()` with a list;
- create a dictionary containing key-value pairs;
- retrieve and update a dictionary value using its key;
- choose whether a list or dictionary better represents a small collection of information.

## Get the files for this class

1. [Download the Class 3 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-03/class-03-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-03`. On Windows, it may appear inside an additional folder named `class-03-files`.
3. Move `class-03` into your local course folder, next to `class-00-setup`, `class-01`, and `class-02`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-03`.

If your course folder already contains `class-03`, you do not need to download it again.

## Rehearsal — put Class 2 in order

The following lines belong to one program, but they are not in the correct order:

```python
print(trials_completed * 5)
trials_completed = int(trials_text)
trials_text = input("Trials completed: ")
```

Create a new Python file inside `class-03` named `class_03_rehearsal.py`. Arrange the three lines so that the program:

1. asks for a number of completed trials;
2. converts the input into an integer;
3. displays the number of points when each trial is worth `5` points.

Predict the result for an input of `6`, then run the program.

<details>
<summary>Check one possible version</summary>

```python
trials_text = input("Trials completed: ")
trials_completed = int(trials_text)
print(trials_completed * 5)
```

For an input of `6`, the output is `30`.

</details>

## Two ways to group related values

Until now, most of our variables held one text or number value. Python also provides types that hold several related values.

| Type | Best fit | Example |
| --- | --- | --- |
| `list` | An ordered sequence of items | A sequence of conditions or stimuli |
| `dict` | Values identified by meaningful labels called keys | One participant or trial record |

Lists use square brackets. Dictionaries use curly braces.

## Lists use positions

```python
conditions = ["control", "treatment", "follow-up"]
```

The items remain in order. Each position has an **index**, and Python starts counting indices at `0`.

| Position in everyday language | Python index | Value |
| --- | ---: | --- |
| First | `0` | `"control"` |
| Second | `1` | `"treatment"` |
| Third | `2` | `"follow-up"` |

`conditions[0]` retrieves the first item. `len(conditions)` reports that the list contains three items.

## Activity 1 — retrieve values from a list

Open [`lists_demo.py`](lists_demo.py). Before running it, predict:

- the type Python will report;
- the first condition;
- the third condition;
- the number of conditions.

Run the file and compare the output with your predictions.

<details>
<summary>Check your predictions</summary>

```text
Type: <class 'list'>
First condition: control
Third condition: follow-up
Number of conditions: 3
```

</details>

Change the first condition from `"control"` to `"baseline"`. Predict which output line will change, save the file, and run it again.

## Activity 2 — add an item to a list

`.append(value)` adds one value to the end of a list. It changes the existing list.

Open [`stimuli_list.py`](stimuli_list.py). Before running it, predict the list and its length after this line executes:

```python
stimuli.append("triangle")
```

Run the file and compare the output with your prediction.

<details>
<summary>Check your prediction</summary>

The list changes from:

```text
['circle', 'square']
```

to:

```text
['circle', 'square', 'triangle']
```

Its new length is `3`.

</details>

Now make two deliberate changes:

1. replace `"triangle"` in the `.append()` line with a stimulus of your choice;
2. add another `.append()` line containing one more stimulus.

Predict the final list and its length before running the file again.

## Dictionaries use labels

A dictionary stores **key-value pairs**. Each key is a label that identifies its corresponding value.

```python
participant = {
    "code": "P014",
    "condition": "control",
    "trials_completed": 6,
}
```

| Key | Corresponding value |
| --- | --- |
| `"code"` | `"P014"` |
| `"condition"` | `"control"` |
| `"trials_completed"` | `6` |

The dictionary is named `participant`. The quoted labels inside it are its keys.

| Action | Code |
| --- | --- |
| Retrieve a value | `participant["code"]` |
| Update a value | `participant["trials_completed"] = 7` |
| Count the key-value pairs | `len(participant)` |

## Activity 3 — retrieve and update a record

Open [`participant_record.py`](participant_record.py). Before running it, predict the four lines of output.

Run the file, compare the output with your prediction, and identify the line that updates the trial count.

<details>
<summary>Check your prediction</summary>

```text
Participant: P014
Condition: control
Trials before update: 6
Trials after update: 7
```

</details>

Change the participant code, condition, and original number of completed trials. Then change the updated trial count. Predict and verify all four output lines.

## Activity 4 — build a small research record

Create a new Python file inside `class-03` named `session_record.py`.

Write a program that:

1. creates a list named `stimuli` containing `"circle"`, `"square"`, and `"triangle"`;
2. creates a dictionary named `session` with the keys `"participant_code"`, `"condition"`, and `"stimuli"`;
3. stores `"P021"`, `"treatment"`, and the variable `stimuli` as the corresponding values;
4. retrieves the stimuli list from the dictionary and assigns it to `stored_stimuli`;
5. displays the participant code, the first stimulus, and the number of stimuli.

The output should be:

```text
Participant: P021
First stimulus: circle
Number of stimuli: 3
```

Try to build and run the program before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
stimuli = ["circle", "square", "triangle"]

session = {
    "participant_code": "P021",
    "condition": "treatment",
    "stimuli": stimuli,
}

stored_stimuli = session["stimuli"]

print("Participant:", session["participant_code"])
print("First stimulus:", stored_stimuli[0])
print("Number of stimuli:", len(stored_stimuli))
```

</details>

Change the participant code and add a fourth stimulus. Predict which output lines will change, then run the file again.

## Class 3 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Collection | One value that groups several related values | A list or dictionary |
| `list` | An ordered collection accessed by numeric indices | `["circle", "square"]` |
| Item | One value inside a list | `"circle"` |
| Index | A numeric position inside a list; the first index is `0` | `stimuli[0]` |
| `len()` | Reports the number of items or key-value pairs | `len(stimuli)` |
| `.append()` | Adds one item to the end of a list | `stimuli.append("triangle")` |
| `dict` | A collection whose values are accessed through keys | `{"code": "P014"}` |
| Key | A label used to retrieve a dictionary value | `"code"` |
| Value | The information associated with a dictionary key | `"P014"` |
| Key-value pair | One key and its corresponding value | `"code": "P014"` |

### List or dictionary?

| Question | Prefer a list | Prefer a dictionary |
| --- | --- | --- |
| Does order or position identify each item? | Yes | Usually no |
| Does each value need a meaningful label? | Usually no | Yes |
| Example | A sequence of stimuli | One participant record |

### Read the brackets carefully

| Code | Meaning |
| --- | --- |
| `["control", "treatment"]` | Creates a list. |
| `conditions[0]` | Retrieves the first list item. |
| `{"code": "P014"}` | Creates a dictionary. |
| `participant["code"]` | Retrieves the value associated with the key `"code"`. |
| `participant["trials_completed"] = 7` | Updates the value associated with that key. |

### Follow the value

In Activity 4:

1. `stimuli` refers to a list.
2. The dictionary stores that list under the key `"stimuli"`.
3. `session["stimuli"]` retrieves the list.
4. `stored_stimuli[0]` retrieves the first item from that list.
5. `len(stored_stimuli)` reports how many items the list contains.

A useful representation question is: **Do I need an ordered sequence of items, or labeled information about one thing?**

## Companion tutorials

For a short review of each collection type:

1. **[Tracing lists | Intro to CS — Python — Khan Academy](https://www.youtube.com/watch?v=m9pvxuHb5y8)** (6 minutes) explains list creation, zero-based indices, retrieving items, and changing an item.
2. **[Dictionaries | Intro to CS — Python — Khan Academy](https://www.youtube.com/watch?v=nf26Yv5JTOc)** (4 minutes) explains key-value pairs, retrieving values by key, and updating a dictionary.

Together they reinforce the exact distinction used throughout this class: lists organize values by position, while dictionaries organize values by meaningful labels.
