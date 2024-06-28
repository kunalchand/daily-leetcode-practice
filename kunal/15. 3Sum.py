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
    def twoSum2(self, nums: List[int], i: int, triplets: Set) -> None:
        j, k = i+1, len(nums) - 1

        while j < len(nums) and k >= 0 and j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                self.twoSum2(nums, i, triplets)

        return [list(triplet) for triplet in triplets]
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
