'''Question: Get a two-digit number from user and make the one's digit as 0, then print it.'''

n = int(input())
print(n - (n % 10))