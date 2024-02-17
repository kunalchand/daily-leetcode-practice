from typing import List

class Solution:
    '''
    APPROACH-1: at every step of recursion, 
    decide to choose or to not choose the current nums[i]
    you have 2 choices at every node of the decision tree
    TIME: O(N * 2 ^ N)
    SPACE: no extra space, but recursion stack
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, subset):
            
            # base case
            if idx == len(nums):
                power_set.append(subset.copy())
                return

            helper(idx + 1, subset)             # don't choose nums[i]

            subset.append(nums[idx])            # choose nums[i]
            helper(idx + 1, subset)
            subset.pop()
        
        power_set = []
        helper(0, [])
        return power_set

    '''
    APPROACH-2: same as approach-1
    coded a lil different
    TIME: O(N * 2 ^ N)
    SPACE: no extra space, but recursion stack
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set, subset = [], []

        def dfs(idx):
            if idx == len(nums):
                power_set.append(subset.copy())
                return

            subset.append(nums[idx])        # include nums[i]
            dfs(idx + 1)

            subset.pop()                    # not include nums[i]
            dfs(idx + 1)

        dfs(0)
        return power_set