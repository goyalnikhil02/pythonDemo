
'''
text="My name is nikhil"

saveFile=open('testingPython.txt','w')
saveFile.write(text)
saveFile.close()
'''

readData=open('testingPython.txt','r').readlines()
print(readData)