"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters

Edge Case
1 => str
2 => "aa" -> ""
3 => "aaba"

Brute Force:
-----
5*4*3*2*1 O(N!)
O(n)

Optimal Approach:
"aaaaaaaaaaaaabbbbbbbbbb"

a b c d e f g

aaaab

"a b a " ""

Time - O(n logn)
Space - O(n)

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

"""
Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
"""


class Solution:
    def pushInHeap(self, maxHeap: List, freq: int, char: str) -> None:
        if freq > 0:
            heapq.heappush(maxHeap, [-freq, char])

    def reorganizeString(self, s: str) -> str:
        # generate dictionary
        charCount = defaultdict(int)
        for char in s:
            charCount[char] += 1

        # generate heap
        maxHeap = []
        for char, freq in charCount.items():
            heapq.heappush(maxHeap, [-freq, char])

        ans = ""

        # generate ans
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            freq *= -1

            if ans == "":
                ans += char
                self.pushInHeap(maxHeap, freq - 1, char)
            else:
                if ans[-1] == char:
                    if not maxHeap:
                        return ""
                    else:
                        secondFreq, secondChar = heapq.heappop(maxHeap)
                        secondFreq *= -1

                        ans += secondChar
                        self.pushInHeap(maxHeap, secondFreq - 1, secondChar)
                        self.pushInHeap(maxHeap, freq, char)
                else:
                    ans += char
                    self.pushInHeap(maxHeap, freq - 1, char)

        return ans
