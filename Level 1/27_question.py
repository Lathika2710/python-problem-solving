'''Question: Get a three-digit number from user. If the sum of the digits is 10 then print "Success",
otherwise print "Failure".'''

n = int(input())
hundreds = n // 100
tens = (n // 10)% 10
ones = n % 10
if hundreds + tens + ones == 10:
    print("Success")
else:
    print("Failure")


