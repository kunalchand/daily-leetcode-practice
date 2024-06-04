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


# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        longest = 0
        oddFound = False
        for char, freq in count.items():
            if freq % 2 == 0:
                longest += freq
            else:
                if freq > 1:
                    longest += freq - 1
                oddFound = True

        if oddFound:
            return longest + 1
        else:
            return longest
