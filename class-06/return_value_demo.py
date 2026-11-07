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


# Calculate and store each participant's bonus.
first_bonus = calculate_bonus([3, 5, 2])
second_bonus = calculate_bonus([4, 1, 3])

# Add the fixed participation fee to each returned bonus (all amounts in pence).
first_payment = 100 + first_bonus
second_payment = 100 + second_bonus

# Display the total payments outside the function.
print("First total payment (pence):", first_payment)
print("Second total payment (pence):", second_payment)
