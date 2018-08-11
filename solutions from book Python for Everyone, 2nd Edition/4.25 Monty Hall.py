
# coding: utf-8

# In[39]:

def hostSelectedDoor(choice1, choice2) :
    choice3 = random.randint(1,3)
    while (choice3 == choice1 or choice3 == choice2):
        choice3 = random.randint(1,3)
    
    return choice3
  
    


# In[40]:

import random

print("Lets play the Monty Hall Paradox game for 1,000 iterations") 
iterations = 1000
strategy1 = 0
strategy2 = 0 
for i in range(iterations):       
# choose a door to keep the car. The door is named as 'prize'
    prize = random.randint(1,3)
    
# Let the player choose a door. The door is named as 'player_choice'
    player_choice = random.randint(1,3)
    
# Let the host choose a door. This door will not be the same as door named 'prize' or door named 'player_choice'
# A function will be defined with name 'hostSelectedDoor'. Two parameters will be passed to this function. The
# first parameter will have door number that has the car (prize). The second parameter will be the door chosen by
# the player (player_choice)
    host_choice = hostSelectedDoor(prize, player_choice)
    
    
# Set a random variable that determines whether player switch the choice or stick to original selected door. If random
# variable value is 1, player sticks to original selected door. If randomly generated value is 2, player switch the door
    choice_switch = random.randint(1,2)
    
    if choice_switch == 2:
        switched_door = hostSelectedDoor(host_choice, player_choice)
        if switched_door == prize:
            strategy1 += 1
            
    elif  player_choice == prize:
        strategy2 += 1
        

        
        
print("Number of times player won by sticking to original choice" , strategy2)
print("Number of times player won by switching to the third choice" , strategy1)

        
            
        
    
    
        




# In[ ]:



