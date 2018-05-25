from sklearn.feature_extraction.text import  TfidfVectorizer
vectorisation=TfidfVectorizer()
vectorisation.fit_transform(doxyDonkeyPosts)