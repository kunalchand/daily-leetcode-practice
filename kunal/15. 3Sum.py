import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


class Solution:
    # Time-O(n*n + n*logn) Two Pointer w/ sort
    """
    def twoSum2(self, nums: List[int], i: int, set_: Set) -> None:
        j, k = i+1, len(nums) - 1

        while j < len(nums) and k < len(nums) and j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                set_.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        set_ = set()

        for i in range(len(nums)):
            self.twoSum2(nums, i, set_)

        return [list(tuple_) for tuple_ in set_]
    """

    # Time-O(n*n) HashMap w/o sort
    # Reference: https://www.youtube.com/watch?v=DhFh8Kw7ymk
    def twoSumOnePass(self, nums: List[int], i: int, set_: Set) -> None:
        exist_set = set()
        for k in range(i + 1, len(nums)):
            j_element = 0 - (nums[i] + nums[k])
            if j_element in exist_set:
                set_.add(tuple(sorted([nums[i], j_element, nums[k]])))

            exist_set.add(nums[k])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set_ = set()
        duplicate_set = set()  # Optimization for [0, 0, 0, ... 0]

        for i in range(len(nums)):
            if nums[i] not in duplicate_set:
                self.twoSumOnePass(nums, i, set_)
                duplicate_set.add(nums[i])

        return [list(tuple_) for tuple_ in set_]
