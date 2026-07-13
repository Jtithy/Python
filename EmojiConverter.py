# Author: Tithy
# Date: 2026-07-13
# Description: Implement emoji converter using dictionary mapping.

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)