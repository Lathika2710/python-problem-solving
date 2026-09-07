"""
Question: Get a string and check whether it is a valid number.

Testcase:
Input: 1234567 -> Output: Valid Number
Input: 12abc35 -> Output: Not a Valid Number
"""

print("Valid Number" if input().isdigit() else "Not a Valid Number")
