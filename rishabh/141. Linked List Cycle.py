# FLOYD'S CYCLE-FINDING ALGORITHM
# FLOYD'S hare and tortoise algo (fast and slow pointers)
# faster will catch up slower one eventually
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
class Solution:
    '''
    APPROACH-1: use a set to keep track of visited nodes
    TIME: O(N)
    SPACE: O(N), set()
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head             # pointer to loop/traverse the list
        while curr:
            if curr in visited: return True
            visited.add(curr)
            curr = curr.next
        return False
        
    '''
    APPROACH-2: change the value of visited nodes
    if a node with changed val is encountered, there's cycle present
    note that it will change the original LL values
    TIME: O(N)
    SPACE: O(1)
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr:
            if curr.val == 10 ** 5 + 1: return True
            curr.val = 10 ** 5 + 1
            curr = curr.next
        return False

    '''
    APPROACH-3: floyd's warshall LL cycle, if hare catches tortoise, it's a cycle
    TIME: O(N)
    SPACE: O(1)
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True
        return False
        