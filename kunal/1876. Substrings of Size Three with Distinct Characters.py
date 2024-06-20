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


# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
class Solution:
    # Brute Force w/ slicing
    """
    def isGood(self, substring: str) -> bool:
        return len(set(list(substring))) == 3

    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s) - 2):
            if self.isGood(s[index : index + 3]):
                count += 1
        return count
    """

    # Brute Force w/o slicing
    """
    def isGood(self, hashset: Set) -> bool:
        return len(hashset) == 3

    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s) - 2):
            hashset = set()
            for idx in range(index, index+3):
                hashset.add(s[idx])
            if self.isGood(hashset):
                count += 1
        return count
    """

    # Sliding Window
    def countGoodSubstrings(self, s: str) -> int:
        hashset = set()
        sliding_window = deque()
        s = deque(s)

        count = 0

        while s:
            char = s.popleft()
            if sliding_window:
                if char in hashset:
                    while sliding_window and char in hashset:
                        hashset.remove(sliding_window.popleft())
                    sliding_window.append(char)
                    hashset.add(char)
                    if len(sliding_window) == 3 and len(hashset) == 3:
                        count += 1
                elif char not in hashset:
                    sliding_window.append(char)
                    hashset.add(char)

                    if len(sliding_window) == 3 and len(hashset) == 3:
                        count += 1
                    elif len(sliding_window) > 3:
                        hashset.remove(sliding_window.popleft())
                        if len(hashset) == 3:
                            count += 1

            elif not sliding_window:
                sliding_window.append(char)
                hashset.add(char)

        return count
