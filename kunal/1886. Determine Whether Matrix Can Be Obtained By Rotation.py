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


# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
class Solution:
    def compare(self) -> None:
        return self.mat == self.target

    def reverse(self) -> None:
        for row in range(self.n):
            self.mat[row] = list(reversed(self.mat[row]))

    def transpose(self) -> None:
        for row in range(self.n):
            for col in range(self.n):
                if row > col:
                    self.mat[row][col], self.mat[col][row] = (
                        self.mat[col][row],
                        self.mat[row][col],
                    )

    def rotate(self) -> None:
        self.transpose()
        self.reverse()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.mat = mat
        self.target = target
        self.n = len(mat)

        for _ in range(5):
            if self.compare():
                return True
            self.rotate()

        return False
