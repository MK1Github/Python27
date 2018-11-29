
str1="te69568596fgfkjgfkj yyyyrtwerwe"
rev_str1=""
for s in str1:
    rev_str1=s+rev_str1
print rev_str1

def reverseSentence(Sentence):
    words = Sentence.split(" ")
    rev_words=words[::-1]
    rev_words=" ".join(rev_words)
    return rev_words
Sentence = "Reverse words in place for sentence"
print reverseSentence(Sentence)

def reverseWordinPlace(Sentence):
    words = Sentence.split(" ")
    rev_Words =[word[::-1] for word in words]
    rev_words = " ".join(rev_Words)
    return rev_words
Sentence = "Reverse words in place for sentence"
print reverseWordinPlace(Sentence)
