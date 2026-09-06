'''Question: Get a three-digit number from user and make the ten's digit as 0, then print it'''

n = int(input())
hundreds = n // 100
ones = n % 10
print(hundreds * 100 + ones)