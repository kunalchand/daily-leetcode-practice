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


# https://leetcode.com/problems/relative-ranks/
class Solution:
    # Using Max-Heap, Time-O(nlogn) Space-O(n)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-value, index) for index, value in enumerate(score)]
        heapq.heapify(heap)

        rank = 1

        while heap:
            _, index = heapq.heappop(heap)

            if rank == 1:
                score[index] = "Gold Medal"
            elif rank == 2:
                score[index] = "Silver Medal"
            elif rank == 3:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(rank)

            rank += 1

        return score
