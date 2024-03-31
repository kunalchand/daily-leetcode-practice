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
    # Time-O(n + n) Space-O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        lcs = 0
        for num in nums:
            if num - 1 in set_:
                # Ignore as sequence already exists with num-1
                # Why? => Start streak only from the lowest element
                pass
            else:
                # New possible streak element
                current_num = num
                current_streak = 1

                while current_num + 1 in set_:
                    current_streak += 1
                    current_num += 1

                lcs = max(lcs, current_streak)

        return lcs


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
