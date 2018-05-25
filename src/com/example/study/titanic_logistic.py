import pandas as pd
#from  pandas import DataFrame as df
# get titanic & test csv files as a DataFrame
titanic_df = pd.read_csv("E:/BackUP/PraticeCode/DEMOPython/src/com/example/study/titanic/train.csv")
test_df    = pd.read_csv("E:/BackUP/PraticeCode/DEMOPython/src/com/example/study/titanic/test.csv")



print("777777777777777777777")
# preview the data
#print(titanic_df.head(5))
#print(titanic_df.info())

def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'Unknown'



def title_map(title):
    if title in ['Mr']:
        return 1
    elif title in ['Master']:
        return 3
    elif title in ['Ms','Mlle','Miss']:
        return 4
    elif title in ['Mme','Mrs']:
        return 5
    else:
        return 2    
    

titanic_df['title'] = titanic_df['Name'].apply(get_title).apply(title_map)
test_df['title'] = test_df['Name'].apply(get_title).apply(title_map)   

#to fidn the unique 
#df = pd.DataFrame(titanic_df)
#print(df.title.unique())
#print(titanic_df.info())
classandSur=pd.crosstab(titanic_df['Pclass'],titanic_df['Survived'])
print(classandSur)
title_xt = pd.crosstab(titanic_df['title'], titanic_df['Survived'])

#print(title_xt)