from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipPreOrder(self, root, set_, ans, level) -> None:
        if root == None:
            return

        if level not in set_:
            ans.append(root.val)
            set_.add(level)

        self.flipPreOrder(root.right, set_, ans, level + 1)
        self.flipPreOrder(root.left, set_, ans, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.flipPreOrder(root, set(), ans, 0)
        return ans
