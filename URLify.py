#All the spaces between words should be replaced by %20
# leading and trailing spaces to be deleted.


def URLify(words):
    res=""
    words=words.strip() # Removes spaces at the start and at the end of the string
    print words
    for w in words:
        if w==' ':
            res+= '%20'
        else:
            res+=w
    print res
    res = ''.join(res)
    return res

print URLify ("    This!@ 34 %^ %20 is John Smith   ")


def urlifyString(str):
    res = []
    #start = False
    str = str.strip() # Removes white space from the beginning and end of the string
    print str
    for char in (str):
        if(char == ' '):
            res += '%20'
        else:
            res += char
        print res
    res = ''.join(res)
    return res

print urlifyString("       Mr John Smith           ")

