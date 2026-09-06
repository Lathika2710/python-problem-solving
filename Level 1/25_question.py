'''Question: Get a four-digit number from user and subtract 5 from that number if ten's digit
position and hundred's digit position are the same, then print the result. Do not use "if"'''

n = int(input())

hundreds = (n // 100)%10
tens = (n // 10)%10

print(n-5*(hundreds == tens))