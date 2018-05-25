import pandas as pd
#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


#df=pd.read_csv('E://BackUP//PraticeCode//DEMOPython//src//pandas//nyc_weather.csv')

#print(df['Temperature'])

#print(df[df['deaths']==62).__getattribute__('origin')


data=pd.read_csv('E://BackUP//PraticeCode//DEMOPython//src//pandas//house.csv')
print(data.info())
regressor = linear_model.LinearRegression()
predictors = data[["Square_Feet"]]
to_predict = data["Price"]

# Train the model using the training set
regressor.fit(predictors, to_predict)

# Check R-Squared
regressor.score(predictors, to_predict)

print(data['Price'].max())
#Equation coefficient and Intercept
print('Coefficient: \n', regressor.coef_)
print('Intercept: \n', regressor.intercept_)
predicted= regressor.predict(1000)
print(predicted)

plt.scatter(predictors,to_predict,color='blue')
#plt.plot(predictors,regressor.predict(predictors),color='red',linewidth=4)
plt.xticks(())
plt.yticks(())
plt.show()