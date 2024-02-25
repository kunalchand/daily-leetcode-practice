from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    '''
    APPROACH-1: ITERATIVE
    TIME: O(N)
    SPACE: O(1)
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, nxt = None, head, None
        while curr:
            nxt = curr.next         # store reference of next before losing it
            curr.next = prev        # change direction
            prev = curr             # update prev
            curr = nxt              # update curr
        return prev

    '''
    APPROACH-2: RECURSIVE
    TIME: O(N)
    SPACE: O(1)
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # logic for start node
        # logic for generic nodes (all the nodes in between)
        # logic for end node
        def reverse(prev, curr):
            if curr.next == None:                   # BASE CASE / END NODE
                curr.next = prev
                return curr
            
            head = reverse(curr, curr.next)         # Logic for generic and first node
            curr.next = prev
            return head

        if not head: return None
        return reverse(None, head)
        