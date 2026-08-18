rating = int(input("Rating from 1 to 7: "))

is_in_range = rating >= 1 and rating <= 7

print("Rating is valid:", is_in_range)

if is_in_range:
    print("Rating accepted")
else:
    print("Please enter a number from 1 to 7")
