# P7.12 common names for boy and girl in babynames.txt dataset

import os

def main() :
    working_dir = os.getcwd()
    filepath = working_dir + "\\babynames.txt"
    inputFile = open(filepath, "r")

    boySet = set()
    girlSet = set()
    for line in inputFile :
        dataFields = line.split()
     # Extract the individual field values.
        boySet.add(dataFields[1])
        girlSet.add(dataFields[3])
    nameSet = boySet.intersection(girlSet)

    print("The below listed names are for both boy and girl:")
    for name in nameSet :
        print(name)

    inputFile.close()
 
 # This program prints the common names between boy and girl
 # Read each file record and store the boynames in set boySet. Store each girl
 # name in set girlSet. Create a new set that is intersection of boySet and
 # girlSet. Print each name on a new line in this new set.

 # Start the program.
main()
