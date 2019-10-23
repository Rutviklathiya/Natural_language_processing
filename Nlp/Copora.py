import nltk
# print(nltk.__file__)


path = '/home/rutvik/.local/lib/python3.6/site-packages/nltk/__init__.py'

from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(10):
    print(tok[x])