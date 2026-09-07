"""
Question: Write a loop program to print the two-digit even numbers whose sum of digits is 6.

Testcase:
Output:
24
42
60
"""

for number in range(10, 100, 2):
    if sum(map(int, str(number))) == 6:
        print(number)
