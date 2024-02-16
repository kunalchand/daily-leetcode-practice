from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time-O(n) Space-O(n) InOrder Traversal
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list_ = []

        def inOrderTraversal(root) -> None:
            if root:
                inOrderTraversal(root.left)
                list_.append(root.val)
                inOrderTraversal(root.right)

        inOrderTraversal(root)

        return list_[k-1]
    """

    # Time-O(k) Space-O(1) InOrder Traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inOrderTraversal(root) -> int:
            nonlocal count
            # nonlocal k

            if root:
                left_val = inOrderTraversal(root.left)
                count += 1
                if count == k:
                    return root.val
                right_val = inOrderTraversal(root.right)

                if left_val != -1:
                    return left_val
                elif right_val != -1:
                    return right_val
                else:
                    return -1
            else:
                return -1

        return inOrderTraversal(root)
