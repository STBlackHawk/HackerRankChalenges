#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: CoinChange Problem
@author: blackhawk
"""

dic = {}
def getWays(n, c):
    if (n,tuple(c)) in dic:
        return dic[(n,tuple(c))]
    else:
        if n < 0 or not c: return 0
        elif n ==0 : return 1
        else :
            ans = getWays(n-c[0], c)+getWays(n,c[1:])
        dic[(n,tuple(c))] = ans
        return ans