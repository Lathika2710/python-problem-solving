"""
Question: Get two numbers from the user and find their LCM.

Testcase:
Input: 20, 30 -> Output: 60
"""

from math import gcd
a, b = map(int, input().replace(",", " ").split())
print(abs(a * b) // gcd(a, b))
