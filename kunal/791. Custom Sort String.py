import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/custom-sort-string/
class Solution:
    # Using Map
    """
    def customSortString(self, order: str, s: str) -> str:
        order = deque(order)
        sCount = Counter(s)
        s = ""

        while order:
            char = order.popleft()
            while sCount[char] > 0:
                sCount[char] -= 1
                s += char

        for  char, count in sCount.items():
            for _ in range(count):
                s += char

        return s
    """

    # Custom Sort
    def customSort(self, a: str, b: str) -> int:
        # a is in order and b isn't
        if a in self.order and b not in self.order:
            return -1  # a comes BEFORE b

        # b is in order and a isn't
        elif b in self.order and a not in self.order:
            return 1  # a comes AFTER b

        # both a & b are in order
        elif a in self.order and b in self.order:
            if self.order[a] < self.order[b]:
                return -1  # a comes BEFORE b
            elif self.order[a] > self.order[b]:
                return 1  # a comes AFTER b
            else:
                return 0

        # both a & b aren't in order
        else:
            return 0

    def customSortString(self, order: str, s: str) -> str:
        # define index wise order
        self.order = defaultdict(int)
        for index, char in enumerate(order):
            self.order[char] = index

        return "".join(sorted(list(s), key=cmp_to_key(self.customSort)))
