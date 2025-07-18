import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/multiply-strings/
class Solution:
    def generate_the_int_version(self, num: str) -> int:
        num_int = 0
        multiply_factor = 1
        for index in range(len(num) - 1, -1, -1):
            char = num[index]
            digit = ord(char) - ord("0")
            num_int += digit * multiply_factor
            multiply_factor *= 10
        return num_int

    def multiply(self, num1: str, num2: str) -> str:
        num1_int = self.generate_the_int_version(num1)
        num2_int = self.generate_the_int_version(num2)

        return str(num1_int * num2_int)
