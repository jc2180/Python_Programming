
# coding: utf-8

# In[19]:

# P5.29 Facebook Reachable People

def reachablePeople(degree, averageFriendsPerUser) :
    total_people = 1
    for i in range(1, degree + 1) :
        total_people = total_people + (averageFriendsPerUser ** i)        
    return total_people
    
         


degree = int(input("Enter the degree of separation: "))
averageFriendsPerUser = int(input("Enter the average number of friends per user: "))
total_reachablePeople = reachablePeople(degree, averageFriendsPerUser)
print("Number of reachable people including the original user: ", total_reachablePeople)

