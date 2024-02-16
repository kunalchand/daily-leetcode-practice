from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        print(len(preorder), len(inorder))

        root_val = preorder[0]

        left_preorder = []
        right_preorder = []

        left_inorder = []
        right_inorder = []

        for val in inorder:
            if val != root_val:
                left_inorder.append(val)
            else:
                break

        left_preorder += preorder[1 : len(left_inorder) + 1]
        right_preorder += preorder[len(left_inorder) + 1 :]

        left_inorder = left_inorder[:]
        right_inorder += inorder[len(left_inorder) + 1 :]

        left = self.buildTree(left_preorder, left_inorder)
        right = self.buildTree(right_preorder, right_inorder)

        return TreeNode(root_val, left, right)
