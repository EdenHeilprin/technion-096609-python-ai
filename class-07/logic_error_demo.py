def calculate_bonus(points):
    bonus = points / 100

    if bonus >= 5:
        bonus == 5

    return bonus


ordinary_actual = calculate_bonus(250)
capped_actual = calculate_bonus(600)

print("Ordinary case — expected: 2.5 actual:", ordinary_actual)
print("Capped case — expected: 5 actual:", capped_actual)

assert ordinary_actual == 2.5
assert capped_actual == 5

print("All bonus tests passed")
