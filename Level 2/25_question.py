"""
Question: Write a program to get a number from the user and print the total number of single-digit prime numbers in the number.

Testcase:
Input: 163496481 -> Output: 1
Input: 364925 -> Output: 3
"""

print(sum(digit in "2357" for digit in input()))
