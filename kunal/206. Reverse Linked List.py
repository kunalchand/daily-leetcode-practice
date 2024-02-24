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
    # Time-O(n) Space-O(1) Iterativly
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            left = None
            current = head

            while True:
                right = current.next

                # Reverse the direction of current
                current.next = left

                # Prepare for movement to right
                if not right:
                    return current

                left = current
                current = right

        else:
            return head
    """

    # Time-O(n) Space-O(1) Recursively
    def helper(self, start, end) -> Tuple[ListNode, ListNode]:
        if start is end:
            end.next = None
        else:
            current = start
            start, end = self.helper(start.next, end)

            end.next = current
            current.next = None
            end = current

        return (start, end)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            start = head
            end = head
            while end.next:
                end = end.next

            start, end = self.helper(start, end)

            return start
