from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time-O(n) Space-O(1) Validate Left and Right Sub-Tree
    """
    def getMaxMin(self, root: Optional[TreeNode]) -> Tuple[int, int, bool]:
        if root == None:
            return (float("-inf"), float("inf"), True)
        else:
            left_max, left_min, left_bool = self.getMaxMin(root.left)
            right_max, right_min, right_bool = self.getMaxMin(root.right)

            return (
                max(left_max, root.val, right_max),
                min(left_min, root.val, right_min),
                left_max < root.val < right_min and left_bool and right_bool,
            )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        root_max, root_min, root_bool = self.getMaxMin(root)
        return root_bool
    """

    # Time-O(n) Space-O(n) In-Order Traversal
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list_ = []

        def inOrderTraversal(root: Optional[TreeNode]) -> None:
            if root:
                inOrderTraversal(root.left)
                list_.append(root.val)
                inOrderTraversal(root.right)

        inOrderTraversal(root)

        for i in range(1, len(list_)):
            if list_[i] <= list_[i - 1]:
                return False

        return True
