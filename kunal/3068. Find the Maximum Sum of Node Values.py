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


# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
class Solution:
    # Reference (Aryan Mittal): https://www.youtube.com/watch?v=3t7y4mBJDoM
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        pos = []
        neg = []

        for num in nums:
            if (num ^ k) > num:
                pos.append((num ^ k) - num)
            else:
                neg.append((num ^ k) - num)

        # Even nodes to operate (flip)
        if len(pos) % 2 == 0:
            return sum(nums) + sum(pos)
        # Odd nodes to operate (flip)
        else:
            if len(neg) == 0:
                return sum(nums) + sum(pos) - min(pos)
            else:
                return max(
                    sum(nums) + sum(pos) - min(pos), sum(nums) + sum(pos) + max(neg)
                )
