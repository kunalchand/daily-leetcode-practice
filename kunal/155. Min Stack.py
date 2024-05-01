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

# https://leetcode.com/problems/min-stack/description/

# Using Stack
"""
class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack:
            self.minstack.append([val, min(val, self.getMin())])
        else:
            self.minstack.append([val, val])

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]
"""


# w/o PreBuilt Data Structure like stack (LLD)
class MinStack:
    class Node:
        def __init__(self, val: int, min: int, next: "Node"):  # type: ignore
            self.val = val
            self.min = min
            self.next = next

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = MinStack.Node(val, val, None)
        else:
            self.head = MinStack.Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
