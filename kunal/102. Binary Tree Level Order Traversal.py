from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        queue = deque()

        queue.append((root, 0))

        current_level = 0
        current_list = []

        while queue:
            node, level = queue.popleft()

            if node:
                if current_level == level:
                    current_list.append(node.val)

                elif current_level < level:
                    ans.append(current_list)
                    current_level = level
                    current_list = []
                    current_list.append(node.val)

                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        if current_list != []:
            ans.append(current_list)

        return ans
