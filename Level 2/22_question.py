"""
Question: Write a program to get a number from the user and print the total number of two-digit odd numbers in the number.

Testcase:
Input: 12345678 -> Output: 3
Input: 987531 -> Output: 4
"""

digits = input()
print(sum(int(digit) % 2 for digit in digits if int(digit) >= 2))
