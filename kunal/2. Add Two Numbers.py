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
    def addAndFindCarry(self, a=0, b=0, c=0) -> Tuple[int, int]:
        string = str(a + b + c)
        if len(string) == 1:
            return (0, int(string[0]))
        else:
            return (int(string[0]), int(string[1]))

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        carry = 0

        while True:
            if not l1 and not l2:
                if carry != 0:
                    cur.next = ListNode(carry)
                break
            else:
                a, l1 = (l1.val, l1.next) if l1 else (0, None)
                b, l2 = (l2.val, l2.next) if l2 else (0, None)
                c = carry

                carry, sumVal = self.addAndFindCarry(a, b, c)
                cur.next = ListNode(sumVal)
                cur = cur.next

        return head.next
