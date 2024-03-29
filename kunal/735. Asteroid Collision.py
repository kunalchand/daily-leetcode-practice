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

# Doubly Linked List Approach
"""
class Asteroid:
    def __init__(self, size: int, direction: str) -> None:
        self.size = size
        self.direction = direction
        self.previous = None
        self.next = None
    
    def __repr__(self) -> str:
        return "(" + str(self.size) + ", " + self.direction + ")"


class Solution:
    def printAsteroidInSpace(self, head: "Asteroid") -> None:
        currentAsteroid = head
        while True:
            print(currentAsteroid, end="->")
            currentAsteroid = currentAsteroid.next
            if currentAsteroid.direction == "tail":
                print(currentAsteroid)
                break
                
    def willCollide(self, previousAsteroid: 'Asteroid', currentAsteroid: 'Asteroid') -> bool:
        if previousAsteroid.direction == "head" or currentAsteroid.direction == "tail":
            return False
        elif previousAsteroid.direction == "right" and currentAsteroid.direction == "left":
            return True
        else:
            return False

    def insertNewAsteroid(self, left: 'Asteroid', mid: 'Asteroid', right: 'Asteroid') -> None:
        left.next = mid
        
        mid.previous = left
        mid.next = right

        right.previous = mid

    def removePreviousAsteroid(self, currentAsteroid: 'Asteroid') -> 'Asteroid':
        currentAsteroid.previous = currentAsteroid.previous.previous
        currentAsteroid.previous.next = currentAsteroid
        return currentAsteroid
    
    def removeCurrentAsteroid(self, currentAsteroid: 'Asteroid') -> 'Asteroid':
        currentAsteroid.previous.next = currentAsteroid.next
        currentAsteroid.next.previous = currentAsteroid.previous
        return currentAsteroid.previous

    def removeBothAsteroids(self, currentAsteroid: 'Asteroid') -> 'Asteroid':
        currentAsteroid.previous.previous.next = currentAsteroid.next
        currentAsteroid.next.previous = currentAsteroid.previous.previous
        return currentAsteroid.next
    
    def generateLeftOver(self, asteroid: 'Asteroid') -> None:
        while asteroid.direction != "tail":
            self.leftOver.append(asteroid.size if asteroid.direction == "right" else (asteroid.size*(-1)))
            asteroid = asteroid.next

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        head = Asteroid(0, "head")
        tail = Asteroid(0, "tail")

        head.next = tail
        tail.previous = head
        
        # self.printAsteroidInSpace(head)

        currentAsteroid = head
        for asteroid in asteroids:
            newAsteroid = Asteroid(abs(asteroid), "left" if asteroid < 0 else "right")
            self.insertNewAsteroid(currentAsteroid, newAsteroid, currentAsteroid.next)
            currentAsteroid = newAsteroid

        currentAsteroid = head.next

        # self.printAsteroidInSpace(head)
        # print(currentAsteroid)

        while True:
            if currentAsteroid.direction == "right":
                currentAsteroid = currentAsteroid.next
            elif currentAsteroid.direction == "left":
                while True:
                    if self.willCollide(currentAsteroid.previous, currentAsteroid):
                        if currentAsteroid.previous.size < currentAsteroid.size:
                            currentAsteroid = self.removePreviousAsteroid(currentAsteroid)
                        elif currentAsteroid.previous.size > currentAsteroid.size:
                            currentAsteroid = self.removeCurrentAsteroid(currentAsteroid)
                        elif currentAsteroid.previous.size == currentAsteroid.size:
                            currentAsteroid = self.removeBothAsteroids(currentAsteroid)
                            break
                    else:
                        currentAsteroid = currentAsteroid.next
                        break
            elif currentAsteroid.direction == "tail":
                break
        
        self.leftOver = []
        self.generateLeftOver(head.next)

        return self.leftOver
"""


# Stack Approach
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        floating = []
        incoming = []

        while asteroids:
            incoming.append(asteroids.pop())

        while incoming:
            incoming_asteroid = incoming[-1]
            if len(floating) == 0:
                floating.append(incoming_asteroid)
                incoming.pop()
            else:
                floating_asteroid = floating[-1]
                # Collide
                if floating_asteroid > 0 and incoming_asteroid < 0:
                    # Incoming asteroid gets destroyed
                    if abs(floating_asteroid) > abs(incoming_asteroid):
                        incoming.pop()
                    # Floating asteroid gets destroyed
                    elif abs(floating_asteroid) < abs(incoming_asteroid):
                        floating.pop()
                    # Both asteroids gets destroyed
                    elif abs(floating_asteroid) == abs(incoming_asteroid):
                        floating.pop()
                        incoming.pop()
                # Not Collide
                else:
                    floating.append(incoming_asteroid)
                    incoming.pop()

        return floating


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
