from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns[1].name())
print(syns[1].lemmas()[0].name())
print(syns[1].definition())
print(syns[1].examples())


synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("\n\nSynonyms")
print(set(synonyms))
print("\n\nAntonyms")
print(set(antonyms))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))