"""
Question: Write a program to print the sum of all two-digit prime numbers.

Testcase:
Output: 1043
"""

print(sum(number for number in range(10, 100) if number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))))
