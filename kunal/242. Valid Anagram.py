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


class Solution:
    # Sort & Compare Time-O(n logn) Space-O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)
        return s1==s2
    """

    # HashTable Time-O(n) Space-O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if s_map == t_map:
            return True
        else:
            return False


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
