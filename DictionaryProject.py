import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):
    if word in data:
        return data[word]
    elif word not in data:
        match = get_close_matches(word,data,3)
        print(match)
        choice = int(input("Did you mean 1, 2 or 3 ?"))-1
        print(choice)
        return data[match[choice]]

LookUp(word)