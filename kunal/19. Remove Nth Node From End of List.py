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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        end = head

        count = 1
        # Create a distance of n+1:
        while end.next is not None and count < n + 1:
            end = end.next
            count += 1

        # n = Number of Nodes
        if count < n + 1:
            return head.next

        while end.next is not None:
            start = start.next
            end = end.next

        start.next = start.next.next

        return head
