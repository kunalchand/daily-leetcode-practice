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


# https://leetcode.com/problems/score-of-a-string/
class Solution:
    # Default For Loop, Time-O(n), Space-O(1)
    """
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index in range(len(s) - 1):
            score += abs(ord(s[index]) - ord(s[index + 1]))
        return score
    """

    # One Liner Index, Time-O(n), Space-O(1)
    """
    def scoreOfString(self, s: str) -> int:
        return sum(
            abs(ord(s[index]) - ord(s[index + 1])) for index in range(len(s) - 1)
        )
    """

    # Using itertools.pairwise, Time-O(n), Space-O(1)
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))


print(Solution().scoreOfString("hello"))
print(Solution().scoreOfString("zaz"))
