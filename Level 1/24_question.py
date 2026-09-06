'''Question: Get a three-digit number from user and subtract 5 from that number if one's digit and
hundred's digit are the same, then print the result. Do not use "if".'''

n = int(input())

hundreds = n // 100
ones = n % 10
print( n - 5*(hundreds == ones ))