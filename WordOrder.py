#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank WordOrder Challenge

@author: blackhawk
"""

import sys
from collections import OrderedDict

_ = int(sys.stdin.readline().strip())

word = OrderedDict()
for line in sys.stdin.readlines():
   line1 = line.strip()
   if line1 in word:
       word[line1] +=1
   else:
        word[line1] =1

print(len(word.items()))
for w in word:
    print(word[w], end=' ')


