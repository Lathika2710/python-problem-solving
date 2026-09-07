"""
Question: Write a loop program to print the two-digit odd numbers whose sum of digits is 7.

Testcase:
Output:
25
43
61
"""

for number in range(10, 100, 2):
    if sum(map(int, str(number))) == 7:
        print(number)
