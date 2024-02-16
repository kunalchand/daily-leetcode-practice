# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    APPROACH: recursion, find mid (idx of root) and divide arrays to make left and right children
    TIME: O(N)
    SPACE: O(N)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])        # mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])          # make left subtree
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])      # make right subtree
        return root

    '''
    same logic but cleaner
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])

            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root