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


# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while True:
            squareSum = 0
            for char in str(n):
                squareSum += int(char) ** 2

            if squareSum == 1:
                return True
            elif squareSum in hashset:
                return False

            hashset.add(squareSum)
            n = squareSum
