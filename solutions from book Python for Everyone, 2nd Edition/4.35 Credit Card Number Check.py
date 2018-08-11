
# coding: utf-8

# In[51]:

# P4.35 Credit Card Number Check

cn = input("Enter the 8 digit card number: ")
if len(cn) != 8 :
    print("Invalid card number. The card number must be a sequence of 8 numbers")
else :
    alt_digit = False
    sum1 = 0
    sum2 = 0
    check_digit = int(cn[7])

    for i in range(len(cn) - 1, -1, -1) :
        cn_digit = int(cn[i])
        if alt_digit :
            dbl_digit = cn_digit * 2
            if (dbl_digit > 9) :
                dbl_digit = (dbl_digit % 10) + 1
            sum2 = sum2 + dbl_digit
            alt_digit = not alt_digit
        else :
            sum1 = sum1 + cn_digit
            alt_digit = not alt_digit

    T_sum = sum1 + sum2
    remainder = T_sum % 10
    if remainder == 0 :
        print("Card Number Is Valid")
    else :
        print ("Invalid Card Number")
        
        if (check_digit >= remainder) :
            check_digit = check_digit - remainder
        else :
            x = 10 - remainder
            check_digit = check_digit + x

        print ("The last digit on the card should be: ", check_digit)
    
   
