#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:10:50 2019

@author: aneesh
"""

crisp_topics = ['sci.space','sci.crypt','rec.sport','talk.politics','comp.graphics']

for topic in crisp_topics:
    for iteration in range(3):
        print 'Enter 3 queries related to ' + topic