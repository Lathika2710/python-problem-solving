"""
Question: Print the smallest three-digit prime number.

Testcase:
Output: 101
"""

for number in range(100, 1000):
    if number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        print(number)
        break
