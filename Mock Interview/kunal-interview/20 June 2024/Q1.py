"""
1876. Substrings of Size Three with Distinct Characters
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/    
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".


Brute:
[a b c d e f g h i j k] O(n-3) * O(m) * O(3) = O(n) * (m + m)

Sliding Window:
xyzbbz

{y, z, b} O(m) - > O(1)
"""

import bisect
import copy
import enum
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


class Solution:
    # Sliding Window Time-Complexity: O(n) | Space-Complexity: O(m)
    """
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        hashset = set()
        sliding_window = deque()

        count = 0
        index = 0

        'axbc'
        '[axb]'
        while index < len(s):
            char = s[index]
            if char in hashset:
                pass
            else:
                if len(sliding_window) < 3:
                    sliding_window.append(char)
                elif len(sliding_window) == 3:
                    count += 1
    """

    "xyzzaz"

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

    def isGood(self, hashset: Set) -> bool:
        return len(hashset) == 3

    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s) - 2):
            hashset = set()
            for idx in range(index, index + 3):
                hashset.add(s[idx])
            if self.isGood(hashset):
                count += 1
        return count
