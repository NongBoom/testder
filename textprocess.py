import pythainlp.util
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize

# Stop word
thai_stopwords = list(thai_stopwords())

#Function process text
def text_process(text):
    # Remove specific characters and punctuation
    final = "".join(u for u in text if u not in ("?",".",";",":","!",'"',"ๆ","ฯ",">","<","/","-",))
    # Tokenize the text using pythainlp's word_tokenize
    final = word_tokenize(final, engine='longest')
    # Join the tokens into a string
    final = " ".join(word for word in final if pythainlp.util.isthai(word))
    # Remove Thai stopwords from the text
    final = " ".join(word for word in final.split() if word.lower not in thai_stopwords)
    return final