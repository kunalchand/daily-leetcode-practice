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


class Solution:
    # O(n*maxPile)
    """
    def kIsSufficient(self, piles: List[int], h: int, k: int) -> bool:
        time = 0

        for pile in piles:
            time += math.ceil(pile/k)

        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(1, max(piles)+1):
            if self.kIsSufficient(piles, h, k):
                return k

        return -1
    """

    # O(n*log(maxPile))
    def kIsSufficient(self, piles: List[int], h: int, k: int) -> bool:
        time = 0

        for pile in piles:
            time += math.ceil(pile / k)

        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            if self.kIsSufficient(piles, h, mid):
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1

        return k
