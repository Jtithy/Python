# Author: Tithy
# Date: 2026-07-14
# Description: Create a reusable emoji converter using functions.

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
    ":)" : "😊",
    ":(" : "😞"
}
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))