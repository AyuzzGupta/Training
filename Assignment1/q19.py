text = input("Enter a string: ")

count = {}

for ch in text:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

print("Character counts:")
for ch in count:
    print(ch, "->", count[ch])
