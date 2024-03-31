from typing import List

class Solution:
    '''
    I:
        +ve, and >= 1
        repeat? => yes
        target >= 1

    O:
        [1], t = 4 => Output = [  ] if no solution exist
        [1,1], t = 2 => output = [ [1,1] ]

    APPROACHES:
        Give TLE, repeated work
        1: 2 choices at every level,
             stop when sum goes beyond or find ans or idx goes beyond len
             remove duplicates by using a set while adding to final res
        
        Good backtracking approach, skips duplicates
        2: left skewed tree where from any point there are only branches forward
             skip duplicate branches, need to be sorted so that adjacent elements can be compared
             use a for loop and compare current and prev branch
    '''
    '''
    approach-1: complete binary tree with 2 choices at every node
    TLE at 172/176
    '''
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_path = []
        seen = set()

        def backtrack(idx, curr_sum):
            if curr_sum == target:
                if tuple(curr_path) not in seen:
                    seen.add(tuple(curr_path))
                    res.append(curr_path.copy())
                return

            if curr_sum > target or idx == len(nums):
                return

            curr_path.append(nums[idx])
            curr_sum += nums[idx]
            backtrack(idx + 1, curr_sum)                  # explore left branch, with curr_ele

            curr_path.pop()          
            curr_sum -= nums[idx]           
            backtrack(idx + 1, curr_sum)                  # explore right branch, without the curr_ele
           
        nums.sort()
        backtrack(0, 0)
        return res

    '''
    approach-2: left skewed, skip duplicate branches
    no need to use a set even
    '''
    # TLE 124/176 if curr_sum > target not included
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr_path = []
        
        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(curr_path[:])
                return

            if curr_sum > target:
                return

            for idx in range(start, len(nums)):
                # skip duplicate branch
                # make sure this isn't the first branch by checking idx > start
                if idx > start and nums[idx - 1] == nums[idx]:
                    continue
                
                curr_path.append(nums[idx])
                curr_sum += nums[idx]

                backtrack(idx + 1, curr_sum)

                curr_path.pop()
                curr_sum -= nums[idx]

        nums.sort()
        backtrack(0, 0)
        return res