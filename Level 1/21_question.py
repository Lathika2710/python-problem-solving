'''Question: Get a number from user and subtract 5 from that number if the number is odd, then
print the result. Do not use "if".'''

n = int(input())
print(n - 5 * (n % 2))