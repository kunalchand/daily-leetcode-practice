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


# https://leetcode.com/problems/edit-distance
class Solution:
    # Recursion, Time-O(3^?), Space-O(1) (TLE)
    """
    def recursion(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        else:
            # Do Nothing
            if word1[0] == word2[0]:
                return 0 + self.recursion(word1[1:], word2[1:])
            else:
                # Insert
                insert = 1 + self.recursion(word1, word2[1:])

                # Delete
                delete = 1 + self.recursion(word1[1:], word2)

                # Replace
                replace = 1 + self.recursion(word1[1:], word2[1:])

                return min(insert, delete, replace)

    def minDistance(self, word1: str, word2: str) -> int:
        return self.recursion(word1, word2)
    """

    # DP, Top Down Memoization, Time-O(n*m) Space-O(n*m)
    def recursion(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        if word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        else:
            # Do Nothing
            if word1[0] == word2[0]:
                self.memo[(word1, word2)] = 0 + self.recursion(word1[1:], word2[1:])
                return self.memo[(word1, word2)]
            else:
                # Insert
                insert = 1 + self.recursion(word1, word2[1:])

                # Delete
                delete = 1 + self.recursion(word1[1:], word2)

                # Replace
                replace = 1 + self.recursion(word1[1:], word2[1:])

                self.memo[(word1, word2)] = min(insert, delete, replace)
                return self.memo[(word1, word2)]

    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}
        return self.recursion(word1, word2)
