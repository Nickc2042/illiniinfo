from illiniinfo.preprocessing import preProcessDoc
from illiniinfo.indexing import TF_IDF_Index, BM25_Index

passages=[]
TF_IDF_Index=None
BM25_Index=None

def buildIndexes(docs):
    global passages,TF_IDF_Index,BM25_Index
    
    passages=[]
    for doc in docs:
        passages.extend(preProcessDoc(doc))
    texts = [passage["text"] for passage in passages] # extract only the text

    if texts:
        TF_IDF_Index = TF_IDF_Index(texts)
        BM25_Index = BM25_Index(texts)
    else:
        TF_IDF_Index = None
        BM25_Index = None

     
