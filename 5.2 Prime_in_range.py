#min=int(input("100:"))
#max=int(input("200:"))
min=100
max=200
for num in range(min,max):
    for x in range(2,num):
        if(num%x==0 and num!=1):
            break
        else:
            print(num,"is prime")
            break
