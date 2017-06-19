from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


f= open("data.txt")
text = f.read()
print(text)
f.close()

words = word_tokenize(text)
stop_words=  set(stopwords.words("kazakh"))


filtered_sentence = []
for w in words:
    if w not  in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
