'''Question: Get a two-digit number from user and print the reverse of the number'''

n = int(input())
tens = n // 10
ones = n % 10
print(ones * 10 + tens)