import json
from autocorrect import Speller
from difflib import SequenceMatcher

data = json.load(open("076 data.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):
    if data.__contains__(word):
        return print(str(data[word]).strip("[]").replace("',","\n"))
    else:
        return print("Sorry, i couldn't find that word")

LookUp(word)