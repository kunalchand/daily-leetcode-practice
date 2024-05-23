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


# https://leetcode.com/problems/the-number-of-beautiful-subsets/
class Solution:
    # Recursion Global Count
    """
    def generateSubset(self, nums: List[int], k: int, subset: List) -> None:
        for index in range(len(nums)):
            if (nums[index] - k) not in subset and (nums[index] + k) not in subset:
                # self.allSubset.append(subset + [nums[index]])
                self.count += 1
                self.generateSubset(nums[index+1:], k, subset + [nums[index]])

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.count = 0
        # self.allSubset = []
        self.generateSubset(nums, k, [])
        # print(self.allSubset)
        return self.count
    """

    # Backtracking, Recursion
    def generateSubset(self, nums: List[int], k: int, subset: List) -> int:
        count = 0
        for index in range(len(nums)):
            if (nums[index] - k) not in subset and (nums[index] + k) not in subset:
                count += 1 + self.generateSubset(
                    nums[index + 1 :], k, subset + [nums[index]]
                )
        return count

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        return self.generateSubset(nums, k, [])
