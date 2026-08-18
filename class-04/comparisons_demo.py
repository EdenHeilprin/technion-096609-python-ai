trials_completed = 8
required_trials = 6
condition = "control"

enough_trials = trials_completed >= required_trials
exactly_required = trials_completed == required_trials
control_condition = condition == "control"
not_treatment = condition != "treatment"

print("Enough trials:", enough_trials)
print("Exactly required:", exactly_required)
print("Control condition:", control_condition)
print("Not treatment:", not_treatment)
print("Comparison type:", type(enough_trials))
