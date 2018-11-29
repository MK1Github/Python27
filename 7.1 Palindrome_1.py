import string
my_str="rgdfgdf"
#my_str=my_str.casefold()
rev_string=reversed(my_str)
if list(my_str)==list(rev_string):
	print("This is a palindrome")
else:
	print("This is not a palindrome")


