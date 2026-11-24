import re

# Three fictional formats for the same example number.
phones = ["054-123-4567", "054 123 4567", "(054)1234567"]
for phone in phones:
    clean = re.sub(r"\D", "", phone)
    print(clean)
