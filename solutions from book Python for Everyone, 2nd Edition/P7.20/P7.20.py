import os

def encrypt_input(input_text, key) :
	pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	#key = 'FEATHRZYXWVUSQPONMLKJIGDCB'
	encrypted_text = ""
	for ch in input_text : 
		if ch.isalpha() :
			formatted_text_index = pattern.index(ch)
			formatted_text = key[formatted_text_index]
			encrypted_text += formatted_text 
		else :
			encrypted_text += ch
	return encrypted_text 


def decrypt_input(input_text, key) :
    pattern = key
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ""
    for ch in input_text :
        if ch.isalpha() :
            formatted_text_index = pattern.index(ch)
            formatted_text = key[formatted_text_index]
            decrypted_text += formatted_text
        else :
            decrypted_text += ch
    return decrypted_text 



def generate_key(input_keyword) :
    rev_AtoZ = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    keySet = set()
    input_keyword.upper()
    key = ""
    for ch in input_keyword :
        if ch not in keySet :
            keySet.add(ch)
            key += ch

    for ch in rev_AtoZ :
        if ch not in keySet :
            key += ch

    return key
            


invalid_input = True
input_keyword = str(input("Enter the keyword: (ex: FEATHER) "))
while invalid_input :    
    if input_keyword.isalpha() :
        invalid_input = False        
    else :
        input_keyword = str(input("Enter the correct alphanumeric keyword. No special characters allowed.(ex: FEATHER): "))


input_func = str(input("Enter the encrypt (E) or decrypt(D) function: (E or D) "))

working_dir = os.getcwd()
filepath = working_dir + "\\encrypt.txt"

input_file = open(filepath, "r")
output_file = open("output.txt", "w")

key = generate_key(input_keyword)

if input_func == 'E' :
    for line in input_file :
        #print(line)
        #input_text = input_file.readline().upper()
        input_text = line.upper()
        #print(input_text)
        encrypted_text  = encrypt_input(input_text, key)
        #print("encrypted_text: ", encrypted_text)
        output_file.write(encrypted_text)
    print("Encryption successful : The encrypted file is output.txt")
   
elif input_func == 'D' :
    for line in input_file :
        input_text = line.upper()
        decrypted_text  = decrypt_input(input_text, key)
        output_file.write(decrypted_text)
    print("Decryption successful : The decrypted file is output.txt")
    
else :
    print("The function value is incorrect. Please re run and enter the correct E / D value")

    

input_file.close()
output_file.close()







 
