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


# https://leetcode.com/problems/car-fleet/
class Solution:
    # Iteratively Right to Left
    """
    def fleetCheck(self, target: int, leftCarPosition: int, rightCarPosition: int, leftCarSpeed: int, rightCarSpeed: int) -> bool:
        d = rightCarPosition - leftCarPosition
        if leftCarSpeed <= rightCarSpeed:
            return False
        else:
            x = (rightCarSpeed * d)/(leftCarSpeed - rightCarSpeed)
            if x <= target - rightCarPosition:
                return True
            else:
                return False

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for index in range(len(position)):
            car.append([position[index],speed[index]])

        car.sort(key = lambda x: x[0])

        fleets = 0

        rightCar = len(car)-1

        while rightCar >= 0:
            leftCar = rightCar - 1
            while leftCar >= 0:
                if self.fleetCheck(target, car[leftCar][0], car[rightCar][0], car[leftCar][1], car[rightCar][1]):
                    leftCar -= 1 # Expanding Fleet
                else:
                    fleets += 1
                    rightCar = leftCar # Search for new Fleet
                    break
            if leftCar != rightCar: # Last 1 Fleet
                fleets += 1
                break

        return fleets
    """

    # Stack Monotonic Stack (Right to Left)
    """
    class Car:
        def __init__(self, position: int, speed: int, timeToReachTarget: int) -> None:
            self.position = position
            self.speed = speed
            self.timeToReachTarget = timeToReachTarget

    def pushInStack(self, car: Car) -> None:
        if len(self.monotonic_stack) == 0:
            self.monotonic_stack.append(car)
        elif car.timeToReachTarget > self.monotonic_stack[-1].timeToReachTarget:
            self.monotonic_stack.append(car)
        
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []

        for index in range(len(position)):
            timeToReachTarget = (target - position[index]) / speed[index]
            car.append(Solution.Car(position[index], speed[index], timeToReachTarget))
        
        car.sort(key = lambda x: x.position)

        self.monotonic_stack = []

        for index in range(len(car)-1, -1, -1):
            self.pushInStack(car[index])

        return len(self.monotonic_stack)
    """

    # Stack Monotonic Stack (Left to Right)
    class Car:
        def __init__(self, position: int, speed: int, timeToReachTarget: int) -> None:
            self.position = position
            self.speed = speed
            self.timeToReachTarget = timeToReachTarget

    def pushInStack(self, car: Car) -> None:
        while (
            len(self.monotonic_stack) != 0
            and self.monotonic_stack[-1].timeToReachTarget <= car.timeToReachTarget
        ):
            self.monotonic_stack.pop()

        self.monotonic_stack.append(car)

    # def pushInStack(self, car: Car) -> None:
    #     if len(self.monotonic_stack) == 0:
    #         self.monotonic_stack.append(car)
    #     elif self.monotonic_stack[-1].timeToReachTarget > car.timeToReachTarget:
    #         self.monotonic_stack.append(car)
    #     elif self.monotonic_stack[-1].timeToReachTarget <= car.timeToReachTarget:
    #         self.monotonic_stack.pop()
    #         self.pushInStack(car)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []

        for index in range(len(position)):
            timeToReachTarget = (target - position[index]) / speed[index]
            car.append(Solution.Car(position[index], speed[index], timeToReachTarget))

        car.sort(key=lambda x: x.position)

        self.monotonic_stack = []

        for index in range(len(car)):
            self.pushInStack(car[index])

        return len(self.monotonic_stack)


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(Solution().carFleet(10, [3], [3]))
print(Solution().carFleet(100, [0, 2, 4], [4, 3, 1]))
