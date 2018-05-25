import nltk;
import pandas as pd
#import textmining

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
d1 = 'Sachin was one of the greatest cricket players who joined politics'
d2 = 'Atal Bihari was active in politics'
d3 = 'cricket and politics run in the blood of indians'
d4 = 'many cricket players join politics'

d = [d1,d2,d3,d4]



TfidfVec = TfidfVectorizer()
corpus=["It was the best of times",
"it was the worst of times",
"it was the age of wisdom",
"it was the age of foolishness"]

#textminingObj=textmining.TermDocumentMatrix()
#textminingObj.add_doc(corpus)


 # Let's print them to the screen.
#for row in textminingObj.rows(cutoff=1):
#    print(row)
    

 
countVector=CountVectorizer()

bag = countVector.fit_transform(corpus)
print(bag)
df = pd.DataFrame(bag.toarray(), columns=countVector.get_feature_names())
print(df)

#bag = countVector.fit_transform(corpus).todense()
print(bag.toarray())
