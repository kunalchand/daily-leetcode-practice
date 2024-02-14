from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root == None:
            return (0, True)

        left_depth, left_flag = self.DFS(root.left)
        right_depth, right_flag = self.DFS(root.right)

        # node_flag = True if abs(right_depth - left_depth) <= 1 else False
        node_flag = abs(right_depth - left_depth) <= 1

        return (
            1 + max(left_depth, right_depth),
            node_flag and left_flag and right_flag,
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth, flag = self.DFS(root)
        return flag
