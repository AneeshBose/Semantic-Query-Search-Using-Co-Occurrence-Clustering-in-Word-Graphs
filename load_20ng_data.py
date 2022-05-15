#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:44:49 2019

@author: aneesh
"""

from nltk.tokenize import word_tokenize
import re,string
from nltk.corpus import stopwords
import os
from glob import glob


def strip_newsgroup_header(text):
    """
    Given text in "news" format, strip the headers, by removing everything
    before the first blank line.
    """
    _before, _blankline, after = text.partition('\n\n')
    return after


_QUOTE_RE = re.compile(r'(writes in|writes:|wrote:|says:|said:'
                       r'|^In article|^Quoted from|^\||^>)')


def strip_newsgroup_quoting(text):
    """
    Given text in "news" format, strip lines beginning with the quote
    characters > or |, plus lines that often introduce a quoted section
    (for example, because they contain the string 'writes:'.)
    """
    good_lines = [line for line in text.split('\n')
                  if not _QUOTE_RE.search(line)]
    return '\n'.join(good_lines)


def strip_newsgroup_footer(text):
    """
    Given text in "news" format, attempt to remove a signature block.

    As a rough heuristic, we assume that signatures are set apart by either
    a blank line or a line made of hyphens, and that it is the last such line
    in the file (disregarding blank lines at the end).
    """
    lines = text.strip().split('\n')
    for line_num in range(len(lines) - 1, -1, -1):
        line = lines[line_num]
        if line.strip().strip('-') == '':
            break
    
    if line_num > 0:
        return '\n'.join(lines[:line_num])
    else:
        return text

stopwrds = stopwords.words('english')
with open('stopwrds.txt') as fp_stop:
    for stop_word in fp_stop.readlines():
        stopwrds.append(unicode(stop_word.strip('\n')))
fp_stop.close()
stopwrds = set(stopwrds)

news_data = {}
doc_tokens = {}

#---------------------------------------------PREPROCESSING---------------------------------------------------
result = [y for x in os.walk("/home/ashish/Aneesh/20news-bydate-train",topdown=False) for y in glob(os.path.join(x[0],'*')) if os.path.isfile(y)]

for filename in result:
    with open(filename,'r') as fp:
        contents = fp.read()
        contents = unicode(contents,errors='ignore')
        raw_text = []
        raw_text.append(contents)
        raw_text = [strip_newsgroup_header(text) for text in raw_text]
        raw_text = [strip_newsgroup_footer(text) for text in raw_text]
        raw_text = [strip_newsgroup_quoting(text) for text in raw_text]
        news_data[filename] = raw_text
        fp.close()
 
for key in news_data:
    unclean_data = word_tokenize(news_data[key][0])
    clean_data = ""
    for token in unclean_data:
        if token.lower() not in stopwrds and token not in string.punctuation and token != '``' and token !="''": 
            clean_data += token.lower()+" "
    del news_data[key]
    news_data[key] = clean_data
    doc_tokens[key] = re.split('[ /-_]*',clean_data)
    
corpus = []
for key in news_data:
    corpus.append(news_data[key])