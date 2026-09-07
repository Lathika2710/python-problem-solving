"""
Question: Write a program to print the total number of single-digit odd numbers.

Testcase:
Output: 5
"""

print(sum(number % 2 for number in range(10)))
