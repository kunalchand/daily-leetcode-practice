from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create dummy node
        head = ListNode()
        current = head

        while list1 and list2:
            # if ele in list1 < ele in list2
            # point the current list to list1
            # update the list1 pointer to next val
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            # if ele in list1 > ele in list2
            # point the current list to list2
            # update the list2 pointer to next val
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # if any of the lists ends (i.e one is smaller than the other)
        current.next = list1 or list2
        
        # dummy node is empty
        # return the next of dummy node which has the whole list
        return head.next

    #REVISIT#   
    '''
    APPROACH: ITERATIVE, creating a new LL
    TIME: O(N)
    SPACE: O(N)
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        res_list = ListNode()
        head = res_list
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val, None)
                res_list.next = node
                res_list = node
                l1 = l1.next          # update l1 pointer     
            elif l1.val > l2.val:
                node = ListNode(l2.val, None)
                res_end.next = node
                res_end = node
                l2 = l2.next          # update l2 pointer

        if l1 and l2 == None: res_end.next = l1
        if l2 and l1 == None: res_end.next = l2

        return head.next
                
    '''
    APPROACH: ITERATIVE, without creating a LL, but a dummy node
    TIME: O(N)
    SPACE: O(1)
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy.next
