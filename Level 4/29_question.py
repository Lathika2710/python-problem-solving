"""
Question: Print the largest four-digit prime number.

Testcase:
Output: 9973
"""

for number in range(9999, 999, -1):
    if number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        print(number)
        break
