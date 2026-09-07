"""
Question: Write a program to get a number from the user and print the sum of all digits.

Testcase:
Input: 123456 -> Output: 21
Input: 76895439 -> Output: 51
Input: 675 -> Output: 18
"""

print(sum(map(int, input().lstrip("-"))))
