"""
Question: Write a program to get a number from the user, print whether that number is prime, and check whether the sum of its digits is equal to 14.

Testcase:
Input: 59 -> Output: Prime & Sum of Digits is 14
Input: 77 -> Output: Not Prime but sum of digits is 14
Input: 13 -> Output: Prime, but sum of Digits is not 14
"""

n = int(input())
prime = n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
digit_sum = sum(map(int, str(n)))
if prime and digit_sum == 14:
    print("Prime & Sum of Digits is 14")
elif not prime and digit_sum == 14:
    print("Not Prime but sum of digits is 14")
elif prime:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime and sum of Digits is not 14")
