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


# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list
class Solution:
    def recursionMagic(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        else:
            carry = self.recursionMagic(head.next)

            number = str(carry + 2 * head.val)

            if len(number) == 2:
                head.val = int(number[1])
                return int(number[0])
            else:
                head.val = int(number[0])
                return 0

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.recursionMagic(head)

        if carry == 0:
            return head
        else:
            return ListNode(carry, head)
