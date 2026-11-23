from sklearn.feature_extraction.text import TfidfVectorizer 
# making life easier and using scikit https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting

# TF IDF Index to build and query
class TF_IDF_Index:
    def __init__(self, passages):
        self.passages = passages # store passages so they can be retrieved AFTER ranking
        self.vectorizer = TfidfVectorizer() # init vectorizer to convert text into TF IDF vectors
        self.index = self.vectorizer.fit_transform(passages) # each row is a passage, each column is a term

    def search(self,query,top_k=5):
        queryVector = self.vectorizer.transform([query]) # turn a search query into a TF IDF vector
        scores = (self.index@queryVector.T).toarray().ravel() # calculate the cosine similarity between the query and every passage
        rankedIndexes = scores.argsort()[::-1] # sort the passages by rel score but with the highest FIRST!

        # return the top matching passages but excluding any zero scores
        results=[]
        for i in rankedIndexes:
            if scores[i] > 0:
                results.append((int(i), float(scores[i])))
            if len(results) >= top_k: # default case when having the necessary # of resutls
                break

        return results
