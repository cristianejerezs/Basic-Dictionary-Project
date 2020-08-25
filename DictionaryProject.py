import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):
    if word in data:
        return data[word]
    elif word not in data:
        match = get_close_matches(word,data,1)
        return data[match[0]]

LookUp(word)