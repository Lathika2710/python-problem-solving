"""
Question: Write a program to print the total count of numbers less than 100000 whose sum of digits is 14.

Testcase:
Output: 4995
"""

print(sum(sum(map(int, str(number))) == 14 for number in range(100000)))
