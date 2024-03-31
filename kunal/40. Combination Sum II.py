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


# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    # Set (TLE)
    """
    def generateCombination(self, candidates: List[int], target: int, current: List[int]) -> None:
        if sum(current) == target:
            if tuple(sorted(current)) not in self.duplicates:
                self.ans.append(current)
                self.duplicates.add(tuple(sorted(current)))
            return
        elif sum(current) > target:
            return
        else:
            for index, candidate in enumerate(candidates):
                self.generateCombination(candidates[index+1:], target, current + [candidate])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.duplicates = set()

        self.generateCombination(candidates, target, [])

        return self.ans
    """

    # Sort
    def generateCombination(
        self, candidates: List[int], target: int, current: List[int]
    ) -> None:
        if sum(current) == target:
            self.ans.append(current)
            return
        elif sum(current) > target:
            return
        else:
            for index, candidate in enumerate(candidates):
                if index == 0 or candidates[index - 1] != candidates[index]:
                    self.generateCombination(
                        candidates[index + 1 :], target, current + [candidate]
                    )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.ans = []

        self.generateCombination(candidates, target, [])

        return self.ans


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
