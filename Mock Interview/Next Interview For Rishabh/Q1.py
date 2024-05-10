"""
2487. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
N/A

Constraints:
N/A


"""

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

        # Generate a Linked List from a List
        # stack = [13 8 4]
        #  [] -> [13] -> [8] -> [4]
        # dummy                 dcur

        # Generate a Linked List from a List
        # stack = [13 8]
        #  [0] -> [13] -> [8]
        # dummy           dcur
        # i = 2

        # [5,  2,  13,  3,  8]
        #              cur
        # stack = bottom [13 8] top


class Solution:
    # Stack, Time-O(n) Space-O(n)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        stack.append(cur.val)

        while cur.next:
            while cur.next.val > stack[-1]:
                stack.pop()
            stack.append(cur.next.val)
            cur = cur.next

        i = 0
        dummyNode = ListNode()
        dcur = dummyNode
        while i < len(stack):
            dcur.next = ListNode(stack[i])
            dcur = dcur.next
            i += 1

        return dummyNode.next
