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


# https://leetcode.com/problems/powx-n/
class Solution:
    # loop product (TLE)
    """
    def myPow(self, x: float, n: int) -> float:
        neg = True if n < 0 else False
        n = abs(n)

        product = 1
        for _ in range(n):
            product *= x

        if neg:
            return 1/product
        else:
            return product
    """

    # recursion
    """
    def binaryExponent(self, x: float, n: int) -> float:
        track = 1
        product = x

        while track < n:
            track += track
            product *= product
        
        if track == n:
            return product
        elif track > n:
            track //= 2
            product = sqrt(product)
            return product*self.myPow(x, n-track)

    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            return 1/self.binaryExponent(x, abs(n))
        elif n > 0:
            return self.binaryExponent(x, n)
        elif n == 0:
            return 1
    """

    # mycodeschool
    # Ref: https://www.youtube.com/watch?v=wAyrtLAeWvI
    def calPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            y = self.myPow(x, n / 2)
            return y * y
        else:
            return x * self.myPow(x, n - 1)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.calPow(x, abs(n))
        elif n > 0:
            return self.calPow(x, n)
        elif n == 0:
            return 1
