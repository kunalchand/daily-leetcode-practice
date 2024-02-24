import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Tweet:
    def __init__(self, userId: int, tweetId: int, time: int) -> None:
        self.userId = userId
        self.tweetId = tweetId
        self.time = time

    def __lt__(self, other):
        return self.time > other.time

    def __repr__(self):
        return (
            "(userId = "
            + str(self.userId)
            + ", tweetId = "
            + str(self.tweetId)
            + ", time = "
            + str(self.time)
            + ")"
        )


class Twitter:
    def handleExistance(self, customerId: int) -> None:
        if customerId not in self.database:
            self.database[customerId] = [list(), set()]

    def __init__(self):
        self.database = {}
        self.clock = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.handleExistance(userId)
        self.database[userId][0].append(Tweet(userId, tweetId, self.clock))
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []

        self.handleExistance(userId)
        maxHeap += self.database[userId][0]

        for followeeId in self.database[userId][1]:
            self.handleExistance(followeeId)
            maxHeap += self.database[followeeId][0]

        heapq.heapify(maxHeap)

        tweetList = []
        count = 0
        while maxHeap and count < 10:
            tweet = heapq.heappop(maxHeap)
            tweetList.append(tweet.tweetId)
            count += 1

        return tweetList

    def follow(self, followerId: int, followeeId: int) -> None:
        self.handleExistance(followerId)
        self.database[followerId][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.handleExistance(followerId)
        self.database[followerId][1].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
