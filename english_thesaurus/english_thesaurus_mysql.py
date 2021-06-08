# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-08 21:35:19
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-08 22:33:06


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
    results = cursor.fetchall()
    if results:
        return(results)
    else:
        return None


def translate(word):
    definitions = []
    cases = (word.lower(), word.title(), word.upper())
    for case in cases:
        definitions = get_defintions(case)
        if definitions:
            return definitions
        else:
            keys = get_keys()
            word = get_close_matches(word, keys)[0]
            yn = input(f"Did you mean {word} instead? Enter Y if yes, or N if no. ")
            if yn == "Y":
                definitions = get_defintions(word)
                return(definitions)
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
    return "The word doesn't exist. Please double check it."


word=input("Enter the word: ")
results = translate(word)
if type(results) != str:
    for result in results:
        print(result[0])
else:
    print(results)


