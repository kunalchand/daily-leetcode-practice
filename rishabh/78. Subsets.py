from typing import List

class Solution:
    '''
    APPROACH-1: BACKTRACKING at every step of recursion, 
    decide to choose or to not choose the current nums[i]
    you have 2 choices at every node of the decision tree
    TIME: O(N * 2 ^ N)
    SPACE: O(N), subset can atmost store N element, ignoring output array powerset
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
    APPROACH-2: (BACKTRACKING) same as approach-1
    coded a lil different
    TIME: O(N * 2 ^ N)
    SPACE: O(N), subset can atmost store N element, ignoring output array powerset
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
    
    '''
    APPROACH-3: RECURSION
    using base and addon list
    at every iteration, expand base and shrink addon
    TIME: O(N * 2 ^ N)
    SPACE: no extra space, but recursion stack
    '''
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        def helper(base: List[int], addon: List[int]) -> None:
            for idx, n in enumerate(addon):
                new_base = base[:] + [n]
                power_set.append(new_base)
                helper(new_base, addon[idx + 1:])

        power_set = []
        power_set.append([])                     # for subset of size 0
        for n in nums: power_set.append([n])     # for subsets of size 1
        
        for idx, n in enumerate(nums):           # for subsets of size 2 or more
            helper([n], nums[idx + 1 : ])
        return power_set
    

print(Solution().subsets3([1,2,3]))