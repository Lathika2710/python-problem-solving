'''Question: Get a four-digit number from user and only reverse the first two digits of the number,
then print the number.'''

n = int(input())

thousands = n // 1000
hundreds = (n // 100)%10
tens = (n // 10)%10
ones = n % 10

print(hundreds * 1000 + thousands * 100 + tens * 10 + ones)