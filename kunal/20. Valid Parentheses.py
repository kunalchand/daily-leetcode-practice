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


class Solution:
    # Time-O(n) Space-O(n)
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "}": "{", "]": "["}
        open_brackets = set(["(", "{", "["])
        close_brackets = set([")", "}", "]"])

        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in close_brackets:
                if stack:
                    top_open = stack.pop()
                    if pair[char] != top_open:
                        return False
                else:
                    return False

        return False if stack else True


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
