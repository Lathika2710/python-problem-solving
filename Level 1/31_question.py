'''Question: Get a three-digit number from user. If the sum of the digits is less than 10, then print
the sum, otherwise add the digits of the sum and continue until the result is a single digit.'''

n = int(input())

hundreds = n // 100
tens = (n // 10)% 10
ones = n%10
sum = hundreds + tens + ones
while sum >= 10:
    sum = (sum // 10 + sum % 10)
print(sum)