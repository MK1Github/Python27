#s = raw_input()
s="asdjhdjkfghasdasddsfds"
d={}
for l in s:
    if l in d:
        d[l] +=1
    else:
        d[l] = 1
for key, value in reversed(sorted(d.iteritems(), key=lambda (k,v): (v,k))):
    print ("%s %s" % (key, value))