"""
Question: Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then print the sum, otherwise print the difference.

Testcase:
Input: 56, 78 -> Output: 22
Input: 14, 65 -> Output: 79
"""

a, b = map(int, input().replace(",", " ").split())
total = a + b
print(total if total < 100 else abs(a - b))
