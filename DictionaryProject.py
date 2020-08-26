import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp(word):
    if word in data:
        return print(data[word])
    else:
        match = get_close_matches(word,data,3)
        print(match)
        choice = input("Did you mean 1, 2 or 3 ?")
        if int(choice)-1 <= 3:
            return print(data[match[choice]])
        else:
            return "Sorry, i cant help those who cant help themselves"

LookUp(word)

"""
import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp2(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data, cutoff=0.6)) > 0:
        choice = input("Did you mean %s instead??" % get_close_matches(word,data, cutoff=0.6)[0])
        if choice.casefold() == "yes":
            return str(data[get_close_matches(word,data,cutoff=0.6)[0]]).rstrip("[]')
        else:
            return "Sorry, please try again"
    else:
        return "Sorry, i can't find that word"

LookUp2(word)

get_close_matches()
"""