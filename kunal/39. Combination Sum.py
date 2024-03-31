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


# https://leetcode.com/problems/combination-sum/
class Solution:
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
                self.generateCombination(
                    candidates[index:], target, current + [candidate]
                )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        self.generateCombination(candidates, target, [])

        return self.ans


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2], 1))
