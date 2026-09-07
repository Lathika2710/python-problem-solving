"""
Question: Write a program to get two numbers from the user and print the LCM of those numbers.

Testcase:
Input: 12, 18 -> Output: 36
Input: 15, 20 -> Output: 60
"""

from math import gcd
a, b = map(int, input().replace(",", " ").split())
print(abs(a * b) // gcd(a, b))
