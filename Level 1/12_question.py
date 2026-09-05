'''Question: Get a three-digit number from user and print sum the digits.'''

n = int(input())
print( n // 100 + (n // 10)%10 + n % 10)