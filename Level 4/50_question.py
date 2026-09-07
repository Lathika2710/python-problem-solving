"""
Question: Get two numbers of up to 50 digits, perform addition, and print the result.

IMPORTANT:
The numbers can contain up to 50 digits. Implement this safely using strings/arrays rather than relying on fixed integer limits.

Testcase:
Input: 123456789123456789, 987654321987654321
Output: 1111111111111111110
"""

first, second = input().replace(",", " ").split()
first_index = len(first) - 1
second_index = len(second) - 1
carry = 0
result = []

while first_index >= 0 or second_index >= 0 or carry:
    first_digit = int(first[first_index]) if first_index >= 0 else 0
    second_digit = int(second[second_index]) if second_index >= 0 else 0
    total = first_digit + second_digit + carry
    result.append(str(total % 10))
    carry = total // 10
    first_index -= 1
    second_index -= 1

print("".join(result[::-1]))
