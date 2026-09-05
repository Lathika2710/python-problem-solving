'''Question: Get a three-digit number from user and print the reverse of the number.'''

n = int(input())

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

print( ones * 100 + tens * 10 + hundreds )