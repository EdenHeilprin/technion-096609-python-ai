def calculate_total_points(trials):
    total_points = 0

    for trial in trials:
        total_points = total_points + trial["points"]
        return total_points


trial_data = [
    {"choice": "left", "points": 4},
    {"choice": "right", "points": 10},
    {"choice": "left", "points": 1},
]

expected_total = 15
actual_total = calculate_total_points(trial_data)

print("Expected total:", expected_total)
print("Actual total:", actual_total)

assert actual_total == expected_total

print("All trial-point tests passed")
