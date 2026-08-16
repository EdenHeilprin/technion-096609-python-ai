"""End-of-course diagnostic using synthetic behavioral data.

This form has the same structure and difficulty as Form A, with different values.
"""

participant_code = "SYN_B01"
reaction_times_ms = [640, 510, 580, 490]
correct_responses = [False, True, True, False]

correct_rt_total = 0

for index in range(len(reaction_times_ms)):
    if correct_responses[index]:
        correct_rt_total = correct_rt_total + reaction_times_ms[index]

# Intended result: the mean reaction time for correct responses only.
mean_correct_rt_ms = correct_rt_total / len(reaction_times_ms)

print("Participant:", participant_code)
print("Mean correct RT (ms):", mean_correct_rt_ms)
