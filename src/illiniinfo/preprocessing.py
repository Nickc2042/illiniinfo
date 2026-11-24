import re

def cleanText(text):
    text = text.replace("\u00a0"," ") # replace nonbreaking spaces with normal spaces
    text = text.replace("\r\n","\n").replace("\r","\n") # normalize the line endings
    text = re.sub(r"[ \t]+"," ",text) # for any mltiple spaces or tabs to be replaced with a single space
    text = re.sub(r" *\n *","\n",text) # remove the spaces before and after linebreaks
    text = re.sub(r"\n{3,}","\n\n",text) # replace specifically 3+ newlines wiht 2
    return text.strip() # finally remove whitespace from beginning and the end


def splitPassages(text,maxWords=150):# for now, it preservers more so the words but not paragraphs
    passages = [] # to store later to return
    text = cleanText(text) # use cleanText()^ to clean it before working with it
    words = text.split() # split text into individual words
    
    for i in range(0,len(words), maxWords): # div the text inot chunks of maxWords
        chunk = words[i:(i+maxWords)]
        passages.append(" ".join(chunk))

    return passages


def preProcessDoc(doc, maxWords=150):
    passages = [] # to store and return
    chunk = splitPassages(doc["text"],maxWords) # idea is to splut a doc's texts into a chunk that can be searched

    for i, chunk in enumerate(chunk):
        passage = {
            "passage_id": f"{doc['document_id']}-p{(i+1):03d}", # :03d so each passage num is like a course num 000
            "document_id": doc["document_id"],
            "title": doc["title"],
            "heading": doc.get("heading", ""),
            "text": chunk,
            "source_url": doc["source_url"],
            "catalog_year": doc.get("catalog_year")
        }
        passages.append(passage)

    return passages

