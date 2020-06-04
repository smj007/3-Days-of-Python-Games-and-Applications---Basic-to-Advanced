import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decision = input("Press y for yes and n for no")
        if decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n":
            return("You have stepped on the wrong guy, I am leaving")
        else:
            return("You have entered a wrong word not from the options")


    else:
        print("You have not entered a valid word in the dictionary")


word = input("Enter the word to find meaning for")
output = translate(word)
if type(output) == list:
    for item in output:
        print (item)

else:
    print(output)
