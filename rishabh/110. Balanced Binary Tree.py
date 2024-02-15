from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    APPROACH: calculate depth at left and right subtree
    if the difference is more than one return false
    keep doing this for every node of the tree
    TIME: O(N)
    SPACE: O(1)
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        '''
        :type node: TreeNode
        :rtype: int: max depth/height of tree till this node
        '''
        def calculate_depth(node) -> int:
            nonlocal balanced
            if not node: return 0

            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)

            # if difference btw heights of left and right subtree is 
            # greater than 1 => trees are not balanced
            if abs(left_depth - right_depth) > 1:
                balanced = False

            return 1 + max(left_depth, right_depth)
        
        calculate_depth(root)
        return balanced