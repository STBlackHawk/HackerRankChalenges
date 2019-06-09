#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: Minion Games

@author: blackhawk
"""

def minion_game(string):
    St = 0 
    Ka = 0
    vowel = 'AEIOU'
    n = len(string)
    for i, s in enumerate(string):
        if s in vowel:
            Ka += n - i
        else :
            St += n - i

    if St > Ka: print('Stuart '+ str(St))
    elif St < Ka: print('Kevin '+ str(Ka))
    else: print('Draw')