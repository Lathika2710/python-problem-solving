"""
Question: Write a program to print the total number of single-digit prime numbers.

Assume 0 and 1 are not prime.

Testcase:
Output: 4
"""

print(sum(number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)) for number in range(10)))
