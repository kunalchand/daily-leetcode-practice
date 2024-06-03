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


# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tDq = deque(list(t))

        for char in s:
            if tDq and char == tDq[0]:
                tDq.popleft()

        return len(tDq)
