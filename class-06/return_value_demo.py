def classify_response_time(response_time):
    if response_time <= 1000:
        speed_label = "fast"
    else:
        speed_label = "slow"

    return speed_label


first_label = classify_response_time(850)
second_label = classify_response_time(1200)

print("First response:", first_label)
print("Second response:", second_label)
