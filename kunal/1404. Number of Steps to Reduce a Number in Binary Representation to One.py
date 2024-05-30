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


# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
class Solution:
    # Convert from bit to int
    """
    def numSteps(self, s: str) -> int:
        steps = 0

        s = int(s, 2)

        while s != 1:
            if s%2 == 0:
                s //= 2
            else:
                s += 1
            steps += 1

        return steps
    """

    # Deque
    def divideByTwo(self) -> None:
        self.deque1.pop()

    def addOne(self) -> None:
        carry = "1"
        while self.deque1:
            bit = self.deque1.pop()
            if bit == "0":
                self.deque2.appendleft("1")
                carry = "0"
                break
            elif bit == "1":
                self.deque2.appendleft("0")
                carry = "1"

        if carry == "1":
            self.deque2.appendleft(carry)

        while self.deque2:
            self.deque1.append(self.deque2.popleft())

    def isNotOne(self) -> bool:
        return len(self.deque1) != 1

    def isEven(self) -> bool:
        return self.deque1[-1] == "0"

    def numSteps(self, s: str) -> int:
        steps = 0

        self.deque1 = deque()
        self.deque2 = deque()

        for char in s:
            self.deque1.append(char)

        while self.isNotOne():
            if self.isEven():
                self.divideByTwo()
            else:
                self.addOne()
            steps += 1

        return steps
