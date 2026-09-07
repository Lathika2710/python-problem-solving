"""
Question: Write a program to print the total number of three-digit prime numbers.

Testcase:
Output: 143
"""

print(sum(number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)) for number in range(100, 1000)))
