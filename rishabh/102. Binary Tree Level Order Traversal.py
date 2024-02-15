from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    APPROACH: BFS
    use a queue to store the elements at current level,
    start popping the elements and add their children to queue
    keep going until the queue is empty
    TIME: O(N)
    SPACE: O(N)
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res, Q = [], deque()
        Q.append(root)

        while Q:
            curr_level, Q_curr_len = [], len(Q)

            for _ in range(Q_curr_len):
                curr_node = Q.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left: Q.append(curr_node.left)
                if curr_node.right: Q.append(curr_node.right)
            
            res.append(curr_level)
        
        return res