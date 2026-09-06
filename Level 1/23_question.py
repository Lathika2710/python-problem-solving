'''Question: Get a two-digit number from user and subtract 5 from that number if the sum of the
digits of the number is odd, then print the result. Do not use "if".'''

n = int(input())

tens = n // 10
ones = n % 10
sum = tens + ones 
print(n - 5 * (sum % 2))