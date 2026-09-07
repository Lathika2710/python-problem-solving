"""
Question: Print the smallest four-digit prime number.

Testcase:
Output: 1009
"""

for number in range(1000, 10000):
    if number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        print(number)
        break
