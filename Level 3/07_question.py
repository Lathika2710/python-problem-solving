"""
Question: Get two numbers from user and compare them. If they are the same, print Same; otherwise print Not Same.

Testcase:
Input: 123, 123 -> Output: Same
Input: 56789, 12345 -> Output: Not Same
"""

a, b = input().replace(",", " ").split()
print("Same" if a == b else "Not Same")
