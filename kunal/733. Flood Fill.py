import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


class Solution:
    def DFS(
        self, image: List[List[int]], x: int, y: int, sourceColor: int, changeColor: int
    ) -> None:
        if (
            not (0 <= x < len(image))
            or not (0 <= y < len(image[0]))
            or (x, y) in self.visited
            or image[x][y] != sourceColor
        ):
            return
        else:
            image[x][y] = changeColor
            self.visited.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.DFS(image, x + dx, y + dy, sourceColor, changeColor)

            return

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        self.visited = set()
        self.DFS(image, sr, sc, image[sr][sc], color)
        return image
