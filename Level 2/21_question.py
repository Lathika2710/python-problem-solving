"""
Question: Write a program to get a number from the user and print the total number of digits that are odd.

Testcase:
Input: 12345678 -> Output: 4
Input: 987531 -> Output: 5
"""

print(sum(int(digit) % 2 for digit in input()))
