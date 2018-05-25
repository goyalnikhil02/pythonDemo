import urllib
import requests
from bs4 import BeautifulSoup
list=[]
def getTextFromURL(url):
        page= urllib.request.urlopen(url).read().decode('utf8','ignore')
        soup=BeautifulSoup(page,"lxml")
        print(soup.find('article').text)
        list=soup.findAll('article')
        ##for elem in list:
        ##    print(elem.text)
        text=''.join(map(lambda p:p.text,soup.findAll('article')))
        #text.replace("was", "Nikhil")
        print(text)    
#textblob


articleURL="https://www.washingtonpost.com/news/morning-mix/wp/2018/03/09/she-said-she-killed-her-son-and-hid-him-in-a-manure-pile-the-truth-is-more-sinister-police-say/?utm_term=.be6124ae91c4"
getTextFromURL(articleURL)

articleURL2="https://www.washingtonpost.com/news/the-fix/wp/2018/03/09/did-trump-just-rush-into-negotiations-with-kim-jong-un-it-sure-looks-that-way/?utm_term=.e1555c5c7d4f"
getTextFromURL(articleURL2)
