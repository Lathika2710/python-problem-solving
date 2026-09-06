'''Question: Get a two-digit number from user. If the sum of the digits is 10 then print "Success",
otherwise print "Failure".'''

n = int(input())
tens = n//10
ones=n%10
sum=ones+tens
if sum == 10:
    print("Success")
else:
    print("Failure")