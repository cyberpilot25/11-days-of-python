#code to identify if word is present in search text
def search(text, word):
    words = text.split()
    if word in words:
        return("Word found")
    else:
        return("Word not found")

text = input()
word = input()

print(search(text, word))