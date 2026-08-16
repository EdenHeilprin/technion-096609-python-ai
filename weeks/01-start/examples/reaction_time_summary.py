"""A first complete Python program using synthetic behavioral data."""

participant_code = "SYN001"
condition = "gain"

trial_1_ms = 480
trial_2_ms = 510
trial_3_ms = 510

mean_reaction_time_ms = (trial_1_ms + trial_2_ms + trial_3_ms) / 3

print("Participant:", participant_code)
print("Condition:", condition)
print("Mean reaction time (ms):", mean_reaction_time_ms)
