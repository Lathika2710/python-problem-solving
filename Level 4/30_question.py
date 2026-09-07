"""
Question: Print the largest eight-digit prime number.

Testcase:
Output: 99999989
"""

for number in range(99999999, 9999998, -1):
    if number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        print(number)
        break
