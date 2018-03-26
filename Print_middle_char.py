# print middle character of a string
import math
str1="Amaon"
if (len(str1)%2==0):
    char1= len(str1)/2
    print str1[char1-1]+str1[char1]
else:
    char1=int(len(str1)/2)
    print str1[char1]



