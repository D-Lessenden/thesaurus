import json 

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        message = f"'{word}' does not appear in our dictionary"
        return print(message)

word = input("Enter word: ")

print(translate(word))