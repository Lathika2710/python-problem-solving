"""
Question: Print the total number of non-decreasing numbers from 1000 to 9999. A non-decreasing number has digits that do not decrease from left to right.

Example:
1234 is non-decreasing, whereas 2134 is not.

Testcase:
Output: 495
"""

print(sum(all(a <= b for a, b in zip(str(number), str(number)[1:])) for number in range(1000, 10000)))
