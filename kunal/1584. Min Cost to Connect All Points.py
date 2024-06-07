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


# https://leetcode.com/problems/min-cost-to-connect-all-points/
class Solution:
    # Prims
    """
    def manhattanDistance(self, point: List[int], otherPoint: List[int]) -> int:
        x_point, y_point = point
        x_otherPoint, y_otherPoint = otherPoint

        return abs(x_point - x_otherPoint) + abs(y_point - y_otherPoint)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Generate Graph
        for point in points:
            for otherPoint in points:
                if point != otherPoint:
                    graph[tuple(point)].append((self.manhattanDistance(point, otherPoint), otherPoint[0], otherPoint[1]))

        minHeap = []
        visited = set()
        cost = 0

        # Begin from first node
        firstNode = points[0]
        visited.add(tuple(firstNode))
        for edge in graph[tuple(firstNode)]:
            heapq.heappush(minHeap, edge)

        # Keep choosing till all nodes gets visited
        while len(visited) != len(points):
            topEdge = minHeap[0]
            distance = topEdge[0]
            coordinate = (topEdge[1], topEdge[2])

            if coordinate in visited:
                heapq.heappop(minHeap)
            else:
                cost += distance
                visited.add(coordinate)
                for edge in graph[coordinate]:
                    heapq.heappush(minHeap, edge)

        return cost
    """

    # Krushkals
    def findRoot(self, point: Optional[Tuple]) -> str:
        if point not in self.roots:
            return point
        else:
            return self.findRoot(self.roots[point])

    def mergeRoots(self, pointRoot: str, otherPointRoot: str) -> None:
        self.roots[otherPointRoot] = pointRoot

    def manhattanDistance(self, point: List[int], otherPoint: List[int]) -> int:
        x_point, y_point = point
        x_otherPoint, y_otherPoint = otherPoint

        return abs(x_point - x_otherPoint) + abs(y_point - y_otherPoint)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        # Generate Edges
        visitedPoint = set()
        for pointIndex in range(len(points)):
            for otherPointIndex in range(pointIndex + 1, len(points)):
                point = points[pointIndex]
                otherPoint = points[otherPointIndex]
                if point != otherPoint:
                    edges.append(
                        (
                            self.manhattanDistance(point, otherPoint),
                            point[0],
                            point[1],
                            otherPoint[0],
                            otherPoint[1],
                        )
                    )

        edges.sort()

        self.roots = {}

        # Create Roots
        rootCount = 1
        for point in points:
            self.roots[tuple(point)] = "root" + str(rootCount)
            rootCount += 1

        cost = 0

        for edge in edges:
            distance, pointX, pointY, otherPointX, otherPointY = edge
            pointRoot = self.findRoot((pointX, pointY))
            otherPointRoot = self.findRoot((otherPointX, otherPointY))
            if pointRoot != otherPointRoot:
                cost += distance
                self.mergeRoots(pointRoot, otherPointRoot)

        return cost


print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
