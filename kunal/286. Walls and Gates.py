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
    # DFS, Each Gate to Cells, Time-O(m*n*(m+n)) Space-O(m*n) (TLE)
    '''
    def DFS(self, x: int, y: int, level: int) -> None:
        if x not in range(self.m) or y not in range(self.n) or self.rooms[x][y] == -1 or (x, y) in self.visited:
            return
        else:
            self.visited.add((x, y))
            self.rooms[x][y] = min(self.rooms[x][y], level)

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                self.DFS(x+dx, y+dy, level+1)

            self.visited.remove((x, y)) # You want to explore the same cell from a shorter path


    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.m = len(rooms)
        self.n = len(rooms[0])
        self.rooms = rooms

        for x in range(self.m):
            for y in range(self.n):
                if self.rooms[x][y] == 0:
                    self.visited = set()
                    self.DFS(x, y, 0)
    '''

    # BFS from All gates at once
    def BFS(self) -> None:
        for x in range(self.m):
            for y in range(self.n):
                if self.rooms[x][y] == 0:
                    self.visited.add((x, y))
                    self.queue.append((x, y, 0))

        while self.queue:
            x, y, level = self.queue.popleft()
            self.rooms[x][y] = level

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    x + dx in range(self.m)
                    and y + dy in range(self.n)
                    and self.rooms[x + dx][y + dy] != 0
                    and self.rooms[x + dx][y + dy] != -1
                    and (x + dx, y + dy) not in self.visited
                ):
                    self.visited.add((x + dx, y + dy))
                    self.queue.append((x + dx, y + dy, level + 1))

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        self.m = len(rooms)
        self.n = len(rooms[0])

        self.rooms = rooms

        self.visited = set()
        self.queue = deque()

        self.BFS()


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

Solution().wallsAndGates(rooms)

print(rooms)

rooms = [[-1]]

Solution().wallsAndGates(rooms)

print(rooms)
