"""
Question: Print the total number of prime numbers below 1,000,000 whose sum of digits is equal to 14.

Example:
59 -> 5 + 9 = 14

Testcase:
Output: 1218
"""

count = 0
for number in range(2, 1000000):
    if sum(map(int, str(number))) == 14 and all(number % d for d in range(2, int(number ** 0.5) + 1)):
        count += 1
print(count)
