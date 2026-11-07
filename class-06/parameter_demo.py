def calculate_bonus(trial_points):
    """Return the bonus in pence for a list of trial points, at 10 pence per point."""
    # Start a fresh total for this participant.
    total_points = 0

    # Add each trial's points to the total.
    for points in trial_points:
        total_points = total_points + points

    # Convert the total to pence at 10 pence per point.
    bonus_pence = total_points * 10
    # Send the calculated bonus back to the code that called the function.
    return bonus_pence


# Call the same function with each participant's trial points.
first_bonus = calculate_bonus([3, 5, 2])
second_bonus = calculate_bonus([4, 1, 3])
third_bonus = calculate_bonus([2, 4])

# Display the returned bonuses.
print("First bonus (pence):", first_bonus)
print("Second bonus (pence):", second_bonus)
print("Third bonus (pence):", third_bonus)
