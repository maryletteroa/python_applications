# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 21:35:19
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 22:21:09


import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def get_keys():
    query = cursor.execute(f"SELECT Expression FROM Dictionary")
    keys = cursor.fetchall()
    return([k[0] for k in keys])

def get_defintions(word):
    query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{word}'")
    print(query)
    results = cursor.fetchall()
    return(results)


def translate(word):
    keys = get_keys()
    word = word.lower()
    if word in keys:
        definitions = get_defintions(word)
        return(definitions)
    elif word.title() in keys:
        definitions = get_defintions(word)
        return(definitions)
    elif word.upper() in keys:
        definitions = get_defintions(word)
        return(definitions)
    elif len(get_close_matches(word, keys)) > 0:
        word = get_close_matches(word, keys)[0]
        yn = input(f"Did you mean {word} instead? Enter Y if yes, or N if no. ")
        if yn == "Y":
            definitions = get_defintions(word)
            return(definitions)
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word=input("Enter the word: ")
results = translate(word)
if type(results) != str:
    for result in results:
        print(result[0])
else:
    print(results)


