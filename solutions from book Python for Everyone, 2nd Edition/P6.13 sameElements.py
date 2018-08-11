
# P6.13 Comparing two lists

# coding: utf-8

# In[19]:

def helper_func(i_list, i_dict) :
    for i in range(len(i_list)) :
        k = i_list.pop()
        if k in i_dict :
            x = i_dict[k]
            x += 1
            i_dict[k] = x
        else :
            i_dict[k] = 1
    return i_dict


# In[20]:

def sameElements(a,b) :
    dictA = {}
    dictB = {}
    
    dictA = helper_func(a, dictA)
        
    dictB = helper_func(b, dictB)
    
    if len(dictA) != len(dictB) :
        return False
    else :
        for key in dictA.keys() :
            valA = dictA[key]
            if key not in dictB:
                return False
            else :
                valB = dictB[key]
                if valA != valB :
                    return False
    return True    


# In[21]:

keep_adding = True
listA = []
listB = []

while keep_adding :
    element = input("Enter the element in list A. To end the list, type 'end': ")
    if element == "end" :
        keep_adding = False
    else :
        listA.append(element)

keep_adding = True
while keep_adding :
    element = input("Enter the element in list B. To end the list, type 'end': ")
    if element == "end" :
        keep_adding = False
    else :
        listB.append(element)

print("List A: ", listA)
print("List B: ", listB)

list_match = sameElements(listA, listB)

if list_match :
    print("List A and List B match")
else :
    print ("List A and List B do not match")    




