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


# https://leetcode.com/problems/rank-teams-by-votes/
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = len(votes[0])

        rank = {}

        for team in votes[0]:
            rank[team] = [0] * teams

        for voter in votes:
            for index in range(len(voter)):
                rank[voter[index]][index] += 1

        votes = [(team, ranking) for team, ranking in rank.items()]

        def custom_method(a, b):
            a_name, a_ranking = a
            b_name, b_ranking = b

            # resolve tie based on vote ranking
            for index in range(len(a_ranking)):
                if a_ranking[index] > b_ranking[index]:
                    return -1  # a comes BEFORE b
                elif a_ranking[index] < b_ranking[index]:
                    return 1  # a comes AFTER b
                elif a_ranking[index] == b_ranking[index]:
                    continue

            # alphabetically or lexicographically
            if a_name < b_name:
                return -1  # a comes BEFORE b
            elif a_name > b_name:
                return 1  # a comes AFTER b
            else:
                return 0

        votes.sort(key=cmp_to_key(custom_method))

        order = ""

        for vote in votes:
            order += vote[0]

        return order


print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
print(Solution().rankTeams(["WXYZ", "XYZW"]))
print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
