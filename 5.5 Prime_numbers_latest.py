import math
min=0
max=10
res=[]
def is_prime(num):
    if num<2:
        return False
    if num==2:
        return True
    for n in range(2,int(math.ceil(math.sqrt(num)))+1):
        if num%n==0:
            return False
    return True

for num in range (min,max):
    if is_prime(num):
        res.append(num)
        #print num, "is prime"
print res
