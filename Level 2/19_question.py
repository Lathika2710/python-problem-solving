"""
Question: Write a program to get a 4-digit number from the user and print whether the middle two digits form a prime number.

Testcase:
Input: 6359 -> Output: Not Prime
Input: 3517 -> Output: Prime
"""

digits = input()
n = int(digits[1:3])
print("Prime" if n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1)) else "Not Prime")
