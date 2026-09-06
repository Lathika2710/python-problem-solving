'''Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is
greater than 10, then print "Success", otherwise print "Failure".'''

n = int(input())

hundreds = (n // 100)% 10
tens = (n //10)%10
if hundreds + tens > 10:
    print("Success")
else:
    print("Failure")