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


# https://leetcode.com/problems/maximize-happiness-of-selected-children/
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [-happyLevel for happyLevel in happiness]
        heapq.heapify(heap)

        maxSum = 0
        deduct = 0

        while k > 0:
            happyLevel = -heapq.heappop(heap)
            happyLevel = (happyLevel - deduct) if (happyLevel - deduct) >= 0 else 0
            maxSum += happyLevel
            deduct += 1
            k -= 1

        return maxSum
