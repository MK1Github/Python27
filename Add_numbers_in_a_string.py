a = "abcd1234efg567"
a=list(a)
count = 0
for i in range(len(a)):
    if a[i].isdigit():
        count = count + int(a[i])
print count



