#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: blackhawk
"""





#I will reverse the linked list and then take one step in each one the
#The node which they have different next is the merging point



            
def reverse(node):
    start = node
    alpha = None
    while start:
        temp = start.next
        start.next = alpha
        alpha = start
        if not temp:
            return start
        start = temp

def Copylinklis(node):
    head = SinglyLinkedListNode(node.data)
    temp = node.next
    temp2 = head
    while temp:
        tempnode = SinglyLinkedListNode(temp.data)
        temp2.next = tempnode
        temp2 = temp2.next
        temp = temp.next
    return head


def findMergeNode(head1, head2):

    step1 = Copylinklis(head1)
    step2 = Copylinklis(head2)

    step1 = reverse(step1)
    step2 = reverse(step2)

    while step1.next and step2.next:
        if step1.next.data!=step2.next.data: break
        elif step1.next.next is None and step2.next.next is None:
            break
        else:
            step1 = step1.next
            step2 = step2.next
    
    return step1.data