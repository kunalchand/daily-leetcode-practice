import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/valid-anagram/
class Solution:
    # Sort & Compare, Time-O(n logn) Space-O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)
        return s1==s2
    """

    # HashTable, Time-O(n) Space-O(n)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)
        
        if s_map == t_map:
            return True
        else:
            return False
    """

    # Array, Time-O(n) Space-O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = [0] * 26
        t_array = [0] * 26

        for s_char in s:
            s_array[ord(s_char) - ord("a")] += 1

        for t_char in t:
            t_array[ord(t_char) - ord("a")] += 1

        for index in range(26):
            if s_array[index] != t_array[index]:
                return False

        return True


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
