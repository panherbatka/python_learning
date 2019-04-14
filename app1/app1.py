import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Type a word: ")

def get_definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        answer = input("Did you mean %s instead? Type Y for yes or N for no: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if answer.lower() == "y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif answer.lower() == "n":
            return "OK, maybe you'll find desired word next time."
        else:
            return "Wrong answer picked"        
    else:
        return "Word doesn't exists. Please double check it."    

output = get_definition(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print(output)