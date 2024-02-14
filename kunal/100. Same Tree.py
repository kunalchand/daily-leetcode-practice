from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        left_flag = self.isSameTree(p.left, q.left)
        right_flag = self.isSameTree(p.right, q.right)

        return left_flag and right_flag and p.val == q.val
