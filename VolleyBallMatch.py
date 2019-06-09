#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: VolleyballMatch

@author: blackhawk
"""


import sys
import math


def choose(n,k):
    return math.factorial(n)//math.factorial(k)//math.factorial(n-k)


#base case is when the winner scores a5 and win the game, another case is when 
#they pas 24 so after that for each round there is two to the power of number of rounds 
#the looser team won because we know that the last two round the winner won and 
#rounds before cannot have many combinations
def numgames(a,b):

    if a < b:
        a, b = b, a

    if a <25 and b<=24 :return(0)
    elif a==25 and b>=24: return(0)
    elif a == 25: return(choose(a+b-1, b))
    elif a> 25 and a-b !=2: return 0
    else:return(choose(48, 24)*2**(b-24))


if __name__=='__main__':
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(numgames(a,b)%1000000007)