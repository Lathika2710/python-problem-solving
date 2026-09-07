"""
Question: Get a number from user and check whether the sum of digits is 14, then print the result.

Testcase:
Input: 59 -> Output: Sum of Digits is 14
Input: 123 -> Output: Sum of Digits is not 14
"""

n = input()
print("Sum of Digits is 14" if sum(map(int, n)) == 14 else "Sum of Digits is not 14")
