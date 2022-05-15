#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:12:55 2019
@author: aneesh
"""
from context1 import search_contents,query,start
from load_20ng_data import news_data,doc_tokens
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from itertools import islice
from rank_bm25 import bm25_ranking
import time

word_doc = defaultdict(list)
target_words = []
for word in search_contents[0]:
    target_words.append(unicode(word))
    
for word in search_contents[1]:
    target_words.append(word)

#for word in target_words:
#    vocab[word] = 0
#    for key in doc_tokens:
#        if word in doc_tokens[key]:
#            vocab[word] += doc_tokens[key].count(word)
#            
#print vocab
        
for word in search_contents[0]:
    for key in doc_tokens:
        if word in doc_tokens[key]:
            word_doc[word].append(key)
            
for word in search_contents[1]:
    for key in doc_tokens:
        if word in doc_tokens[key]:
            word_doc[word].append(key)  #get the document number(s) where word has occurred

docs = set()
for word in word_doc:
    for doc in word_doc[word]:
        docs.add(doc)
docs = list(docs)

search_space = []
mapper = {}
c = 0

for doc in docs:
    search_space.append(news_data[doc])
    mapper[c] = doc
    c += 1

raw_text = ""
for token in query:
    raw_text += token + " "
    
for word in search_contents[1]:
    raw_text += word + " "

search_space.append(raw_text)
cv = TfidfVectorizer(vocabulary = target_words)
x = cv.fit_transform(search_space)

print 'Vocabulary for the query ',len(target_words)

vocab = cv.vocabulary_

#ADD WEIGHTS TO SEARCH LEVEL FOR MODIFYING COSINE SIMILARITY
l0_indices = []
for word in search_contents[0]:
    if word in vocab:
        l0_indices.append(vocab[word])
        
for idx in l0_indices:
    for i in range(x.shape[0]):
        x[i,idx] *= 6

result = cosine_similarity(x[-1:],x)
pairs_mapper = []

for idx,val in enumerate(result[0]):
    pairs_mapper.append((idx,val))
    
pairs1_mapper = sorted(pairs_mapper,reverse = True,key = lambda x: x[1])


cosine_ranking = []
for idx in islice(pairs1_mapper[1:],10):
    cosine_ranking.append(mapper[idx[0]])

del search_space[-1:]

print 'Cosine Ranking'
for doc in cosine_ranking:
    print doc
    
#print 'BM25 Ranking'
#for doc in bm25_ranking:
#    print doc
    
print 'Time taken to fetch results:', time.time() - start
tp = 0
fp = 0
fn = 0

for doc in cosine_ranking:
    if doc.find('med') != -1:
        tp += 1
    else:
        fp += 1
        
#for doc in bm25_ranking:
#    if doc not in cosine_ranking:
#        fn += 1
        
precision = tp * 1.0/(tp + fp)
#recall = tp * 1.0/(tp + fn)


print 'Calculating accuracy...'
print precision
#print 'Accuracy of cosine keeping BM25 as benchmark :%f' % (2.0 * precision * recall/(precision + recall))
        
