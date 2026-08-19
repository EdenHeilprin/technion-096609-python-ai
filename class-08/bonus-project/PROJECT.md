# Bonus calculator project

This small project converts decision-making experiment points into bonus currency units.

## Files

- `bonus_rules.py` defines the conversion function.
- `run_bonus.py` applies the function to several point totals and displays the results.
- `test_bonus_rules.py` contains executable expectations for the function.

## Current rule

Every 100 points are worth 1 bonus unit. The current implementation has no maximum.

## Requested change

Introduce a maximum bonus of 5 units.

The completed change must satisfy all of these requirements:

1. Point totals below 500 keep their existing conversion.
2. Exactly 500 points return 5 bonus units.
3. Point totals above 500 also return 5 bonus units.
4. The name `points_to_bonus`, its `points` parameter, and the output labels in `run_bonus.py` remain unchanged.
5. The implementation uses familiar arithmetic, comparison, `if`, assignment, and `return` rather than a new shortcut.
6. The tests include an above-cap case using 750 points.
7. Both Python programs run successfully after the change.
