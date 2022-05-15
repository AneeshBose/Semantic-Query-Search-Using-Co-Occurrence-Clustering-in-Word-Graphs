#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:54:35 2019

@author: aneesh
"""
#---------------------------------------------IMPORT MODULES---------------------------------------------------
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import string
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

#---------------------------------------------EXTRACT TOPICS---------------------------------------------------

topics = ['alt.atheism','sci.space','talk.politics.misc','rec.sport.baseball','comp.graphics']

text = ""
news_data = {}
c = 0
stopwrds = stopwords.words('english')
abbreviations = ["'ve","n't","''","``",'et','al','aint','arent','cannot','cant',
                 'couldnt','darent','nope','not','nothing','nowhere','edu','com',
                 'um','uh','no','inc','ah','oh','you']
for orthographics in abbreviations:
    text = unicode(orthographics,errors='ignore')
    stopwrds.append(text)

#---------------------------------------------PREPROCESSING---------------------------------------------------
for x in topics:
    cnt = 0
    path = '/home/saurabh/saurabh_aneesh/aneesh/NLP_Work/20news-bydate-train/' + x +'/*'
    for filename in glob.glob(path):
        with open(filename,'r') as fp:
            text = fp.read()
            
            unclean_data = word_tokenize(text)
            clean_data = ""
            for token in unclean_data:
                    if token.lower() not in stopwrds and token not in string.punctuation and token not in string.ascii_letters:
                        clean_data += token.lower()+" "
            news_data[c] = clean_data
            c += 1
            cnt += 1
            fp.close()
    print 'Finished reading ' + str(cnt) + ' topics.'
corpus = []

for key in news_data:
    corpus.append(news_data[key])

#---------------------------------------COMPUTING COUNTS AND TF_IDF-------------------------------------------
cv = CountVectorizer(analyzer='word',token_pattern=r"\b[a-zA-Z][^ -\/]+\b",min_df=5,max_df=1000)
cv.fit_transform(corpus)


print cv.get_feature_names()
 

G = nx.Graph()
tfidf_vectorizer = TfidfVectorizer(encoding='utf-8',decode_error='ignore',analyzer='word',stop_words='english',token_pattern=r"\b[a-zA-Z0-9][^ -\/]+\b",max_df=100,min_df=20)
tfidf_vectorizer.fit_transform(corpus)

#create dictionary to find a tf-idf word for each word
word2tfidf = dict(zip(cv.get_feature_names(),tfidf_vectorizer.idf_))
l = [(key, value) for key, value in word2tfidf.items()]
idf_scores = sorted(l,reverse=True,key=lambda x: x[1])
    
#-----------------------------------------CAPTURE CO_OCCURRENCES----------------------------------------------
#for word,score in idf_scores[:300]:
#    #print 'Node added',word,score
#    G.add_node(word)
#
#for w1,w2 in combinations(idf_scores[:50],2):
#    co_occur = 0
#    print 'Testing co-occurrence between '+ w1[0]+' and '+w2[0]
#    for i in range(len(news_data)):
#        if w1[0] in news_data[i] and w2[0] in news_data[i]:
#            co_occur += 1
#    if co_occur >= 3:
#        print 'Edge added'
#        G.add_edge(w1[0],w2[0],weight=co_occur)

#------------------------------------------BUILD NETWORKX GRAPH-----------------------------------------------
search_contents = {}
print "Enter search key for the graph:"
query = raw_input().lower()
if query in G.nodes():
    print 'Valid search query. Generating levels...'
    l = 0
    prev_path = []
    prev_path.append(query)
    prev_path = set(prev_path)
    search_contents[l] = query
    l += 1
    while l < 4:
        new_path = nx.single_source_shortest_path_length(G,source=query,cutoff=l)
        new_path = set(new_path)
        search_contents[l] = list(new_path.difference(prev_path))
        prev_path = new_path
        l += 1
else:
    print 'Invalid search query'
        
for key in search_contents:
    print 'Nodes in level ', key
    print search_contents[key]
        
#--------------------------------------------PLOT USING MATPLOTLIB.PYPLOT--------------------------------------
plt.figure(figsize=(20,14))    
nx.draw(G,with_labels=True,dpi=1200)
plt.savefig('co_occurrence1.png')
plt.show()