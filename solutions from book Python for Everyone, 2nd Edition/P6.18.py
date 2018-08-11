
# P6.18 List Permutations

# coding: utf-8

# In[11]:

def list_permutation() :
    global list1
    global list2
    pos = random.randint(0,len(list2) - 1)
    last_element = list2.pop(pos)
    list1.remove(last_element)
    list1.append(last_element)
    return list1


# In[12]:

import random
list1 = [1,2,3,4,5,6,7,8,9,10] #permutation list
list2 = [1,2,3,4,5,6,7,8,9,10]  # second list

print("Permutation List: ", list1)
print("Second List: ", list2)
print("The ten permuatations of the permutation list are listed below from list 1 to list 10.")

for i in range(1,11) :
    newList = list_permutation()
    print("The List ", i, " is: ", newList)

    



