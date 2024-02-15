# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    APPROACH:
    find out where the split occurs
    if value of p and q > curr node val => p and q lies in right subtree
    if value of p and q < curr node val => p and q lies in left subtree
    if p and q lies in different subtrees, OR 
      (p or q) is the current node and other node lies in one of the subtrees:
          then current node is the lowest common ancestor
    TIME: O(N) for worst case, if balanced then log (N)
    SPACE: O(1), if recursion stack not considered
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p and q exists in different subtrees OR
        # (p or q) is the current node and other node lies in one of the subtrees:
        else: 
            return root
        
    '''
    same solution as above but Iterative 
    '''    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # TIME: O(n) for worst case, if balanced then log (n)
        # SPACE: O(1)
        curr = root

        # given that p and q will exist in tree
        while curr:
            
            # curr node is less than q and q, check in right subtree (containing larger values)
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # curr node is greater than q and q, check in left subtree (containing smaller values)
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left

            # split occurs (answer), or curr is one of inputs
            else:
                return curr
    