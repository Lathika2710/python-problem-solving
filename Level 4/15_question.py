"""
Question: Write a program to print the total number of two-digit odd numbers.

Testcase:
Output: 45
"""

print(sum(number % 2 for number in range(10, 100)))
