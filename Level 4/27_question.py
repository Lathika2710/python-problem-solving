"""
Question: Print the largest three-digit prime number.

Testcase:
Output: 997
"""

for number in range(999, 99, -1):
    if number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        print(number)
        break
