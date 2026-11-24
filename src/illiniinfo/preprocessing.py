import re

def cleanText(text):
    text = text.replace("\u00a0"," ") # replace nonbreaking spaces with normal spaces
    text = text.replace("\r\n","\n").replace("\r","\n") # normalize the line endings
    text = re.sub(r"[ \t]+"," ",text) # for any mltiple spaces or tabs to be replaced with a single space
    text = re.sub(r" *\n *","\n",text) # remove the spaces before and after linebreaks
    text = re.sub(r"\n{3,}","\n\n",text) # replace specifically 3+ newlines wiht 2
    return text.strip() # finally remove whitespace from beginning and the end



