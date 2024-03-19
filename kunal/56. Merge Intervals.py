import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Solution:
    # Approach 1: Pop the last merged/inserted interval
    """
    def checkAndMerge(self, old: List, new: List) -> List:
        old_start, old_end = old[0], old[1]
        new_start, new_end = new[0], new[1]

        if new_start <= old_end:
            return [[old_start, max(old_end, new_end)]]
        else:
            return [old, new]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            old = result.pop()
            result.extend(self.checkAndMerge(old, interval))

        return result
    """

    # Approach 2: Push till you see any non overlapping interval
    def checkAndMerge(self, old: List, new: List) -> List:
        old_start, old_end = old[0], old[1]
        new_start, new_end = new[0], new[1]

        if new_start <= old_end:
            return [[old_start, max(old_end, new_end)]]
        else:
            return [old, new]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        old = intervals[0]

        for interval in intervals[1:]:
            # Overlapping
            if len(self.checkAndMerge(old, interval)) == 1:
                old = self.checkAndMerge(old, interval)[0]
            # Non-Overlapping
            else:
                result.append(old)
                old = self.checkAndMerge(old, interval)[1]

        result.append(old)

        return result
