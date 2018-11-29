word = "aaadddkkkjjjdef"
word=list(word)
print word
#count =0
for w in word:
    if w not in word:
        count=1
    else:
        count=count+1
    print w,count


        
