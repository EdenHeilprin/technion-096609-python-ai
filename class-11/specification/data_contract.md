# Trial-level data contract

## Unit of observation

One row represents **one participant completing, or timing out on, one decision trial**.

## Required fields

| Field | Meaning | Stored type or values | Missing-value rule |
| --- | --- | --- | --- |
| `participant_code` | Anonymous participant label | Text such as `P001` | Never missing |
| `condition` | Option-order assignment | `sure_first` or `risky_first` | Never missing; constant within participant |
| `trial_id` | Identity of the decision problem | `T01`, `T02`, `T03`, or `T04` | Never missing; each appears once per participant |
| `display_position` | Position in that participant's randomized sequence | Integer from 1 through 4 | Never missing; each appears once per participant |
| `option_1` | Semantic option displayed first | `sure` or `risky` | Never missing; determined by `condition` |
| `selected_key` | Key pressed by the participant | `1` or `2` | Missing only when `timed_out` is `True` |
| `choice` | Meaning of the selected option, independent of screen position | `sure` or `risky` | Missing only when `timed_out` is `True` |
| `response_time_ms` | Time from option display to a valid response | Number greater than 0 and at most 12000 | Missing only when `timed_out` is `True` |
| `timed_out` | Whether no valid response was recorded within 12 seconds | `True` or `False` | Never missing |

## Relationships between fields

- `sure_first` requires `option_1` to be `sure`; `risky_first` requires it to be `risky`.
- Key `1` selects the value stored in `option_1`; key `2` selects the other option.
- A completed trial has a selected key, semantic choice, and response time.
- A timed-out trial has none of those three response values.
