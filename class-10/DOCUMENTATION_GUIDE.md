# Documentation guide

Documentation helps another person understand a program's purpose, inputs, outputs, and important decisions without reconstructing everything from syntax alone.

## Three useful forms

### Module docstring

A short description at the top of a Python file:

```python
"""Build checked analysis tables and a plot from decision-trial data."""
```

For a longer script, name its main input and outputs as well as its purpose.

### Function docstring

A concise contract immediately inside a function:

```python
def points_to_bonus(points):
    """Convert points to ILS using the study's fixed exchange rate."""
```

### Comment

A note beginning with `#` beside a decision that would otherwise be unclear:

```python
# Completion is defined by a recorded response time, not by positive points.
completed_mask = trials["response_time_ms"].notna()
```

## What useful documentation explains

- the purpose of a file or function;
- the data entering and leaving it;
- a research rule or assumption;
- why a verification step exists;
- a limitation that a reader could otherwise miss.

Do not add comments that merely translate obvious syntax, such as `# import pandas` or `# print the table`. Documentation should reduce the reader's work, not make the code longer without adding meaning.
