"""
Question: Get a string of numbers up to 50 digits and remove all leading zeroes.

Testcase:
Input: 00000012345 -> Output: 12345
"""

print(input().lstrip("0") or "0")
