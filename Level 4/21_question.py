"""
Question: Write a program to print the total number of two-digit prime numbers.

Testcase:
Output: 21
"""

print(sum(number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)) for number in range(10, 100)))
