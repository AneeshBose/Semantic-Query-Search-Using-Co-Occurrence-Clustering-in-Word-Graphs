#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:54:03 2019

@author: aneesh
"""

from context1 import search_contents,query,vocab
from load_20ng_data import news_data,doc_tokens,corpus
from bm25 import BM25


bm25 = BM25(doc_tokens)

bm25_ranking = []
for position,index in enumerate(bm25.ranked(query,10)):
    bm25_ranking.append(bm25.mapper[index])
    
    
