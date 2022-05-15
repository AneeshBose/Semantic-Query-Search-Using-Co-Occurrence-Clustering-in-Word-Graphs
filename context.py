#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:54:35 2019

@author: aneesh
"""
#---------------------------------------------IMPORT MODULES---------------------------------------------------
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import networkx as nx
from load_20ng_data import corpus,doc_tokens,stopwrds
import os.path,difflib
import matplotlib.pyplot as plt
import time

def print_topics(G,query):
    node_query = []
    for query_word in query:
        if query_word in stopwrds:
            query.remove(query_word)
    
    for f_query in query:
        if G.has_node(f_query):
            node_query.append(f_query)
        else:
            print f_query+' not found in graph. Closest matches are:'
            for word in difflib.get_close_matches(f_query,vocab,cutoff=0.8):
                print word
            add_word = raw_input()
            if add_word == '':
                continue
            else:
                node_query.append(add_word)                    
                
    if len(node_query) >= 1:
        print 'Valid search query. Generating levels...'
        l = 0
        prev_path = []
        for node in node_query:
            prev_path.append(node)
        prev_path = set(prev_path)
        search_contents[l] = prev_path
        
        l += 1
        union_path = set()
        while l < 5:
            for f_query in node_query:
                new_path = nx.single_source_shortest_path_length(G,source=f_query,cutoff=l)
                new_path = set(new_path)
                union_path = new_path.union(union_path)
            search_contents[l] = union_path.difference(prev_path)
            prev_path = union_path
            l += 1
            
        for key in search_contents:
            print 'Nodes in level', key
            print list(search_contents[key])
    else:
        print 'Invalid search query'

#---------------------------------------------EXTRACT TOPICS---------------------------------------------------
global search_contents
search_contents = {}
query = []
cv = CountVectorizer(analyzer='word',token_pattern=r"\b[a-zA-Z][^ -=\|\/]{2,}\b",min_df=8,max_df=0.95,stop_words=stopwrds)
cv.fit_transform(corpus)
vocab = cv.vocabulary_
print 'Vocabulary for the word graph ',len(vocab)

if os.path.exists('/home/ashish/Aneesh/Generate_Levels1/graph.gpickle'):
    G = nx.read_gpickle('graph.gpickle') 
    print "Enter search key for the graph:"
    query =  word_tokenize(raw_input().lower())
    start = time.time()
    print_topics(G,query)
else:    
#---------------------------------------COMPUTING COUNTS AND TF_IDF-------------------------------------------    
    features = []
    fp1 = open('vocab.txt','w')
    for feature in cv.get_feature_names():
        features.append(feature)
        fp1.write(str(feature)+'\n')
    fp1.close()
    print 'Finished writing words'
    
    G = nx.Graph()
    tfidf_vectorizer = TfidfVectorizer(encoding='utf-8',decode_error='ignore',analyzer='word',stop_words=stopwrds,token_pattern=r"\b[a-zA-Z0-9][^ -=\|\/]{2,}\b",max_df=0.95,min_df=8)
    tfidf_vectorizer.fit_transform(corpus)
    
    #create dictionary to find a tf-idf word for each word
    word2tfidf = dict(zip(cv.get_feature_names(),tfidf_vectorizer.idf_))
    l = [(key, value) for key, value in word2tfidf.items()]
    idf_scores = sorted(l,reverse=True,key=lambda x: x[1])
    
    #-----------------------------------------CAPTURE CO_OCCURRENCES----------------------------------------------
    for word,score in idf_scores:
        G.add_node(word)
    
    idf_dict = {} 
    co_occur_dict = {}
    for tup in idf_scores:
        idf_dict[tup[0]] = tup[1]
    
    c = 1
    window_size = 10
    for key in doc_tokens:
        doc = doc_tokens[key]
        for j in range(len(doc)-window_size+1):
            if doc[j] in features:  
                k = j + window_size
                for idx in range(j+1,k):
                    if doc[idx] in features and doc[idx] != doc[j]:
                        pair = (doc[j],doc[idx])
                        pair = tuple(sorted(pair))
                        if pair not in co_occur_dict:
                            co_occur_dict[pair] = 1
                        else:
                            co_occur_dict[pair] += 1
                            
        print 'Finished %d out of %d documents' % (c,len(doc_tokens))
        c += 1
                        
    for pair in co_occur_dict:
        if co_occur_dict[pair] > 10:
            G.add_edge(pair[0],pair[1],weight=co_occur_dict[pair])
            
    nx.write_gpickle(G,'graph.gpickle')
    print "Enter search key for the graph:"
    query =  word_tokenize(raw_input().lower())
    start = time.time()
    print_topics(G,query)    
#   -----------------------------------------PLOT USING GEPHI------------------------------------------------------
nodes_subgraph = []
i = 0
while i < 2:
    for node in search_contents[i]:
        nodes_subgraph.append(node)
    i += 1
    
subgraph = G.subgraph(nodes_subgraph)
nx.write_gexf(subgraph,"query_graph.gexf")
plt.figure(1,figsize=(16,14))
pos = nx.spring_layout(subgraph)
nx.draw_networkx(subgraph,data = True, pos = pos)