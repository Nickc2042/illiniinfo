from illiniinfo.preprocessing import preProcessDoc
from illiniinfo.indexing import TF_IDF_Index, BM25_Index

passages=[]
TFIDFIndex=None
BM25Index=None

def buildIndexes(docs):
    global passages,TFIDFIndex,BM25Index
    
    passages=[]
    for doc in docs:
        passages.extend(preProcessDoc(doc))
    texts = [passage["text"] for passage in passages] # extract only the text

    if texts:
        TFIDFIndex = TF_IDF_Index(texts)
        BM25Index = BM25_Index(texts)
    else:
        TFIDFIndex = None
        BM25Index = None

def search(query,*,method="tfidf",top_k=5):
    rankedPassages = []

    if method not in ("tfidf","bm25"): # default case
        raise ValueError("The METHOD has to be EITHER TF_IDF OR BM25")

    if not isinstance(top_k,int) or isinstance(top_k,bool) or (top_k<1): # verify the # of requested results
        raise ValueError("The top_k has to be a POSITIVE integer")

    if not isinstance(query,str) or not query.strip(): # anything empty ignore
        return []

    if TFIDFIndex is None or BM25Index is None: # no searrching until docs have been indexed!
        return []


    # choosing algo based on what was passed
    if method == "tfidf":
        results = TFIDFIndex.search(query,top_k)
    else:
        results = BM25Index.search(query,top_k)

    for passageIndex, score in results:
        passage = passages[passageIndex].copy()
        passage["score"] =score
        rankedPassages.append(passage)

    return rankedPassages
    