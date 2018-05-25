import numpy as np 
from tensorflow.python.framework.dtypes import float64_ref


#dt = np.dtype([('name', int), ('grades', int)])
#x = np.array([[("goayk",1),("nikhil",2)]], dtype=dt)
#print(x)

#a=np.array(["TEXT", 1, 1], dtype='S, i4, i4') 
#print(a)


arr=np.array([[1,2,2],[3,2,2],[4,2,3]])
print(arr) 
print(arr.ndim) 
print(arr.itemsize)    

print(arr.dtype)     
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
         
floatarr=np.array([[1,2,2,1],[3,2,2,1],[4,2,3,2],[4,2,3,2]],dtype=np.int16)
print(floatarr)
print(floatarr.size)
print(floatarr.shape)
#print(floatarr.reshape(2,8))
print(floatarr.max())
print(floatarr.dtype)     
print(floatarr.itemsize)         


intarr=np.array([[1,2],[3,4],[5,6]])

print(intarr.sum(axis=0))

print(intarr.sum(axis=1))





arrayA=np.array([[1,2],[3,4]])
arrayB=np.array([[3,2],[6,2]])
print(arrayA+arrayB)

print(arrayA[0:1])


for cell in arrayA.flat:
    print(cell)
    
bool=arrayA>2
print(bool)    