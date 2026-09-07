"""
Question: Get a string and a character from the user. Find all positions where the character is present and print them.

IMPORTANT:
Follow the position numbering shown in the testcase.

Testcase:
Input String: hellohellohello
Input Character: h
Output: 1, 6, 11
"""

text = input()
character = input()
print(", ".join(str(index + 1) for index, value in enumerate(text) if value == character))
