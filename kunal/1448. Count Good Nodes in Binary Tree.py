from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findGoodNode(self, root: Optional[TreeNode], prev_max) -> int:
        if root == None:
            return 0
        else:
            if root.val >= prev_max:
                return (
                    1
                    + self.findGoodNode(root.left, root.val)
                    + self.findGoodNode(root.right, root.val)
                )
            else:
                return self.findGoodNode(root.left, prev_max) + self.findGoodNode(
                    root.right, prev_max
                )

    def goodNodes(self, root: TreeNode) -> int:
        return self.findGoodNode(root, float("-inf"))
