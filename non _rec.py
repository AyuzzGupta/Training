text = input("Enter a string: ")
count = {}

for ch in text.lower():
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

for ch in count:
    if count[ch] ==1:
        print(ch)
        break
    

