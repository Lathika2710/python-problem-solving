"""
Question: Write a program to get a number from the user and print whether the last two digits form a prime number.

Testcase:
Input: 359 -> Output: Prime
Input: 3577 -> Output: Not Prime
"""

n = int(input()) % 100
print("Prime" if n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1)) else "Not Prime")
