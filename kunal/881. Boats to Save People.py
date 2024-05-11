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


# https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = deque(sorted(people))

        boat = 0

        while people and len(people) > 1:
            if people[-1] + people[0] > limit:
                people.pop()
                boat += 1
            else:
                people.pop()
                people.popleft()
                boat += 1

        return boat if not people else boat + 1
