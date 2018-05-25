import numpy as np
import pandas as pd 

my_series = pd.Series( data = [2,3,3,4],             # Data
                       index= ['a', 'a', 'c', 'd'])  # Indexes


dict={"apple":'red',"banana":'yellow'}

print(dict.keys())

my_dict = {"name" : ["Joe","Bob","Frans"],
           "age" : np.array([10,15,20]),
           "weight" : [75,123,239],
           "height" : pd.Series([4.5, 5, 6.1], 
                                index=["Joe","Bob","Frans"]),
           "siblings" : 1,
           "gender" : "M"}
 
df=pd.DataFrame(my_dict)
print(my_dict)
my_hashmap=pd.Series(dict)
print(my_series)
print(my_hashmap)
print(my_series['a'])
