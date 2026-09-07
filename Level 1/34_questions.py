"""
Question: Get two 3-digit numbers from user. Print the difference between the one's digit and hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit.

Testcase:
Input: 856, 978 -> Output: 1
Input: 128, 365 -> Output: 2
"""

a, b = map(int, input().replace(",", " ").split())
n = a if (a // 10) % 10 > (b // 10) % 10 else b
print(abs(n % 10 - n // 100))
