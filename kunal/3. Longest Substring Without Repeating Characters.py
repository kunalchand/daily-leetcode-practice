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


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # Brute Force Time-O(n*n*n) Space-O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for index, _ in enumerate(s):
            for pointer in range(index, len(s)):
                found = False
                for i in range(index, pointer):
                    if s[i] == s[pointer]:
                        found = True
                        break
                if not found:
                    max_length = max(max_length, pointer - index + 1)
                else:
                    break

        return max_length
    """

    # Brute Force Time-O(n*n) Space-O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for index, _ in enumerate(s):
            set_ = set()
            for pointer in range(index, len(s)):
                if s[pointer] not in set_:
                    max_length = max(max_length, pointer - index + 1)
                    set_.add(s[pointer])
                else:
                    break
        
        return max_length
    """

    # Sliding Window Implemntation 1, Time-O(n) Space-O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        set_ = set()

        start = 0
        end = 0

        while end < len(s):
            if s[end] not in set_:
                max_length = max(max_length, end - start + 1)
                set_.add(s[end])
                end += 1
            else:
                set_.remove(s[start])
                start += 1

        return max_length
    """

    # Sliding Window Implemntation 2, Time-O(n) Space-O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        elementsInWindow = set()
        longest = 0

        for char in s:
            if char not in elementsInWindow:
                elementsInWindow.add(char)
                longest = max(longest, len(elementsInWindow))
            else:
                while char in elementsInWindow:
                    elementsInWindow.remove(s[left])
                    left += 1
                elementsInWindow.add(char)
                longest = max(longest, len(elementsInWindow))

        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
