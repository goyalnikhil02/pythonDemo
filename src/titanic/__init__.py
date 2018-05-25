import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("E://BackUP//PraticeCode//DEMOPython//src//titanic//data//train.csv")
#print(titanic.info())
print("Tota No of Rows:" + str(titanic.shape[0]))
print("Tota No of Columns:" + str(titanic.shape[1]))
print(titanic.columns)
print(titanic["Sex"].value_counts())
print(titanic["Age"].unique())
# It will drop all rows where any column has missing values

# Fill Misisng values

mean_value = titanic['Age'].mean()
#titanic['Age']= titanic['Age'].fillna(mean_value)
#print(titanic['Age'])
 # Dataframe Subsetting : Selecting rows and columns

# Select PassengerId and Survived

#titanic[['PassengerId','Survived']]


# Selecting rows where Age>20 and Survived=1

#titanic[(titanic['Age']>20) & titanic['Survived']==1]

print(titanic["Ticket"][0:15])
print(titanic["Ticket"].describe())