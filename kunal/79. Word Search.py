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
    def searchDFS(self, board: List[List[str]], word: str, x: int, y: int) -> bool:
        if len(word) == 0:
            return True
        elif not (0 <= x < self.m) or not (0 <= y < self.n) or (x, y) in self.visited:
            return False
        elif word[0] == board[x][y]:
            self.visited.add((x, y))

            flag = (
                False
                or self.searchDFS(board, word[1:], x - 1, y)
                or self.searchDFS(board, word[1:], x, y - 1)
                or self.searchDFS(board, word[1:], x + 1, y)
                or self.searchDFS(board, word[1:], x, y + 1)
            )

            self.visited.remove((x, y))

            return flag
        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])

        self.visited = set()

        for x in range(len(board)):
            for y in range(len(board[x])):
                if self.searchDFS(board, word, x, y):
                    return True

        return False


print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)

print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
)

print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)
