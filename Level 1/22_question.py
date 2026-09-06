'''Question: Get a number from user and subtract 5 from that number if the number's ten's position
digit is odd, then print the result. Do not use "if".'''

n = int(input())

tens = (n // 10) % 10
print(n - 5 * (tens % 2))