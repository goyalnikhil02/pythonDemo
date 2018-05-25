

def example():
    variable=2
    sum=2+variable
    print(sum)
    print("Hi")
    
def summation(num2,num1):
    print(num2+num1)    


def sumList(list):
    sumvalue=0
    for element in list:        
        sumvalue=sumvalue+element
        print('currentSum:' ,sumvalue)
    print(sumvalue)

example()
summation(2,3)
list=[1,2,3,4]
print('>>>>>>')
sumList(list)






















'''def simple(num1,num2):
    pass
'''
def simple(num1,num2=5):
    print(num1,num2)
    

simple(2)
    
    
    
x=12
def data():
    global x
    print(x)
    x=x+5
    print(x)    
    
data()    

def done():
    pass
    

def meth():
    print('done')
    
print('nikhil')    
        