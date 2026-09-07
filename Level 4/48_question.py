"""
Question: Adjust the carry in an integer array. Convert a two-digit number into a single digit and add the carry to the previous position.

Testcase:
Input: 6 12 3 15 7
Output: 7 2 4 5 7
"""

digits = list(map(int, input().split()))
for index in range(len(digits) - 1, 0, -1):
    digits[index - 1] += digits[index] // 10
    digits[index] %= 10
print(*digits)
