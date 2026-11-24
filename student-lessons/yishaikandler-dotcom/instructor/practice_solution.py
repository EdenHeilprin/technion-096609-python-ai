# Exercise 1: Remove spaces at both ends.
response = "  study group  "
clean = response.strip()
print(repr(clean))  # Expected: 'study group'

# Exercise 2: Standardize the capitalization.
response = "GEMINI"
clean = response.lower()
print(repr(clean))  # Expected: 'gemini'

# Exercise 3: Remove each exclamation mark.
response = "yes!!!"
clean = response.replace("!", "")
print(repr(clean))  # Expected: 'yes'

# Exercise 4: Combine all three steps.
response = "  CHATGPT!!!  "
clean = response.strip().lower().replace("!", "")
print(repr(clean))  # Expected: 'chatgpt'
