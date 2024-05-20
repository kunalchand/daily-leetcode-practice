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


# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
class Solution:
    def formSubset(self, XOR: int, nums: List[int]) -> None:
        self.sumation += XOR

        for index, num in enumerate(nums):
            self.formSubset(num ^ XOR, nums[index + 1 :])

    def subsetXORSum(self, nums: List[int]) -> int:
        self.sumation = 0
        self.formSubset(0, nums)
        return self.sumation
