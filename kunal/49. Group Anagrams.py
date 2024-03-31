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
    # Sorted String as Key Time-O(n*k*logk) Space-O(n*k) n=strs.length, k=max(strs[i].length)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            buckets[sorted_string].append(string)

        return buckets.values()
    """

    # Character Count Time-O(n*k) Space-O(n*26) n=strs.length, k=max(strs[i].length)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for str_ in strs:
            count = [0] * 26
            for char in str_:
                count[ord(char) - ord("a")] += 1
            buckets[tuple(count)].append(str_)

        return buckets.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
