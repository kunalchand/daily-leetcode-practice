from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    Recursive approach:
    will start swap from leaf nodes and come back to root 
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # Base case: empty tree
            if not node: return

            left_node = dfs(node.left)
            right_node = dfs(node.right)
            
            node.left, node.right = right_node, left_node
            return node
            
        return dfs(root)

    '''
    Recursive approach:
    will start swap from leaf nodes and come back to root 
    same logic as above but no helper function
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root: return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root

    '''
    Iterative approach:
    will swap the child of current node first and then move down, doing the same
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # empty tree
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        
        