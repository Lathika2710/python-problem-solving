"""
Question: Write a program to get two numbers from the user and print the HCF of those numbers.

Testcase:
Input: 12, 18 -> Output: 6
Input: 24, 36 -> Output: 12
"""

from math import gcd
a, b = map(int, input().replace(",", " ").split())
print(gcd(a, b))
