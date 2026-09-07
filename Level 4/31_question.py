"""
Question: Print the number of zeroes encountered between 0 and 1000.

This counts zeroes from 1 through 1000.

Testcase:
Output: 193
"""

print(sum(str(number).count("0") for number in range(1, 1001)))
