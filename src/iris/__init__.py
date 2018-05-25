import pandas as pd
df = pd.read_csv(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']
)

# store feature matrix in "X"
X = df.drop('class', axis=1).values

levels = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica':2}
# map 'class' column to numberic and store response vector in "y"
y = df['class'].map(lambda x: levels[x]).values



print(df)
# check the types of the features and response
print (type(X))
print (type(y))

# check the shape of the features
print (X.shape)

# check the shape of the response
print (y.shape)
       
       
       
       