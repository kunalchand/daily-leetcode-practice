from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    APPROACH: calculate depth and diameter at every node and return them
    TIME: O(N)
    SPACE: O(1), O(N) if consider recursion stack
    uses the same concept as in https://leetcode.com/problems/maximum-depth-of-binary-tree/
    calculate diameter using left_depth + right_depth
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns (depth, diameter) 
        def dfs(node):
            if not node: return (0, 0)
            
            left_depth, left_diameter = dfs(node.left)
            right_depth, right_diameter = dfs(node.right)
            
            curr_diameter = left_depth + right_depth 

            # return depth and diameter, depth is used to calculate diameter
            return (max(left_depth, right_depth) + 1,
                    max(curr_diameter, left_diameter, right_diameter))

        depth, diameter = dfs(root)
        return diameter

    '''
    same as above, just uses the concept of nonlocal variable to update diameter
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        # return depth
        def dfs(node):
            nonlocal max_diameter
            if not node: return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            max_diameter = max(max_diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return max_diameter