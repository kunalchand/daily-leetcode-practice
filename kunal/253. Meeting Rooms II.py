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


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"


class Solution:
    def isOverlap(self, old: List, new: List) -> bool:
        if new.start < old.end:
            return True
        else:
            return False

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = [Interval(interval[0], interval[1]) for interval in intervals]
        intervals.sort(key=lambda x: x.start)

        totalRooms = 1
        minHeap = []

        for interval in intervals:
            while minHeap:
                topInterval = minHeap[0]
                if self.isOverlap(topInterval, interval):
                    break
                else:
                    heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval)

            totalRooms = max(totalRooms, len(minHeap))

        return totalRooms


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(Solution().minMeetingRooms([[7, 10], [2, 4]]))
