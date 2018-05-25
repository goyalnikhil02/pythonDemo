from sklearn.neighbors import  KNeighborsClassifier
from IPython.display import IFrame
IFrame('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', width=300, height=200)
from sklearn.datasets import load_iris
# save "bunch" object containing iris dataset and its attributes
iris = load_iris()
type(iris)
print(type(iris))
# print the iris data
print(iris.data)
#print(iris.target)
#print(iris.target_names)
#print(iris.DESCR)
#print(iris.feature_names)

x=iris.data
y=iris.target
print(x.shape)
print(y.shape)

knn=KNeighborsClassifier(n_neighbors=1)
print(knn)
