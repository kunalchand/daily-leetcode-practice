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
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for index in range(1, len(intervals)):
            if intervals[index][0] < intervals[index - 1][1]:
                return False

        return True


print(Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(Solution().canAttendMeetings([[7, 10], [2, 4]]))
