# reverse only words in sentence
i = input("Enter Sentence")
words = i.split()
rev = ""
for a in range(len(words)-1,-1,-1):
    rev=rev+" "+words[a]
print(rev)