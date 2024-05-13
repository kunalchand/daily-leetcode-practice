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


class Solution:
    def flipRow(self, grid: List[List[int]], row: int) -> None:
        for col in range(self.n):
            if grid[row][col] == 0:
                self.colZero[col] -= 1
                grid[row][col] = 1
            elif grid[row][col] == 1:
                self.colZero[col] += 1
                grid[row][col] = 0

    def flipCol(self, grid: List[List[int]], col: int) -> None:
        for row in range(self.m):
            if grid[row][col] == 0:
                self.colZero[col] -= 1
                grid[row][col] = 1
            elif grid[row][col] == 1:
                self.colZero[col] += 1
                grid[row][col] = 0

    def matrixScore(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.colZero = [-1] * self.n

        # Fill colZero
        for col in range(self.n):
            count = 0
            for row in range(self.m):
                if grid[row][col] == 0:
                    count += 1
            self.colZero[col] = count

        # Modifying the most significant bit
        for row in range(self.m):
            if grid[row][0] == 0:
                self.flipRow(grid, row)

        # Modifying columns to eliminate 0s
        for col in range(1, self.n):
            if self.colZero[col] > self.m // 2:
                self.flipCol(grid, col)

        # Convert each row to int
        score = 0
        for row in range(self.m):
            num = 0
            for col in range(self.n):
                if grid[row][col] == 1:
                    num += 1 << (self.n - col - 1)
            score += num

        return score

    """
    Greedy Proof:
    I see some people are struggling to get an intuition or proof for the greedy solution.
    The idea is that the priority is to make the msot sigificant bit 1, 
    even if it means sacrificing the least significant bit to 0s.
    eg. 01101
    Even if you manage to convert this to 01111, It will still be less than 10000.
    Hence the first greedy step is to convert the most signifcant bit to 1.
    So 10010.
    Now the game is to maximise the other significant bits. 
    But if we now do any row operation, it will affect the highest significant bit, 
    so we can now only do column opereation. Hence do column operation if number of 
    0s are more than 1s. Why?
    10010
    11001
    10110
    and
    10010
    10001
    11110
    The only difference between them is the placement of 1. But the sum will still the same. 
    So no matter where the 1 is in a column, as long as the frequency of number of 1s is greater 
    than 0s, it will increase our sum.
    """
