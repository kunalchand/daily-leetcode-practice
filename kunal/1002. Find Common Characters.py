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


# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordMap = []

        for word in words:
            wordMap.append(Counter(word))

        ans = []

        for char in "abcdefghijklmnopqrstuvwxyz":
            minCount = float("inf")
            for wm in wordMap:
                minCount = min(minCount, wm[char])
            for _ in range(minCount):
                ans.append(char)

        return ans
