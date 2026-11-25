from sklearn.feature_extraction.text import TfidfVectorizer # making life easier and using scikit https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
import bm25s # github.com/xhluca/bm25s


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

# BM25 Index to build and query
class BM25_Index:
    def __init__(self,passages):
        self.passages = passages # store the original passages
        self.tokenizePassages = bm25s.tokenize(passages,show_progress=False)
        self.index =bm25s.BM25() # init bm25 index
        self.index.index(self.tokenizePassages,show_progress=False) # build bm25 index

    def search(self,query,top_k=5):
        queryTokens = bm25s.tokenize([query], show_progress=False) # tokenize query w/ same tokenizer as the passages
        
        k = min(top_k,len(self.passages))
        rankedIndexes,scores = self.index.retrieve(queryTokens,k=k,show_progress=False) # get top matching passage indices and respective bm25 scores

        results=[]
        for i, score in zip(rankedIndexes[0], scores[0]):
            if score>0:
                results.append((int(i), float(score)))


        # what's neat is bm25s already sorts and retrieves the top k results so we dont need to argsort
        return results




