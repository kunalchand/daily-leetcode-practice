"""
2330. Valid Palindrome IV
https://leetcode.com/problems/valid-palindrome-iv/

You are given a 0-indexed string s consisting of only lowercase English letters. 
In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing 
exactly one or two operations, or return false otherwise.

1 <= len <= 10 ^ 5

s = "abcd" => "abca" > "acca" > 
s = "abcd" => "aaa" > T


valid:
    even 
    odd: only one key should be odd, everything else should be even

    
  l    r
dcxZZZZycd

op = 2

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
    def makePalindrome(self, s: str) -> bool:
        # s = list(s)
        if len(s) != 1:
            l, r = 0, len(s) - 1
            oprs = 2

            while l <= r:
                if s[l] != s[r]:
                    # s[l] = s[r]
                    oprs -= 1

                l, r = l + 1, r - 1

            if oprs < 0:
                return False
        return True
    
    #    l r
    # abcdedcba
        #   lr
        # fecdef