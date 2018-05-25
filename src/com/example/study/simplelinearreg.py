# Importing Necessary Libraries
#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Validation using Scikit Learn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#plt.rcParams['figure.figsize'] = (20.0, 10.0)
import pickle
from  sklearn.externals import joblib
# Reading Data
data = pd.read_csv('C:/Users/nikhil.goyal/Desktop/itbodhi/LinerarRegdataset/headbrain.csv')
# Collecting X and Y
X = data['Head_Size'].values
Y = data['Brain_Weight'].values


list_pickle_path = 'simplelinear.pkl'


m = len(X)

#print(m)

X = X.reshape((m, 1))
# Model Intialization
reg = LinearRegression()
# Data Fitting
reg = reg.fit(X, Y)
# Y Prediction
Y_pred = reg.predict(X)
# Model Evaluation
rmse = np.sqrt(mean_squared_error(Y, Y_pred))
r2 = reg.score(X, Y)

#print("RMSE")
#print(rmse)
#print("R2 Score")
#print(r2)
#print("Pridiction value for Brain Weight:")
print("Brain Weight for Head Size 3777 would be:"+str(reg.predict(3777)))
print("for Head_Size: 3777 but actuall value is 1282 ")


# Create an variable to pickle and open it in write mode
list_pickle = open(list_pickle_path, 'wb')
pickle.dump(reg, list_pickle)
list_pickle.close()


# now you can save it to a file
joblib.dump(reg, 'filename.sav') 
print(joblib)
