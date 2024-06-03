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


# https://leetcode.com/problems/single-number-iii/
class Solution:
    # Time-O(n) Space-O(n)
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        ans = []
        for num, freq in hashmap.items():
            if freq == 1:
                ans.append(num)
        return ans
    """

    # Time-O(n) Space-O(1)
    # Reference (NeetCode): https://www.youtube.com/watch?v=faoVORjd-T8
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorAll = 0
        for num in nums:
            xorAll ^= num

        # binary = "".join(reversed(bin(xorAll)))
        # shifts = binary.index("1")
        # mask = 1 << shifts

        mask = xorAll & (-xorAll)

        a = 0
        b = 0

        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]
