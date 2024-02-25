import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getListLength(self, head) -> int:
        num = 0
        while head:
            num += 1
            head = head.next
        return num

    def findOddMid(self, head) -> ListNode:
        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def findEvenMid(self, head) -> ListNode:
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, prev, cur) -> ListNode:
        if cur.next != None:
            head = self.reverseList(cur, cur.next)
        else:
            head = cur

        cur.next = prev
        return head

    def mergeList(self, list1, list2, turn: str) -> ListNode:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        else:
            if turn == "list1":
                list1.next = self.mergeList(list1.next, list2, "list2")
                return list1
            elif turn == "list2":
                list2.next = self.mergeList(list1, list2.next, "list1")
                return list2

    def findPrevMid(self, head, mid):
        prevMid = head
        while prevMid.next is not mid:
            prevMid = prevMid.next
        return prevMid

    def printLists(self, head1, head2) -> None:
        cur = head1

        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next

        print("")

        cur = head2

        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = self.getListLength(head)

        if length == 0 or length == 1:
            pass
        elif length % 2 == 1:  # Odd
            mid = self.findOddMid(head)

            list1 = head
            list2 = self.reverseList(None, mid.next)
            mid.next = None

            self.mergeList(list1, list2, "list1")
        elif length % 2 == 0:  # Even
            mid = self.findEvenMid(head)
            prevMid = self.findPrevMid(head, mid)

            list1 = head
            list2 = self.reverseList(None, mid)
            prevMid.next = None
            mid.next = None

            self.mergeList(list1, list2, "list1")
