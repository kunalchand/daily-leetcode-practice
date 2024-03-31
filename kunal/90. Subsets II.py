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


# https://leetcode.com/problems/subsets-ii/description/
class Solution:
    # Set (TLE Approach) (Won't give TLE just because of the constraints)
    """
    def generateSubsets(self, nums: List[int], current: List[int]) -> None:
        if tuple(sorted(current)) not in self.duplicates:
            self.subsets.append(current)
            self.duplicates.add(tuple(sorted(current)))

        for index, num in enumerate(nums):
            self.generateSubsets(nums[index+1:], current + [num])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.duplicates = set()

        # Size 0 or more
        for num in nums:
            self.generateSubsets(nums, [])

        return self.subsets
    """

    # Sort
    def generateSubsets(self, nums: List[int], current: List[int]) -> None:
        self.subsets.append(current)

        for index, num in enumerate(nums):
            if index == 0 or nums[index - 1] != nums[index]:
                self.generateSubsets(nums[index + 1 :], current + [num])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        self.subsets = []

        # Size 0 or more
        self.generateSubsets(nums, [])

        return self.subsets


print(Solution().subsetsWithDup([1, 2, 2]))
print(Solution().subsetsWithDup([0]))
