"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/

There is a car with capacity empty seats. The vehicle only drives east 
(i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where 
trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has 
numPassengersi passengers and the locations to pick them up and 
drop them off are fromi and toi respectively. The locations are given 
as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all 
passengers for all the given trips, or false otherwise.

Example:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
"""

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


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass
