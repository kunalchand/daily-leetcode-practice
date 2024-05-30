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


# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
class Solution:
    # Suffix Count
    """
    def specialArray(self, nums: List[int]) -> int:
        newNums = sorted(Counter(nums).items())
        suffixCount = [0] * len(newNums)

        for index in range(len(newNums) - 2, -1, -1):
            suffixCount[index] = newNums[index + 1][1] + suffixCount[index + 1]

        x = 0
        pointer = 0

        while pointer < len(newNums):
            key = newNums[pointer][0]
            freq = newNums[pointer][1]
            suffix = suffixCount[pointer]
            if x <= key:
                if x == freq + suffix:
                    return x
                x += 1
            elif x > key:
                pointer += 1

        return -1
    """

    # Deque
    def specialArray(self, nums: List[int]) -> int:
        stream = deque(sorted(nums))

        x = 0

        while stream:
            if x <= stream[0]:
                if x == len(stream):
                    return x
                x += 1
            else:
                stream.popleft()

        return -1
