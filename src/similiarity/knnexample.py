from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from time import time
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier

users = {"Gaurav": {"Bahubali2": 3.5, "Half-Girlfriend": 2.0, "Kaabil": 4.5, "Raees": 5.0, "Sultaan": 1.5, "Dangal": 2.5, "Piku": 2.0},
         "Somendra":{"Bahubali": 2.0, "Half-Girlfriend": 3.5, "Sarkaar3": 4.0, "Raees": 2.0, "Sultaan": 3.5, "Piku": 3.0},
         "Paras": {"Bahubali2": 5.0, "Half-Girlfriend": 1.0, "Sarkaar3": 1.0, "Kaabil": 3.0, "Raees": 5, "Sultaan": 1.0},
         "Ram": {"Bahubali2": 3.0, "Half-Girlfriend": 4.0, "Sarkaar3": 4.5, "Raees": 3.0, "Sultaan": 4.5, "Dangal": 4.0, "Piku": 2.0},
         "Tomar": {"Half-Girlfriend": 4.0, "Sarkaar3": 1.0, "Kaabil": 4.0, "Dangal": 4.0, "Piku": 1.0},
         "Atul":  {"Half-Girlfriend": 4.5, "Sarkaar3": 4.0, "Kaabil": 5.0, "Raees": 5.0, "Sultaan": 4.5, "Dangal": 4.0, "Piku": 4.0},
         "Sumit": {"Bahubali2": 5.0, "Half-Girlfriend": 2.0, "Kaabil": 3.0, "Raees": 5.0, "Sultaan": 4.0, "Dangal": 5.0},
         "Diwakar": {"Bahubali2": 3.0, "Kaabil": 5.0, "Raees": 4.0, "Sultaan": 2.5, "Dangal": 3.0}
        }


#print(users["Gaurav"])
  


def manhattanApproach(user1,user2):
    
    distance=0
    commonRating=False
    for key1 in user1:
       if key1 in user2:
           distance += abs(user1[key1] - user2[key1])
          # print(distance)
           commonRating=True
           
    if(commonRating):
        return distance
    else:
        return -1
           
           
print(manhattanApproach(users['Gaurav'],users['Atul']))
## calculate the distance with other members with the given user
def manhattanApproachNearestNeighbour(inputuser):
    Listdistance=[]
    for user in users:
        if user!=inputuser:
         distance = manhattanApproach(inputuser, user)
         Listdistance.append(((distance,user))
         #distance.append((distance,user))


##print("Done")


#print(manhattanApproach(users['Gaurav'],users['Atul']))  
#print(manhattanApproach(users['Paras'], users['Sumit']))  

#print(manhattanApproachNearestNeighbour(users['Gaurav']))

