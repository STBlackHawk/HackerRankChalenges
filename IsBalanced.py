#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: IsBalanced

@author: blackhawk
"""


#using stack data structure to keep track of the last in first out order.

def isBalanced(s):
    Open ='{[('
    dic = {'}':'{', ')':'(', ']':'[' }
    close = '}])'
    stack=[]
    for char in s:
        if char in Open:
            stack.append(char)
        elif char in close:
            if not stack: return 'NO'
            else:
                t = stack.pop()
                if dic[char] != t: return 'NO'
    
    if stack: return 'NO'
    else: return 'YES'