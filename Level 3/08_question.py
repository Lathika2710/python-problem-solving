"""
Question: Get a number from user and check whether its digits are in ascending order.

Testcase:
Input: 1234 -> Output: Yes
Input: 5687 -> Output: No
"""

digits = input()
print("Yes" if all(a <= b for a, b in zip(digits, digits[1:])) else "No")
