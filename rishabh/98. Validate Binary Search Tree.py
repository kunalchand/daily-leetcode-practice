from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    APPROACH-1: 
    split at every node and call the valid function for children
    update left and right boundaries accordingly
    TIME: O(N)
    SPACE: O(1), if recursion stack not considered
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_validity(node, left, right) -> bool:
            if not node: return True

            # if bst condition is invalid
            if not (left < node.val < right): return False

            # else bst condition is valid till now
            # check for child nodes/subtrees
            is_left_valid = check_validity(node.left, left, node.val)
            is_right_valid = check_validity(node.right, node.val, right)
            return is_left_valid and is_right_valid
        
        return check_validity(root, float("-inf"), float("inf"))
        
    '''
    APPROACH-2: 
    starts bottom-up
    check if a subtree is a valid bst by checking
    if its left and right subtrees are valid bst
    returning min and max value from each subtree
    TIME: O(N)
    SPACE: O(1), if recursion stack not considered
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # returns if a tree till this node is a 
        # (valid bst, min_val in this bst, max_val in this bst)
        def dfs(node) -> Tuple[bool, int, int]:
            if not node: return (True, float('inf'), float('-inf'))
            
            left_valid_bst, left_min_val, left_max_val = dfs(node.left)
            right_valid_bst, right_min_val, right_max_val = dfs(node.right)

            valid_bst = left_max_val < node.val < right_min_val
            max_val = max(left_max_val, node.val, right_max_val)
            min_val = min(left_min_val, node.val, right_min_val)

            return (valid_bst and left_valid_bst and right_valid_bst, 
                    min_val, max_val)

        # pick the first value of tuple
        return dfs(root)[0]
        