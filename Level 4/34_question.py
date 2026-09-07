"""
Question: Print the total number of palindrome numbers less than 100000.

Examples:
101, 12321, 656, 99899.

Testcase:
Output: 1098
"""

print(sum(str(number) == str(number)[::-1] for number in range(100000)))
