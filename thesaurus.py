import json 
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead of'{word}'? Enter Y for yes or N for no: ")
        response = response.lower()
        if response == "y":
            return data[get_close_matches(word, data.keys())[0]]   
        elif response == "n":
            message = f"Sorry, '{word}' does not appear in our dictionary."
            return print(message)
        else:
            return "Sorry, we didn't understand your entry"
    else:
        message = f"Sorry, '{word}' does not appear in our dictionary."
        return print(message)

word = input("Enter word: ")

output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)