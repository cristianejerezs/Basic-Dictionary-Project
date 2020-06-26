import json
from difflib import SequenceMatcher

data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):

    error = "Sorry, i cant do this :c "
    print(data.get(word, error))

LookUp(word)

SequenceMatcher(None,"rainn",data.keys())
