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
    def checkAndMerge(self, original, new) -> List[int]:
        original_start = original[0]
        original_end = original[1]

        new_start = new[0]
        new_end = new[1]

        if new_start < original_start:
            if new_end < original_start:
                return [new, original]
            else:
                return [[new_start, max(original_end, new_end)]]
        elif new_start == original_start:
            return [[new_start, max(original_end, new_end)]]
        elif new_start <= original_end:
            return [[original_start, max(original_end, new_end)]]
        else:
            return [original, new]

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = [newInterval]

        for interval in intervals:
            newInterval = result.pop()
            result.extend(self.checkAndMerge(interval, newInterval))

        return result
