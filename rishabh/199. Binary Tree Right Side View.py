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
    APPROACH-1: BFS, exactly same as BFS implementation just
    pick the right most element at each level
    TIME: O(N)
    SPACE: O(N)
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
            res.append(curr_level[-1])          # pick the right most element at each level
        
        return res
    
    '''
    APPROACH-2: DFS
    do opposite of preorder traversal, use dfs
    add curr_node to res if curr-level not in visited (a set to keep track of visited levels)
    visit right child
    visit left child
    TIME: O(N)
    SPACE: O(N)
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visited = set()
        res = []
        
        def helper(node, level):
            if not node: return
            if level not in visited: 
                visited.add(level)
                res.append(node.val)
                
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        
        helper(root, 0)
        return res