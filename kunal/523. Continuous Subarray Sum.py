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


# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    # Reference (Aryan Mittal): https://www.youtube.com/watch?v=1W_HYBqvDLw
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = [0]
        summation = 0

        for num in nums:
            summation += num
            prefixSum.append(summation % k)

        hashmap = defaultdict(list)
        for index, pS in enumerate(prefixSum):
            hashmap[pS].append(index)

        for indexList in hashmap.values():
            if indexList[-1] - indexList[0] > 1:
                return True

        return False
