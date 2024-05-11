import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from curses.ascii import SO
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        max_len = max(len(v1), len(v2))
        v1 += ["0"] * (max_len - len(v1))
        v2 += ["0"] * (max_len - len(v2))

        for r1, r2 in zip(v1, v2):
            if int(r1) < int(r2):
                return -1
            elif int(r1) > int(r2):
                return 1

        return 0


print(Solution().compareVersion("1.2", "1.10"))
print(Solution().compareVersion("1.01", "1.001"))
print(Solution().compareVersion("1.0", "1.0.0.0"))
