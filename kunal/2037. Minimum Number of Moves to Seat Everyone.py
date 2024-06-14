import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
class Solution:
    def eliminate(self, seats: List[int], students: List[int]) -> None:
        seat_index = 0
        student_index = 0

        while seat_index < len(seats) and student_index < len(students):
            seat = seats[seat_index]
            student = students[student_index]

            if seat == student:
                seats[seat_index] *= -1
                students[student_index] *= -1

                seat_index += 1
                student_index += 1

            elif seat < student:
                seat_index += 1

            elif seat > student:
                student_index += 1

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        # Remove students who are already sitting
        self.eliminate(seats, students)

        # Start Shifting
        minHeap = []

        for seat in seats:
            if seat > 0:
                heapq.heappush(minHeap, seat)

        moves = 0
        for student in students:
            if student > 0:
                emptySeat = heapq.heappop(minHeap)
                moves += abs(student - emptySeat)

        return moves
