sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""
for word in words:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]
    result = result + reversed_word + " "

print("Reversed words:", result.strip())
