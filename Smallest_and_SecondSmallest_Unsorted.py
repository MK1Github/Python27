

#Find second smallest element in an array without sorting


list1 = [12, 54, 22, 554, 67, 34, 1, 8, 2]
#list1 = [12, 54, 22, 67, 34, 2, 8, 1, 3]
#list1 = [12, 54, 22, 67, 34, 2, 1,1,8, 1, 3]
#list1=[]

if len(list1)==0 or len(list1)==1:
    print "Insufficient elements to compare. Need atleast 2."
else:
    smallest=list1[0]
    smallest2=list1[0]
    for item in list1:
        if item < smallest:
            smallest2=smallest
            smallest=item
        elif smallest2 != smallest and smallest2>item:
            smallest2=item
#print largest
    print smallest
    print smallest2



