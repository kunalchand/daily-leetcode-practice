from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root == None:
            return (0, 0)

        left_depth, left_diameter = self.DFS(root.left)
        right_depth, right_diameter = self.DFS(root.right)

        node_diameter = left_depth + right_depth

        return (
            1 + max(left_depth, right_depth),
            max(node_diameter, left_diameter, right_diameter),
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.DFS(root)
        return diameter
