"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered 
from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to 
the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.



Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
Example 2:


Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.


Constraints:

1 <= k <= n <= 500


Brute Foce: simulation using circular linked list / queue
    Space-O(n) Time-O(k * n)

    [5 6 7 8 1 2 3] n - k

    start [] end

    [1 2 3 4 5] n=5 k=2
        5-2 = 3
    [3 4 5 1 2]
    [3 4 5 1] n=4 k=2
        4-2 = 2
    [5 1 3 4]
    [5 1 3] n=3 k=2
        3-2 = 1
    [3 5 1]
    [3 5] n=2 k=2
        2-2=0
    [3]

     # Edge Case
     [1, 2, 3, 4, 5]
     4 5 1 2 3
     4 5 1 2
     2 4 5 1
     2 4 5 n=3 k=3
     2 4 n = 2 k = 3

    # Edge Case 2
    1 2 3 4 5 6   n=6 k=4 n-k=2
    6 1 2 3 4 5
    5 6 1 2 3 4   
    5 6 1 2 3  n=5 k=4 n-k=1
    3 5 6 1 2
    3 5 6 1 n=4 k=4 n-k=0
    3 5 6 n=3 k=4 n-k=-1
    5 6 3
    5 6 n=2 k=4 n-k=-2
    5

    1 2 3 4 5 6 n=6 k=4
    2 3 4 5 6 1 
    3 4 5 6 1 2
    4 5 6 1 2 3
      5 6 1 2 3 n=5 k=4
      6 1 2 3 5
      1 2 3 5 6
      2 3 5 6 1
        3 5 6 1 n=4 k=4
        3 5 6 1
          5 6 1 n=3 k=4
          1 6 5
          5 6 1


"""

from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        # left [] right

        # Generate Queue
        for personIndex in range(n, 0, -1):
            queue.appendleft(personIndex)

        while len(queue) > 1:
            # Rotate the queue n-k times
            for _ in range(len(queue) - k + 1):
                person = queue.pop()
                queue.appendleft(person)

            # Remove the kth element
            queue.pop()

        return queue[-1]
