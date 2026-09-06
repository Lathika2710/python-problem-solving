'''Question: Get a three-digit number from user and make the one's digit as 2, then print it.'''

n = int(input())
hundreds = n // 100
tens = (n // 10) % 10
print(hundreds * 100 + tens * 10 + 2)