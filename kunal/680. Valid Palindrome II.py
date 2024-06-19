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
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def checkPalindrome(self, s: Deque) -> bool:
        s = "".join(s)
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        dq = deque(s)

        while dq:
            if dq[0] == dq[-1]:
                dq.popleft()
                if dq:
                    dq.pop()
            else:
                left = dq.popleft()
                right = dq.pop()
                return self.checkPalindrome(
                    dq + deque([right])
                ) or self.checkPalindrome(deque([left]) + dq)

        return True
