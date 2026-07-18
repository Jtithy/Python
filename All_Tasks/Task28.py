# Author: Tithy
# Date: 2026-07-16
# Description: Count the occurrences of each word in a sentence.

sentence = input("Enter a sentence: ")

#Split the sentence into words
words = sentence.lower().split()

word_count ={}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurences: ")
for word, count in word_count.items():
    print(f"{word}:{count}")