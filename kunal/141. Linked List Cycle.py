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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time-O(n) Space-O(n)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()

        cur = head

        while cur:
            if cur in hashset:
                return True
            else:
                hashset.add(cur)
                cur = cur.next

        return False
    """

    # Time-O(n) Space-O(1) Modifying Original List
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        while cur:
            if cur.val == 100001:
                return True
            else:
                cur.val = 100001
                cur = cur.next
        
        return False
    """

    # Time-O(n) Space-O(1) Slow Fast Approach
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = ListNode(0, head)
        fast = ListNode(0, head)

        while slow and fast:
            if slow is fast:
                return True
            else:
                slow = slow.next
                if fast.next is None:
                    return False
                fast = fast.next.next

        return False
    """

    # Time-O(n) Space-O(1) Tortoise Hare Approach
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while tortoise and hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False
