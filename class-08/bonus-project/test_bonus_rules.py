from bonus_rules import points_to_bonus


assert points_to_bonus(0) == 0
assert points_to_bonus(250) == 2.5
assert points_to_bonus(500) == 5

print("All bonus-rule tests passed")
