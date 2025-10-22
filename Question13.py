word=input("enter a word:")
index=len(word)-1
rev_word=""
while index>=0:
    rev_word+=word[index]
    index=index-1
print("Reversed word:",rev_word)
