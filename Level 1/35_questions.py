"""
Question: Get two 3-digit numbers from user. Add the one's and hundred's digits of both numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits is bigger.

Testcase:
Input: 856, 978 -> Output: 24
Input: 128, 365 -> Output: 11
"""

a, b = map(int, input().replace(",", " ").split())
a_edge = a % 10 + a // 100
b_edge = b % 10 + b // 100
n = a if a_edge > b_edge else b
print(sum(map(int, str(n))))
