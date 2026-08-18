responses = ["left", "right", "left", "left"]
left_count = 0

for response in responses:
    if response == "left":
        left_count = left_count + 1

print("Left responses:", left_count)
