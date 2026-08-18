participant = {
    "code": "P014",
    "condition": "control",
    "trials_completed": 6,
}

print("Participant:", participant["code"])
print("Condition:", participant["condition"])
print("Trials before update:", participant["trials_completed"])

participant["trials_completed"] = 7

print("Trials after update:", participant["trials_completed"])
