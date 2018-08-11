
# P5.30 Validate Password

# coding: utf-8

# In[1]:

def validatePwd(pwd1) :
    if len(pwd1) < 8 :
        print("Incorrect Password Format. Password must be atleast 8 characters long")
        return True
    else :
        upperCase = 0
        lowerCase = 0
        digitValue = 0
        nonAlpha = 0
        for i in range(0, len(pwd1) - 1) :
            if pwd1[i].isdigit() == True :
                digitValue += 1
            elif pwd1[i] == pwd1[i].upper() :
                upperCase += 1
            elif pwd1[i] == pwd1[i].lower() :
                lowerCase += 1                
            
        if upperCase == 0 or lowerCase == 0 or digitValue == 0 :
            print("Incorrect Password Format. Password must have atleast one uppercase letter, atleast one lowercase letter and atleast one digit.")
            return True
        else :
            return False 
        
           


# In[4]:

pwd1 = input("Please Enter the new password: ")
re_enter = input("Please enter the new password again: ")
InvalidPassword = True
while InvalidPassword :
    if pwd1 != re_enter :
        re_enter = input("Passwords do not match. Please reenter the password: ")
    else :
        InvalidPassword = validatePwd(pwd1)
        if InvalidPassword :
            pwd1 = input("Please reenter the password: ")
            re_enter = input("Please enter the new password again: ")

print("The Password you have entered has been updated")
        
        




