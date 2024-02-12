from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    APPROACH-1: Recursion
    calculate the depth at leaf nodes first
    and keep adding/returning that root node 
    TIME: O(N)
    SPACE: O(1), O(N) if consider recursion stack
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    '''
    APPROACH-2: Iterative + Recursion
    count the depth at current node first
    keep increasing the count until reach the leaf node
    while returning, return whatever the max depth is from the left and right subtree
    TIME: O(N)
    SPACE: O(1), O(N) if consider recursion stack
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count_nodes(node, node_count):
            if not node: return 0 

            # increase node_count as soon as encounter a node
            node_count += 1

            # return node_count when encounter leaf node
            if not node.left and not node.right: return node_count

            # calculate node_count for left and right subtrees
            return max(count_nodes(node.left, node_count),
                        count_nodes(node.right, node_count))
        
        return count_nodes(root, 0)

