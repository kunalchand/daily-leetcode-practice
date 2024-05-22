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


# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    # Backtracking, Recursion
    """
    def isPalindrome(self, s: str) -> bool:
        return s == "".join(reversed(s))

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        ans = []

        for index in range(1, len(s) + 1):
            if self.isPalindrome(s[:index]):
                for partition in self.partition(s[index:]):
                    ans.append([s[:index]] + partition)

        return ans
    """

    # DP, Top Down Memoization
    def isPalindrome(self, s: str) -> bool:
        return s == "".join(reversed(s))

    def palindromePartitioning(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        ans = []

        for index in range(1, len(s) + 1):
            if self.isPalindrome(s[:index]):
                if s[index:] not in self.memo:
                    self.memo[s[index:]] = self.palindromePartitioning(s[index:])
                for partition in self.memo[s[index:]]:
                    ans.append([s[:index]] + partition)

        return ans

    def partition(self, s: str) -> List[List[str]]:
        self.memo = {}

        return self.palindromePartitioning(s)
