#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackeRank: Company Logo

@author: blackhawk
"""


from collections import Counter




if __name__ == '__main__':
    s = input()

c = Counter(s)
ans = sorted(list(c.items()), key = lambda x: (-x[1],x[0]))
for i in range(3):
    print(ans[i][0]+' '+str(ans[i][1]))