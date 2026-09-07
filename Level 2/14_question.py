"""
Question: Write a program to get a number from the user and interchange the first and last digits, then print the result.

Testcase:
Input: 123456 -> Output: 623451
Input: 76895439 -> Output: 96895437
Input: 675 -> Output: 576
"""

digits = input()
print(digits[-1] + digits[1:-1] + digits[0])
