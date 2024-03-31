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


# https://leetcode.com/problems/subsets/
class Solution:
    def generateSubsets(self, nums: List[int], current: List[int]) -> None:
        self.ans.append(current)
        for index, num in enumerate(nums):
            self.generateSubsets(nums[index + 1 :], current + [num])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        # Size 0 or more
        self.generateSubsets(nums[:], [])

        return self.ans


print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([0]))
