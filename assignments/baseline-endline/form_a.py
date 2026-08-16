"""Beginning-of-course diagnostic using synthetic behavioral data.

The program runs, but its reported mean does not match its stated intention.
"""

participant_code = "SYN_A01"
reaction_times_ms = [520, 480, 600, 550]
correct_responses = [True, False, True, True]

correct_rt_total = 0

for index in range(len(reaction_times_ms)):
    if correct_responses[index]:
        correct_rt_total = correct_rt_total + reaction_times_ms[index]

# Intended result: the mean reaction time for correct responses only.
mean_correct_rt_ms = correct_rt_total / len(reaction_times_ms)

print("Participant:", participant_code)
print("Mean correct RT (ms):", mean_correct_rt_ms)
