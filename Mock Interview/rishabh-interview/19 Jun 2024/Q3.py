"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/

There is a car with capacity empty seats. The vehicle only drives east 
(i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where 
trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has 
numPassengersi passengers and the locations to pick them up and 
drop them off are fromi and toi respectively. The locations are given 
as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all 
passengers for all the given trips, or false otherwise.

1 -> 4

(P,1,2) (P,2,3), (P,3,4)

1 

Example:
    Input: trips = [[2,1,5],[3,5,7]], capacity = 5 => 

    trips = [ 
        
        1 -> [[v, S]]
        5 -> [[2, E], [3, S]]
        [3, S] -> v
        [7, E] -> v
        
        ]

    Output: true

    trips [A, B, C]

  2       2
0 1 2 3 4 5 6 7 8 
      3       3
        1   1

0 2 2 5 6 4 3 0             
        
1 9

1000 * 1000 => 10 ^ 6
 
n -> len(t)
m -> range

O(n + m)
O(m)


1 6 
2 7
3 8



"""

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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cust_map = defaultdict(list)

        for trip in trips:
            p, s, e = trip
            cust_map[s].append([p,"S"])
            cust_map[e].append([p,"E"])
        
        curr_cap = 0
        for i in range(1001):
            if i in cust_map:

                for psngr, sep in cust_map[i]:
                    if sep == "S":
                        curr_cap += psngr
                    else:
                        curr_cap -= psngr

                if curr_cap > capacity:
                    return False 
            
        return True