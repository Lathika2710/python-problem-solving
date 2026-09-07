"""
Question: Write a program to print the total number of three-digit odd numbers.

Testcase:
Output: 450
"""

print(sum(number % 2 for number in range(100, 1000)))
