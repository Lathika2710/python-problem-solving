'''Question: Get a three-digit number from user. If the sum of the one's digit and hundred's digit is
less than 10, then print "Success", otherwise print "Failure".'''

n = int(input())

hundreds = n // 100
ones = n % 10
if hundreds + ones < 10:
    print("Success")
else:
    print("Failure")