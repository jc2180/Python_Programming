#P8.11 

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

print("Let's print the alphabet and the corresponding words from the file")
for key in dict1.keys():
    values = dict1[key]
    print("Words with the alphabet ", key, "are: ", end= "")
    print(values)
    




