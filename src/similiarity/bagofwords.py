import nltk;
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from string import punctuation

TfidfVec = TfidfVectorizer()
corpusData=["It was the best of times",
"it was the worst of times",
"it was the age of wisdom",
"it was the age of foolishness"]

data=[]

sent_tokens = nltk.sent_tokenize("My name is nikhil goyal. Please nikhil goyal telll me your name?")
word_tokens = nltk.word_tokenize("My name is nikhil goyal. nikhil Please tell me your name is ?")

for sentence in corpusData:
    #words=nltk.word_tokenize(sentence)
    data.append(nltk.word_tokenize(sentence)) 
print(data)    



#print(sent_tokens)


#stop_words=set(stopwords.words('english'))
#woutpuncstop=[words for words in word_tokens if  words not in stopwords.words('english') +list(punctuation)]

woutpuncstop=[words for words in word_tokens if  words not in list(punctuation)]
print(set(woutpuncstop))
print(len(set(woutpuncstop)))


countVector=CountVectorizer()
print(countVector)


bag = countVector.fit_transform(corpusData).todense()
print(bag)
