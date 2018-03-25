
str1="abc0"
str2="bc"
if str2 in str1*2:
    print "is"
else:
    print "no"

str1="abc0"
str2="c0ab"
for s in range (len(str1)):
    if (str2.startswith(str1[s:]) and str2.endswith(str1[:s])):
        print "is a rotation"