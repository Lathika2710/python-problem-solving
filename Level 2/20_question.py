"""
Question: Write a program to print the total number of single-digit prime numbers.

Testcase:
Output: 4
"""

print(sum(number > 1 and all(number % d for d in range(2, int(number ** 0.5) + 1)) for number in range(10)))
