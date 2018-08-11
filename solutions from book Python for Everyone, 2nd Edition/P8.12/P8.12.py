#P8.12

import os

working_dir = os.getcwd()
filepath = working_dir + "\\words.txt"
input_file = open(filepath, "r")
dict1 = {}
for line in input_file :    
    words = line.lower().rstrip("\n").split(" ")
    for word in words :
        for i in range(len(word)):
            key = word[i]
            if key.isalpha() :
                if key in dict1 :
                    value = dict1[key]
                    value.add(word)
                    dict1[key] = value
                else :
                    value = set()
                    value.add(word)
                    dict1[key] = value
                
input_file.close()


user_input = str(input("Enter a word: "))
first_run = True
for i in range(len(user_input)):
    x = user_input[i]
    if x in dict1 :
        set1  = dict1[x]
    if not first_run:
        intersect_set = set1.intersection(set2)
        set2 = intersect_set.copy()
    else :
        first_run = False
        set2 = set1.copy()

print("The words from the file that contain all the input word letters: ")
if len(set2) == 0 :
    print("none of the words from the file has all the letters of input word")
else:
    print(set2)

    
