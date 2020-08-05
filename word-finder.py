import json                     # for loading the word_list
import re

def writeHook(num, hook):       # writes the hook
    return f"- num: {num}\n  link: {hook}\n"    


def createPattern(num):         # return a pattern
    conversion_list = []            # aids in creating the final_pattern
    i = 0
    while i < len(str(num)):
        conversion_list.append('[')
        conversion_list[i] += ''.join(translation_map[str(num[i])])
        conversion_list[i] += ']'
        i += 1

    pattern = '^'                   # holds the final pattern
    for s in conversion_list:
        pattern += '[aeiouxy]*'
        pattern += s

    pattern += '[aeiouxy]*$'
    return pattern


def searchForMatches(pattern, b):
    for word in words:
        isMatch = re.search(pattern, word)  # return a boolean if it's a match
        if isMatch:
            b.append(word)




file_name = "./words_dictionary.json"
words = []                      # a container for all the words
with open(file_name) as f:
    words = json.load(f)
# num = str(input('Enter A Number:' ))                          # for containing the seed number for words
translation_map = {             # translates numbers to letters
    '0': ['r'],
    '1': ['t', 'd'],
    '2': ['n'],
    '3': ['m'],
    '4': ['q', 'c', 'k'],
    '5': ['l'],
    '6': ['s', 'z'],
    '7': ['f'],
    '8': ['g', 'j'],
    '9': ['b', 'p', 'v', 'w'],
}                               # x, y are wild characters...

nlist = []
yaml = ""
with open('list.txt', 'w') as l:
    for value in range(210, 1000):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("--------------------------------------NEXT--------------------------------------")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        hold_options = []               # hold the matches in this list
        counter = 0
        searchForMatches(createPattern(str(value)), hold_options)
        for option in hold_options:
            print(f"{counter} - {option}")
            counter += 1
        n = int(input(f"Choose an Option for {value}: "))
        l.write(f"{str(n)}\n")
        try:
            yaml += writeHook(value, hold_options[n])
        except IndexError:
            yaml += writeHook(value, "NO_VALUE")

with open('vancamp.yml', 'w') as v:
    v.write(yaml)
