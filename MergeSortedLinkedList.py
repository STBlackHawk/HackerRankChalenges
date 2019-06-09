#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: MergedtwoSortedLinkedList

@author: blackhawk
"""

def mergeLists(head1, head2):
    srt = SinglyLinkedList()
    while (head1) or (head2):
        if head2 is None:
            srt.insert_node(head1.data)
            head1 = head1.next
        elif head1 is None:
            srt.insert_node(head2.data)
            head2 = head2.next
        else:
            if head1.data < head2.data:
                srt.insert_node(head1.data)
                head1 = head1.next 
            else:
                srt.insert_node(head2.data)
                head2 = head2.next
    return srt.head