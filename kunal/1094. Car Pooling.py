import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/car-pooling/
class Solution:
    # Heap, Time-O(nlogn) Space-O(n)
    # Similar to 253. Meeting Rooms II: https://leetcode.com/problems/meeting-rooms-ii/
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [(f, t, num) for num, f, t in trips]
        trips.sort()

        minHeap = []
        peopleInCar = 0
        for trip in trips:
            while minHeap and minHeap[0][0] <= trip[0]:
                peopleInCar -= heapq.heappop(minHeap)[2]

            heapq.heappush(minHeap, (trip[1], trip[0], trip[2]))
            peopleInCar += trip[2]

            if peopleInCar > capacity:
                return False

        return True
    """

    # PrefixSum, Time-O(nlogn) Space-O(n)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []

        for trip in trips:
            num, f, t = trip
            timestamps.append([f, num])
            timestamps.append([t, -num])

        timestamps.sort()

        peopleInCar = 0

        for timestamp in timestamps:
            time, people = timestamp
            peopleInCar += people

            if peopleInCar > capacity:
                return False

        return True
