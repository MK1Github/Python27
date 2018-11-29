a=[34,12,22,6,18,78,88,7,87]
min=a[0]
max=a[0]
for i in range (len(a)):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
print "Max number in the list is ", max
print "Min number in the list is", min
