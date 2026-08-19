def points_to_bonus(points):
    return points / 100


participant_points = "250"

print("Converting points")
bonus = points_to_bonus(participant_points)
print("Bonus:", bonus)
