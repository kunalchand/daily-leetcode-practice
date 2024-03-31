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
    def validateRow(self, board: List[List[str]], row: int) -> bool:
        set_ = set()
        for col in range(len(board[row])):
            val = board[row][col]
            if val in set_ and val != ".":
                return False
            else:
                set_.add(val)
        return True

    def validateCol(self, board: List[List[str]], col: int) -> bool:
        set_ = set()
        for row in range(len(board)):
            val = board[row][col]
            if val in set_ and val != ".":
                return False
            else:
                set_.add(val)
        return True

    def validateGrid(self, board: List[List[str]], row: int, col: int) -> bool:
        set_ = set()
        for i in range(3):
            for j in range(3):
                val = board[row + i][col + j]
                if val in set_ and val != ".":
                    return False
                else:
                    set_.add(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            if not self.validateRow(board, row):
                return False

        for col in range(len(board[0])):
            if not self.validateCol(board, col):
                return False

        for row in range(0, len(board), 3):
            for col in range(0, len(board[row]), 3):
                if not self.validateGrid(board, row, col):
                    return False

        return True


print(
    Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
