import json
from autocorrect import Speller
from difflib import SequenceMatcher

data = json.load(open("076 data.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):
    error = "Sorry, i cant do this"
    print(data.get(word, error))

LookUp(word)