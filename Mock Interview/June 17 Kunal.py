"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:


[-4, -1, 2, -2]
Set = {1, 2, 4}
1 , 2, 3, 4 (n)
ans
"""

# [-4, -1, 2, -2]
"""
def fun1(self, nums: List[int]) -> List[int]:
    ans = []

    for num in nums:
        index = abs(num) - 1
        # Flip
        nums[index] *= -1 if nums[index] > 0 else 1

    for index, num in enumerate(nums):
        if num > 0:
            ans.append(index + 1)

    return ans
"""


"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


"""

"""
def fun2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    else:
        # Compare Node Value
        if p.val != q.val:
            return False
        # Check if left node is missing
        elif (not p.left and q.left) or (p.left and not q.left):
            return False
        # Check if right node is missing
        elif (not p.right and q.right) or (p.right and not q.right):
            return False
        else:
            # Check left and then right
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""
