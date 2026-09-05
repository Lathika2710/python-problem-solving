'''Question: Get a two-digit number from user and make the ten's digit 1, then print it'''

n = int(input())
ones = n % 10
print(10 + ones)