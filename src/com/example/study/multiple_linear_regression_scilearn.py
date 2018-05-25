import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('C:/Users/nikhil.goyal/Desktop/itbodhi/LinerarRegdataset/student.csv')
print(data.shape)
data.head()

math = data['Math'].values
read = data['Reading'].values
write = data['Writing'].values
m = len(math)


X = np.array([math, read]).T
print(X[0])
Y = np.array(write)

# Model Intialization
reg = LinearRegression()
# Data Fitting
reg = reg.fit(X, Y)
# Y Prediction
Y_pred = reg.predict(X)

# Model Evaluation
rmse = np.sqrt(mean_squared_error(Y, Y_pred))
r2 = reg.score(X, Y)

print("RMSE")
print(rmse)
print("R2 Score")
print(r2)

Nikhil=X.reshape(-1, 1)[0][0]
print(reg.predict([[79,80]]))