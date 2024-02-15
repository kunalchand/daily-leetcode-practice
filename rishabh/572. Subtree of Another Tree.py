from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    APPROACH:
    uses this as a helper function: https://leetcode.com/problems/same-tree/description/
    check if sub_root is subtree of root:
        check if root and sub_root are same trees using is_same_tree()
        check if sub_root is subtree of left subtree 
        check if sub_root is subtree of right subtree 
    TIME: O( r * q )
    SPACE: O(1), not considering recursion stack
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


        if not root and subRoot: return False           # if first tree is empty and second isn't, can't be a subtree
        if root and not subRoot: return True            # null would be a subtree of any tree

        # both are non-empty
        if is_same_tree(root, subRoot): return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        