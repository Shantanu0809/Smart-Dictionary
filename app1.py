import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def check(w):
    return data[w]



def defination(wrd):
        wrd=wrd.lower()
        if wrd in data:
            return data[wrd]
        elif len(get_close_matches(wrd,data.keys())) > 0:
            confirm=input("\nDid you mean %s ? [Y/N]\t" % get_close_matches(wrd,data.keys())[0])
            confirm=confirm.lower()
            if confirm=='y':
                    return check(get_close_matches(wrd,data.keys())[0])
            elif confirm=='n':
                    return "\nWord not found"
            else:
                    return "\nDid not understand your query"
        else:
            return("\nWord not found. Please double check it")


word=input("\nEnter a word : ")
output=defination(word)
if type(output) is list:
    for item in output:
            print(item)
else:
    print(output)
