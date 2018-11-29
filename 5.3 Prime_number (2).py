x=1
if (x > 1):
    for i in range(2,x):
        if (x%i)==0:
            print "This is not a prime number"
            break
    else:
        print "This is a prime number"
else:
    print "This is a not a prime number"

