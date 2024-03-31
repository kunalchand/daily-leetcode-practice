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


# https://leetcode.com/problems/permutations/description/
class Solution:
    # Reduce Options Approach
    def generatePermutations(self, current: List[int], options: Set) -> None:
        if len(options) == 0:
            self.ans.append(current)
            return
        else:
            for option in options.copy():
                options.remove(option)
                self.generatePermutations(current + [option], options)
                options.add(option)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        self.generatePermutations([], set(nums))

        return self.ans


print(Solution().permute([1, 2, 3]))
print(Solution().permute([0, 1]))
print(Solution().permute([1]))
