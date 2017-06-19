
from nltk.util import ngrams
from nltk import word_tokenize
from collections import Counter


f= open("data.txt")
text = f.read()
print(text)
f.close()


token = word_tokenize(text)
unigram = ngrams(token, 1)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

print(Counter(unigram))