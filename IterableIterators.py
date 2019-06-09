#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: Iterable and Iterators

@author: blackhawk
"""

#There are two ways to approach this problem one using Itertools to produce all
#all the possible combinations, another one is to use combinatorics to count the
#probability that no 'a' comes and then return 1-p

import sys
import math

def Choose(n,k):
    return math.factorial(n)//math.factorial(k)//math.factorial(n-k)


n = int(sys.stdin.readline())
line = list(sys.stdin.readline().strip().split())
k = int(sys.stdin.readline())

a = 0  
for c in line:
    if c=='a': a+=1

ans = 0 
if a == n:
     ans = 1
elif a==0:
    ans = 0
elif k==n:
    ans = 1
elif k==0:
    ans=0
else:
    ans = 1- Choose(n-a, k)/Choose(n,k) 

print('%.3f'%ans)
