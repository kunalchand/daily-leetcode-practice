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
    def checkAndRemove(self, old: List, new: List) -> List:
        old_start, old_end = old[0], old[1]
        new_start, new_end = new[0], new[1]

        if new_start < old_end:
            return [new] if new_end < old_end else [old]
        else:
            return [old, new]

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            old = result.pop()
            result.extend(self.checkAndRemove(old, interval))

        return len(intervals) - len(result)
