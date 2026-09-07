"""
Question: Add two integer arrays of up to 50 digits and store the result in a 51-digit array.

Testcase:
Input: [1, 2, 3], [4, 5, 6]
Output: [5, 7, 9]
"""

first = list(map(int, input().strip("[] ").split(",")))
second = list(map(int, input().strip("[] ").split(",")))
print([a + b for a, b in zip(first, second)])
