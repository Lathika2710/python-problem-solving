"""
Question: Write a program to print the biggest 4-digit number which is divisible by 7 and 9.

Testcase:
Output: 9954
"""

for number in range(9999, 999, -1):
    if number % 7 == 0 and number % 9 == 0:
        print(number)
        break
