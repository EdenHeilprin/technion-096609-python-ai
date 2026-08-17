"""Class 0 setup check for Technion course 096609.

Students are not expected to understand this code before Class 1.
"""

import platform
import sys


system_name = platform.system()
display_system_name = "macOS" if system_name == "Darwin" else system_name
supported_python = sys.version_info[:2] == (3, 13)

print("Technion 096609 — Class 0 setup check")
print("Operating system:", display_system_name)
print("Python version:", platform.python_version())
print("Test calculation: 2 + 3 =", 2 + 3)

if supported_python:
    print("SETUP CHECK PASSED")
else:
    print("SETUP CHECK NEEDS ATTENTION")
    print("This course expects Python 3.13.x.")
    print("Select a Python 3.13 interpreter in VS Code and run this file again.")
