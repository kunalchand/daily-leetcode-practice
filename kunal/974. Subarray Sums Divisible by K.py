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


# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    # Followup of LeetCode 523. Continuous Subarray Sum
    # (https://leetcode.com/problems/continuous-subarray-sum/)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        summation = 0

        for num in nums:
            summation += num
            prefixSum.append(summation % k)

        hashmap = defaultdict(list)
        for index, pS in enumerate(prefixSum):
            hashmap[pS].append(index)

        count = 0
        for indexList in hashmap.values():
            n = len(indexList)
            count += n * (n - 1) // 2

        return count
