"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


"a"

"()"
")(" => ""

if ( => push
if ) => pop

abc()d))
abc()d

()()())()

"((((((((" => ""

[]

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
N/A

Example 3:
N/A

Constraints:
N/A
"""

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
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_ele_idx = set()
        res = []

        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            if ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove_ele_idx.add(idx)

        if stack:
            for ele in stack:
                remove_ele_idx.add(ele)

        for idx, ch in enumerate(s):
            if idx not in remove_ele_idx:
                res.append(s[idx])

        return "".join(res)