from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    '''
    APPROACH: 
    a) make a new list (deep copy), 
    weave that new list with the old list (A->A`->B->B`)
    b) connect random pointers
    c) disconnect the OG list from the new list (i.e. unweave)
    TIME: O(N)
    SPACE: O(N), new list
    '''
    def printLL(self, node):
        while node:
            print(f"val:{node.val}, next:{node.next.val if node.next else None}, random:{node.random.val if node.random else None}",end=" -> ")
            node = node.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None : return None   

        # A) make a new deep copy
        curr = head                     # curr pointer, to loop through the list
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
       
        # B) connect random pointers
        curr = head                     # reset loop variable
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # C) disconnect org->copy links
        curr = head.next                 # reset loop variable
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        
        return head.next

        # 7->7->10->10