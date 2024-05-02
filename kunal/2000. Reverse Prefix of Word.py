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


# https://leetcode.com/problems/reverse-prefix-of-word/
class Solution:
    # Using InBuilt Reverse
    """
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            for index, character in enumerate(word):
                if character == ch:
                    return "".join(reversed(word[:index+1])) + word[index+1:]
    """

    # Using Stack
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            ans = ""
            stack = []

            for index, character in enumerate(word):
                stack.append(character)
                if character == ch:
                    while stack:
                        ans += stack.pop()

                    return ans + word[index + 1 :]


print(Solution().reversePrefix(word="abcdefd", ch="d"))
print(Solution().reversePrefix(word="xyxzxe", ch="z"))
print(Solution().reversePrefix(word="abcd", ch="z"))
