import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        c = 0
        direction = "up"
        for _ in range(k):
            if c == n - 1:
                direction = "down"
            elif c == 0:
                direction = "up"

            if direction == "down":
                c -= 1
            elif direction == "up":
                c += 1

        return c
