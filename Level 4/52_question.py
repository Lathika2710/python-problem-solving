"""
Question: Get a main string and a substring. Check whether the substring is present in the main string and print its position.

IMPORTANT:
Follow the position numbering shown in the testcase.

Testcase:
Input String: hellosurabee
Input Substring: sura
Output: 6
"""

text = input()
substring = input()
print(text.find(substring) + 1)
