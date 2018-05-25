import pickle
from sklearn.externals import  joblib 


list_unpickle = open('simplelinear.pkl', 'rb')

# load the unpickle object into a variable
#reg = pickle.load(list_unpickle)
#print(reg)
#print(reg.predict(3613))


clf = joblib.load('filename.sav')
print(clf.predict(3613))