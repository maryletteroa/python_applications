# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 20:25:08
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 21:16:54

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
        best_match = get_close_matches(word, data.keys())[0]
        yn = input(f"Did you mean {best_match} instead? Enter Y if yes, or N if no. ")
        if yn == "Y":
            return data[best_match]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)