# -*- coding: utf-8 -*-


def ngram_probs(filename='raw_sentences.txt'):
    return bigram_probs, trigram_probs

cnt2, cnt3 = ngram_probs()
print(cnt2[('we', 'are')])


with open(r"d:\glia\raw_sentences.txt", "r") as fileObject:
     allword = fileObject.read()

fileObject.close()

lower_allword= allword.lower()

wordcount={}
for word in lower_allword.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print ( "Word : \'we\' total count = ",  wordcount["we"])
print ( "Word : \'are\' total count = ",  wordcount["are"])

