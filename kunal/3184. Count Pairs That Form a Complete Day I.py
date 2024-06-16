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


# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        hashmap = defaultdict(list)

        count = 0
        for index, num in enumerate(nums):
            counterPart = target - num
            if counterPart in hashmap:
                count += len(hashmap[counterPart])
            hashmap[num].append(index)

        return count

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [hour % 24 for hour in hours]

        return self.twoSum(hours, 24) + self.twoSum(hours, 0)
