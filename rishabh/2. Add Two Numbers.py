from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)
    
class Solution:
    '''
    APPROACH: sum curr value at both pointers and carry, create a new node. Take care of carry value
    TIME: O(max(M + N)), M, N : lenght of two lists
    SPACE: O(N), for result
    '''
    def printLL(self, ll):
        curr = ll
        while curr:
            print(curr, end=" -> ")
            curr = curr.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_node = dummy    
        carry = 0                               # carry would be 0 for first unit digit addition
        
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            digit = s % 10                      # update digit based on sum
            carry = s // 10                     # update carry based on sum

            new_node.next = ListNode(digit)     # create new node             
            new_node = new_node.next            # update new_node pointer
            
            if l1: l1 = l1.next                 # update loop pointers
            if l2: l2 = l2.next
        
        return dummy.next

# 243, 564
# l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
# l2 = ListNode(5, ListNode(6, ListNode(4, None)))
# Solution().printLL(l1)
# Solution().printLL(l2)
# Solution().printLL(Solution().addTwoNumbers(l1, l2))

l1 = ListNode(val=4, next=None)
l2 = ListNode(val=5, next=None)
Solution().printLL(Solution().addTwoNumbers(l1, l2))