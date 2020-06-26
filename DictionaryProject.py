import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("DicData.json"))

word = str(input("Please input a word or vague description:").casefold())

def LookUp2(word):
    if data.__contains__(word):
        return print(str(data[word]).strip("[]").replace("',","\n"))
    elif not data.__contains__(word):
        count=0
        print("Did you mean?:")
        for i in get_close_matches(word,data.keys()):
            count+=1
            print(str(count )+i)
        correction = input("1,2,3: " )
        if data.__contains__(get_close_matches(word,data.keys())[int(correction)-1]):
            print(str(data[get_close_matches(word,data.keys())[int(correction)-1]]))
        elif not data.__contains__(get_close_matches(word,data.keys())[int(correction)-1]):
            print("Sorry, i can't do this :C")

LookUp2(word)
