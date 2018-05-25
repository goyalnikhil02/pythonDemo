import numpy as np 
#from scipy.io.matlab.tests.test_mio import dtype

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
astudent = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print (astudent)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
dt = np.dtype([('name', np.unicode_, 16), ('grades', np.float64, (2,))])

x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)

print(x["name"])
print(x["grades"])

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")


x1 = np.array([(1,2.,'Hello'), (2,3.,"World")],
             dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])
print(x1['foo'])
print(x1['bar'])
print(x1['baz'])


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")