from bonus_rules import points_to_bonus


point_values = [250, 500, 750]

for points in point_values:
    bonus = points_to_bonus(points)
    print(points, "points ->", bonus, "bonus units")
