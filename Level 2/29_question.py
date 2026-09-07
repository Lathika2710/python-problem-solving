"""
Question: Write a program to get three numbers from the user and print the LCM of those numbers.

Testcase:
Input: 2, 3, 4 -> Output: 12
Input: 4, 6, 8 -> Output: 24
"""

from math import gcd
a, b, c = map(int, input().replace(",", " ").split())
lcm = abs(a * b) // gcd(a, b)
print(abs(lcm * c) // gcd(lcm, c))
