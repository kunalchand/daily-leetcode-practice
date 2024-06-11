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


# https://leetcode.com/problems/relative-sort-array/
class Solution:
    # Using Map
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 = deque(arr2)
        arr1Count = Counter(arr1)
        arr1 = []

        while arr2:
            num = arr2.popleft()
            while arr1Count[num] > 0:
                arr1Count[num] -= 1
                arr1.append(num)

        for  num, count in sorted(list(arr1Count.items())):
            for _ in range(count):
                arr1.append(num)

        return arr1
    """

    # Custom Sort
    def customSort(self, a: int, b: int) -> int:
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
            if a < b:
                return -1  # a comes BEFORE b
            elif a > b:
                return 1  # a comes AFTER b
            else:
                return 0

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # define index wise order
        self.order = defaultdict(int)
        for index, num in enumerate(arr2):
            self.order[num] = index

        return sorted(arr1, key=cmp_to_key(self.customSort))
