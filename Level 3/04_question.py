"""
Question: Get a number from user and check whether it is prime or not, then print the result.

Testcase:
Input: 61 -> Output: Number is Prime
Input: 1200 -> Output: Number is not Prime
"""

n = int(input())
prime = n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
print("Number is Prime" if prime else "Number is not Prime")
