from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q != None) or (p != None and q == None):
            return False
        elif p == None and q == None:
            return True

        left_flag = self.checkTree(p.left, q.left)
        right_flag = self.checkTree(p.right, q.right)

        return left_flag and right_flag and p.val == q.val

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return self.checkTree(None, subRoot)

        node_flag = self.checkTree(root, subRoot)

        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True

        return node_flag
