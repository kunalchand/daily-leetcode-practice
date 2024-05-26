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


# https://leetcode.com/problems/faulty-keyboard/
class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for char in s:
            if char == "i":
                ans = "".join(reversed(ans))
            else:
                ans += char
        return ans
