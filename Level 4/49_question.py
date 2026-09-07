"""
Question: Write a function to convert an integer array into a character array and print it.

IMPORTANT: This question specifically requires a function.

Testcase:
Input: 1 4 5 8 7 6 3 -> Output: 1458763
"""

def array_to_characters(numbers):
    return "".join(map(str, numbers))

print(array_to_characters(map(int, input().split())))
