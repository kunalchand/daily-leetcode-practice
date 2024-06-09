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


# https://leetcode.com/problems/maximum-total-reward-using-operations-i/
class Solution:
    # DP Top Down Memoization
    def recursion(self, r: List[int], i: int, x: int) -> int:
        if (i, x) in self.memo:
            return self.memo[(i, x)]

        # if x goes more than the largest reward, then can't choose anything
        if i == len(r) or x >= r[-1]:
            return 0
        else:
            if r[i] > x:
                choose = r[i] + self.recursion(r, i + 1, x + r[i])
                notChoose = self.recursion(r, i + 1, x)
                self.memo[(i, x)] = max(choose, notChoose)
            else:
                notChoose = self.recursion(r, i + 1, x)
                self.memo[(i, x)] = notChoose

            return self.memo[(i, x)]

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # rewardValues = sorted(list(set(rewardValues)))
        rewardValues.sort()
        self.memo = {}
        return self.recursion(rewardValues, 0, 0)
