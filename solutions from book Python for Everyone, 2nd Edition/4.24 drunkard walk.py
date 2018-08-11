
# coding: utf-8

# In[20]:

def drunkardWalk(n):
    global x 
    global y
    for i in range(n):
        r = random.randint(1,4)
        # value of r generated randomly will determine the direction of the random walk
        if r == 1:  # random walk in north directions
            x += 0
            y += 1
            print("Random walk at: ", x, y)
        elif r == 2: # random walk in south direction
            x += 0
            y -= 1
            print("Random walk at: ", x, y)
        elif r == 3: # random walk in East direction
            x += 1
            y += 0
            print("Random walk at: ", x, y)
        elif r == 4: # random walk in West direction
            x -= 1
            y += 0
            print("Random walk at: ", x, y)
    return (x,y)
            


# In[21]:

import random
print("Lets implement the drunkard walk over 100 intersections") 
x = 0
y = 0
drunkardWalk(100)
print("The ending location is: ", x, y)
    
    


# In[ ]:



