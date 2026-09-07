"""
Question: Write a program to get a number from the user and print whether that number is prime or not.

Testcase:
Input: 31 -> Output: Prime
Input: 27 -> Output: Not Prime
"""

n = int(input())
is_prime = n > 1 and all(n % divisor for divisor in range(2, int(n ** 0.5) + 1))
print("Prime" if is_prime else "Not Prime")
