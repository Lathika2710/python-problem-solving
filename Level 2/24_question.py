"""
Question: Write a program to get a number from the user and print the total number of two-digit perfect square numbers in the number.

Testcase:
Input: 163496481 -> Output: 4
Input: 364925 -> Output: 4
"""

digits = input()
print(sum(digits[index:index + 2] in {"16", "25", "36", "49", "64", "81"} for index in range(len(digits) - 1)))
