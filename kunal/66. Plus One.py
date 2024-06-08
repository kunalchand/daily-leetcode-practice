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


# https://leetcode.com/problems/plus-one/
class Solution:
    # int & str conversion
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        newDigits = list(str(int("".join(digits)) + 1))
        return [int(newDigit) for newDigit in newDigits]
    """

    # carry (right to left)
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            digits[index] += carry
            if digits[index] > 9:
                carry = 1
            else:
                carry = 0
            digits[index] %= 10

        if carry == 1:
            digits.insert(0, 1)

        return digits
