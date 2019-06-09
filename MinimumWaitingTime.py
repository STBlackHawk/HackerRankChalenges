#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:13:21 2019

@author: blackhawk
"""

import heapq

def minimumAverage(customers):
    atDoor = []
    instores = []
    aver = 0 
    for c in customers:
        heapq.heappush(atDoor, c)
    now = 0

    while atDoor or instores:
        
        if not instores and now <atDoor[0][0]: now = atDoor[0][0]

        while atDoor and  atDoor[0][0] <= now:
            c = heapq.heappop(atDoor)
            heapq.heappush(instores,(c[1], c[0]))
        
        
        t = heapq.heappop(instores)
        now += t[0]
        aver += now - t[1]

        

    return aver/len(customers) 


customers = [(0, 3),(1,9),(2,6)]

minimumAverage(customers)