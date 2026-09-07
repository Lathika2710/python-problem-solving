"""
Question: Write a program to print the sum of all three-digit prime numbers.

Testcase:
Output: 75067
"""

print(sum(number for number in range(100, 1000) if number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))))
