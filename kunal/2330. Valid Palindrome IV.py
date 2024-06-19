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


# https://leetcode.com/problems/valid-palindrome-iv/
class Solution:
    # Two Pointer w/ Deque, Time-O(n), Space-O(n)
    def makePalindrome(self, s: str) -> bool:
        dq = deque(list(s))

        count = 0
        while dq:
            if dq[0] != dq[-1]:
                count += 1
                if count > 2:
                    return False
            dq.popleft()
            if dq:
                dq.pop()

        return True
