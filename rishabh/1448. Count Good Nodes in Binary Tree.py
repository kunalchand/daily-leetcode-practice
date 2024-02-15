# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    APPROACH: run a dfs and increment count for every good node
    check if the curr node is good node if its val > max_val till now
    TIME: O(N)
    SPACE: O(1), if recursion stack is not considered
    '''
    def goodNodes(self, root: TreeNode) -> int:
        count, max_val = 0, float('-inf')

        # this doesn't return anything
        # its purpose is to traverse the tree and 
        # increment count for every good node encountered
        def dfs(node, max_val):
            nonlocal count
            if not node: return 

            # update count and max val
            if node.val >= max_val:         
                count += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, max_val)
        return count