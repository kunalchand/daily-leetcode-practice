import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Solution:
    # Time-O(n) Space-O(n) Reversed
    """
    def removeOtherCharacters(self, s: str) -> str:
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += str.lower(char)

        return new_string

    def isPalindrome(self, s: str) -> bool:
        s = self.removeOtherCharacters(s)

        s_reversed = "".join(reversed(s))

        if s == s_reversed:
            return True
        else:
            return False
    """

    # Time-O(n) Space-O(n) Two Pointer
    """
    def removeOtherCharacters(self, s: str) -> str:
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += str.lower(char)
        
        return new_string

    def isPalindrome(self, s: str) -> bool:
        s = self.removeOtherCharacters(s)

        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
    """

    # Time-O(n) Space-O(1) Two Pointer
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            while start < len(s) and not s[start].isalnum():
                start += 1

            while end >= 0 and not s[end].isalnum():
                end -= 1

            if start <= end and str.lower(s[start]) != str.lower(s[end]):
                return False

            start += 1
            end -= 1

        return True
