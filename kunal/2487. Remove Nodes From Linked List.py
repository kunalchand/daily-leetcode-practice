import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/remove-nodes-from-linked-list/
class Solution:
    # Monotonic Deque/Stack/Queue, Time-O(n) Space-O(n)
    """
    def pushInDeque(self, monotonic_deque: Deque, val: int) -> None:
        while monotonic_deque and monotonic_deque[-1] < val:
            monotonic_deque.pop()
        monotonic_deque.append(val)

    def generateList(self, monotonic_deque: Deque, head: ListNode) -> None:
        if not monotonic_deque:
            return
        else:
            head.next = ListNode(monotonic_deque.popleft())
            head = head.next
            self.generateList(monotonic_deque, head)

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        monotonic_deque = deque()

        while head:
            self.pushInDeque(monotonic_deque, head.val)
            head = head.next

        head = ListNode(monotonic_deque.popleft())

        self.generateList(monotonic_deque, head)

        return head
    """

    # Recursion, Time-O(n) Space-O(1)
    def cleanList(self, head: Optional[ListNode]) -> Tuple[int, bool]:
        if not head:
            return (float("-inf"), False)

        maxOnRight, removeRight = self.cleanList(head.next)

        if removeRight:
            head.next = head.next.next

        if head.val < maxOnRight:
            return (maxOnRight, True)
        elif head.val >= maxOnRight:
            return (head.val, False)

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(float("inf"), head)
        head = dummyNode

        self.cleanList(head)

        return head.next
