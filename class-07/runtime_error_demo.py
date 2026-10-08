def points_to_bonus(points):
    """Return a bonus in pence at 10 pence per point."""
    return points * 10


participant_points = input("Points earned: ")

bonus = points_to_bonus(participant_points)
total_payment = 100 + bonus

print("Bonus (pence):", bonus)
print("Total payment (pence):", total_payment)
