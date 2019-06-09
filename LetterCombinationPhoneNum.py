#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Letter Combinations Of a phone number

@author: blackhawk
"""
from itertools import product

d = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs',8:'tuv', 9:'wzy'}



def LetterCombinations(a):
    if type(a) is str:
        num = list(map(int, list(a)))
    else: num = a
    l = []
    if len(num)==1:
        for p in product(d[num[0]],repeat=2):
            l.append(''.join(p))
        return l
    
    elif len(num) == 2:
        for p in product(d[num[0]], d[num[1]]):
            l.append(''.join(p))
        return l
    elif len(num)>2: 
        
        for p in product(d[num[0]], LetterCombinations(num[1:])):
                l.append(''.join(p))
        return l

LetterCombinations('234')

