"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.

abac => t
abba => t

abca => aba


    l         r
b a c b b b a c b


  l r
a b c a


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
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(st):
            return st == st[::-1]

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                # skip R
                l = l
                r -= 1
                first_res = is_palindrome(s[l:r+1])
                r += 1


                # skip L
                l += 1
                r = r
                second_res = is_palindrome(s[l:r+1])
                break

            l, r = l + 1, r - 1    

        return first_res or second_res 
   