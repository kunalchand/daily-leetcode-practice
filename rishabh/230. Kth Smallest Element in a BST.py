from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    APPROACH-1: in-order traversal, pick the kth element
    TIME: O(N)
    SPACE: O(N)
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def in_order_traversal(node):
            if not node: return
            in_order_traversal(node.left)
            res.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)        
        return res[k-1]         # pick the kth element by accessing k-1 idx


    '''
    APPROACH-2: do in-order traversal, and keep incrementing the count
    pick ans when count == k, return ans
    TIME: O(N)
    SPACE: O(N)
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = 0, None

        def in_order_traversal(node):
            nonlocal count
            nonlocal ans
            
            if not node: return -1

            in_order_traversal(node.left)
            count += 1
            if count == k: 
                ans = node.val
                return
            in_order_traversal(node.right)
            
            
        in_order_traversal(root)
        return ans