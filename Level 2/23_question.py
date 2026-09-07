"""
Question: Write a program to get a number from the user and print the total number of single-digit perfect square numbers in the number.

Testcase:
Input: 123456789 -> Output: 3
Input: 987531 -> Output: 2
"""

print(sum(digit in "0149" for digit in input()))
