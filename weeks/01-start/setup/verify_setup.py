"""Small account-free setup check for Class 1."""

import platform
import sys


print("Python version:", sys.version.split()[0])
print("Operating system:", platform.system())
print("Test calculation:", (480 + 510 + 510) / 3)
print("SETUP CHECK PASSED")
